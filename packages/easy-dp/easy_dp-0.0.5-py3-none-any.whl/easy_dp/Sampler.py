from typing import List

import torch
from torch.utils.data import Sampler

class DistributedPoissonSampler(Sampler):
    '''
    Distributed Poisson sampler. This is a distributed version of the Poisson sampler which selects a variable number of samples per batch (instead of a fixed number of samples per batch).
    Each batch is constructed by selecting a sample with prob sample_rate.
    The Distributed version works by assigning a subset of the dataset to each replica, and then selecting a batch with Poisson subsampling.
    So, each gpu can have a different number of samples in the batch, but the number of batches is the same.
    '''
    def __init__(self, len_dataset: int, sample_rate: float, rank: int, shuffle: bool = True, shuffle_seed: int = 42):

        self.len_dataset = len_dataset
        self.sample_rate = sample_rate
        self.rank = rank
        self.epoch = 0
        self.shuffle = shuffle
        self.shuffle_seed = shuffle_seed
        self.world_size = torch.distributed.get_world_size()
        self.generator = torch.Generator()

        self.num_samples_per_device = self.len_dataset // self.world_size
        if self.rank < self.len_dataset % self.world_size:
            # The first replicas get an extra datapoint if necessary (balanced)
            self.num_samples_per_device += 1

        # Number of batches: same as non-distributed Poisson sampling, but each batch is smaller
        self.num_batches = int(1 / self.sample_rate)

    def __iter__(self):
        if self.shuffle:
            # deterministically shuffle based on epoch and seed
            g = torch.Generator()
            g.manual_seed(self.shuffle_seed + self.epoch)
            indices = torch.randperm(self.len_dataset, generator=g)
        else:
            indices = torch.arange(self.len_dataset)

        # Subset of the dataset assigned to this replica
        # (Different from the regular distributed loader that pads with more samples)
        indices = indices[self.rank : self.len_dataset : self.world_size]
        assert len(indices) == self.num_samples_per_device, f"len(indices) = {len(indices)} != {self.num_samples_per_device} = num_samples_per_device"

        # Now, select a batch with Poisson subsampling
        for _ in range(self.num_batches):
            mask = (
                torch.rand(self.num_samples_per_device, generator=self.generator)
                < self.sample_rate
            )
            selected_examples = mask.nonzero(as_tuple=False).reshape(-1)
            if len(selected_examples) > 0:
                yield indices[selected_examples]

    def __len__(self) -> int:
        """
        Expected number of batches.
        """
        return self.num_batches

    def set_epoch(self, epoch: int) -> None:
        """
        Sets the epoch for this sampler. When :attr:`shuffle=True`, this ensures all replicas
        use a different random ordering for each epoch. Otherwise, the next iteration of this
        sampler will yield the same ordering.
        Args:
            epoch (int): Epoch number.
        """
        self.epoch = epoch
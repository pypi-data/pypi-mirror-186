from . import accounting_manager
import torch

class PrivacyEngine:
    '''
    This class is used to compute the amount of noise to add to the gradients in order to satisfy the privacy budget.
    For now we only support the rdp accountant.
    '''
    def __init__(self, len_dataset: int, batch_size: int, max_grad_norm: float, num_epochs: int, target_epsilon: float, target_delta: float):
        '''
        Parameters:
            len_dataset: The number of samples in the dataset.
            batch_size: The batch size used for training.
            max_grad_norm: The maximum norm of the gradients.
            num_epochs: The number of epochs to train for.
            target_epsilon: The target epsilon value.
            target_delta: The target delta value.
        '''
        self.len_dataset = len_dataset
        self.batch_size = batch_size
        self.max_grad_norm = max_grad_norm
        self.num_epochs = num_epochs
        self.target_epsilon = target_epsilon
        self.target_delta = target_delta
        self.steps_per_epoch = len_dataset // batch_size
        self.total_steps = self.steps_per_epoch * num_epochs

        self.sample_rate = self.batch_size / self.len_dataset

        # Needed for rdp accountant
        self.alphas = accounting_manager.DEFAULT_ALPHAS

        self.manager = accounting_manager.RDPManager(alphas=self.alphas)
        self.noise_multiplier = self.manager.compute_sigma(
            target_epsilon=target_epsilon,
            target_delta=target_delta,
            sample_rate=self.sample_rate,
            epochs=self.num_epochs,
        )
        print(f"PrivacyEngine: noise_multiplier = {self.noise_multiplier}")

    def add_noise(self, grad):
        '''
        Injects noise to the gradient.
        Parameters:
            grad: The gradient of a single sample.
        Returns:
            The gradient with noise added.
        '''
        noise = torch.normal(
            mean=0.0,
            std=self.noise_multiplier * self.max_grad_norm,
            size=grad.shape,
            device=grad.device,
            dtype=grad.dtype,
        )
        return grad + noise

    def clip_gradient(self, grad):
        '''
        Clips the gradient to the maximum norm. Modify the gradient in place.
        Parameters:
            grad: The gradient of a single sample.
        '''
        torch.nn.utils.clip_grad_norm_(grad, self.max_grad_norm)
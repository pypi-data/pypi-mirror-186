import torch
from torch.utils.data import Dataset, random_split
import pandas as pd
from typing import List, Tuple

class TextDataset(Dataset):
    def __init__(self, texts: List[str], tokenizer, max_seq_len: int):
        self.input_ids = []
        self.attn_masks = []
        for txt in texts:
            # Add <sos> token
            txt = "<sos>" + txt
            encodings_dict = tokenizer(
                txt, truncation=True, max_length=max_seq_len, padding="max_length")
            self.input_ids.append(torch.tensor(encodings_dict['input_ids']))
            self.attn_masks.append(torch.tensor(
                encodings_dict['attention_mask']))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attn_masks[idx]

def get_dataset(tokenizer, dataset_file_name: str, max_seq_len: int, return_eval=True, seed=42, test_subset=False) -> Tuple[TextDataset, TextDataset]:
    # Read the data
    df = pd.read_csv(dataset_file_name, sep='\t')
    texts = df['text'].tolist()
    if test_subset:
        print("Using subset: limiting to 100 samples")
        texts = texts[:100]

    dataset = TextDataset(texts, tokenizer, max_seq_len=max_seq_len)

    train_size = int(0.8 * len(dataset))
    train_dataset, val_dataset = random_split(dataset, [train_size, len(
        dataset) - train_size], generator=torch.Generator().manual_seed(seed))

    if return_eval:
        return train_dataset, val_dataset
    else:
        return train_dataset
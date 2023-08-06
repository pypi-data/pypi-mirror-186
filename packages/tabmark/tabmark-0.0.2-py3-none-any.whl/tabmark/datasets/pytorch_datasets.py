import torch
from torch.utils.data import Dataset as pt_Dataset
from torch.utils.data import TensorDataset

from tabmark.datasets import DatasetConverter

class TorchDataset(pt_Dataset, DatasetConverter):
    def __init__(self, dataset, dtype_X=torch.float, dtype_y=torch.long):
        self.X = torch.from_numpy(dataset.X.to_numpy()).to(dtype_X)
        self.y = torch.from_numpy(dataset.y.values).to(dtype_y)
        self.columns = dataset.X.columns

    def split(self, percentages, return_datasets=False, shuffle=True, random_state=None):
        tensors = super().split(percentages, shuffle=shuffle, random_state=random_state)
        if return_datasets:
            Xs = tensors[:len(tensors)//2]
            ys = tensors[len(tensors)//2:]
            ds_list = [TensorDataset(_x, _y) for _x, _y in zip(Xs, ys)]
            return tuple(ds_list)
        else:
            return tensors

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

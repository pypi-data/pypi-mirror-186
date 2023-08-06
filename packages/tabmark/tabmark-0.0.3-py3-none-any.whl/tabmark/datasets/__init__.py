from .datasets import NumpyDataset, Dataset, DatasetConverter, Heloc, Adult, Higgs, list_of_datasets

try:
    from .pytorch_datasets import TorchDataset
except ImportError as e:
    import warnings
    print(e)
    warnings.warn('PyTorch not installed. Some methods are unavailable')
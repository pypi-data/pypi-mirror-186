import numpy as np

from sklearn.datasets import fetch_openml

from tabmark.utils import to_random_state

list_of_datasets = [
    {'name': 'higgs', 'version': 2, 'type': 'classification' },
    {'name': 'heloc', 'version': 2, 'type': 'classification' },
    {'name': 'adult', 'version': 2, 'type': 'classification' },
]

class Dataset:

    def __init__(self, name, version, preprocessing=True):
        self.name = name
        self.version = version
        self.X, self.y = fetch_openml(name, version=version, return_X_y=True)

        self.rename_y()

        if preprocessing:
            self.preprocessing()

    # If the labels are not ascending from 0 or are strings, renumber them
    def rename_y(self):
        pass

    def preprocessing(self):
        pass

    # Remove rows with at least one NaN
    def remove_nan_rows(self):
        nan_row_indices = self.X.isna().any(axis=1)
        self.X = self.X[~nan_row_indices]
        self.y = self.y[~nan_row_indices]

    def remove_columns(self, columns):
        self.X.drop(columns=columns, inplace=True)

    def normalize_zero_mean(self, columns):
        relevant_data = self.X[columns]
        relevant_data = (relevant_data - relevant_data.mean()) / relevant_data.std()
        self.X[columns] = relevant_data

class Higgs(Dataset):

    def __init__(self):
        super().__init__('higgs', 2)

    def preprocessing(self):
        self.remove_nan_rows()
        self.normalize_zero_mean(self.X.columns)

    def rename_y(self):
        self.y = self.y.astype(int)

class Adult(Dataset):

    def __init__(self, remove_country=True, remove_nan=False):
        self.remove_country = remove_country
        self.remove_nan = remove_nan
        super().__init__('adult', 2)

    def preprocessing(self):
        if self.remove_country:
            self.remove_columns(['native-country'])
        if self.remove_nan:
            self.remove_nan_rows()

        # TODO: Normalizing numeric values?

    def rename_y(self):
        self.y = self.y.map({ '<=50K': 0, '>50K': 1 })

class Heloc(Dataset):

    def __init__(self):
        super().__init__('heloc', 2)

    def preprocessing(self):
        self.remove_nan_rows()
        self.normalize_zero_mean(self.X.columns)

    def rename_y(self):
        self.y = self.y.astype(int)

class DatasetConverter:
    # Get indices for split of dataset based on percentage
    def _split_indices(self, percentages, n_samples):
        split_sizes = [int(p * n_samples) for p in percentages]
        
        # Calculate the split points
        split_points = [0] + [sum(split_sizes[:i-1]) for i in range(2, len(percentages)+1)] + [n_samples]
        split_indices = list(zip(split_points[:-1], split_points[1:]))

        return split_indices

    def split(self, percentages, shuffle=True, subset_size=None, random_state=None):
        rng = to_random_state(random_state)

        # Shuffle
        n_samples = len(self.X)
        if shuffle:
            indices = rng.choice(n_samples, size=n_samples, replace=False)
        else:
            indices = np.arange(n_samples)
        _X = self.X[indices]
        _y = self.y[indices]

        # Make dataset smaller if percentage of subset size is given
        if subset_size is not None:
            subset_size_int = int(subset_size * n_samples)
            _X = _X[:subset_size_int]
            _y = _y[:subset_size_int]

        n_samples = len(_X)

        # Split
        split_indices = self._split_indices(percentages, n_samples)
        return tuple([_X[start:stop] for (start, stop) in split_indices] + [_y[start:stop] for (start, stop) in split_indices])

class NumpyDataset(DatasetConverter):

    def __init__(self, dataset):
        self.X = dataset.X.to_numpy()
        self.y = dataset.y.values
        self.columns = dataset.X.columns
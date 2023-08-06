import numpy as np
import pandas as pd
import torch

from .validation import check_is_finite


class PandasToTensorConverter:

    def __init__(self, check_finite=True):
        self.check_finite = check_finite

    def convert(self, X, names, dtype):
        converters = {
            'float': self._to_float,
            'long': self._to_long
        }

        tensor = converters[dtype](X[names])
        if self.check_finite:
            return check_is_finite(tensor, names)
        return tensor

    def _to_float(self, X):
        return torch.tensor(X.to_numpy(np.float), dtype=torch.float)

    def _to_long(self, X):
        return torch.tensor(X.to_numpy(np.long), dtype=torch.long)


def series_to_2d(series):
    return series.values.reshape(-1, 1)


def numpy_2d_to_pandas(arrays, columns=None, dtypes=None):
    """Converts collection of 2-D numpy arrays to a single pandas DataFrame.

    Parameters
    ----------
    arrays : list of 2-D numpy arrays

    columns : array-like, default=None
        Column labels to use for resulting frame when data does not have them,
        defaulting to RangeIndex(0, 1, 2, …, n).

    dtypes : data type, or dict of column name -> data type, default=None

    Returns
    -------
    pandas_df : pd.DataFrame
    """
    pandas_df = pd.DataFrame(np.vstack(arrays), columns=columns)
    if dtypes is not None:
        return pandas_df.astype(dtype=dtypes)
    return pandas_df

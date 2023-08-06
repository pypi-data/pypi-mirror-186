from collections import Sequence

import numpy as np
import pandas as pd
from torch.utils.data import Dataset


class SliceDataset(Sequence, Dataset):
    """Makes Dataset sliceable.

    Helper class that wraps a torch dataset to make it work with
    sklearn. That is, sometime sklearn will touch the input data, e.g. when
    splitting the data for a grid search. This will fail when the input data is
    a torch dataset. To prevent this, use this wrapper class for your
    dataset.

    ``dataset`` attributes are also available from :class:`SliceDataset`
    object (see Examples section).

    Parameters
    ----------
    dataset : torch.utils.data.Dataset
      A valid torch dataset.

    indices : list, np.ndarray, or None (default=None)
      If you only want to return a subset of the dataset, indicate
      which subset that is by passing this argument. Typically, this
      can be left to be None, which returns all the data.

    Examples
    --------
    >>> X = MyCustomDataset()
    >>> search = GridSearchCV(net, params, ...)
    >>> search.fit(X, y)  # raises error
    >>> ds = SliceDataset(X)
    >>> search.fit(ds, y)  # works
    >>> ds.a  # returns 1 since ``X`` attributes are also available from ``ds``

    Notes
    -----
    This class will only return the X value by default (i.e. the
    first value returned by indexing the original dataset). Sklearn,
    and hence skorch, always require 2 values, X and y. Therefore, you
    still need to provide the y data separately.

    This class behaves similarly to a PyTorch
    :class:`~torch.utils.data.Subset` when it is indexed by a slice or
    numpy array: It will return another ``SliceDataset`` that
    references the subset instead of the actual values. Only when it
    is indexed by an int does it return the actual values. The reason
    for this is to avoid loading all data into memory when sklearn,
    for instance, creates a train/validation split on the
    dataset. Data will only be loaded in batches during the fit loop.
    """

    def __init__(self, dataset, indices=None):
        self.dataset = dataset
        self.indices = indices
        self.indices_ = (
            self.indices if self.indices is not None
            else np.arange(len(self.dataset))
        )
        self.ndim = 1

    @property
    def shape(self):
        return len(self)

    def transform(self, data):
        """Additional transformations on ``data``.

        Notes
        -----
        If you use this in conjunction with PyTorch
        :class:`~torch.utils.data.DataLoader`, the latter will call
        the dataset for each row separately, which means that the
        incoming ``data`` is a single rows.

        """
        return data

    def __getattr__(self, attr):
        """If attr is not in self, look in self.dataset.

        Notes
        -----
        Issues with serialization were solved with the following discussion:
        https://stackoverflow.com/questions/49380224/how-to-make-classes-with-getattr-pickable
        """
        if 'dataset' not in vars(self):
            raise AttributeError
        return getattr(self.dataset, attr)

    def __len__(self):
        return len(self.indices_)

    def __getitem__(self, i):
        if isinstance(i, (int, np.integer)):
            Xn = self.dataset[self.indices_[i]]
            return self.transform(Xn)
        if isinstance(i, slice):
            return SliceDataset(self.dataset, indices=self.indices_[i])
        if isinstance(i, np.ndarray):
            if i.ndim != 1:
                raise IndexError(
                    "SliceDataset only supports slicing with 1 "
                    "dimensional arrays, got {} dimensions "
                    "instead".format(i.ndim)
                )
            if i.dtype == np.bool:
                i = np.flatnonzero(i)
        return SliceDataset(self.dataset, indices=self.indices_[i])


def safe_math_eval(string):
    """Evaluates simple math expression

    Since built-in eval is dangerous, this function limits the possible
    characters to evaluate.

    Parameters
    ----------
    string : str

    Returns
    -------
    evaluated ``string`` : float
    """
    allowed_chars = "0123456789+-*(). /"
    for char in string:
        if char not in allowed_chars:
            raise ValueError("Unsafe eval character: {}".format(char))
    return eval(string, {"__builtins__": None}, {})


def loc_group(X, group_ids, id):
    """Auxiliary for locating rows in dataframes with one or multiple group_ids.

    Parameters
    ----------
    X : pd.DataFrame
        Dataframe to filter.

    group_ids: tuple
        Tuple of columns names.

    id : tuple
        Id of the wanted group.

    Returns
    -------
    pd.DataFrame
    """
    # Broadcasted numpy comparison
    return X[(X[group_ids].values == id).all(1)].copy()


def empty_ndarray(shape):
    """Private function that returns empty numpy array of desired shape.
    """
    return np.ndarray(shape=shape)


def hstack(arrays, cast_to_object=True):
    """Private function for horizontally stacking numpy arrays.

    Parameters
    ----------
    arrays : sequence of ndarrays
        The arrays must have the same shape along all but the second axis,
        except 1-D arrays which can be any length.

    cast_to_object : bool, default=True
        If ``np.stack`` raises TypeError, converts all arrays to object
        dtype and tries again.

    Returns
    -------
    stacked : ndarray
        The array formed by stacking the given arrays.
    """
    try:
        return np.hstack(arrays)
    except TypeError as e:
        if cast_to_object:
            obj_arrays = [arr.astype(object) for arr in arrays]
            return np.hstack(obj_arrays)
        raise e

import pandas as pd
import torch
from pandas.api.types import is_datetime64_any_dtype
from pytorch_forecasting.data import timeseries


def check_is_finite(tensor, names):
    """Checks if 2D tensor contains NAs or infinite values.

    Parameters
    ----------
    tensor : torch.Tensor
        Tensor to check

    names : Union[str, List[str]]
        Name(s) of column(s) (used for error messages)

    Returns
    -------
    torch.Tensor: returns tensor if checks yield no issues
    """
    return timeseries.check_for_nonfinite(tensor, names)


def check_group_id_presence(X, group_ids, group_id):
    """Checks passed `group_id` exists.
    """
    all_groups = list(X.groupby(group_ids).groups)
    if group_id not in all_groups:
        raise ValueError(f'Group id {group_id} does not exist.')


def check_is_datetime(X):
    """Checks if passed pandas `series` is datetime64 compatible.
    """
    if not is_datetime64_any_dtype(X):
        raise ValueError('Series is not datetime64 compatible.')


def check_pandas(X, series_or_dataframe, transformer):
    pandas_types = {
        'series': pd.Series,
        'dataframe': pd.DataFrame
    }
    pandas_type_to_check = pandas_types[series_or_dataframe]
    if not isinstance(X, pandas_type_to_check):
        fmt = "Transformer {transformer} only accepts {correct_type}. " \
              "Instead got {wrong_type}"
        fmt_kwargs = {
            'transformer': transformer.__class__.__name__,
            'correct_type': pandas_type_to_check,
            'wrong_type': type(X)
        }
        raise TypeError(fmt.format(**fmt_kwargs))


def check_group_ids(X, group_ids):
    """Checks `group_ids` columns are present in `X`.
    """
    msg = 'group_id column {} not found in X.'
    for col in group_ids:
        if col not in X:
            raise ValueError(msg.format(col))

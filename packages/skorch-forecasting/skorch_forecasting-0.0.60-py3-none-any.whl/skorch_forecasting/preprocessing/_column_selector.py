import pandas as pd
from sklearn.compose import make_column_selector


class ColumnSelector(make_column_selector):
    """Creates a callable to select columns to be used with
    :class:`ColumnTransformer`.

    :class:`ColumnSelector` extends the implementation of the
    :class:`make_column_selector` from sklearn by adding both
    ``pattern_include`` and ``pattern_exclude`` params.


    Parameters
    ----------
    pattern_include : str or list, default=None
        A selection of columns to include.

        - If None, column selection will not be performed based on this param.
        - If list, the elements will be joined using the regex '|' operator.
            Columns matching the resulting regex will be selected
        - if str, the pattern is used as regex and columns matching will
            be selected

    pattern_exclude : str or list, default=None
        A selection of columns to exclude.

        - If None, column selection will not be performed based on this param.
        - If list, the elements will be joined using the regex '|' operator.
            Columns matching the resulting regex will be omitted from
            selection.
        - If str, the pattern is used as regex and columns matching will be
            omitted from selection.

    dtype_include : column dtype or list of column dtypes, default=None
        A selection of dtypes to include.

    dtype_exclude : column dtype or list of column dtypes, default=None
        A selection of dtypes to exclude.

    Returns
    -------
    selector : callable
        Callable for column selection to be used by a
        :class:`ColumnTransformer`.
    """

    def __init__(self, pattern_include=None, pattern_exclude=None,
                 dtype_include=None, dtype_exclude=None):
        super().__init__(
            pattern=self._to_regex(pattern_include),
            dtype_include=dtype_include,
            dtype_exclude=dtype_exclude
        )
        self.pattern_exclude = self._to_regex(pattern_exclude)

    def __call__(self, X):
        cols = pd.Series(super().__call__(X))
        if self.pattern_exclude is not None and not cols.empty:
            cols = pd.Series(cols)
            cols = cols[-cols.str.contains(self.pattern_exclude, regex=True)]
            return cols.tolist()
        return cols.tolist()

    def _to_regex(self, x, join_with='|'):
        if isinstance(x, list):
            return join_with.join(x)
        return x

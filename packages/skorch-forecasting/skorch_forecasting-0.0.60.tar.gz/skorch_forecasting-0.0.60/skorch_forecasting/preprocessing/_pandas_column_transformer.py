from itertools import chain

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import make_column_transformer
from sklearn.compose._column_transformer import (
    _is_empty_column_selection,
    _check_feature_names_in
)
from sklearn.utils.validation import check_is_fitted

from ..exceptions import InverseTransformFeaturesError
from ..utils.data import loc_group, hstack, empty_ndarray
from ..utils.validation import check_group_ids


def _make_column_transformer(
        transformers,
        sparse_threshold=0,
        remainder="passthrough",
):
    """Private function for instantiating a sklearn :class:`ColumnTransformer`.
    """
    return make_column_transformer(
        *transformers,
        sparse_threshold=sparse_threshold,
        remainder=remainder,
        verbose_feature_names_out=False
    )


class PandasColumnTransformer(BaseEstimator, TransformerMixin):
    """Pandas wrapper for sklearn :class:`ColumnTransformer`.

    This wrapper returns pandas DataFrames instead of numpy arrays in
    transform and inverse_transform methods.

    Parameters
    ----------
     *transformers : tuples
        Tuples of the form (transformer, columns) specifying the
        transformer objects to be applied to subsets of the data.

        transformer : {'drop', 'passthrough'} or estimator
            Estimator must support :term:`fit` and :term:`transform`.
            Special-cased strings 'drop' and 'passthrough' are accepted as
            well, to indicate to drop the columns or to pass them through
            untransformed, respectively.
        columns : str,  array-like of str, int, array-like of int, slice, \
                array-like of bool or callable
            Indexes the data on its second axis. Integers are interpreted as
            positional columns, while strings can reference DataFrame columns
            by name. A scalar string or int should be used where
            ``transformer`` expects X to be a 1d array-like (vector),
            otherwise a 2d array will be passed to the transformer.
            A callable is passed the input data `X` and can return any of the
            above. To select multiple columns by name or dtype, you can use
            :obj:`make_column_selector`.

    Attributes
    ----------
    column_transformer_ : sklearn :class:`ColumnTransformer` object
    """

    def __init__(self, transformers):
        self.transformers = transformers

    def fit(self, X, y=None):
        column_transformer = _make_column_transformer(self.transformers)
        column_transformer.fit(X)
        self._set_attributes(X, column_transformer)
        return self

    def _set_attributes(self, X, column_transformer):
        self.feature_dtypes_in_ = X.dtypes.to_dict()
        self.feature_names_in_ = column_transformer.feature_names_in_
        self.column_transformer_ = column_transformer

    def transform(self, X):
        """Transform X separately by each transformer and concatenate results
        in a single pandas DataFrame.

        Parameters
        ----------
        X : pd.DataFrame
            DataFrame to be transformed by subsets.

        Returns
        -------
        X_out : pd.DataFrame
        """
        arr = self.column_transformer_.transform(X)
        columns = self.get_feature_names_out()
        dtypes = self.get_feature_dtypes_out()
        return pd.DataFrame(arr, columns=columns).astype(dtypes)

    def inverse_transform(self, X):
        """Inverse transforms X separately by each transformer and concatenate
        results in a single pandas DataFrame.

        Transformed columns whose corresponding transformer does not have
        implemented an :meth:`inverse_transform` method will not appear
        after calling this inverse transformation. Hence, it is possible the
        resulting DataFrame ``X_out``  is not equal to the original X, that
        is, the expression X = f-1(f(X)) wont be satisfied.


        Parameters
        ----------
        X : pd.DataFrame
            DataFrame to be inverse transformed by subsets

        Returns
        -------
        X_out : pd.DataFrame
        """
        check_is_fitted(self)
        inverse_transformer = PandasInverseTransformer(self)
        return inverse_transformer.inverse_transform(X)

    def get_feature_names_out(self, input_features=None):
        """Get output feature names for transformation.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        """
        return self.column_transformer_.get_feature_names_out(input_features)

    def get_feature_dtypes_out(self):
        """Get feature dtypes from all transformers.

        Returns
        -------
        feature_dtypes : dict, str -> dtype
        """
        dtypes_out = {}
        for name, trans, column, _ in self.iter():
            trans_dtype_out = self._get_feature_dtype_out_for_transformer(
                name, trans, column)
            dtypes_out.update(trans_dtype_out)

        return dtypes_out

    def iter(self, fitted=True, replace_strings=False, column_as_strings=True):
        """Generate (name, trans, column, weight) tuples.


        Notes
        -----
        This is an interface for private method :meth:`_iter` of a sklearn
        :class:`ColumnTransformer` instance.

        Parameters
        ----------
        fitted : bool, default=True
            If True, use the fitted transformers, else use the
            user specified transformers updated with converted column names
            and potentially appended with transformer for remainder.

        replace_strings : bool, default=False
            If True, string transformers are replaced with a identity
            transformer through a :class:`FunctionTransformer` instance.

        column_as_strings : bool, default=True
            If True, columns are yielded with their name. Else, with their
            index position.

        Yields
        ------
        (name, trans, column, weight) tuples
        """
        return self.column_transformer_._iter(
            fitted=fitted, replace_strings=replace_strings,
            column_as_strings=column_as_strings)

    def get_feature_name_out_for_transformer(
            self, name, trans, column, input_features
    ):
        """Gets feature names of transformer.

        Used in conjunction with self.iter(fitted=True)

        Notes
        -----
        Thi is an interface for private method
        :meth:`_get_feature_name_out_for_transformer` of a sklearn
        :class:`ColumnTransformer` instance.

        Returns
        -------
        feature_names_out : list
        """
        input_features = _check_feature_names_in(
            self.column_transformer_, input_features)
        return self.column_transformer_._get_feature_name_out_for_transformer(
            name, trans, column, input_features)

    def _get_feature_dtype_out_for_transformer(self, name, trans, column):
        """Gets feature dtypes of transformer.

        Used in conjunction with self._iter(fitted=True) in
        get_feature_dtypes_out.
        """
        if trans == "drop" or _is_empty_column_selection(column):
            return {}
        elif trans == "passthrough":
            return {c: self.feature_dtypes_in_[c] for c in column}

        # An actual transformer
        if not hasattr(trans, "get_feature_names_out"):
            raise AttributeError(
                f"Transformer {name} (type {type(trans).__name__}) does "
                "not provide get_feature_names_out."
            )
        features_out = trans.get_feature_names_out()
        trans_dtypes = {}
        for feature in features_out:
            if not hasattr(trans, "dtype"):
                if feature not in self.feature_dtypes_in_:
                    raise AttributeError(
                        f"Cannot obtain dtype for Transformer "
                        f"{name} (type {type(trans).__name__}) since it does "
                        "not provide attribute `dtype` and "
                        "features_names_in_ != feature_names_out_."
                    )
                trans_dtypes[feature] = self.feature_dtypes_in_[feature]
            else:
                trans_dtypes[feature] = trans.dtype

        return trans_dtypes


class PandasInverseTransformer:
    """Inverse transformation of a :class:`PandasColumnTransformer` instance.

    Parameters
    ----------
    pd_column_transformer : PandasColumnTransformer
        Fitted :class:`PandasColumnTransformer` instance.
    """

    def __init__(
            self, pd_column_transformer, non_inverse_transformers='ignore'
    ):
        check_is_fitted(pd_column_transformer)
        self.pd_column_transformer = pd_column_transformer
        self.non_inverse_transformers = non_inverse_transformers

    def inverse_transform(self, X):
        """Inverse transforms X.

        Parameters
        ----------
        X : pd.DataFrame
            DataFrame to be inverse transformed.

        Returns
        -------
        X_inv : pd.DataFrame
        """
        inverse_transforms = []
        pandas_columns = []
        for name, trans, features_in, _ in self.pd_column_transformer.iter():
            features_out = self._get_features_out(name, trans, features_in)

            if features_out is not None:
                x = self._check_missing_features(X, name, trans, features_out)
                inv_array = self._inverse_transform(x, name, trans)

                # Since we allow "passthrough" to continue with missing
                # features, is possible that len(x.columns) < len(features_in).
                # Continuing without changes will cause the final column
                # labels for pandas to be more than needed, so set
                # ``features_in`` to whatever is in x.
                if trans == "passthrough":
                    features_in = x.columns

                # Only consider non-empty inverse transformations. Empty
                # inverse transformations arise from transformers without an
                # :meth:`inverse_transform` method when ``raise`` param is set
                # to "ignore".
                if inv_array.size != 0:
                    inverse_transforms.append(inv_array)
                    if isinstance(features_in, str):
                        features_in = [features_in]
                    pandas_columns.append(features_in)

        return self._to_pandas(inverse_transforms, pandas_columns)

    def _to_pandas(self, inverse_transforms, pandas_columns):
        columns = list(chain.from_iterable(pandas_columns))
        dtypes = self._get_feature_dtypes_in()

        # Keep only dtypes with presence in ``columns``.
        dtypes = {col: dtype for col, dtype in dtypes.items() if col in columns}

        arr = hstack(inverse_transforms)
        return pd.DataFrame(arr, columns=columns).astype(dtypes)

    def _check_missing_features(self, X, name, trans, features):
        """Checks missing features in ``X``.

        Raises MissingFeaturesInInverseTransformation when there are missing
        features in X. Else, returns subset of X containing the passed
        features.

        Notes
        -----
        Only "passthrough" transformation is allowed to have missing features.


        Returns
        -------
        X : pd.DataFrame
            Subset of X containing the passed features.
        """
        missing_features = self._get_missing_features(X, features)
        if missing_features:
            if trans == "passthrough":
                # Only "passthrough" transformation is allowed to have
                # missing features (only the ones present in X are returned).
                intersection = self._get_features_intersection(X, features)
                return X[intersection]

            raise InverseTransformFeaturesError(
                name=name, type=type(trans).__name__,
                missing_features=missing_features)

        return X[features]

    def _get_features_out(self, name, trans, features_in):
        """Returns features names out in from ``self.pd_column_transformer``.
        """
        return self.pd_column_transformer.get_feature_name_out_for_transformer(
            name, trans, features_in, input_features=None)

    def _get_feature_dtypes_in(self):
        """Returns feature dtypes in from ``self.pd_column_transformer``.
        """
        return self.pd_column_transformer.feature_dtypes_in_

    def _get_missing_features(self, X, features):
        """Returns features present in ``features`` but not in  ``X``.
        """
        return list(set(features) - set(X))

    def _get_features_intersection(self, X, features):
        """Returns features present in both ``features`` and  ``X``.
        """
        return list(set(features).intersection(set(X)))

    def _inverse_transform(self, X, name, trans):
        """Performs an inverse transformation on the given `columns_to_inv`
        in `X`.

        An empty DataFrame is returned when inverse transformation is not
        possible.

        Parameters
        ----------
        X : pd.DataFrame
            DataFrame to be inverse transformed.

        trans : transformer estimator or 'passthrough'

        Returns
        -------
        X_inv : 2-D numpy array
            Array with inverse transformed columns.
        """
        if trans == 'passthrough':
            return X.values

        if hasattr(trans, 'inverse_transform'):
            return trans.inverse_transform(X)
        else:
            if self.non_inverse_transformers == 'ignore':
                return empty_ndarray(shape=(len(X), 0))
            elif self.non_inverse_transformers == 'raise':
                raise AttributeError(
                    f"Transformer {name} (type {type(trans).__name__}) does "
                    "not provide `inverse_transform` method."
                )
            else:
                raise ValueError(
                    '`non_inverse_transformers` param can either be "ignore" '
                    f'or "raise". Instead got {self.non_inverse_transformers}'
                )


class GroupWiseColumnTransformer(BaseEstimator, TransformerMixin):
    """Transformer that transforms by groups.

    For each group, a :class:`PandasColumnTransformer` is fitted and
    applied.

    Notes
    -----
    The order of the columns in the transformed feature matrix follows the
    order of how the columns are specified in the transformers list. Since the
    passthrough kwarg is set, columns not specified in the transformers list
    are added at the right to the output.

    Parameters
    ----------
    *transformers : tuples
        Tuples of the form (transformer, columns) specifying the
        transformer objects to be applied to subsets of the data.

        transformer : {'drop', 'passthrough'} or estimator
            Estimator must support :term:`fit` and :term:`transform`.
            Special-cased strings 'drop' and 'passthrough' are accepted as
            well, to indicate to drop the columns or to pass them through
            untransformed, respectively.
        columns : str,  array-like of str, int, array-like of int, slice, \
                array-like of bool or callable
            Indexes the data on its second axis. Integers are interpreted as
            positional columns, while strings can reference DataFrame columns
            by name. A scalar string or int should be used where
            ``transformer`` expects X to be a 1d array-like (vector),
            otherwise a 2d array will be passed to the transformer.
            A callable is passed the input data `X` and can return any of the
            above. To select multiple columns by name or dtype, you can use
            :obj:`make_column_selector`.


    Attributes
    ----------
    mapping_ : dict, str -> ColumnTransformer object
        Dictionary mapping from group_id to its corresponding fitted
        ColumnTransformer object
    """

    def __init__(self, transformers, group_ids):
        self.transformers = transformers
        self.group_ids = group_ids

    def fit(self, X, y=None):
        """Fits a sklearn ColumnTransformer object to each group inside ``X``.

        In other words, each group in ``X`` gets assigned its own
        :class:`PandasColumnTransformer` instance which is then fitted to the
        data inside such group.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe having __init__ ``group_ids`` column(s).

        y : None
            This param exists for compatibility purposes with sklearn.

        Returns
        -------
        self (object): Fitted transformer.
        """
        check_group_ids(X, self.group_ids)

        # Mapping from group_id to ColumnTransformer object.
        self.mapping_ = {}

        groups = X.groupby(self.group_ids).groups
        for i, group_id in enumerate(groups):
            pandas_ct = PandasColumnTransformer(self.transformers)
            group = loc_group(X, self.group_ids, group_id)
            pandas_ct.fit(group)
            self.mapping_[group_id] = pandas_ct

        self.pd_column_transformer_ = next(iter(self.mapping_.values()))
        return self

    def transform(self, X):
        """Transforms every group in X using its corresponding
        :class:`ColumnTransformer`.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe having __init__ ``group_ids`` column(s).

        Returns
        -------
        X_out : pd.DataFrame.
            Transformed dataframe
        """
        check_is_fitted(self)
        check_group_ids(X, self.group_ids)

        transformed_dataframes = []
        for group_id, column_transformer in self.mapping_.items():
            group = loc_group(X, self.group_ids, group_id)
            if not group.empty:
                transformed_group = column_transformer.transform(group)
                transformed_dataframes.append(transformed_group)

        return pd.concat(transformed_dataframes).reset_index(drop=True)

    def inverse_transform(self, X):
        """Inverse transformation.

        Notes
        -----
        Transformed columns whose corresponding transformer does not have
        implemented an :meth:`inverse_transform` method will not appear after
        calling this inverse transformation. This causes that the resulting
        DataFrame ``X_out`` might not be equal to the original X, that is, the
        expression X = f-1(f(X)) wont be satisfied.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to be inverse transformed.

        Returns
        -------
        X_inv : pd.DataFrame
            Inverse transformed dataframe
        """
        check_is_fitted(self)
        check_group_ids(X, self.group_ids)

        inverse_transforms = []
        for group_id, pandas_column_transformer in self.mapping_.items():
            group = loc_group(X, self.group_ids, group_id)
            if not group.empty:
                inv = pandas_column_transformer.inverse_transform(group)
                inverse_transforms.append(inv)

        return pd.concat(inverse_transforms)

    def iter(self, fitted=True, replace_strings=False, column_as_strings=True):
        return self.pd_column_transformer_.iter(
            fitted, replace_strings, column_as_strings)

    @property
    def feature_names_in_(self):
        return self.pd_column_transformer_.feature_names_in_

    def get_feature_names_out(self, input_features=None):
        return self.pd_column_transformer_.get_feature_names_out(input_features)

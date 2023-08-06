import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array

from ..utils.conversions import series_to_2d
from ..utils.validation import check_pandas


def _identity(X):
    """The identity function."""
    return X


class IdentityTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return _identity(X)

    def inverse_transform(self, X):
        return _identity(X)


class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, to_drop):
        self.to_drop = to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X.drop(self.to_drop, axis='columns')


class ColumnDuplicator(BaseEstimator, TransformerMixin):
    """
    Parameters
    ----------
    out_feature : str
        Name of output column.
    """

    def __init__(self, out_feature, identity_inverse=True):
        self.out_feature = out_feature
        self.identity_inverse = identity_inverse

    def fit(self, X, y=None):
        self.feature_names_in_ = np.array([X.name])
        self.dtype = X.dtype
        return self

    def transform(self, X):
        check_pandas(X, 'series', self)
        X = series_to_2d(X)
        return np.tile(X, 2)

    def inverse_transform(self, X):
        if self.identity_inverse:
            inverse_transformer = IdentityTransformer()
        else:
            inverse_transformer = ColumnDropper(self.out_feature)

        return inverse_transformer.transform(X)

    def get_feature_names_out(self, input_features=None):
        a1 = self.feature_names_in_
        a2 = np.array([self.out_feature])
        return np.concatenate((a1, a2))


class UnitCircleProjector(BaseEstimator, TransformerMixin):
    def __init__(self, feature_name_out_prefix=None, dtype=np.float):
        self.feature_name_out_prefix = feature_name_out_prefix
        self.dtype = dtype

    def fit(self, X, y=None):
        self.data_max_ = X.max()
        return self

    def transform(self, X):
        X = check_array(X)
        sine = self._sine_transform(X)
        cosine = self._cosine_transform(X)
        return np.concatenate((sine, cosine), axis=1)

    def _sine_transform(self, X):
        """Fourier sine transformation on X.
        """
        return np.sin((2 * np.pi * X) / self.data_max_)

    def _cosine_transform(self, X):
        """Fourier cosine transformation on X.
        """
        return np.cos((2 * np.pi * X) / self.data_max_)

    def get_feature_names_out(self):
        if self.feature_name_out_prefix is None:
            prefix = ''
        else:
            prefix = self.feature_name_out_prefix

        return np.array([prefix + '_sine', prefix + '_cosine'])

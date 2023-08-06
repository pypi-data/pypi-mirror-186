from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.utils.validation import check_is_fitted


class PreprocessorEstimatorWrapper(BaseEstimator):
    """Wraps preprocessor and estimator into a single sklearn pipeline.

    Parameters
    ----------
    estimator : Estimator
        Fitted estimator (implementing `fit`/`predict`).

    preprocessor : Transformer
        Fitted transformer (implementing `fit`/`transform`).

    inverse_transform_steps : list of str
        Steps inside preprocessor whose inverse transformation will be used
        after prediction. If None, all the ``preprocessor`` will be used
        for inverse transforming predictions, that is,
        preprocessor.inverse_transform(output).
    """

    def __init__(self, preprocessor, estimator, inverse_transform_steps=None):
        self.preprocessor = preprocessor
        self.estimator = estimator

        self.inverse_transform_steps = inverse_transform_steps

    def fit(self, X, y=None):
        """Fits pipeline composed by both the preprocessor and estimator on X.

        Parameters
        ----------
        X : pd.DataFrame
            Input data

        y : None
            Compatibility purposes.

        Returns
        -------
        self (object)
        """
        self.pipeline_ = self.make_pipeline()
        self.pipeline_.fit(X)
        return self

    def make_pipeline(self):
        steps = [
            ('preprocessor', self.preprocessor),
            ('estimator', self.estimator)
        ]
        return Pipeline(steps)

    def predict(self, X):
        check_is_fitted(self)
        output = self.pipeline_.predict(X, raw=False)
        return self._inverse_transform_prediction(output)

    def _inverse_transform_prediction(self, X):
        preprocessor = self.pipeline_['preprocessor']
        for step in self.inverse_transform_steps:
            inverse_transformer = preprocessor[step]
            X = inverse_transformer.inverse_transform(X)
        return X

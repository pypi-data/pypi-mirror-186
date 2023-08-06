import pandas as pd
from pytorch_forecasting import \
    TimeSeriesDataSet as pytorchForecastingTimeseriesDataset


class TimeseriesDataset(pytorchForecastingTimeseriesDataset):
    """Dataset for time series models.

    Parameters
    ----------
    data : pd.DataFrame
        Dataframe with time series data. Each row can be identified with
        ``date`` and the ``group_ids``.

    group_ids : list of str
        List of column names identifying a time series. This means that the
        ``group_ids`` identify a sample together with ``date``. If you
        have only one times series, set this to the name of column that is
        constant.

    time_idx : str
        Time index column.

    target : str
        Target column.

    max_prediction_length : int
        Maximum prediction/decoder length. Usually this is defined by the
        difference between forecasting dates.

    max_encoder_length : int, default=None
        Maximum length to encode (also known as `input sequence length`). This
        is the maximum history length used by the time series dataset.

    time_varying_known_reals : list of str
        List of continuous variables that change over time and are known in the
        future (e.g. price of a product, but not demand of a product).

    time_varying_unknown_reals : list of str
        List of continuous variables that change over time and are not known in
        the future. You might want to include your ``target`` here.

    static_categoricals : list of str
        List of categorical variables that do not change over time (also known
        as `time independent variables`). You might want to include your
        ``group_ids`` here for the learning algorithm to distinguish between
        different time series.
    """

    def __init__(
            self, data, group_ids, time_idx, target, max_prediction_length,
            max_encoder_length, time_varying_known_reals,
            time_varying_unknown_reals, static_categoricals, scalers=None,
            categorical_encoders=None, target_normalizer=None,
            predict_mode=False
    ):

        if scalers is None:
            scalers = {}
        if categorical_encoders is None:
            categorical_encoders = {}
        super().__init__(
            data=data, time_idx=time_idx, target=target, group_ids=group_ids,
            max_encoder_length=max_encoder_length,
            max_prediction_length=max_prediction_length,
            time_varying_known_reals=time_varying_known_reals,
            time_varying_unknown_reals=time_varying_unknown_reals,
            static_categoricals=static_categoricals,
            scalers=scalers, categorical_encoders=categorical_encoders,
            target_normalizer=target_normalizer, predict_mode=predict_mode
        )

    def _construct_index(
            self,
            data: pd.DataFrame,
            predict_mode: bool
    ) -> pd.DataFrame:

        df_index = super()._construct_index(data, predict_mode=False)

        if predict_mode:
            # Get the rows containing the max sequence length of their group.
            # Note that if a group has multiple max values, all will be
            # returned.
            max_on_each_row = df_index.groupby('sequence_id')[
                'sequence_length'].transform(max)
            idx = (max_on_each_row == df_index['sequence_length'])
            return df_index.loc[idx].reset_index(drop=True)

        return df_index

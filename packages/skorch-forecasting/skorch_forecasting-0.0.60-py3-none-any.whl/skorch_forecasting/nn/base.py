import inspect
from abc import ABCMeta, abstractmethod
from copy import deepcopy

import numpy as np
import pandas as pd
import skorch.dataset
import torch
from pytorch_forecasting.metrics import MultiHorizonMetric, RMSE
from sklearn.base import BaseEstimator as sklearnBaseEstimator
from sklearn.utils.validation import check_is_fitted
from skorch import NeuralNet
from skorch.callbacks import Callback, LRScheduler
from skorch.helper import predefined_split
from skorch.utils import params_for
from torch.utils.data import Dataset
from torch.utils.data.dataloader import default_collate

from ..utils.data import SliceDataset, safe_math_eval
from ..utils.pytorch_forecasting import output_class, output_transformer


class BaseModule(torch.nn.Module, metaclass=ABCMeta):
    """Base class for pytorch neural network modules.

    .. note::
        This class should not be used directly. Use derived classes instead.
    """

    @classmethod
    @abstractmethod
    def from_dataset(cls, dataset, **kwargs):
        """Create model from dataset

        Parameters
        ----------
        dataset : timeseries dataset

        Returns
        -------
        BaseModule: Model that can be trained
        """
        pass


class NeuralNetEstimator(sklearnBaseEstimator):
    """Base class for all neural net estimators in skorch-forecasting.
    """

    def _get_param_names(self):
        return (k for k in self.__dict__ if not k.endswith('_'))

    def get_params(self, deep=True):
        params = super().get_params(deep=deep)

        # Don't include the following attributes.
        to_exclude = {'module', 'dataset'}
        return {key: val for key, val in params.items() if
                key not in to_exclude}

    def get_init_signature(self, cls):
        """Inspects given class using the inspect package and extracts the
        parameter attribute from its signature

        Parameters
        ----------
        cls : class

        Returns
        -------
        init params : list
        """
        init = getattr(cls.__init__, "deprecated_original", cls.__init__)
        if init is object.__init__:
            # No explicit constructor to introspect
            return []
        return inspect.signature(init)

    def get_kwargs_for(self, name, add_prefix=False):
        """Collects __init__ kwargs for an attribute.

        Attributes must be type class and could be, for instance, pytorch
        modules, criteria or data loaders.

        The returned kwargs are obtained by inspecting the __init__ method
        from the passed attribute (e.g., module.__init__()) and from prefixed
        kwargs (double underscore notation, e.g., 'module__something') passed
        at __init__.

        Parameters
        ----------
        name : str
            The name of the attribute whose arguments should be
            returned. E.g. for the module, it should be ``'module'``.

        add_prefix : bool
            If True, keys will contain ``name`` with double underscore as
            prefix.

        Returns
        -------
        kwargs : dict
        """
        cls = getattr(self, name)
        init_signature = self.get_init_signature(cls)

        # Consider the constructor parameters.
        kwargs = {
            k: v
            for k, v in vars(self).items()
            if k in init_signature.parameters
        }

        # Consider also kwargs with prefix "name".
        prefixed_kwargs = params_for(prefix=name, kwargs=self.__dict__)
        kwargs.update(prefixed_kwargs)

        if add_prefix:
            kwargs = {name + '__' + k: v for k, v in kwargs.items()}
        return kwargs


class BaseCollateFn:
    """Base collate function.

    Collate functions are used by PyTorch to combine mini batches.

    Parameters
    ----------
    dataset : Dataset, default=None
    """

    def __init__(self, dataset=None):
        self.dataset = dataset

    def __call__(self, batch):
        """Default collate function.

        Parameters
        ----------
        batch : list of tuples.
        """
        return default_collate(batch)


class TimeSeriesEstimator(NeuralNetEstimator):
    """Base class for trainers

    In addition to the parameters listed below, there are parameters
    with specific prefixes that are handled separately. To illustrate
    this, here is an example:

    >>> net = NeuralNet(
    ...    [...],
    ...    optimizer=torch.optim.SGD,
    ...    optimizer__momentum=0.95,
    ...)

    This way, when ``optimizer`` is initialized, :class:`.NeuralNet`
    will take care of setting the ``momentum`` parameter to 0.95.
    (Note that the double underscore notation in
    ``optimizer__momentum`` means that the parameter ``momentum``
    should be set on the object ``optimizer``. This is the same
    semantic as used by sklearn.). Supported prefixes include:
    ['module',
    'iterator_train',
    'iterator_valid',
    'optimizer',
    'criterion',
    'callbacks',
    'dataset']

    .. note::
        This class should not be used directly. Use derived classes instead.
    
    Parameters
    ----------
    module : class
        Neural network class that inherits from :class:`BaseModule`

    group_ids : list of str
        List of column names identifying a time series. This means that the
        group_ids identify a sample together with the time_idx. If you have
        only one time series, set this to the name of column that is constant.

    time_idx : str
        Time index column. This column is used to determine the sequence of
        samples.

    target : str
        Target column. Column containing the values to be predicted.

    max_prediction_length : int
        Maximum prediction/decoder length (choose this not too short as it can
        help convergence)

    max_encoder_length : int
        Maximum length to encode. This is the maximum history length used by
        the time series dataset.

    time_varying_known_reals : list of str
        List of continuous variables that change over time and are known in the
        future (e.g. price of a product, but not demand of a product). If None,
        every numeric column excluding ``target`` is used.

    time_varying_unknown_reals : list of str
        List of continuous variables that change over time and are not known in
        the future. You might want to include your ``target`` here. If None,
        only ``target`` is used.

    static_categoricals : list of str
        List of categorical variables that do not change over time (also known
        as `time independent variables`). You might want to include your
        ``group_ids`` here for the learning algorithm to distinguish between
        different time series. If None, only ``group_ids`` is used.
      
    dataset : class
        The dataset is necessary for the incoming data to work with
        pytorch :class:`DataLoader`. Must inherit from
        :class:`pytorch.utils.data.Dataset`.

    min_encoder_length : int, default=None
        Minimum allowed length to encode. If None, defaults to
        ``max_encoder_length``.

    criterion : class, default=None
        The uninitialized criterion (loss) used to optimize the
        module. If None, the root mean squared error (:class:`RMSE`) is used.

    optimizer : class, default=None
        The uninitialized optimizer (update rule) used to optimize the
        module. If None, :class:`Adam` optimizer is used.

    lr : float, default=1e-5
        Learning rate passed to the optimizer.

    max_epochs : int, default=10
        The number of epochs to train for each :meth:`fit` call. Note that you
        may keyboard-interrupt training at any time.

    batch_size : int, default=64
        Mini-batch size. If ``batch_size`` is -1, a single batch with all the
        data will be used during training and validation.

    callbacks: None, “disable”, or list of Callback instances, default=None
        Which callbacks to enable.

        - If callbacks=None, only use default callbacks which include:
            - `epoch_timer`: measures the duration of each epoch
            - `train_loss`: computes average of train batch losses
            - `valid_loss`: computes average of valid batch losses
            - `print_log`:  prints all of the above in nice format

        - If callbacks="disable":
            disable all callbacks, i.e. do not run any of the callbacks.

        - If callbacks is a list of callbacks:
            use those callbacks in addition to the default ones. Each
            callback should be an instance of skorch :class:`.Callback`.

        Alternatively, a tuple ``(name, callback)`` can be passed, where
        ``name`` should be unique. Callbacks may or may not be instantiated.
        The callback name can be used to set parameters on specific
        callbacks (e.g., for the callback with name ``'print_log'``, use
        ``net.set_params(callbacks__print_log__keys_ignored=['epoch',
        'train_loss'])``).

    warm_start: bool, default=False
        Whether each fit call should lead to a re-initialization of the module
        (cold start) or whether the module should be trained further
        (warm start).

    verbose : int, default=1
        This parameter controls how much print output is generated by
        the net and its callbacks. By setting this value to 0, e.g. the
        summary scores at the end of each epoch are no longer printed.
        This can be useful when running a hyperparameters search. The
        summary scores are always logged in the history attribute,
        regardless of the verbose setting.

    device : str, torch.device, default='cpu'
        The compute device to be used. If set to 'cuda', data in torch
        tensors will be pushed to cuda tensors before being sent to the
        module. If set to None, then all compute devices will be left
        unmodified.

    kwargs : dict
       Extra prefixed parameters (see list of supported prefixes above).

    Attributes
    ----------
    callbacks_ : list of (name, obj) tuples
        Callbacks used during training.

    dataset_params_ : dict
        Training dataset parameters.

    net_ : skorch NeuralNet
        Fitted neural net.
    """

    prefixes = [
        'module',
        'iterator_train',
        'iterator_valid',
        'optimizer',
        'criterion',
        'callbacks',
        'dataset'
    ]

    def __init__(self, module, dataset, group_ids, time_idx, target,
                 max_prediction_length, max_encoder_length,
                 time_varying_known_reals, time_varying_unknown_reals,
                 static_categoricals, cv_split=None, min_encoder_length=None,
                 criterion=None, optimizer=None, lr=1e-5, max_epochs=10,
                 batch_size=64, callbacks=None, warm_start=False, verbose=1,
                 device='cpu', **kwargs):
        self.module = module
        self.dataset = dataset
        self.group_ids = group_ids
        self.time_idx = time_idx
        self.target = target
        self.max_prediction_length = max_prediction_length
        self.max_encoder_length = max_encoder_length
        self.time_varying_known_reals = time_varying_known_reals
        self.time_varying_unknown_reals = time_varying_unknown_reals
        self.static_categoricals = static_categoricals
        self.cv_split = cv_split
        self.min_encoder_length = min_encoder_length
        self.criterion = RMSE if criterion is None else criterion
        self.optimizer = torch.optim.Adam if optimizer is None else optimizer
        self.lr = lr
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.callbacks = callbacks
        self.warm_start = warm_start
        self.verbose = verbose
        self.device = device
        self._collate_fn = BaseCollateFn
        self._output_decoder = None
        self._check_params()
        vars(self).update(kwargs)

    def fit(self, X, y=None):
        """Initialize and fit the neural net estimator.

        If the module was already initialized, by calling fit, the module
        will be re-initialized (unless warm_start is True).

        Parameters
        ----------
        X : pd.DataFrame
            The input data

        y : None
            This parameter only exists for sklearn compatibility and must
            be left in None

        Returns
        -------
        self : trained neural net
        """
        X = self.get_dataset(X)

        # Fit :attr:`net_` if it already exists.
        if hasattr(self, 'net_'):
            self.net_.fit(X)
        else:
            self.dataset_params_ = X.get_parameters()
            self.net_ = self._initialize_skorch_net(X)
            self.net_.fit(X)

        return self

    def predict(self, X, raw=True):
        """Predicts input data X.

        Parameters
        ----------
        X : pd.DataFrame
            Input values

        Returns
        -------
        X_out : np.array.
            Predicted values.
        """
        check_is_fitted(self)

        dataset = self.get_dataset(
            X, params=self.dataset_params_, predict_mode=True)
        raw_output = self.net_.predict(dataset)

        if raw:
            return raw_output

        output_decoder = self.get_output_decoder()
        if output_decoder is None:
            raise

        return output_decoder(dataset).decode(raw_output, out=X)

    def get_dataset(self, X, params=None, sliceable=False, **kwargs):
        """Constructs torch dataset using the input data ``X``

        Parameters
        ----------
        X : pd.DataFrame
            Input data

        params : dict, default=None
            If given, generates torch dataset using this parameters. Otherwise,
            the parameters are obtained from the object (self) attributes.

        sliceable : bool, default=False
            If True, the sliceable version of the dataset is returned

        **kwargs : key-word arguments
            Additional parameters passed to dataset class. If given,
            kwargs will override values given to ``params``.

        Returns
        -------
        dataset: torch dataset
            The initialized dataset.
        """
        # Return ``X`` if already is a dataset
        if isinstance(X, torch.utils.data.Dataset):
            return X
        if params is not None:
            dataset = self.dataset.from_parameters(params, X, **kwargs)
        else:
            dataset_params = self.get_kwargs_for('dataset')
            dataset_params.update(kwargs)
            dataset = self.dataset(X, **dataset_params)
        if sliceable:
            return SliceDataset(dataset)
        return dataset

    def _get_train_split(self, train_dataset):
        """Obtains the validation technique used during training.

        Parameters
        ----------
        train_dataset : torch Dataset
            Training torch dataset

        Returns
        -------
        iterable
        """
        if self.cv_split is None:
            return None

        if isinstance(self.cv_split, (pd.DataFrame, torch.utils.data.Dataset)):
            valid_dataset = self.get_dataset(
                X=self.cv_split,
                params=self.dataset_params_
            )
            return predefined_split(valid_dataset)
        elif isinstance(self.cv_split, int):
            if not hasattr(train_dataset, 'timeseries_cv'):
                obj_name = type(train_dataset).__name__
                raise ValueError(
                    'Dataset {} does not have a '
                    'timeseries_cv method'.format(obj_name)
                )
            # ``cv`` is list containing train, validation splits (tuples)
            cv = train_dataset.timeseries_cv(self.cv_split)
            return skorch.dataset.CVSplit(cv=cv)
        elif isinstance(self.cv_split, skorch.dataset.CVSplit):
            return self.cv_split
        else:
            obj_name = type(self.cv_split).__name__
            raise ValueError(
                'Passed `cv_split` {} not supported'.format(obj_name)
            )

    def _initialize_skorch_net(self, X):
        """Initializes :class:`NeuralNet`.

        Parameters
        ----------
        X : torch dataset
            Training dataset

        Returns
        -------
        skorch NeuralNet fitted
        """
        collate_fn = self.get_collate_fn()(X)
        return NeuralNet(
            module=self._initialize_module(X),
            criterion=self.criterion,
            optimizer=self.optimizer,
            lr=self.lr,
            max_epochs=self.max_epochs,
            batch_size=self.batch_size,
            callbacks=self._initialize_callbacks(X),
            verbose=self.verbose,
            device=self.device,
            warm_start=self.warm_start,
            train_split=self._get_train_split(X),
            iterator_train__shuffle=True,
            iterator_train__collate_fn=collate_fn,
            iterator_valid__collate_fn=collate_fn
        )

    def get_collate_fn(self):
        return self._collate_fn

    def get_output_decoder(self):
        return self._output_decoder

    def _initialize_module(self, X):
        """Instantiates pytorch module using object (self) attributes and
        training dataset

        Parameters
        ----------
        X : torch dataset
            Training dataset. Used as input in ``from_dataset`` method

        Returns
        -------
        module : torch neural net object
            Instantiated neural net
        """
        module_kwargs = self.get_kwargs_for('module')
        module = self.module.from_dataset(X, **module_kwargs)
        return module.to(self.device)

    def _initialize_callbacks(self, train_dataset):
        """Evaluates string expressions in callbacks.

        Returns
        -------
        callbacks : list of callbacks
        """
        # Do not alter original callbacks
        callbacks = deepcopy(self.callbacks)

        if self.callbacks is not None:
            # ``iterations`` is the number of batches on each epoch
            iterations = int(np.ceil(len(train_dataset) / self.batch_size))
            for name, obj in callbacks:
                if isinstance(obj, LRScheduler):
                    for key, value in vars(obj).items():
                        if isinstance(value, str):
                            if 'iterations' in value:
                                value = value.replace(
                                    'iterations', str(iterations)
                                )
                                vars(obj)[key] = safe_math_eval(value)
                            elif hasattr(self, value):
                                vars(obj)[key] = getattr(self, value)
        return callbacks

    def _check_params(self):
        """Collection of parameters validations.
        """
        if not issubclass(self.optimizer, torch.optim.Optimizer):
            raise ValueError(
                'optimizer must be a subclass of torch.optim.Optimizer. '
                'Instead got {}'.format(self.optimizer)
            )
        if not issubclass(self.criterion, torch.nn.Module):
            raise ValueError(
                'criterion must be a subclass of torch.nn.Module. Instead got '
                '{}'.format(self.optimizer)
            )
        if self.callbacks is not None:
            for i, tup in enumerate(self.callbacks):
                if not isinstance(tup, tuple):
                    raise ValueError(
                        'callbacks must contain a list of (name, callback) '
                        'tuples. Instead on index {} got {}'.format(i, tup)
                    )
                name, obj = tup
                if not isinstance(obj, Callback):
                    obj_name = obj.__class__.__name__
                    raise ValueError(
                        'callback with name {} is not a skorch Callback '
                        'object. Instead got {}'.format(name, obj_name)
                    )
        if not isinstance(self.criterion(), MultiHorizonMetric):
            raise ValueError(
                'criterion must be a pytorch_forecasting metric. Select one '
                'from module pytorch_forecasting.metrics'
            )


class PytorchForecastingEstimator(TimeSeriesEstimator):
    """Base class for pytorch_forecasting models that collects common
    methods between them.

    .. note::
        This class should not be used directly. Use derived classes instead.
    """

    def __init__(
            self, module, dataset, group_ids, time_idx, target,
            max_prediction_length, max_encoder_length,
            time_varying_known_reals, time_varying_unknown_reals,
            static_categoricals, cv_split=None, min_encoder_length=None,
            criterion=None, optimizer=None, lr=1e-5, max_epochs=10,
            batch_size=64, callbacks=None, verbose=1, device='cpu',
            **kwargs
    ):
        super().__init__(
            module=module, dataset=dataset,
            group_ids=group_ids, time_idx=time_idx, target=target,
            max_prediction_length=max_prediction_length,
            max_encoder_length=max_encoder_length,
            time_varying_known_reals=time_varying_known_reals,
            time_varying_unknown_reals=time_varying_unknown_reals,
            static_categoricals=static_categoricals, cv_split=cv_split,
            min_encoder_length=min_encoder_length, criterion=criterion,
            optimizer=optimizer, lr=lr, max_epochs=max_epochs,
            batch_size=batch_size, callbacks=callbacks, verbose=verbose,
            device=device, **kwargs
        )
        self.loss = self.criterion()

    def interpret_output(self, X):
        """Provides a visual interpretation of the models output that includes
        feature ranking and attention across time index.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to predict / Dataframe whose prediction wants to be
            interpreted

        Returns
        -------
        None
        """
        raw_predictions = self._raw_predict(X)
        interpretation = self.net_.module_.interpret_output(
            raw_predictions, reduction="sum"
        )
        self.net_.module_.plot_interpretation(interpretation)

    def plot_prediction(self, X, idx, add_loss_to_title=False, ax=None):
        """Provides a visual view of the model's output.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to predict
        idx : int
            Number of sequence to visualize
        add_loss_to_title : bool
            If True, the loss is given inside the ax title
        ax : matplotlib ax
            matplotlib axes to plot on

        Returns
        -------
        None
        """
        raw_predictions, x = self._raw_predict(X, return_x=True)
        self.net_.module_.plot_prediction(
            x, raw_predictions, idx=idx, add_loss_to_title=add_loss_to_title,
            ax=ax
        )

    def _initialize_module(self, train_dataset):
        """Instantiates pytorch module using object (self) attributes and
        training dataset.

        Complete compatibility with skorch requires assigning two methods:
        `output_transformer` and `output_class`. See their docstring for
        further details

        Returns
        -------
        module : torch neural net object
            Instantiated neural net
        """
        module_kwargs = self.get_kwargs_for('module')
        module_kwargs.update({'output_transformer': output_transformer})
        module = self.module.from_dataset(train_dataset, **module_kwargs)
        module._output_class = output_class
        return module

    def _raw_predict(self, X, return_x=False):
        """Computes raw prediction.

        Used in `interpret_output` and `plot_prediction` methods.
        ``raw_predictions`` is a dictionary containing a lot of info about
        the model's output for any X. They are used for model interpretation
        and plotting output methods. To access raw predictions, the
        _output_class attribute has to be silenced to activate the default
        behaviour inside the TemporalFusionTransformer forward method. Such
        default behaviour along with kwarg mode='raw' will give us the
        raw predictions. At the end, the _output_class attribute is recovered.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to predict
        return_x : bool
            If True, the given X is returned in tensor format

        Returns
        -------
        raw predictions : dict
        """
        # Delete _output_class attribute from skorch module
        if hasattr(self.net_.module, '_output_class'):
            module = True
            delattr(self.net_.module, '_output_class')
        else:
            module = False
        if hasattr(self.net_.module_, '_output_class'):
            module_ = True
            delattr(self.net_.module_, '_output_class')
        else:
            module_ = False

        # Generate raw predictions
        ds = self.get_dataset(X)
        raw_predictions = self.net_.module_.predict(
            ds, mode='raw', batch_size=len(ds), return_x=return_x
        )
        # Recover _output_class attribute
        if module:
            self.net_.module._output_class = output_class
        if module_:
            self.net_.module_._output_class = output_class
        return raw_predictions

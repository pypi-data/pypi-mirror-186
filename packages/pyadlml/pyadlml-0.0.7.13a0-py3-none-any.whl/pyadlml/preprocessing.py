import pandas as pd
import numpy as np

from sklearn.utils.metaestimators import _safe_split
import sklearn.preprocessing as preprocessing
from sklearn.base import BaseEstimator, TransformerMixin

from pyadlml.dataset._representations.raw import create_raw, resample_raw
from pyadlml.dataset._representations.changepoint import create_changepoint, resample_changepoint
from pyadlml.dataset._representations.lastfired import create_lastfired, resample_last_fired
from pyadlml.dataset._core.acts_and_devs import label_data
from pyadlml.constants import ACTIVITY, TIME, DEVICE, VALUE, END_TIME, START_TIME, \
                              ENC_RAW, ENC_LF, ENC_CP, REPS
from pyadlml.dataset._core.devices import create_device_info_dict
from pyadlml.pipeline import XOrYTransformer, XAndYTransformer, YTransformer
from pyadlml.constants import OTHER


class Df2Numpy(TransformerMixin, XOrYTransformer):
    """ Transforms dataframes to numpy arrays by respecting
    the column order
    """
    _x_columns = []
    _y_columns = []

    def __init__(self):
        pass

    def fit(self, X, y=None):
        self._x_columns = X.columns
        if y is not None:
            self._y_columns = y.columns


    def fit_transform(self, X, y):
        self.fit(X,y)
        return self.transform(X,y)

    def transform(self, X, y):
        # reorder columns
        X = X[self._x_columns]
        y = y[self._y_columns]

        #
        X_np = X.values
        y_np = y.values
        return X_np, y_np


class DfCaster(TransformerMixin, XOrYTransformer):
    """ Transforms dataframes to torch tensors by respecting
    the column order
    """
    _x_columns = []
    _y_columns = []
    Df2Numpy = 'df->np'
    Df2Torch = 'df->torch'

    def __init__(self, x_conv, y_conv):
        self.y_conv = y_conv
        self.x_conv = x_conv

    def fit(self, X, y=None):
        assert self.y_conv in [self.Df2Numpy, self.Df2Torch]
        assert self.x_conv in [self.Df2Numpy, self.Df2Torch]

        self._x_columns = X.columns
        if y is not None:
            self._y_columns = y.columns


    def fit_transform(self, X, y=None):
        self.fit(X, y=y)
        return self.transform(X, y=y)

    def transform(self, X, y=None):
        """
        Parameters
        ----------
        X : pd
        """

        # reorder columns
        X = X[self._x_columns]

        # cast to respective format
        if self.x_conv == self.Df2Torch:
            import torch
            X_prime = torch.tensor(X.values, dtype=torch.float32)
        elif self.x_conv == self.Df2Numpy:
            X_prime = X.values.astype('float32')

        if y is not None:
            y = y[self._y_columns]
            if self.y_conv == self.Df2Torch:
                import torch
                y_prime = torch.tensor(y.values, dtype=torch.int64)
            elif self.y_conv == self.Df2Numpy:
                # ensure that y has dim (N,) and is of correct type
                y_prime = y.values.squeeze().astype('int64')
            return X_prime, y_prime
        else:
            return X_prime


class Df2Torch(TransformerMixin, XOrYTransformer):
    """ Transforms dataframes to torch tensors by respecting
    the column order
    """
    _x_columns = []
    _y_columns = []

    def __init__(self, only_y=False, only_X=False):
        self.only_y = only_y
        self.only_X = only_X

    def fit(self, X, y=None):
        self._x_columns = X.columns
        if y is not None:
            self._y_columns = y.columns


    def fit_transform(self, X, y):
        self.fit(X,y)
        return self.transform(X,y)

    def transform(self, X, y):
        """
        Parameters
        ----------
        X : pd
        """
        import torch

        # reorder columns
        X = X[self._x_columns]
        y = y[self._y_columns]

        # cast to tensors
        y_tensor = torch.tensor(y.values, dtype=torch.int64)
        X_tensor = torch.tensor(X.values, dtype=torch.float32)

        return X_tensor, y_tensor


class IdentityTransformer(TransformerMixin, XOrYTransformer):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    @XOrYTransformer.x_or_y_transform
    def transform(self, X=None, y=None):
        return X, y


class RandomUnderSampler(TransformerMixin, XAndYTransformer):

    def __init__(self, sampling_strategy):
        self.sampling_strategy = sampling_strategy

    def fit(self, X, y, *args):
        from imblearn.under_sampling import RandomUnderSampler as ImbRUS
        self.rus_ = ImbRUS(sampling_strategy=self.sampling_strategy)
        return self

    def fit_transform(self, X, y, **fit_params):
        self.fit(X, y)
        return self.transform(X, y)

    def transform(self, X, y):
        return self.rus_.fit_resample(X,y)


class DropNanRows(XOrYTransformer):
    """
    Drops all rows where the label or the data has a nan-value
    """
    def fit(self, X,y=None):
        return self

    def fit_transform(self, X, y=None):
        return self.transform(X, y=y)

    def transform(self, X, y=None):
        """
        If X is given transform y
        """
        if y is not None:
            if isinstance(y, pd.DataFrame):
                nan_mask = y[ACTIVITY].isna().values
                return X[~nan_mask], y[~nan_mask]

            elif isinstance(y, np.ndarray):
                raise NotImplementedError
        else:
            nan_mask = X.isna().values
            return X[~nan_mask]


class DropDuplicates(TransformerMixin, XOrYTransformer):
    def __init__(self, ignore_columns=[], merge_on='time'):
        BaseEstimator.__init__(self)
        XOrYTransformer.__init__(self)

        self.ignore_columns = [ignore_columns] if not isinstance(ignore_columns, list) else ignore_columns
        self.merge_on = merge_on

    def fit(self, X, y=None):
        return self

    def fit_transform(self, X, y=None, **fit_params):
        return self.transform(X, y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X=None, y=None):
        """  Depending if X or y is given drop either all Nans in y or all nans in X or
        all Nans in the union of X and y.

        """
        if y is not None and X is not None:
            assert isinstance(y, pd.DataFrame)
            tmp = X.copy().reset_index(drop=True)
            y = y.copy().reset_index(drop=True)

            y_cols = y.columns.to_list()
            if len(y.columns) > 1:
                y_cols.remove(self.merge_on)
                tmp = tmp.merge(y, on=self.merge_on)
            else:
                tmp[y_cols] = y
            comp_cols = list(set(tmp.columns) - set(self.ignore_columns))
            dup_mask = tmp[comp_cols].duplicated()

            y = y[~dup_mask].reset_index(drop=True)
            X = X[~dup_mask].reset_index(drop=True)

        if y is not None and X is None:
            y = y.drop_duplicates()
        if X is not None and y is None:
            X = X.drop_duplicates()
        return X, y


class DropTimeIndex(TransformerMixin, XOrYTransformer):
    def __init__(self):
        XOrYTransformer.__init__(self)

    def fit(self, X=None, y=None):
        return self

    def fit_transform(self, X=None, y=None, **fit_params):
        """ Drops columns that are not time dependent
        """
        return self.transform(X, y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X=None, y=None):
        if X is not None:
            X = X.loc[:, X.columns != TIME]
        if y is not None:
            y = y.loc[:, y.columns != TIME]
        return X, y


class CVSubset(TransformerMixin, XOrYTransformer):
    """ Selects the subset from the whole dataset based on a given data_range.

    Attributes
    ----------
    data_range  : list of either indices or interval
        Either
    y : boolean, default=False
        Only

    """
    def __init__(self, data_range=None, y=False):
        self.data_range = data_range
        XOrYTransformer.__init__(self)

    def set_range(self, data_range):
        self.data_range = data_range

    def _extract_first_sample(self, data_range):
        try:
            sample = data_range[0][0]
        except TypeError:
            sample = data_range[0]
        except IndexError:
            sample = data_range[0]
        return sample


    def fit(self, X, y=None):
        error_msg = "Data range has to be set to either time intervals or list of indicies. Not 'None'"
        assert self.data_range is not None, error_msg

        # determine whether the splits are made based on index ranges or timestamp tuples
        sample = self._extract_first_sample(self.data_range)
        self.timestamps_ = not (isinstance(sample, int) or isinstance(sample, np.int64))

        return self

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X, y=None):
        """ Selects a subset of X and y based on the data_range and the split type
        """
        if self.timestamps_:
            x_mask = _create_mask(X, self.data_range)
            X = X[x_mask]
            if y is not None:
                assert len(X) == len(y)
                y_mask = _create_mask(y, self.data_range)
                y = y[y_mask]
            return X, y
        else:
            X, y = _safe_split(None, X, y, self.data_range)
            return X, y


def _create_mask(X, date_range):
    x_mask = (X[TIME] == 'false_init')
    if isinstance(date_range, tuple):
        date_range = [date_range]
    for time_pair in date_range:
        x_mask = x_mask | ((time_pair[0] < X[TIME]) & (X[TIME] < time_pair[1]))
    return x_mask


class StateVectorEncoder(BaseEstimator, TransformerMixin):
    """
    Create a State-vector sequence from a device event stream.
    Read more in the :ref:`User Guide <preprocessing_discretization>`.

    Parameters
    ----------
    encode : {'raw', 'changepoint', 'last_fired'}, default='raw'
        Determines the state-vectors encoding.

        raw
            Encode the event stream as vector, where each field
            represents a device. Each entry represents the current
            state that the device is in.

        changepoint
            Encode the event stream as one-hot binary vector, where
            each field represents a device. A one indicates the
            device that produced the event.

        last_fired
            Encode the event stream as one-hot binary vector,
            where each field represents a device. The device that produced
            the last event is indicated with one.

    dt : str, optional, default=None
        The timeslices resolution for discretizing the event stream. If
        set to None the event stream is not discretized.

    Attributes
    ----------
    encode : string
        The encoding for the vectors
    dt : str or None
        If not None, determines the binsize the event stream is discretized into
    data_info_ : dict or None
        Dictionary containing further device information such as most likely value
        or device datatype. This is used to speed up internal computation.
    classes_ : list
        A list of all devices. The lists order corresponds to the device order of the
        transformed state-vectors.

    Examples
    --------
    >>> from pyadlml.dataset import fetch_amsterdam
    >>> data = fetch_amsterdam()
    >>> from pyadlml.preprocessing import StateVectorEncoder
    >>> sve = StateVectorEncoder(encode='raw')
    >>> X = sve.fit_transform(data.df_devices)
    >>> sve2 = StateVectorEncoder(encode='changepoint+raw', dt='6s')
    >>> X_upsampled = sve2.fit_transform(data.df_devices)

    """

    def __init__(self, encode=ENC_RAW, dt=None):
        self.encode = encode
        self.dt = dt
        self.data_info_ = None
        self.classes_ = []

    @classmethod
    def _is_valid_encoding(cls, encoding):
        from itertools import chain, permutations
        def helper(iterable):
            s = list(iterable)
            return chain.from_iterable(permutations(s, r) for r in range(len(s)+1))
        # generate all possible valid combinations
        valid_combos = ['+'.join(combo) for combo in helper(REPS)]
        return encoding in valid_combos

    def fit(self, df_devs, y=None):
        """
        Fit the estimator.

        Parameters
        ----------
        df_devs : pd.DataFrame, optional
            recorded devices from a dataset. For more information refer to
            :ref:`user guide<device_dataframe>`.
        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`~sklearn.pipeline.Pipeline`.

        Returns
        -------
        self
        """
        assert StateVectorEncoder._is_valid_encoding(self.encode)

        # create hashmap off all input features with mean for numerical
        # and most common value for binary or categorical features
        self.data_info_ = create_device_info_dict(df_devs)
        self.classes_ = self.data_info_.keys()
        return self

    def transform(self, df_devs=None,y=None, initial_states={}):
        """
        Discretize the data.

        Parameters
        ----------
        df_devs : array-like of shape (n_samples, n_features)
            The device dataframe to be transformed.
        y : None
            todo copy standard scipy sentence
        initial_states : dict
            A dictionary with device state mapping containing information about
            the last state the device held before the first event. If no dictionary 
            is given the states are infered by most likely values for 
            categorical and boolean devices.

        Returns
        -------
        Xt : {ndarray, sparse matrix}, dtype={np.float32, np.float64}
            Data in the binned space. Will be a sparse matrix if
            `self.encode='onehot'` and ndarray otherwise.
        """
        PRAEFIX_LF = 'lf_'
        PRAEFIX_CP = 'cp_'


        df_lst = []
        iters = self.encode.split('+')
        for enc in iters:
            if enc == ENC_RAW:
                data = create_raw(df_devs, self.data_info_, dev_pre_values=initial_states)
                if self.dt is not None:
                    data = resample_raw(data, df_dev=df_devs, dt=self.dt,
                                        most_likely_values=self.data_info_
                                        )

                # convert boolean data into integers (1,0)
                dev_bool = [dev for dev in self.data_info_.keys() if self.data_info_[dev]['dtype'] == 'boolean']
                data[dev_bool] = data[dev_bool].astype(int)

            elif enc == ENC_CP:
                data = create_changepoint(df_devs)
                if self.dt is not None:
                    data = resample_changepoint(data, self.dt)

                # set values that are missing in transform but were present when fitting to 0
                dev_diff = set(self.classes_) - set(data.columns)
                if len(dev_diff) > 0:
                    for dev in dev_diff:
                        data[dev] = 0

                # add prefix to make column names unique
                if len(iters) > 1:
                    data.columns = [TIME] + list(map(PRAEFIX_CP.__add__, data.columns[1:]))


            elif enc == ENC_LF:
                data = create_lastfired(df_devs)
                if self.dt is not None:
                    data = resample_last_fired(data, self.dt)

                # set values that are missing in transform but were present when fitting to 0
                dev_diff = set(self.classes_) - set(data.columns)
                if len(dev_diff) > 0:
                    for dev in dev_diff:
                        data[dev] = 0

                # add prefix to make column names unique
                if len(iters) > 1:
                    data.columns = [TIME] + list(map(PRAEFIX_LF.__add__, data.columns[1:]))

            else:
                raise ValueError
            data = data.set_index(TIME)
            df_lst.append(data)

        return pd.concat(df_lst, axis=1).reset_index()


    def fit_transform(self, df_devs, y=None):
        """

        Parameters
        ----------
        df_devs : pd.DataFrame, optional
            recorded devices from a dataset. For more information refer to
            :ref:`user guide<device_dataframe>`.
        y : None
            Ignored. This parameter exists only for compatibility with
            :class:`~sklearn.pipeline.Pipeline`.
        """
        self.fit(df_devs)
        return self.transform(df_devs)


class LabelMatcher(BaseEstimator, TransformerMixin, YTransformer):
    """
    Labels a dataframe with corresponding activities

    Attributes
    ----------
    idle : bool, default=False
        If true items that are not

    """
    def __init__(self, other : bool = False):
        """
        Parameters
        ----------
        other : bool, default=False
            The other activity TODO

        Returns
        -------
        self
        """
        self.other = other

    def fit(self, y, X):
        """
        Fit label encoder.

        Parameters
        ----------
        y : pd.DataFrame
            recorded activities from a dataset. Fore more information refer to the
            :ref:`user guide<activity_dataframe>`.

        Returns
        -------
        self : returns an instance of self
        """
        self.lbl_enc_ = preprocessing.LabelEncoder()
        self.df_acts_ = y

        # add actvities to sklearns LabelEncoder
        activities = list(y[ACTIVITY].values)
        if self.other:
            activities.append(OTHER)
        #self.lbl_enc_.fit(activities)
        #self.classes_ = self.lbl_enc_.classes_
        self.classes_ = activities
        return self


    def fit_transform(self, y, X):
        """
        Fit label encoder and return encoded labels.

        Parameters
        ----------
        y : pd.DataFrame
            An activity dataframe recorded activities from a dataset. Fore more information refer to the
            :ref:`user guide<activity_dataframe>`.
        X : pd.DataFrame
            A dataframe containing a column with name 'time' of timestamps.

        Returns
        ------
        df : pd.DataFrame
            The X dataframe with an additional column containing the corresponding activity labels
        """
        self.fit(y, X)
        return self.transform(y, X)

    def inverse_transform(self, y, retain_index=False):
        """
        Transform labels back to original encoding.

        Parameters
        ----------
        x : array like or pd.DataFrame or pd.Series
            array of numbers that are transformed to labels
        retain_index : bool, default=False
            TODO

        Returns
        -------
            TODO
        """
        if isinstance(y, int):
            # Case when a string is passed
            return self.id2class(y)
        elif self._is_iterable(y):
            # Iter through thing and replace values with encodings
            return self._wrap_iterable(list(map(self.id2class, y)), y)
        else:
            raise ValueError('Passed weird argument!!!')
        raise NotImplementedError
        #if isinstance(x, np.ndarray):
        #    res = self._lbl_enc.inverse_transform(x)
        #    if retain_index:
        #        return pd.Series(data=res, index=self.df_devs.index[:len(res)])
        #    else:
        #        return res
        #
        #elif isinstance(x, pd.DataFrame) or isinstance(x, pd.Series):
        #    tmp_index = x.index
        #    res = self._lbl_enc.inverse_transform(x.values)
        #    return pd.Series(data=res, index=tmp_index)
        #else:
        #    raise ValueError

    def id2class(self, y: int) -> str:
        """ Get class label corresponding to the numeric label.
        """
        return self.classes_[y]


    def class2id(self, y: str) -> int:
        """ Get numeric label from class label.
        """
        return np.argmax(self.classes_ == y)

        
    def _is_iterable(self, z):
        try:
            iter(z)
            return True
        except:
            return False


    def _wrap_iterable(self, lst, iter):
        """ list 
        """
        if isinstance(iter, np.ndarray):
            return np.array(lst)
        elif isinstance(iter, list):
            return lst
        elif isinstance(iter, list):
            return lst
        elif isinstance(iter, pd.Series):
            tmp = pd.Series(lst)
            tmp.index = iter.index
            return tmp
        else:
            raise NotImplementedError


    def transform(self, y: pd.DataFrame, X: pd.DataFrame = None) -> pd.DataFrame:
        """

        Parameters
        ----------
        y : pd.DataFrame
            An activity dataframe
        X : pd.DataFrame
            A device dataframe

        Returns
        -------
        pd.DataFrame
            A dataframe with column TIME, ACTIVITY matchin the rows of X
            TODO asdf
        """
        # normal case where X an y are provided
        if X is not None:
            return label_data(X, y, self.other)[[TIME, ACTIVITY]].copy()
            # remove Nans before encoding the labels and then concatenate again
            #if not self.other:
                #nan_mask = df[ACTIVITY].isna()
                #df_san_nan = df[~nan_mask]
                #encoded_labels = self.lbl_enc_.transform(df_san_nan[ACTIVITY].values)
                #new_san_nan = pd.DataFrame(data={TIME: df_san_nan[TIME].values, ACTIVITY: encoded_labels})
                #new_nans = pd.DataFrame(data={TIME: df[nan_mask][TIME].values, ACTIVITY: np.nan})
                #return pd.concat([new_nans, new_san_nan]).sort_values(by=TIME)
            #else:
                #encoded_labels = self.lbl_enc_.transform(df[ACTIVITY].values)
                #return pd.DataFrame(data={TIME: df[TIME].values, ACTIVITY: encoded_labels})
        else:

            if isinstance(y, str):
                # Case when a string is passed
                return self.class2id(y)
            elif self._is_iterable(y):
                # Iter through thing and replace values with encodings
                return self._wrap_iterable(list(map(self.class2id, y)), y)
            else:
                raise ValueError('Passed weird argument!!!')


class SequenceSlicer(TransformerMixin, XOrYTransformer):
    """ Slices a sequence into batches.

    Parameters
    ----------

    .. image:: ../_static/images/many_to_many.svg
       :height: 200px
       :width: 500 px
       :scale: 90%
       :alt: alternate text
       :align: center


    .. image:: ../_static/images/reps/image.svg
       :height: 200px
       :width: 500 px
       :scale: 80%
       :alt: alternate text
       :align: center


    Many-To-Many
    ^^^^^^^^^^^^

    To get *many-to-many* batches use the window size :math:`w` to split the data

    .. math::
        f(X_{N,K},y_{N}) \rightarrow (X_{W, N,K}, y_{W, N})

    In addition you can specify a stride.


    .. code:: python

        from pyadlml.preprocessing import SequenceDicer

        raw = StateVectorEncoder(encode='raw', t_res='10s')\
              .fit_transform(data.df_devices)
        labels = LabelEncoder().fit_transform(raw, data.df_activities)

        X = raw.values
        y = labels.values

        X, y = SequenceDicer(rep='many-to-many', window_length='5m')\
               .fit_transform(X, y)

    Many-To-One
    ^^^^^^^^^^^

    .. math::
        f(X_{N,K},y_{N}) \rightarrow (X_{W, N, K}, y_{N})


    .. code:: python

        from pyadlml.preprocessing import SequenceDicer

        raw = StateVectorEncoder(encode='raw', t_res='10s')\
              .fit_transform(data.df_devices)
        labels = LabelEncoder().fit_transform(raw, data.df_activities)

        X = raw.values
        y = labels.values

        X, y = SequenceDicer(rep='many-to-one', window_length='20s')\
               .fit_transform(X, y)

    """
    REP_M2M = 'many-to-many'
    REP_M2O = 'many-to-one'

    def __init__(self, rep='many-to-many', window_size=10, stride=1):
        TransformerMixin.__init__(self)
        XOrYTransformer.__init__(self)

        self.rep = rep
        self.window_size = window_size
        self.stride = stride

    def fit(self, X,y=None, **fit_params):
        # TODO not having this method throws an error ! dirty hack
        return self

    def fit_transform(self, X, y=None):
        """
        Parameters
        ----------
        X : nd.array
            Some kind of numpy array
        y : nd.array

        Returns
        -------
        x : nd.array
            todo
        y : nd.array
            todo
        """
        return self.transform(X, y)

    @XOrYTransformer.x_or_y_transform
    def transform(self, X=None, y=None):
        """

        """
        assert self.rep in [self.REP_M2M, self.REP_M2O]

        if X is not None:
            assert self.window_size < len(X)
            assert self.stride < len(X)

            X = self._transform_X(X)

        if y is not None:
            assert self.window_size < len(y)
            assert self.stride < len(y)

            y = self._transform_Y(y)

        return X, y

    def _calc_new_N(self, n_old):
        return int(np.floor((n_old-self.window_size)/self.stride)+1)

    def _transform_X(self, X):
        """

        """
        n_prime = self._calc_new_N(X.shape[0])
        new_shape =[n_prime, self.window_size, X.shape[1]]

        res = np.zeros(shape=new_shape, dtype='float32')
        if not isinstance(X, np.ndarray):
            import torch
            if isinstance(X, torch.Tensor):
                try:
                    res = torch.zeros(new_shape, dtype=torch.float32)
                except TypeError:
                    print('asdf')
            else:
                raise ValueError('X has to be either ndarray or of type torch tensor')

        for r, i in enumerate(range(0, n_prime*self.stride, self.stride)):
            res[r, :, :] = X[i: i+self.window_size, :]
        return res

    def _transform_Y(self, y):
        """


        """
        dtype = 'int64'
        if self.rep == self.REP_M2M:
            n_prime = self._calc_new_N(y.shape[0])
            new_shape = [n_prime, self.window_size]

            if isinstance(y, np.ndarray):
                res = np.zeros(shape=[n_prime, self.window_size], dtype=object)
                res = res.astype(dtype)
            else:
                import torch
                if isinstance(y, torch.Tensor):
                    res = torch.zeros(new_shape, dtype=torch.int64)
                else:
                    raise ValueError('X has to be either ndarray or of type torch tensor')

            for r, i in enumerate(range(0, n_prime*self.stride, self.stride)):
                res[r, :] = y[i: i+self.window_size]
            return res.squeeze()

        elif self.rep == self.REP_M2O:
            res = y[list(range(self.window_size-1, y.shape[0], self.stride))]
            if isinstance(y, np.ndarray):
                res = res.squeeze().astype(dtype)
                return res
            else:
                import torch
                raise NotImplementedError
                #return res
        else:
            raise ValueError
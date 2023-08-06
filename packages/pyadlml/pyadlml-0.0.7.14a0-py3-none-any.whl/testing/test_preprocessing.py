import sys
import unittest

import pathlib
working_directory = pathlib.Path().absolute()
script_directory = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(working_directory))

from pyadlml.dataset import set_data_home, DEVICE
from pyadlml.preprocessing import StateVectorEncoder

class TestPreprocessingBase(unittest.TestCase):
    __test__ = False


    def __init__(self, *args, **kwargs):
        self.data = None
        self.data_home = None
        self.fetch_method = None

        self.df_activity_attrs = []
        self.lst_activity_attrs = []

        super().__init__(*args, **kwargs)

    def _setUp(self):
        self.data = self.fetch_method(cache=True)

    def setUp(self):
        set_data_home(self.data_home)
        self._setUp()


    def _column_matches_devices(self, df_dev, x):
        l1 = df_dev[DEVICE].unique()
        l2 = list(x.columns[1:])
        return (set(l1) == set(l2)) & (len(l1) == len(l2))


    def test_state_vector_encoder(self):
        from pyadlml.preprocessing import StateVectorEncoder
        df_dev = self.data.df_devices

        # test state vector encoder
        sve = StateVectorEncoder(encode='raw')
        x = sve.fit_transform(df_dev)
        assert len(x) == len(df_dev)
        assert self._column_matches_devices(df_dev, x)
        # TODO test that all devices have same dtype as before the transformation

        sve = StateVectorEncoder(encode='changepoint')
        x = sve.fit_transform(df_dev)
        assert len(x) == len(self.data.df_devices)
        assert self._column_matches_devices(df_dev, x)
        # TODO test for dtypes x_i \in {0,1}

        sve = StateVectorEncoder(encode='last_fired')
        x = sve.fit_transform(df_dev)
        assert len(x) == len(self.data.df_devices)
        assert self._column_matches_devices(df_dev, x)
        # TODO test for dtypes x_i \in {0,1}


    def test_sve_timeslices(self):
        from pyadlml.preprocessing import StateVectorEncoder
        df_dev = self.data.df_devices

        t_res = '1h'
        # test state vector encoder
        sve = StateVectorEncoder(encode='raw', dt=t_res)
        x = sve.fit_transform(df_dev)

        sve = StateVectorEncoder(encode='changepoint', dt=t_res)
        x = sve.fit_transform(df_dev)

        sve = StateVectorEncoder(encode='last_fired', dt=t_res)
        x = sve.fit_transform(df_dev)

        t_res = '30s'
        # test state vector encoder
        sve = StateVectorEncoder(encode='raw', dt=t_res)
        x = sve.fit_transform(df_dev)

        sve = StateVectorEncoder(encode='changepoint', dt=t_res)
        x = sve.fit_transform(df_dev)

        sve = StateVectorEncoder(encode='last_fired', dt=t_res)
        x = sve.fit_transform(df_dev)
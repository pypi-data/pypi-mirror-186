import sys
import pathlib

from sklearn.neighbors import KernelDensity
from sklearn.svm import SVC

working_directory = pathlib.Path().absolute()
script_directory = pathlib.Path(__file__).parent.absolute()
sys.path.append(str(working_directory))
import unittest
from sklearn.ensemble import RandomForestClassifier
from pyadlml.dataset import set_data_home, load_act_assist, TIME
from pyadlml.pipeline import Pipeline
from pyadlml.preprocessing import StateVectorEncoder, LabelMatcher, DropTimeIndex
from pyadlml.model_selection import TimeSeriesSplit, LeaveKDayOutSplit, train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from pyadlml.dataset import fetch_amsterdam

SUBJECT_ADMIN_NAME = 'admin'


class TestCrossValidation(unittest.TestCase):
    def setUp(self):
        dataset_dir = str(script_directory) + '/datasets/partial_dataset'
        self.data = load_act_assist(dataset_dir, subjects=[SUBJECT_ADMIN_NAME])
        self.data.df_activities = self.data.df_activities_admin

    def test_ts_split(self):
        df = self.data.df_devices
        cv1 = TimeSeriesSplit(n_splits=3)
        cv2 = TimeSeriesSplit(n_splits=3, return_timestamp=True)

        # compare the two splits (indici based and timestamp based)
        for (train_idx, test_idx), (train_ts, test_ts) in zip(cv1.split(df),
                                                              cv2.split(df)):
            tmp1 = df.iloc[train_idx]
            train_sel = df[(train_ts[0] < df[TIME]) & (df[TIME] < train_ts[1])]
            assert tmp1.equals(train_sel)

            tmp2 = df.iloc[test_idx]
            test_sel = df[(test_ts[0] < df[TIME]) & (df[TIME] < test_ts[1])]
            assert tmp2.equals(test_sel)

        cv3 = TimeSeriesSplit(n_splits=3, temporal_split=True, return_timestamp=False)
        cv4 = TimeSeriesSplit(n_splits=3, temporal_split=True, return_timestamp=True)
        # compare the two splits (indici based and timestamp based)
        for (train_idx, test_idx), (train_ts, test_ts) in zip(cv3.split(df),
                                                              cv4.split(df)):
            tmp1 = df.iloc[train_idx]
            train_sel = df[(train_ts[0] < df[TIME]) & (df[TIME] < train_ts[1])]
            assert tmp1.equals(train_sel)

            tmp2 = df.iloc[test_idx]
            test_sel = df[(test_ts[0] < df[TIME]) & (df[TIME] < test_ts[1])]
            assert tmp2.equals(test_sel)



    def test_lkdo_split(self):
        cv = LeaveKDayOutSplit(k=1, n_splits=2)
        # todo do some asserts

    def test_train_test_split(self):
        x_train, x_test, y_train, y_test = train_test_split(
            self.data.df_devices,
            self.data.df_activities
        )
        # todo do some asserts

        x_train, x_test, y_train, y_test, rnd_day = train_test_split(
            self.data.df_devices,
            self.data.df_activities,
            return_day=True
        )
        # todo do some asserts

if __name__ == '__main__':
    unittest.main()
from pyadlml.dataset import fetch_kasteren_2010, set_data_home, \
    TIME, START_TIME, END_TIME, ACTIVITY, DEVICE
from pyadlml.dataset.stats.activities import coverage
from pyadlml.dataset.util import infer_dtypes, fetch_by_name, DATASET_STRINGS
import argparse

path = '/media/data/ml_datasets/pyadlml'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', type=str, default='amsterdam',
                        choices=DATASET_STRINGS,
                        help='Select an avaliable dataset.'
                        )
    args = parser.parse_args()

    # Setup data
    set_data_home(path)
    data = fetch_by_name(args.dataset)

    df_acts = data['activities']
    df_devs = data['devices']

    # Determine start and end_time
    start_time = min(df_devs[TIME].iloc[0], df_acts[START_TIME].iloc[0])
    end_time = max(df_devs[TIME].iloc[-1], df_acts[END_TIME].iloc[-1])

    # Compute activity statistics
    nr_activities = len(df_acts[ACTIVITY].unique())
    nr_activity_recordings = len(df_acts)

    # Compute device statistics
    nr_devices = len(df_devs[DEVICE].unique())
    nr_device_recordings = len(df_devs)
    dev_types = [k for k, v in infer_dtypes(df_devs).items() if len(v) > 0]


    act_cov_dp = coverage(df_acts, df_devs, datapoints=True)
    act_cov_time = coverage(df_acts, df_devs, datapoints=False)

    print(f'From:\t\t{start_time}')
    print(f'To:\t\t\t{end_time}')
    print(f'Activites:\t{nr_activities}/{nr_activity_recordings}')
    print(f'Devices:\t{nr_devices}/{nr_device_recordings}')
    print(f'DeviceType:\t{dev_types}')
    print(f'Coverage:\t{act_cov_time:.2f}/{act_cov_dp:.2f}')

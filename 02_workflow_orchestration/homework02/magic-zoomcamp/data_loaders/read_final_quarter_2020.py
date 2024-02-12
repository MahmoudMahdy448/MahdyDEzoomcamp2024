if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
import os


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    url_download = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/'
    year = 2020
    months = [10, 11, 12]

    #green_tripdata_{year}-{month}.csv.gz

    # reduces memory usage in pandas
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'RatecodeID':pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'ehail_fee': float,
        'improvement_surcharge':float,
        'total_amount': float,
        'payment_type': pd.Int64Dtype(),
        'trip_type': float,
        'congestion_surcharge':float
    }

    data = pd.DataFrame()
    for month in months:
        url = os.path.join(
            url_download,
            f"green_tripdata_{year}-{month}.csv.gz"
        )
        print(url)
        data_month = pd.read_csv(
            url, sep=',', compression='gzip', dtype=taxi_dtypes, 
            parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        )
        data = pd.concat([data, data_month], ignore_index=True)
        print(data.shape)
    return data


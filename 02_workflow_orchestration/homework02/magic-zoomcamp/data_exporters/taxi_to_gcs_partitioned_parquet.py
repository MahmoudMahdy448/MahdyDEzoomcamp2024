import pyarrow as pa
import pyarrow.parquet as pq
import os

#... other code

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/gcp_credentials.json'
bucket_name = 'mage-zoomcamp-mahdy'
project_id = 'nyc-tl-taxi'
table_name = 'nyc_taxi_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table, 
        root_path=root_path, 
        partition_cols=['tpep_pickup_date'], 
        filesystem=gcs)

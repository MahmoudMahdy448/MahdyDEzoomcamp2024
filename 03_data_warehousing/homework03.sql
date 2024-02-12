-- first we will create a pipeline using mage for loading our data into gcs using:
-- 1. a data loader py script which apending the parquet dataframe into one big parquet data frame
--2.  a data exporter py script which contains export_data_to_google_cloud_storage function,
-- the function's job is to declare the timestamps "lpep_dropoff_date and lpep_pickup_date", also the the gcs bucket name we're using and the object key variables. 
-- running the above pipeline gets our parquet data uploaded successfully into the the gcs bucket 

-- Next, we'll add the data to bigquery from gcs simply from the bigquery studio
--, after this we're ready to answer the below queries:

--Question 1. What is count of records for the 2022 Green Taxi Data?

SELECT count(*)  FROM `nyc-tl-taxi.green_taxi_data_2022.green_taxi`

--answer is 840402

--Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).

 CREATE OR REPLACE TABLE nyc-tl-taxi.green_taxi_data_2022.gt_non_partitoned AS SELECT * FROM nyc-tl-taxi.`green_taxi_data_2022.green_taxi`

--Question 2:
--Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
--What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

SELECT COUNT(DISTINCT PULocationID) AS TotalDistinctPULocationIDs FROM nyc-tl-taxi.green_taxi_data_2022.green_taxi;

SELECT COUNT(DISTINCT PULocationID) AS TotalDistinctPULocationIDs FROM nyc-tl-taxi.green_taxi_data_2022.gt_non_partitoned;

--Question 3:
--How many records have a fare_amount of 0?

select count(*) from `nyc-tl-taxi.green_taxi_data_2022.green_taxi`
where fare_amount = 0
--answer is 1622


-- Question 5:
-- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

-- Use the materialized table you created earlier in your from clause and note the estimated bytes.
-- Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed.
-- What are these values?
SELECT COUNT(DISTINCT PULocationID)  FROM nyc-tl-taxi.green_taxi_data_2022.gt_non_partitoned
WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30' --answer is: This query will process 12.82 MB when run.

SELECT COUNT(DISTINCT PULocationID)  FROM nyc-tl-taxi.green_taxi_data_2022.green_taxi
WHERE lpep_pickup_date BETWEEN '2022-06-01' AND '2022-06-30' --answer is: This query will process 0 MB when run.

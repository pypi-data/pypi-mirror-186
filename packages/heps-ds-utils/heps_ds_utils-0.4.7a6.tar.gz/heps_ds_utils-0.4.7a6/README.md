# Hepsiburada Data Science Utilities

This module includes utilities for Hepsiburada Data Science Team.

- Library is available via PyPi. 
- Library can be downloaded using pip as follows: `pip install heps-ds-utils`
- Existing library can be upgraded using pip as follows: `pip install heps-ds-utils --upgrade`

***
## Available Modules

1. Hive Operations

```python
from heps_ds_utils import HiveOperations

# A connection is needed to be generated in a specific runtime.
# There are 3 ways to set credentials for connection.

# 1) Instance try to set default credentials from Environment Variables.
hive_ds = HiveOperations()
hive_ds.connect_to_hive()

# 2) One can pass credentials to instance initiation to override default.
hive_ds = HiveOperations(HIVE_HOST="XXX", HIVE_PORT="YYY", HIVE_USER="ZZZ", HIVE_PASS="WWW", HADOOP_EDGE_HOST="QQQ")
hive_ds = HiveOperations(HIVE_USER="ZZZ", HIVE_PASS="WWW")
hive_ds.connect_to_hive()

# 3) One can change any of the credentials after initiation using appropriate attribute.
hive_ds = HiveOperations()
hive_ds.hive_username = 'XXX'
hive_ds.hive_password = 'YYY'
hive_ds.connect_to_hive()

# Execute an SQL query to retrieve data.
# Currently Implemented Types: DataFrame, Numpy Array, Dictionary, List.
SQL_QUERY = "SELECT * FROM {db}.{table}"
data, columns = hive_ds.execute_query(SQL_QUERY, return_type="dataframe", return_columns=False)

# Execute an SQL query to create and insert data into table.
SQL_QUERY = "INSERT INTO .."
hive_ds.create_insert_table(SQL_QUERY)

# Send Files to Hive and Create a Table with the Data.
# Currently DataFrame or Numpy Array can be sent to Hive.
# While sending Numpy Array columns have to be provided.
SQL_QUERY = "INSERT INTO .."
hive_ds.send_files_to_hive("{db}.{table}", data, columns=None)

# Close the connection at the end of the runtime.

hive_ds.disconnect_from_hive()

```

2. BigQuery Operations

```python
from heps_ds_utils import BigQueryOperations, execute_from_bq_file

# A connection is needed to be generated in a specific runtime.
# There are 3 ways to set credentials for connection.

# 1) Instance try to set default credentials from Environment Variables.
bq_ds = BigQueryOperations()

# 2) One can pass credentials to instance initiation to override default.
bq_ds = BigQueryOperations(gcp_key_path="/tmp/keys/ds_qos.json")

# Unlike HiveOperations, initiation creates a direct connection. Absence of
# credentials will throw an error.

# Execute an SQL query to retrieve data.
# Currently Implemented Types: DataFrame.
QUERY_STRING = """SELECT * FROM `[project_name].[dataset_name].[table_name]` LIMIT 20"""
data = bq_ds.execute_query(QUERY_STRING, return_type='dataframe')

# Create a Dataset in BigQuery.
bq_ds.create_new_dataset("example_dataset")

# Create a Table under a Dataset in BigQuery.
schema = [
    {"field_name": "id", "field_type": "INTEGER", "field_mode": "REQUIRED"},
    {"field_name": "first_name", "field_type": "STRING", "field_mode": "REQUIRED"},
    {"field_name": "last_name", "field_type": "STRING", "field_mode": "REQUIRED"},
    {"field_name": "email", "field_type": "STRING", "field_mode": "REQUIRED"},
    {"field_name": "gender", "field_type": "STRING", "field_mode": "REQUIRED"},
    {"field_name": "ip_address", "field_type": "STRING", "field_mode": "REQUIRED"}]

bq_ds.create_new_table(dataset='example_dataset', table_name='mock_data', schema=schema)

# Insert into an existing Table from Dataframe.
# Don't create and insert in the same runtime.
# Google throws an error when creation and insertion time is close.
bq_ds.insert_rows_into_existing_table(dataset='example_dataset', table='mock_data', data=df)

# Delete a Table.
bq_ds.delete_existing_table('example_dataset', 'mock_data')

# Delete a Dataset.
# Trying to delete a dataset consisting of tables will throw an error.
bq_ds.delete_existing_dataset('example_dataset')

# Load Dataframe As a Table. BigQuery will infer the data types.
bq_ds.load_data_to_table('example_dataset', 'mock_data', df, overwrite=False)

# To execute BQ commands sequentially from a BigQuery Script without a return statement !
execute_from_bq_file(bq_client=bq_ds, bq_file_path="tests/test_data/test_case_2.bq", verbose=True)

```

3. Logging Operations

```python
from heps_ds_utils import LoggingOperations

# A connection is needed to be generated in a specific runtime.
# There are 3 ways to set credentials for connection.

# 1) Instance try to set default credentials from Environment Variables.
logger_ds = LoggingOperations()

# 2) One can pass credentials to instance initiation to override default.
logger_ds = LoggingOperations(gcp_key_path="/tmp/keys/ds_qos.json")

# Unlike HiveOperations, initiation creates a direct connection. Absence of
# credentials will throw an error.


```

4. Bucket Operations

```python
from heps_ds_utils import BucketOperations

# A connection is needed to be generated in a specific runtime.
# There are 2 ways to set credentials for connection.

# 1) Instance try to set default credentials from Environment Variables.
bct_ds = BucketOperations()

# 2) One can pass credentials to instance initiation to override default.
bct_ds = BucketOperations(gcp_key_path="/tmp/keys/ds_qos.json")

# Unlike HiveOperations, initiation creates a direct connection. Absence of
# credentials will throw an error.

BUCKET_NAME = "bucket-name"

# Upload File using filepath.
# Blob name is the filepath you want the file to be under the bucket.
# Filepath is the path to the file you want to upload.
bct_ds.upload_from_filepath(BUCKET_NAME, "project_name/dev/data/output.csv", "data/output.csv")

# Upload File from memory data.
# If you want to save the data in memory to a file, you can use this function.
bct_ds.upload_from_memory(BUCKET_NAME, "project_name/dev/model/model.pkl", model)

# Download file from bucket to filepath.
bct_ds.download_to_filepath(BUCKET_NAME, "project_name/dev/data/sample.json", "data/sample.json")

# Download data from bucket to memory.
# If you want to save the data in a file to memory, you can use this function.
frame = bct_ds.download_to_memory(BUCKET_NAME, "project_name/dev/data/sample.csv", "dataframe")

# Delete file from bucket.
bct_ds.delete_file_from_bucket(BUCKET_NAME, "project_name/dev/data/sample.json")

# Create empty folder to bucket.
bct_ds.create_new_folders(BUCKET_NAME, "project_name/dev/data/")

OVERWRITE = True/False
# Download files from bucket recursively.
bct_ds.download_recursively(BUCKET_NAME, "path/to/blob", OVERWRITE, "local/destination/path")

# Upload files to bucket recursively
bct_ds.upload_recursively(BUCKET_NAME, "path/to/blob", OVERWRITE, "local/source/path")

# Check if blob already exists.
bct_ds.does_blob_exist(BUCKET_NAME, 'path/to/blob')

```

5. Elastic Operations
```python
from heps_ds_utils import ElasticOperations

# A connection is needed to be generated in a specific runtime.
# There are 2 ways to set credentials for connection.

# 1) Instance try to set default credentials from Environment Variables.
elastic_ds = ElasticOperations()

# 2) One can pass credentials to instance initiation to override default.
elastic_ds = ElasticOperations(ip="connetcion-ip", port="connection-port")

INDEX_NAME = "index-name"

# Get data count of index
count = elastic_ds.get_count(INDEX_NAME)

# Adjust read only parameter of the index.
# Prevent index from modifications.
elastic_ds.adjust_readonly(INDEX_NAME, True)

# Allow index to modifications
elastic_ds.adjust_readonly(INDEX_NAME, False)

# Recreate the index.
# Deletes the index and generates new one with same name.
elastic_ds.recreate_index(INDEX_NAME)

# Upload data to index.
# Example data
data = [{'field-name1' : ['0000', '0001', '0002'],
        'field-name2' : '2011-20-11'},
        {'field-name1' : ['0003', '0002', '0001', '0000'],
        'field-name2' : '2011-21-11'}]
elastic_ds.send_data_to_elastic(INDEX_NAME, data=data)

# Get data from the index.
# Currently Implemented Types: DataFrame.
data = elastic_ds.get_data_from_elastic(INDEX_NAME)

# Run custom search query at ElasticSearch.
# Implemented return methods: Hits-Hits (Default), Raw, Hits, Total, Value
result = elastic_ds.run_query(indexName=INDEX_NAME,
                               return_method="raw",
                               body={"query": {"match_all": {}}})
                            
```

6. Mongo Operations
```python
from heps_ds_utils import MongoOperations
# A connection is needed to be generated in a specific runtime.
# There are 2 ways to set credentials for connection.

# 1) One can pass connection string to instance initiation.
mongo_ds = MongoOperations(connection_string="connection-string")

# 2) One can pass ip and port credentials to instance initiation.
mongo_ds = MongoOperations(ip="connetcion-ip", port=int("connection-port"))

DATABASE_NAME = "database-name"
COLLECTION_NAME = "collection-name"

# Create database
database = mongo_ds.create_database(DATABASE_NAME)

# Create collection
collection = mongo_ds.create_collection(DATABASE_NAME, COLLECTION_NAME)

# Get database
database = mongo_ds.get_database(DATABASE_NAME)

# Get collection
collection = mongo_ds.get_collection(DATABASE_NAME, COLLECTION_NAME)

# Get document count of collection.
# filter parameter is optional
count = mongo_ds.get_count(DATABASE_NAME, COLLECTION_NAME, filter='filter')

# Find documents in collection
# filter, sort and limit parameters are optional.
# Currently Implemented Types: List of dictionaries, DataFrame
documents = mongo_ds.find_document(database_name=DATABASE_NAME,
                                   collection_name=COLLECTION_NAME,
                                   filter='filter',
                                   sort='sort',
                                   limit='limit')

# Insert Document
# Currently Implemented Types: Dictionary, Records (List of Dictionaries), DataFrame
mongo_ds.insert_document(database_name=DATABASE_NAME,
                        collection_name=COLLECTION_NAME,
                        data='data')

# Update Document
mongo_ds.update_document(database_name=DATABASE_NAME,
                         collection_name=COLLECTION_NAME,
                         filter='filter',
                         new_values='new-values')

# Delete Document
mongo_ds.delete_document(database_name=DATABASE_NAME,
                         collection_name=COLLECTION_NAME,
                         filter='filter')

# Drop Database
mongo_ds.drop_database(database_name=DATABASE_NAME)

# Drop Collection
mongo_ds.drop_collection(database_name=DATABASE_NAME,
                         collection_name=COLLECTION_NAME)
                         
```

Release Notes:

0.4.4:
- BigQueryOperations:
    - insert_rows_into_existing_table: insertion exception handling added.
    - insert_rows_into_existing_table: retry added. 
        - Put time between table creation and insertion.
    - execute_query: total_bytes_processed info added.
    - execute_query: max allowed total_bytes_processed set to 100GB.
    - execute_query: return_type=None for Queries w/o any return.
    - load_data_to_table: kwargs['overwrite'] is added.
        - load_data_to_table(..., overwrite=True) to overwrite to table.
        - load_data_to_table(..., overwrite=False) to append to table.
        - not passing overwrite kwarg will print a DeprecationWarning.
    - execute_from_bq_file: sequential execution of BigQuery commands from
    a file. It has its own parser. 
        - execute_from_bq_file(..., verbose=True) to print BigQuery commands to console.
        - execute_from_bq_file(..., verbose=False) not to print BigQuery commands to console.

0.4.5:
- LoggingOperations
    - Bug Fix in Authentication to GCP Logging !
- BigQueryOperations
    - Executing BQ files for different environments !

0.4.6:
- BigQueryOperations
    - BQ Parser bug fix !
    - BQ File Execution dependent queries
        - Some of the queries depends on the previous command executions. For these cases:
        dependent_queries is needed to be set to True !
        execute_from_bq_file(
            bq_ds,
            "tests/test_data/test_case_4.bq",
            verbose=True,
            config=configs,
            dependent_queries=True)
    - BQ Create Table Results in Empty Table Check Added!
        - Raises an error if CREATE TABLE ... SELECT AS ... query results in empty table.
        - This doesn't work in the case of dependent_queries=True !!!
    - 100GB limit is turned into a warning, which will not be displayed in prod env.
    - BQ Return Types Implemented (Numpy Array and Arrow Formats)
- LoggingOperations
    - protobuf dependency issue resolved!
- BucketOperations
    - upload_from_filepath function added.
    - upload_from_memory function added.
    - download_to_filepath function added.
    - download_to_memory function added.
    - delete_file_from_bucket function added.
    - create_new_folders function added.
    - delete_folder function added.

0.4.7
- ElasticOperations
    - create_client function added.
    - get_count function added.
    - set_max_result_window function added.
    - check_readonly function added.
    - nonreadonly function added.
    - readonly function added.
    - adjust_readonly function added.
    - create_index function added.
    - delete_index function added.
    - recreate_index function added.
    - send_data_to_elastic function added.
    - get_data_from_elastic function added.
    - run_query function added.
- MongoOperations
    - create_client function added.
    - show_databases function added.
    - show_collections function added.
    - create_database function added.
    - create_collection function added.
    - get_database function added.
    - get_collection function added.
    - get_count function added.
    - find_document function added.
    - insert_document function added.
    - update_document function added. 
    - delete_document function added.
    - drop_database function added.
    - drop_collection function added.
- BigQueryOperations
    - execute_query: return_type="records" (list of dictionaries) implemented.
    - Different Region connection implemented.
- HiveOperations
    - MAJOR UPDATE: HiveOperations are now in extras.
    - If you want to install extra hive dependencies 
    - poetry add heps-ds-utils=^0.4.7a3 -extras hive
- BucketOperations
    - upload_from_filepath: uploaded file and source file size check added.
    - download_to_filepath: zip extraction added.
    - download_recursively function added.
    - upload_recursively function added.
    - does_blob_exist function added.

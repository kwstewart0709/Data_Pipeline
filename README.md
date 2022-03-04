# Data_Pipeline

# Built a batch processing pipeline that ingest home sales data to be ingested and analyzed each month.

# This pipeline is uses csv files that are stored in buckets in Amazon S3. The data is then uploaded into a Jupyter notebook via python boto3. The data is ingested from s3 to the jupyter notebook as a csv file. The csv file is then opened and read as a dataframe. I then condensed the dataframe to run simple queries on a smaller dataset. I viewed the data graphically. From there I installed sqlalchemy to create a database to open in sqlite. After creating the database I created a table called homesales to perform transformations in SQlite3. 

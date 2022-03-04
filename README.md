Data_Pipeline

Built a batch processing pipeline that ingest home sales data to be ingested and analyzed each month.

Project Description:

 This pipeline is uses csv files that are stored in buckets in Amazon S3. The data is then uploaded into a Jupyter notebook via python boto3. The data is ingested from s3 to the jupyter notebook as a csv file. The csv file is then opened and read as a dataframe. I then condensed the dataframe to run simple queries on a smaller dataset. I viewed the data graphically. From there I installed sqlalchemy to create a database to open in sqlite. After creating the database I created a table called homesales to perform transformations in SQlite3. 

Partner(s)/Contributor(s)
• Kevin Stewart

Methods and Models Used

• Amazon Web Servi

Technologies

• Python, AWS, Sqlite3, S3, Pandas

Project Description

Predict who would take H1N1 vaccinations based on socio-economic factors such as employment, race, educataion etc. The goal is to determine the likelihood that an individual would take a vaccination. The data set is based off a 2009 survey taking in regards to the H1N1 flu.

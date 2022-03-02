#!/usr/bin/env python
# coding: utf-8

# In[236]:


import boto3
import configparser
from datetime import date
from venv import create
from matplotlib.pyplot import table
# Importing packages needed 
import pandas as pd
from sklearn import pipeline
from sqlalchemy import VARCHAR
print("Data Pipline")
import os
import numpy as np
import configparser
import sys


# # Process needed installs needed to build pipeline

# In[15]:


pip install s3fs


# In[16]:


import psycopg2 as db


# In[17]:


pip install fsspec==2022.02.0


# In[18]:


pip install touch


# In[19]:


pip install botocore


# # Install AWS Command line Interface

# In[20]:


pip install awscli


# ## Install configure  and botocore

# In[21]:


pip install configure


# In[237]:


pip install botocore


# # Import data from Amazon S3 into python to do data transformation.

# In[23]:


client = boto3.client('s3')


# In[24]:


path = 's3://mod7-pipeline/raw_sales.csv'


# In[25]:


path


# In[26]:


df = pd.read_csv(path)


# In[27]:


df = pd.read_csv(path)


# In[238]:


df.head(10)


# # Creating a condensed dataframe to import into SQLite

# In[234]:


db_1 = df[['price', 'bedrooms', 'propertyType']]


# In[235]:


db_1


# # Import visualization packages to view data

# In[29]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[30]:


sns.barplot(y='price', x ='bedrooms', data=df);


# In[31]:


sns.barplot(y='price', x ='propertyType', data=df);


# ## Connect Jupyter notebook dataframe to SQlite to begin running sql queries for transformation

# In[231]:


pip install sqlalchemy


# In[232]:


# import create engine to connect with sqlite3
from sqlalchemy import create_engine


# In[233]:


# View first five rows of data
df.head()


# In[225]:


#creating a file to import into sqlite3 
engine = create_engine('sqlite:///df.db', echo=True)
sqlite_connection = engine.connect()


# In[228]:


#Creating a table to perform transformation
sqlite_table = 'salesdata1'
db_1.to_sql(sqlite_table, sqlite_connection, if_exists='fail')


# In[214]:


#creating a file to import into sqlite3 
engine = create_engine('sqlite:///db_1.db', echo=True)
sqlite_connection = engine.connect()


# In[215]:


# Send pandas dataframe from redshift to sqlite3 for transformation
sqlite_table = 'homesales'
db_1.to_sql(sqlite_table, sqlite_connection, if_exists='fail')


# In[239]:


# Close the  database conneciton 
sqlite_connection.close()


# In[ ]:





# In[ ]:





# In[ ]:





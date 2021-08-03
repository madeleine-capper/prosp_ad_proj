#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


import re


# In[6]:


data_arr = []
with open('webservertrafficlog/access.log') as log:
    for line in log.readlines():
        match = re.match(r'(.+) - - \[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\] \"(\w+) .+', line)
        if match:
            data_arr.append([match.group(1), match.group(2), match.group(3)])

data = pd.DataFrame(data_arr, columns=['ip_address', 'datetime', 'request_type'])


# In[7]:


data


# In[8]:


#Convert string datetime to Timestamp

data['datetime'] = data.datetime.apply(lambda x: x.replace('Jan', '01'))
data['datetime'] = pd.to_datetime(data.datetime, format='%d/%m/%Y:%H:%M:%S')


# In[9]:


#add datetime columns to group by

data['day'] = data['datetime'].apply(lambda x: x.day)
data['hour'] = data['datetime'].apply(lambda x: x.hour)
data['minute'] = data['datetime'].apply(lambda x: x.minute)


# In[10]:


#aggregate by minute and by hour

aggByMin = data.groupby(['day', 'hour', 'minute'], as_index=False).agg('count')  .rename({'ip_address': 'count'}, axis=1).drop(['datetime', 'request_type'], axis=1)

aggByHour = data.groupby(['day', 'hour'], as_index=False).agg('count')  .rename({'ip_address': 'count'}, axis=1).drop(['datetime', 'request_type', 'minute'], axis=1)


# In[11]:


data.to_csv('cleaned_log.csv')


# In[12]:


data.info()


# In[ ]:





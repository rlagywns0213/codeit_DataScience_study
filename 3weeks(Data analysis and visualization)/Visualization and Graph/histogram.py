#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[6]:


df = pd.read_csv('body.csv', index_col=0)
df.head(10)


# In[7]:


df.plot(kind='hist', y='Height')


# In[11]:


df.plot(kind='hist', y='Height', bins=15)


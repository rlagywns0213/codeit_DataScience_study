#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd


# In[3]:


df = pd.read_csv('broadcast.csv', index_col=0)
df


# In[5]:


df.loc[2017].plot(kind='pie')


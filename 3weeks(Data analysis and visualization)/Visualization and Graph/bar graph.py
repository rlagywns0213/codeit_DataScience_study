#!/usr/bin/env python
# coding: utf-8

# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')
    
import pandas as pd


# In[25]:


df = pd.read_csv('sports.csv', index_col=0)
df


# In[28]:


df.plot(kind = 'bar')


# In[30]:


#가로
df.plot(kind = 'barh')


# In[32]:


df.plot(kind = 'bar', stacked=True)


# In[34]:


#여성만을 대상으로 한 막대그래프
df['Female'].plot(kind='bar')


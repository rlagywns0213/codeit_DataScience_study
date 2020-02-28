#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[5]:


df = pd.read_csv('broadcast.csv', index_col=0)
df


# In[21]:


df.plot(y = ['KBS','JTBC'])


# In[16]:


df[['KBS','JTBC']].plot()


# In[19]:


#SERIES 에도 그래프 잘 나옴
df['KBS'].plot()


# 

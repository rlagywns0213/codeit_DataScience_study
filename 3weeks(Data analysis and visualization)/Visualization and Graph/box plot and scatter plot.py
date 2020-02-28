#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[3]:


df= pd.read_csv('exam.csv')
df


# In[6]:


df['math score'].describe()


# In[8]:


df.plot(kind='box', y='math score')


# In[12]:


df.plot(kind='box', y=['math score', 'reading score', 'writing score'])


# 산점도

# In[15]:


df.plot(kind='scatter', x='math score', y='reading score')


# In[17]:


df.plot(kind='scatter', x='math score', y='writing score')


# In[18]:


df.plot(kind='scatter', x='writing score', y='reading score')


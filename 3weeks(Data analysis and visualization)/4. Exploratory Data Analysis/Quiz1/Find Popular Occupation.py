#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 여성분들이 가장 많이 종사하고 있는 직종이 무엇인지 파악해 보세요.


# In[2]:


import pandas as pd
import seaborn as sns


# In[6]:


df = pd.read_csv('occupations.csv')
df


# In[13]:


womden = df[df['gender']=='F']


# In[18]:


womden['occupation'].value_counts().sort_values(ascending=False)


# In[23]:


#1. 여성분들이 가장 많이 종사하고 있는 직종이 무엇인지 파악해 보세요.
men = df[df['gender']=='M']
men


# In[25]:


men['occupation'].value_counts().sort_values(ascending=False)


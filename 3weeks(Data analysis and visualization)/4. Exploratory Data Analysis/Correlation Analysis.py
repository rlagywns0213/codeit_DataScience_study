#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[4]:


df = pd.read_csv('young_survey.csv')
df.head()


# In[8]:


music = df.iloc[:,:19]
music.head()


# In[10]:


sns.heatmap(music.corr())


# In[32]:


df.corr()['Age'].sort_values(ascending=False)                                           


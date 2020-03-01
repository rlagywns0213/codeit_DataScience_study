#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[3]:


df = pd.read_csv('young_survey.csv')
df.head()


# In[6]:


interests = df.loc[:,'History' : 'Pets']
interests


# In[9]:


corr = interests.corr()
corr['History'].sort_values(ascending =False)


# In[12]:


sns.clustermap(corr)


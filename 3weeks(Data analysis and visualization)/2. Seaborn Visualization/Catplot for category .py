#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


laptops_df = pd.read_csv('laptops.csv')
laptops_df.head()


# In[5]:


laptops_df['os'].unique()


# In[8]:


#카테고리별
sns.catplot(data=laptops_df, x='os', y='price', kind='box')
#각 데이터가 몇개씩 있는지 모름


# In[10]:


sns.catplot(data=laptops_df, x='os', y='price', kind='violin')
#각 데이터가 몇개씩 있는지 모름


# In[12]:


#각 데이터가 몇개 있는지 표현
sns.catplot(data=laptops_df, x='os', y='price', kind='strip')


# In[14]:


laptops_df['processor_brand'].unique()


# In[16]:


#hue 브랜드별로 색깔 나타내줌
sns.catplot(data=laptops_df, x='os', y='price', kind='strip', hue='processor_brand')


# In[17]:


#점들 겹쳐져보이는거 해결해줌
sns.catplot(data=laptops_df, x='os', y='price', kind='swarm', hue='processor_brand')


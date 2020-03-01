#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns


# In[5]:


df = pd.read_csv('young_survey.csv')
df.head()


# In[7]:


basic_info = df.iloc[:,140:]
basic_info.head()


# In[9]:


basic_info.describe()


# In[11]:


basic_info['Gender'].value_counts()


# In[13]:


basic_info['Handedness'].value_counts()


# In[15]:


basic_info['Education'].value_counts()


# In[22]:


sns.violinplot(data=basic_info, y= 'Age')
#10대후반에서 20대 초반의 젊은 사람들 대다수


# In[25]:


sns.violinplot(data=basic_info, x= 'Gender', y= 'Age')


# In[27]:


sns.violinplot(data=basic_info, x= 'Gender', y= 'Age', hue='Handedness')
#


# In[29]:


sns.jointplot(data=basic_info, x='Height', y= 'Weight')
#


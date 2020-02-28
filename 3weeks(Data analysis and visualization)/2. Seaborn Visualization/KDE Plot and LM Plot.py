#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install seaborn==0.9.0')


# In[3]:


import pandas as pd
import seaborn as sns


# In[6]:


body_df = pd.read_csv('body.csv', index_col=0)
body_df.head()


# In[15]:


body_df['Height'].value_counts().sort_index().plot()


# In[24]:


#bw 파라미터 : 추측을 어느정도 수준으로 할지 설정
sns.kdeplot(body_df['Height'], bw=0.5)


# **활용

# In[26]:


body_df.plot(kind='hist', y='Height', bins =15)


# In[29]:


#히스토그램 + KDE
sns.distplot(body_df['Height'],bins=15)


# In[30]:


body_df.plot(kind='box', y='Height')


# In[32]:


#kde 그래프 2개가 누워있는것같음
#분포 전체를 보여주며 시각적으로 근사함
sns.violinplot(y=body_df['Height'])


# In[34]:


body_df.plot(kind='scatter', x='Height', y='Weight')


# In[36]:


#등고선 3차원으로 그린 것
#선이 가까울수록 가파르고 멀수록 평평한것
sns.kdeplot(body_df['Height'], body_df['Weight'])


# In[38]:


sns.kdeplot(body_df['Height'])


# In[40]:


sns.kdeplot(body_df['Weight'])


# LM Plot

# In[41]:


#회귀선 + 산점도 나옴
sns.lmplot(data=body_df, x='Height', y='Weight')


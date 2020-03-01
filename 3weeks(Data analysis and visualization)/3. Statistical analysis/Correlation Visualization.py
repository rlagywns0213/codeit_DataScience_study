#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import seaborn as sns
df = pd.read_csv('exam.csv')

df.corr()


# In[7]:


#상관계수 시각화 : heatmap 메소드
sns.heatmap(df.corr(), annot = True)
#색이 밝을수록 상관계수가 더 높다


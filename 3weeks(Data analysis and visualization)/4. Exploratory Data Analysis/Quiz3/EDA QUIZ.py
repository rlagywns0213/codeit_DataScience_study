#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''생존 여부는 'Survived' column에 저장되어 있습니다. 0이 사망, 1이 생존을 의미합니다.
좌석 등급은 'Pclass' column에 저장되어 있습니다. 1은 1등실, 2는 2등실, 3은 3등실을 의미합니다.
지불한 요금은 'Fare' column에 저장되어 있습니다.

다양한 방면으로 EDA(탐색적 데이터 분석)를 한 후, 다음 보기 중 맞는 것을 모두 고르세요.


1
타이타닉의 승객은 30대와 40대가 가장 많다.

2
가장 높은 요금을 낸 사람은 30대이다.

3
생존자가 사망자보다 더 많다.

4
1등실, 2등실, 3등실 중 가장 많은 사람이 탑승한 곳은 3등실이다.

5
가장 생존율이 높은 객실 등급은 1등실이다.

6
나이가 어릴수록 생존율이 높다.

7
나이보다 성별이 생존율에 더 많은 영향을 미친다.'''


# In[73]:


import pandas as pd
import seaborn as sns

df= pd.read_csv('titanic.csv')
#1
df.plot(kind='hist', y='Age', bins= 30)


# In[37]:


#2
df.plot(kind='scatter', x='Age', y='Fare')


# In[40]:


#3
df['Survived'].value_counts()


# In[42]:


#4
df['Pclass'].value_counts()


# In[56]:


#5
sns.kdeplot(df['Pclass'], df['Survived'])


# In[66]:


#6
sns.violinplot(data=df, x='Survived',y='Age')


# In[77]:


#9
sns.stripplot(data=df, x="Survived", y="Age", hue="Sex")


# In[78]:



sns.catplot(data=df, x="Survived", y="Age", hue="Sex")


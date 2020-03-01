#!/usr/bin/env python
# coding: utf-8

# In[31]:


#일찍 일어나는 사람들이 좋아할 만한 음악이 무엇인지 분석해 보려고 합니다.
import pandas as pd
df= pd.read_csv('young_survey.csv')
df.corr()['Getting up'][1:19].sort_values(ascending=True)


# In[26]:


'''
경영학과 3학년이 된 영준이는 스타트업을 준비하고 있습니다.
사업 아이템을 고민하면서, 나름대로 가설을 몇 개 세워봤습니다.


악기를 다루는 사람들은 시 쓰기를 좋아하는 경향이 있을 것이다.
외모에 돈을 많이 투자하는 사람들은 브랜드 의류를 선호할 것이다.
메모를 자주 하는 사람들은 새로운 환경에 쉽게 적응할 것이다.
워커홀릭들은 건강한 음식을 먹으려는 경향이 있을 것이다.

이 내용을 사업 아이템으로 확장하기 전에, 데이터를 통해 가설을 검증해보려고 하는데요.  
설문조사 데이터(다운로드)를 바탕으로, 가장 가능성이 낮은 가설을 골라보세요.


이 가설과 관련이 있는 column은 다음과 같습니다.


Branded clothing: 나는 브랜드가 없는 옷보다 브랜드가 있는 옷을 선호한다.
Healthy eating: 나는 건강하거나 품질이 좋은 음식에는 기쁘게 돈을 더 낼 수 있다.
Musical instruments: 나는 악기 연주에 관심이 많다.
New environment: 나는 새 환경에 잘 적응하는 편이다.
Prioritising workload: 나는 일을 미루지 않고 즉시 해결해버리려고 한다.
Spending on looks: 나는 내 외모에 돈을 많이 쓴다.
Workaholism: 나는 여가 시간에 공부나 일을 자주 한다.
Writing: 나는 시 쓰기에 관심이 많다.
Writing notes: 나는 항상 메모를 한다.
'''


# In[38]:


print(df.corr()['Writing']['Musical instruments'])
print(df.corr()['Spending on looks']['Branded clothing'])
print(df.corr()['Writing notes']['New environment'])
print(df.corr()['Workaholism']['Healthy eating'])


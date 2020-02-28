'''
실리콘 밸리에서 일하는 남자 관리자 (Managers)에 대한 인종 분포를 막대 그래프로 다음과 같이 그려보세요.
'''

%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')

# 코드를 작성하세요.
condition1 = df['gender'] =='Male'
condition2 = df['job_category'] =='Managers'
#race_ethnicity 가 all인 경우는 제외
condition3 = df['race_ethnicity'] !='All'
df[condition1 & condition2 &condition3].plot(x='race_ethnicity', y='count', kind='bar')
'''어도비(Adobe)의 직원 분포를 한번 살펴봅시다.
어도비 전체 직원들의 직군 분포를 파이 그래프로 그려보세요.
(인원이 0인 직군은 그래프에 표시되지 않아야 합니다.)'''

%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 코드를 작성하세요.
condition1 = df['count'] !=0
condition2 = df['company']=='Adobe'
condition3 = df['race'] == 'Overall_totals'
condition4 = (df['job_category'] !='Totals') & (df['job_category'] !='Previous_totals')
#중요 x축을 job_category로 index해주는 것
final = df[condition1&condition2&condition3&condition4].set_index('job_category')
#출력
final.plot(kind='pie', x= 'job_category',y='count')
'''이번에는 여자 비율이 높은 직업과, 남자 비율이 높은 직업이 무엇인지 궁금한데요.


groupby 문법을 사용해서 '여성 비율'이 높은 순으로 직업을 나열해 보세요.


DataFrame이 아닌 Series로, 'gender'에 대한 값만 아래와 같이 출력되어야 합니다.
'''

import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.
occupation_group = df.groupby('occupation')
# 성별이 'M', 'F' 에서 > 0, 1 로 인덱싱 : 비율을 구하기 위해서!!
df.loc[df['gender'] == 'M', 'gender'] =0
df.loc[df['gender'] == 'F', 'gender'] =1 
occupation_group.mean()['gender'].sort_values(ascending =False)
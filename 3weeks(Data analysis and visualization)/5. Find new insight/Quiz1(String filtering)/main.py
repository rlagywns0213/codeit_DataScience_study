import pandas as pd

df = pd.read_csv('data/museum_1.csv')

# 코드를 작성하세요.
a= df['시설명'].str.contains('대학')
df.loc[a==True, '분류']= '대학'
df.loc[a==False, '분류']= '일반'
df
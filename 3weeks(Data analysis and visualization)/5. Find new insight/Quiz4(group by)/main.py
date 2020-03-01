import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.
a= df.groupby('occupation')
a.mean().sort_values(by='age')
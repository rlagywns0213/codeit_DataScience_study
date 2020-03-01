import pandas as pd

df = pd.read_csv('data/museum_2.csv')

# 코드를 작성하세요.
a = df['운영기관전화번호'].str.split("-",n=1, expand = True)
df["지역번호"] = a[0]
df
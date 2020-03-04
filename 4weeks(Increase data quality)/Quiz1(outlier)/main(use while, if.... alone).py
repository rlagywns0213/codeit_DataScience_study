%matplotlib inline
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
q1 = df['budget'].quantile(0.25)
q3 = df['budget'].quantile(0.75)
iqr = q3 - q1
condition = df['budget'] > q3+ 5*iqr
i =0
while i < 5042:
    i += 1
    if condition[i] == True: 
        df.drop(i, inplace = True)
        
df.plot(kind='scatter' , x='budget', y='imdb_score')
%matplotlib inline
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
drop_index = df['budget'].sort_values(ascending= False).head(15).index
df.drop(drop_index, inplace=True)
df.plot(kind='scatter', x= 'budget', y='imdb_score')
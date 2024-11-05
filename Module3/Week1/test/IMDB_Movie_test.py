import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Module3.Week1.model.IMDB_Movie import rating_group

path = '../dataset/IMDB-Movie-Data.csv'

# Read dataset from .csv file
data = pd.read_csv(path)
# Read dataset with specified explicit index .
# We will use this later in our analysis
data_indexed = pd.read_csv(path, index_col="Title")
print(data.head())
print(data.info())

# Extract dataset as series
genre = data['Genre']
print(genre)
# Extract dataset as dataframe
print(data[['Genre']])

some_cols = data[['Title', 'Genre', 'Actors', 'Director', 'Rating']]
print(data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']])
print(data[((data['Year'] >= 2010) & (data['Year'] <= 2015)) & (data['Rating'] < 6.0) & (
        data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])

print(data.groupby('Director')[['Rating']].mean().head())
print(data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending=False).head())
print(data.isnull().sum())

# Use drop function to drop columns
data.drop('Metascore', axis=1).head()
data.dropna()

revenue_mean = data_indexed['Revenue (Millions)'].mean()
print("The mean revenue is: ", revenue_mean)
# We can fill the null values with this mean revenue
data_indexed['Revenue (Millions)'].fillna(revenue_mean, inplace=True)

# Lets apply this function on our movies dataset
# creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)
data[['Title', 'Director', 'Rating', 'Rating_category']].head(5)

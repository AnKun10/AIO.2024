from Module2.Week4.model.text_retrieval import *
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Ex 10
vi_data_df = pd.read_csv("../dataset/vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
print(context_embedded.toarray()[7][0])

# Ex 11
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(results[0]['cosine_score'])

# Ex 12
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(results[1]['corr_score'])

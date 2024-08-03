from Module2.Week4.model.statistics import compute_correlation_coefficient
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    # lowercasing before encoding
    question = question.lower()
    query_embedded = tfidf_vectorizer.transform([question])
    cosine_scores = cosine_similarity(context_embedded, query_embedded)
    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[- top_d:][:: -1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]}
        results.append(doc_score)
    return results


def corr_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    # lowercasing before encoding
    question = question.lower()
    query_embedded = tfidf_vectorizer.transform([question])
    query_vector = query_embedded.toarray().flatten()
    context_vectors = context_embedded.toarray()
    corr_scores = np.array([np.corrcoef(query_vector, doc_vector)[0, 1] for doc_vector in context_vectors])
    # Get top k correlation score and index its
    results = []
    for idx in corr_scores.argsort()[- top_d:][:: -1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results

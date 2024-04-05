# utils/keyword_extraction.py

from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(texts, top_n=10):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the texts
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Get the feature names (keywords)
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the top keywords for each document
    top_keywords = []
    for doc in tfidf_matrix:
        top_indices = doc.toarray()[0].argsort()[-top_n:][::-1]
        top_keywords.append([feature_names[i] for i in top_indices])
    
    return top_keywords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TEDRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df = self.df[['title', 'description', 'url']].dropna()
        self.df.reset_index(drop=True, inplace=True)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['description'])

    def recommend(self, input_text, top_n=5):
        input_vec = self.vectorizer.transform([input_text])
        cosine_similarities = cosine_similarity(input_vec, self.tfidf_matrix).flatten()
        indices = cosine_similarities.argsort()[-top_n:][::-1]
        recommendations = self.df.iloc[indices]
        return recommendations[['title', 'url']]
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MarkingSystem:
    @staticmethod
    def mark_description(description: str, markers: [(int, str)]) -> [int]:
        descriptions = [description] + [marker[1] for marker in markers]

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(descriptions)

        cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        relevant_indices = np.argwhere(cosine_similarities > 0.1).flatten()

        tags = [markers[index][0] for index in relevant_indices]

        return tags

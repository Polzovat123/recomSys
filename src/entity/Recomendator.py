import fasttext
import fasttext.util
import numpy as np
from scipy import spatial

from src.entity.course import Course


class RecommendFasttextEfanna:
    def __init__(self, path=r'D:\Projects\pythonProject\recomSys\source\models\course_finding\model\model.bin'):
        self.description_emb_model = fasttext.load_model(path)

    def embed_description_course(self, description):
        sentense = self.description_emb_model.get_sentence_vector(description)
        return sentense

    def get_medium_interest(self, interest):
        summed_vector = np.sum(interest, axis=0)
        mean_interest = summed_vector / np.linalg.norm(summed_vector)
        return mean_interest

    def is_recommend(self, better_course, optional_course, treshold=0.3):
        coeff_similarity = spatial.distance.cosine(better_course, optional_course)
        if treshold < coeff_similarity:
            return True
        return False
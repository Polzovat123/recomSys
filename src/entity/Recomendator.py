import fasttext
import fasttext.util
from scipy import spatial

from src.entity.course import Course


class RecommendFasttextEfanna:
    def __init__(self, path='/model.bin'):
        self.description_emb_model = fasttext.load_model(path)

    def embed_description_course(self, description):
        sentense = self.description_emb_model.get_sentence_vector(description)
        return sentense

    def is_recommend(self, better_course, optional_course, treshold=0.3):
        coeff_similarity = spatial.distance.cosine(better_course, optional_course)
        if treshold < coeff_similarity:
            return True
        return False
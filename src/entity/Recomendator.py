import fasttext
import fasttext.util
from scipy import spatial

from src.entity.course import Course


class RecommendFasttextEfanna:
    def __init__(self, path=r'D:\Projects\pythonProject\recomSys\source\models\course_finding\model\model.bin'):
        self.description_emb_model = fasttext.load_model(path)

    def embed_description_course(self, description):
        print(description)
        sentense = self.description_emb_model.get_sentence_vector(description)
        print(sentense)
        return sentense

    def is_recommend(self, better_course, optional_course, treshold=0.3):
        coeff_similarity = spatial.distance.cosine(better_course, optional_course)
        if treshold < coeff_similarity:
            return True
        return False


if __name__ == "__main__":
    fasttext.util.download_model('en', if_exists='ignore')
    ft = fasttext.load_model('../../source/models/course_finding/model/cc.en.300.bin')
    ft.save_model("model.bin")
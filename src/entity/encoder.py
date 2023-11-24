from src.entity.course import Course


class EcnoderModel:
    @staticmethod
    def encode_course(course: Course):
        embeding = []
        embeding.append(course.score)
        embeding.extend(course.description)

        return embeding
from typing import List

from pydantic import BaseModel


class RequestRecommendation(BaseModel):
    id_user: str
    size_pool: int


class FindCourse(BaseModel):
    id_course: str


class Recommendation(BaseModel):
    courses: List[FindCourse]


class RequestEncodeDescription(BaseModel):
    description: str
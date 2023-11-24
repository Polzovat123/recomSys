from fastapi import APIRouter, HTTPException

from src.adapters.db_worker import DBworker
from src.adapters.json_parse import JSONAdapter
from src.application.additional_routes.recomendadtion_course.model import Recommendation, RequestRecommendation, \
    RequestEncodeDescription
from src.entity.Recomendator import RecommendFasttextEfanna

router = APIRouter(
    prefix='/course'
)


@router.get("/")
async def read_root():
    return {"message": "Closest ID course"}


@router.post("/encode_course")
async def encode_course(request: RequestEncodeDescription):
    try:
        msg = JSONAdapter().parse_request_enc_description(request)
        enc_msg = RecommendFasttextEfanna().embed_description_course(msg)

        return {
            "sucsessfull": True,
            "description": list(enc_msg.tolist())
        }
    except BaseException as e:
        return HTTPException(status_code=500, detail=str(e))


@router.post("/find_best_courses", response_model=Recommendation)
async def recommend_courses(request: RequestRecommendation):
    user, size_pool = JSONAdapter.parse_request_recommendation(request)

    preferense_courses = DBworker.get_best_course(user, get=1)
    best_200_course = DBworker.get_course()

    rkm = RecommendFasttextEfanna()

    try:
        mean_interest = rkm.get_medium_interest(preferense_courses)
        recommend_course = []
        for course in best_200_course:
            if rkm.is_recommend(course.description, mean_interest):
                recommend_course.append(course)

        return {
            "sucsessfull": True,
            "description": list(recommend_course)
        }
    except BaseException as e:
        return HTTPException(status_code=500, detail=str(e))


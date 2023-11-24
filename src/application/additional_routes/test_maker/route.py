from fastapi import APIRouter, HTTPException

from src.adapters.db_worker import DBworker
from src.adapters.json_parse import JSONAdapter
from src.application.additional_routes.recomendadtion_course.model import Recommendation, RequestRecommendation, \
    RequestEncodeDescription
from src.entity.Recomendator import RecommendFasttextEfanna

router = APIRouter(
    prefix='/test_maker'
)


@router.get("/")
async def read_root():
    return {"message": "Help creation test by lesson"}


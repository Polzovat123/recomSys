from fastapi import APIRouter, HTTPException

from src.adapters.json_parse import JSONAdapter
from src.application.additional_routes.preferense_mark.model import RequestDescription
from src.entity.LLM_model import MarkingSystem
from src.entity.Recomendator import RecommendFasttextEfanna

router = APIRouter(
    prefix='/preference_mark'
)


@router.get("/")
async def read_root():
    return {"message": "Mark preferenses"}


@router.post("/mark_description")
async def encode_course(request: RequestDescription):
    try:
        msg, tags = JSONAdapter().parse_request_tags_description(request)

        code_mark = MarkingSystem.mark_description(msg, tags)

        return {
            "sucsessfull": True,
            "description": code_mark
        }
    except BaseException as e:
        print(e)
        return HTTPException(status_code=500, detail=str(e))


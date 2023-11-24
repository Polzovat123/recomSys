from fastapi import APIRouter

from src.adapters.json_parse import JSONAdapter
from src.entity.Recomendator import RecommendFasttextEfanna

router = APIRouter(
    prefix='/course'
)


@router.get("/")
async def read_root():
    return {"message": "Closest ID course"}


@router.post("/encode_course")
async def recommend_courses(request):
    try:
        msg = JSONAdapter().parse_request_enc_description(request)
        enc_msg = RecommendFasttextEfanna.embed_description_course(msg)

        return {
            "sucsessfull": True,
            "description": enc_msg
        }
    except BaseException as e:
        return {
            "sucsessfull": False,
            "description": None
        }
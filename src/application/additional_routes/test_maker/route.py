from fastapi import APIRouter, HTTPException

from src.adapters.json_parse import JSONAdapter
from src.application.additional_routes.test_maker.model import RequestMakeTest
from src.entity.llm_model import LLMbot

router = APIRouter(
    prefix='/test_maker'
)


@router.get("/")
async def read_root():
    return {"message": "Help creation test by lesson"}

@router.post("make_test")
async def make_test(request: RequestMakeTest):
    msg = JSONAdapter.parse_request_make_test(request)

    new_test = LLMbot().make(msg)

    return {
        "msg": new_test
    }

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix='/find_friend'
)


@router.get("/")
async def read_root():
    return {"message": "Service to help communicate with another people"}



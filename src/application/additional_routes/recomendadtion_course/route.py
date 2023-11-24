from fastapi import APIRouter

router = APIRouter(
    prefix='/course'
)


@router.get("/")
async def read_root():
    return {"message": "Closest ID course"}


@router.post("/recommend_courses")
async def recommend_courses():
    ...
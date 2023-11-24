from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from additional_routes.test_maker.route import router as testmaker_router
from additional_routes.recomendadtion_course.route import router as course_router
from additional_routes.recomendation_friend.route import router as friendrecom_router

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello on my recomendadn system"}


app.include_router(course_router)
app.include_router(testmaker_router)
app.include_router(friendrecom_router)
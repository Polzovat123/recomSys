from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from additional_routes.recomendadtion_course.route import router as course_router

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
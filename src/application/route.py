from fastapi import FastAPI
from additional_routes.recomendadtion_course.route import router as course_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello on my recomendadn system"}


app.include_router(course_router)
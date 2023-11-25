from typing import List

from pydantic import BaseModel


class Tags(BaseModel):
    id: int
    name: str


class RequestDescription(BaseModel):
    description: str
    tags: List[Tags]

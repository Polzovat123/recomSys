from typing import List, Optional

from pydantic import BaseModel


class Course(BaseModel):
    description: str
    score: List[int]
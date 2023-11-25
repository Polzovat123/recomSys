from typing import List

from pydantic import BaseModel


class RequestMakeTest(BaseModel):
    task: str
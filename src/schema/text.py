"""
Schema da rota /text
"""

from pydantic import BaseModel, Field

class ValidTextRouter(BaseModel):

    prompt:str
    input:str
    temperature:float
    max_token: float|int|None = Field(default=None)
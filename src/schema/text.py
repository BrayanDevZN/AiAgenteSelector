"""
Schema da rota /text
"""

from pydantic import BaseModel

class ValidTextRouter(BaseModel):

    prompt:str
    input:str
    temperature:float
    max_token = float|int|None = None
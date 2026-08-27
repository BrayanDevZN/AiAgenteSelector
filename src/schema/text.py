"""
Schema da rota /text
"""

from pydantic import BaseModel, Field, field_validator
class ValidTextRouter(BaseModel):

    prompt:str
    input:str
    temperature:float
    max_token: float|int|None = Field(default=None)
    optimizate: dict|None = Field(default=None)
    verbosity: bool = Field(default=False)



    @field_validator("optimizate")
    def valid(cls, v:dict|None):

        if v is not None:

            expeteds_keys = ["verbosity", "limit"]

            for key, value in v.items():

                if not key in expeteds_keys:

                    raise KeyError(f"Not Exepted key {key} in optimizate")

                if key == "verbosity":

                    if not value in ["high", "medium", "low"]:

                        raise ValueError(f"Not expeted value {value} of key verbosity in optmizate")

                else:

                    if not isinstance(value, int) or isinstance(value, None):

                        raise TypeError(f"Expeted type of {value} int or None")

                    

        return v


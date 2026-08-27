from src.logs.log import logger


"""
faz a requisição pro modelo da open ai
"""


from openai import OpenAI
from typing import Literal
async def request_llm(verbosity:Literal["high", "medium", "low"],model:str, input:str, temperature:float, prompt:str, api_key:str, max_token:int|None|float = None) -> str:

    try:

        logger.info(f"Enviando requisição pra open ai usando modelo {model}... ")

        NO_TEMPERATURE_MODELS = [
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    "gpt-5.6-luna",
    "gpt-5.6-terra",
    "gpt-5.6-sol",
    ]


        client = OpenAI(api_key=api_key)


        if not model in NO_TEMPERATURE_MODELS:

            

            response = client.responses.create(
                model=model, temperature=temperature, instructions=prompt, input=input
            ) if max_token is None else client.responses.create(
                model=model, temperature=temperature, instructions=prompt, input=input, max_output_tokens=max_token
            )

        else:

            logger.warning(f"model {model} not support param temperature")

            response = client.responses.create(
                            model=model,  instructions=prompt, input=input, text={"verbosity":verbosity}
                        ) if max_token is None else client.responses.create(
                            model=model,  instructions=prompt, input=input, max_output_tokens=max_token, text={"verbosity":verbosity}
                        )



        return response.output_text

    except Exception as e:
        logger.error(e)
        raise Exception(e)
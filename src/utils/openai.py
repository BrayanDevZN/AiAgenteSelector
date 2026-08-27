from src.logs.log import logger


"""
faz a requisição pro modelo da open ai
"""


from openai import OpenAI
from typing import Literal
async def request_llm(model:str, input:str, temperature:float, prompt:str, 
                      api_key:str, max_token:int|None|float = None, verbosity:Literal["high", "medium", "low"]=None) -> str:

    try:

        

        NO_TEMPERATURE_MODELS = [
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    "gpt-5.6-luna",
    "gpt-5.6-terra",
    "gpt-5.6-sol",
    ]


        client = OpenAI(api_key=api_key)



        if max_token is not None and verbosity is not None:

            logger.info(f"Enviando requisição pra open ai usando modelo {model} com o nivel de verbosidade {verbosity} e o numero maximo de tokens de saida de {max_token}... ")


            response = client.responses.create(
                model=model,
                input=input,
                temperature=temperature,
                instructions=prompt,
                max_output_tokens=max_token,
                text={"verbosity":verbosity}


            ) if not model in NO_TEMPERATURE_MODELS else client.responses.create(
                model=model,
                input=input,
                instructions=prompt,
                max_output_tokens=max_token,
                text={"verbosity":verbosity})

        elif max_token is not None and verbosity is None:

            logger.info(f"Enviando requisição pra open ai usando modelo {model} com o numero maximo de tokens de saida de {max_token}... ")

            response = client.responses.create(
                            model=model,
                            input=input,
                            temperature=temperature,
                            instructions=prompt,
                            max_output_tokens=max_token
            
                        ) if not model in NO_TEMPERATURE_MODELS else client.responses.create(
                            model=model,
                            input=input,
                            instructions=prompt,
                            max_output_tokens=max_token)

        elif max_token is None and verbosity is not None:

            logger.info(f"Enviando requisição pra open ai usando modelo {model} com o nivel de verbosidade de {verbosity}... ")

            response = client.responses.create(
                            model=model,
                            input=input,
                            temperature=temperature,
                            instructions=prompt,
                        
                            text={"verbosity":verbosity}
            
            
                        ) if not model in NO_TEMPERATURE_MODELS else client.responses.create(
                            model=model,
                            input=input,
                            instructions=prompt,
                            text={"verbosity":verbosity})


        else:

            logger.info(f"Enviando requisição pro modelo {model}...")

            response = client.responses.create(
                                        model=model,
                                        input=input,
                                        temperature=temperature,
                                        instructions=prompt,
                        
                        
                                    ) if not model in NO_TEMPERATURE_MODELS else client.responses.create(
                                        model=model,
                                        input=input,
                                        instructions=prompt,
                                        )
            
        return response.output_text

    except Exception as e:
        logger.error(e)
        raise Exception(e)
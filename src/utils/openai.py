from logs.log import logger


"""
faz a requisição pro modelo da open ai
"""


from openai import OpenAI

def request_llm(model:str, input:str, temperature:float, prompt:str, api_key:str, max_token:int|None|float = None) -> str:

    try:

        logger.info(f"Enviando requisição pra open ai usando modelo {model}... ")


        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model=model, temperature=temperature, instructions=prompt, input=input
        ) if max_token is None else client.responses.create(
            model=model, temperature=temperature, instructions=prompt, input=input, max_output_tokens=max_token
        )

        return response.output_text

    except Exception as e:
        logger.error(e)
        raise Exception(e)
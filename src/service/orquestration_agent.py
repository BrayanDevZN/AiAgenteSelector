from src.logs.log import logger

"""
Junta as variaveis de ambiente mais o prompt e a função que chama a llm para criar o agente orquestrador
"""

from src.utils.openai import request_llm
from src.repository.module import prompt_orquestration,prompt_orq_verbosity
from src.config.settings import api_key
from repository.module import ControlCache

async def orquestration_model(input:str, verbosity:bool, user:str) -> str:

    logger.info("Executando agente orquestrador...")

    instance = ControlCache()

    name = f"{user}:model"
    model = await instance.get(name)

    if model is None:

        model = await request_llm(
            
            model="gpt-5-nano",
            temperature=0.1,
            prompt=prompt_orquestration if not verbosity else prompt_orq_verbosity,
            api_key=api_key,
            input=input,
            verbosity="low"
            
        )

        await instance.set(name=name, data=model)


    return model



    

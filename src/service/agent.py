from src.logs.log import logger

"""
Junta as variaveis de ambiente mais o prompt e a função que chama a llm para criar o agente orquestrador
"""

from src.utils.openai import request_llm
from src.repository.module import prompt
from src.config.settings import api_key

def orquestration_model(input:str) -> str:

    logger.info("Executando agente orquestrador...")

    return request_llm(
        
        model="gpt-4.1-mini",
        temperature=0.1,
        prompt=prompt,
        api_key=api_key,
        input=input
        
    )



    

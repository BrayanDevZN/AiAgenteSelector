from src.logs.log import logger

"""
Junta as variaveis de ambiente mais o prompt e a função que chama a llm para criar o agente otimizador de prompts
"""

from src.utils.openai import request_llm
from src.repository.module import prompt_optimizate
from src.config.settings import api_key

async def optimizate_model(input:str) -> str:

    logger.info("Executando agente otimizador...")

    return await request_llm(
        
        model="gpt-5.6-terra",
        temperature=0.1,
        prompt=prompt_optimizate,
        api_key=api_key,
        input=input,
        verbosity="high"
        
        
    )



    
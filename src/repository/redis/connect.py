from src.config.settings import port, host
from src.logs.log import logger

"""
Cria conexão com redis
"""

from redis import Redis


logger.info("Criando conexão com redis...")

try:

    client = Redis(
        host=host, port=port, decode_responses=True
    ).pipeline()

except Exception as e:

    logger.error(e)

    raise Exception(e)

from src.logs.log import logger
from src.repository.redis.connect import client


"""
Controla o redis
"""

class ControlCache:

    #Cria o dado
    def set(self, name:str, data:int, time:str|None = None) -> dict:

        try:

            logger.info(f"salvando {name}...")

            client.set(name, data)

            client.expire(name=name, time=time if time is not None else 60)

            client.execute()

            return {"status": True}

        except Exception as e:

            logger.error(e)
            raise Exception(e)

    #LE
    def get(self, name:str) -> None|int:

        try:

            logger.info(f"Lendo {name}...")

            data = client.get(name=name)
            client.execute()


            return data

        except Exception as e:

            logger.error(e)
            raise Exception(e)


        
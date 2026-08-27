from src.logs.log import logger
from src.repository.redis.connect import client
from redis import WatchError

"""
Controla o redis
"""

class ControlCache:

    async def set(self, name:str, data:str, time:str|None=None):

        while True:

            try:

                logger.info(f"Salvando {name}...")

                
                with client as cache:

                        cache.watch(name)

                        cache.multi()

                        cache.set(name=name, value=data, ex=time if time is not None else 30)

                        cache.execute()

            except WatchError as e:
                continue

            

                



    
        

    #Cria o dado em operação atomica, incrementando automatico
    async def Iset(self, name:str, time:str|None = None) -> dict:

        try:

            logger.info(f"salvando {name}...")

            client.incr(name)

            client.expire(name=name, time=time if time is not None else 60)

            client.execute()

            return {"status": True}

        except Exception as e:

            logger.error(e)
            raise Exception(e)

    #LE
    async def get(self, name:str) -> None|int:

        try:

            logger.info(f"Lendo {name}...")

            client.get(name=name)
            


            return client.execute()[0]

        except Exception as e:

            logger.error(e)
            raise Exception(e)


    


        
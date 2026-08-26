from src.logs.log import logger

"""
Midlleware que varifica rate limit
"""


from src.config.settings import rate_limit, global_rate_limit
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from repository.module import ControlCache
class Midlleware(BaseHTTPMiddleware):


    def dispatch(self, request:Request, call_next):


        instance = ControlCache()


        #Confere se o rate limite global excedeu

        logger.info("Conferindo o  limite de requisições global...")
        global_instance = instance.get(name="global_rate_limit")

        if global_instance is not None and global_instance >= global_rate_limit:

            logger.warning("limite de requisições global excedido")

            raise HTTPException(
                status_code=429,
                detail="Exceded global rate limit"
            )

        else:
            instance.set(name="global_rate_limit")


        #usuario que faz a requisição
        user = request.headers["X-instance_user"]
        logger.info(f"Conferindo o limite de requisições do usuario {user}...")

        user_instance = instance.get(name=f"rate_limit:{user}")

        if user_instance is not None and user_instance >= rate_limit:

            logger.warning(f"Limite de requisições do usuario {user} excedido")

            raise HTTPException(
                            status_code=429,
                            detail=f"Exceded  rate limit for user {user}"
                        )

        call_next(request)


    




            



        


    
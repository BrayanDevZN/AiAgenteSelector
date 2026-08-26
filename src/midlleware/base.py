from src.logs.log import logger

"""
Midlleware que varifica rate limit
"""


from src.config.settings import rate_limit, global_rate_limit
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from src.repository.module import ControlCache
from fastapi.responses import JSONResponse
class Midlleware(BaseHTTPMiddleware):


    async def dispatch(self, request:Request, call_next):

        logger.info(f"Executando rota {request.url.path}...")

        if not "X-instance_user" in request.headers:

            return JSONResponse(
                status_code=422, content={"error": "Expeted header X-instance_user"}
            )

        


        instance = ControlCache()


        #Confere se o rate limite global excedeu

        logger.info("Conferindo o  limite de requisições global...")
        global_instance = instance.get(name="global_rate_limit")

        if global_instance is not None and global_instance >= global_rate_limit:

            logger.warning("limite de requisições global excedido")

            return JSONResponse(
                status_code=429,
                content={"error":"Exceded global rate limit"}
            )

        else:
            instance.set(name="global_rate_limit")


        #usuario que faz a requisição
        user = request.headers["X-instance_user"]
        logger.info(f"Conferindo o limite de requisições do usuario {user}...")

        user_instance = instance.get(name=f"rate_limit:{user}")

        if user_instance is not None and user_instance >= rate_limit:

            logger.warning(f"Limite de requisições do usuario {user} excedido")

            JSONResponse(
                status_code=429,
                content={"error":f"Exceded rate limit of user {user}"}
            )

        return await call_next(request)


    




            



        


    
"""
Inicia toda a aplicação
"""

from src.config.settings import origin
from fastapi import FastAPI
from src.midlleware.base import Midlleware
from src.handles.text import router_text
from fastapi.middleware.cors import CORSMiddleware
class AppAgent:

    def __init__(self)-> None:

        self.app = FastAPI()
        self.routes = [router_text]


    #Cors
    def _cors(self) -> None:

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[origin],
            allow_headers=["X-instance_user"],
            allow_credentials=False,
            allow_methods=["POST"]
        )




    


    #Adiciona o midlleware
    def _mid(self) -> None:

        self.app.add_middleware(Midlleware)

    #Adiciona as rotas
    def _router(self) -> None:

        for router in self.routes:

            self.app.include_router(router)

    #Retorna o objeto do fastapi e executa os metodos
    def run(self) -> FastAPI:

        self._cors()
        self._mid()
        self._router()
        return self.app


instance = AppAgent()
app = instance.run()



    
        
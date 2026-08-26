"""
Inicia toda a aplicação
"""


from fastapi import FastAPI
from src.midlleware.base import Midlleware
from src.handles.text import router_text

class AppAgent:

    def __init__(self)-> None:

        self.app = FastAPI()
        self.routes = [router_text]


    #Adiciona o midlleware
    def _mid(self) -> None:

        self.app.add_middleware(Midlleware)

    #Adiciona as rotas
    def _router(self) -> None:

        for router in self.routes:

            self.app.include_router(router)

    #Retorna o objeto do fastapi e executa os metodos
    def run(self) -> FastAPI:

        self._mid()
        self._router()
        return self.app


instance = AppAgent()
app = instance.run()



    
        
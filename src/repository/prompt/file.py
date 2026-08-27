from src.logs.log import logger

"""
Pega o prompt
"""
import os
from pathlib import Path


class FilePrompt:

    def __init__(self)-> None:

        self.dir = [Path(__file__).resolve().parent / "orquestration_withverbosity.md", 
                    Path(__file__).resolve().parent / "optimizate.md",
                    Path(__file__).resolve().parent / "orquestration.md"
                    ]
        

    #Confere se o arquivo existe
    def _exists(self, path:str) -> None:

        if not os.path.exists(path):
            msg = f"Expeted {path}"

            logger.error(msg)
            raise FileNotFoundError(msg)

    #Le o arquivo do prompt
    def _read(self, path:str) -> str|None:

        with open(path, "r", encoding="utf-8") as f:

            return f.read()

    #Confere se o arquivo é vazio
    def _len(self, path:str) -> None:

        if len(path) <=0:

            msg = f"Expeted prompt in {path}"
            logger.error(msg)
            raise ValueError(msg)

    #insere o prompt na lista
    def _run(self) -> None:

        for number, path in enumerate(self.dir):

            self._exists(path=path)

            prompt = self._read(path=path)

            self._len(path=prompt)

            self.dir[number] = prompt


    #Executa run e retorna a lista dos prompts
    def get(self) -> list:

        try:

            self._run()
            return self.dir

        except Exception as e:

            raise(e)


instance = FilePrompt()
prompts = instance.get()
prompt_orquestration = prompts[0]
prompt_optimizate = prompts[1]
prompt_orq_verbosity = prompts[2]





    

    



    
        

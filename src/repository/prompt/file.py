from src.logs.log import logger

"""
Pega o prompt
"""


try:

    from pathlib import Path



    #Caminho onde o prompt ta salvo
    BASE_DIR = Path(__file__).resolve().parent / "orquestration.md"



    #Confere se o caminho existe
    import os
    if not os.path.exists(BASE_DIR):

        raise FileNotFoundError(f"Expeted {BASE_DIR}")


    with open(BASE_DIR, "r", encoding="utf-8") as f:

        prompt = f.read()

    if len(prompt) == 0:
        msg = "Expeted prompt"
        logger.error(msg)

        raise ValueError(msg)


except Exception as e:

    logger.error(e)
    raise Exception(e)

    


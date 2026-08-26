"""
Pega as variaveis de ambiente do redis
"""

try:

    import os
    from pathlib import Path

    #Caminho inicial
    BASE_DIR = Path(__file__).resolve().parent / ".env" 

    #Se o caminho do .env não existir, tenta puxar da raiz do projeto
    if not os.path.exists(BASE_DIR):
        

        BASE_DIR = Path(__file__).resolve().parent.parent.parent 
    


    #Carrega as variaveis
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR)


    port = os.getenv("port")
    host = os.getenv("host")
    rate_limit = os.getenv("rate_limit")
    global_rate_limit = os.getenv("global_rate_limit")
    api_key = os.getenv("api_key")

    if api_key is None:

        raise ValueError("Expeted enviroin api_key")

    if rate_limit is None or global_rate_limit is None:

        raise ValueError("Expeted enviroins rate limit")
    
    

    if port is None or host is None:

        raise ValueError("Expeted enviroin port and host")

except Exception as e:

    raise Exception(e)

    




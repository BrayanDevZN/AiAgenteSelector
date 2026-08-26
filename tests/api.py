"""
Testa as rotas da api
"""

import requests
url = " http://127.0.0.1:8000/text"


payload = {
    "temperature":0.5, "input": "Faz uma calculadora", "prompt": "seje um bom programador"
}

response = requests.post(url=url, json=payload, headers={"X-instance_user": "Brayan"}).json()

print(response["output"])
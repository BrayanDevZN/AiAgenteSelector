"""
Testa as rotas da api
"""

import requests
url = "http://127.0.0.1:8000/text"


payload = {
    "temperature":0.5, "input": "Oi, o que voce faz?", "prompt": "Faça uma calculadora"
}

response = requests.post(url=url, json=payload, headers={"X-instance_user": "Brayan"}).json()

print(response)
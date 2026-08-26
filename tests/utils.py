"""
teste de utils
"""

key = "sua chave api aqui"


from src.utils.openai import request_llm
from src.repository.module import prompt

input = "Cria uma calculadora em python com loop e com opção de sair e com poo"
model = request_llm(prompt=prompt, input=input, model="gpt-4.1-mini", temperature=0.1, api_key=key)


print(request_llm(model=model, input=input, temperature=0.5, api_key=key, prompt="Seje educado"))
"""
teste de utils
"""

key = "sua chave api aqui"

if __name__ == "__main__":
    from src.utils.openai import request_llm

    print(request_llm(model="gpt-4.1-mini", input=input, temperature=0.5, api_key=key, prompt="Seje educado"))
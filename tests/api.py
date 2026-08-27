"""
Testa e compara as rotas da API
"""

from time import perf_counter
import requests

url = "http://127.0.0.1:8000/text"

headers = {
    "X-instance_user": "Brayan"
}

payload = {
    "temperature": 0.5,
    "input": "Me ensine redis",
    "prompt": "Seje um professor",
    "optimizate": False
}


# Sem otimização
start = perf_counter()

response = requests.post(
    url=url,
    json=payload,
    headers=headers
).json()

time_without = perf_counter() - start

print("\n=== SEM OTIMIZAÇÃO ===")
print(response["output"])
print(f"\nTempo: {time_without:.3f}s")


# Com otimização
payload["optimizate"] = True

start = perf_counter()

response = requests.post(
    url=url,
    json=payload,
    headers=headers
).json()

time_with = perf_counter() - start

print("\n=== COM OTIMIZAÇÃO ===")
print(response["output"])
print(f"\nTempo: {time_with:.3f}s")


# Comparação
difference = time_with - time_without

print("\n=== COMPARAÇÃO ===")
print(f"Sem otimização: {time_without:.3f}s")
print(f"Com otimização: {time_with:.3f}s")
print(f"Diferença:      {difference:+.3f}s")
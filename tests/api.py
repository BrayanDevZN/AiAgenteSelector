"""
Testa optimizate_limit
"""

from time import perf_counter
import requests

url = "http://127.0.0.1:8000/text/"

headers = {
    "X-instance_user": "Brayan"
}

payload = {
    "temperature": 0.5,
    "input": "Me ensine redis",
    "prompt": "Seje um professor",
    "optimizate": {"verbosity": "medium", "limit": 20},
    "verbosity":True
}

start = perf_counter()

response = requests.post(
    url=url,
    json=payload,
    headers=headers
)

elapsed = perf_counter() - start

print(f"Status: {response.status_code}")
print(response.json()["output"])
print(f"\nTempo: {elapsed:.3f}s")
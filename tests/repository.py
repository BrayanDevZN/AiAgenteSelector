"""
Testes de repository
"""

from src.repository.module import prompt, ControlCache


print(prompt)






instance = ControlCache()

print(instance.set(name="rate_limit", data=1))

print(instance.get(name="rate_limit"))

"""
Testes de repository
"""
if __name__ == "__main__":
    from src.repository.module import prompt_orquestration, prompt_optimizate, ControlCache


    print(prompt_orquestration, prompt_optimizate)






    instance = ControlCache()

    print(instance.set(name="rate_limit", data=1))

    print(instance.get(name="rate_limit"))

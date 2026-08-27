"""
Cria teste em service
"""
if __name__ == "__main__":
    from src.service.orquestration_agent import orquestration_model
    from src.service.optimizate_agent import optimizate_model
    import asyncio

    async def test():

        print(await orquestration_model(input="Cria uma calculado com loop"))

        print(await optimizate_model(input="Cria uma calculadora"))


    asyncio.run(test())
        
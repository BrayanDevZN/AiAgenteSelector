"""
teste de src/config
"""


from src.config.settings import rate_limit, global_rate_limit

if __name__ == "__main__":

    
    print(f"rate limit: {rate_limit} \nglobal rate limit: {global_rate_limit}")
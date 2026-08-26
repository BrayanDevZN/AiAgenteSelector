"""
teste de src/config
"""


from src.config.settings import port, host, rate_limit, global_rate_limit

if __name__ == "__main__":

    print(f"port: {port} \nhost:{host}")
    print(f"rate limit: {rate_limit} \nglobal rate limit: {global_rate_limit}")
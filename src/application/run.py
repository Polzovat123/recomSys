import os
import openai
import uvicorn

if __name__ == "__main__":
    os.environ['host'] = '26.191.10.163'
    os.environ['user'] = 'postgres'
    os.environ['password'] = 'admin'
    os.environ['db'] = 'ufa_hack_2023'
    os.environ['port'] = '5432'

    api_key = "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"
    openai.api_key = api_key

    # os.environ["url_connect"] = f"dbname='{db}' user='{user}' host='{host}' password='{password}' port='{port}'"

    uvicorn.run("route:app", host="0.0.0.0", port=2309)

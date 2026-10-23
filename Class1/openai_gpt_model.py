import os

# pip install openai
from openai import OpenAI # from (kis module) import (kaun si class/function)
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()  # reads OPENAI_API_KEY from .env

# OpenAI provides us a client to call different models.
client = OpenAI() # As we not not provided any api_key and base_url, it will automatically read from the environment variables OPENAI_API_KEY and OPENAI_BASE_URL

response = client.chat.completions.create(
    model= "openai/gpt-oss-20b", # a openai model on OpenAI
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a poem about the beauty of nature."}
    ]
)


print(response.choices[0].message.content)
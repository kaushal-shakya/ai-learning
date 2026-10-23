import os

# pip install openai
from openai import OpenAI # from (kis module) import (kaun si class/function)
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv() 

#  Groq exposes an OpenAI-compatible API, so we reuse the
#  exact same client — just point it at a different base_url
#  and swap in a free open-source model.  Zero new concepts.

# OpenAI provides us a client to call different models.
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url=os.getenv("GROQ_API_BASE_URL")
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",  # a free Llama model on Groq
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a poem about the beauty of nature."}
    ]
)


print(response.choices[0].message.content)
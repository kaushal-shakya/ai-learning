
# agent.py
# Your first tiny AGENT using Anthropic Claude
# Run: python agent.py

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

# ---- our tiny "database" ----
PRICES = {
    "shoes": 799,
    "hat": 399,
    "bag": 1420,
    "shorts": 1299,
    "pants": 1699
}


# ---- Step 1: Define the actual Python function ----
def get_price(item):
    print(f"🔧 tool called: get_price({item})")
    return f"₹{PRICES.get(item.lower(), 'unknown')}"


# ---- Step 2: Describe the tool for Claude ----
# ---- This is the "tool spec" that tells Claude what tools it can use, and how to call them. ----
# ---- This is different from the OpenAI tools json spec, but the idea is the same: you describe your tools to the model so it can use them. ----
tools = [
    {
        "name": "get_price",
        "description": "Get the price of a shop item the user asks about.",
        "input_schema": {
            "type": "object",
            "properties": {
                "item": {
                    "type": "string",
                    "description": "The item name"
                }
            },
            "required": ["item"]
        }
    }
]


# ---- Step 3: Agent loop ----
def agent(user_message):

    messages = [
        {"role": "user", "content": user_message}
    ]

    while True:

        # 1. Send messages and tools to Claude
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=messages,
            tools=tools
        )

        # 2. Check whether Claude wants to use a tool
        if response.stop_reason == "tool_use":

            # Save Claude's tool request
            messages.append({
                "role": "assistant",
                "content": response.content
            })

            tool_results = []

            # 3. Execute requested tools
            for block in response.content:

                if block.type == "tool_use":

                    if block.name == "get_price":
                        item = block.input["item"]
                        result = get_price(item)
                        is_error = False
                    else:
                        result = f"Unknown tool: {block.name}"
                        is_error = True

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                        "is_error": is_error
                    })

            # 4. Return tool results to Claude
            messages.append({
                "role": "user",
                "content": tool_results
            })

            # Continue until Claude produces a final answer
            continue

        # 5. Return Claude's final text response
        return "\n".join(
            block.text
            for block in response.content
            if block.type == "text"
        )


if __name__ == "__main__":

    print(agent("How much are the shoes?"))
    print(agent("Hi! What can you help with?"))

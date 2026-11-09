# Section 2 — Giving Agents Tools

| Notebook | What it covers |
|---|---|
| `01_building_tools.ipynb` | Function → tool with `@tool`, a tip calculator, a multi-tool sales assistant, a custom inventory checker |
| `02_prebuilt_and_aws_tools.ipynb` | Prebuilt tools (`calculator`, `http_request`, `file_write`) and `use_aws` against S3, DynamoDB and Lambda |
| `03_advanced_tool_patterns.ipynb` | The database-connection problem and class-based tools; async tools that run in parallel |

## Run

```bash
pip install -r requirements.txt
jupyter lab
```

Notebook 2 creates a small S3 bucket, a DynamoDB table and a Lambda function, and deletes them in its last cell.

## Note on deprecation warnings

`strands-agents-tools` 0.8.x prints a deprecation notice for some prebuilt tools (`calculator`, `http_request`, `tavily`, `current_time`). They still work — this course pins `strands-agents-tools<0.9` so they keep working. The replacements, for when you move on: `http_request`/`web_fetch` from `strands.vended_tools`, the official Tavily MCP server, and `ContextInjector` for the current time.

## Bonus: Strands Agent Builder

An interactive terminal agent that can write and test tools for you:

```bash
pipx install strands-agents-builder     # or: pip install strands-agents-builder
strands                                 # interactive mode
strands "Build a tool that converts Celsius to Fahrenheit"
```

Browse all prebuilt tools at https://github.com/strands-agents/tools.

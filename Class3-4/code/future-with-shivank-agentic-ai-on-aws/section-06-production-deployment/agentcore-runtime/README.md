# AgentCore Runtime — Deploy a Strands Agent

| File | Purpose |
|---|---|
| `agent.py` | The agent: a normal Strands agent + 4 lines of `BedrockAgentCoreApp` boilerplate |
| `requirements.txt` | Packages installed **inside** the deployed container |
| `deploy_to_agentcore_runtime.ipynb` | Configure → launch → invoke (toolkit and boto3) → stop session → destroy |
| `Dockerfile` | Reference copy of what the starter toolkit generates (it is regenerated on configure) |

## Test locally

```bash
pip install bedrock-agentcore strands-agents
python agent.py
# in another terminal
curl -X POST http://localhost:8080/invocations -H "Content-Type: application/json" \
  -d '{"prompt": "What are the key clauses in a standard NDA?"}'
```

## Deploy

Open `deploy_to_agentcore_runtime.ipynb` and run the cells in order. The build runs in AWS CodeBuild (ARM64), so you don't need Docker.

Prefer the CLI? The same flow:

```bash
pip install bedrock-agentcore-starter-toolkit
agentcore configure -e agent.py --non-interactive
agentcore deploy
agentcore invoke '{"prompt": "Summarize the termination clause risks"}'
agentcore destroy
```

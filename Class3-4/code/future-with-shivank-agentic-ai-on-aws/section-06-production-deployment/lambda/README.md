# Deploy a Strands Agent to AWS Lambda

A serverless contract-analysis agent behind API Gateway. POST a document; get back key terms, flagged risks and a summary.

```
User → API Gateway → Lambda (container image) → Strands agent → Amazon Bedrock
```

## Prerequisites

1. AWS CLI configured (`aws sts get-caller-identity`)
2. AWS SAM CLI (`sam --version`)
3. Docker running (`docker info`)

On Windows, run the scripts from WSL (recommended) or Git Bash.

## Deploy

```bash
chmod +x deploy.sh cleanup.sh
./deploy.sh
```

The script detects your CPU architecture (arm64 for Apple Silicon/Graviton, x86_64 otherwise), builds the image, and deploys with SAM. Takes 2–3 minutes. Set `BEDROCK_MODEL_ID` before running to use a different model.

## Test

```bash
curl -X POST <ApiEndpoint printed by deploy.sh> \
  -H "Content-Type: application/json" \
  -d '{"document_text": "This agreement is entered into by Party A and Party B. Party A shall deliver 1000 units by March 2027. Late delivery incurs unlimited liability."}'
```

The first request is slower (cold start, 5–15 s).

> API Gateway REST APIs time out after 29 seconds by default. Keep requests short, use a faster model (`global.anthropic.claude-haiku-4-5-20251001-v1:0`), or use a Lambda Function URL / AgentCore Runtime for long-running agents.

> ⚠️ The demo API has no authentication — anyone with the URL can call it and spend your Bedrock budget. Don't share the URL, and run `./cleanup.sh` the same day. For real use, add an API key/usage plan, IAM auth or a Cognito authorizer.

## Clean up

```bash
./cleanup.sh
```

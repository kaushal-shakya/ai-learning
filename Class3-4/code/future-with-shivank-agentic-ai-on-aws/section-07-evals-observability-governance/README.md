# Section 7 — Evals, Observability and Governance

How well is the agent doing? What is it doing? What is it allowed to do?

```
section-07-evals-observability-governance/
├── agent-evaluation/
│   ├── end_to_end_eval.ipynb         # deploy → custom judge → invoke → evaluate → report
│   ├── agent_app.py                  # travel assistant deployed to AgentCore Runtime
│   ├── travel_quality_metric.json    # custom LLM-as-judge config
│   ├── agent_requirements.txt        # packages inside the deployed agent
│   └── requirements.txt              # packages for the notebook
├── agent-observability/
│   ├── 01_console_tracing.ipynb      # spans printed to stdout
│   ├── 02_jaeger_tracing.ipynb       # local waterfall UI (Docker)
│   ├── 03_langfuse_tracing.ipynb     # Langfuse
│   ├── 04_langsmith_tracing.ipynb    # LangSmith
│   ├── 05_cloudwatch_adot_tracing.ipynb  # CloudWatch GenAI Observability via ADOT
│   ├── agentcore_agent.py            # agent run under opentelemetry-instrument
│   └── otel-collector/               # one collector → Datadog + Langfuse
└── ai-governance/
    ├── 01_bedrock_guardrails.ipynb   # control what the agent SAYS
    ├── 02_agentcore_policy_cedar.ipynb  # control what the agent DOES
    ├── cedar-policies/               # refund limit, patient records, org boundary
    └── governance_checklist.md       # agent card, audit trail, incident response
```

## Before you start

- AWS credentials, `AWS_REGION=us-east-1`
- Turn on **CloudWatch Transaction Search** once (CloudWatch console → *Application Signals* → *Transaction Search* → *Enable*). AgentCore Evaluations and CloudWatch GenAI Observability read traces from it.
- Optional accounts: Langfuse, LangSmith, Datadog. Optional: Docker (Jaeger, OTel Collector).

## Run

```bash
cd agent-evaluation && pip install -r requirements.txt && jupyter lab end_to_end_eval.ipynb
cd ../agent-observability && pip install -r requirements.txt && jupyter lab
cd ../ai-governance && pip install -r requirements.txt && jupyter lab
```

## Guardrails vs Policy

| | Bedrock Guardrails | AgentCore Policy |
|---|---|---|
| Controls | Model input/output text | Tool-call execution |
| Rules written in | Guardrail configuration | Cedar |
| Enforcement | Content filters and classifiers | Deterministic rule evaluation |
| Can a clever prompt get around it? | Hard, but possible | No — evaluated outside the model |
| Knows who the user is? | No | Yes (OAuth claims / IAM principal) |
| Scope | Each model call | Each tool call |

Use guardrails for what the agent says; use policy for what it does. In a well-governed system, both are on.

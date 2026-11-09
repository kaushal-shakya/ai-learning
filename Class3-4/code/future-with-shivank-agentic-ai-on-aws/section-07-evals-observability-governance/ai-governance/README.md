# AI Governance

| Item | What it covers |
|---|---|
| `01_bedrock_guardrails.ipynb` | Create a guardrail (content filters, denied topic, PII), attach it to an agent, test it — then show that guardrails can't stop a $50,000 refund tool call |
| `02_agentcore_policy_cedar.ipynb` | Put the refund tool behind an AgentCore Gateway, attach a Cedar policy engine, and watch $500 succeed while $50,000 is denied |
| `cedar-policies/` | Four Cedar rules: allow the refund tool, forbid refunds > $1,000, physician-only patient records, organisation data boundary |
| `governance_checklist.md` | The human layer: agent card, risk assessment, audit trail, incident response |

## Run

```bash
pip install -r requirements.txt
jupyter lab
```

IAM: `bedrock:CreateGuardrail`/`GetGuardrail`/`DeleteGuardrail`, `bedrock:InvokeModel`; for notebook 2 also `bedrock-agentcore:*` (gateway, policy), `lambda:*` on the demo function, and IAM role management.

## Cost

Minimal. Guardrails are billed per 1,000 text units. Both notebooks delete what they create in their last cell.

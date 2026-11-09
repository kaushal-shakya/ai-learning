# End-to-End Agent Evaluation (AgentCore Evaluations)

| Step | What happens |
|---|---|
| 1 | Deploy a travel assistant to AgentCore Runtime (CodeBuild — no Docker) |
| 2 | Create a custom LLM-as-judge evaluator (5-point scale) |
| 3 | Invoke the agent with in-scope and out-of-scope prompts in one session |
| 4 | Run built-in evaluators: GoalSuccessRate (session), Correctness and Helpfulness (trace) |
| 5 | Run the custom evaluator and see it catch the out-of-scope answer |
| 6 | Print a score table, save results to JSON, clean up |

## The agent

`agent_app.py` has three tools — `get_flight_info`, `get_hotel_recommendations`, `get_weather_forecast` — and is told to stay in the travel domain. The custom evaluator (`travel_quality_metric.json`) scores any out-of-scope answer as **Very Poor (0.0)**.

## Prerequisites

- IAM: `bedrock-agentcore:*`, `ecr:*`, `iam:CreateRole`/`PassRole`, `codebuild:*`, `s3:*`, `logs:*`, `xray:*`
- CloudWatch Transaction Search enabled

## Run

```bash
pip install -r requirements.txt
jupyter lab end_to_end_eval.ipynb
```

First deployment takes 5–10 minutes. Expected: travel prompts score **Good / Very Good**; the Python-scripting prompt scores **Very Poor** on the custom evaluator.

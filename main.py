import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from agents.manager_agent import manager_agent

queries = {
    "rag": "Which phrasal verbs appear in my notes, explain their meanings?",
}
query = queries["rag"]

result = manager_agent.run(query)
print(result)
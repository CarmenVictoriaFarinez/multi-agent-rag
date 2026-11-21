from smolagents import CodeAgent
from models.ollama_model import get_model

classifier_agent = CodeAgent(
    model=get_model("llama3.2:3b"),
    tools=[],
    name="classifier_agent",
    description=(
        "Agente para clasificar texto por tema gramatical."
    ),
    instructions=(
        "Agente especializado en clasificar por tema gramatical el texto que "
        "recibe. Indica brevemente la categoria y la evidencia textual. No "
        "afirmes haber consultado archivos que no se hayan proporcionado. "
        "Responde en espanol."
    ),
    max_steps=3,
)
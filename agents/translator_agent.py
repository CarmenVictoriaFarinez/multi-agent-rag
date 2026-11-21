from models.ollama_model import get_model
from smolagents import CodeAgent

translator_agent = CodeAgent(
    model=get_model("qwen2.5-coder:7b"),
    tools=[],
    name="translator_agent",
    description=(
        "Agente para traducir textos entre idiomas."
    ),
    instructions=(
        "Agente especializado en traducir textos. Traduce el texto "
        "proporcionado al idioma solicitado, conserva su significado y no "
        "añadas explicaciones salvo que el usuario las pida."
    ),
    max_steps=3,
)
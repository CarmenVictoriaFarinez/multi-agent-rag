from smolagents import CodeAgent
from models.ollama_model import get_model

summarizer_agent = CodeAgent(
    model=get_model("llama3.2:3b"),
    tools=[],
    name="summarizer_agent",
    description=(
        "Agente para resumir textos."
    ),
    instructions=(
        "Agente especializado en resumir el texto que recibe. Conserva las "
        "ideas principales y responde en el idioma del texto, salvo que se "
        "solicite otro."
    ),
    max_steps=3,
)
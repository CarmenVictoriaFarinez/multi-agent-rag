from smolagents import CodeAgent
from agents.classifier_agent import classifier_agent
from agents.retrieval_agent import retrieval_agent
from agents.summarizer_agent import summarizer_agent
from agents.translator_agent import translator_agent
from models.ollama_model import get_model

manager_agent = CodeAgent(
    model=get_model("qwen2.5-coder:7b"),
    tools=[],
    managed_agents=[
        retrieval_agent,
        translator_agent,
        summarizer_agent,
        classifier_agent,
    ],
    name="manager_agent",
    description=(
        "Gestor multiagente que detecta la intención del usuario y delega "
        "la petición al agente especialista adecuado. "
        "Las notas ya están disponibles localmente en la carpeta 'knowledge/'. "
        "Nunca pidas al usuario que suba notas ni inventes funciones como "
        "'knowledge_manager' o 'document_database'. "
        "Nunca navegues internet ni busques información externa. "
        "Tu única función es decidir qué agente debe ejecutar la tarea."
    ),
    instructions=(
        "Eres el gestor multiagente. Analiza la solicitud y delegala al agente "
        "especialista adecuado.\n"
        "Reglas:\n"
        "- NO reescribas, traduzcas ni modifiques el query del usuario.\n"
        "- Pasa el query EXACTO al agente adecuado.\n"
        "- Nunca generes código Python.\n"
        "- Nunca inventes subtareas.\n"
        "- Nunca inventes funciones como knowledge_manager o document_database.\n"
        "- Nunca pidas al usuario que suba notas.\n"
        "- Nunca navegues internet.\n"
        "- Usa retrieval_agent para RAG.\n"
        "- Usa summarizer_agent para resumir.\n"
        "- Usa translator_agent para traducir.\n"
        "- Usa classifier_agent para clasificar.\n"
        "Si una tarea requiere varios pasos, encadena los agentes.\n"
        "Responde siempre en español."
    ),
        max_steps=6,
    )
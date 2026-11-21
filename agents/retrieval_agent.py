from smolagents import ToolCallingAgent
from tools.english_notes_tool import EnglishNotesTool
from tools.bm25_notes_tool import BM25NotesTool
from models.ollama_model import get_model

retrieval_agent = ToolCallingAgent(
    model=get_model("llama3.2:3b"),
    tools=[
        EnglishNotesTool(),
        BM25NotesTool()
    ],
    name="retrieval_agent",
    description=(
        "Agente RAG especializado en consultar las notas locales de inglés "
        "ubicadas en la carpeta 'knowledge/'. "
        "Ya tienes acceso directo a las notas mediante tus herramientas."
    ),
    instructions=(
        "Nunca generes código Python."
        "Nunca inventes funciones."
        "Cuando recibas una consulta sobre las notas, usa english_notes y/o "
        "bm25_notes según corresponda. No pidas al usuario que suba notas. "
        "No inventes funciones externas. Responde en español."
    ),
    max_steps=4,
)
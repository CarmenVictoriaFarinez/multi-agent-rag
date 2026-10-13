# examples/english_rag_demo.py

from tools.bm25_notes_tool import BM25NotesTool
from tools.english_notes_tool import EnglishNotesTool
from models.ollama_model import get_model
from smolagents import CodeAgent, ToolCallingAgent

def main():
    agent = ToolCallingAgent(
    tools=[EnglishNotesTool(), BM25NotesTool()],
    model=get_model(),
    max_steps=3
)

    prompt = (
        "Eres un asistente que ayuda a Carmen con su curso de inglés.\n\n"
        "REGLAS ESTRICTAS:\n"
        "1. No puedes responder sin usar una herramienta.\n"
        "2. Usa la herramientas disponibles. Responde SOLO con JSON..\n"
        "3. Usa las dos herramientas disponibles:\n"
        "   - english_notes \n"
        "   - bm25_notes \n"
        "4. Cada vez que te pregunte algo sobre mis notas, debes usar una herramienta.\n\n"
        "Question: Which phrasal verbs appear in my notes and explain their meanings?\n"
    )

    print(agent.run(prompt))




if __name__ == "__main__":
    main()

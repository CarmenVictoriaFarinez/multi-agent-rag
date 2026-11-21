# tools/english_notes_tool.py

from smolagents import Tool
import os

class EnglishNotesTool(Tool):
    """
    Herramienta RAG sencilla que busca información en TODOS los archivos .txt
    dentro de la carpeta 'knowledge'. Ideal para tus notas de inglés.
    """

    name = "english_notes"
    description = (
        "Busca información en todos los archivos .txt de la carpeta 'knowledge'. "
        "Devuelve fragmentos relevantes indicando de qué archivo provienen."
    )

    inputs = {
        "query": {
            "type": "string",
            "description": "Texto o tema a buscar en las notas."
        }
    }

    output_type = "string"

    def forward(self, query: str) -> str:
        """
        Lógica del RAG sencillo:
        - Recorre todos los .txt en knowledge/
        - Busca coincidencias de texto (case-insensitive)
        - Devuelve las líneas relevantes agrupadas por archivo
        """

        # Carpeta donde guardas tus notas
        base_dir = os.path.dirname(os.path.dirname(__file__))
        knowledge_dir = os.path.join(base_dir, "knowledge")

        if not os.path.exists(knowledge_dir):
            return "No se encontró la carpeta 'knowledge'."

        query_lower = query.lower()
        results = []

        # Recorremos todos los archivos .txt
        for filename in os.listdir(knowledge_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(knowledge_dir, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                lines = content.split("\n")

                # Buscamos coincidencias en este archivo
                matches = [
                    line for line in lines
                    if query_lower in line.lower()
                ]

                # Si encontramos algo, lo guardamos indicando el archivo
                if matches:
                    results.append(
                        f"Archivo: {filename}\n" +
                        "\n".join(matches)
                    )

        # Si no hubo coincidencias en ningún archivo
        if not results:
            return (
                f"No encontré nada relacionado con '{query}' "
                "en ninguno de tus archivos de notas."
            )

        # Unimos todos los resultados
        return "\n\n" + "\n\n".join(results)

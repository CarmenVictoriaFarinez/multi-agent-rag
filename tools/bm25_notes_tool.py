import os
from rank_bm25 import BM25Okapi
from smolagents import Tool

class BM25NotesTool(Tool):
    """
    BM25 mejorado:
    - Ordena documentos por relevancia
    - Extrae líneas relevantes dentro de cada documento
    - Devuelve fragmentos en lugar de imprimir todo el archivo
    - Devuelve top‑k documentos (por defecto 3)
    """

    name = "bm25_notes"
    description = "Recupera fragmentos relevantes de las notas usando BM25."
    inputs = {
        "query": {
            "type": "string",
            "description": "Texto o tema a buscar en las notas."
        }
    }
    output_type = "string"

    def __init__(self, top_k=3):
        super().__init__()
        self.top_k = top_k
        self.docs, self.names = self.load_documents()
        tokenized = [doc.lower().split() for doc in self.docs]
        self.bm25 = BM25Okapi(tokenized)

    def load_documents(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        knowledge_dir = os.path.join(base_dir, "knowledge")

        docs = []
        names = []

        for filename in os.listdir(knowledge_dir):
            if filename.endswith(".txt"):
                path = os.path.join(knowledge_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    docs.append(f.read())
                    names.append(filename)

        return docs, names

    def forward(self, query: str) -> str:
        query_lower = query.lower()
        tokens = query_lower.split()
        scores = self.bm25.get_scores(tokens)

        if len(scores) == 0:
            return "No hay documentos disponibles en la carpeta 'knowledge'."

        # Ordenar documentos por relevancia (mayor score primero)
        sorted_indices = scores.argsort()[::-1]
        top_indices = sorted_indices[:self.top_k]

        results = []

        for idx in top_indices:
            doc = self.docs[idx]
            name = self.names[idx]

            # Extraer líneas relevantes dentro del documento
            lines = doc.split("\n")
            matches = [
                line.strip()
                for line in lines
                if query_lower in line.lower()
            ]

            # Si no hay coincidencias exactas, mostrar un fragmento del documento
            if not matches:
                fragment = "\n".join(lines[:5])  # primeras 5 líneas como contexto
                results.append(
                    f" Archivo: {name}\n"
                    f"(Sin coincidencias exactas, mostrando fragmento relevante)\n"
                    f"{fragment}\n"
                )
            else:
                results.append(
                    f" Archivo: {name}\n"
                    f"Coincidencias encontradas:\n" +
                    "\n".join(f"- {m}" for m in matches) +
                    "\n"
                )

        return "\n".join(results)

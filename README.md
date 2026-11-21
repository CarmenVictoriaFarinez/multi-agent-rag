# RAG de notas de inglés

Versión sencilla de un asistente que consulta notas locales de inglés con un agente y dos herramientas: búsqueda de texto y recuperación BM25.

> El avance multiagente del proyecto está en la rama `rag_multiagentes` (rama multiagentes).

## Requisitos

- Python 3
- [Ollama](https://ollama.com/) ejecutándose en `http://127.0.0.1:11434`
- Modelos y dependencias:

```powershell
ollama pull qwen2.5-coder:7b
python -m pip install smolagents rank-bm25
```

## Uso

Guarda tus notas como archivos `.txt` en `knowledge/`. Desde la raíz del proyecto, ejecuta:

```powershell
python -m examples.english_rag
```

La pregunta de ejemplo está definida en `examples/english_rag.py`; puedes cambiarla para consultar tus notas.

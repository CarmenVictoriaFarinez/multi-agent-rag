# RAG multiagente

Asistente local para consultar notas de inglés y realizar tareas de traducción, resumen y clasificación gramatical. Un agente gestor identifica la intención y delega la solicitud al agente especializado. Los modelos se ejecutan localmente con Ollama y la coordinación usa `smolagents`.

## Requisitos

- Python 3.
- [Ollama](https://ollama.com/) instalado y ejecutándose en `http://127.0.0.1:11434`.
- Los modelos que utiliza el proyecto:
  - `qwen2.5-coder:7b` para el gestor y el traductor.
  - `llama3.2:3b` para recuperación, resumen y clasificación.

Descarga los modelos antes de ejecutar la aplicación:

```powershell
ollama pull qwen2.5-coder:7b
ollama pull llama3.2:3b
```

## Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual e instala las dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install smolagents rank-bm25
```

Si Ollama no está iniciado como servicio, ejecuta `ollama serve` en otra terminal.

## Notas de conocimiento

Guarda tus notas como archivos `.txt` codificados en UTF-8 dentro de `knowledge/`. El proyecto ya incluye algunos ejemplos. El agente de recuperación utiliza dos herramientas:

- `english_notes`: encuentra líneas que contienen el texto de búsqueda.
- `bm25_notes`: ordena los documentos por relevancia BM25 y devuelve fragmentos; por defecto considera hasta tres documentos.

`bm25_notes` carga su índice al iniciar la aplicación. Reiníciala después de añadir o modificar archivos para que BM25 vuelva a indexarlos.

## Ejecutar

Desde la carpeta raíz del proyecto:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

La consulta inicial está definida en `main.py`, en la variable `query`. Edítala para solicitar, por ejemplo, una búsqueda en tus notas, una traducción, un resumen o una clasificación gramatical; el gestor delegará la solicitud correspondiente. La aplicación procesa una consulta por ejecución.

## Agentes

| Agente | Función |
| --- | --- |
| `manager_agent` | Detecta la intención y delega la solicitud; responde en español. |
| `retrieval_agent` | Consulta los archivos de `knowledge/` mediante `english_notes` y `bm25_notes`. |
| `translator_agent` | Traduce entre idiomas. |
| `summarizer_agent` | Resume textos conservando sus ideas principales. |
| `classifier_agent` | Clasifica textos por tema gramatical e indica evidencia textual. |

El gestor no navega por internet: las consultas RAG se limitan a las notas locales.

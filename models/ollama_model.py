from smolagents import OpenAIServerModel

def get_model(model_id: str = "qwen2.5-coder:7b"):
    return OpenAIServerModel(
        model_id=model_id,
        api_base="http://127.0.0.1:11434/v1",
        api_key="ollama",
    )




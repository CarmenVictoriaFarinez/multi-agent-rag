from smolagents import OpenAIServerModel

def get_model():
    return  OpenAIServerModel(
        model_id="qwen2.5-coder:7b",
        api_base="http://127.0.0.1:11434/v1",
        api_key="ollama",
)

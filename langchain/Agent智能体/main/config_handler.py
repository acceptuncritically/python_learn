from main.path_tool import get_abs_path
import yaml
def load_rag_config():
    with open(get_abs_path("config/rag.yml"), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
def load_chroma_config():
    with open(get_abs_path("config/chroma.yml"), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
def load_agent_config():
    with open(get_abs_path("config/agent.yml"), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
def load_prompts_config():
    with open(get_abs_path("config/prompts.yml"), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
rag_config = load_rag_config()
chroma_config = load_chroma_config()
agent_config = load_agent_config()
prompts_config = load_prompts_config()
if __name__ == "__main__":
    print(rag_config["model"])


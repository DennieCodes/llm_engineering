import yaml
from pathlib import Path

def load_user_prompts(yaml_filename: str = "user_prompt.yaml"):
    prompts_path = Path(__file__).parent.parent / "prompts" / yaml_filename
    with open(prompts_path, "r") as f:
        return yaml.safe_load(f)

def get_user_prompt(prompt_name: str, yaml_filename: str = "user_prompt.yaml"):
    prompts = load_user_prompts(yaml_filename)
    return prompts.get(prompt_name)

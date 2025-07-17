import yaml
from pathlib import Path

def load_prompts(yaml_filename: str = "system_prompt.yaml"):
    prompts_path = Path(__file__).parent.parent / "prompts" / yaml_filename
    with open(prompts_path, "r") as f:
        return yaml.safe_load(f)

def get_prompt(prompt_name: str, yaml_filename: str = "system_prompt.yaml"):
    prompts = load_prompts(yaml_filename)
    return prompts.get(prompt_name)

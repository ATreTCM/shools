from pathlib import Path

import yaml


BASE_DIR = Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'data_base.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)

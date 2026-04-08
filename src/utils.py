import yaml

def load_config(config_path):
    """
    Loads configuration from a YAML file.
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def save_config(config, config_path):
    """
    Saves configuration to a YAML file.
    """
    with open(config_path, 'w') as f:
        yaml.safe_dump(config, f)

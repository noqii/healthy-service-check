from config.config import load_config, CONSTANT_CONFIG_FILENAME

loaded_config = load_config()

def reload_config(file: str = CONSTANT_CONFIG_FILENAME):
    loaded_config = load_config(file)
    return loaded_config

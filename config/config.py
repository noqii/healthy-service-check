import yaml
from config.constants import CONSTANT_CONFIG_FILENAME

def load_config(file: str = CONSTANT_CONFIG_FILENAME):
    config_file = open(file, 'r')

    try:
        config = yaml.load(config_file, yaml.SafeLoader)
        config_file.close()

        return config
    except Exception as error:
        print("[config.load_config] Exception: " + repr(error))
        return None
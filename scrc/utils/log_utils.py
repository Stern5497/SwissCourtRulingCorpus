from root import ROOT_DIR
import os
import yaml
import logging.config
import logging
import coloredlogs

from dotenv import load_dotenv

load_dotenv()


def get_logger(name='debug_logger', default_path=ROOT_DIR / 'logging.yaml', default_level=logging.INFO,
               env_key='LOG_CFG'):
    """
    | **@author:** Prathyush SP
    | Logging Setup
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')

    logger = logging.getLogger(name)
    logger.setLevel(os.getenv("LOGLEVEL", "DEBUG"))
    return logger

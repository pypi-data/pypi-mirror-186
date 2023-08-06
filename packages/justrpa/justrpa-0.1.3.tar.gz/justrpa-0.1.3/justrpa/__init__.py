import logging
import logging.config
import sys
import os
import json
from .errors import *

__version__ = "0.1.3"
DEFAULT_LOGGER_NAME = "robot"

def create_logger(log_level:int, formatter:str, output_stream, name=None) -> logging.Logger:
    log_level = log_level # to set log level
    formatter = logging.Formatter(formatter)
    my_logger = logging.getLogger(name)
    my_logger.setLevel(log_level)
    log_handler = logging.StreamHandler(output_stream)
    log_handler.setLevel(log_level)
    log_handler.setFormatter(formatter)
    my_logger.addHandler(log_handler)
    return my_logger

def create_default_logger()->logging.Logger:
    Default_Log_level = 10
    Default_Formatter = "[%(asctime)s] [%(levelname)s] [%(message)s]"
    Default_Output = sys.stdout
    return create_logger(Default_Log_level, Default_Formatter, Default_Output, DEFAULT_LOGGER_NAME)

def load_logging_config():
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, "conf/logging.json")
    if os.path.isfile(file_path) == False:
        return {}
    with open(file_path, encoding="utf-8") as fp:
            conf = json.load(fp)
    return conf

def _init_logger():
    log_config = load_logging_config()
    if log_config:
        logging.config.dictConfig(log_config)
    if DEFAULT_LOGGER_NAME not in logging.Logger.manager.loggerDict.keys():
        create_default_logger()

_init_logger()
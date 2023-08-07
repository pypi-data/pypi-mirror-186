import logging
import logging.config
from os import getenv
import pathlib
from .config import get_path

config_file = get_path("logging.conf")
if pathlib.Path(config_file).is_file():
    logging.config.fileConfig(config_file, disable_existing_loggers=False)
else:
    logging.basicConfig(
        level=getenv("LOG_LEVEL", "INFO"),
        format="%(threadName)s %(message)s",
        datefmt="[%X]",
        handlers=[logging.StreamHandler()],
    )

logger = logging

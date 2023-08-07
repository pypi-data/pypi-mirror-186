from os import getenv
from pathlib import Path

# This will be the root where we read key and secret from
config_path = getenv('CONFIG_PATH', '/var/run')

def get_path(path: str) -> Path:
  return Path(f'{config_path}/{path}')

def read_config(path: str) -> str:
  return get_path(path).read_text()
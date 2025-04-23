import json
import logging.config
from pathlib import Path


def setup_logging(log_config_path: Path):
    with open(log_config_path) as f:
        log_config = json.loads(f.read())

    logging.config.dictConfig(log_config)

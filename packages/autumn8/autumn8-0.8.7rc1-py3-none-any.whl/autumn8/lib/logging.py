import os
import logging
import logging.config

# pylint: disable=wildcard-import,unused-wildcard-import  # this is a wrapper for the `logging` module
from logging import *
from logging import getLogger as oldGetLogger


import yaml

with open(
    os.path.join(os.path.dirname(__file__), ".", "logging.yaml"),
    "r",
    encoding="utf-8",
) as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


def getLogger(
    name=None,
):  # pylint: disable=invalid-name,function-redefined  # overriding a builtin function from 'logging'
    logger = oldGetLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger

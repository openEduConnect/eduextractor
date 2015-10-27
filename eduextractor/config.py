"""Loads the config file from ~/.eduextractor.yml
which should contain all the passwords, etc, and then exposes them as
Python object.
"""
import yaml
import os
from os.path import expanduser

def _load_secrets(path=None):
    if path is None:
        path = os.path.join(expanduser('~'), '.eduextractor.yml')

    with open(path, 'r') as f:
        data_map = yaml.safe_load(f)
    return data_map

secrets = _load_secrets(os.environ.get('EDUEXTRACTOR_CONFIG'))

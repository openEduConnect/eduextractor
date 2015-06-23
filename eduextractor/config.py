"""Loads the config file from ~/.eduextractor.yml
which should contain all the passwords, etc, and then exposes them as
Python object. 
"""
import yaml 

def _load_secrets(path):
    f = open(path)
    data_map = yaml.safe_load(f)
    return data_map

secrets = _load_secrets('/Users/howens/.eduextractor.yml')



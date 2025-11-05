import os 
import json
import yaml


def parser(filepath):
    format = os.path.splitext(filepath)[1].lower()

    if format == ".json":
        with open(filepath) as file:
            return json.load(file)
    elif format == ".yaml" or format == ".yml":
        with open(filepath) as file:
            return yaml.safe_load(file)

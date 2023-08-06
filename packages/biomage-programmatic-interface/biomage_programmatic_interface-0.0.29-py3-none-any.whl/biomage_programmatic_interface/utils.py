import json
from importlib import resources


def load_json(path):
    with resources.open_text("biomage_programmatic_interface", path) as raw_file:
        json_obj = json.load(raw_file)
    return json_obj


def is_file_hidden(path):
    return path.split("/")[-1][0] == "."

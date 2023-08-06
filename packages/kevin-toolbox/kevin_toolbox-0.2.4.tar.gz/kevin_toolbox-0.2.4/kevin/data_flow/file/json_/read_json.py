import json
from kevin.data_flow.file.json_.converter import integrate


def read_json(file_path, converters=None):
    with open(file_path, 'r') as f:
        obj = json.load(f, object_hook=integrate(converters))
    return obj

import os
import json


def write_json(content, file_path, sort_keys=False):
    file_path = os.path.abspath(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w') as f:
        json.dump(content, f, indent=4, ensure_ascii=False, sort_keys=sort_keys)

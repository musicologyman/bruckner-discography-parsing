import json
import os

import yaml

from collections.abc import Mapping
from typing import Any

from toolz.functoolz import pipe

def get_json_files(path="json_files"):
    return sorted([os.path.join(path, f) for f 
                   in os.listdir(path) if f.endswith(".json")], key=str.lower)

def read_json_file(filename:str):
    with open(filename) as fp:
        return json.load(fp)

def convert_to_yaml(input):
    return yaml.dump(input)

def write_all_text(filename, text):
    with open(filename, mode="w") as fp:
        fp.write(text)

def main():
    for json_file in get_json_files():
        yaml_text = pipe(json_file, 
                         read_json_file,
                         convert_to_yaml)
        yaml_file = "yaml_files/" + json_file[10:-4] + "yaml"
        write_all_text(yaml_file, yaml_text)

if __name__ == "__main__":
    main()

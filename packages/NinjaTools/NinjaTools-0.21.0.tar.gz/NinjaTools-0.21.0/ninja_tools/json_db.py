import json
import os
from functools import reduce
from typing import List


class DB:
    def __init__(self, json_path):
        self.json_path = json_path

        # Check if file exists
        if not os.path.exists(self.json_path):
            # Create file
            with open(self.json_path, 'w') as f:
                json.dump({}, f, indent=4)

    # Function that creates or update nested dictionaries from a list of keys
    # Input dict, list of keys, value
    # Output dict
    def set(self, keys: List, value):
        if not isinstance(keys, list):
            raise TypeError('Keys must be a list')

        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        # Use reduce to check if key exists, if not create it
        reduce(lambda d, key: d.setdefault(key, {}), keys[:-1], data)[keys[-1]] = value

        # Save to file
        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return data

    def get(self, keys: List):
        if not isinstance(keys, list):
            raise TypeError('Keys must be a list')

        with open(self.json_path, 'r', encoding='utf-8') as f:
            try:
                data = json.loads(f.read())
                return reduce(dict.get, keys, data)
            except TypeError:
                return None

    def get_all(self, dump=False):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

        if dump:
            return json.dumps(data, indent=4)
        else:
            return data

    def delete(self, keys: List):
        if not isinstance(keys, list):
            raise TypeError('Keys must be a list')

        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            del reduce(dict.get, keys[:-1], data)[keys[-1]]

        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return data

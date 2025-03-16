import json
import os.path
from typing import Any, List


class JsonFileDB:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load()

    def load(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except Exception as e:
            print(f"Error loading database: {e}")
            return {}

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, path: List[str]) -> Any:
        node = self.data
        for p in path:
            if p not in node:
                raise KeyNotFound(f"Path {path} not found in database")
            node = node[p]
        return node

    def set(self, path: List[str], value: Any):
        node = self.data
        for p in path[:-1]:
            if p not in node:
                node[p] = {}
            node = node[p]
        node[path[-1]] = value
        self.save()

    def delete(self, path: List[str]):
        node = self.data
        for p in path[:-1]:
            if p not in node:
                raise KeyNotFound(f"Path {path} not found in database")
            node = node[p]
        del node[path[-1]]
        self.save()

class KeyNotFound(Exception):
    pass

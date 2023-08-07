import json
import os
from pathlib import Path


def ensure_path_exists(path):
    if not isinstance(path, str):
        raise TypeError(f"path must be of type str:{path}")
    if not os.path.exists(path):
        Path(path).mkdir(parents=True, exist_ok=True)


def to_file(content, path, mode="w+"):
    with open(path, mode) as f:
        f.write(content)


def from_file(path, mode="r"):
    with open(path, mode) as f:
        return f.read()


def save_json(path: str, obj: dict):
    to_file(json.dumps(obj), path)


def load_json(path: str):
    return json.loads(from_file(path))

import glob
import json
import os
import platform
from typing import Any, ByteString, Optional

import yaml

from .exceptions import StorageError


def global_workdir() -> str:
    home_folder = os.path.expanduser("~")
    platform_name = platform.system().lower()

    if platform_name == "linux" \
            or platform_name == "darwin" \
            or platform_name == "windows" \
            or platform_name == "freebsd":
        return os.path.join(home_folder, ".config", "tons")
    else:
        raise OSError("Your operating system is not supported yet")


def local_workdir(local_dir_name) -> str:
    return os.path.join(os.getcwd(), local_dir_name)


def find_local_workdir(local_dir_name) -> Optional[str]:
    system_root = os.path.abspath(os.sep)
    current_dir = os.getcwd()

    path = os.path.join(current_dir, local_dir_name)
    while current_dir != system_root:
        if os.path.exists(path):
            return path
        current_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        path = os.path.join(current_dir, local_dir_name)

    return None


def read_yaml(filepath: str):
    with open(filepath) as f:
        try:
            return yaml.safe_load(f)
        except (yaml.scanner.ScannerError, PermissionError, FileNotFoundError) as e:
            raise StorageError(e)


def read_json(filepath: str):
    with open(filepath, "r") as f:
        return json.loads(f.read())


def read_bytes(filepath: str):
    with open(filepath, "rb") as f:
        return f.read()


def save_json(filepath: str, data: Any):
    ensure_parent_dir_exists(filepath)

    if not data:
        data = None

    with open(filepath, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_yaml(filepath: str, data: Any):
    ensure_parent_dir_exists(filepath)

    if not data:
        data = None

    try:
        with open(filepath, 'w') as f:
            yaml.safe_dump(data, f, default_flow_style=False)
    except (PermissionError, FileNotFoundError) as e:
        raise StorageError(e)


def save_bytes(filepath: str, data: ByteString):
    ensure_parent_dir_exists(filepath)

    try:
        with open(filepath, 'wb') as f:
            f.write(data)
    except (PermissionError, FileNotFoundError) as e:
        raise StorageError(e)


def ensure_parent_dir_exists(filepath: str):
    dirname = os.path.dirname(filepath)
    if dirname:
        ensure_dir_exists(dirname)


def ensure_dir_exists(dirpath: str):
    os.makedirs(dirpath, exist_ok=True)


def exists(path: str):
    return os.path.exists(path)


def get_filenames_by_ptrn(dir: str, pattern: str):
    return glob.glob(os.path.join(dir, pattern))

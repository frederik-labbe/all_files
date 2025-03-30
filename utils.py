import os

from typing import List

def utf_8_challenge(content: str) -> bool:
    try:
        content.encode('utf-8')
        return True
    except:
        return False

def all_files(root: str, filters: List[str] = []):
    for path in [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(root) for f in filenames]:
        if len(filters) > 0 and not path.endswith(tuple(filters)):
            continue

        yield path

def test_arg_enu(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        if 'AFX_ARG_ENU' in f.read():
            return True
        return False
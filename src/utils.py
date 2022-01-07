from pathlib import Path

def get_abs_path(n_parent: int = 0):
    path = Path('../' * n_parent).resolve()
    return str(path)
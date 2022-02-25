import json
import os
from utils import get_abs_path

project_path = get_abs_path(0)
files_path = project_path + '/data/train/planned_maps'

paths = []
for (dirpath, dirnames, filenames) in os.walk(files_path):
            paths.extend(filenames)
            break

paths = sorted(paths)

files = []
for path in paths:
    with open(files_path + "/" + path) as f:
        files.append(json.load(f))

compressed_json = {}
for file in files:
    print(file)
    print(a)

# with open(files_path + 'paths.json', 'w') as f:
#     json.dump(compressed_json, f)
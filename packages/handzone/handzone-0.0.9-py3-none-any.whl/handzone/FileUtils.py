import json
import os
import shutil
from os.path import join


def get_file_list(root, ext=".jpg", max=-1, ret_full=False):
    files = []
    dirs = sorted(os.listdir(root))
    while len(dirs) > 0:
        path = dirs.pop()
        fullname = join(root, path)
        if os.path.isfile(fullname) and fullname.endswith(ext):
            if ret_full:
                files.append(fullname)
            else:
                files.append(path)
        elif os.path.isdir(fullname):
            names = sorted(os.listdir(fullname))
            if max != -1 and os.path.isfile(join(fullname, names[0])):
                names = names[:max]
            for s in names:
                newDir = join(path, s)
                dirs.append(newDir)
    files = sorted(files)
    return files


def read_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def save_json(file, data):
    if file is None:
        return 0
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

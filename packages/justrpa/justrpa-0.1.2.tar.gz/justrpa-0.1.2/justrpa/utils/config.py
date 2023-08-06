import os
import json
import requests

def merge_conf(origin:dict, custom:dict)->dict:
    for key, value in custom.items():
        origin[key] = value
    return origin

def load_conf(filename):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, filename)
    if os.path.isfile(file_path) == False:
        return {}
    with open(file_path, encoding="utf-8") as fp:
            conf = json.load(fp)
    return conf

def load_override_conf(filename, default_dir="conf", override_dir="devdata"):
    path_origin, path_override = [ os.path.join(d, filename) for d in [default_dir, override_dir]]
    conf_default, conf_override = [ load_conf(p) for p in [path_origin, path_override] ]
    return conf_override if len(conf_override) > 0 else conf_default

def load_merge_conf(filename, default_dir="conf",override_dir="devdata"):
    path_origin, path_override = [ os.path.join(d, filename) for d in [default_dir, override_dir]]
    conf_default, conf_override = [ load_conf(p) for p in [path_origin, path_override] ]
    return merge_conf(conf_default, conf_override)

def load_json_from_url(url:str):
    res = requests.get(url)
    data = json.loads(res.text)
    return data
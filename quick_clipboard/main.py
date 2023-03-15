import os
import json
import sys
from pathlib import Path

import yaml
from fuzzywuzzy import process

from quick_clipboard import k8s

SOURCES = {}


def attach_config_cmds():
    cwd = os.path.dirname(os.path.abspath(__file__))
    yaml_files = [f for f in os.listdir(cwd) if f.endswith('.yaml')]
    for f in yaml_files:
        with open(os.path.join(cwd, f), 'r', encoding='utf-8') as file:
            content = yaml.safe_load(file)
            for k, v in content.items():
                SOURCES[Path(f).stem + '_' + k] = v


def attach_module_cmds():
    for module in (k8s,):
        for k, v in module.__dict__.items():
            if k.startswith('__') or not isinstance(v, str):
                continue
            SOURCES[module.__name__.rsplit('.', maxsplit=1)[-1] + '_' + k] = v


def build_arg(origin):
    host_prefix = "host=$(hostname|cut -d. -f1);"
    sysargv = sys.argv[2:] if len(sys.argv) > 2 else []
    args = ""
    for index, v in enumerate(sysargv):
        args += (f"{chr(ord('@')+index+1)}=\"{v}\";")

    if 'host' in origin:
        return host_prefix + args + origin

    return args + origin


def find_best_matches(prompt):
    attach_config_cmds()
    attach_module_cmds()

    matches = process.extractBests(prompt, SOURCES.keys(), limit=10)
    sys.stdout.write(json.dumps({
        "items": [{
            "uid": m[1],
            "type": "file",
            "title": m[0],
            "arg": build_arg(SOURCES[m[0]]),
            "subtitle": SOURCES[m[0]]
        } for m in matches]
    }))


def main():
    find_best_matches(sys.argv[1])


if __name__ == '__main__':
    main()

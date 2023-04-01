import os
import yaml

import uvicorn
from fastapi import FastAPI

app = FastAPI()

icons = {
    'ceph': '💽',
    'docker': '🐳',
    'es': '📊',
    'git': '🐱',
    'golang': '🐹',
    'iscsi': '📀',
    'k8s': '🔥',
    'kubernetes': '🐙',
    'linux': '🐧',
    'mysql': '🐬',
    'python': '🐍',
    'openstack': '🧱',
    'symbol': '🔣',
    'vscode': '📝',
}


@app.get("/subscription")
def get_subscription():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    categories = []
    entries = []
    for file in os.listdir(current_dir):
        if file.endswith(".yaml"):
            filename = file.replace('.yaml', '')
            categories.append({
                'name': filename,
                'icon': icons.get(filename, '😊')
            })
            with open(os.path.join(current_dir, file), encoding='utf-8') as f:
                content = yaml.safe_load(f)
                for k, v in content.items():
                    entries.append({
                        'title': k,
                        'subtitle': v,
                        'category': filename,
                    })

    return {
        'categories': categories,
        'entries': entries,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

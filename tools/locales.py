#!/usr/bin/env python3
"""Schreibt die Lampenshop-Texte (tools/lamp-strings.json) in alle Theme-Sprachdateien.

Aufruf im Repo-Root:  python3 tools/locales.py

Quelle ist tools/lamp-strings.json: { "gruppe.schluessel": { "de": "…", "en": "…" } }.
Deutsch landet in locales/de.json, Englisch in locales/en.default.json und als Rückfall
in allen übrigen Sprachdateien. Der Block "lamp" wird dabei jedes Mal komplett ersetzt,
der Rest der Dateien bleibt unverändert.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
strings = json.load(open(os.path.join(ROOT, 'tools', 'lamp-strings.json'), encoding='utf-8'))


def tree(lang):
    out = {}
    for key, val in strings.items():
        node = out
        parts = key.split('.')
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = val.get(lang, val['en'])
    return out


for path in sorted(glob.glob(os.path.join(ROOT, 'locales', '*.json'))):
    name = os.path.basename(path)
    if name.endswith('.schema.json'):
        continue
    lang = 'de' if name == 'de.json' else 'en'
    block = json.dumps({'lamp': tree(lang)}, indent=2, ensure_ascii=False)
    block = block[block.index('\n') + 1:block.rindex('\n')] + ','  # ohne äußere Klammern
    src = open(path, encoding='utf-8').read()
    src = re.sub(r'\n  "lamp": \{.*?\n  \},', '', src, count=1, flags=re.S)
    start = src.index('{', src.index('*/') + 2 if src.lstrip().startswith('/*') else 0)
    src = src[:start + 1] + '\n' + block + src[start + 1:]
    open(path, 'w', encoding='utf-8').write(src)
print('ok:', len(strings), 'Texte')

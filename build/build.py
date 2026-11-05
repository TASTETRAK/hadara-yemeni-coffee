#!/usr/bin/env python3
"""Rebuild index.html from build/template.html, embedding the assets as base64.

Usage (from the repo root):  python3 build/build.py
Placeholders in the template: {{MARK}} {{WORDMARK}} {{PHOTO_SIGN}} {{PHOTO_WINDOW}}
"""
import base64, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def b64(rel, mime):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode())
html = open(os.path.join(ROOT, 'build', 'template.html'), encoding='utf-8').read()
html = html.replace('{{MARK_BROWN}}', b64('assets/hadara-mark-brown.png', 'image/png'))
html = html.replace('{{MARK}}', b64('assets/hadara-mark.png', 'image/png'))
html = html.replace('{{WORDMARK}}', b64('assets/hadara-wordmark.png', 'image/png'))
html = html.replace('{{PHOTO_SIGN}}', b64('assets/photo-sign.jpg', 'image/jpeg'))
html = html.replace('{{PHOTO_WINDOW}}', b64('assets/photo-window.jpg', 'image/jpeg'))
assert '{{' not in html, 'unreplaced placeholder'
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html', len(html.encode()), 'bytes')

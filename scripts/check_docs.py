#!/usr/bin/env python3
"""Validate local documentation targets, public scope and screenshot provenance."""
import hashlib,json,re
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]; errors=[];links=0
for p in ROOT.rglob('*.md'):
 s=p.read_text()
 targets=re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',s)+re.findall(r'(?:src|href)="([^"]+)"',s)
 for target in targets:
  if target.startswith(('https:','http:','mailto:','#')):continue
  rel=unquote(urlsplit(target).path); links+=1
  if not (p.parent/rel).exists():errors.append(f'{p.relative_to(ROOT)}: missing {target}')
 for label,pattern in [('operational address',r'\b(?:10|192\.168|100\.\d+)\.\d+\.\d+\b'),('private origin',r'(?:proxy\.morloksmaze\.com|morloksmaze\.com|docs\.google\.com/spreadsheets)')]:
  if re.search(pattern,s):errors.append(f'{p.relative_to(ROOT)}: {label}')
for item in json.loads((ROOT/'assets/screenshots/manifest.json').read_text()):
 if hashlib.sha256((ROOT/item['file']).read_bytes()).hexdigest()!=item['sha256']:errors.append(item['file']+': hash mismatch')
theme=ROOT/'sections/13-brass-labyrinth'
for item in json.loads((theme/'screenshots.json').read_text()):
 if hashlib.sha256((theme/item['file']).read_bytes()).hexdigest()!=item['sha256']:errors.append(item['file']+': theme capture hash mismatch')
for item in json.loads((ROOT/'assets/figma/manifest.json').read_text())['boards']:
 if hashlib.sha256((ROOT/item['file']).read_bytes()).hexdigest()!=item['sha256']:errors.append(item['file']+': Figma export hash mismatch')
for folder in (ROOT/'sections').iterdir():
 for name in ['README.md','PLAN.md']:
  if not (folder/name).exists():errors.append(str(folder/name))
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {links} local links, {len(list((ROOT/"sections").iterdir()))} section folders, screenshot/Figma hashes and public text scope')

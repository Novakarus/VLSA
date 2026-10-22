from pathlib import Path
import hashlib,json,re
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
def validate():
 checks=[]
 def check(value,label):
  checks.append(label);assert value,label
 manifest=json.loads((ROOT/'releases/0.69.3/manifest.json').read_text(encoding='utf-8'))
 for name,digest in manifest['files'].items():
  check(hashlib.sha256((ROOT/'plugin'/name).read_bytes()).hexdigest()==digest,'tested source '+name)
 a=json.loads((ROOT/'plugin/plugin.json').read_text(encoding='utf-8-sig'));b=json.loads((ROOT/'plugin/.codex-plugin/plugin.json').read_text(encoding='utf-8-sig'))
 check(a['name']==b['name'] and a['version']==b['version']=='0.69.3','manifest identity/version')
 skills=list((ROOT/'plugin/skills').glob('*/SKILL.md'));check(len(skills)==13,'13 skills')
 for p in skills:check(p.read_text(encoding='utf-8-sig').startswith('---'),'frontmatter '+p.parent.name)
 for p in (ROOT/'docs').rglob('*.html'):
  s=p.read_text(encoding='utf-8');check('lang="vi"' in s,'Vietnamese '+str(p.relative_to(ROOT)))
  check('chưa công bố' not in s and '[ngày công bố' not in s,'published status '+str(p.relative_to(ROOT)))
  for target in re.findall(r'(?:href|src)="([^"]+)"',s):
   u=urlsplit(target)
   if u.scheme or u.netloc or not u.path:continue
   dest=(p.parent/unquote(u.path)).resolve()
   if u.path.endswith('/'):dest=dest/'index.html'
   check(dest.is_file(),'local link '+str(p.relative_to(ROOT))+' -> '+target)
 for p in ROOT.rglob('*'):
  if not p.is_file():continue
  if any(x in {'.git','__pycache__','dist'} for x in p.relative_to(ROOT).parts):continue
  check(not any(x in {'.env','__pycache__','work','runs'} for x in p.relative_to(ROOT).parts),'public path '+str(p.relative_to(ROOT)))
  if p.suffix in {'.md','.html','.json','.py','.yml'}:
   check(not re.search(r'(?:C:\\Users\\|sk-[A-Za-z0-9]{24}|gh[pousr]_[A-Za-z0-9]{30})',p.read_text(encoding='utf-8-sig')),'no local paths/credential patterns '+str(p.relative_to(ROOT)))
 print(json.dumps({'status':'PASS','checks':len(checks),'skills':len(skills),'behavioral_test_run':False}))
if __name__=='__main__':validate()

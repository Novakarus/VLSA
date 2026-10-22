from pathlib import Path
import zipfile,hashlib
from validate import ROOT,validate
validate()
files=list((ROOT/'plugin').rglob('*'))
dest=ROOT/'dist';dest.mkdir(exist_ok=True)
target=dest/'Vietnam-Legal-Advisor-0.69.3.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(files):
  if p.is_file() and p.name!='LICENSE.md':
   entry=zipfile.ZipInfo(p.relative_to(ROOT/'plugin').as_posix(),date_time=(1980,1,1,0,0,0));entry.create_system=0;entry.compress_type=zipfile.ZIP_DEFLATED;entry.external_attr=0o100644<<16;z.writestr(entry,p.read_bytes())
target.with_suffix('.zip.sha256').write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n',encoding='utf-8')
print('Created '+str(target))


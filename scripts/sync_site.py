from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
for p in (root/'docs').rglob('*'):
 if p.is_file() and (p.suffix in {'.html','.css','.png'} or p.name=='.nojekyll'):
  dest=root/p.relative_to(root/'docs');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
print('Updated root compatibility copy from docs/')

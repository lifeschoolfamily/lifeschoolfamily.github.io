import json,sys,base64,glob,os
D='/tmp/claude-tool-results/f2159017-2b0c-5ffc-bdab-ad77f842d036/'
out=sys.argv[1]; ids=sys.argv[2:]
s=''
for i in ids:
    f=glob.glob(D+'*'+i+'*.txt')[0]
    t=json.load(open(f))[0]['text']
    o,_=json.JSONDecoder().raw_decode(t.strip())
    s+=o.strip() if isinstance(o,str) else ''
open(out,'wb').write(base64.b64decode(s)); print(out,os.path.getsize(out))

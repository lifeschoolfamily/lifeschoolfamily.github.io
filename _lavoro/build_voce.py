# Prepara i testi per la voce ElevenLabs: un capitolo per ogni riquadro letto dagli altoparlanti.
import re,os,json,html,sys
from bs4 import BeautifulSoup
SITE='/home/claude/anteprima'; OUT='/home/claude/voce'
TAG='[slow, calm, warm pace] '
def clean(t):
    t=t.replace('4mums','four mums').replace('€',' euro').replace('·',',').replace('→','').replace('«','"').replace('»','"')
    t=re.sub(r'https?://\S+','',t)
    t=re.sub(r'[\U0001F300-\U0001FAFF☀-➿️]','',t)
    t=re.sub(r'\s+',' ',t).strip()
    t=re.sub(r'\s+([.,!?;:])',r'\1',t)
    return t
def text_of(node):
    for x in node.select('a.btn, .btn, .tag, .note-bozza, button, .bars, img, script, .idx, figure, iframe, .meta, .tpills, .crumb'): x.decompose()
    for b in node.find_all(['b','strong']):
        bt=b.get_text(strip=True)
        if bt and not bt.endswith(('.','!','?',':',',')) and b.next_sibling and str(b.next_sibling).strip()[:1] not in ('.',',',':','!','?',')'):
            b.append('.')
    parts=[]
    for el in node.find_all(['h1','h2','h3','h4','p','li','summary']):
        if el.find_parent(['li']) and el.name!='li': continue
        t=clean(el.get_text(' ',strip=True))
        if not t: continue
        if el.name in ('h1','h2','h3','h4','summary','li') and not t.endswith(('.','!','?',':',';')): t+='.'
        parts.append(t)
    return '\n\n'.join(parts)
def soup(p): return BeautifulSoup(open(os.path.join(SITE,p),encoding='utf-8').read(),'html.parser')
CH=[]  # (id, titolo, testo)
# --- Home
m=soup('index.html').find('main'); secs=m.find_all('section',recursive=False)
names=['Benvenuto','Cosa facciamo ogni giorno','Materiali didattici inclusivi','Materiali gratuiti','Quiz di orientamento']
for i,(s,n) in enumerate(zip(secs[:5],names),1): CH.append((f'home-{i}',f'Home · {n}',text_of(s)))
# --- Chi sono
m=soup('chi-sono/index.html').find('main')
CH.append(('chi-0','Chi sono · Benvenuto',text_of(m.find('section'))))
for i,d in enumerate(m.find_all('details'),1):
    n=d.find('summary').get_text(' ',strip=True); CH.append((f'chi-{i}',f'Chi sono · {n}',text_of(d)))
CH.append(('chi-9','Chi sono · Saluto',text_of(m.find_all('section')[-1])))
# --- Libri
m=soup('libri/index.html').find('main'); CH.append(('libri-0','Libri · Introduzione',text_of(m.find('section'))))
for slug,n in [('danza-delle-parentesi','La Danza delle Parentesi'),('specchio-e-finestra','Specchio e Finestra')]:
    m=soup(f'libri/{slug}/index.html').find('main')
    for i,s in enumerate(m.find_all('section'),1): CH.append((f'{slug}-{i}',f'Libri · {n} {i}',text_of(s)))
# --- Materiali omaggio e Contatti
m=soup('materiali-omaggio/index.html').find('main'); CH.append(('omaggio-1','Materiali omaggio',text_of(m.find('section'))))
# --- Blog
B=[]
for d in sorted(os.listdir(os.path.join(SITE,'blog'))):
    p=os.path.join('blog',d,'index.html')
    if not os.path.exists(os.path.join(SITE,p)) or d=='img': continue
    sp=soup(p); t=clean(sp.find('h1').get_text(' ',strip=True)); art=sp.find('article',class_='body')
    date=sp.find(class_='meta').get_text(' ',strip=True) if sp.find(class_='meta') else ''
    B.append((f'blog-{d}',f'Blog · {t}',re.sub(r'\.\.+$','.',t if t.endswith(('.','!','?')) else t+'.')+'\n\n'+text_of(art),date))
pages=[c for c in CH if c[2]]
tot_p=sum(len(c[2]) for c in pages); tot_b=sum(len(b[2]) for b in B)
json.dump({'pagine':[dict(id=a,titolo=b,testo=c) for a,b,c in pages],'blog':[dict(id=a,titolo=b,testo=c) for a,b,c,_ in B]},open(os.path.join(OUT,'voce.json'),'w'),ensure_ascii=False,indent=1)
print('pagine',len(pages),tot_p,'blog',len(B),tot_b)
for c in pages: print(c[0],len(c[2]),'|',c[2][:90].replace('\n',' '))
for b in B: print(b[0][:45],len(b[2]))

# --- EPUB per ElevenLabs Studio: un capitolo per ogni audio
from ebooklib import epub
bk=epub.EpubBook(); bk.set_identifier('lsf-voce-sito'); bk.set_title('Life School Family · Testi per la voce del sito'); bk.set_language('it'); bk.add_author('Mary · Life School Family')
items=[]
for cid,tit,txt in [(a,b,c) for a,b,c in pages]+[(a,b,c) for a,b,c,_ in B]:
    name=f'{cid} | {tit}'
    body=''.join(f'<p>{html.escape((TAG if i==0 else "")+p)}</p>' for i,p in enumerate(txt.split('\n\n')))
    c=epub.EpubHtml(title=name,file_name=f'{cid}.xhtml',lang='it'); c.content=f'<html><head><title>{html.escape(name)}</title></head><body>{body}</body></html>'
    bk.add_item(c); items.append(c)
bk.toc=items; bk.spine=items; bk.add_item(epub.EpubNcx()); bk.add_item(epub.EpubNav())
epub.write_epub(os.path.join(OUT,'LSF voce sito.epub'),bk)
# copia leggibile
with open(os.path.join(OUT,'LSF voce sito.txt'),'w') as f:
    for cid,tit,txt in [(a,b,c) for a,b,c in pages]+[(a,b,c) for a,b,c,_ in B]:
        f.write(f'===== {cid} | {tit} =====\n{TAG}{txt}\n\n')
print('epub ok')

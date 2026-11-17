import json,re,sys,os,html
SITE=sys.argv[1]; DATA=sys.argv[2]
sys.argv=[sys.argv[0],SITE]
exec(open('build_pages.py').read().split("MAT=[")[0])  # head, foot, page()
d=json.load(open(DATA,encoding='utf-8'))
CATS=[('storia','Storia'),('geografia','Geografia'),('italiano','Italiano'),('scienze','Scienze'),('arte','Arte'),('matematica','Matematica'),('inglese','Inglese'),('altro','Feste, gite e altro')]
def cats(t):
    T=t.lower(); c=[]
    if re.search(r'storia|carolingi|feudal|longobard|impero|islam|monachesimo|ottoni|papato|chiesa|popoli italici|paleolitico|civilt|sumeri|polis|atene|grec|fonti storiche|storico|divinit|barbari|mappa e linea|introduzione alla storia|linea del tempo.preistoria',T) and 'arte' not in T.split('_')[-1] : c.append('storia')
    if re.search(r'regioni|lombardia|friuli|italia in cucina|nord italia|europa in mappe',T): c.append('geografia')
    if re.search(r'antologia|testo|testi|analisi logica|analisi grammaticale|vocal|sillab|plurali|leggi|scrivi|volgare|epica|uso dell.h|scarabeo|favola|fiaba|racconto|mito|lettera',T): c.append('italiano')
    if re.search(r'scienz|pianeti|sistema solare|funghi|protisti|metodo scientifico|vulcano|dinosauri|luna|evoluzione|ere geologiche|galassia|virus|vegetali|animali|cellule|materia|procarioti',T): c.append('scienze')
    if re.search(r'kit multimodale arte|arte1|arte_|arte e tempio|diari della bellezza|colori primari|galleria d.arte|scheda del film|schede del libro',T): c.append('arte')
    if re.search(r'area|tabelline|misurazione|organizzare i dati|frazioni|geometria|operazioni',T): c.append('matematica')
    if re.search(r'english',T): c.append('inglese')
    if re.search(r'caccia al tesoro|avvento|biglietto|ded|caa',T): c.append('altro')
    if 'lapbook' in T: c.append('lapbook')
    if re.search(r'1°\s*media|2media|2°\s*media|medie',T): c.append('medie')
    if 'arte' in c and 'storia' in c and 'kit multimodale arte' in T: c.remove('storia')
    return c if any(x not in ('lapbook','medie') for x in c) else c+['altro']
items=[];free_items=[]
for x in d:
    pid=x['path'].split('/')[0]
    pr=x['price']; free=bool(re.search(r'grat',pr,re.I))
    title=re.sub(r'\s*_\s*',' · ',x['title']).replace('[GRATIS] ','').strip(' ·')
    it=dict(id=pid,t=title,p='Gratis' if free else pr,f=free,pg=x['pages'],n='Nuovo' in x['label'],b='Bestseller' in x['label'],k=('bundle' in x['title'].lower() or 'kit scienze' in x['title'].lower() or 'kit multimodale: viaggio' in x['title'].lower()),c=cats(x['title']),u='https://eduki.com/it/materiale/'+x['path'])
    (free_items if free else items).append(it)
# --- Edudoro: solo i materiali che non sono su Eduki ---
EDO=json.load(open(os.path.join(os.path.dirname(DATA),'edudoro_solo.json'),encoding='utf-8'))
EDO_SKIP={'agenda-homeschooler'}  # agenda 2023/24, da chiedere a Mary
edo_free=[]
for x in EDO:
    if x['slug'] in EDO_SKIP: continue
    title=re.sub(r'_?slide\+.*$','',x['title'])
    title=re.sub(r'\s*_\s*',' · ',title).strip(' ·')
    it=dict(id=x['id'],t=title,p='Gratis' if x['free'] else x['price'],f=x['free'],pg='',n=False,b=False,k=False,c=cats(x['title']),u='https://edudoro.eu/it_IT/products/'+x['slug'],src='edudoro')
    (edo_free if x['free'] else items).append(it)
json.dump(edo_free,open(os.path.join(os.path.dirname(DATA),'edudoro_gratis.json'),'w'),ensure_ascii=False,indent=0)
CSS='''
.shop-tools{display:flex;flex-direction:column;gap:10px}
.search{width:100%;font:inherit;font-size:17px;border:3px solid var(--ink);border-radius:14px;padding:12px 14px;background:#fff}
.chips2{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px;-webkit-overflow-scrolling:touch}
.chips2 button{flex:0 0 auto;font:inherit;font-size:14px;font-weight:800;border:2.5px solid var(--ink);border-radius:999px;padding:6px 14px;background:#fff;cursor:pointer}
.chips2 button[aria-pressed=true]{background:var(--ink);color:#fff}
.count{font-size:14px;font-weight:700;color:#444}
.pgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
@media(min-width:640px){.pgrid{grid-template-columns:repeat(3,minmax(0,1fr))}}
.prod{position:relative;background:#fff;border:3px solid var(--ink);border-radius:18px;box-shadow:4px 4px 0 var(--ink);padding:10px;display:flex;flex-direction:column;gap:8px;text-decoration:none;color:inherit}
.prod img{width:100%;aspect-ratio:3/4;object-fit:cover;object-position:top;border:2px solid var(--ink);border-radius:12px;background:var(--tint)}
.prod h3{font-size:14px;line-height:1.25;font-weight:800}
.prod .row{display:flex;align-items:center;justify-content:space-between;gap:6px;margin-top:auto}
.price{font-weight:800;font-size:17px}
.price.free{color:var(--green)}
.pgs{font-size:12px;font-weight:700;color:#555}
.go{display:block;text-align:center;background:var(--red);color:#fff;border:2.5px solid var(--ink);border-radius:12px;padding:8px;font-weight:800;font-size:14px;box-shadow:2px 2px 0 var(--ink)}
.tag{position:absolute;top:16px;left:16px;font-size:11px;font-weight:800;border:2px solid var(--ink);border-radius:999px;padding:2px 8px;background:var(--yellow)}
.tag.new{background:var(--green);color:#fff}
.prod img.ed{object-fit:contain;object-position:center;background:#fff}
.go.ed{background:var(--blue)}
'''
chips=[('','Tutti'),('lapbook','Lapbook'),('medie','Blocchi studio medie'),('nuovi','Novità'),('bundle','Pacchetti')]+CATS
btns=''.join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if not k else "false"}">{n}</button>' for k,n in chips)
body=f'''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <div class="side"><div class="txt"><h1>Materiali</h1><p class="lead">Scopri i materiali didattici inclusivi di Life School Family.</p></div>
  <img src="../img/indica-busto.webp?v=2" alt=""></div>
</section>
<section class="shop-tools">
  <input class="search" type="search" placeholder="Cerca un materiale…" aria-label="Cerca un materiale">
  <div class="chips2" role="group" aria-label="Filtra">{btns}</div>
  <p class="count"></p>
</section>
<div class="pgrid" id="pgrid"></div>
<section class="card yellow">
  <p><b>Ti piacciono le nostre risorse? C'è molto altro da esplorare!</b></p>
  <p>Scegli la tua piattaforma preferita ed esplora i cataloghi!</p>
  <div class="plat">
    <a href="https://edudoro.eu/it_IT/vendors/life-school-family" target="_blank" rel="noopener"><img src="../img/materiali/edudoro.webp" alt="Edudoro"></a>
    <a href="https://eduki.com/it/autore/3412802/life-school-family-1" target="_blank" rel="noopener"><img src="../img/materiali/eduki.webp" alt="Eduki"></a>
  </div>
</section>
<script>
const P={json.dumps(items,ensure_ascii=False)};
const g=document.getElementById('pgrid'),q=document.querySelector('.search'),cnt=document.querySelector('.count');let F='';
function esc(s){{return s.replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c])}}
function draw(){{const s=q.value.trim().toLowerCase();const L=P.filter(p=>(!F||(F==='gratis'?p.f:F==='nuovi'?p.n:F==='bundle'?p.k:p.c.includes(F)))&&(!s||p.t.toLowerCase().includes(s)));
g.innerHTML=L.map(p=>`<a class="prod" href="${{p.u}}" target="_blank" rel="noopener">${{p.n?'<span class="tag new">Nuovo</span>':p.b?'<span class="tag">Bestseller</span>':''}}${{p.src?`<img class="ed" src="../img/edudoro/${{p.id}}.webp" alt="" loading="lazy">`:`<img src="../img/eduki/${{p.id}}.webp" alt="" loading="lazy">`}}<h3>${{esc(p.t)}}</h3><div class="row"><span class="price ${{p.f?'free':''}}">${{p.p}}</span>${{p.pg?`<span class="pgs">${{p.pg}} pag.</span>`:''}}</div>${{p.src?'<span class="go ed">Vedi su Edudoro</span>':'<span class="go">Vedi su Eduki</span>'}}</a>`).join('');
cnt.textContent=L.length+(L.length===1?' materiale':' materiali');}}
document.querySelectorAll('.chips2 button').forEach(b=>b.addEventListener('click',()=>{{F=b.dataset.f;document.querySelectorAll('.chips2 button').forEach(x=>x.setAttribute('aria-pressed',x===b));draw()}}));
q.addEventListener('input',draw);draw();
</script>'''
CSS_EXTRA+=CSS
page(os.path.join(SITE,'materiali','index.html'),'Materiali | Life School Family','I materiali didattici inclusivi di Life School Family: lapbook, kit multimodali di storia, scienze, italiano, arte e geografia.','Materiali',body)
from collections import Counter
print(len(items), Counter(c for i in items for c in i['c']), sum(i['f'] for i in items),'gratis', sum(i['k'] for i in items),'bundle')
for i in items:
    if i['c']==['altro']: print('ALTRO:',i['t'])

json.dump(free_items,open(os.path.join(os.path.dirname(DATA),'eduki_gratis.json'),'w'),ensure_ascii=False,indent=0)
print('gratis tolti:',[i['t'] for i in free_items])

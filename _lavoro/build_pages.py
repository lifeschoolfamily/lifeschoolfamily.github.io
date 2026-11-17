import re,sys,os,html
SITE=sys.argv[1]
tpl=open(os.path.join(SITE,'blog','index.html'),encoding='utf-8').read()
head,rest=tpl.split('<main class="wrap">',1)
foot=rest.split('</main>',1)[1]
foot=re.sub(r'<script>.*?</script>','',foot,flags=re.S)
CSS_EXTRA='''
.mgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.mcard{background:#fff;border:3px solid var(--ink);border-radius:18px;box-shadow:4px 4px 0 var(--ink);padding:10px;display:flex;flex-direction:column;gap:8px}
.mcard img{width:100%;aspect-ratio:3/4;object-fit:cover;object-position:top;border:2px solid var(--ink);border-radius:12px;background:var(--tint)}
.mcard h3{font-size:15px;line-height:1.2}
.mcard .btn{min-height:44px;font-size:15px;box-shadow:3px 3px 0 var(--ink);margin-top:auto}
.guide{display:flex;flex-direction:column;gap:12px}
.guide img{width:100%;border:3px solid var(--ink);border-radius:16px}
.plat{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.plat a{display:flex;align-items:center;justify-content:center;background:#fff;border:3px solid var(--ink);border-radius:16px;box-shadow:4px 4px 0 var(--ink);padding:10px;min-height:70px}
.plat img{max-width:100%;max-height:56px}
.form-ph{background:#fff;border:3px dashed var(--ink);border-radius:16px;padding:16px;display:flex;flex-direction:column;gap:10px}
.form-ph .f{border:2.5px solid var(--ink);border-radius:12px;padding:12px;color:#777;background:#fff}
.form-ph .note{font-size:13px;color:#555}
.idx{display:flex;flex-wrap:wrap;gap:8px}
.idx a{border:2.5px solid var(--ink);border-radius:999px;padding:6px 14px;font-weight:800;background:#fff;text-decoration:none;font-size:14px}
'''
def page(out, title, desc, here, body, noindex=False):
    h=head
    h=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)}</title>',h,flags=re.S)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(desc)}">',h)
    if noindex: h=h.replace('<meta charset="utf-8">','<meta charset="utf-8"><meta name="robots" content="noindex, nofollow, noarchive">')
    h=h.replace('</style>',CSS_EXTRA+'</style>')
    h=h.replace(' class="here"','')
    if here: h=h.replace(f'>{here}</a>',f' class="here">{here}</a>',1).replace(f'<a href',f'<a href',0)
    # fix: the class must be inside <a ...>
    h=re.sub(r'(<a href="[^"]*")> class="here">',r'\1 class="here">',h)
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'w',encoding='utf-8').write(h+'<main class="wrap">\n'+body+'\n</main>'+foot)

MAT=[('m01','Colori Primari e Secondari','1h2qfkq2Jnt4kKxM0Vly9tkNM02pE24MQ'),
('m02','Mappa Fonti Storiche + attività','1pPKHSA0P74E2fRDXMDAUJPIBIE-D72F6'),
('m03','Template Lapbook Mitologia Greca','1bVoTw74IOzojE2WnvOno23sMrehW3TJH'),
('m04',"Cartina dell'Italia: i Piatti Tipici",'1YT-2iqmFrVQBKs1CqZIZdvpTg9APjZ8u'),
('m05','Frazioni Colorate','1eQD-9a8Dn1qbDdXFcUwFA0qvhmdSIHkh'),
('m06','English - Avverbi di Luogo','1oGde1mGgbhiRQqIH4D0zsGOBNeBnr5Xi'),
('m07','Template Lapbook Vulcano da Compilare','1nRBaABIpTh1hnVPgba7Y3Hs0W9oODZXe'),
('m08','Template Lapbook Testo Poetico da Compilare','1ReYfteX6wbgsh6kRcJwoAs2Cb3sK2iXO'),
('m09','Template Lapbook Testo Narrativo da Compilare','1UB-dLdYXm6xKaDqf0xTyZPqAl9xOSlKT'),
('m10','Divinità Egizie da Colorare','1atlE1pgyWIMQ-jPMKb2La8--_6jXwhOl')]
PLAT='''<section class="card yellow">
  <p><b>Ti piacciono le nostre risorse gratuite? C'è molto altro da esplorare!</b></p>
  <p>Scegli la tua piattaforma preferita ed esplora i cataloghi!</p>
  <div class="plat">
    <a href="https://edudoro.eu/it_IT/vendors/life-school-family" target="_blank" rel="noopener"><img src="../img/materiali/edudoro.webp" alt="Edudoro"></a>
    <a href="https://eduki.com/it/autore/3412802/life-school-family-1" target="_blank" rel="noopener"><img src="../img/materiali/eduki.webp" alt="Eduki"></a>
  </div>
</section>'''
def card(k,t,i):
    return f'''<div class="mcard"><img src="../img/materiali/{k}.webp" alt="{html.escape(t)}" loading="lazy"><h3>{html.escape(t)}</h3><a class="btn green" href="https://drive.google.com/file/d/{i}/view" target="_blank" rel="noopener">Scarica Gratis</a></div>'''
groups=[MAT[0:4],MAT[4:8],MAT[8:10]]
body='''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <h1>Materiali Didattici</h1>
  <div class="idx"><a href="#materiali-gratuiti">Materiali Didattici Gratuiti</a><a href="#guide-gratuite">Guide Pratiche Gratuite</a></div>
</section>
<h2 id="materiali-gratuiti">Materiali Didattici Gratuiti</h2>
'''
for g in groups:
    body+='<div class="mgrid">'+''.join(card(*m) for m in g)+'</div>\n'+PLAT+'\n'
import json as _j
_F=[x for x in _j.load(open('/home/claude/shop/eduki_gratis.json',encoding='utf-8')) if x['id'] not in ('1941197','1486393','1941213','1943617')]
if _F:
    body+='<div class="mgrid">'+''.join(f'<div class="mcard"><img src="../img/eduki/{x["id"]}.webp" alt="{html.escape(x["t"])}" loading="lazy"><h3>{html.escape(x["t"])}</h3><a class="btn green" href="{x["u"]}" target="_blank" rel="noopener">Scarica Gratis</a></div>' for x in _F)+'</div>\n'+PLAT+'\n'
body+='''<h2 id="guide-gratuite">Guide Pratiche Gratuite</h2>
<section class="card guide">
  <img src="../img/materiali/g01.webp" alt="Bambini Neurodivergenti ai Campi Estivi" loading="lazy">
  <h3 style="font-size:21px">Bambini Neurodivergenti ai Campi Estivi</h3>
  <p>Questa guida è la vostra "pillola" di inclusione immediata. Attraverso il nostro Metodo Multimodale, trasformiamo il campo estivo in un ambiente sereno e accogliente, fornendo soluzioni concrete nate dall'esperienza in trincea per abbattere le barriere cognitive e sensoriali, permettendo a ogni mente di brillare.</p>
  <p><b>Contenuto del Pacchetto.</b></p>
  <p><b>Infografica "5 Cose da Fare":</b> Strategie di cuore per coinvolgere attivamente il bambino, valorizzando la sua neurodiversità come risorsa.</p>
  <p><b>Infografica "5 Cose da NON Fare":</b> Errori da evitare per prevenire stress e isolamento, garantendo un'estate di successo per tutti.</p>
  <p><b>Checklist Operativa:</b> Uno strumento visivo per educatori che hanno poco tempo ma tanta voglia di fare la differenza.</p>
  <a class="btn green" href="https://drive.google.com/file/d/1MvogGzXNJGzBz6hgcMnb_kOKXINNhg4c/view" target="_blank" rel="noopener">Scarica Gratis</a>
</section>
'''+PLAT
page(os.path.join(SITE,'materiali-didattici','index.html'),'Materiali Didattici | Life School Family','Materiali didattici gratuiti di Life School Family.',None,body,noindex=True)

body2='''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <div class="side"><div class="txt"><h1>Unisciti a noi e Accedi ai Materiali Didattici Gratuiti di Life School Family</h1></div>
  <img src="../img/idea-busto.webp" alt=""></div>
</section>
<section class="card tint">
  <div class="form-ph">
    <b>[ Qui va il modulo Brevo dei materiali omaggio ]</b>
    <div class="f">La vostra mail</div>
    <a class="btn blue" href="../materiali-didattici/index.html">VOGLIO I MATERIALI</a>
    <p class="note">Nell'anteprima il pulsante porta direttamente alla pagina riservata. Sul sito vero: chi lascia la mail riceve da Brevo una mail con il link alla pagina riservata.</p>
  </div>
</section>
<div class="mgrid">'''+''.join(f'<div class="mcard"><img src="../img/materiali/{k}.webp" alt="{html.escape(t)}" loading="lazy"><h3>{html.escape(t)}</h3></div>' for k,t,i in MAT[:4])+'</div>'
page(os.path.join(SITE,'materiali-omaggio','index.html'),'Materiali omaggio | Life School Family','Materiali didattici gratuiti di Life School Family: lascia la tua mail e accedi.','Materiali omaggio',body2)
print('ok')

SOC=[('Instagram','https://www.instagram.com/life_school_family/','life_school_family','var(--red)'),
('YouTube','https://www.youtube.com/@LifeSchoolFamily.Italia','@LifeSchoolFamily.Italia','var(--red)'),
('Facebook','https://www.facebook.com/LifeSchoolFamily.it','LifeSchoolFamily.it','var(--blue)'),
('Pinterest','https://it.pinterest.com/life_school_family/','life_school_family','var(--green)'),
('TikTok','https://www.tiktok.com/@lifeschoolfamily','@lifeschoolfamily','var(--ink)')]
soc=''.join(f'<a class="post" href="{u}" target="_blank" rel="noopener"><small style="display:flex;align-items:center;gap:8px"><i style="width:14px;height:14px;border-radius:999px;border:2px solid var(--ink);background:{c};display:inline-block"></i>{n}</small><span>{h}</span></a>' for n,u,h,c in SOC)
body3=f'''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <div class="side"><div class="txt"><h1>Contatti e social</h1></div>
  <img src="../img/saluto-busto.webp" alt="Mary di Life School Family che saluta"></div>
</section>
<section class="card yellow">
  <h2>Scrivimi</h2>
  <a class="btn blue" href="mailto:lifeschoolfamily.shop@gmail.com">lifeschoolfamily.shop@gmail.com</a>
</section>
<section class="card tint">
  <h2>Vieni a conoscerci sui social</h2>
  <div class="posts">{soc}</div>
</section>
<section class="card">
  <h2>I nostri materiali</h2>
  <div class="plat">
    <a href="https://edudoro.eu/it_IT/vendors/life-school-family" target="_blank" rel="noopener"><img src="../img/materiali/edudoro.webp" alt="Edudoro"></a>
    <a href="https://eduki.com/it/autore/3412802/life-school-family-1" target="_blank" rel="noopener"><img src="../img/materiali/eduki.webp" alt="Eduki"></a>
  </div>
</section>'''
page(os.path.join(SITE,'contatti','index.html'),'Contatti e social | Life School Family','Contatti di Life School Family: mail, Instagram, YouTube, Facebook, Pinterest e TikTok.','Contatti e social',body3)
print('contatti ok')

CHI_CSS='''
details.cap{background:#fff;border:3px solid var(--ink);border-radius:18px;box-shadow:4px 4px 0 var(--ink);overflow:hidden}
details.cap summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px;font-weight:800;font-size:20px}
details.cap summary::-webkit-details-marker{display:none}
details.cap summary::after{content:"+";flex:0 0 auto;width:34px;height:34px;border:2.5px solid var(--ink);border-radius:999px;display:flex;align-items:center;justify-content:center;font-size:22px;background:var(--yellow)}
details.cap[open] summary::after{content:"–"}
details.cap[open] summary{border-bottom:2.5px dashed var(--ink)}
details.cap .in{padding:14px 16px 18px;display:flex;flex-direction:column;gap:12px;font-size:17px}
details.cap summary:focus-visible{outline:3px solid var(--blue);outline-offset:-3px}
'''
CSS_EXTRA+=CHI_CSS
def cap(t,ps,color):
    return f'<details class="cap"><summary><span style="display:flex;align-items:center;gap:10px"><i style="width:14px;height:14px;border-radius:999px;border:2px solid var(--ink);background:{color};display:inline-block"></i>{t}</span></summary><div class="in">'+''.join(f'<p>{p}</p>' for p in ps)+'</div></details>'
body4='''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <div class="side"><div class="txt"><h1>Chi sono</h1>
  <p class="lead">Ciao! Entra pure, qui non serve bussare.</p>
  <p>Sono Maria Silvia Santi, ma per quasi tutti sono Mary. Tata Mary dal 2011, per la precisione. Siediti un attimo: ti racconto da dove arriva tutto questo.</p></div>
  <img src="../img/saluto-busto.webp" alt="Mary di Life School Family che saluta"></div>
</section>
'''+cap('Tata Mary',["Vivo a Bologna e lavoro con i bambini da più di vent'anni. Sono educatrice diplomata.","Nel 2011 ho aperto Tata Mary: un servizio di tate condivise. Niente asilo, niente struttura. Una casa, un piccolo gruppo di bambini, al massimo cinque per ogni adulto. Pasti veri, a km 0. Un orto curato dai bambini stessi, con le mani nella terra e le scarpe da lavare la sera.","La cosa più bella? Crescere insieme a loro. Vederli arrivare in braccio e, anni dopo, vederli correre via verso la scuola senza voltarsi. E crescere anche con le loro famiglie: affiancarle, non sostituirle. I genitori restavano i genitori. Io ero un pezzo in più della loro rete, quello che c'è quando serve.","Per quindici anni è stata la mia casa, anche quando la casa era piena di stivaletti bagnati.","Poi ho dovuto chiudere. E fa ancora male. Non si chiude un servizio: si salutano bambini, mamme, papà, nonni. Si chiude una parte di te.","Ma quello che ho imparato in quella casa non se n'è andato. È tutto qui, in ogni materiale che preparo."],'var(--red)')+cap('4mums',["Poi è nata 4mums. L'ho fondata insieme all'ostetrica e alla doula che mi hanno accompagnata quando i miei figli sono nati in casa. Sapevamo bene quanto conta non essere sole, all'inizio.","Io mi occupavo di fasce e babywearing, come consulente certificata, e della pannolinoteca dei lavabili: tante mamme hanno imparato da me a portare i loro piccoli addosso e a lavare un pannolino senza paura."],'var(--green)')+cap('I miei tre uragani',["E poi sono arrivati loro: Beatrice, Ginevra e Federico. I miei tre uragani. Con loro è arrivata anche la scelta che ha cambiato tutto: l'istruzione parentale.","Non l'ho vissuta come un dovere da sbrigare. È diventata il nostro modo di stare insieme. Ogni giorno preparo io i loro materiali: blocchi di studio, lapbook, mappe, giochi. Li costruisco su misura, perché ogni testa impara a modo suo, e una scheda uguale per tutti non va bene per nessuno."],'var(--blue)')+cap('Life School Family',["Da lì è nata Life School Family. Quello che funziona a casa nostra lo metto a disposizione di altre famiglie e di chi insegna, soprattutto di chi ha davanti una mente che non segue la strada dritta. ADHD, DSA, plusdotazione: qui non sono etichette da nascondere, sono modi di funzionare da conoscere.","Di materiali ne ho preparati circa 300. Su Eduki ed Edudoro ne trovi già una parte. Gli altri? Prima o poi li caricherò tutti. Promesso. Più o meno.",'<a class="btn green" href="../materiali/index.html">Guarda i materiali</a>'],'#E07A00')+cap('I libri',['Scrivo anche libri: li trovi nella pagina Libri.'],'#C2185B')+'''
<section class="card yellow">
  <p class="lead">Se leggendo hai riconosciuto un pezzo di casa tua, scrivimi. Anche solo per raccontarmi com'è la tua giornata, o per chiedermi una cosa che non hai il coraggio di chiedere altrove.</p>
  <p>Rispondo io, sempre. A volte tra un lapbook e una lavatrice, ma rispondo.</p>
  <a class="btn blue" href="../contatti/index.html">Scrivimi</a>
</section>'''
page(os.path.join(SITE,'chi-sono','index.html'),'Chi sono | Life School Family',"Mary, Maria Silvia Santi: educatrice, Tata Mary dal 2011, mamma in istruzione parentale e fondatrice di Life School Family.",'Chi sono',body4)
print('chi sono ok')

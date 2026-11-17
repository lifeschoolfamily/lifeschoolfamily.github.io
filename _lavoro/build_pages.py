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
def page(out, title, desc, here, body, noindex=False, js=''):
    h=head
    h=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)}</title>',h,flags=re.S)
    h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(desc)}">',h)
    if noindex: h=h.replace('<meta charset="utf-8">','<meta charset="utf-8"><meta name="robots" content="noindex, nofollow, noarchive">')
    h=h.replace('</style>',CSS_EXTRA+'</style>')
    h=h.replace(' class="here"','')
    if here: h=h.replace(f'>{here}</a>',f' class="here">{here}</a>',1).replace(f'<a href',f'<a href',0)
    # fix: the class must be inside <a ...>
    h=re.sub(r'(<a href="[^"]*")> class="here">',r'\1 class="here">',h)
    f=foot
    if out.replace(SITE,'').strip('/').count('/')==2:
        for a in ('href="../','src="../'):
            h=h.replace(a,a.replace('../','../../')); f=f.replace(a,a.replace('../','../../'))
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'w',encoding='utf-8').write(h+'<main class="wrap">\n'+body+'\n</main>'+(f.replace('</body>',js+'\n</body>') if js else f))

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
_E=_j.load(open('/home/claude/shop/edudoro_gratis.json',encoding='utf-8'))
if _F:
    body+='<div class="mgrid">'+''.join(f'<div class="mcard"><img src="../img/eduki/{x["id"]}.webp" alt="{html.escape(x["t"])}" loading="lazy"><h3>{html.escape(x["t"])}</h3><a class="btn green" href="{x["u"]}" target="_blank" rel="noopener">Scarica Gratis</a></div>' for x in _F)+'</div>\n'+PLAT+'\n'
if _E:
    body+='<div class="mgrid">'+''.join(f'<div class="mcard"><img src="../img/edudoro/{x["id"]}.webp" alt="{html.escape(x["t"])}" loading="lazy" style="object-fit:contain;object-position:center;background:#fff"><h3>{html.escape(x["t"])}</h3><a class="btn green" href="{x["u"]}" target="_blank" rel="noopener">Scarica Gratis</a></div>' for x in _E)+'</div>\n'+PLAT+'\n'
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
  <img src="../img/idea-busto.webp?v=2" alt=""></div>
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
  <img src="../img/saluto-busto.webp?v=2" alt="Mary di Life School Family che saluta"></div>
</section>
<section class="card yellow">
  <h2>Scrivimi</h2>
  <a class="btn blue" href="mailto:lifeschoolfamily.shop@gmail.com">lifeschoolfamily.shop@gmail.com</a>
  <a class="btn green" href="https://wa.me/393386523639" target="_blank" rel="noopener">WhatsApp 338 65 23 639</a>
</section>
<section class="card tint" id="newsletter">
  <h2>La newsletter</h2>
  <div class="form-ph">
    <b>[ Qui va il modulo Brevo della newsletter ]</b>
    <div class="f">La vostra mail</div>
    <span class="btn blue">ISCRIVITI</span>
  </div>
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
  <img src="../img/saluto-busto.webp?v=2" alt="Mary di Life School Family che saluta"></div>
</section>
'''+cap('Tata Mary',["Vivo a Bologna e lavoro con i bambini da più di vent'anni. Sono educatrice diplomata.","Nel 2011 ho aperto Tata Mary: un servizio di tate condivise. Niente asilo, niente struttura. Una casa, un piccolo gruppo di bambini, al massimo cinque per ogni adulto. Pasti veri, a km 0. Un orto curato dai bambini stessi, con le mani nella terra e le scarpe da lavare la sera.","La cosa più bella? Crescere insieme a loro. Vederli arrivare in braccio e, anni dopo, vederli correre via verso la scuola senza voltarsi. E crescere anche con le loro famiglie: affiancarle, non sostituirle. I genitori restavano i genitori. Io ero un pezzo in più della loro rete, quello che c'è quando serve.","Per quindici anni è stata la mia casa, anche quando la casa era piena di stivaletti bagnati.","Poi ho dovuto chiudere. E fa ancora male. Non si chiude un servizio: si salutano bambini, mamme, papà, nonni. Si chiude una parte di te.","Ma quello che ho imparato in quella casa non se n'è andato. È tutto qui, in ogni materiale che preparo."],'var(--red)')+cap('4mums',["I miei figli sono nati in casa. Accanto a me c'erano un'ostetrica e una doula. Quando tutto è finito, o meglio, quando tutto è cominciato, ci siamo guardate e abbiamo pensato la stessa cosa: nessuna mamma dovrebbe sentirsi sola, in quei primi mesi.","Così, nel 2016, è nata 4mums.","Io mi occupavo di fasce e babywearing: sono consulente certificata. Insegnavo alle mamme, e a molti più papà e nonni di quanto possiate immaginare, a portare i loro piccoli addosso. Pancia contro pancia, mani libere, cuore vicino.","E poi c'era la pannolinoteca dei lavabili. Pannolini da provare prima di comprarli, da toccare, da lavare insieme. Sembra una cosa da niente, finché non ti trovi alle tre di notte con un neonato in braccio e mille dubbi in testa.","Oggi non la seguo più direttamente, ma 4mums c'è ancora, ed è viva. Vive grazie all'ostetrica Carlotta Tonelli, alla doula Stefania Fioravanti e a tutte le professioniste e i professionisti che ci portano la loro esperienza: corsi in gravidanza, incontri tra mamme, allattamento, psicomotricità, la fascioteca.",'<a class="btn green" href="https://www.team4mums.com" target="_blank" rel="noopener">Scopri 4mums</a>'],'var(--green)')+cap('I miei tre uragani',["E poi sono arrivati loro. Tre teste diverse, tre modi di stare al mondo, una casa che non sta mai zitta.","<b>Beatrice</b> è la creatrice di mondi. Viola ovunque, idee a getto continuo e un'adolescenza appena cominciata, che arriva come un temporale d'estate: all'improvviso, e piena di vita.","<b>Ginevra</b> è il nostro sole. E il nostro terremoto. Gira per casa ridendo e sbattendo dappertutto, perché non guarda mai dove va: è già alla cosa dopo. Ogni mattina però si infila nel lettone per dieci minuti di coccole, e la giornata parte giusta.","<b>Federico</b> è il nostro marmottino. Lego, dinosauri, vulcani: ne parla per ore, anche con gli sconosciuti al parco. La casa è invasa dai suoi disegni, e in ognuno ci siamo noi.","E poi c'è <b>Francesco</b>. La mia roccia. Non mi \"aiuta\": fa la sua parte. Siamo genitori insieme, cinquanta e cinquanta. È lui che mi porta un bicchiere d'acqua quando parto per la tangente, che costruisce il carrello con le rotelle per tutti i Lego, che tante volte vede le cose prima di me. Noi cinque siamo una squadra, sempre.","L'istruzione parentale non è stata un salto nel buio. È stata il naturale proseguimento di Tata Mary. Il modo di seguire i bambini è lo stesso di quella casa: piccoli gruppi, tempi lenti, le mani nelle cose. Solo che stavolta è cresciuto insieme a loro. Dal cortile e dall'orto siamo passati ai libri, alle mappe, alla storia, alle scienze.","Ogni giorno preparo io i loro materiali: blocchi di studio, lapbook, mappe, giochi. Li costruisco su misura, perché ogni testa impara a modo suo, e una scheda uguale per tutti non va bene per nessuno.","Io e Francesco vogliamo che sappiano una cosa sola: vanno bene così. Il mondo forse non è ancora pronto. Noi sì.",'<a class="btn blue" href="../blog/eccoli-qui-vi-presento-i-miei-tre/index.html">Conoscili meglio nel blog</a>'],'var(--blue)')+cap('Life School Family',["Vita, scuola, famiglia. Per me sono la stessa cosa: un filo unico che si intreccia tutti i giorni, al tavolo della cucina.","Proprio da qui è nata Life School Family. Quello che funziona a casa nostra lo metto a disposizione di altre famiglie e di chi insegna, soprattutto di chi ha davanti una mente che non segue la strada dritta. ADHD, DSA, plusdotazione: qui non sono etichette da nascondere, sono modi di funzionare da conoscere.","Come lavoro? Mescolo le materie come in cucina. Un po' di matematica con i Lego, la storia con un gioco di ruolo, le scienze con le mani in pasta. Mappe colorate da guardare, alette da aprire, cose da toccare. E si ride, tanto, perché si impara meglio quando ci si diverte.","Poi ci sono i film. Da noi la sera sul divano non finisce coi titoli di coda. Un film diventa una porta: la storia che c'è dietro, la geografia dei posti, la scienza di quello che succede sullo schermo, le emozioni dei personaggi. Lo guardiamo, ne parliamo, e da lì parte un percorso di studio vero, che attraversa più materie insieme. Per questo preparo anche schede di analisi cinematografica, perché imparare dallo schermo si può, se qualcuno ti insegna a guardare.","Dietro c'è tanto studio. Alli Beltrame e Valeria Mattaliano, con l'Educazione Responsabile, sono la mia bussola: prima la relazione, poi il voto. Da Gardner ho imparato le intelligenze multiple, da Pikler e Malaguzzi l'osservazione profonda. Ogni bambino è unico, e merita un modo tutto suo.","Una mamma una volta mi ha scritto: \"Mio figlio ha sorriso mentre faceva storia. Prima piangeva.\" È per questo che lo faccio.","Di materiali ne ho preparati circa 300. Su Eduki ed Edudoro ne trovi già una parte. Gli altri? Prima o poi li caricherò tutti. Promesso. Più o meno.","Una sola richiesta: diffondi il piacere di imparare, non il file.",'<a class="btn green" href="../materiali/index.html">Guarda i materiali</a>','<a class="btn" href="../materiali-omaggio/index.html">Materiali gratuiti</a>'],'#E07A00')+cap('I libri',["Chi stampa materiali a casa lo sa: la stampante finisce l'inchiostro sempre la sera prima. Le pagine escono storte, poi bisogna rilegare, bucare, cercare la cartellina giusta.","Per questo alcuni dei miei materiali sono diventati libri. Belli da tenere in mano, pratici da usare, già pronti. Si aprono e si comincia, senza stampare niente. Fanno risparmiare inchiostro, carta e soprattutto tempo, che in una casa con tre bambini è la cosa più preziosa.","Ci sono libri di attività, come \"Danza delle Parentesi\" e il Calendario dell'Avvento \"Specchio e Finestra\". E ci sono le agende, per tenere in ordine giornate che di ordinato hanno poco.",'<a class="btn" style="background:#C2185B;color:#fff" href="../libri/index.html">Scopri i libri</a>'],'#C2185B')+'''
<section class="card yellow">
  <p class="lead">Se leggendo hai riconosciuto un pezzo di casa tua, scrivimi. Anche solo per raccontarmi com'è la tua giornata, o per chiedermi una cosa che non hai il coraggio di chiedere altrove.</p>
  <p>Rispondo io, sempre. A volte tra un lapbook e una lavatrice, ma rispondo.</p>
  <a class="btn blue" href="../contatti/index.html">Scrivimi</a>
  <a class="btn green" href="../contatti/index.html#newsletter">Iscriviti alla newsletter</a>
</section>'''
page(os.path.join(SITE,'chi-sono','index.html'),'Chi sono | Life School Family',"Mary, Maria Silvia Santi: educatrice, Tata Mary dal 2011, mamma in istruzione parentale e fondatrice di Life School Family.",'Chi sono',body4,js='<script src="../js/voce.js" data-pagina="chi" data-base="../audio/voce/" defer></script>')
print('chi sono ok')

# ================= LIBRI =================
CSS_LIBRI='''
.books{display:flex;flex-direction:column;gap:18px}
.book{background:#fff;border:3px solid var(--ink);border-radius:18px;box-shadow:4px 4px 0 var(--ink);padding:14px;display:grid;grid-template-columns:120px 1fr;gap:14px;align-items:start}
.book img{width:100%;border:2px solid var(--ink);border-radius:10px;box-shadow:3px 3px 0 var(--ink)}
.book h2{font-size:20px;line-height:1.15;margin:0 0 6px}
.book p{margin:0 0 8px}
.book .tag{display:inline-block;font-size:13px;font-weight:800;border:2px solid var(--ink);border-radius:999px;padding:2px 10px;background:var(--yellow);margin:0 6px 8px 0}
.book .btn{min-height:44px;font-size:15px}
.bhero{display:grid;grid-template-columns:1fr;gap:16px}
.bhero img{width:min(320px,80%);margin:0 auto;display:block;border:3px solid var(--ink);border-radius:14px;box-shadow:5px 5px 0 var(--ink)}
.porte{display:flex;flex-direction:column;gap:10px}
.porte div{border:3px solid var(--ink);border-radius:14px;padding:10px 14px}
.facts{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px}
.facts li{border-bottom:2px dashed #ccc;padding:6px 0}
.note-bozza{background:#FFF3BF;border:3px dashed var(--ink);border-radius:14px;padding:12px 14px;font-size:14px}
.legal h2{font-size:19px;margin-top:18px}
.legal p,.legal li{font-size:16px}
@media(min-width:720px){.book{grid-template-columns:170px 1fr}.bhero{grid-template-columns:300px 1fr;align-items:start}.bhero img{width:100%}}
'''
CSS_EXTRA+=CSS_LIBRI
DANZA_AMZ='https://www.amazon.it/dp/B0GZ1ZFJ94'
AVV_AMZ='https://www.amazon.it/dp/B0HRNKV19Y'
AVV_EDUKI='https://eduki.com/it/material/2441856/calendario-avvento---specchio-e-finestra'

libri_idx='''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <h1>I libri</h1>
  <p class="lead">Niente stampante, niente inchiostro finito la sera prima. Si apre il libro e si comincia.</p>
  <p>Alcuni dei miei materiali sono diventati libri veri, di carta. Li trovi su Amazon.</p>
</section>
<div class="books">
<article class="book"><a href="danza-delle-parentesi/index.html"><img src="../img/libri/danza.webp" alt="Copertina del libro La Danza delle Parentesi e altre avventure"></a><div>
<h2>La Danza delle Parentesi e altre avventure</h2>
<span class="tag">Matematica</span><span class="tag">7-13 anni</span>
<p>Più di 150 giochi per imparare la matematica con il corpo, le mani e la testa. Per famiglie, insegnanti e chi fa istruzione parentale.</p>
<a class="btn blue" href="danza-delle-parentesi/index.html">Scopri il libro</a></div></article>
<article class="book"><a href="specchio-e-finestra/index.html"><img src="../img/libri/avvento.webp" alt="Copertina del Calendario dell'Avvento Specchio e Finestra"></a><div>
<h2>Calendario dell'Avvento "Specchio e Finestra"</h2>
<span class="tag">Avvento</span><span class="tag">8-13 anni</span>
<p>24 giorni per guardarsi dentro e guardarsi negli occhi. Una domanda vera al giorno, per ragazzi e per gli adulti che vivono con loro.</p>
<a class="btn red" href="specchio-e-finestra/index.html">Scopri il calendario</a></div></article>
<article class="book"><a href="agende/index.html"><img src="../img/libri/agenda.webp" alt="Copertina dell'Agenda d'Autore 2026/2027"></a><div>
<h2>Le agende</h2>
<span class="tag">2026/2027</span>
<p>Per tenere in ordine giornate che di ordinato hanno poco.</p>
<a class="btn green" href="agende/index.html">Guarda le agende</a></div></article>
</div>
<section class="card yellow">
  <p>I link portano ad Amazon. Se compri da lì, una piccola parte arriva a me come autrice, e a te non costa niente in più.</p>
</section>'''
page(os.path.join(SITE,'libri','index.html'),'I libri | Life School Family',"I libri di Mary di Life School Family: La Danza delle Parentesi, il Calendario dell'Avvento Specchio e Finestra e le agende.",'Libri',libri_idx)

danza='''<p><a href="../index.html">← Tutti i libri</a></p>
<section class="card"><div class="bhero">
<img src="../../img/libri/danza.webp" alt="Copertina del libro La Danza delle Parentesi e altre avventure">
<div><h1>La Danza delle Parentesi e altre avventure</h1>
<p class="lead">Basta soffrire per la matematica.</p>
<p>Questo libro è nato sul pavimento della mia cucina. Tra mattoncini Lego, hula-hoop e fogli piegati male. E da una domanda che non mi lasciava in pace: e se il problema non fosse il bambino, ma il modo in cui gli offriamo la matematica?</p>
<a class="btn blue" href="'''+DANZA_AMZ+'''" target="_blank" rel="noopener sponsored">Compralo su Amazon</a></div></div></section>
<section class="card"><h2>Tre porte per entrare</h2>
<p>Ogni argomento si può aprire da tre porte diverse. Scegli quella che funziona per il tuo bambino, o provale tutte.</p>
<div class="porte">
<div style="background:#E3F7EC"><b>Porta cinestetica.</b> La matematica si salta, si corre, si mima. Un angolo retto si capisce meglio con le braccia che con il goniometro.</div>
<div style="background:#FFF3BF"><b>Porta sensoriale.</b> Bottoni, legumi, farina, calzini. La matematica passa dalle dita prima di arrivare alla testa.</div>
<div style="background:#E6EBFF"><b>Porta logica.</b> Carte, sfide, giochi da tavolo. Si ragiona per vincere, e intanto si impara.</div></div></section>
<section class="card"><h2>Cosa c'è dentro</h2>
<ul class="facts">
<li>Gli insiemi</li><li>Le espressioni</li><li>Le frazioni</li><li>La geometria</li><li>Le potenze</li><li>mcm e MCD</li>
<li>Il metodo a spirale: si torna sugli stessi argomenti, ogni volta con un gioco nuovo</li></ul>
<p>Un esempio? Il diagramma di Venn diventa due hula-hoop in giardino. E chi ha sia le scarpe bianche sia gli occhiali deve stare in mezzo. Lo capisce con i piedi, prima che con la testa.</p></section>
<section class="card"><h2>Per chi è</h2>
<ul class="facts"><li>Bambini e ragazzi dai 7 ai 13 anni</li><li>Genitori stanchi della guerra dei compiti</li><li>Insegnanti che vogliono portare la vita vera in classe</li><li>Famiglie in istruzione parentale</li><li>Ogni tipo di cervello: ADHD, autismo, DSA, plusdotazione</li></ul>
<p>Togliti le scarpe. Siediti per terra con noi. Nessuno resta fuori.</p>
<a class="btn blue" href="'''+DANZA_AMZ+'''" target="_blank" rel="noopener sponsored">Compralo su Amazon</a></section>'''
page(os.path.join(SITE,'libri','danza-delle-parentesi','index.html'),'La Danza delle Parentesi | Life School Family',"La Danza delle Parentesi e altre avventure: più di 150 giochi di matematica multimodale per bambini e ragazzi dai 7 ai 13 anni.",'Libri',danza.replace('href="../index.html">← Tutti','href="../index.html">← Tutti'))

avv='''<p><a href="../index.html">← Tutti i libri</a></p>
<section class="card"><div class="bhero">
<img src="../../img/libri/avvento.webp" alt="Copertina del Calendario dell'Avvento Specchio e Finestra">
<div><h1>Calendario dell'Avvento "Specchio e Finestra"</h1>
<p class="lead">Conoscersi, crescere, volersi bene.</p>
<p>Questo calendario non cambia la vita in sette minuti al giorno. Nessun calendario lo fa.</p>
<p>Fa un'altra cosa: dal 1° al 24 dicembre mette la famiglia intorno al tavolo a guardarsi. Ognuno dentro di sé, e poi negli occhi degli altri.</p>
<a class="btn red" href="'''+AVV_AMZ+'''" target="_blank" rel="noopener sponsored">Il libro su Amazon</a>
<a class="btn" href="'''+AVV_EDUKI+'''" target="_blank" rel="noopener">Il PDF su Eduki</a></div></div></section>
<section class="card"><h2>Come funziona ogni giorno</h2>
<ul class="facts">
<li><b>La storia.</b> Si parte da un racconto, un fumetto, un quadro o una canzone.</li>
<li><b>Lo strumento.</b> Una pagina pratica, con una tecnica da provare subito.</li>
<li><b>Lo specchio.</b> Una stella da colorare dal centro verso fuori. Niente numeri, niente punteggi.</li>
<li><b>La finestra.</b> Un'attività da fare con qualcun altro e un pezzo da ritagliare.</li>
<li><b>La mappa della tribù.</b> Ogni pezzo ritagliato va su un cartellone, uno solo per tutta la famiglia. Il 24 dicembre, al centro, va il cuore della tribù.</li></ul></section>
<section class="card"><h2>Le quattro settimane</h2>
<div class="idx"><a>Chi sono</a><a>Come funziono</a><a>Io e gli altri</a><a>Noi e il domani</a></div>
<p>Si scrive pochissimo. Si colora, si ritaglia, si mette una crocetta. È un gioco, non un compito.</p>
<p>Serve poco: matite colorate, forbici, colla e un cartellone grande. E se saltate un giorno, il cartellone non si rovina.</p></section>
<section class="card yellow"><h2>Libro o PDF?</h2>
<p><b>Il libro su Amazon</b> arriva già pronto: si apre e si comincia, senza stampare niente.</p>
<p><b>Il PDF su Eduki</b> lo stampi tu, in tre versioni: a colori, in bianco e nero da colorare, in scala di grigi.</p>
<a class="btn red" href="'''+AVV_AMZ+'''" target="_blank" rel="noopener sponsored">Il libro su Amazon</a>
<a class="btn" href="'''+AVV_EDUKI+'''" target="_blank" rel="noopener">Il PDF su Eduki</a></section>'''
page(os.path.join(SITE,'libri','specchio-e-finestra','index.html'),"Calendario dell'Avvento Specchio e Finestra | Life School Family","Calendario dell'Avvento Specchio e Finestra: 24 giorni di gioco per conoscersi e volersi bene, per ragazzi dagli 8 ai 13 anni e le loro famiglie.",'Libri',avv)

ag='''<p><a href="../index.html">← Tutti i libri</a></p>
<section class="card"><div class="bhero">
<img src="../../img/libri/agenda.webp" alt="Copertina dell'Agenda d'Autore 2026/2027">
<div><h1>Le agende</h1>
<p class="lead">Agenda d'Autore 2026/2027</p>
<p>Per tenere in ordine giornate che di ordinato hanno poco.</p>
<p class="note-bozza">BOZZA: qui vanno la descrizione delle agende e i link Amazon che mi mandi tu.</p>
</div></div></section>'''
page(os.path.join(SITE,'libri','agende','index.html'),"Le agende | Life School Family","Le agende di Life School Family per l'anno 2026/2027.",'Libri',ag)

# ================= CONSIGLIATI =================
cons='''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <h1>Consigliati</h1>
  <p class="lead">Le cose che usiamo davvero, a casa nostra.</p>
  <p>Niente lista infinita. Solo quello che è passato dal nostro tavolo e ci è rimasto.</p>
</section>
<p class="note-bozza">BOZZA: le sezioni sono un'idea. I prodotti li scegli tu, e i link arrivano quando avremo l'account di affiliazione.</p>
<section class="card"><h2>Per stampare e costruire lapbook</h2><p class="note-bozza">Esempi da scegliere: plastificatrice, taglierina, cartoncini colorati, colla, fermacampioni.</p></section>
<section class="card"><h2>Per la matematica con le mani</h2><p class="note-bozza">Esempi: regoli, abaco, dadi, bilancia, Lego.</p></section>
<section class="card"><h2>Giochi da tavolo che insegnano</h2><p class="note-bozza">I giochi che usate di più in famiglia.</p></section>
<section class="card"><h2>Libri che mi hanno cambiato lo sguardo</h2><p class="note-bozza">Beltrame e Mattaliano, Gardner, Pikler, Malaguzzi...</p></section>
<section class="card yellow"><p><b>In trasparenza:</b> in qualità di Affiliato Amazon io ricevo un guadagno dagli acquisti idonei. A te non costa niente in più, e io consiglio solo quello che usiamo davvero.</p></section>'''
page(os.path.join(SITE,'consigliati','index.html'),'Consigliati | Life School Family',"Gli strumenti, i giochi e i libri che Mary usa davvero a casa per l'istruzione parentale.",'Consigliati',cons)

# ================= PRIVACY =================
priv='''<section class="card legal">
<h1>Privacy</h1>
<p class="lead">Ultimo aggiornamento: novembre 2026</p>
<p class="note-bozza">BOZZA da far controllare a un professionista prima della pubblicazione.</p>
<h2>Chi tratta i dati</h2>
<p>Il sito Life School Family è curato da Maria Silvia Santi (Mary). Per qualsiasi domanda sui tuoi dati scrivi a <a href="mailto:lifeschoolfamily.shop@gmail.com">lifeschoolfamily.shop@gmail.com</a>.</p>
<h2>Cosa succede quando visiti il sito</h2>
<p>Il sito è ospitato su GitHub Pages (GitHub Inc.). Come ogni servizio di hosting, GitHub può registrare dati tecnici delle visite, ad esempio l'indirizzo IP, per motivi di sicurezza e funzionamento. Io non li vedo e non li uso.</p>
<p>Il sito non usa cookie di profilazione, non usa strumenti di statistica e non mostra pubblicità. I caratteri sono caricati dal sito stesso, senza passare da servizi esterni.</p>
<h2>Video</h2>
<p>Alcuni articoli del blog contengono video di YouTube in modalità "privacy avanzata" (youtube-nocookie.com). Quando premi play, YouTube (Google) può raccogliere dati secondo la sua informativa.</p>
<h2>Link ad altri siti</h2>
<p>Nel sito trovi link ad Amazon, Eduki, Edudoro, Instagram, Facebook, YouTube, WhatsApp e altri. Quando li apri, valgono le regole privacy di quei siti.</p>
<p>Alcuni link ad Amazon sono link di affiliazione: se compri, Amazon sa che arrivi da qui e a me riconosce una piccola percentuale. Amazon può usare cookie per farlo. Io non ricevo i tuoi dati personali, solo il totale delle vendite.</p>
<h2>Se mi scrivi</h2>
<p>Se mi scrivi via mail o WhatsApp, uso i tuoi dati solo per risponderti. Non li passo a nessuno.</p>
<h2>Newsletter e materiali omaggio</h2>
<p>Se ti iscrivi alla newsletter o chiedi i materiali omaggio, il tuo nome e la tua mail vengono salvati su Brevo (Sendinblue SAS, Francia), il servizio che uso per spedire le mail. Li uso solo per mandarti le mie mail. Puoi cancellarti quando vuoi con il link in fondo a ogni messaggio.</p>
<h2>Il test e i colloqui</h2>
<p>Il test "Dopo le medie? Tre strade per te!" ha una sua pagina con le sue informazioni. Le prenotazioni passano da Cal.com e i pagamenti da Stripe.</p>
<h2>I tuoi diritti</h2>
<p>Puoi chiedermi in ogni momento di vedere, correggere o cancellare i tuoi dati, scrivendo a <a href="mailto:lifeschoolfamily.shop@gmail.com">lifeschoolfamily.shop@gmail.com</a>. Puoi anche rivolgerti al Garante per la protezione dei dati personali (garanteprivacy.it).</p>
</section>'''
page(os.path.join(SITE,'privacy','index.html'),'Privacy | Life School Family',"Informativa privacy del sito Life School Family.",None,priv)
print('libri consigliati privacy ok')

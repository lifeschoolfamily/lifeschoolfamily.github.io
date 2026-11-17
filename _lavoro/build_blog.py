"""Genera il blog nuovo di Life School Family.
Uso: python3 build_blog.py <json del blog> <cartella del sito> [cartella immagini locali]
Scrive <sito>/blog/index.html e <sito>/blog/<slug>/index.html.
Le immagini: se esiste <sito>/blog/img/<slug>/<n>.<ext> usa quella, altrimenti l'indirizzo di Blogger.
"""
import json, re, sys, os, html
from bs4 import BeautifulSoup, NavigableString, Comment

SRC, SITE = sys.argv[1], sys.argv[2]

TEMI = [
    ("neurodiversita", "Capire la neurodiversità", "var(--blue)"),
    ("adhd-dsa", "ADHD, DSA, autismo, plusdotazione", "var(--red)"),
    ("istruzione-parentale", "Istruzione parentale", "var(--green)"),
    ("materiali-metodo", "Materiali e metodo", "#7B3FE4"),
    ("esperimenti", "Esperimenti e scienze", "#E07A00"),
    ("famiglia", "Vita di famiglia", "#C2185B"),
]
NOMI = {k: (n, c) for k, n, c in TEMI}
# slug -> temi (approvati da Mary il 17/11/2026)
ASSEGNA = {
    "il-linguaggio-segreto-della": ["neurodiversita"],
    "essere-non-avere-perche-la": ["neurodiversita"],
    "la-neurodiversita-non-e-un-guasto-e-un": ["neurodiversita", "materiali-metodo"],
    "quando-lintuizione-dellamore-vale-piu": ["adhd-dsa"],
    "plusdotazione-perche-il-qi-di-tuo": ["adhd-dsa"],
    "dsa-non-e-pigrizia-e-un-cervello-che": ["adhd-dsa"],
    "adhd-quello-che-nessuno-ti-dice-finche": ["adhd-dsa"],
    "life-school-family-quando-la-vita-la": ["istruzione-parentale"],
    "in-istruzione-parentale-la-colpa-e": ["istruzione-parentale"],
    "perche-i-materiali-inclusivi-sono-la": ["materiali-metodo"],
    "dalla-fiaba-alla-scienza-perche-olio-e": ["esperimenti"],
    "eccoli-qui-vi-presento-i-miei-tre": ["famiglia"],
    "la-mia-roccia-il-ruolo-del-papa-nel": ["famiglia"],
    "pasqua-tra-big-bang-lasagne-e-il": ["famiglia"],
    "quando-leccellenza-diventa-veleno": ["famiglia"],
}
MESI = "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split()

def data_it(iso):
    y, m, g = iso[:10].split("-")
    return f"{int(g)} {MESI[int(m)-1]} {y}"

home = open(os.path.join(SITE, "index.html"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", home, re.S).group(1)
CSS += """
.crumb{font-size:15px;font-weight:700}
.meta{font-size:14px;font-weight:700;color:#444}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.tpill{display:inline-flex;align-items:center;border:2px solid var(--ink);border-radius:999px;padding:3px 12px;font-size:13px;font-weight:800;color:#fff;text-decoration:none}
.filters{display:flex;flex-wrap:wrap;gap:8px}
.filters button{font:inherit;font-size:14px;font-weight:800;border:2.5px solid var(--ink);border-radius:999px;padding:6px 14px;background:#fff;cursor:pointer}
.filters button[aria-pressed=true]{background:var(--ink);color:#fff}
.plist{display:flex;flex-direction:column;gap:16px}
.pcard{display:flex;flex-direction:column;gap:8px;text-decoration:none;color:inherit}
.pcard h2{font-size:19px;line-height:1.2}
.pcard p.ex{font-size:16px;color:#222}
.more{font-weight:800;color:var(--blue)}
article.body{font-size:17px;line-height:1.6}
article.body > * + *{margin-top:14px}
article.body h2{font-size:21px;margin-top:26px}
article.body h3{font-size:18px;margin-top:22px}
article.body h4{font-size:18px;margin-top:18px}
article.body ul,article.body ol{padding-left:24px}
article.body li + li{margin-top:6px}
article.body figure{margin:18px 0}
article.body figure img{display:block;width:100%;height:auto;border:3px solid var(--ink);border-radius:16px;background:var(--tint);min-height:60px}
article.body hr{border:0;border-top:3px dashed var(--ink);margin:24px 0}
.thumb{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;border:3px solid var(--ink);border-radius:14px;background:var(--tint)}
.keys{font-size:13px;color:#555}
"""

def header(root, here):
    voci = [("Home", root + "index.html"), ("Chi sono", root + "chi-sono/index.html"),
            ("Materiali", root + "materiali/index.html"), ("Libri", root + "libri/index.html"), ("Consigliati", root + "consigliati/index.html"), ("Materiali omaggio", root + "materiali-omaggio/index.html"),
            ("Blog", root + "blog/index.html"), ("Quiz orientamento", "https://lifeschoolfamily.github.io/tre-strade/"), ("Contatti e social", root + "contatti/index.html")]
    li = "".join(f'<li><a{" class=\"here\"" if n == here else ""} href="{u}">{n}</a></li>' for n, u in voci)
    return f'''<div class="strip">BLACK FRIDAY EDUKI!!! Fino a domenica 29 novembre tutto al 50% con il codice <b>LIFE_K924V7</b></div>
<header><div class="bar"><a class="brand" href="{root}index.html"><img class="lg" src="{root}img/logo.png" alt="Logo Life School Family"><img class="sc" src="{root}img/scritta.png" alt="Life School Family"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu" onclick="var n=document.getElementById('menu');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">☰ Menu</button></div>
<nav id="menu"><ul>{li}</ul></nav></header>'''

FOOTER_T = '''<footer><div class="in"><p>© 2026 Life School Family. Tutti i diritti riservati.</p><p>Risorse create da Life School Family: diffondi il piacere di imparare, non il file.</p><p><a href="mailto:lifeschoolfamily.shop@gmail.com">lifeschoolfamily.shop@gmail.com</a> · <a href="{root}privacy/index.html">Privacy</a></p></div></footer>'''

def page(title, desc, root, here, body, extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="{root}img/logo.png"><link rel="stylesheet" href="{root}fonts/fonts.css">
{extra_head}<style>{CSS}</style></head><body>
{header(root, here)}
<main class="wrap">
{body}
</main>
{FOOTER_T.replace('{root}',root)}
</body></html>'''

KEEP = {"p", "h2", "h3", "h4", "ul", "ol", "li", "b", "strong", "i", "em", "a", "br", "hr", "blockquote"}

def clean(raw, slug):
    soup = BeautifulSoup(raw, "html.parser")
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    # immagini: ogni img diventa figure a sé
    n = 0
    for img in soup.find_all("img"):
        n += 1
        a = img.find_parent("a")
        src = (a.get("href") if a and a.get("href") and "googleusercontent" in a.get("href", "") else img.get("src"))
        src = re.sub(r"/(s\d+|w\d+-h\d+[^/]*)/", "/s1200/", src)
        src = re.sub(r"=(s\d+|w\d+-h\d+[^/]*)$", "=s1200", src)
        ext = os.path.splitext(src.split("?")[0])[1].lower() or ".jpg"
        local = None
        if len(sys.argv) > 3:
            for e in (ext, ".webp", ".jpg", ".png"):
                f = os.path.join(SITE, "blog", "img", slug, f"{n}{e}")
                if os.path.exists(f):
                    local = f"img/{slug}/{n}{e}"  # relativo a blog/<slug>/ → ../img/
                    break
        fig = soup.new_tag("figure")
        new = soup.new_tag("img", src=("../" + local) if local else src, alt=img.get("alt", "") or "", loading="lazy")
        fig.append(new)
        (a or img).replace_with(fig)
    # togli gli attributi e i tag inutili
    for hh in soup.find_all(["h1", "h2", "h3", "h4"]):
        if hh.find(["p", "div", "ul", "ol"]):
            hh.unwrap()
    BLOCK = ["p", "h1", "h2", "h3", "h4", "ul", "ol", "li", "div", "figure", "blockquote", "hr"]
    for t in reversed(soup.find_all(True)):
        if t.name == "figure" or t.name == "img":
            continue
        if t.name in ("h1",):
            t.name = "h2"
        if t.name not in KEEP:
            blocky = t.name == "div" or t.name.startswith("labs") or "display: block" in (t.get("style") or "")
            if blocky and not t.find(BLOCK) and t.find_parent(["p", "li", "h2", "h3", "h4"]) is None:
                t.name = "p"; t.attrs = {}
            else:
                t.unwrap()
            continue
        t.attrs = {k: v for k, v in t.attrs.items() if t.name == "a" and k == "href"}
    out = str(soup)
    out = out.replace("\xa0", " ").replace("&nbsp;", " ")
    # le figure non possono stare dentro un <p>: le porto fuori
    soup = BeautifulSoup(out, "html.parser")
    for fig in soup.find_all("figure"):
        par = fig.find_parent(["p", "b", "i", "em", "strong", "li"])
        while par is not None:
            par.insert_after(fig.extract())
            par = fig.find_parent(["p", "b", "i", "em", "strong", "li"])
    # paragrafi e grassetti vuoti
    changed = True
    while changed:
        changed = False
        for t in soup.find_all(["p", "b", "strong", "i", "em", "h2", "h3", "h4", "li"]):
            if not t.get_text(strip=True) and not t.find(["figure", "img"]):
                t.decompose(); changed = True
    # br doppi in testa/coda
    out = str(soup)
    out = re.sub(r"(<br/?>\s*){2,}", "<br>", out)
    out = re.sub(r">\s*<br/?>\s*</", "></", out)
    return out.strip(), n

def excerpt(clean_html, n=190):
    t = BeautifulSoup(clean_html, "html.parser").get_text(" ", strip=True)
    t = re.sub(r"\s+", " ", t)
    if len(t) <= n:
        return t
    return t[:n].rsplit(" ", 1)[0] + "…"

def pills(temi, root):
    return '<div class="pills">' + "".join(
        f'<a class="tpill" style="background:{NOMI[k][1]}" href="{root}blog/index.html#{k}">{NOMI[k][0]}</a>' for k in temi) + "</div>"

data = json.load(open(SRC, encoding="utf-8"))
posts = []
for p in data["posts"]:
    slug = p["url"].rstrip("/").split("/")[-1].replace(".html", "")
    body, nimg = clean(p["html"], slug)
    posts.append(dict(slug=slug, title=p["title"].strip(), date=p["published"], labels=p.get("labels", []),
                      body=body, temi=ASSEGNA[slug], ex=excerpt(body), old=p["url"], nimg=nimg))
posts.sort(key=lambda x: x["date"], reverse=True)

os.makedirs(os.path.join(SITE, "blog"), exist_ok=True)
for i, p in enumerate(posts):
    root = "../../"
    prev = posts[i + 1] if i + 1 < len(posts) else None
    nxt = posts[i - 1] if i > 0 else None
    nav = ""
    if nxt: nav += f'<a class="post" href="../{nxt["slug"]}/index.html"><small>Articolo più recente</small><span>{html.escape(nxt["title"])}</span></a>'
    if prev: nav += f'<a class="post" href="../{prev["slug"]}/index.html"><small>Articolo precedente</small><span>{html.escape(prev["title"])}</span></a>'
    body = f'''<p class="crumb"><a href="../index.html">← Tutti gli articoli</a></p>
<section class="card">
  {pills(p["temi"], root)}
  <h1 style="font-size:26px">{html.escape(p["title"])}</h1>
  <p class="meta">{data_it(p["date"])} · Mary di Life School Family</p>
</section>
<section class="card"><article class="body">
{p["body"]}
</article>
<p class="keys">Parole chiave: {html.escape(", ".join(p["labels"]))}</p>
</section>
<div class="posts">{nav}</div>
<a class="btn blue" href="../index.html">Tutti gli articoli</a>'''
    d = os.path.join(SITE, "blog", p["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
        page(p["title"] + " | Life School Family", p["ex"], root, "Blog", body))

# elenco
cards = ""
for p in posts:
    cards += f'''<a class="card pcard" href="{p["slug"]}/index.html" data-temi="{" ".join(p["temi"])}">
  <img class="thumb" src="img/{p["slug"]}/1.webp" alt="" loading="lazy">
  <span class="meta">{data_it(p["date"])}</span>
  <h2>{html.escape(p["title"])}</h2>
  <p class="ex">{html.escape(p["ex"])}</p>
  <div class="pills">{"".join(f'<span class="tpill" style="background:{NOMI[k][1]}">{NOMI[k][0]}</span>' for k in p["temi"])}</div>
  <span class="more">Leggi l'articolo →</span>
</a>'''
btns = '<button type="button" data-t="" aria-pressed="true">Tutti</button>' + "".join(
    f'<button type="button" data-t="{k}" aria-pressed="false">{n}</button>' for k, n, c in TEMI)
script = """<script>
(function(){var b=document.querySelectorAll('.filters button'),c=document.querySelectorAll('.pcard');
function show(t){b.forEach(function(x){x.setAttribute('aria-pressed',x.dataset.t===t)});
c.forEach(function(x){x.style.display=(!t||x.dataset.temi.split(' ').indexOf(t)>=0)?'':'none'})}
b.forEach(function(x){x.addEventListener('click',function(){show(x.dataset.t);try{history.replaceState(null,'',x.dataset.t?'#'+x.dataset.t:location.pathname)}catch(e){}})});
function fromHash(){var h=location.hash.slice(1);show(document.querySelector('.filters button[data-t="'+h+'"]')?h:'')}
window.addEventListener('hashchange',fromHash);fromHash();})();
</script>"""
body = f'''<section class="card">
  <div class="bars" aria-hidden="true"><i style="background:#FF3131"></i><i style="background:#00BF63"></i><i style="background:#5170FF"></i></div>
  <h1>Il blog</h1>
  <p class="lead">Neurodiversità, istruzione parentale, materiali e vita di famiglia.</p>
</section>
<div class="filters" role="group" aria-label="Scegli un tema">{btns}</div>
<div class="plist">{cards}</div>
{script}'''
open(os.path.join(SITE, "blog", "index.html"), "w", encoding="utf-8").write(
    page("Il blog | Life School Family", "Il blog di Life School Family: neurodiversità, ADHD, DSA, autismo, plusdotazione, istruzione parentale, materiali inclusivi e vita di famiglia.", "../", "Blog", body))
print("articoli:", len(posts), "immagini:", sum(p["nimg"] for p in posts))

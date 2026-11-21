/* Commenti del blog di Life School Family – modulo "fatto in casa".
   Chi commenta scrive nome e commento: finiscono in un Google Modulo di Mary
   (foglio "Commenti del blog - Life School Family (Risposte)" nel suo Drive).
   I commenti approvati stanno nel foglio "Commenti blog LSF - Pubblicati"
   (pubblicato sul web in CSV): compaiono qui sotto solo le righe con la
   casella "pubblicato" spuntata. Come riserva si legge anche blog/commenti.json
   (chiave = nome della cartella dell'articolo). */
(function () {
  /* foglio "Pubblicati", scheda "Commenti", pubblicato sul web in CSV */
  var CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR__lMzmNjW-pzaRniWJrIswuiT42DdxhtpKoHYIem2ZyJY2jqMl_D8rKHOud5awa8xvn4ncXvBvJo3/pub?gid=1142690083&single=true&output=csv";
  var DEST ="https://docs.google.com/forms/d/e/1FAIpQLSdvEh4tC-o_prZx3bbnYdzxS3e4DsvNvUeSF-qRoY6FN9uqlg/formResponse";
  var E = { articolo: "entry.980406699", nome: "entry.1617996346", commento: "entry.1637038581", mail: "entry.859030588" };
  /* modulo Brevo "Materiali omaggio" (newsletter + materiali omaggio) */
  var BREVO = "https://077c5c83.sibforms.com/serve/MUIFANq45jkBJOM0lQjtImPOak8nERttZViUr-Q0QuH1I_T6nMQEM8LgYo7VJt2GO87Ygu3lzlmDpsOsHxpqlHDzIilhtpo2qvgBssqJzCWTF_r7T-ELBm4dBW_yw41W0L0vFX_ybwApcS6l8LNlxdObGgtflDxpVfU1WNPXeCkDrb0DLfiZ7CJFKg2whKstnWEPUyqzsHqprY9-8g==";
  var art = document.querySelector("article.body");
  if (!art) return;
  var card = art.closest("section") || art;
  var parti = location.pathname.split("/").filter(Boolean);
  var slug = parti[parti.length - 1] === "index.html" ? parti[parti.length - 2] : parti[parti.length - 1];
  var h1 = document.querySelector("h1");
  var titolo = h1 ? h1.textContent.trim() : document.title;

  var css = document.createElement("style");
  css.textContent =
    ".cm h2{font-size:21px}" +
    ".cm-list{display:flex;flex-direction:column;gap:12px}" +
    ".cm-item{border:2.5px solid var(--ink);border-radius:14px;padding:10px 14px;background:#fff}" +
    ".cm-item.mary{background:var(--yellow)}" +
    ".cm-item b{display:block;font-weight:800}" +
    ".cm-item small{font-size:13px;font-weight:700;color:#444}" +
    ".cm-item p{margin-top:6px;line-height:1.5;white-space:pre-line}" +
    ".cm-empty{font-weight:600;color:#444}" +
    ".cm form{display:flex;flex-direction:column;gap:10px}" +
    ".cm label{font-weight:800}" +
    ".cm input[type=text],.cm input[type=email],.cm textarea{font:inherit;font-size:16px;border:2.5px solid var(--ink);border-radius:12px;padding:10px 12px;width:100%;background:#fff}" +
    ".cm textarea{min-height:130px;resize:vertical}" +
    ".cm .ok{display:flex;gap:10px;align-items:flex-start;font-weight:600;font-size:15px}" +
    ".cm .ok input{width:22px;height:22px;flex:0 0 auto;margin-top:1px}" +
    ".cm .nota{font-size:14px;color:#444}" +
    ".cm .esito{font-weight:800;border:2.5px solid var(--ink);border-radius:12px;padding:10px 12px}" +
    ".cm .esito.si{background:#DFF5E8}.cm .esito.no{background:#FFE3E3}" +
    ".cm .hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}" +
    ".cm button.btn{cursor:pointer;font-family:inherit;width:100%}" +
    ".cm button[disabled]{opacity:.6;cursor:wait}";
  document.head.appendChild(css);

  var box = document.createElement("section");
  box.className = "card cm";
  box.id = "commenti";
  box.innerHTML =
    '<h2>Commenti</h2>' +
    '<div class="cm-list" aria-live="polite"><p class="cm-empty">Ancora nessun commento: il primo può essere il tuo.</p></div>' +
    '<h3>Lascia un commento</h3>' +
    '<form novalidate>' +
    '<label for="cm-nome">Il tuo nome</label>' +
    '<input type="text" id="cm-nome" name="Nome" maxlength="60" autocomplete="given-name" required>' +
    '<label for="cm-testo">Il tuo commento</label>' +
    '<textarea id="cm-testo" name="Commento" maxlength="3000" required></textarea>' +
    '<label for="cm-mail">La tua mail per ricevere la newsletter <span style="font-weight:600">(facoltativa)</span></label>' +
    '<input type="email" id="cm-mail" name="Mail" maxlength="120" autocomplete="email" inputmode="email">' +
    '<p class="nota">Se la scrivi, ti arrivano la mia newsletter e i materiali omaggio. Puoi cancellarti quando vuoi. Sotto il commento la mail non compare mai.</p>' +
    '<div class="hp" aria-hidden="true"><label>Non compilare<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>' +
    '<label class="ok"><input type="checkbox" id="cm-ok" required><span>Ho letto la <a href="../../privacy/index.html#commenti">privacy</a> e sono d\'accordo che il mio nome e il mio commento vengano pubblicati sotto l\'articolo.</span></label>' +
    '<p class="nota">I commenti li leggo io prima di pubblicarli, quindi potrebbe volerci qualche giorno.</p>' +
    '<button type="submit" class="btn blue">INVIA IL COMMENTO</button>' +
    '<p class="esito" hidden></p>' +
    '</form>';
  var dopo = card.nextElementSibling;
  card.parentNode.insertBefore(box, dopo);

  var lista = box.querySelector(".cm-list");
  var form = box.querySelector("form");
  var esito = box.querySelector(".esito");
  var bottone = form.querySelector("button");

  function dataIt(s) {
    var d = new Date(s + "T12:00:00");
    if (isNaN(d)) return s;
    return d.toLocaleDateString("it-IT", { day: "numeric", month: "long", year: "numeric" });
  }
  function mostra(cs) {
    if (!cs || !cs.length) return;
    lista.innerHTML = "";
    cs.forEach(function (c) {
      var el = document.createElement("div");
      el.className = "cm-item" + (c.mary ? " mary" : "");
      var b = document.createElement("b");
      b.textContent = c.mary ? "Mary di Life School Family" : c.nome;
      var sm = document.createElement("small");
      sm.textContent = c.data ? dataIt(c.data) : "";
      var p = document.createElement("p");
      p.textContent = c.testo;
      el.appendChild(b); if (c.data) el.appendChild(sm); el.appendChild(p);
      lista.appendChild(el);
    });
  }
  /* legge un CSV (virgolette, virgole e a capo dentro il testo compresi) */
  function leggiCsv(t) {
    var righe = [], r = [], c = "", q = false, i, ch;
    t = String(t).replace(/^﻿/, "");
    for (i = 0; i < t.length; i++) {
      ch = t.charAt(i);
      if (q) {
        if (ch === '"') {
          if (t.charAt(i + 1) === '"') { c += '"'; i++; } else { q = false; }
        } else { c += ch; }
      } else if (ch === '"') { q = true; }
      else if (ch === ",") { r.push(c); c = ""; }
      else if (ch === "\n" || ch === "\r") {
        if (ch === "\r" && t.charAt(i + 1) === "\n") i++;
        r.push(c); c = ""; righe.push(r); r = [];
      } else { c += ch; }
    }
    if (c !== "" || r.length) { r.push(c); righe.push(r); }
    return righe;
  }
  function vero(s) { return /^(true|vero|si|sì|x|1|yes)$/i.test(String(s || "").trim()); }
  function dataIso(s) {
    s = String(s || "").trim();
    var m = s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})/);
    if (m) return m[3] + "-" + ("0" + m[2]).slice(-2) + "-" + ("0" + m[1]).slice(-2);
    return s.slice(0, 10);
  }
  /* righe del foglio per questo articolo, solo se "pubblicato" è spuntato */
  function daFoglio(testo) {
    var righe = leggiCsv(testo);
    if (!righe.length) return [];
    var h = righe[0].map(function (x) { return x.trim().toLowerCase(); });
    var ix = { a: h.indexOf("articolo"), n: h.indexOf("nome"), d: h.indexOf("data"), t: h.indexOf("testo"), m: h.indexOf("mary"), p: h.indexOf("pubblicato") };
    if (ix.a < 0 || ix.t < 0 || ix.p < 0) return [];
    var fuori = [];
    righe.slice(1).forEach(function (x) {
      var a = (x[ix.a] || "").trim(), t = (x[ix.t] || "").trim();
      if (!a || !t || !vero(x[ix.p])) return;
      if (a !== slug && a.indexOf("(" + slug + ")") < 0) return;
      fuori.push({
        nome: ix.n >= 0 ? (x[ix.n] || "").trim() : "",
        data: ix.d >= 0 ? dataIso(x[ix.d]) : "",
        testo: t,
        mary: ix.m >= 0 && vero(x[ix.m])
      });
    });
    return fuori;
  }
  var ritardo = Math.floor(Date.now() / 300000); /* il foglio si aggiorna ogni pochi minuti */
  Promise.all([
    fetch("../commenti.json?t=" + Date.now(), { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (j) { return (j && j[slug]) || []; })
      .catch(function () { return []; }),
    fetch(CSV + "&_=" + ritardo)
      .then(function (r) { return r.ok ? r.text() : ""; })
      .then(daFoglio)
      .catch(function () { return []; })
  ]).then(function (v) { mostra(v[0].concat(v[1])); });

  /* iscrizione a Brevo con un modulo nascosto (niente problemi di CORS) */
  function iscrivi(mail, nome) {
    try {
      var fr = document.createElement("iframe");
      fr.name = "cm-brevo"; fr.style.display = "none"; fr.setAttribute("aria-hidden", "true");
      document.body.appendChild(fr);
      var f = document.createElement("form");
      f.method = "POST"; f.action = BREVO; f.target = "cm-brevo"; f.style.display = "none";
      [["EMAIL", mail], ["NOME", nome], ["email_address_check", ""], ["locale", "it"], ["html_type", "simple"]].forEach(function (x) {
        var i = document.createElement("input"); i.type = "hidden"; i.name = x[0]; i.value = x[1]; f.appendChild(i);
      });
      document.body.appendChild(f);
      f.submit();
    } catch (e) {}
  }
  function avviso(testo, ok) {
    esito.textContent = testo;
    esito.className = "esito " + (ok ? "si" : "no");
    esito.hidden = false;
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var nome = form.Nome.value.trim();
    var testo = form.Commento.value.trim();
    var mail = form.Mail.value.trim();
    if (form._honey.value) return;
    if (mail && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) { avviso("La mail non sembra giusta: controllala, oppure lascia il campo vuoto.", false); return; }
    if (!nome || !testo) { avviso("Scrivi il tuo nome e il commento, poi invia.", false); return; }
    if (!document.getElementById("cm-ok").checked) { avviso("Per inviare spunta la casella della privacy.", false); return; }
    bottone.disabled = true;
    bottone.textContent = "Invio in corso, aspetta qualche secondo…";
    var corpo = new URLSearchParams();
    corpo.set(E.articolo, titolo + " (" + slug + ")");
    corpo.set(E.nome, nome);
    corpo.set(E.commento, testo);
    corpo.set(E.mail, mail);
    fetch(DEST, {
      method: "POST",
      mode: "no-cors",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: corpo.toString()
    })
      .then(function () {
        if (mail) iscrivi(mail, nome);
        form.reset();
        avviso("Grazie! Ho ricevuto il tuo commento. Lo leggo e lo pubblico qui appena posso.", true);
        bottone.textContent = "Commento inviato";
      })
      .catch(function () {
        avviso("Ops, il commento non è partito. Riprova tra poco oppure scrivimi a lifeschoolfamily.shop@gmail.com.", false);
        bottone.disabled = false;
        bottone.textContent = "INVIA IL COMMENTO";
      });
  });
})();

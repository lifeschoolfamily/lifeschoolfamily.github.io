/* Sfondi stagionali di Life School Family.
   Il sito sceglie DA SOLO il tema in base alla data, ogni anno.
   Tabella decisa con Mary il 17/11/2026:
   - Autunno: 22/9 – 14/10 e dal 2/11 fino all'inizio del Thanksgiving
   - Halloween: 15/10 – 1/11
   - Thanksgiving: dal giovedì prima del Ringraziamento al giorno del Ringraziamento (4° giovedì di novembre)
   - Natale: dal giorno dopo il Ringraziamento al 6/1
   - Inverno: 7/1 – 9/3 (tranne il Carnevale)
   - Carnevale: dalle 2 settimane prima del martedì grasso al martedì grasso
   - San Valentino: 7/2 – 14/2 (se cade nel Carnevale, vince San Valentino)
   - San Patrizio: 10/3 – 17/3
   - Primavera: 18/3 – 20/6 (tranne Pasqua)
   - Pasqua: dai 7 giorni prima di Pasqua al lunedì dell'Angelo
   - Estate: 21/6 – 31/8
   - Rientro a scuola: 1/9 – 21/9
   Prova di un tema in qualsiasi giorno: aggiungi ?tema=halloween (o un altro nome) all'indirizzo.
   Pagine escluse (hanno un tema loro): calendario-avvento, tre-strade. */
(function (glob) {
  function pasqua(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4,
      f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30,
      i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451),
      mo = Math.floor((h + l - 7 * m + 114) / 31), da = ((h + l - 7 * m + 114) % 31) + 1;
    return new Date(y, mo - 1, da, 12);
  }
  function gg(d, n) { var x = new Date(d); x.setDate(x.getDate() + n); return x; }
  function ringraziamento(y) { var p = new Date(y, 10, 1, 12); return new Date(y, 10, 1 + ((4 - p.getDay() + 7) % 7) + 21, 12); }
  function d(y, m, g) { return new Date(y, m - 1, g, 12); }

  function tema(oggi) {
    var o = new Date(oggi); o.setHours(12, 0, 0, 0);
    var y = o.getFullYear(), P = pasqua(y), grasso = gg(P, -47), TG = ringraziamento(y);
    function tra(a, b) { return o >= a && o <= b; }
    if (tra(gg(P, -7), gg(P, 1))) return 'pasqua';
    if (tra(d(y, 2, 7), d(y, 2, 14))) return 'sanvalentino';
    if (tra(gg(grasso, -14), grasso)) return 'carnevale';
    if (tra(d(y, 3, 10), d(y, 3, 17))) return 'sanpatrizio';
    if (tra(d(y, 1, 1), d(y, 1, 6)) || tra(gg(TG, 1), d(y, 12, 31))) return 'natale';
    if (tra(gg(TG, -7), TG)) return 'thanksgiving';
    if (tra(d(y, 10, 15), d(y, 11, 1))) return 'halloween';
    if (tra(d(y, 9, 22), d(y, 10, 14)) || tra(d(y, 11, 2), gg(TG, -8))) return 'autunno';
    if (tra(d(y, 9, 1), d(y, 9, 21))) return 'scuola';
    if (tra(d(y, 6, 21), d(y, 8, 31))) return 'estate';
    if (tra(d(y, 3, 18), d(y, 6, 20))) return 'primavera';
    return 'inverno';
  }

  var TEMI = {
    autunno:      { bg: '#FFF2E3', e: ['🍂', '🍁', '🌰', '🍄'] },
    halloween:    { bg: '#FFEEDD', e: ['🎃', '👻', '🦇', '🍬'] },
    thanksgiving: { bg: '#FCEFE0', e: ['🦃', '🌽', '🥧', '🍁'] },
    natale:       { bg: '#ECF7EF', e: ['🎄', '⭐', '❄️', '🎁'] },
    inverno:      { bg: '#EAF3FC', e: ['❄️', '⛄', '🧣', '❄️'] },
    carnevale:    { bg: '#FBEFFF', e: ['🎭', '🎉', '🎈', '🎊'] },
    sanvalentino: { bg: '#FFEEF3', e: ['💗', '💌', '❤️', '🍫'] },
    sanpatrizio:  { bg: '#E9F8ED', e: ['☘️', '🍀', '🌈', '🪙'] },
    primavera:    { bg: '#FFF0F6', e: ['🌸', '🌷', '🦋', '🌼'] },
    pasqua:       { bg: '#F4EFFF', e: ['🐣', '🥚', '🌷', '🐰'] },
    estate:       { bg: '#FFF8DA', e: ['☀️', '🌊', '🐚', '🍉'] },
    scuola:       { bg: '#F3F5FF', e: ['✏️', '📚', '🎒', '📐'] }
  };

  function sfondo(nome) {
    var t = TEMI[nome]; if (!t) return '';
    var pos = [[30, 40, -15], [140, 25, 20], [85, 120, 0], [200, 135, -25], [25, 200, 10], [150, 215, 15]];
    var s = '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240"><g opacity=".22" font-size="30" text-anchor="middle">';
    for (var i = 0; i < pos.length; i++) {
      s += '<text x="' + pos[i][0] + '" y="' + pos[i][1] + '" transform="rotate(' + pos[i][2] + ' ' + pos[i][0] + ' ' + pos[i][1] + ')">' + t.e[i % t.e.length] + '</text>';
    }
    s += '</g></svg>';
    return 'body{background-color:' + t.bg + ';background-image:url("data:image/svg+xml,' + encodeURIComponent(s) + '");background-repeat:repeat}';
  }

  var api = { tema: tema, pasqua: pasqua, ringraziamento: ringraziamento, temi: TEMI };

  if (typeof document !== 'undefined') {
    var nome = tema(new Date());
    var q = location.search.match(/[?&](?:tema|banner)=([a-z]+)/); if (q && TEMI[q[1]]) nome = q[1];
    api.oggi = nome;
    document.documentElement.setAttribute('data-tema', nome);
    var st = document.createElement('style'); st.id = 'sfondo-stagionale'; st.textContent = sfondo(nome);
    document.head.appendChild(st);
    /* Banner della famiglia in Home */
    api.banner = function (id, cartella) { var img = document.getElementById(id); if (img) img.src = cartella + nome + '.webp'; };
  }
  glob.LSF = api;
  if (typeof module !== 'undefined') module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);

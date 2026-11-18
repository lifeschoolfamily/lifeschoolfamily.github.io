// Altoparlanti: ogni riquadro si può ascoltare letto con la voce di Mary.
// Uso: <script src="js/voce.js" data-pagina="home" data-base="audio/voce/" defer></script>
(function(){
  var me=document.currentScript;
  var pagina=me.getAttribute('data-pagina'), base=me.getAttribute('data-base')||'audio/voce/';
  var main=document.querySelector('main'); if(!main) return;
  var mappa=[]; // [elemento, codice audio, dove mettere il pulsante]
  if(pagina==='home'){
    var cards=main.querySelectorAll(':scope > section:not(#avvento)');
    for(var i=0;i<5&&i<cards.length;i++) mappa.push([cards[i],'home-'+(i+1),'card']);
    var av=document.getElementById('avvento'); if(av) mappa.push([av,'home-avvento','card']);
  } else if(pagina==='avvento'){
    var asecs=main.querySelectorAll(':scope > section');
    for(var a=0;a<4&&a<asecs.length;a++) mappa.push([asecs[a],'avvento-'+(a+1),'card']);
  } else if(pagina==='blog'){
    var prima=main.querySelector(':scope > section');
    if(prima) mappa.push([prima,me.getAttribute('data-audio'),'card']);
  } else if(pagina==='chi'){
    var secs=main.querySelectorAll(':scope > section');
    if(secs.length) mappa.push([secs[0],'chi-0','card']);
    var det=main.querySelectorAll('details');
    for(var j=0;j<det.length;j++) mappa.push([det[j],'chi-'+(j+1),'summary']);
    if(secs.length>1) mappa.push([secs[secs.length-1],'chi-9','card']);
  }
  if(!mappa.length) return;

  var st=document.createElement('style');
  st.textContent='.voce-riga{display:flex;justify-content:flex-end;margin:-4px -4px 0 0}'+
  '.voce-btn{display:inline-flex;align-items:center;gap:6px;min-height:40px;padding:4px 12px;border:2.5px solid var(--ink,#1d1d1b);border-radius:999px;background:var(--yellow,#FFD23F);color:var(--ink,#1d1d1b);font:inherit;font-weight:800;font-size:14px;line-height:1;box-shadow:2px 2px 0 var(--ink,#1d1d1b);cursor:pointer;flex:0 0 auto}'+
  '.voce-btn svg{width:18px;height:18px}.voce-btn[aria-pressed="true"]{background:#fff}'+
  '.voce-btn:focus-visible{outline:3px solid var(--blue,#1E5AA8);outline-offset:3px}'+
  '.voce-fissa{position:sticky;top:var(--voce-top,64px);z-index:4;margin:0 0 -42px;padding-top:6px;height:46px;pointer-events:none}.voce-fissa .voce-btn{pointer-events:auto;box-shadow:3px 3px 0 var(--ink,#1d1d1b)}'+
  'summary .voce-btn{margin-left:auto;font-size:14px}'+
  '@media (prefers-reduced-motion:no-preference){.voce-btn[aria-pressed="true"] svg{animation:voce-p 1.2s ease-in-out infinite}}'+
  '@keyframes voce-p{50%{transform:scale(1.15)}}';
  document.head.appendChild(st);

  if(pagina==='blog'){ var hd=document.querySelector('header'); var alt=function(){ document.documentElement.style.setProperty('--voce-top',((hd?hd.offsetHeight:56)+6)+'px'); }; alt(); window.addEventListener('resize',alt); }
  var ICO='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg>';
  var PAUSA='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
  var audio=new Audio(); audio.preload='none';
  var attivo=null;

  function aspetto(b,suona){
    b.setAttribute('aria-pressed',suona?'true':'false');
    b.innerHTML=(suona?PAUSA:ICO)+'<span>'+(suona?'Pausa':(pagina==='blog'?'Ascolta l\'articolo':'Ascolta'))+'</span>';
    b.setAttribute('aria-label',suona?'Metti in pausa la lettura':(pagina==='blog'?'Ascolta l\'articolo letto da Mary':'Ascolta questo riquadro letto da Mary'));
  }
  function ferma(){ if(attivo){aspetto(attivo,false);} }
  audio.addEventListener('ended',function(){ferma();attivo=null;});
  audio.addEventListener('pause',function(){ferma();});
  audio.addEventListener('play',function(){ if(attivo) aspetto(attivo,true); });

  mappa.forEach(function(m){
    var el=m[0], cod=m[1], b=document.createElement('button');
    b.type='button'; b.className='voce-btn'; b.setAttribute('data-voce',cod); aspetto(b,false);
    b.addEventListener('click',function(e){
      e.preventDefault(); e.stopPropagation();
      var sigla=document.getElementById('sigla'); if(sigla&&!sigla.paused) sigla.pause();
      if(attivo===b && !audio.paused){ audio.pause(); return; }
      if(attivo!==b){ ferma(); attivo=b; audio.src=base+cod+'.mp3?v=4'; }
      audio.play().catch(function(){ ferma(); });
    });
    if(m[2]==='summary'){ var s=el.querySelector('summary'); if(s) s.appendChild(b); }
    else if(pagina==='blog'){ var f=document.createElement('div'); f.className='voce-riga voce-fissa'; f.appendChild(b); main.insertBefore(f,el); }
    else { var r=document.createElement('div'); r.className='voce-riga'; r.appendChild(b); el.insertBefore(r,el.firstChild); }
  });
})();

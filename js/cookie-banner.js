(function () {
  var KEY = 'lsf_cookie_pinterest';
  var PIN_ID = '2614215185273';
  var privacyHref = location.pathname.indexOf('/blog/') > -1 ? '../privacy/' : 'privacy/';

  function getChoice() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setChoice(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
  }

  function loadPinterest() {
    if (window.pintrk) return;
    window.pintrk = function () {
      window.pintrk.queue.push(Array.prototype.slice.call(arguments));
    };
    window.pintrk.queue = [];
    window.pintrk.version = '3.0';
    var t = document.createElement('script');
    t.async = true;
    t.src = 'https://s.pinimg.com/ct/core.js';
    document.head.appendChild(t);
    window.pintrk('load', PIN_ID);
    window.pintrk('page');
  }

  function btn(label, primary) {
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = label;
    b.style.cssText = 'font:inherit;padding:4px 10px;border:1px solid #666;border-radius:4px;background:#fff;color:#222;cursor:pointer;white-space:nowrap';
    return b;
  }

  function showBanner() {
    var bar = document.createElement('div');
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookie');
    bar.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#fff;border-top:1px solid #ddd;box-shadow:0 -1px 4px rgba(0,0,0,.08);padding:6px 12px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;justify-content:center;font:12px/1.4 system-ui,sans-serif;color:#333';

    var text = document.createElement('span');
    text.innerHTML = 'Usiamo i cookie di Pinterest per misurare le visite. <a href="' + privacyHref + '" style="color:#333">Privacy</a>';

    var accept = btn('Accetta');
    var refuse = btn('Rifiuta');

    accept.onclick = function () { setChoice('yes'); bar.remove(); loadPinterest(); };
    refuse.onclick = function () { setChoice('no'); bar.remove(); };

    bar.appendChild(text);
    bar.appendChild(accept);
    bar.appendChild(refuse);
    document.body.appendChild(bar);
  }

  var choice = getChoice();
  if (choice === 'yes') loadPinterest();
  else if (choice !== 'no') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', showBanner);
    else showBanner();
  }
})();

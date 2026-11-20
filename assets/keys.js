(function () {
  var sheet = null;
  function build() {
    var d = document.createElement('div');
    d.className = 'keys-sheet';
    d.innerHTML = '<div class="keys-inner"><h3>Keyboard</h3><dl>' +
      '<dt>j</dt><dd>next dossier</dd><dt>k</dt><dd>previous dossier</dd>' +
      '<dt>/</dt><dd>focus search</dd><dt>t</dt><dd>switch theme</dd>' +
      '<dt>?</dt><dd>this sheet</dd><dt>Esc</dt><dd>close</dd></dl></div>';
    d.addEventListener('click', function (e) { if (e.target === d) close(); });
    document.body.appendChild(d);
    return d;
  }
  function close() { if (sheet) { sheet.remove(); sheet = null; } }
  document.addEventListener('keydown', function (e) {
    if (e.target.matches('input,textarea,select')) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var pager = document.querySelector('.pager');
    if (e.key === 'j' && pager) { var n = pager.querySelectorAll('a')[1]; if (n) location.href = n.href; }
    else if (e.key === 'k' && pager) { var p = pager.querySelectorAll('a')[0]; if (p) location.href = p.href; }
    else if (e.key === '/') { var s = document.querySelector('input[type=search]'); if (s) { e.preventDefault(); s.focus(); } }
    else if (e.key === 't') { var b = document.querySelector('[data-pref=theme]'); if (b) b.click(); }
    else if (e.key === '?') { sheet ? close() : (sheet = build()); }
    else if (e.key === 'Escape') { close(); }
  });
  var links = [].slice.call(document.querySelectorAll('.toc a'));
  if (links.length && 'IntersectionObserver' in window) {
    var heads = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); }).filter(Boolean);
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + en.target.id); });
      });
    }, { rootMargin: '-96px 0px -70% 0px' });
    heads.forEach(function (hd) { io.observe(hd); });
  }
})();

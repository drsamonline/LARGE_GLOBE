/* Ctrl-K / ⌘K command palette over the same index the search page uses.
   The index is fetched on first open (233 KB) rather than inlined on 187 pages. */
(function () {
  var box = null, input = null, list = null, data = null, hits = [], sel = 0, loading = false;

  function open() {
    if (!box) build();
    box.hidden = false;
    input.value = '';
    input.focus();
    render('');
    if (!data && !loading) load();
  }
  function close() { if (box) box.hidden = true; }

  function load() {
    loading = true;
    fetch('search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (j) { data = j; if (input.value) render(input.value); })
      .catch(function () {
        loading = false;
        list.innerHTML = '<li class="pal-note">The index could not be loaded here (a local file, or no connection). ' +
          '<a href="search.html">Open the search page →</a></li>';
      })
      .then(function () { loading = false; });
  }

  function build() {
    box = document.createElement('div');
    box.className = 'pal';
    box.hidden = true;
    box.innerHTML =
      '<div class="pal-inner" role="dialog" aria-modal="true" aria-label="Search the archive">' +
      '<input type="search" id="pal-q" placeholder="Search 162 dossiers and 830 collection rows…" autocomplete="off" spellcheck="false">' +
      '<ul id="pal-list" role="listbox"></ul>' +
      '<p class="pal-foot"><kbd>↑</kbd><kbd>↓</kbd> move · <kbd>↵</kbd> open · <kbd>esc</kbd> close</p>' +
      '</div>';
    box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.body.appendChild(box);
    input = box.querySelector('#pal-q');
    list = box.querySelector('#pal-list');
    input.addEventListener('input', function () { render(input.value); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
      else if (e.key === 'Enter') { e.preventDefault(); var a = list.querySelectorAll('a')[sel]; if (a) location.href = a.href; }
      else if (e.key === 'Escape') { close(); }
    });
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function move(d) {
    var links = list.querySelectorAll('a');
    if (!links.length) return;
    sel = (sel + d + links.length) % links.length;
    [].forEach.call(links, function (a, i) { a.classList.toggle('on', i === sel); });
    links[sel].scrollIntoView({ block: 'nearest' });
  }

  function render(term) {
    term = (term || '').trim().toLowerCase();
    sel = 0;
    if (!data) { list.innerHTML = '<li class="pal-note">Loading the index…</li>'; return; }
    var pool = [];
    data.d.forEach(function (d) { pool.push({ k: 'Dossier', t: d.t, u: d.u, s: d.s, l: d.l, c: d.c, hay: (d.t + ' ' + d.s + ' ' + d.l + ' ' + d.g).toLowerCase() }); });
    data.e.forEach(function (e) { pool.push({ k: 'Entry', t: e.t, u: e.u, s: e.s, l: e.l, c: e.b, hay: (e.t + ' ' + e.s + ' ' + e.l + ' ' + e.g + ' ' + (e.c || '')).toLowerCase() }); });
    hits = term ? pool.filter(function (p) { return p.hay.indexOf(term) > -1; }) : pool.filter(function (p) { return p.k === 'Dossier'; });
    list.innerHTML = hits.slice(0, 12).map(function (h, i) {
      return '<li><a href="' + esc(h.u) + '"' + (i === 0 ? ' class="on"' : '') + '>' +
        '<span class="pal-k">' + h.k + '</span><span class="pal-t">' + esc(h.t) + '</span>' +
        '<span class="badge ' + esc(h.c || 'b-doc') + '">' + esc(h.l) + '</span></a></li>';
    }).join('') || '<li class="pal-note">Nothing matches. Try a theme, a label or a year.</li>';
    if (hits.length > 12) list.innerHTML += '<li class="pal-note">' + (hits.length - 12) + ' more — open the search page</li>';
  }

  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); box && !box.hidden ? close() : open(); }
    else if (e.key === 'Escape' && box && !box.hidden) close();
  });
})();

(function () {
  var root = document.documentElement;
  var SIZE = ['sm', 'md', 'lg'];
  function set(k, v) { try { localStorage.setItem('lwa-' + k, v); } catch (e) {} }
  function apply() {
    document.querySelectorAll('[data-pref]').forEach(function (b) {
      var k = b.getAttribute('data-pref');
      if (k === 'theme') b.setAttribute('aria-pressed', root.dataset.theme === 'light' ? 'true' : 'false');
      if (k === 'size') b.setAttribute('aria-pressed', (root.dataset.size || 'md') !== 'md' ? 'true' : 'false');
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-pref]');
    if (!b) return;
    var k = b.getAttribute('data-pref');
    if (k === 'theme') { var t = root.dataset.theme === 'light' ? 'dark' : 'light'; root.dataset.theme = t; set('theme', t); }
    if (k === 'size') {
      var i = SIZE.indexOf(root.dataset.size || 'md'); var n = SIZE[(i + 1) % SIZE.length];
      root.dataset.size = n; set('size', n);
    }
    apply();
  });
  apply();
})();

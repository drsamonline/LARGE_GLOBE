(function(){
  document.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-copy]');
    if (!b) return;
    var text = b.getAttribute('data-copy');
    var done = function () { var o = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = o; }, 1400); };
    if (navigator.clipboard) { navigator.clipboard.writeText(text).then(done, function(){}); }
  });
})();

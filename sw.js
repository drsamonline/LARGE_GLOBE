/* The Larger World Archive — offline reading.
   Pages are network-first with a cache fallback, so a read page stays readable on
   a train and a returning reader gets the current text. Assets are
   stale-while-revalidate: the cached copy answers immediately and the network
   copy replaces it, so a stylesheet change reaches a reader on their next visit
   instead of never. */
const V = 'lwa-v3';
const SHELL = [
  './', 'index.html', 'assets/style.css', 'assets/prefs.js', 'assets/keys.js',
  'assets/cite.js', 'favicon.svg', 'assets/icon-192.png', 'offline.html'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(V).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== V).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;

  const isPage = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');

  if (isPage) {
    e.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(V).then((c) => c.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req).then((hit) => hit || caches.match('offline.html')))
    );
    return;
  }

  // stale-while-revalidate for everything else
  e.respondWith(
    caches.match(req).then((hit) => {
      const net = fetch(req)
        .then((res) => {
          if (res.ok && res.type === 'basic') {
            const copy = res.clone();
            caches.open(V).then((c) => c.put(req, copy));
          }
          return res;
        })
        .catch(() => hit);
      return hit || net;
    })
  );
});

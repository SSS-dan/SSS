var staticCacheName = 'djangopwa-v1'+ new Date().getTime();

self.addEventListener('install', function(event) {
event.waitUntil(
	caches.open(staticCacheName).then(function(cache) {
	return cache.addAll([
		'/offline/',  // add the actual path to your offline page
		'/static/css/app.css',  // add paths to any static files you want to cache
		'/static/js/app.js',
	]);
	})
);
});

self.addEventListener('fetch', function(event) {
var requestUrl = new URL(event.request.url);
	if (requestUrl.origin === location.origin) {
	if ((requestUrl.pathname === '/')) {
		event.respondWith(caches.match(''));
		return;
	}
	}
	event.respondWith(
	caches.match(event.request).then(function(response) {
		return response || fetch(event.request);
	})
	);
});

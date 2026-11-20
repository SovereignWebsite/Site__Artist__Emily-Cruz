// Click to load: nothing is fetched from Spotlight until the visitor presses play.
// Without JavaScript the link opens the reel on Spotlight instead.
document.querySelectorAll('.frame[data-src]').forEach(function (frame) {
  var link = frame.querySelector('.play');
  link.addEventListener('click', function (e) {
    e.preventDefault();
    var f = document.createElement('iframe');
    f.src = frame.getAttribute('data-src');
    f.title = frame.parentElement.querySelector('h3').textContent;
    f.allow = 'autoplay; fullscreen; picture-in-picture';
    f.allowFullscreen = true;
    f.referrerPolicy = 'strict-origin-when-cross-origin';
    frame.replaceChildren(f);
  });
});

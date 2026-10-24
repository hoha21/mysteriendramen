/* Rubriken-Filter für die Blogübersicht.
   Liest die Rubriken aus den Einträgen (<span class="tag">) und baut daraus Schaltflächen.
   Neue Rubriken erscheinen automatisch. Ohne JavaScript bleibt die vollständige Liste sichtbar.
   Direktlink auf eine Rubrik: /blog/#rubrik=Kontexte */
(function () {
  var list = document.querySelector('.post-list');
  var bar = document.getElementById('rubriken');
  if (!list || !bar) return;
  var items = Array.prototype.slice.call(list.querySelectorAll('li'));
  var counts = {};
  items.forEach(function (li) {
    var t = li.querySelector('.tag');
    var name = t ? t.textContent.trim() : '';
    li.dataset.rubrik = name;
    if (name) counts[name] = (counts[name] || 0) + 1;
  });
  var names = Object.keys(counts).sort(function (a, b) { return a.localeCompare(b, 'de'); });
  if (names.length < 2) return;
  var buttons = [];
  function make(label, value, n) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'rubrik-chip';
    b.textContent = label + ' (' + n + ')';
    b.dataset.value = value;
    b.addEventListener('click', function () { select(value, true); });
    bar.appendChild(b);
    buttons.push(b);
  }
  function select(value, push) {
    items.forEach(function (li) { li.hidden = !!value && li.dataset.rubrik !== value; });
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.value === value)); });
    if (push) {
      var hash = value ? '#rubrik=' + encodeURIComponent(value) : ' ';
      try { history.replaceState(null, '', hash === ' ' ? location.pathname : hash); } catch (e) {}
    }
  }
  var label = document.createElement('span');
  label.className = 'rubriken-label';
  label.textContent = 'Rubriken:';
  bar.appendChild(label);
  make('Alle', '', items.length);
  names.forEach(function (n) { make(n, n, counts[n]); });
  bar.hidden = false;
  var m = /rubrik=([^&]+)/.exec(location.hash);
  var start = m ? decodeURIComponent(m[1]) : '';
  select(counts[start] ? start : '', false);
})();

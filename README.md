# Mysteriendramen
Blog über Rudolf Steiners Mysteriendramen (mysteriendramen.ch, Alexander Höhne).

## Neuer Beitrag: Checkliste
- Beitrag als `blog/JJJJ-MM-TT-kurztitel.html` (Kopfbereich wie bei den bestehenden
  Beiträgen: Beschreibung höchstens 160 Zeichen, Titel höchstens etwa 65 Zeichen,
  Open-Graph-Angaben, Block `application/ld+json`), unter dem Titel die Autorenzeile
  `<p class="meta byline">von <a href="/ueber-mich.html">Alexander Höhne</a></p>`.
- Eintrag zuoberst in `blog/index.html` (mit Rubrik in `<span class="tag">`; der
  Rubriken-Filter übernimmt neue Rubriken automatisch).
- Eintrag zuoberst unter «Neueste Beiträge» in `index.html`, höchstens fünf.
- `sitemap.xml` und `feed.xml` neu erzeugen: `python tools/sitemap_feed.py`
  (liest Titel, Datum, Rubrik und Anriss aus dem JSON-LD-Block; Seiten mit
  `noindex` und alles in `entwuerfe/` bleiben aussen vor).
- Fertige, noch nicht fällige Beiträge liegen in `entwuerfe/` (nicht öffentlich)
  und werden erst am Erscheinungstag nach `blog/` verschoben.
- Englischer Bereich (`en/`): in `tools/en_build.py` (Liste ARTICLES) englischen Titel und
  Zusammenfassung ergänzen, dann `python tools/en_build.py en` ausführen.
- Veröffentlichen: GitHub Desktop, «Commit to main», «Push origin».

## Rubriken (fester Satz)
Jeder Beitrag erhält genau eine Rubrik (`<span class="tag">`, im JSON-LD als
`articleSection`, im Feed als `<category>`):
- **Allgemeines** – über die Seite, Überblicke, Einstiege
- **Aspekte** – Motive, Bilder und Themen der Dramen (z. B. Spiegelmetaphorik)
- **Figuren** – Porträts einzelner Gestalten
- **Dramaturgie** – Bühne, Sprache, Inszenierung, eigene dramaturgische Arbeit
- **Kontexte** – die Dramen in Literatur-, Theater- und Geistesgeschichte

## Redaktionsplan
Themen und Termine: [REDAKTIONSPLAN.md](REDAKTIONSPLAN.md). Beiträge erscheinen
in der Regel sonntags alle zwei Wochen, im Wechsel mit karmaforschung.ch;
zusätzliche Beiträge sind jederzeit möglich.

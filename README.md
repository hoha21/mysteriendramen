# Mysteriendramen
Blog über Rudolf Steiners Mysteriendramen (mysteriendramen.ch, Alexander Höhne).

## Neuer Beitrag: Checkliste
- Beitrag als `blog/JJJJ-MM-TT-kurztitel.html` aus der Vorlage `tools/vorlage-beitrag.html`
  (Kopfbereich mit Open-Graph-Angaben, Block `application/ld+json` und GoatCounter;
  Beschreibung höchstens 160 Zeichen, Titel höchstens etwa 65 Zeichen). Alle Platzhalter
  `{{…}}` ersetzen: `{{TITEL}}`, `{{ANRISS}}`, `{{DATEINAME}}`, `{{DATUM_ISO}}` (JJJJ-MM-TT),
  `{{DATUM_LANG}}` (z. B. „15. November 2026“), `{{RUBRIK}}`, Text und Weiterlesen-Links.
  Das Motto ist optional. Jeder Beitrag endet mit einer Quellenliste (`<ul class="sources">`:
  Autor, Titel, Ausgabe, Seite oder Vers); nicht Belegtes steht als Deutung oder
  Arbeitshypothese im Text oder in `<p class="note">`.
  Im Block `application/ld+json` keine geraden Anführungszeichen " im Text, sondern „…“.
- Eintrag zuoberst in `blog/index.html` (mit Rubrik in `<span class="tag">`; der
  Rubriken-Filter übernimmt neue Rubriken automatisch).
- Eintrag zuoberst unter «Neueste Beiträge» in `index.html`, höchstens fünf.
- Quellenverzeichnis `literatur.html` neu erzeugen: `python tools/literatur.py`
  (sammelt die Einträge aller `<ul class="sources">` der Beiträge).
- `sitemap.xml` und `feed.xml` neu erzeugen: `python tools/sitemap_feed.py`
  (liest Titel, Datum, Rubrik und Anriss aus dem JSON-LD-Block; Seiten mit
  `noindex` und alles in `entwuerfe/` bleiben aussen vor).
- Fertige, noch nicht fällige Beiträge liegen in `entwuerfe/` (nicht öffentlich)
  und werden erst am Erscheinungstag nach `blog/` verschoben.
- Englischer Bereich (`en/`): in `tools/en_build.py` (Liste ARTICLES) englischen Titel und
  Zusammenfassung ergänzen, dann `python tools/en_build.py en` ausführen.
- Veröffentlichen: GitHub Desktop, «Commit to main», «Push origin».

## Überarbeitungen
Veröffentlichte Beiträge werden weiter gepflegt (Impressum, Abschnitt «Pflege der Texte»).
Bei inhaltlichen Änderungen am Ende des Beitrags vermerken
(`<p class="meta"><em>Überarbeitet am …:</em> was geändert wurde.</p>`), im JSON-LD
`"dateModified"` und im Kopf `article:modified_time` setzen, dann `tools/literatur.py`
und `tools/sitemap_feed.py` ausführen. Tippfehler und Glättungen ohne Vermerk.

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

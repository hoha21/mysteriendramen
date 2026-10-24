# Mysteriendramen
Blog über Rudolf Steiners Mysteriendramen (mysteriendramen.ch, Alexander Höhne).

## Neuer Beitrag: Checkliste
- Beitrag als `blog/JJJJ-MM-TT-kurztitel.html` (Kopfbereich wie bei den bestehenden
  Beiträgen: Beschreibung höchstens 160 Zeichen, Titel höchstens etwa 65 Zeichen,
  Open-Graph-Angaben, Block `application/ld+json`).
- Eintrag zuoberst in `blog/index.html` (mit Rubrik in `<span class="tag">`; der
  Rubriken-Filter übernimmt neue Rubriken automatisch).
- Eintrag zuoberst unter «Neueste Beiträge» in `index.html`, höchstens fünf.
- `<item>` zuoberst in `feed.xml` und `<url>` in `sitemap.xml`.
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
sonntags alle zwei Wochen, im Wechsel mit karmaforschung.ch.

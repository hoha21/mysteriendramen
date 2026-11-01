"""Erzeugt literatur.html: das Quellenverzeichnis aller Beiträge.

Aufruf im Hauptordner der Webseite:   python tools/literatur.py

Grundsätze
- Gelesen werden alle Beiträge in blog/ (ohne blog/index.html und ohne Seiten mit
  noindex, also ohne Weiterleitungen). Entwürfe ausserhalb von blog/ bleiben aussen vor.
- Aus jedem Beitrag werden die Einträge der Quellenliste <ul class="sources"> übernommen.
- Gleichlautende Einträge werden zusammengefasst; zu jedem Eintrag steht, in welchen
  Beiträgen er vorkommt.
- Einträge zum selben Werk (gleiche Autorin oder gleicher Autor und gleicher Titel)
  werden unter dem Werk zusammengefasst, jeweils mit Ausgabe und Stelle.
- Sortiert wird nach dem Nachnamen der Autorin oder des Autors (Text vor dem ersten
  Doppelpunkt). Einträge ohne Autor, etwa „Zu …“, „Art. …“ oder Lexikonartikel,
  stehen am Ende unter „Weitere Nachweise“.
- Kopf, Navigation und Fusszeile werden aus ueber-mich.html übernommen, damit die
  Seite immer zum aktuellen Seitengerüst passt (einschliesslich Statistik-Code).
- Die Seite wird nach jedem neuen oder geänderten Beitrag neu erzeugt, danach
  tools/sitemap_feed.py ausführen.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = (ROOT / "CNAME").read_text(encoding="utf-8").strip()
BASE = f"https://{DOMAIN}"
SITE = "Karmaforschung" if "karma" in DOMAIN else "Mysteriendramen"
TITEL = "Literatur und Quellen"
BESCHREIBUNG = (f"Verzeichnis aller Quellen, auf die sich die Beiträge auf {DOMAIN} stützen, "
                "mit Verweisen auf die Beiträge.")


def lies(pfad):
    return pfad.read_text(encoding="utf-8")


def beitraege():
    for pfad in sorted((ROOT / "blog").glob("*.html"), reverse=True):
        if pfad.name == "index.html":
            continue
        text = lies(pfad)
        if re.search(r'<meta\s+name="robots"\s+content="[^"]*noindex', text, re.I):
            continue
        titel = pfad.stem
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try:
                daten = json.loads(block)
            except json.JSONDecodeError:
                continue
            if daten.get("@type") == "BlogPosting":
                titel = daten.get("headline", titel)
        liste = re.search(r'<ul class="sources">(.*?)</ul>', text, re.S)
        eintraege = re.findall(r"<li>(.*?)</li>", liste.group(1), re.S) if liste else []
        yield pfad.name, titel, [" ".join(e.split()) for e in eintraege]


def rein(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def zerlege(eintrag):
    """Teilt einen Eintrag in Autor, Werktitel und Rest (Ausgabe, Stelle, Links)."""
    m = re.match(r"(?P<autor>[^:<„]+?):\s*(?P<titel><em>.*?</em>|„[^“]*“)(?P<rest>.*)", eintrag)
    if not m:
        return None, None, eintrag
    return m["autor"].strip(), m["titel"], m["rest"].lstrip(" ,.")


def nachname(autor):
    erster = re.split(r" / |,| und | u\. a\.", autor)[0].strip()
    teile = erster.split()
    return teile[-1].lower() if teile else erster.lower()


def ist_weiterer(eintrag):
    return re.match(r"(Zu|Zum|Zur|Art\.|Artikel)\s|„", rein(eintrag)) is not None


def main():
    verzeichnis = {}
    for datei, titel, eintraege in beitraege():
        for e in eintraege:
            verzeichnis.setdefault(e, [])
            if (datei, titel) not in verzeichnis[e]:
                verzeichnis[e].append((datei, titel))

    def belege(e):
        return ", ".join(f'<a href="/blog/{d}">{html.escape(t, quote=False)}</a>' for d, t in verzeichnis[e])

    # Gruppen nach Autor und Werktitel; Einträge ohne erkennbaren Werktitel stehen einzeln.
    gruppen, weitere = {}, []
    for e in verzeichnis:
        if ist_weiterer(e):
            weitere.append(e)
            continue
        autor, werk, _ = zerlege(e)
        if autor:
            schluessel = (autor, rein(werk))
        else:
            # ohne erkennbaren Werktitel: einzeln, aber nach dem Autor vor dem Doppelpunkt sortiert
            kopf = rein(e).split(":", 1)
            schluessel = (kopf[0].strip(), rein(e)) if len(kopf) == 2 else (rein(e), rein(e))
        gruppen.setdefault(schluessel, []).append(e)

    def sortierung(schluessel):
        autor, werk = schluessel
        return (nachname(autor), autor.lower(), werk.lower())

    zeilen = []
    for schluessel in sorted(gruppen, key=sortierung):
        eintraege = sorted(gruppen[schluessel], key=lambda e: rein(e).lower())
        if len(eintraege) == 1:
            e = eintraege[0]
            zeilen.append(f'      <li>{e}<br><span class="meta">Zitiert in: {belege(e)}</span></li>')
            continue
        autor, werk, _ = zerlege(eintraege[0])
        unter = "\n".join(
            f'          <li>{zerlege(e)[2] or "Werk allgemein"}<br><span class="meta">Zitiert in: {belege(e)}</span></li>'
            for e in eintraege)
        zeilen.append(f"      <li>{autor}: {werk}\n        <ul>\n{unter}\n        </ul>\n      </li>")

    if zeilen or weitere:
        inhalt = '    <ul class="sources">\n' + "\n".join(zeilen) + "\n    </ul>\n"
        if weitere:
            inhalt += ('\n    <h2>Weitere Nachweise</h2>\n    <ul class="sources">\n'
                       + "\n".join(f'      <li>{e}<br><span class="meta">Zitiert in: {belege(e)}</span></li>'
                                   for e in sorted(weitere, key=lambda e: rein(e).lower()))
                       + "\n    </ul>\n")
    else:
        inhalt = "    <p>Die Quellenlisten der Beiträge werden zurzeit ergänzt.</p>\n"

    vorlage = lies(ROOT / "ueber-mich.html")
    kopf, rest = vorlage.split('<main id="inhalt">', 1)
    fuss = rest.split("</main>", 1)[1]
    url = f"{BASE}/literatur.html"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": TITEL,
          "description": BESCHREIBUNG, "url": url, "inLanguage": "de-CH",
          "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE}/"}}
    kopf = re.sub(r"<title>.*?</title>", f"<title>{TITEL} — {SITE}</title>", kopf)
    kopf = re.sub(r'<meta name="description" content="[^"]*">',
                  f'<meta name="description" content="{BESCHREIBUNG}">', kopf)
    kopf = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', kopf)
    kopf = re.sub(r'<meta property="og:title" content="[^"]*">',
                  f'<meta property="og:title" content="{TITEL}">', kopf)
    kopf = re.sub(r'<meta property="og:description" content="[^"]*">',
                  f'<meta property="og:description" content="{BESCHREIBUNG}">', kopf)
    kopf = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', kopf)
    kopf = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', "", kopf)
    kopf = re.sub(r'<script type="application/ld\+json">.*?</script>',
                  lambda m: '<script type="application/ld+json">\n'
                  + json.dumps(ld, ensure_ascii=False, indent=2) + "\n</script>", kopf, flags=re.S)
    kopf = kopf.replace(' aria-current="page"', "")

    seite = (kopf + '<main id="inhalt">\n  <div class="wrap">\n\n'
             f"    <h1>{TITEL}</h1>\n"
             '    <p class="meta">Dieses Verzeichnis sammelt die Quellen, auf die sich die Beiträge stützen. '
             "Zu jedem Eintrag steht, in welchen Beiträgen er herangezogen wird. "
             "Die Angaben sind vor der Veröffentlichung an einer zugänglichen Ausgabe geprüft.</p>\n\n"
             + inhalt + "\n  </div>\n</main>" + fuss)
    (ROOT / "literatur.html").write_text(seite, encoding="utf-8")
    print(f"literatur.html: {len(verzeichnis)} Einträge")


if __name__ == "__main__":
    main()

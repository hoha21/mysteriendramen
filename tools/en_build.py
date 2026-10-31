"""Erzeugt den englischen Bereich von mysteriendramen.ch (Ordner en/).
Aufruf im Hauptordner:  python tools/en_build.py en
Bei jedem neuen Beitrag in der Liste ARTICLES oben einen Eintrag mit
englischem Titel und Zusammenfassung ergänzen und das Skript erneut ausführen.
--draft erzeugt Entwürfe (noindex, Entwurfsvermerk)."""
import json
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
DRAFT = "--draft" in sys.argv
BASE = "https://mysteriendramen.ch"
KF = "https://karmaforschung.ch/blog/2026-10-25-karma-auf-der-buehne.html"

NAV = [("/en/", "Home"), ("/en/articles.html", "Articles"), ("/en/characters.html", "Characters"),
       ("/en/legal-notice.html", "Legal notice")]

# English page -> German counterpart (for hreflang and the language switch)
PAIRS = {
    "index.html": "/",
    "four-mystery-dramas.html": "/blog/2026-09-06-vier-dramen-ueberblick.html",
    "characters.html": "/gestalten.html",
    "legal-notice.html": "/impressum.html",
    "articles.html": "/blog/",
}


def de(path, text):
    """Link to a German page, marked as such."""
    return f'<a href="{path}" hreflang="de">{text}</a> <span class="meta">(in German)</span>'


def page(name, title, desc, h1, body, nav_active, ld_type="WebPage"):
    url = f"{BASE}/en/" + ("" if name == "index.html" else name)
    de_url = BASE + PAIRS[name]
    nav = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == nav_active else ""}>{t}</a>' for h, t in NAV)
    nav += f'\n      <a href="{PAIRS[name]}" hreflang="de" lang="de">Deutsch</a>'
    robots = '<meta name="robots" content="noindex">\n' if DRAFT else ""
    banner = '    <p class="meta"><strong>Draft for review</strong> — not yet published.</p>\n\n' if DRAFT else ""
    ld = {"@context": "https://schema.org", "@type": ld_type, "name": title, "url": url, "inLanguage": "en",
          "isPartOf": {"@type": "WebSite", "name": "Mysteriendramen", "url": f"{BASE}/"},
          "author": {"@type": "Person", "name": "Alexander G. Höhne", "url": "https://alexanderhoehne.ch/"}}
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="de" href="{de_url}">
<link rel="alternate" hreflang="x-default" href="{de_url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mysteriendramen">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="de_CH">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Mysteriendramen — mysteriendramen.ch">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
<a class="skip-link" href="#content">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/en/">Mysteriendramen</a>
    <div class="tagline">Research, dramaturgy and interpretation of Rudolf Steiner’s Mystery Dramas</div>
    <nav class="site-nav">
{nav}
    </nav>
  </div>
</header>

<main id="content">
  <div class="wrap">

{banner}    <h1>{h1}</h1>

{body}
  </div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <span>© 2026 Alexander Höhne</span>
    <span>Texts prepared with AI assistance · <a href="/en/legal-notice.html#ai">Note</a></span>
    <span>More: <a href="https://alexanderhoehne.ch">alexanderhoehne.ch</a> · <a href="https://karmaforschung.ch" hreflang="de">karmaforschung.ch</a></span>
    <a href="/en/legal-notice.html">Legal notice &amp; privacy</a>
  </div>
</footer>

</body>
</html>
'''


PAGES = {}

# ---------------------------------------------------------------- Home
PAGES["index.html"] = page(
    "index.html",
    "Rudolf Steiner’s Mystery Dramas: Research and Dramaturgy",
    "Essays, research and dramaturgical notes on Rudolf Steiner’s four Mystery Dramas by Alexander G. Höhne, long-time dramaturgical adviser at the Goetheanum stage.",
    "Approaches to the Mystery Dramas",
    '''    <p>This site is devoted to a single, unusually dense body of work: the four Mystery Dramas that Rudolf Steiner wrote between 1910 and 1913 — <em>The Portal of Initiation</em>, <em>The Soul’s Probation</em>, <em>The Guardian of the Threshold</em> and <em>The Souls’ Awakening</em>. Four closely linked plays follow the inner development of a group of characters across several lives.</p>

    <p>I approach them from two sides at once: as a scholar of language and literature who studies their images, motifs and place in the literature around 1900, and as a long-time dramaturgical adviser at the Goetheanum stage in Dornach, who knows them from practical work — from conversations with directors and performers, and from rehearsals and performances.</p>

    <p><strong>The articles on this site are written in German.</strong> This English section offers a way in: an overview of the four plays, a guide to their characters, and English summaries of every article.</p>

    <hr class="rule">

    <h2>Start here</h2>
    <ul>
      <li><a href="/en/four-mystery-dramas.html">The Four Mystery Dramas</a> — titles, first performances and the core of each play</li>
      <li><a href="/en/characters.html">The Characters of the Mystery Dramas</a> — the figures, their forms of knowing and their earlier lives</li>
      <li><a href="/en/articles.html">Articles</a> — English summaries of all articles, with links to the German originals</li>
    </ul>

    <h2>About me</h2>
    <p>I am Alexander G. Höhne. My background is in German linguistics, bordering on literary studies. In 2005 I received my doctorate from the German Department of the University of Basel with a study of mirror metaphors in Rudolf Steiner’s four Mystery Dramas, published in 2006 in the series <em>Basler Studien zur deutschen Sprache und Literatur</em> (A. Francke Verlag). Since then I have been working on a literary-historical study that places these plays in the context of modernism around 1900.</p>
    <p>From 2013 to 2017 I was officially dramaturgical adviser to the <em>Faust</em> production at the Goetheanum, and from 1988 to 2025 I accompanied the stage informally as a dramaturgical adviser, mainly in conversation with the directors. More about my work: <a href="https://alexanderhoehne.ch">alexanderhoehne.ch</a>.</p>
    <p>New articles appear in German roughly every two weeks, occasionally more often. My second research field, reincarnation and karma in European intellectual history, has its own site: <a href="https://karmaforschung.ch" hreflang="de">karmaforschung.ch</a> <span class="meta">(in German)</span>.</p>
''',
    "/en/", "WebPage")

# ---------------------------------------------------------------- Four dramas
PAGES["four-mystery-dramas.html"] = page(
    "four-mystery-dramas.html",
    "Rudolf Steiner’s Four Mystery Dramas: An Overview",
    "An introduction to Rudolf Steiner’s four Mystery Dramas: titles, first performances in Munich 1910–1913 and the core of each play.",
    "The Four Mystery Dramas: An Overview",
    f'''    <p>Between 1910 and 1913 Rudolf Steiner wrote four closely connected plays that are usually called the “Mystery Dramas” today. Steiner gave each play a subtitle of its own; <em>The Portal of Initiation</em>, for instance, he called “A Rosicrucian Mystery”. Each was first performed in Munich in August of its year — a small festival rhythm of its own, spread over four summers.</p>

    <h2>The Portal of Initiation (1910)</h2>
    <p><em>Die Pforte der Einweihung.</em> First performed on 15 August 1910 at the Schauspielhaus in Munich. At its centre is the painter Johannes Thomasius, who sets out on a path of initiation together with Maria under the guidance of the spiritual teacher Benedictus. Johannes has to come to know himself in painful inner trials, and in doing so he encounters the adversary powers Lucifer and Ahriman. Around him stand the learned Professor Capesius and the scientifically trained, sceptical Doctor Strader — two figures who, each in his own way, are also searching for knowledge.</p>

    <h2>The Soul’s Probation (1911)</h2>
    <p><em>Die Prüfung der Seele.</em> First performed on 17 August 1911 at the Gärtnerplatz-Theater in Munich. The second play continues the action but turns the view towards the past: Capesius, Maria and Johannes experience a retrospect into earlier incarnations in the fourteenth century. There Capesius is the First Preceptor of the Templar order and the head of a mine; he had separated from his family early on, before he became a Templar. The individuality we know as Maria was then a monk, preacher and administrator of the church, who upheld the cause of the church against the Templar order. Johannes, in this constellation, is the son of the earlier Capesius and at the same time a pupil of that monk. It is the monk who estranges Johannes from his father, because the two hold different views of truth and spirit. This entanglement has to be transformed in the present through conscious knowledge.</p>

    <h2>The Guardian of the Threshold (1912)</h2>
    <p><em>Der Hüter der Schwelle.</em> First performed on 24 August 1912, again at the Gärtnerplatz-Theater in Munich. Johannes falls under the influence of Lucifer, and his love turns to Theodora. The “Guardian of the Threshold” of the title is a stern watcher who demands that Johannes free himself from what binds him to the conditions of everyday life before he crosses into the spiritual world. Before him Johannes recognises that his being in love was not directed at Theodora but at a projection: he had fallen in love with an image of his own wishes that had merely taken on Theodora’s form. At this moment his Double steps towards him: „Erkenne mich – und schaue dich in mir.“ (“Know me – and see yourself in me.”)</p>

    <h2>The Souls’ Awakening (1913)</h2>
    <p><em>Der Seelen Erwachen.</em> First performed on 22 August 1913 at the Volkstheater in Munich. The fourth and last play shows how the pupils around Benedictus try to put their spiritual insights into concrete, earthly work — an undertaking that threatens to fail through inner resistance and outer scepticism. At the end Strader dies; in his last lines he writes that the obstacles did not come only from outside but also from inner shortcomings of his work. At the same time, deeper karmic connections across the group’s earlier lives come to light.</p>

    <h2>What connects the four plays</h2>
    <p>All four plays share the same circle of characters — Johannes Thomasius, Maria, Capesius, Strader, Benedictus and others — and follow them across several incarnations. This “drama of reincarnation”, as one might call it, is the real dramaturgical construction: not a continuous plot in the classical sense, but a path of development that stretches across lifetimes and ages and is seen from a different angle in each of the four parts. A guide to the figures is on the page <a href="/en/characters.html">The Characters of the Mystery Dramas</a>.</p>

    <p class="meta">Quotations from the plays are given in the German original; the English renderings in brackets are my own.</p>

    <h2>Read on</h2>
    <ul>
      <li>{de("/blog/2026-09-06-vier-dramen-ueberblick.html", "Die vier Dramen im Überblick")} — the German original of this page</li>
      <li>{de("/blog/2026-09-20-spiegelmetaphorik.html", "Die Spiegelmetaphorik in den Mysteriendramen")} — on mirror metaphors</li>
      <li>{de(KF, "Karma auf der Bühne")} — how the plays show karma on stage (karmaforschung.ch)</li>
    </ul>
''',
    "", "Article")

# ---------------------------------------------------------------- Characters
PAGES["characters.html"] = page(
    "characters.html",
    "The Characters of Rudolf Steiner’s Mystery Dramas",
    "Johannes Thomasius, Maria, Capesius, Strader, Theodora, Felix Balde, Benedictus and the spiritual figures: the characters of the four Mystery Dramas and their earlier lives.",
    "The Characters of the Mystery Dramas",
    f'''    <p>Rudolf Steiner’s four Mystery Dramas — <em>The Portal of Initiation</em> (1910), <em>The Soul’s Probation</em> (1911), <em>The Guardian of the Threshold</em> (1912) and <em>The Souls’ Awakening</em> (1913) — share a common circle of characters. The same people meet one another across all four plays and, in the retrospects, also in earlier lives. This page introduces the most important figures briefly. An outline of the plot is given in <a href="/en/four-mystery-dramas.html">The Four Mystery Dramas</a>.</p>

    <p>The fairy-tale quality of the plays has to do with their starting point. Steiner developed them from a process that he himself describes as putting Goethe’s <em>Fairy Tale of the Green Snake and the Beautiful Lily</em> on the stage; his own statements and the drafts of the plays (GA 44) show this very clearly. Goethe’s fairy tale in turn takes up Johann Valentin Andreae’s <em>Chymical Wedding of Christian Rosenkreutz</em> (1616). The Mystery Dramas are thus a dramatisation of soul-spiritual experiences and insights in a tradition that leads from Andreae through Goethe to Steiner. Other authors also play a part but remain in the background: Lessing with the <em>Hamburg Dramaturgy</em> and <em>Nathan the Wise</em>, Goethe’s novel of development <em>Wilhelm Meister</em>, and the mythology and legends of Faust.</p>

    <p>So, alongside the human beings, the plays bring stage figures that seem like figures from a fairy tale. Some take up historical and mythological figures, others create a new mythology, such as the figures of the soul forces and the temple guardians. These figures are linked to real characters in the plays, but in the soul-spiritual realms they represent something other than themselves — a kind of soul-spiritual alchemy. Lucifer and Ahriman, by contrast, appear as forces outside the human being. They serve human development reluctantly, yet would gladly make human beings useful for their own interests. Thus representatives of ordered and healthy soul-spiritual forces stand opposite reluctant, disordered, disruptive and illness-causing forces (see <a href="#spiritual-figures">Spiritual figures</a>).</p>

    <p class="meta">Contents: <a href="#centre">Johannes and Maria</a> · <a href="#knowing">Forms of knowing</a> · <a href="#spiritual-figures">Spiritual figures</a> · <a href="#earlier-lives">Earlier lives</a> · <a href="#more">Further figures</a></p>

    <h2 id="centre">Johannes and Maria</h2>

    <h3 id="johannes-thomasius">Johannes Thomasius</h3>
    <p>A painter and the central developing figure of the four plays. Maria leads him to the path of spiritual training under Benedictus. Johannes is interested in the forces of Lucifer and Ahriman because he recognises them at work within himself, above all Lucifer, who works in beautiful semblance. As a painter, Johannes works in exactly this field. His training therefore aims at distinguishing, within beautiful semblance, what is humane and beneficial from what creates illusion and delusion. In the sense of building a competence, this distinction must succeed not only intellectually but also emotionally and in one’s intentions. In <em>The Guardian of the Threshold</em> he recognises that his being in love was not directed at Theodora but at a projection: he had fallen in love with an image of his own wishes that had merely taken on Theodora’s form. At this moment he meets his Double. In depth: {de("/blog/2026-10-04-johannes-thomasius.html", "Johannes Thomasius — Porträt einer Entwicklungsfigur")}.</p>

    <h3 id="maria">Maria</h3>
    <p>A pupil of Benedictus and the one who leads Johannes onto the spiritual path. The retrospects show that this bond has a prehistory: in the fourteenth century Maria’s individuality was a monk, preacher and administrator of the church, and the teacher of young Thomas, Johannes’ earlier incarnation; in the Egyptian retrospect of <em>The Souls’ Awakening</em> she is the youth who, as a neophyte, is to receive the temple’s consecration in order to become counsellor to the king (see <a href="#earlier-lives">Earlier lives</a>).</p>

    <h2 id="knowing">Forms of knowing</h2>
    <p>Around Johannes and Maria stand figures who each embody a form of knowing of their own. On one side are two representatives of scientific thinking with different starting points; on the other, three figures who know in imaginative or spiritual ways.</p>

    <p><strong>Scientific thinking</strong></p>

    <h3 id="capesius">Professor Capesius</h3>
    <p>Capesius represents historically oriented scholarship in the humanities. <em>The Soul’s Probation</em> opens with his shock: „Bin ich denn noch, der ich vordem war?“ (“Am I still the one I was before?”) There follows his retrospect into the fourteenth century, in which he recognises himself as First Preceptor of the Templar order and head of a mine, and in young Thomas his own son.</p>

    <h3 id="strader">Doctor Strader</h3>
    <p>Strader represents modern natural science. In the fourteenth century his individuality appears as Simon, a natural scientist and physician of Jewish culture. In <em>The Souls’ Awakening</em> he dies; in his last lines he writes that the obstacles to his work came not only from outside but also from its own inner shortcomings.</p>

    <p><strong>Imaginative and spiritual knowing</strong></p>
    <p>Theodora and Felix Balde work with a natural gift and develop their experiences directly. Benedictus, by contrast, joins his experiences to an ordered training.</p>

    <h3 id="theodora">Theodora</h3>
    <p>Theodora has a mediumistic gift through which she can grasp spiritual processes imaginatively. In <em>The Guardian of the Threshold</em> Johannes falls in love with her, until he recognises that it was not Theodora he loved but an image of his own wishes that had merely taken on her form.</p>

    <h3 id="felix-balde">Felix Balde</h3>
    <p>Felix Balde has a perceptive gift through which he grasps the processes of nature imaginatively.</p>

    <h3 id="benedictus">Benedictus</h3>
    <p>The spiritual teacher around whom the community of pupils forms. Benedictus, too, works with imaginative experience, but he raises it to inspired and intuitive forms of knowing. These terms are meant in the sense of Steiner’s stages of higher knowledge (<em>The Stages of Higher Knowledge</em>, GA 12), not in their everyday use. He joins his experiences to an ordered training in the tradition of modern orders and brotherhoods. From this, together with his pupils, he develops a new method of spiritual education. It no longer depends on withdrawal, seclusion and the protection of vows of silence, but seeks to appear and to be effective in public. In <em>The Souls’ Awakening</em> his pupils try to put their spiritual insights into concrete, earthly work.</p>

    <h2 id="spiritual-figures">Spiritual figures</h2>

    <h3 id="lucifer-ahriman">Lucifer and Ahriman</h3>
    <p>The two adversary powers, shown as forces outside the human being. They serve human development reluctantly, yet seek to make human beings useful for their own interests. Lucifer works in beautiful semblance, in illusion and delusion. Both confront Johannes already in the trials of <em>The Portal of Initiation</em>; in <em>The Guardian of the Threshold</em> he falls under Lucifer’s influence.</p>

    <h3 id="guardian">The Guardian of the Threshold</h3>
    <p>The stern watcher at the boundary of the spiritual world, after whom the third play is named. He demands that Johannes free himself from what binds him to everyday life only in outer social and practical life. Beyond the threshold other conditions apply — another logic or culture, as it were. It cannot be grasped or acquired as long as one clings to the familiar conditions as the only possible way of living and experiencing.</p>

    <h3 id="double">The Double</h3>
    <p>In the moment of his self-knowledge, Johannes’ Double steps towards him: „Erkenne mich – und schaue dich in mir.“ (“Know me – and see yourself in me.”) The scene is a key example of the mirror metaphors through which the plays make encountering oneself the condition of knowledge: {de("/blog/2026-09-20-spiegelmetaphorik.html", "Die Spiegelmetaphorik in den Mysteriendramen")}.</p>

    <h2 id="earlier-lives">Earlier lives</h2>
    <p>Two retrospects show the familiar characters in earlier incarnations. The list of characters and the stage directions assign them explicitly.</p>

    <h3 id="fourteenth-century">Fourteenth century (<em>The Soul’s Probation</em>)</h3>
    <ul>
      <li><strong>Thomas</strong>, a master miner, is the earlier incarnation of Johannes.</li>
      <li><strong>His father</strong>, First Preceptor of the Templar order and head of the mine, is the earlier incarnation of Capesius. He had separated from his family early on, before he became a Templar.</li>
      <li><strong>The monk</strong>, preacher and administrator of the church, is the earlier incarnation of Maria. He is Thomas’ teacher and upholds the cause of the church against the Templar order.</li>
      <li><strong>Simon</strong>, a natural scientist and physician of Jewish culture, is the earlier incarnation of Strader.</li>
    </ul>
    <p>Thomas finds his father and at the same time has to recognise that he is his teacher’s opponent: „Ich habe ihn zum zweiten Mal verloren.“ (“I have lost him a second time.”) Between father and teacher, between Templar order and church, stand different views of truth and spirit.</p>

    <h3 id="third-cultural-epoch">“Third cultural epoch of the earth” (<em>The Souls’ Awakening</em>)</h3>
    <p>The retrospect leads into a “temple in the Egyptian style”. The individuality of Johannes appears as an <strong>Egyptian woman</strong>. I read her as the companion of a <strong>youth</strong>, Maria’s individuality, who as a <strong>neophyte</strong> is to receive the temple’s consecration in order to become counsellor to the king. With this he enters a different social circle and commits himself to a different way of life.</p>
    <p>For the Egyptian woman this means a double separation: social, because her partner leaves their shared circle of life, and inner, because from now on he leads his life by other standards. She laments that he must tear himself away from her „für immer“ (“for ever”), and speaks of „Trauer nur für mich, Entsagung, Leid“ (“grief alone for me, renunciation, sorrow”).</p>
    <p>How the plays show these connections rather than explain them is the subject of {de(KF, "Karma auf der Bühne")} on karmaforschung.ch.</p>

    <h2 id="more">Further figures</h2>
    <p>The circle of characters is larger than this first version shows. Further figures will be added as they are treated in articles of their own.</p>

    <p class="meta">Quotations from the plays are given in the German original; the English renderings in brackets are my own. German original of this page: {de("/gestalten.html", "Die Gestalten der Mysteriendramen")}.</p>
''',
    "/en/characters.html", "CollectionPage")

# ---------------------------------------------------------------- Articles
ARTICLES = [
    ("2026-10-30-messianismus", "30 October 2026", "Contexts",
     "Redemption as a path? The Mystery Dramas and messianism",
     "The years around 1900 were full of messianic expectation. The article distinguishes Steiner’s talk of the reappearance of Christ in the etheric — a change in human perception, not the arrival of a person — from the messianism of his time, looks at Theodora’s vision in <em>The Portal of Initiation</em>, and sets the plays beside the conflict over Krishnamurti, in the course of which the Anthroposophical Society was founded."),
    ("2026-11-01-steiner-unter-zeitgenossen", "29 October 2026", "Contexts",
     "Steiner among his contemporaries — Schuré, Maeterlinck, Hofmannsthal",
     "The Mystery Dramas as theatre of literary modernism: Édouard Schuré as a forerunner, Maurice Maeterlinck and Hugo von Hofmannsthal as neighbours and counterpoles. The plays ask the same questions as their contemporaries — how theatre can show the inner life, what language can still achieve — and answer them in their own way, with a drama of conversation that makes knowing itself the dramatic event."),
    ("2026-10-18-kein-lesedrama", "18 October 2026", "Dramaturgy",
     "Not a closet drama — how I came to the stage of the Mystery Dramas",
     "From a first reading through the Goetheanum performance of 1989 to many years of dramaturgical advice: a personal account of why the mystery of these plays lies in language and conversation, and why they need the stage."),
    ("2026-10-04-johannes-thomasius", "4 October 2026", "Characters",
     "Johannes Thomasius — portrait of a developing figure",
     "Johannes Thomasius is the central developing figure of the four plays: from the painter who follows Maria, through the retrospect into an earlier life, to the self-knowledge before the Guardian of the Threshold and the meeting with his Double."),
    ("2026-09-20-spiegelmetaphorik", "20 September 2026", "Aspects",
     "Mirror metaphors in the Mystery Dramas",
     "Why the plays again and again let their characters meet themselves — as a Double, as an earlier life, as a higher self. Where Romantic literature made the encounter with one’s double an image of terror, the Mystery Dramas make it the condition of knowledge. Based on my doctoral thesis (Basel 2005/2006)."),
    ("2026-09-06-vier-dramen-ueberblick", "6 September 2026", "General",
     "The four dramas at a glance",
     "An introduction for new readers: titles, first performances and the core of each of Steiner’s four Mystery Dramas. Also available in English: <a href=\"/en/four-mystery-dramas.html\">The Four Mystery Dramas</a>."),
    ("2026-08-23-neustart", "23 August 2026", "General",
     "A new start: why this site is coming back to life",
     "A look back at the first articles of 2022 and an explanation of why mysteriendramen.ch is now being continued regularly."),
]
items = "\n".join(
    f'''      <li>
        <div class="meta">{d} &middot; <span class="tag">{c}</span></div>
        <h2><a href="/blog/{slug}.html" hreflang="de">{t}</a></h2>
        <p class="post-excerpt">{s} <span class="meta">(Article in German)</span></p>
      </li>''' for slug, d, c, t, s in ARTICLES)
PAGES["articles.html"] = page(
    "articles.html",
    "Articles on Rudolf Steiner’s Mystery Dramas — English summaries",
    "English summaries of all articles on mysteriendramen.ch about Rudolf Steiner’s Mystery Dramas: research, contexts and dramaturgy.",
    "Articles",
    f'''    <p>All articles on this site are written in German. Here you will find an English summary of each, with a link to the original. The titles in English are my translations. New articles appear roughly every two weeks, occasionally more often.</p>

    <ul class="post-list">
{items}
    </ul>
''',
    "/en/articles.html", "CollectionPage")

# ---------------------------------------------------------------- Legal notice
PAGES["legal-notice.html"] = page(
    "legal-notice.html",
    "Legal notice and privacy policy — Mysteriendramen",
    "Legal notice and privacy policy of mysteriendramen.ch, based on Swiss data protection law and, where applicable, the EU General Data Protection Regulation.",
    "Legal notice and privacy policy",
    '''    <p><strong>Responsible for the content:</strong><br>
    Alexander G. Höhne<br>
    Dornacherstrasse 49-51<br>
    CH-4053 Basel<br>
    Switzerland</p>

    <p><strong>Contact:</strong><br>
    E-mail: <a href="mailto:alexander@alexanderhoehne.ch">alexander@alexanderhoehne.ch</a></p>

    <p class="meta">This is a translation of the <a href="/impressum.html" hreflang="de">German legal notice</a>. In case of doubt, the German version applies.</p>

    <h2>Disclaimer</h2>
    <p>The content of this site has been prepared with care but makes no claim to completeness, currency or scholarly finality. No liability is accepted for links to external websites; their operators alone are responsible for their content.</p>

    <h2 id="privacy">Privacy policy</h2>
    <p><strong>Legal framework.</strong> This site is operated from Switzerland. The processing of personal data is governed by the Swiss Federal Act on Data Protection (FADP). Where the EU General Data Protection Regulation (GDPR) applies to visitors from the European Union or the European Economic Area, this policy is also intended to provide the information required by the GDPR.</p>
    <p><strong>Controller</strong> for the processing of personal data on mysteriendramen.ch is Alexander G. Höhne, Dornacherstrasse 49-51, CH-4053 Basel, Switzerland, e-mail: <a href="mailto:alexander@alexanderhoehne.ch">alexander@alexanderhoehne.ch</a>.</p>
    <p><strong>No data collection of my own.</strong> This site uses no cookies, no analytics or tracking tools, no forms and no comment function. I myself do not collect any personal data when you visit the site.</p>
    <p><strong>Hosting via GitHub Pages.</strong> The site is served by GitHub Pages, a service of GitHub, Inc. (USA). According to GitHub, it logs and stores visitors’ IP addresses for security reasons when the site is accessed. This data may be transferred to the USA. The processing serves the secure and reliable delivery of the site (under the GDPR: legitimate interest, Art. 6(1)(f)). Details: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub General Privacy Statement</a>.</p>
    <p><strong>Fonts.</strong> The typeface Cormorant Garamond (SIL Open Font License) is hosted on this site itself. No data is transmitted to Google or other font providers when the site is accessed.</p>
    <p><strong>Contact by e-mail.</strong> If you write to me, I use your e-mail address and the content of your message only to answer your enquiry (under the GDPR: Art. 6(1)(b) or (f)). I do not pass this data on and delete it when it is no longer needed.</p>
    <p><strong>External links.</strong> Links to other websites transmit data to their operators only when you click on them. The respective operators are responsible for their data processing.</p>
    <p><strong>Your rights.</strong> You can request information about the personal data I hold about you, and its correction or deletion. Where the GDPR applies, you also have the right to restriction of processing, to object, and to data portability. Please contact me at the e-mail address above. You also have the right to lodge a complaint with a supervisory authority — in Switzerland the Federal Data Protection and Information Commissioner (FDPIC), in the EU the data protection authority of your country of residence.</p>
    <p class="meta">Last updated: October 2026</p>

    <h2 id="ai">Use of artificial intelligence</h2>
    <p>The texts on this site are prepared with the assistance of artificial intelligence (Claude, Anthropic): in drafting, editing, copy-editing and translation. Alexander G. Höhne is responsible for content, selection, the checking of sources and the final version.</p>
    <p>AI is used only in preparing the texts. No data is transmitted to AI services when you visit this site.</p>

    <h2>Copyright</h2>
    <p>All texts on this site are subject to the author’s copyright unless otherwise indicated. Re-use is permitted only with prior consent and with acknowledgement of the source.</p>
''',
    "/en/legal-notice.html", "WebPage")

OUT.mkdir(parents=True, exist_ok=True)
for name, html in PAGES.items():
    (OUT / name).write_text(html, encoding="utf-8", newline="\n")
print("written:", ", ".join(PAGES))

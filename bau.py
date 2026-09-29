"""Baut index.html für EDGE x Deutsche Bank (Stamm: EDGE Unternehmenspräsentation, bereit.edge-digital.ai).

Aufruf:  python3 bau.py
Folien, Texte, Logos und Collage werden hier gepflegt, nie direkt in index.html.
Gestaltung: Stamm aus cbl-ueberblick (Raumschwarz, Galaxie, Avenir Next, Schimmer).
Dramaturgie: von ROT und vielen ECKEN zu BLAU ohne Ecken, am Ende bleibt nur die Kante: die EDGE.
"""
import json
import math
import random
from pathlib import Path

ORDNER = Path(__file__).parent

# ----------------------------------------------------------------------------
# Inhalte
# ----------------------------------------------------------------------------

BAUSTELLEN = [
    ("fachkraefte", "Fachkräfte", "Gute Menschen werden schwerer zu gewinnen und teurer zu verlieren.", "Recruiting · Arbeitgeberattraktivität · Wissen"),
    ("kundengewinnung", "Kundengewinnung", "Aufmerksamkeit wird knapper. Akquise wird aufwendiger. Geschwindigkeit entscheidet.", "Leads · Vertrieb · Neukunden"),
    ("sichtbarkeit", "Sichtbarkeit", "Wer digital nicht relevant ist, findet immer weniger statt.", "KI statt Google · Social Media · Content"),
    ("kundenverstaendnis", "Kundenverständnis", "Märkte verändern sich schneller, als klassische Analysen mithalten können.", "Zielgruppen · Daten · Trends"),
    ("erreichbarkeit", "Erreichbarkeit", "Kunden erwarten Antworten sofort, unabhängig von Uhrzeit und Kanal.", "Telefon · Website · Support"),
    ("prozesse", "Prozesse &amp; KI", "Mitarbeiter nutzen KI längst. Prozesse, Systeme und Datenschutz hinken hinterher.", "Datenschutz · Digitale Souveränität · Automatisierung"),
]

# Referenzen, für die es noch keine Logodatei gibt: erscheinen als Schriftzug. Ziel ist eine leere Liste.
NUR_TEXT = ["Rotary Club", "Forum Ehrenamt", "TH Lübeck", "Energiecluster", "Stadtwerke Geesthacht", "Sprungtuch",
            "Change School Summit", "Digital für alle", "TQ", "K2Konzept", "HanseFriseur", "EGOH"]

# (name, kennung eines Trägerlogos oder None). Der Überflieger hat kein eigenes Logo, er läuft unter StartUp SH.
PREISE = [("Existenzgründerpreis", "lnpreis"), ("Gründerpreis der Sparkasse zu Lübeck", "sparkasse"), ("Social Hackathon", "socialhackathon"), ("Überflieger Wettbewerb", "startupsh")]

# Team: (name, rolle, bilddatei oder None)
SERVICE_KOPF = ("Eddie", "Head of AI-Services", "eddie.png")
SERVICE = [("Chakira", "AI Content Creatorin", "chakira.png"), ("Sohal", "AI Network Expertin", "sohal.png"), ("Jorge", "Data Scientist", "jorge.png")]
SOFTWARE_KOPF = ("Dom", "Head of AI-Software", "dom.png")
SOFTWARE = [("Mats", "Frontend Entwickler", "mats.png"), ("Saroj", "Backend Entwickler", "saroj.png"), ("Nadira", "AI und Software Engineer", "nadira.png")]

SERVICE_PUNKTE = ["Fachkräftesicherung (+2000 Bewerbungen allein in 2025)", "Kundengewinnung (wöchentliche Neukundengespräche)",
                  "Digitale Sichtbarkeit (Tausende Follower aufgebaut)", "Zielgruppenanalysen mit Millionen von Datenpunkten",
                  "Schulungen, Workshops und Webinare für Ihr Team", "Websites, Werbekampagnen, Content und vieles mehr"]
SOFTWARE_PUNKTE = ["KI aus Deutschland, für Deutschland", "Datenschutzkonforme KI", "Telefon-KI: rund um die Uhr erreichbar für Ihre Kunden",
                   "Website Chatbots für Ihre Kunden", "Schnittstellen zu all Ihren Tools", "KI-Workflows in Ihrer Firma implementieren"]

KONTAKT_MAIL = "emre@edge-digital.com"
KONTAKT_TEL = "0157 72461737"

# ----------------------------------------------------------------------------
# Formen als SVG. Fester Zufallsstart, damit jeder Bau gleich aussieht.
# ----------------------------------------------------------------------------

def wuerfel(cx, cy, s):
    """Isometrischer Drahtwürfel: Sechseck plus drei Kanten zur Mitte."""
    w, h = 0.866 * s, 0.5 * s
    aussen = [(cx, cy - s), (cx + w, cy - h), (cx + w, cy + h), (cx, cy + s), (cx - w, cy + h), (cx - w, cy - h)]
    pfad = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in aussen) + " Z"
    pfad += f" M{cx:.0f},{cy:.0f} L{cx:.0f},{cy + s:.0f} M{cx:.0f},{cy:.0f} L{cx + w:.0f},{cy - h:.0f} M{cx:.0f},{cy:.0f} L{cx - w:.0f},{cy - h:.0f}"
    return pfad


def kunst_rot():
    """Würfel und Pixel mit roten Neonkanten. Digitale Bedrohung, links bleibt Platz für die Schrift."""
    z = random.Random(7)
    lagen = [(1490, 520, 250), (1180, 250, 110), (1760, 190, 90), (1820, 820, 150), (1230, 860, 130), (960, 640, 60),
             (1610, 960, 70), (1010, 130, 50), (1380, 90, 40), (700, 960, 46), (380, 110, 38), (1900, 480, 60), (120, 900, 70), (860, 380, 34)]
    pfade = " ".join(wuerfel(*l) for l in lagen)
    pixel = []
    for _ in range(95):
        # Pixel häufen sich rechts und an den Rändern, wie ein Befall, der sich ausbreitet
        x = int(z.triangular(0, 1920, 1560)); y = int(z.uniform(0, 1080)); g = z.choice([8, 8, 12, 12, 16, 22, 30])
        x -= x % 16; y -= y % 16
        if 120 < x < 1000 and 330 < y < 760:
            continue
        pixel.append(f'<rect x="{x}" y="{y}" width="{g}" height="{g}" fill="#FF2D3D" opacity="{z.uniform(.12, .75):.2f}"/>')
    balken = "".join(f'<rect x="{int(z.uniform(900, 1700))}" y="{int(z.uniform(60, 1020))}" width="{int(z.uniform(80, 340))}" height="3" fill="#FF5A3C" opacity="{z.uniform(.25, .6):.2f}"/>' for _ in range(9))
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="gl-rot" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="9"/></filter></defs>
  <g fill="none" stroke="#FF1F3D" stroke-width="7" stroke-linejoin="miter" filter="url(#gl-rot)" opacity=".75"><rect width="1920" height="1080" fill="none" stroke="none"/><path d="{pfade}"/></g>
  <g fill="rgba(255,31,61,.05)" stroke="#FF5468" stroke-width="2.5" stroke-linejoin="miter"><path d="{pfade}"/></g>
  {"".join(pixel)}{balken}
</svg>'''


def dreieck(cx, cy, r, dreh):
    """Gleichseitiges Dreieck, Spitze nach oben, um wenige Grad gedreht."""
    punkte = []
    for k in range(3):
        a = math.radians(-90 + 120 * k + dreh)
        punkte.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in punkte) + " Z"


def kunst_pink():
    """Weiche Dreiecke mit runden Ecken, die Spitze zeigt immer leicht nach oben."""
    lagen = [(1480, 560, 330, 8, .30), (1130, 300, 150, -14, .22), (1790, 250, 120, 19, .26), (1760, 880, 170, -9, .20),
             (1150, 850, 120, 12, .24), (880, 170, 70, -20, .20), (330, 930, 90, 16, .16), (150, 170, 60, -11, .16), (960, 960, 50, 6, .20)]
    teile = []
    for cx, cy, r, dreh, deck in lagen:
        d = dreieck(cx, cy, r, dreh); rund = max(14, r * .22)
        # Dicke Kontur in Füllfarbe mit runden Ecken ergibt die iPhone Ecke
        teile.append(f'<path d="{d}" fill="url(#vl-pink)" stroke="url(#vl-pink)" stroke-width="{rund:.0f}" stroke-linejoin="round" opacity="{deck}"/>')
    glut = "".join(f'<path d="{dreieck(cx, cy, r, dreh)}" fill="none" stroke="#FF6FBA" stroke-width="{max(14, r * .22) + 8:.0f}" stroke-linejoin="round" opacity=".28"/>' for cx, cy, r, dreh, _ in lagen[:5])
    kontur = "".join(f'<path d="{dreieck(cx, cy, r + max(14, r * .22) / 2, dreh)}" fill="none" stroke="#FFB3DC" stroke-width="2" stroke-linejoin="round" opacity=".55"/>' for cx, cy, r, dreh, _ in lagen)
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="gl-pink" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="26"/></filter>
  <linearGradient id="vl-pink" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC2E4"/><stop offset="1" stop-color="#FF3D9A"/></linearGradient></defs>
  <g filter="url(#gl-pink)"><rect width="1920" height="1080" fill="none" stroke="none"/>{glut}</g>{"".join(teile)}{kontur}
</svg>'''


def kunst_lila():
    """Zwei Kreise, die sich überlappen, in zwei Lilatönen, die das Auge noch unterscheidet."""
    return '''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="gl-lila" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="34"/></filter></defs>
  <g filter="url(#gl-lila)" opacity=".55"><rect width="1920" height="1080" fill="none" stroke="none"/><circle cx="1260" cy="560" r="330" fill="none" stroke="#7C3AED" stroke-width="16"/><circle cx="1570" cy="560" r="330" fill="none" stroke="#C77DFF" stroke-width="16"/></g>
  <g style="mix-blend-mode:screen"><circle cx="1260" cy="560" r="330" fill="#6D28D9" opacity=".42"/><circle cx="1570" cy="560" r="330" fill="#B565F2" opacity=".38"/></g>
  <circle cx="1260" cy="560" r="330" fill="none" stroke="#9F67FF" stroke-width="2.5" opacity=".9"/><circle cx="1570" cy="560" r="330" fill="none" stroke="#DDA8FF" stroke-width="2.5" opacity=".9"/>
</svg>'''


def kunst_dunkelblau():
    """Einzelne Kreise, jeder für sich. Sie kündigen die runden Portraits der nächsten Folie an."""
    lagen = [(1500, 540, 250, .34), (1130, 250, 96, .26), (1800, 190, 70, .30), (1790, 900, 110, .24), (1120, 880, 74, .28), (870, 140, 40, .22), (250, 930, 56, .18), (140, 160, 34, .18)]
    voll = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#vl-db)" opacity="{o}"/>' for x, y, r, o in lagen)
    rand = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#5B8CFF" stroke-width="2.5" opacity=".85"/>' for x, y, r, _ in lagen)
    glut = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#2F5BFF" stroke-width="14"/>' for x, y, r, _ in lagen[:5])
    return f'''<svg class="kunst" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs><filter id="gl-db" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="22"/></filter>
  <radialGradient id="vl-db" cx=".35" cy=".3" r=".9"><stop offset="0" stop-color="#3D6BFF"/><stop offset="1" stop-color="#0B1E8A"/></radialGradient></defs>
  <g filter="url(#gl-db)" opacity=".6"><rect width="1920" height="1080" fill="none" stroke="none"/>{glut}</g>{voll}{rand}
</svg>'''


def kunst_kante(kennung, stopps):
    """Die EDGE: eine leuchtende Kante am Rand eines dunklen Körpers. stopps = Farbverlauf entlang der Kante.

    Bewusst OHNE SVG Filter gebaut: Safari schneidet deren Schein an der Formgrenze ab.
    Ein senkrechter Farbverlauf wird durch einen kreisförmigen Verlauf maskiert, das rendert überall gleich.
    """
    # Oben und unten läuft die Kante ins Nichts aus, dazwischen liegen die Farben
    farben = ", ".join(f"{f} {18 + o * 64:.0f}%" for o, f in stopps)
    verlauf = f"linear-gradient(to bottom, transparent 3%, {farben}, transparent 97%)"
    mitte = "1640px 540px"
    schein = f"radial-gradient(circle at {mitte}, transparent 0, transparent 637px, rgba(0,0,0,.95) 639px, #000 641px, rgba(0,0,0,.62) 645px, rgba(0,0,0,.34) 664px, rgba(0,0,0,.16) 710px, rgba(0,0,0,.06) 790px, transparent 900px)"
    koerper = f"radial-gradient(circle at {mitte}, #030309 0, #030309 637px, transparent 640px)"
    return f'''<div class="kunst kante" aria-hidden="true">
  <div style="position:absolute;inset:0;background:{koerper};"></div>
  <div style="position:absolute;inset:0;background:{verlauf};-webkit-mask-image:{schein};mask-image:{schein};"></div>
</div>'''


# ----------------------------------------------------------------------------
# Bausteine
# ----------------------------------------------------------------------------

def kopf_kreis(name, rolle, bild, klasse, gross=False):
    """Rundes Portrait mit farbigem Ring. Ohne Bild erscheint ein markierter Platzhalter."""
    if bild:
        innen = f'<img src="assets/team/{bild}" alt="{name}" width="720" height="720">'
    else:
        innen = f'<span class="leer">{name[0]}</span>'
    zusatz = (" gross" if gross else "") + ("" if bild else " fehlt")
    return f'''<figure class="person {klasse}{zusatz}">
  <div class="rund">{innen}</div>
  <figcaption><b>{name}</b><span>{rolle}</span></figcaption>
</figure>'''


def team_seite(klasse, titel, kopf, leute, punkte):
    reihe = "".join(kopf_kreis(n, r, b, klasse) for n, r, b in leute)
    liste = "".join(f"<li>{p}</li>" for p in punkte)
    return f'''<div class="seite {klasse}">
  <p class="seiten-titel">{titel}</p>
  {kopf_kreis(*kopf, klasse, gross=True)}
  <div class="reihe">{reihe}</div>
  <ul class="punkte">{liste}</ul>
</div>'''


# ----------------------------------------------------------------------------
# Remix aus dem Rotary-Vortrag (EDGE x Rotary.key, Folien 13 bis 16)
# ----------------------------------------------------------------------------

# (Beschriftung, Zeit, Mitte der Insel im Bild in Prozent der Breite)
ZEITSTRAHL = [("Faustkeil &amp; Feuer", "vor 2,5 Mio. Jahren", 6.6), ("Schrift", "um 3000 v. Chr.", 18.6), ("Buchdruck", "um 1450", 30.6),
              ("Dampfmaschine", "um 1760", 43.2), ("Computer", "ab 1940", 56.3), ("Smartphone", "2007", 68.5),
              ("Avatare", "ab 2020", 80.3), ("KI", "heute", 92.7)]
ZEITSTRAHL_LINIE = 52.3  # Höhe der leuchtenden Linie im Bild, in Prozent

DREISCHRITT = [("Wir", "bedienten", "Technologie."), ("Wir", "kommunizierten", "mit Technologie."), ("Jetzt", "begegnen", "wir Technologie.")]


def kurve():
    """Moore's Law (Verdopplung alle 18 Monate) gegen KI (alle 6 Monate) über zehn Jahre, lineare Skala bis 100."""
    x0, x1, y0, y1 = 90, 1450, 560, 40
    px = lambda t: x0 + (x1 - x0) * t / 10
    py = lambda v: y0 - (y0 - y1) * min(v, 100) / 100
    def linie(halbwert, ende):
        schritte = [ende * i / 200 for i in range(201)]
        return "M" + " L".join(f"{px(t):.1f},{py(2 ** (t / halbwert)):.1f}" for t in schritte)
    ki_ende = 0.5 * math.log2(100)
    achsen = f'<path d="M{x0},{y1 - 10} L{x0},{y0} L{x1 + 20},{y0}" fill="none" stroke="rgba(244,246,255,.35)" stroke-width="2"/>'
    jahre = "".join(f'<text x="{px(t):.0f}" y="{y0 + 44}" text-anchor="middle">{t} J.</text>' for t in range(2, 11, 2))
    return f'''<svg class="kurve" viewBox="0 0 1520 640" aria-label="Moore's Law gegen KI-Wachstum">
  <defs><linearGradient id="vl-ki" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#2F5BFF"/><stop offset="1" stop-color="#7FD4FF"/></linearGradient></defs>
  {achsen}<g class="jahre">{jahre}</g>
  <path class="linie moore" pathLength="1" d="{linie(1.5, 10)}" fill="none" stroke="rgba(244,246,255,.55)" stroke-width="5" stroke-linecap="round"/>
  <path class="linie ki" pathLength="1" d="{linie(0.5, ki_ende)}" fill="none" stroke="url(#vl-ki)" stroke-width="8" stroke-linecap="round"/>
  <text class="kurven-name ki" x="{px(ki_ende) + 30:.0f}" y="{y1 + 20}">KI: alle 6 Monate doppelt</text>
  <text class="kurven-name moore" x="{x1}" y="{py(14):.0f}" text-anchor="end">Moore's Law: alle 18 Monate doppelt</text>
</svg>'''


EXTRA_STIL = """
/* ---------- EDGE x Deutsche Bank: Zusatzstil ---------- */
.titel-duo { display: flex; align-items: center; gap: 70px; }
.titel-duo .titel-logo { width: 560px; }
.titel-duo .mal { font-size: 90px; font-weight: 400; color: var(--w-45); line-height: 1; }
.titel-duo .db-logo { height: 210px; width: auto; display: block; margin: 0; }

.dreischritt { display: grid; grid-template-columns: repeat(3, auto); justify-content: space-between; gap: 50px; margin-top: auto; margin-bottom: auto; }
.dreischritt p { margin: 0; font-size: 58px; line-height: 1.12; font-weight: 700; text-transform: uppercase; letter-spacing: -.015em; white-space: nowrap; }
.dreischritt p span { display: block; }

.zs-buehne { position: absolute; left: 80px; top: 110px; width: 1760px; aspect-ratio: 1344 / 752; }
.zs-buehne img { --rand-x: linear-gradient(90deg, transparent 0, #000 7%, #000 93%, transparent 100%); --rand-y: linear-gradient(180deg, transparent 0, #000 22%, #000 80%, transparent 100%);
  -webkit-mask-image: var(--rand-x), var(--rand-y); -webkit-mask-composite: source-in; mask-image: var(--rand-x), var(--rand-y); mask-composite: intersect; }
.zs-buehne img { position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; object-fit: cover; margin: 0 !important; max-width: none !important; max-height: none !important; }
.zs-punkt { position: absolute; top: calc(var(--linie) + 9%); transform: translateX(-50%); text-align: center; white-space: nowrap; }
.zs-punkt b { display: block; font-size: 23px; font-weight: 700; letter-spacing: .01em; text-transform: uppercase; }
.zs-punkt span { display: block; font-size: 19px; color: var(--w-45); margin-top: 6px; }
.slide.zeitstrahl { justify-content: flex-start; }
.slide.zeitstrahl .headline { position: relative; }

.kurve { width: 100%; height: auto; margin-top: 30px; overflow: visible; }
.kurve .jahre text { font-size: 24px; fill: rgba(244,246,255,.45); font-family: var(--font); }
.kurve .kurven-name { font-size: 30px; font-weight: 700; font-family: var(--font); }
.kurve .kurven-name.ki { fill: #7FD4FF; }
.kurve .kurven-name.moore { fill: rgba(244,246,255,.7); }
.kurve .linie { stroke-dasharray: 1; stroke-dashoffset: 1; }
.kurve .kurven-name { opacity: 0; }
.reveal section.present .kurve .linie.moore { animation: zeichnen 2.4s .3s ease-out forwards; }
.reveal section.present .kurve .linie.ki { animation: zeichnen 1.6s 1.2s ease-in forwards; }
.reveal section.present .kurve .kurven-name.moore { animation: auftauchen .6s 2.5s forwards; }
.reveal section.present .kurve .kurven-name.ki { animation: auftauchen .6s 2.8s forwards; }
body.standbild .kurve .linie { stroke-dashoffset: 0; }
body.standbild .kurve .kurven-name { opacity: 1; }
@keyframes zeichnen { to { stroke-dashoffset: 0; } }
@keyframes auftauchen { to { opacity: 1; } }

.hero.frage { font-size: 112px; max-width: 1500px; }

/* Hochkant (Handy) */
body.hochkant .titel-duo { flex-direction: column; gap: 40px; align-items: flex-start; }
body.hochkant .titel-duo .titel-logo { width: 620px; }
body.hochkant .dreischritt { grid-template-columns: 1fr; gap: 90px; }
body.hochkant .dreischritt p { font-size: 70px; white-space: normal; }
body.hochkant .zs-buehne { width: 1080px; left: 0; top: 640px; }
body.hochkant .zs-punkt b { font-size: 26px; letter-spacing: 0; }
body.hochkant .zs-punkt span { display: none; }
body.hochkant .zs-punkt:nth-child(odd of .zs-punkt) { top: calc(var(--linie) - 22%); }
body.hochkant .hero.frage { font-size: 80px; }
"""


def bau():
    logos = json.loads((ORDNER / "assets/logos/referenzen.json").read_text(encoding="utf8"))
    gross = [l for l in logos if l["klasse"] == "g"]
    klein = [l for l in logos if l["klasse"] == "k"]
    logo_img = lambda l: f'<div><img src="assets/logos/ref-{l["id"]}.png" alt="{l["name"]}" width="{l["w"]}" height="{l["h"]}"></div>'
    spalten = 10 if len(klein) <= 40 else (11 if len(klein) <= 44 else 12)
    preis_chips = "".join(
        f'<span class="preis"><b>{n}</b>' + (f'<img src="assets/logos/ref-{k}.png" alt="">' if k else "") + "</span>" for n, k in PREISE)

    kante_titel = kunst_kante("titel", [(0, "#FF1F3D"), (.3, "#FF4FA3"), (.55, "#A855F7"), (.78, "#2F5BFF"), (1, "#7FD4FF")])
    kante_ende = kunst_kante("ende", [(0, "#A8E4FF"), (.5, "#7FD4FF"), (1, "#4FC3FF")])

    dreischritt = "".join(f'<p class="fragment"><span>{a}</span><span class="schimmer">{v}</span><span>{r}</span></p>' for a, v, r in DREISCHRITT)
    punkte = "".join(f'<div class="zs-punkt" style="left:{x}%;"><b>{n}</b><span>{z}</span></div>' for n, z, x in ZEITSTRAHL)

    folien = f'''
<!-- ============ 1: DECKBLATT ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  {kante_titel}
  <div class="slide" style="justify-content:center;">
    <div class="titel-duo">
      <img class="titel-logo" src="assets/logos/edge-logo-white.png" alt="EDGE Digital">
      <span class="mal">×</span>
      <img class="db-logo" src="assets/logos/ref-deutschebank.png" alt="Deutsche Bank" width="240" height="240">
    </div>
  </div>
</section>

<!-- ============ 2: COLLAGE ============ -->
<section class="f-pink" data-stimmung="pink">
  <img class="collage" src="assets/collage/collage.jpg" alt="EDGE unterwegs: Vorträge, Preise, Kunden, Team" width="2560" height="1440">
  <div class="collage-hoch"><div style="background-position:left center;"></div><div style="background-position:right center;"></div></div>
  <div class="collage-schleier"></div>
</section>

<!-- ============ 3: REFERENZEN ============ -->
<section class="f-lila" data-stimmung="lila">
  <div class="slide wand rollbar" data-prevent-swipe>
    <div class="logos gross">{"".join(logo_img(l) for l in gross)}</div>
    <hr class="trenner">
    <div class="logos klein" style="--spalten:{spalten};">{"".join(logo_img(l) for l in klein)}</div>
    <div class="preise"><span class="label">Preise &amp; Nominierungen</span><div class="preis-reihe">{preis_chips}</div></div>
  </div>
</section>

<!-- ============ 4: TEAM ============ -->
<section data-stimmung="neutral">
  <div class="slide team rollbar" data-prevent-swipe>
    {team_seite("service", "„KI &amp; Daten für Ihre Firma nutzen“", SERVICE_KOPF, SERVICE, SERVICE_PUNKTE)}
    <div class="mitte">
      {kopf_kreis("Emre", "Geschäftsführer", "emre.png", "gf", gross=True)}
    </div>
    {team_seite("software", "„KI in Ihrer Firma implementieren“", SOFTWARE_KOPF, SOFTWARE, SOFTWARE_PUNKTE)}
  </div>
</section>

<!-- ============ 5: BEDIENEN, KOMMUNIZIEREN, BEGEGNEN ============ -->
<section class="f-rot" data-stimmung="rot">
  <div class="slide">
    <div class="dreischritt">{dreischritt}</div>
  </div>
</section>

<!-- ============ 6: ZEITSTRAHL ============ -->
<section data-stimmung="neutral">
  <div class="zs-buehne" style="--linie:{ZEITSTRAHL_LINIE}%;">
    <img src="assets/illu/zeitstrahl.jpg" alt="Von Faustkeil und Feuer bis KI" width="1344" height="752">
    {punkte}
  </div>
  <div class="slide zeitstrahl">
    <h2 class="headline">Von der Steinzeit <span class="schimmer">bis heute.</span></h2>
  </div>
</section>

<!-- ============ 7: KURVE ============ -->
<section class="f-dblau" data-stimmung="dblau">
  <div class="slide">
    <h2 class="headline">Moore's Law gegen <span class="schimmer">KI.</span></h2>
    {kurve()}
  </div>
</section>

<!-- ============ 8: DIE FRAGE ============ -->
<section class="f-lila" data-stimmung="lila">
  {kunst_lila()}
  <div class="slide uebergang">
    <h2 class="hero frage">Was passiert, wenn Intelligenz nicht mehr nur <span class="schimmer">menschlich</span> ist?</h2>
  </div>
</section>

<!-- ============ 9: ENDE ============ -->
<section class="f-hblau" data-chrome="zahl" data-stimmung="hblau">
  {kante_ende}
  <div class="slide ende">
    <h2 class="hero gesetzt">Vielen <span class="schimmer">Dank.</span></h2>
    <div class="kontakt"><img src="assets/logos/edge-logo-white.png" alt="EDGE Digital"><p>{KONTAKT_MAIL}<br>{KONTAKT_TEL}</p></div>
  </div>
</section>
'''
    html = (ORDNER / "stamm.html").read_text(encoding="utf8")
    html = html.replace("</style>", EXTRA_STIL + "</style>", 1).replace("<!--FOLIEN-->", folien)
    html = html.replace("<title>EDGE Digital | Künstliche Intelligenz. Echte Wirkung.</title>", "<title>EDGE x Deutsche Bank</title>")
    (ORDNER / "index.html").write_text(html, encoding="utf8")
    print("index.html gebaut:", len(html) // 1024, "KB")


if __name__ == "__main__":
    bau()

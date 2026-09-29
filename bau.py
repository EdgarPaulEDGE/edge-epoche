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
# EDGE x Deutsche Bank: Inhalte aus Emres Vorlage (DB.pptx, 29.09.2026)
# ----------------------------------------------------------------------------

# (Beschriftung, Zeit, Mitte der Insel im Bild in Prozent der Breite)
ZEITSTRAHL = [('<i class="nur-quer">Faustkeil &amp; </i>Feuer', "ab 2,5 Mio. v. Chr.", 6.6), ("Schrift", "ca. 3.000 v. Chr.", 18.6),
              ("Buchdruck", "1450 n. Chr.", 30.6), ("Dampfmaschine", "ca. 1760–1830", 43.2), ("Computer", "ab 1940", 56.3),
              ("Smartphone", "ab 2007", 68.5), ("Avatare", "2024+", 80.3), ("KI", "heute", 92.7)]
ZEITSTRAHL_LINIE = 52.3  # Höhe der leuchtenden Linie im Bild, in Prozent

DREISCHRITT = [("Wir", "bedienten", "Technologie."), ("Wir", "kommunizierten", "mit Technologie."), ("Jetzt", "begegnen", "wir Technologie.")]

EHRENAEMTER = ["Vorstand für Innovation und Technologie im HanseBelt e.V.", "Rotarier", "Kaufmannschaft Lübeck", "Energiecluster Lübeck"]

# Icons im Lucide-Stil (24er Raster, nur Konturen)
ICON = {
    "name": '<rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="8" cy="12" r="2.2"/><path d="M5 17c.6-1.6 1.7-2.4 3-2.4s2.4.8 3 2.4M14 10h5M14 14h4"/>',
    "adresse": '<path d="M20 10c0 5-5.5 10.2-7.4 11.8a1 1 0 0 1-1.2 0C9.5 20.2 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    "telefon": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.9.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-9 5.7a2 2 0 0 1-2 0L2 7"/>',
    "nummer": '<path d="M4 9h16M4 15h16M10 3 8 21M16 3l-2 18"/>',
    "betrag": '<path d="M4 10h12M4 14h9M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.8 5.2-2"/>',
    "privat": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "person": '<circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/>',
    "antwort": '<path d="M21 12a8.5 8.5 0 0 1-12.6 7.4L3 21l1.6-5.4A8.5 8.5 0 1 1 21 12z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/>',
}
CHECKLISTE = [("name", "Name"), ("adresse", "Adresse"), ("telefon", "Telefonnummer"), ("mail", "Mailadresse"),
              ("nummer", "Nummern mit Personenbezug"), ("betrag", "Konkrete Beträge"), ("privat", "Private Details")]

# Umzugs-Collage wie in Emres Vorlage (Folie 9): Lage in Folienpixeln 1920x1080 und Zuschnitt (links, oben, rechts, unten)
# Reihenfolge = Stapelung, das Sofa liegt unten
UMZUG = [("start-1", 412, -382, 1097, 1462, (0, 0, 0, 0)),
         ("start-2", -1, 555, 412, 525, (0, .0459, 0, 0)),
         ("start-3", 1508, 625, 437, 456, (0, .0960, .0017, .1222)),
         ("start-4", -1, 0, 518, 656, (0, .2747, .2368, 0)),
         ("start-5", 1328, 0, 592, 684, (.0092, .1422, 0, 0))]


def umzug():
    teile = []
    for n, x, y, w, h, (l, o, r, u) in UMZUG:
        bw, bh = w / (1 - l - r), h / (1 - o - u)
        teile.append(f'<div class="stueck" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;">'
                     f'<img src="assets/fotos/{n}.jpg" alt="" style="left:{-l * bw:.0f}px;top:{-o * bh:.0f}px;width:{bw:.0f}px;height:{bh:.0f}px;"></div>')
    return f'<div class="umzug">{"".join(teile)}</div>'


TRIPTYCHON = [("damals-waschbrett", "heute-kleid"), ("damals-feuer", "heute-teller"), ("damals-rechnungen", "heute-handschlag")]

ADRESSE = "Marlesgrube 1, 23552 Lübeck"


def icon(k, klasse=""):
    return f'<svg class="icon {klasse}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'


def kurs():
    """Die Kurslinie des Deckblatts: kommt seitwärts rein, crasht, erholt sich und schießt im EDGE-Verlauf nach oben."""
    d = ("M0,430 C110,418 190,446 290,428 C350,418 378,432 408,520 C438,618 462,760 505,782 "
         "C548,802 572,650 622,606 C680,556 722,612 772,592 C852,560 900,420 962,300 C1012,200 1062,92 1160,-20")
    return f'''<svg class="kurs" viewBox="0 0 1160 900" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
  <defs>
    <linearGradient id="vl-kurs" x1="0" y1="0" x2="1160" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FF1F3D" stop-opacity="0"/><stop offset=".1" stop-color="#FF1F3D"/><stop offset=".38" stop-color="#FF4FA3"/><stop offset=".6" stop-color="#A855F7"/><stop offset=".8" stop-color="#2F5BFF"/><stop offset="1" stop-color="#7FD4FF"/>
    </linearGradient>
    <linearGradient id="vl-flaeche" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7C5CFF" stop-opacity=".30"/><stop offset="1" stop-color="#7C5CFF" stop-opacity="0"/></linearGradient>
  </defs>
  <path class="schein" pathLength="1" d="{d}" fill="none" stroke="url(#vl-kurs)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
  <path class="linie" pathLength="1" d="{d}" fill="none" stroke="url(#vl-kurs)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''


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
  <text class="kurven-name moore" x="{x1}" y="{py(3):.0f}" text-anchor="end">Moore's Law: alle 18 Monate doppelt</text>
</svg>'''


def blackbox():
    """Input, Black Box, Output. Der Würfel ist der Drahtwürfel aus der roten Phase, gefüllt mit Fragezeichen."""
    fragen = "".join(f'<text x="{x}" y="{y}" font-size="{s}" transform="rotate({r} {x} {y})">?</text>' for x, y, s, r in
                     [(-70, -40, 70, -12), (10, -70, 56, 8), (60, -10, 80, 14), (-20, 30, 90, -6), (-90, 60, 50, 10), (70, 80, 60, -10), (5, 110, 46, 4)])
    return f'''<svg class="bbox" viewBox="-230 -230 460 460" aria-hidden="true">
  <path d="{wuerfel(0, 0, 200)}" fill="rgba(193,93,230,.08)" stroke="#C77DFF" stroke-width="3" stroke-linejoin="round"/>
  <g class="fragen" fill="#F4F6FF" font-family="var(--font)" font-weight="700" text-anchor="middle">{fragen}</g>
</svg>'''


EXTRA_STIL = """
/* ---------- EDGE x Deutsche Bank: Zusatzstil ---------- */
/* Folie 1: nur schwarz, auch ohne Galaxie. So startet Emre die Kurslinie selbst. */
#kosmos, .stimmung, .vignette { transition: opacity 1.1s ease; }
body[data-stimmung="aus"] #kosmos, body[data-stimmung="aus"] .stimmung { opacity: 0 !important; }

/* Vollflächige Bilder und Schleier */
.voll { position: absolute; inset: 0; width: 1920px; height: var(--buehne-h); object-fit: cover; display: block; margin: 0 !important; max-width: none !important; max-height: none !important; }
.schleier-unten { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(3,3,9,.92) 0%, rgba(3,3,9,.55) 30%, rgba(3,3,9,0) 58%); }
.schleier-mitte { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(3,3,9,.82) 0%, rgba(3,3,9,.45) 32%, rgba(3,3,9,0) 55%); }
/* Holstentor: unten schwarz, nach oben auslaufend bis unter den Titel, dazu eine leichte Abdunklung fürs ganze Bild */
.schleier-holstentor { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(3,3,9,.96) 0%, rgba(3,3,9,.8) 22%, rgba(3,3,9,.5) 45%, rgba(3,3,9,.18) 68%, rgba(3,3,9,0) 72%), rgba(3,3,9,.28); }
body.hochkant .schleier-holstentor { background: linear-gradient(0deg, rgba(3,3,9,.95) 0%, rgba(3,3,9,.8) 30%, rgba(3,3,9,.3) 60%, rgba(3,3,9,.25) 100%); }
.schleier-oben { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(3,3,9,.78) 0%, rgba(3,3,9,.15) 34%, rgba(3,3,9,0) 55%, rgba(3,3,9,.72) 100%); }
.bild-quelle { position: absolute; right: 40px; bottom: 26px; font-size: 16px; color: rgba(244,246,255,.4); letter-spacing: .06em; }

/* Deckblatt: Logos oben links, Titel darunter, rechts die Kurslinie */
.titel-duo { display: flex; align-items: center; gap: 38px; }
.titel-duo .titel-logo { width: 360px; }
.titel-duo .mal { font-size: 54px; font-weight: 400; color: var(--w-45); line-height: 1; }
.titel-duo .db-logo { height: 118px; width: auto; display: block; margin: 0; }
.deckblatt { justify-content: space-between; padding-top: 110px; padding-bottom: 110px; }
.deckblatt .hero { font-size: 140px; position: relative; }
.deckblatt .unterzeile { font-size: 50px; font-weight: 600; margin: 22px 0 0; color: var(--w-70); position: relative; }
.kurs { position: absolute; left: 760px; top: calc(var(--extra) + 90px); width: 1120px; height: 870px; overflow: visible; filter: drop-shadow(0 0 16px rgba(168,85,247,.45)); }
.kurs .linie, .kurs .schein { stroke-dasharray: 1; stroke-dashoffset: 1; }
.kurs .schein { opacity: .28; }
.kurs .flaeche { opacity: 0; }
.reveal section.present .kurs .linie, .reveal section.present .kurs .schein { animation: zeichnen 3.6s .5s cubic-bezier(.55,.05,.35,1) forwards; }
.reveal section.present .kurs .flaeche { animation: auftauchen 1.2s 3.4s forwards; }
body.standbild .kurs .linie, body.standbild .kurs .schein { stroke-dashoffset: 0; }
body.standbild .kurs .flaeche { opacity: 1; }

/* Große Aussagen */
.slide.mittig { justify-content: center; align-items: center; text-align: center; }
.slide.unten { justify-content: flex-end; padding-bottom: 120px; }
.zitat { font-size: 96px; line-height: 1.12; font-weight: 700; letter-spacing: -.02em; margin: 0; max-width: 1560px; }
.quelle { margin-top: 40px; font-size: 30px; color: var(--w-45); letter-spacing: .04em; }

/* Emre */
.emre-foto { position: absolute; right: 0; top: 0; width: 1000px; height: var(--buehne-h); object-fit: cover; object-position: 60% 30%; margin: 0 !important; max-width: none !important; max-height: none !important;
  -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 34%); mask-image: linear-gradient(90deg, transparent 0, #000 34%); }
.slide.emre { justify-content: center; }
.slide.emre .headline { font-size: 104px; margin-bottom: 10px; }
.slide.emre .lead { max-width: 900px; }
.aemter { list-style: none; margin: 56px 0 0; padding: 0; }
.aemter li { font-size: 32px; line-height: 1.35; padding: 14px 0 14px 34px; position: relative; color: var(--weiss); border-top: 1px solid var(--hairline); max-width: 900px; white-space: nowrap; }
.aemter li::before { content: ""; position: absolute; left: 4px; top: 29px; width: 11px; height: 11px; border-radius: 50%; background: linear-gradient(135deg, #FF4FA3, #7FD4FF); }

/* Umzugs-Collage: auf 1080 gebaut und mit der Bühne skaliert, damit sie auch auf 16:10 randlos bleibt */
.umzug { position: absolute; left: 50%; top: 0; width: 1920px; height: 1080px; overflow: hidden; transform-origin: 50% 0; transform: translateX(-50%) scale(var(--buehne-skala, 1)); }
.umzug .stueck { position: absolute; overflow: hidden; }
.umzug .stueck img { position: absolute; display: block; margin: 0 !important; max-width: none !important; max-height: none !important; }
section > .band { display: none; }
body.hochkant .umzug { display: none; }
body.hochkant section > .band { display: grid; }

/* Fotobänder */
.band { position: absolute; left: 0; top: 0; width: 1920px; height: var(--buehne-h); display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
.band img { width: 100%; height: 100%; object-fit: cover; display: block; margin: 0 !important; max-width: none !important; max-height: none !important; }
.privat { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 22px; margin-top: 24px; flex: 1; min-height: 0; }
.reihe-fotos { display: flex; gap: 22px; justify-content: center; }
/* Ganze Fotos, nichts abgeschnitten: gleiche Höhe, Breite ergibt sich aus dem Bild */
.privat img { height: 392px; width: auto; border-radius: 6px; display: block; margin: 0 !important; max-width: none !important; max-height: none !important; }

/* Definition */
.definition { font-size: 58px; line-height: 1.3; font-weight: 600; margin: 34px 0 0; max-width: 1560px; color: var(--w-70); }

/* Dreischritt */
.dreischritt { display: grid; grid-template-columns: repeat(3, auto); justify-content: space-between; gap: 50px; margin-top: auto; margin-bottom: auto; }
.dreischritt p { margin: 0; font-size: 58px; line-height: 1.12; font-weight: 700; text-transform: uppercase; letter-spacing: -.015em; white-space: nowrap; }
.dreischritt p span { display: block; }

/* Zeitstrahl */
.zs-buehne { position: absolute; left: 150px; top: calc(150px + var(--extra)); width: 1620px; aspect-ratio: 1344 / 752; }
.zs-buehne img { --rand-x: linear-gradient(90deg, transparent 0, #000 7%, #000 93%, transparent 100%); --rand-y: linear-gradient(180deg, transparent 0, #000 22%, #000 80%, transparent 100%);
  -webkit-mask-image: var(--rand-x), var(--rand-y); -webkit-mask-composite: source-in; mask-image: var(--rand-x), var(--rand-y); mask-composite: intersect;
  position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; object-fit: cover; margin: 0 !important; max-width: none !important; max-height: none !important; }
.zs-punkt { position: absolute; top: calc(var(--linie) + 9%); transform: translateX(-50%); text-align: center; white-space: nowrap; }
.zs-punkt b { display: block; font-size: 21px; font-weight: 700; letter-spacing: .01em; text-transform: uppercase; }
.zs-punkt i { font-style: normal; }
.zs-punkt span { display: block; font-size: 19px; color: var(--w-45); margin-top: 6px; }
.slide.zeitstrahl .headline { position: relative; }

/* Kurve */
.kurve { width: 100%; height: auto; margin-top: 30px; overflow: visible; }
.kurve .jahre text { font-size: 24px; fill: rgba(244,246,255,.45); font-family: var(--font); }
.kurve .kurven-name { font-size: 30px; font-weight: 700; font-family: var(--font); opacity: 0; }
.kurve .kurven-name.ki { fill: #7FD4FF; }
.kurve .kurven-name.moore { fill: rgba(244,246,255,.7); }
.kurve .linie { stroke-dasharray: 1; stroke-dashoffset: 1; }
.reveal section.present .kurve .linie.moore { animation: zeichnen 2.4s .3s ease-out forwards; }
.reveal section.present .kurve .linie.ki { animation: zeichnen 1.6s 1.2s ease-in forwards; }
.reveal section.present .kurve .kurven-name.moore { animation: auftauchen .6s 2.5s forwards; }
.reveal section.present .kurve .kurven-name.ki { animation: auftauchen .6s 2.8s forwards; }
body.standbild .kurve .linie { stroke-dashoffset: 0; }
body.standbild .kurve .kurven-name { opacity: 1; }
@keyframes zeichnen { to { stroke-dashoffset: 0; } }
@keyframes auftauchen { to { opacity: 1; } }

/* Brücke */
.ufer { display: flex; justify-content: space-between; align-items: flex-end; flex: 1; padding-bottom: 40px; }
.ufer p { font-size: 46px; font-weight: 600; margin: 0; white-space: nowrap; text-shadow: 0 4px 30px rgba(3,3,9,.9); }
.schatten { text-shadow: 0 6px 40px rgba(3,3,9,.85), 0 2px 10px rgba(3,3,9,.6); }

/* Pizza: zwei Spalten, getrennt nur durch eine feine Linie */
.pizza { display: grid; grid-template-columns: 1fr 1px 1fr; gap: 70px; flex: 1; align-items: stretch; }
.pizza .trennlinie { background: linear-gradient(180deg, transparent, rgba(244,246,255,.25), transparent); }
.pizza > div:not(.trennlinie) { display: flex; flex-direction: column; align-items: center; text-align: center; }
.pizza .label { margin-bottom: 26px; }
.pizza .label.gut { color: #7FD4FF; }
.pizza .ansage { min-height: 170px; display: flex; align-items: center; justify-content: center; margin: 0; font-weight: 700; }
.pizza .ansage.kurz { font-size: 88px; }
.pizza .ansage.lang { font-size: 36px; line-height: 1.4; max-width: 780px; font-weight: 600; }
.pizza img { height: 400px; width: auto; display: block; margin: 20px 0 !important; }
.pizza .ergebnis { font-size: 32px; margin: 0; color: var(--w-45); }
.pizza .ergebnis.gut { color: #7FD4FF; font-weight: 600; }

/* Black Box */
.io { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 40px; flex: 1; }
.io-seite { display: flex; flex-direction: column; align-items: center; text-align: center; }
.io-seite .icon { width: 150px; height: 150px; color: var(--weiss); }
.io-seite b { font-size: 64px; font-weight: 700; letter-spacing: .02em; margin-top: 18px; }
.io-seite span { margin-top: 10px; font-size: 30px; color: var(--w-45); letter-spacing: .14em; text-transform: uppercase; }
.bbox { width: 520px; height: 520px; overflow: visible; filter: drop-shadow(0 0 24px rgba(193,93,230,.45)); }
.io-pfeil { position: relative; }
.io-erklaerung { text-align: center; font-size: 34px; line-height: 1.45; color: var(--w-70); margin: 0 auto; max-width: 1400px; }

/* Checkliste */
.verbote { display: grid; grid-template-columns: repeat(7, 1fr); gap: 26px; margin-top: 110px; }
.verbote div { display: flex; flex-direction: column; align-items: center; text-align: center; }
.verbote .icon { width: 120px; height: 120px; color: #FF5468; filter: drop-shadow(0 0 14px rgba(255,31,61,.45)); }
.verbote p { margin: 28px 0 0; font-size: 25px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; line-height: 1.3; }

/* Harvard x BCG */
.studie { display: flex; flex-direction: column; justify-content: center; flex: 1; }
.riesig { font-size: 300px; line-height: .95; font-weight: 700; letter-spacing: -.04em; margin: 16px 0 0; }
.riesig small { font-size: 72px; letter-spacing: -.01em; margin-left: 28px; color: var(--weiss); -webkit-text-fill-color: var(--weiss); }
.nebenzahlen { display: flex; gap: 90px; margin-top: 40px; font-size: 44px; font-weight: 600; color: var(--w-70); }
.nebenzahlen b { color: var(--weiss); }
.haelften { display: flex; gap: 90px; margin-top: 50px; font-size: 44px; font-weight: 600; }
.haelften b { color: #7FD4FF; }
.training { margin-top: 56px; font-size: 44px; font-weight: 700; }

/* Triptychon */
.trip { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: 1fr 1fr; gap: 22px 30px; flex: 1; min-height: 0; margin-top: 10px; }
.trip img { width: 100%; height: 100%; object-fit: cover; border-radius: 6px; display: block; margin: 0 !important; max-width: none !important; max-height: none !important; }
.trip .heute img { box-shadow: 0 0 0 1.5px rgba(168,85,247,.55), 0 0 44px rgba(47,91,255,.35), 0 0 80px rgba(255,79,163,.18); }
.trip > div { min-height: 0; position: relative; }
.trip .wann { position: absolute; left: 20px; top: 16px; font-size: 20px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: rgba(244,246,255,.85); text-shadow: 0 2px 12px rgba(0,0,0,.8); }
.bestimmung { margin: 34px 0 0; font-size: 72px; line-height: 1.1; font-weight: 700; text-transform: uppercase; letter-spacing: -.02em; text-align: center; }

/* Ende */
.ende-foto { position: absolute; right: 0; top: 0; width: 820px; height: var(--buehne-h); object-fit: cover; object-position: 50% 40%; margin: 0 !important; max-width: none !important; max-height: none !important;
  -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 30%); mask-image: linear-gradient(90deg, transparent 0, #000 30%); }
.slide.schluss { justify-content: center; }
.slide.schluss .hero { font-size: 96px; max-width: 1060px; }
.slide.schluss .kontakt { margin-top: 80px; display: flex; align-items: center; gap: 36px; }
.slide.schluss .kontakt img { width: 260px; height: auto; margin: 0; }
.slide.schluss .kontakt p { margin: 0; font-size: 28px; line-height: 1.5; color: var(--w-70); }
.slide.schluss .kontakt p b { color: var(--weiss); }

/* ---------- Hochkant (Handy) ---------- */
body.hochkant .titel-duo .titel-logo { width: 420px; }
body.hochkant .titel-duo .db-logo { height: 130px; }
body.hochkant .deckblatt .hero { font-size: 104px; }
body.hochkant .deckblatt .unterzeile { font-size: 50px; }
body.hochkant .kurs { left: -60px; top: 900px; width: 1200px; height: 900px; }
body.hochkant .zitat { font-size: 78px; }
body.hochkant .emre-foto { width: 1080px; height: 1000px; top: auto; bottom: 0; -webkit-mask-image: linear-gradient(180deg, transparent 0, #000 40%); mask-image: linear-gradient(180deg, transparent 0, #000 40%); }
body.hochkant .slide.emre { justify-content: flex-start; }
body.hochkant .slide.emre .headline { font-size: 84px; }
body.hochkant .aemter li { font-size: 34px; white-space: normal; }
body.hochkant .band { grid-template-columns: repeat(2, 1fr); grid-auto-rows: 1fr; }
body.hochkant .band img:last-child { grid-column: span 2; }
body.hochkant .reihe-fotos { flex-wrap: wrap; }
body.hochkant .privat img { height: 260px; }
body.hochkant .definition { font-size: 56px; }
body.hochkant .dreischritt { grid-template-columns: 1fr; gap: 90px; }
body.hochkant .dreischritt p { font-size: 70px; white-space: normal; }
body.hochkant .zs-buehne { width: 980px; left: 50px; top: 640px; }
body.hochkant .zs-punkt b { font-size: 26px; letter-spacing: 0; }
body.hochkant .zs-punkt span { display: none; }
body.hochkant .zs-punkt:nth-child(odd of .zs-punkt) { top: calc(var(--linie) - 22%); }
body.hochkant .nur-quer { display: none; }
body.hochkant .zeitstrahl .headline .schimmer { display: block; }
body.hochkant .ufer { flex-direction: column; align-items: flex-start; justify-content: flex-end; gap: 30px; }
body.hochkant .ufer p { font-size: 50px; white-space: normal; }
body.hochkant .pizza { grid-template-columns: 1fr; gap: 50px; }
body.hochkant .pizza .trennlinie { display: none; }
body.hochkant .pizza img { height: 300px; }
body.hochkant .io { grid-template-columns: 1fr; gap: 20px; }
body.hochkant .verbote { grid-template-columns: repeat(2, 1fr); gap: 60px 30px; margin-top: 70px; }
body.hochkant .riesig { font-size: 220px; }
body.hochkant .nebenzahlen, body.hochkant .haelften { flex-direction: column; gap: 16px; }
body.hochkant .trip { grid-template-columns: 1fr 1fr; grid-template-rows: none; grid-auto-rows: 330px; grid-auto-flow: column; grid-template-rows: repeat(3, 330px); }
body.hochkant .trip > div:nth-child(n+4) { grid-column: 2; }
body.hochkant .bestimmung { font-size: 64px; }
body.hochkant .ende-foto { width: 1080px; height: 900px; top: auto; bottom: 0; -webkit-mask-image: linear-gradient(180deg, transparent 0, #000 40%); mask-image: linear-gradient(180deg, transparent 0, #000 40%); }
body.hochkant .slide.schluss { justify-content: flex-start; }
body.hochkant .slide.schluss .hero { font-size: 84px; }
/* Im Hochformat dürfen die sonst einzeiligen Sätze umbrechen */
body.hochkant .zitat, body.hochkant .headline { white-space: normal !important; }
body.hochkant .zitat { font-size: 72px !important; }
body.hochkant .riesig { font-size: 190px; white-space: nowrap; }
body.hochkant .riesig small { display: block; margin: 10px 0 0; }
"""


def bau():
    logos = json.loads((ORDNER / "assets/logos/referenzen.json").read_text(encoding="utf8"))
    # Deutsche Bank sitzt im Publikum: ihr Logo gehört hier nicht auf die Referenzwand
    logos = [l for l in logos if l["id"] != "deutschebank"]
    # Die Buhck Gruppe rückt in die Lücke, die das Deutsche-Bank-Logo im großen Raster hinterlässt (rechts, dritte Reihe)
    gross = [l for l in logos if l["klasse"] == "g"] + [l for l in logos if l["id"] == "buhck"]
    klein = [l for l in logos if l["klasse"] == "k" and l["id"] != "buhck"]
    logo_img = lambda l: f'<div><img src="assets/logos/ref-{l["id"]}.png" alt="{l["name"]}" width="{l["w"]}" height="{l["h"]}"></div>'
    spalten = 10 if len(klein) <= 40 else (11 if len(klein) <= 44 else 12)
    preis_chips = "".join(
        f'<span class="preis"><b>{n}</b>' + (f'<img src="assets/logos/ref-{k}.png" alt="">' if k else "") + "</span>" for n, k in PREISE)

    dreischritt = "".join(f'<p class="fragment"><span>{a}</span><span class="schimmer">{v}</span><span>{r}</span></p>' for a, v, r in DREISCHRITT)
    punkte = "".join(f'<div class="zs-punkt" style="left:{x}%;"><b>{n}</b><span>{z}</span></div>' for n, z, x in ZEITSTRAHL)
    aemter = "".join(f"<li>{a}</li>" for a in EHRENAEMTER)
    band = "".join(f'<img src="assets/fotos/start-{i}.jpg" alt="" loading="lazy">' for i in range(1, 6))
    privat_bild = lambda i: f'<img src="assets/fotos/privat-{i}.jpg" alt="" loading="lazy">'
    # Kindheit, Studium, Trading oben; Familie und EDGE unten
    privat = f'<div class="reihe-fotos">{"".join(privat_bild(i) for i in (1, 4, 5))}</div><div class="reihe-fotos">{"".join(privat_bild(i) for i in (2, 3))}</div>'
    verbote = "".join(f'<div>{icon(k)}<p>{t}</p></div>' for k, t in CHECKLISTE)
    trip_damals = "".join(f'<div><img src="assets/illu/{d}.jpg" alt="" loading="lazy"><span class="wann">Damals</span></div>' for d, _ in TRIPTYCHON)
    trip_heute = "".join(f'<div class="heute fragment" data-fragment-index="1"><img src="assets/illu/{h}.jpg" alt="" loading="lazy"><span class="wann">Heute</span></div>' for _, h in TRIPTYCHON)
    kante_ende = kunst_kante("ende", [(0, "#A8E4FF"), (.5, "#7FD4FF"), (1, "#4FC3FF")])

    folien = f'''
<!-- ============ 1: SCHWARZ. Emre startet von hier die Kurslinie ============ -->
<section data-chrome="aus" data-stimmung="aus">
  <div class="slide"></div>
</section>

<!-- ============ 2: DECKBLATT · BUY THE DIP ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  {kurs()}
  <div class="slide deckblatt">
    <div class="titel-duo">
      <img class="titel-logo" src="assets/logos/edge-logo-white.png" alt="EDGE Digital">
      <span class="mal">×</span>
      <img class="db-logo" src="assets/logos/ref-deutschebank.png" alt="Deutsche Bank" width="240" height="240">
    </div>
    <div>
      <h1 class="hero">Buy the <span class="schimmer">Dip!</span></h1>
      <p class="unterzeile">Warum jetzt in KI einsteigen?</p>
    </div>
  </div>
</section>

<!-- ============ 3: BANKFILIALE DER 90ER ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  <img class="voll" src="assets/illu/bank-90er.jpg" alt="Bankfiliale in den 90ern mit Röhrenmonitor und Fax">
  <div class="schleier-unten"></div>
  <div class="slide unten">
    <p class="zitat" style="text-align:left;font-size:88px;white-space:nowrap;">„Das Internet? Das geht wieder weg.“</p>
    <span class="bild-quelle">Bild mit KI erstellt</span>
  </div>
</section>

<!-- ============ 4: HEUTE ÜBER KI ============ -->
<section class="f-rot" data-stimmung="rot">
  {kunst_rot()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt" style="font-size:120px;">„Heute sagen viele<br>dasselbe <span class="schimmer">über KI.</span>“</h2>
  </div>
</section>

<!-- ============ 5: ABER VORAB ============ -->
<section data-stimmung="neutral">
  <div class="slide uebergang">
    <p class="label" style="position:relative;font-size:26px;margin-bottom:26px;">Aber vorab</p>
    <h2 class="hero gesetzt" style="font-size:112px;">Wer bin ich? Und warum<br>spreche ich <span class="schimmer">darüber?</span></h2>
  </div>
</section>

<!-- ============ 6: EMRE ============ -->
<section data-stimmung="neutral">
  <img class="emre-foto" src="assets/fotos/emre.jpg" alt="Emre Erdogan">
  <div class="slide emre">
    <h2 class="headline">Emre <span class="schimmer">Erdogan</span></h2>
    <p class="lead">Gründer und Geschäftsführer der Firma EDGE Digital</p>
    <ul class="aemter">{aemter}</ul>
  </div>
</section>

<!-- ============ 7: COLLAGE ============ -->
<section class="f-pink" data-stimmung="pink">
  <img class="collage" src="assets/collage/collage.jpg" alt="EDGE unterwegs: Vorträge, Preise, Kunden, Team" width="2560" height="1440">
  <div class="collage-hoch"><div style="background-position:left center;"></div><div style="background-position:right center;"></div></div>
  <div class="collage-schleier"></div>
</section>

<!-- ============ 8: REFERENZEN (ohne Deutsche Bank) ============ -->
<section class="f-lila" data-stimmung="lila">
  <div class="slide wand rollbar" data-prevent-swipe>
    <div class="logos gross">{"".join(logo_img(l) for l in gross)}</div>
    <hr class="trenner">
    <div class="logos klein" style="--spalten:{spalten};">{"".join(logo_img(l) for l in klein)}</div>
    <div class="preise"><span class="label">Preise &amp; Nominierungen</span><div class="preis-reihe">{preis_chips}</div></div>
  </div>
</section>

<!-- ============ 9: DIE ANFÄNGE ============ -->
<section data-stimmung="neutral">
  {umzug()}
  <div class="band">{band}</div>
</section>

<!-- ============ 10: EHRLICH ============ -->
<section data-stimmung="neutral">
  <div class="slide" style="padding-top:118px;padding-bottom:44px;">
    <h2 class="headline" style="font-size:68px;white-space:nowrap;margin-bottom:0;">Wir sind ehrlich zueinander… <span class="schimmer">ich fange an.</span></h2>
    <div class="privat">{privat}</div>
  </div>
</section>

<!-- ============ 11: WAS IST KI? ============ -->
<section class="f-dblau" data-stimmung="dblau">
  {kunst_dunkelblau()}
  <div class="slide uebergang">
    <h2 class="hero gesetzt">Was ist <span class="schimmer">KI?</span></h2>
  </div>
</section>

<!-- ============ 12: DEFINITION ============ -->
<section class="f-dblau" data-stimmung="dblau">
  <div class="slide" style="justify-content:center;">
    <h2 class="headline" style="font-size:104px;">Künstliche <span class="schimmer">Intelligenz</span></h2>
    <p class="definition">beschreibt Systeme, die menschliche Denkprozesse wie Lernen, Entscheiden oder Problemlösen automatisiert nachahmen können.</p>
  </div>
</section>

<!-- ============ 13: ZEITSTRAHL ============ -->
<section data-stimmung="neutral">
  <div class="zs-buehne" style="--linie:{ZEITSTRAHL_LINIE}%;">
    <img src="assets/illu/zeitstrahl.jpg" alt="Von Faustkeil und Feuer bis KI" width="1344" height="752">
    {punkte}
  </div>
  <div class="slide zeitstrahl">
    <h2 class="headline">Technologie im <span class="schimmer">Wandel.</span></h2>
  </div>
</section>

<!-- ============ 14: KURVE ============ -->
<section class="f-dblau" data-stimmung="dblau">
  <div class="slide">
    <h2 class="headline">Moore's Law gegen <span class="schimmer">KI.</span></h2>
    {kurve()}
  </div>
</section>

<!-- ============ 15: BEDIENEN, KOMMUNIZIEREN, BEGEGNEN ============ -->
<section class="f-rot" data-stimmung="rot">
  <div class="slide">
    <div class="dreischritt">{dreischritt}</div>
  </div>
</section>

<!-- ============ 16: DIE BRÜCKE ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  <img class="voll" src="assets/robo/bruecke.jpg" alt="">
  <div class="schleier-oben"></div>
  <div class="slide">
    <h2 class="hero schatten" style="font-size:118px;text-align:center;">Die Brücke.</h2>
    <div class="ufer"><p>Unsere Leute nutzen sie nicht.</p><p>Unsere Leute nutzen sie.</p></div>
    <span class="bild-quelle">Bild mit KI erstellt</span>
  </div>
</section>

<!-- ============ 17: WIR FRAGEN SCHLECHT ============ -->
<section data-chrome="aus" data-stimmung="neutral">
  <img class="voll" src="assets/robo/holstentor.jpg" alt="">
  <div class="schleier-holstentor"></div>
  <div class="slide mittig" style="justify-content:flex-start;padding-top:96px;">
    <h2 class="hero schatten" style="font-size:96px;margin-bottom:14px;">Die KI liefert nicht schlecht.</h2>
    <p class="hero schimmer" style="font-size:126px;margin:0;filter:drop-shadow(0 4px 24px rgba(3,3,9,.7));">Wir fragen schlecht.</p>
    <span class="bild-quelle">Bild mit KI erstellt</span>
  </div>
</section>

<!-- ============ 18: PIZZA ============ -->
<section data-stimmung="neutral">
  <div class="slide">
    <div class="pizza">
      <div>
        <p class="label">Ihr sagt</p>
        <p class="ansage kurz">„Pizza.“</p>
        <img src="assets/robo/pizza-schlecht.png" alt="">
        <p class="ergebnis">Ihr bekommt irgendwas.</p>
      </div>
      <div class="trennlinie"></div>
      <div>
        <p class="label gut">Oder ihr sagt</p>
        <p class="ansage lang">„Eine Salami, 32er, dünner Boden, extra Käse, in einer halben Stunde, Marlesgrube&nbsp;1.“</p>
        <img src="assets/robo/pizza-gut.png" alt="">
        <p class="ergebnis gut">Ihr bekommt, was ihr wolltet.</p>
      </div>
    </div>
  </div>
</section>

<!-- ============ 19: BLACK BOX ============ -->
<section class="f-lila" data-stimmung="lila">
  <div class="slide">
    <div class="io">
      <div class="io-seite">{icon("person")}<b>Input</b><span>Anfrage</span></div>
      {blackbox()}
      <div class="io-seite">{icon("antwort")}<b>Output</b><span>Antwort</span></div>
    </div>
    <p class="io-erklaerung">Ein System ist eine Black Box, wenn man nur Input und Output kennt,<br>aber den inneren Mechanismus nicht nachvollziehen kann.</p>
  </div>
</section>

<!-- ============ 20: CHECKLISTE ============ -->
<section class="f-rot" data-stimmung="rot">
  <div class="slide" style="justify-content:center;">
    <h2 class="headline" style="text-align:center;font-size:96px;">Was darf nie in die <span class="schimmer">KI?</span></h2>
    <div class="verbote">{verbote}</div>
  </div>
</section>

<!-- ============ 21: HARVARD x BCG ============ -->
<section class="f-dblau" data-stimmung="dblau">
  <div class="slide">
    <div class="studie">
      <p class="label" style="font-size:26px;">Harvard × BCG · 758 Berater · mit KI vs. ohne</p>
      <p class="riesig schimmer">+40 %<small>Qualität</small></p>
      <div class="nebenzahlen"><span><b>25 %</b> schneller</span><span><b>12 %</b> mehr geschafft</span></div>
      <div class="haelften fragment"><span>Schwächere Hälfte: <b>+43 %</b></span><span>Stärkere Hälfte: <b>+17 %</b></span></div>
      <p class="training fragment">Mit Training: noch besser. <span class="schimmer">Genau das bekommt ihr heute.</span></p>
    </div>
  </div>
</section>

<!-- ============ 22: NORBERT WIENER ============ -->
<section class="f-lila" data-stimmung="lila">
  <div class="slide mittig">
    <p class="zitat">„Wir formen unsere Werkzeuge, und danach <span class="schimmer">formen sie uns.</span>“</p>
    <p class="quelle">Norbert Wiener, Vater der Kybernetik</p>
  </div>
</section>

<!-- ============ 23: HÄNDE · DAMALS UND HEUTE ============ -->
<section data-stimmung="neutral">
  <div class="slide" style="padding-top:110px;padding-bottom:70px;">
    <div class="trip">{trip_damals}{trip_heute}</div>
    <p class="bestimmung fragment" data-fragment-index="1">Unsere Bestimmung ist <span class="schimmer">größer.</span></p>
  </div>
</section>

<!-- ============ 24: ENDE ============ -->
<section class="f-hblau" data-chrome="zahl" data-stimmung="hblau">
  <img class="ende-foto" src="assets/fotos/team-db.jpg" alt="Das EDGE Team">
  <div class="slide schluss">
    <p class="label" style="font-size:26px;margin-bottom:24px;">Und jetzt…</p>
    <h2 class="hero gesetzt">Einfach nur noch ausprobieren, <span class="schimmer" style="white-space:nowrap;">ohne Stop-Loss.</span></h2>
    <div class="kontakt"><img src="assets/logos/edge-logo-white.png" alt="EDGE Digital"><p><b>Künstliche Intelligenz. Echte Wirkung.</b><br>{ADRESSE}</p></div>
  </div>
</section>
'''
    html = (ORDNER / "stamm.html").read_text(encoding="utf8")
    html = html.replace("</style>", EXTRA_STIL + "</style>", 1).replace("<!--FOLIEN-->", folien)
    html = html.replace("<title>EDGE Digital | Künstliche Intelligenz. Echte Wirkung.</title>", "<title>EDGE x Deutsche Bank · Buy the Dip!</title>")
    (ORDNER / "index.html").write_text(html, encoding="utf8")
    print("index.html gebaut:", len(html) // 1024, "KB,", html.count("<section"), "Folien")


if __name__ == "__main__":
    bau()

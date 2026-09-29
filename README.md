# EDGE x Deutsche Bank

Reveal.js Deck, 1920 x 1080, Stamm aus der EDGE Unternehmenspräsentation (bereit.edge-digital.ai):
Raumschwarz, Galaxie, Avenir Next, Schimmer Verlauf. Inhalt: EDGE Vorstellung plus Remix aus dem Rotary-Vortrag.

## Live

**https://epoche.edge-digital.ai/**
GitHub Pages aus `main`, Repo `EdgarPaulEDGE/edge-epoche`. DNS: CNAME `epoche` auf `edgarpauledge.github.io` bei Wix.

## Ändern

Folien und Texte stehen in `bau.py`, der Grundstil in `stamm.html`. Nie `index.html` direkt ändern, danach immer:

```bash
python3 bau.py
```

Lokal ansehen: `python3 -m http.server 8793`, dann http://localhost:8793. `?nofrag` für Standbilder.
Bilder in `assets/illu/` entstehen mit Higgsfield (Zeitstrahl: gpt_image_2_5, auf 4K hochskaliert).

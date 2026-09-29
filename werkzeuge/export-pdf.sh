#!/bin/sh
# Baut "EDGE Digital Unternehmenspräsentation.pdf" im Projektordner. Aufruf: sh werkzeuge/export-pdf.sh
cd "$(dirname "$0")/.." || exit 1
TMP="$(mktemp -d)"; python3 bau.py
python3 -m http.server 8794 >/dev/null 2>&1 & SRV=$!; sleep 1
node werkzeuge/export-pdf.mjs "$TMP"; kill $SRV
python3 - "$TMP" <<'PY'
import sys, glob
from PIL import Image
seiten = [Image.open(f).convert("RGB") for f in sorted(glob.glob(sys.argv[1] + "/s-*.png"))]
seiten[0].save("EDGE Digital Unternehmenspräsentation.pdf", save_all=True, append_images=seiten[1:], resolution=288, quality=90)
print("PDF geschrieben:", len(seiten), "Seiten")
PY
rm -rf "$TMP"

#!/usr/bin/env python3
"""Baut index.html aus quelle.html: setzt Lucide-Icons (icons/) und BMAD-Icons
(bmad-icons.json) ein und schreibt den MIT-Hinweis von BMAD an den Anfang.

    python3 bauen.py
"""
import json
import pathlib
import re
import sys

HIER = pathlib.Path(__file__).resolve().parent


def innen(svg: str) -> str:
    elemente = re.findall(r"<(?:path|circle|rect|line|polyline|polygon|ellipse)\b.*?/>", svg, re.S)
    return "".join(re.sub(r"\s+", " ", e) for e in elemente)


def main() -> int:
    quelle = (HIER / "quelle.html").read_text(encoding="utf-8")
    lucide = {p.stem: innen(p.read_text(encoding="utf-8")) for p in sorted((HIER / "icons").glob("*.svg"))}
    bmad = json.loads((HIER / "bmad-icons.json").read_text(encoding="utf-8"))

    benutzt = set(re.findall(r'(?:\bi|icon|data-icon)[:=]"([a-z0-9-]+)"', quelle)) | set(re.findall(r'(?:svgI|ico)\("([a-z0-9-]+)"', quelle)) | {"sun", "moon"}
    fehlt = sorted(n for n in benutzt if n not in lucide)
    if fehlt:
        sys.exit("Icons fehlen in icons/: " + ", ".join(fehlt))

    lizenz = (HIER / "LICENSE-BMAD.txt").read_text(encoding="utf-8").replace("--", "- -")
    seite = quelle.replace("/*__LUCIDE__*/null", json.dumps(lucide, ensure_ascii=False, separators=(",", ":")))
    seite = seite.replace("/*__BMAD__*/null", json.dumps(bmad, ensure_ascii=False, separators=(",", ":")))
    if "__LUCIDE__" in seite or "__BMAD__" in seite:
        sys.exit("Platzhalter nicht ersetzt")
    seite = seite.replace("<!doctype html>\n", "<!doctype html>\n<!-- Erzeugt aus quelle.html mit bauen.py.\n"
                          "Brainstorming-Teil und Technik-Icons nach BMad Method, bmad-toolbox, skills/bmad-brainstorming:\n"
                          + lizenz + "-->\n", 1)
    (HIER / "index.html").write_text(seite, encoding="utf-8")
    print(f"index.html: {len(seite)} Bytes, {len(lucide)} Lucide-Icons, {len(bmad)} BMAD-Icons")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

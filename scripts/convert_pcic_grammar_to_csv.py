#!/usr/bin/env python3
"""
Convert grammar JSON from https://github.com/pollow/spanish-pcic-json
into the confirmed CSV schema for dele-plan-curricular.

Usage:
  python convert_pcic_grammar_to_csv.py path/to/a1.json ...
  # or download first then run
"""

import json
import csv
import sys
from pathlib import Path

SCHEMA = [
    "id", "level", "component", "chapter", "section",
    "descriptor", "exponent", "example", "notes",
    "source_url", "chinese", "anki_ready"
]

def convert_item(item):
    examples = [e.replace("\n", " ").strip() for e in item.get("examples", []) if e and e.strip()]
    exponent = "; ".join(examples) if examples else ""
    topic = (item.get("topic") or "").strip()
    desc = (item.get("description") or "").strip()
    if topic and desc and topic not in desc:
        descriptor = f"{topic}: {desc}"
    else:
        descriptor = desc or topic
    notes = "; ".join(item.get("regional_variants") or [])
    return {
        "id": item.get("id", ""),
        "level": item.get("level", ""),
        "component": "Gramática",
        "chapter": item.get("category", ""),
        "section": item.get("subcategory", ""),
        "descriptor": descriptor,
        "exponent": exponent,
        "example": "",
        "notes": notes,
        "source_url": "https://github.com/pollow/spanish-pcic-json",
        "chinese": "",
        "anki_ready": "yes" if exponent else "no",
    }

def main():
    files = sys.argv[1:] or list(Path(".").glob("*.json"))
    all_rows = []
    for fp in files:
        data = json.loads(Path(fp).read_text(encoding="utf-8"))
        all_rows.extend(convert_item(item) for item in data)
    out = Path("output/gramatica.csv")
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SCHEMA)
        w.writeheader()
        w.writerows(all_rows)
    print(f"Wrote {len(all_rows)} rows to {out}")

if __name__ == "__main__":
    main()

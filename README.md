# DELE Plan Curricular Scraper

Scraper for the Instituto Cervantes *Plan curricular del Instituto Cervantes. Niveles de referencia para el español* (CVC electronic edition).

## Goals
- Crawl **all** components of the Plan Curricular
- Produce clean, fine-grained CSV files suitable for Anki and Cloudflare Pages
- Chinese translations to be added later via batch AI (column left empty)

## CSV Schema (confirmed)

| Field | Description |
|-------|-------------|
| id | Unique identifier |
| level | A1 / A2 / B1 / B2 / C1 / C2 |
| component | Funciones, Gramática, Nociones generales, Nociones específicas, etc. |
| chapter | Main section |
| section | Subsection |
| descriptor | Function / grammar point / notion description |
| exponent | Spanish expression / collocation |
| example | Full example sentence (if available) |
| notes | Original notes from source |
| source_url | Source page URL |
| chinese | Chinese translation (empty initially, fill later) |
| anki_ready | yes/no |

## Current Data

### Gramática (done)
- Source: [pollow/spanish-pcic-json](https://github.com/pollow/spanish-pcic-json) (2523 structured grammar points, A1–C2)
- Conversion script: `scripts/convert_pcic_grammar_to_csv.py`
- Output: `output/gramatica.csv` (or per-level CSVs)

CVC site is currently under maintenance. Grammar data is already available in machine-readable form from the above repo.

## Structure
- `scraper/` — Python crawler (skeleton started)
- `scripts/` — Conversion utilities
- `output/` — Generated CSVs
- `site/` — Cloudflare Pages source (later)

Source: https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular

## Next steps
1. Extend parser for Funciones + Nociones (see notes on pollow parse.mjs)
2. Generate remaining CSVs when CVC is back or via alternative sources
3. Build Cloudflare Pages viewer + Anki export

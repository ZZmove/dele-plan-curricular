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

## Structure
- `scraper/` — Python crawler (skeleton started)
- `output/` — Generated CSVs (to be added)
- `site/` — Cloudflare Pages source (later)

Source: https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular

## Next steps
1. Implement full crawler for all inventories (Funciones, Gramática, Nociones, etc.)
2. Generate CSVs
3. Build Cloudflare Pages viewer + Anki export

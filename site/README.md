# Cloudflare Pages site

Static site that reads the CSV(s) in `/output/` and provides:
- Filtering by level and component
- Search
- Anki TSV export of filtered results

Deploy: connect this repo to Cloudflare Pages, set build output to `site/` (or root if using `_redirects`).

Currently a skeleton. Full CSV loading to be wired once data is in place.

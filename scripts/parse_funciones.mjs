#!/usr/bin/env node
/**
 * Skeleton parser for PCIC Funciones inventory.
 *
 * Adapted from pollow/spanish-pcic-json parse.mjs.
 * Structure is similar (h2/h3 + tables with level columns + nested lists),
 * but needs adjustment once raw HTML from CVC is available.
 *
 * Expected output: funciones/*.json or direct CSV matching our schema.
 */

import { readFileSync, writeFileSync, mkdirSync } from "fs";
import * as cheerio from "cheerio";

// TODO: fill with actual file paths when CVC is back
const FILES = [
  // { path: "raw/funciones_a1-a2.htm", levels: ["A1", "A2"] },
  // { path: "raw/funciones_b1-b2.htm", levels: ["B1", "B2"] },
  // { path: "raw/funciones_c1-c2.htm", levels: ["C1", "C2"] },
];

function parseFuncionesFile(htmlPath, levels) {
  const html = readFileSync(htmlPath, "utf-8");
  const $ = cheerio.load(html);
  const results = { [levels[0]]: [], [levels[1]]: [] };

  // TODO: adapt selectors based on actual Funciones page structure
  // Typical pattern: h2 (main function category) -> tables with two tds
  $("h2").each((_, h2) => {
    const chapter = $(h2).text().trim();
    // Find following tables until next h2
    // Extract descriptor, exponents (usually in <em> or bold), examples
    // Map to our schema fields
  });

  return results;
}

// Placeholder main
console.log("Funciones parser skeleton. Waiting for CVC HTML to implement selectors.");
console.log("Reuse the grammar parser logic: walk headings + tables + lists, extract <em> as exponents.");

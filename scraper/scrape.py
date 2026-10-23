#!/usr/bin/env python3
"""
Scraper skeleton for Cervantes Plan Curricular.
TODO: Implement full crawling of all components.
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path

BASE_URL = "https://cvc.cervantes.es"
INDEX_URL = "https://cvc.cervantes.es/Ensenanza/biblioteca_ele/plan_curricular/indice.htm"

def main():
    print("Scraper skeleton — implement parsers for each component.")
    # Rate limit
    time.sleep(1)

if __name__ == "__main__":
    main()

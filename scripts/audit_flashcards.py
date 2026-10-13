import sqlite3
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('data/acupuncture.db')
c = conn.cursor()
c.execute('SELECT id, category, title, front, back, variations, consensus FROM flashcards ORDER BY id')
cards = c.fetchall()

print(f"Total flashcards in DB: {len(cards)}")

anomalies = []
for cid, cat, title, front, back, var, cons in cards:
    # Check for double-nested titles
    if re.search(r'\([A-Z]+\s*\([^)]+\)', title):
        anomalies.append((cid, title, "DOUBLE_NESTED_TITLE"))
        
    # Check for OCR typos
    for typo in [r'\bth e\b', r'\binform of\b', r'\b1 fun\b', r'\b2 fun\b', r'\b4 fun\b']:
        if re.search(typo, back, re.IGNORECASE) or re.search(typo, front, re.IGNORECASE) or re.search(typo, title, re.IGNORECASE):
            anomalies.append((cid, title, f"TYPO: {typo}"))

print(f"Found {len(anomalies)} anomalies in flashcards.")
for a in anomalies:
    print(a)

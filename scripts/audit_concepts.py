import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from modules.concepts import CONCEPTS_DATA

print(f"Total concepts: {len(CONCEPTS_DATA)}")

for c in CONCEPTS_DATA:
    # Check all string fields
    text = " ".join([
        c.get('title', ''),
        c.get('tagline', ''),
        c.get('summary', ''),
        c.get('mnemonic', ''),
        " ".join(c.get('principles', [])),
        " ".join(" ".join(row) for row in c.get('table_rows', [])),
        " ".join(c.get('board_traps', [])),
        " ".join(c.get('clinical_points', []))
    ])
    
    # Check for OCR typos
    for typo in [r'\bth e\b', r'\binform of\b', r'\b1 fun\b', r'\b2 fun\b', r'\b4 fun\b', r'\bunconsciousness\b']:
        if re.search(typo, text, re.IGNORECASE):
            print(f"Found typo {typo} in concept {c['id']}")

print("Concepts text scan complete.")

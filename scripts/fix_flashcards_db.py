import sqlite3
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Update SQLite DB directly
db_path = BASE_DIR / "data" / "acupuncture.db"
conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

# Fix double-nested titles
cursor.execute("UPDATE flashcards SET title = 'EX-UE7 (Yaotongxue / 腰痛穴)' WHERE id = 647")
cursor.execute("UPDATE flashcards SET title = 'EX-LE2 (Heding / 鹤顶)' WHERE id = 651")

# Fix OCR typos across all cards
cursor.execute("SELECT id, title, front, back, variations, consensus FROM flashcards")
rows = cursor.fetchall()

fixed_count = 0
for cid, title, front, back, var, cons in rows:
    new_title = re.sub(r'\bth e\b', 'the', title, flags=re.IGNORECASE)
    new_front = re.sub(r'\bth e\b', 'the', front, flags=re.IGNORECASE)
    new_back = re.sub(r'\bth e\b', 'the', back, flags=re.IGNORECASE)
    new_var = re.sub(r'\bth e\b', 'the', var, flags=re.IGNORECASE) if var else var
    new_cons = re.sub(r'\bth e\b', 'the', cons, flags=re.IGNORECASE) if cons else cons
    
    # Fix double-nested patterns in text
    new_back = re.sub(r'\(([A-Z0-9]+)\s*\(([^)]+)\)\s*/\s*([^)]+)\)', r'(\1 (\2 / \3))', new_back)
    
    if (new_title != title or new_front != front or new_back != back or new_var != var or new_cons != cons):
        cursor.execute("""
            UPDATE flashcards
            SET title = ?, front = ?, back = ?, variations = ?, consensus = ?
            WHERE id = ?
        """, (new_title, new_front, new_back, new_var, new_cons, cid))
        fixed_count += 1

conn.commit()
conn.close()
print(f"Successfully fixed {fixed_count} cards in SQLite database.")

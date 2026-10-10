# -*- coding: utf-8 -*-
"""Insert Bina Review Course expansion flashcards into data/acupuncture.db.
"""

import sys
import sqlite3
import json
from pathlib import Path

# Ensure UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "scripts"))

from cards_bina_expansion import CARDS_BINA
from modules.tcm_points import format_point_bilingual

DB_PATH = BASE_DIR / "data" / "acupuncture.db"


def insert_cards():
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM flashcards")
    before_count = cursor.fetchone()[0]
    print(f"Cards in database before insertion: {before_count}")

    cursor.execute("SELECT title FROM flashcards")
    existing_titles = set(r[0] for r in cursor.fetchall())

    inserted_count = 0
    skipped_count = 0

    for card in CARDS_BINA:
        raw_title = card["title"]
        bilingual_title = format_point_bilingual(raw_title)

        if raw_title in existing_titles or bilingual_title in existing_titles:
            print(f"  [SKIP] '{raw_title}' already exists.")
            skipped_count += 1
            continue

        bilingual_front = format_point_bilingual(card["front"])
        bilingual_back = format_point_bilingual(card["back"])
        bilingual_consensus = format_point_bilingual(card.get("consensus", ""))
        bilingual_variations = format_point_bilingual(card.get("variations", ""))
        sources_json = card.get("sources", '["TCM Review Seminars"]')
        importance = card.get("importance_level", 1)

        cursor.execute("""
        INSERT INTO flashcards (
            category, title, front, back, consensus, variations, sources,
            mastery_level, review_count, importance_level
        ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
        """, (
            card["category"],
            bilingual_title,
            bilingual_front,
            bilingual_back,
            bilingual_consensus,
            bilingual_variations,
            sources_json,
            importance
        ))
        inserted_count += 1
        print(f"  [INSERTED] ({card['category']}) {bilingual_title}")

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM flashcards")
    after_count = cursor.fetchone()[0]
    print(f"\nInsertion Complete: {inserted_count} inserted, {skipped_count} skipped.")
    print(f"Total cards now in database: {after_count}")

    cursor.execute("SELECT category, COUNT(*) FROM flashcards GROUP BY category ORDER BY category")
    print("\nBreakdown by Category:")
    for cat, count in cursor.fetchall():
        print(f"  • {cat}: {count} cards")

    conn.close()


if __name__ == "__main__":
    insert_cards()

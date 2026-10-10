"""Script to insert the 100 expansion cards into data/acupuncture.db safely.
"""

import sys
import sqlite3
import json
from pathlib import Path

# Ensure UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"d:\TCM\acupuncture_app")
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "scripts"))

from cards_expansion_100 import CARDS_100
from modules.tcm_points import format_point_bilingual

DB_PATH = BASE_DIR / "data" / "acupuncture.db"


def insert_cards():
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Check current card count
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    before_count = cursor.fetchone()[0]
    print(f"Cards in database before insertion: {before_count}")

    # Get existing titles to prevent duplication
    cursor.execute("SELECT title FROM flashcards")
    existing_titles = set(r[0] for r in cursor.fetchall())

    inserted_count = 0
    skipped_count = 0

    for card in CARDS_100:
        raw_title = card["title"]
        bilingual_title = format_point_bilingual(raw_title)

        # Check if already present
        if raw_title in existing_titles or bilingual_title in existing_titles:
            print(f"  [SKIP] '{raw_title}' already exists.")
            skipped_count += 1
            continue

        bilingual_front = format_point_bilingual(card["front"])
        bilingual_back = format_point_bilingual(card["back"])
        bilingual_consensus = format_point_bilingual(card.get("consensus", ""))
        bilingual_variations = format_point_bilingual(card.get("variations", ""))
        sources_json = card.get("sources", '["Textbook Synthesis"]')
        importance = card.get("importance_level", 2)

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

    conn.commit()

    # Check new total
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    after_count = cursor.fetchone()[0]
    print(f"\nInsertion complete!")
    print(f"  Newly inserted: {inserted_count} cards")
    print(f"  Skipped (duplicates): {skipped_count} cards")
    print(f"  Total cards in database: {after_count} cards")

    # Category breakdown
    print("\n--- Summary by Category ---")
    cursor.execute("SELECT category, COUNT(*) FROM flashcards GROUP BY category ORDER BY category")
    for cat, count in cursor.fetchall():
        print(f"  • {cat}: {count} cards")

    # Tier breakdown
    print("\n--- Summary by Exam Importance Tier ---")
    cursor.execute("SELECT importance_level, COUNT(*) FROM flashcards GROUP BY importance_level ORDER BY importance_level")
    tier_labels = {1: "🔥 Tier 1: High Yield (Must-Know)", 2: "⭐ Tier 2: Core Clinical", 3: "💡 Tier 3: Foundation & Nuance"}
    for tier, count in cursor.fetchall():
        print(f"  • {tier_labels.get(tier, f'Tier {tier}')}: {count} cards ({count*100//after_count}%)")

    conn.close()


if __name__ == "__main__":
    insert_cards()

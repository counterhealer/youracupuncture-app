"""Database Population Script for TCM Acupuncture Study Suite.

Imports cards from all 7 category files, clears old seed records,
and populates acupuncture.db with the new high-yield deck.
"""

import sys
import os
import sqlite3
import json
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# Add parent and scripts directory to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "scripts"))

from cards_wm import CARDS as WM_CARDS
from cards_points import CARDS as POINTS_CARDS
from cards_diag import CARDS as DIAG_CARDS
from cards_illness import CARDS as ILLNESS_CARDS
from cards_gyn import CARDS as GYN_CARDS
from cards_paed import CARDS as PAED_CARDS
from cards_safety import CARDS as SAFETY_CARDS
from cards_supplemental import CARDS as SUPPLEMENTAL_CARDS

DB_PATH = BASE_DIR / "data" / "acupuncture.db"


def populate():
    print(f"Connecting to SQLite database: {DB_PATH}")
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Recreate or ensure table schema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        title TEXT NOT NULL,
        front TEXT NOT NULL,
        back TEXT NOT NULL,
        consensus TEXT,
        variations TEXT,
        sources TEXT,
        mastery_level INTEGER DEFAULT 0,
        review_count INTEGER DEFAULT 0,
        importance_level INTEGER DEFAULT 2,
        last_reviewed TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Clear old table content
    cursor.execute("DELETE FROM flashcards")
    conn.commit()

    all_cards = (
        WM_CARDS +
        POINTS_CARDS +
        DIAG_CARDS +
        ILLNESS_CARDS +
        GYN_CARDS +
        PAED_CARDS +
        SAFETY_CARDS +
        SUPPLEMENTAL_CARDS
    )

    print(f"Total cards prepared to insert: {len(all_cards)}")

    from migrate_importance import determine_tier

    inserted = 0
    for card in all_cards:
        tier = determine_tier(card["title"], card["category"])
        cursor.execute("""
        INSERT INTO flashcards (category, title, front, back, consensus, variations, sources, mastery_level, review_count, importance_level)
        VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
        """, (
            card["category"],
            card["title"],
            card["front"],
            card["back"],
            card.get("consensus", ""),
            card.get("variations", ""),
            card.get("sources", "[]"),
            tier
        ))
        inserted += 1

    conn.commit()

    # Verify counts by category
    cursor.execute("SELECT category, COUNT(*) FROM flashcards GROUP BY category ORDER BY category")
    rows = cursor.fetchall()

    print("\n--- Summary of Inserted Flashcards by Category ---")
    total = 0
    for cat, count in rows:
        print(f"  • {cat}: {count} cards")
        total += count
    print(f"\nTotal Flashcards in Database: {total}")

    conn.close()


if __name__ == "__main__":
    populate()

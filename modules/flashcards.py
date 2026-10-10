"""Flashcard Generation and Review Module for Acupuncture Study App.

Generates and stores interactive flashcards in SQLite.
Crucial: When processing multiple versions or competing textbooks, the generator
cross-references sources, synthesizes consensus, and notes variations if sources
conflict (e.g., differing needling depths, angles, or indications).
All points are formatted bilingually with Code, Pinyin, Hanzi, and English.
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Union

from modules.rag_engine import DATA_DIR, retrieve_context, detect_variations_and_conflicts
from modules.tcm_points import get_point_bilingual_name, format_point_bilingual

DB_PATH = DATA_DIR / "acupuncture.db"

# Available Categories for Filtering and Generation
FLASHCARD_CATEGORIES = [
    "All Categories",
    "Western Medicine",
    "Meridians and Points",
    "Diagnosis",
    "Illness",
    "Gynecology",
    "Paediatrics",
    "Safety and Ethics"
]


def get_db_connection():
    """Establish connection to SQLite database."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize SQLite tables for flashcards and clinical case history."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Flashcards table
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
    
    # Ensure importance_level column exists for existing tables
    cursor.execute("PRAGMA table_info(flashcards)")
    existing_cols = [r[1] for r in cursor.fetchall()]
    if "importance_level" not in existing_cols:
        cursor.execute("ALTER TABLE flashcards ADD COLUMN importance_level INTEGER DEFAULT 2")
        conn.commit()
    
    # Clinical case history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS case_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id TEXT,
        case_title TEXT NOT NULL,
        patient_profile TEXT,
        user_diagnosis TEXT,
        user_prescription TEXT,
        score INTEGER,
        feedback_markdown TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    
    # Check if flashcards table is empty or needs default seeding
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    count = cursor.fetchone()[0]
    if count == 0:
        seed_default_flashcards(conn)
        
    conn.close()


def seed_default_flashcards(conn):
    """Seed comprehensive bilingual initial flashcards across all 7 categories."""
    try:
        from scripts.populate_database import populate
        populate()
    except Exception as e:
        print(f"Error seeding default flashcards via populate(): {e}")


def get_flashcards(
    category: Optional[Union[str, List[str]]] = None,
    mastery_level: Optional[int] = None,
    importance_level: Optional[int] = None
) -> List[Dict[str, Any]]:
    """Retrieve flashcards from SQLite database with optional filters.
    
    `category` can be:
    - None or "All Categories": retrieve cards across all categories.
    - str: retrieve cards matching a single category.
    - list/tuple/set: retrieve cards matching ANY of the chosen categories.
    
    `importance_level` can be:
    - None: retrieve all importance levels.
    - 1: Tier 1 - High Yield (Must-Know)
    - 2: Tier 2 - Core Clinical
    - 3: Tier 3 - Foundation & Nuance
    """
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM flashcards WHERE 1=1"
    params = []
    
    if category is not None:
        if isinstance(category, (list, tuple, set)):
            filtered_cats = [str(c) for c in category if c and c != "All Categories"]
            if len(category) > 0 and len(filtered_cats) == 0 and "All Categories" in category:
                # User selected "All Categories"
                pass
            elif len(filtered_cats) == 0:
                # No categories selected
                query += " AND 1=0"
            else:
                placeholders = ", ".join(["?"] * len(filtered_cats))
                query += f" AND category IN ({placeholders})"
                params.extend(filtered_cats)
        elif isinstance(category, str) and category != "All Categories":
            query += " AND category = ?"
            params.append(category)
        
    if mastery_level is not None and mastery_level >= 0:
        query += " AND mastery_level = ?"
        params.append(mastery_level)
        
    if importance_level is not None and importance_level in (1, 2, 3):
        query += " AND importance_level = ?"
        params.append(importance_level)
        
    query += " ORDER BY id DESC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    cards = []
    for row in rows:
        cards.append(dict(row))
    return cards


def add_flashcard(
    category: str,
    title: str,
    front: str,
    back: str,
    consensus: str = "",
    variations: str = "",
    sources: Optional[List[str]] = None,
    importance_level: int = 2
) -> int:
    """Insert a new flashcard into the database."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sources_json = json.dumps(sources or ["Textbook Synthesis"])
    
    # Ensure bilingual formatting
    bilingual_title = format_point_bilingual(title)
    bilingual_front = format_point_bilingual(front)
    bilingual_back = format_point_bilingual(back)
    bilingual_consensus = format_point_bilingual(consensus)
    bilingual_variations = format_point_bilingual(variations)
    
    cursor.execute("""
    INSERT INTO flashcards (category, title, front, back, consensus, variations, sources, mastery_level, importance_level)
    VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)
    """, (category, bilingual_title, bilingual_front, bilingual_back, bilingual_consensus, bilingual_variations, sources_json, importance_level))
    
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def update_card_mastery(card_id: int, rating: str) -> bool:
    """Update flashcard mastery status based on user review."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT mastery_level, review_count FROM flashcards WHERE id = ?", (card_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return False
        
    current_level = row["mastery_level"]
    current_count = row["review_count"]
    
    if rating == "again":
        new_level = 0
    elif rating == "good":
        new_level = min(3, current_level + 1)
    elif rating == "mastered":
        new_level = 3
    else:
        new_level = current_level
        
    now = datetime.now().isoformat()
    
    cursor.execute("""
    UPDATE flashcards
    SET mastery_level = ?, review_count = ?, last_reviewed = ?
    WHERE id = ?
    """, (new_level, current_count + 1, now, card_id))
    
    conn.commit()
    conn.close()
    return True


def delete_flashcard(card_id: int) -> bool:
    """Remove a flashcard from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM flashcards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return True


def get_flashcard_stats() -> Dict[str, Any]:
    """Calculate flashcard deck statistics for analytics."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM flashcards")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE mastery_level = 0")
    new_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE mastery_level IN (1, 2)")
    learning_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE mastery_level = 3")
    mastered_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE importance_level = 1")
    tier1_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE importance_level = 2")
    tier2_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM flashcards WHERE importance_level = 3")
    tier3_cards = cursor.fetchone()[0]
    
    cursor.execute("SELECT category, COUNT(*) FROM flashcards GROUP BY category")
    cat_counts = {r[0]: r[1] for r in cursor.fetchall() if r[0]}
    
    # Combine with predefined category list
    all_cats = list(dict.fromkeys(FLASHCARD_CATEGORIES[1:] + list(cat_counts.keys())))
    
    conn.close()
    return {
        "total": total,
        "new": new_cards,
        "learning": learning_cards,
        "mastered": mastered_cards,
        "tier1": tier1_cards,
        "tier2": tier2_cards,
        "tier3": tier3_cards,
        "categories": all_cats,
        "category_counts": cat_counts
    }


def generate_synthesized_flashcard(topic: str, provider: str = "demo", api_key: Optional[str] = None) -> Tuple[bool, str, Optional[Dict[str, Any]]]:
    """Generate an interactive flashcard from indexed textbooks for a given topic.
    
    Synthesizes consensus and explicitly notes textbook variations (e.g. differing
    needling depths or indications) with bilingual nomenclature.
    """
    contexts = retrieve_context(topic, top_k=5)
    variations_list = detect_variations_and_conflicts(topic, contexts)
    sources = list({c.get("source") for c in contexts if c.get("source")}) or ["Indexed Notes"]
    
    # If using OpenAI / Gemini / Ollama
    if provider in ["openai", "gemini", "ollama"] and (api_key or provider == "ollama"):
        try:
            prompt = f"""
You are an expert Acupuncture and TCM scholar.
Generate a high-yield study flashcard for the topic: '{topic}'.
Based on the following textbook excerpts:
{json.dumps([c['text'] for c in contexts])}

CRITICAL REQUIREMENTS:
1. Always include BOTH the Chinese name (Pinyin & Hanzi) and English translation when mentioning any acupuncture point (e.g. ST36 (Zusanli / 足三里 - Leg Three Miles)).
2. When processing multiple versions or competing textbooks, you MUST cross-reference sources:
   - Synthesize general consensus (channel, location, primary actions).
   - Explicitly identify and note variations, discrepancies, or conflicting views across textbooks (e.g. differing needling depths, angles, contraindications like pregnancy, divergent indications).

Return a JSON object with exactly these keys:
{{
  "category": "Acupoints: Stomach & Yangming" or appropriate category from standard list,
  "title": "Bilingual Topic Title (e.g. ST36 (Zusanli / 足三里 - Leg Three Miles) Needling & Variations)",
  "front": "Concise Question or Clinical Prompt for the front of the flashcard",
  "back": "Detailed answer synthesizing textbook insights",
  "consensus": "Agreed-upon aspects across sources",
  "variations": "Explicit variations or conflicts between textbooks (e.g., CAM vs Deadman vs Maciocia)"
}}
"""
            raw_text = ""
            if provider == "gemini":
                try:
                    from google import genai
                    client = genai.Client(api_key=api_key)
                    for m in ["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-flash-latest"]:
                        try:
                            resp = client.models.generate_content(model=m, contents=prompt)
                            if resp and resp.text:
                                raw_text = resp.text.strip()
                                break
                        except Exception:
                            continue
                except Exception:
                    raw_text = ""
                if not raw_text:
                    try:
                        import google.generativeai as genai_old
                        genai_old.configure(api_key=api_key)
                        model = genai_old.GenerativeModel("gemini-1.5-flash")
                        raw_text = model.generate_content(prompt).text.strip()
                    except Exception:
                        pass
            elif provider == "openai":
                try:
                    import urllib.request
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    payload = json.dumps({
                        "model": "gpt-4o-mini",
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.3
                    }).encode("utf-8")
                    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=payload, headers=headers)
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        resp_data = json.loads(resp.read().decode("utf-8"))
                        raw_text = resp_data["choices"][0]["message"]["content"].strip()
                except Exception:
                    pass
            else:
                raw_text = ""
            if raw_text.startswith("```json"):
                raw_text = raw_text[7:]
            if raw_text.endswith("```"):
                raw_text = raw_text[:-3]
            data = json.loads(raw_text.strip())
            
            card_id = add_flashcard(
                category=data.get("category", "Acupoints & Needling"),
                title=format_point_bilingual(data.get("title", topic)),
                front=format_point_bilingual(data.get("front", f"Review {topic}")),
                back=format_point_bilingual(data.get("back", "Detailed textbook synthesis.")),
                consensus=format_point_bilingual(data.get("consensus", "Standard consensus.")),
                variations=format_point_bilingual(data.get("variations", "No significant conflicts noted.")),
                sources=sources
            )
            data["id"] = card_id
            data["sources"] = sources
            return True, f"Generated and saved card #{card_id} successfully!", data
        except Exception:
            pass
            
    # Built-in TCM Synthesis Engine
    bilingual_topic = format_point_bilingual(topic.strip())
    title = f"{bilingual_topic} (Textbook Synthesis)"
    category = "Acupoints & Needling"
    
    if variations_list:
        v_item = variations_list[0]
        v_text = f"• {v_item['textbook_a']}\n• {v_item['textbook_b']}\nClinical note: {v_item['clinical_significance']}"
    else:
        v_text = f"Synthesized from {len(sources)} indexed textbook references. Depths and indications generally align across standard curricula."
        
    front = f"What are the location, cardinal actions, needling techniques, and cross-textbook variations for {bilingual_topic}?"
    
    back_excerpts = "\n\n".join([f"[{c['source']}]: {c['text'][:250]}..." for c in contexts[:2]])
    back = f"Primary Actions & Characteristics for {bilingual_topic}:\n{back_excerpts if back_excerpts else 'Key clinical acupuncture point / concept.'}\n\n⚠️ Textbook Comparison:\n{v_text}"
    consensus = f"Consensus across {', '.join(sources)}: Standard point location and primary actions established in core curriculum."
    
    card_id = add_flashcard(
        category=category,
        title=title,
        front=front,
        back=back,
        consensus=consensus,
        variations=v_text,
        sources=sources
    )
    
    card_data = {
        "id": card_id,
        "category": category,
        "title": title,
        "front": front,
        "back": back,
        "consensus": consensus,
        "variations": v_text,
        "sources": sources
    }
    return True, f"Generated and saved card #{card_id} for '{topic}'!", card_data

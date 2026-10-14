# -*- coding: utf-8 -*-
"""Mistake Notebook (错题本) Module for NCCAOM & Pan-Canadian Board Prep.

Persistently tracks, manages, and re-tests missed questions from:
- Practice Exam Simulator
- Clinical Case Simulator
Stored in data/acupuncture.db under the `mistake_notebook` table.
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "acupuncture.db"


def get_db_connection() -> sqlite3.Connection:
    """Create a database connection with row factory."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_mistake_db() -> None:
    """Initialize the mistake_notebook table if it does not exist."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS mistake_notebook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id TEXT UNIQUE,
        source TEXT NOT NULL,
        title TEXT,
        question TEXT NOT NULL,
        options_json TEXT NOT NULL,
        correct_index INTEGER NOT NULL,
        user_answer INTEGER,
        explanation TEXT,
        category TEXT,
        difficulty TEXT,
        exam_board TEXT,
        missed_count INTEGER DEFAULT 1,
        last_missed_at TEXT,
        mastered INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()


def add_missed_question(
    question_data: Dict[str, Any],
    source: str = "practice_exam",
    user_answer: Optional[int] = None
) -> None:
    """Insert or update a missed question into the Mistake Notebook."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()

    q_id = str(question_data.get("id") or question_data.get("question_id") or "")
    if not q_id:
        # Fallback hash if no id
        q_id = str(hash(question_data.get("question", "")[:60]))

    title = question_data.get("title", "")
    question = question_data.get("question") or question_data.get("prompt", "")
    options = question_data.get("options", [])
    correct_idx = question_data.get("answer") if "answer" in question_data else question_data.get("correct_index", 0)
    explanation = question_data.get("explanation", "")
    if not explanation and "explanations" in question_data:
        exps = question_data.get("explanations", [])
        if correct_idx < len(exps):
            explanation = exps[correct_idx]
        else:
            explanation = "; ".join(exps)

    category = question_data.get("category", "General")
    difficulty = question_data.get("difficulty", "Medium")
    exam_board = question_data.get("exam", "Board Exam")
    now_str = datetime.now().isoformat()

    options_json = json.dumps(options, ensure_ascii=False)

    c.execute("""
    INSERT INTO mistake_notebook (
        question_id, source, title, question, options_json,
        correct_index, user_answer, explanation, category,
        difficulty, exam_board, missed_count, last_missed_at, mastered
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, 0)
    ON CONFLICT(question_id) DO UPDATE SET
        missed_count = missed_count + 1,
        user_answer = excluded.user_answer,
        last_missed_at = excluded.last_missed_at,
        mastered = 0
    """, (
        q_id, source, title, question, options_json,
        correct_idx, user_answer, explanation, category,
        difficulty, exam_board, now_str
    ))

    conn.commit()
    conn.close()


def get_all_missed_questions(only_unmastered: bool = True) -> List[Dict[str, Any]]:
    """Retrieve all recorded missed questions from the database."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()

    if only_unmastered:
        rows = c.execute("""
            SELECT * FROM mistake_notebook
            WHERE mastered = 0
            ORDER BY missed_count DESC, last_missed_at DESC
        """).fetchall()
    else:
        rows = c.execute("""
            SELECT * FROM mistake_notebook
            ORDER BY mastered ASC, missed_count DESC, last_missed_at DESC
        """).fetchall()

    conn.close()

    results = []
    for r in rows:
        results.append({
            "id": r["id"],
            "question_id": r["question_id"],
            "source": r["source"],
            "title": r["title"],
            "question": r["question"],
            "options": json.loads(r["options_json"]),
            "answer": r["correct_index"],
            "correct_index": r["correct_index"],
            "user_answer": r["user_answer"],
            "explanation": r["explanation"],
            "category": r["category"],
            "difficulty": r["difficulty"],
            "exam": r["exam_board"],
            "missed_count": r["missed_count"],
            "last_missed_at": r["last_missed_at"],
            "mastered": bool(r["mastered"])
        })
    return results


def mark_question_mastered(question_id: str, mastered: bool = True) -> None:
    """Toggle the mastery flag of a missed question."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        UPDATE mistake_notebook
        SET mastered = ?
        WHERE question_id = ?
    """, (1 if mastered else 0, str(question_id)))
    conn.commit()
    conn.close()


def delete_missed_question(question_id: str) -> None:
    """Delete a question permanently from the mistake notebook."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM mistake_notebook WHERE question_id = ?", (str(question_id),))
    conn.commit()
    conn.close()


def clear_all_missed_questions() -> None:
    """Remove all records from the mistake notebook."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM mistake_notebook")
    conn.commit()
    conn.close()


def get_mistake_stats() -> Dict[str, Any]:
    """Return summary statistics of the Mistake Notebook."""
    init_mistake_db()
    conn = get_db_connection()
    c = conn.cursor()
    total = c.execute("SELECT count(*) FROM mistake_notebook").fetchone()[0]
    unmastered = c.execute("SELECT count(*) FROM mistake_notebook WHERE mastered = 0").fetchone()[0]
    mastered = c.execute("SELECT count(*) FROM mistake_notebook WHERE mastered = 1").fetchone()[0]
    sources = dict(c.execute("SELECT source, count(*) FROM mistake_notebook GROUP BY source").fetchall())
    categories = dict(c.execute("SELECT category, count(*) FROM mistake_notebook WHERE mastered = 0 GROUP BY category").fetchall())
    conn.close()

    return {
        "total": total,
        "unmastered": unmastered,
        "mastered": mastered,
        "sources": sources,
        "categories": categories
    }

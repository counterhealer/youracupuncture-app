# -*- coding: utf-8 -*-
"""
Script to update modules/exam_bank.py with full Mistake Notebook (错题本) integration:
1. Automatic recording of missed questions on exam submission.
2. Mode switch between "📝 10-Question Exam Simulator" and "🎯 Mistake Notebook / 错题本".
3. "🎯 Start Mistake Drill": Drill directly on unmastered missed questions.
4. Mark as mastered and delete individual or all mistake records.
"""

import os

EXAM_BANK_PATH = "modules/exam_bank.py"

content = '''# -*- coding: utf-8 -*-
"""TCM Practice Exam Module (800+ Question Bank: Pan-Canadian CARB-TCMPA & NCCAOM).

Delivers authentic multiple-choice board examination simulation sessions (10 questions at a time)
spanning Easy, Medium, and Hard difficulty tiers across all major acupuncture and herbal domains:
- Pan-Canadian CARB-TCMPA Clinical Case Studies & Herbal Formulations
- Point Locations & Anatomy
- Point Actions & Indications
- Needling Safety & Precautions
- Special Point Categories
- Zang-Fu & Diagnostics
- Prescriptions & Clinical Vignettes
Includes persistent "Mistake Notebook" (错题本) for focused re-testing of missed questions.
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Any, Optional

import streamlit as st
from modules.mistake_notebook import (
    add_missed_question,
    get_all_missed_questions,
    mark_question_mastered,
    delete_missed_question,
    clear_all_missed_questions,
    get_mistake_stats
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
QUESTIONS_FILE = DATA_DIR / "exam_questions.json"

_CACHED_QUESTIONS: Optional[List[Dict[str, Any]]] = None


def load_all_questions() -> List[Dict[str, Any]]:
    """Load all questions from data/exam_questions.json with in-memory caching."""
    global _CACHED_QUESTIONS
    if _CACHED_QUESTIONS is not None:
        return _CACHED_QUESTIONS

    if QUESTIONS_FILE.exists():
        try:
            with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
                _CACHED_QUESTIONS = json.load(f)
                return _CACHED_QUESTIONS
        except Exception as e:
            st.error(f"Error loading exam questions: {e}")
            return []
    return []


def get_bank_stats() -> Dict[str, Any]:
    """Return summary statistics of the 800+ question exam bank."""
    questions = load_all_questions()
    categories = {}
    difficulties = {}
    exams = {}
    for q in questions:
        cat = q.get("category", "General")
        diff = q.get("difficulty", "Medium")
        exam = q.get("exam", "NCCAOM & National Domains")
        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1
        exams[exam] = exams.get(exam, 0) + 1
    return {
        "total": len(questions),
        "categories": categories,
        "difficulties": difficulties,
        "exams": exams
    }


def sample_exam_questions(
    count: int = 10,
    difficulty: Optional[str] = None,
    category: Optional[str] = None,
    exam: Optional[str] = None,
    seed: Optional[int] = None
) -> List[Dict[str, Any]]:
    """Sample a batch of N questions matching the desired board exam, difficulty, and category."""
    questions = load_all_questions()
    if not questions:
        return []

    filtered = questions
    if exam and exam != "All Exam Boards (Pan-Canadian & NCCAOM)":
        filtered = [q for q in filtered if q.get("exam", "NCCAOM & National Domains") == exam]

    if difficulty and difficulty != "All Difficulties (Mixed)":
        filtered = [q for q in filtered if q.get("difficulty") == difficulty]

    if category and category != "All Topics":
        filtered = [q for q in filtered if q.get("category") == category]

    if not filtered:
        filtered = questions  # Fallback to all if filter is too narrow

    if seed is not None:
        rng = random.Random(seed)
        return rng.sample(filtered, min(count, len(filtered)))
    else:
        return random.sample(filtered, min(count, len(filtered)))


def render_practice_exam_tab():
    """Render the Board Exam Simulator and Mistake Notebook tab."""
    # Custom CSS for Practice Exam white text and high contrast styling
    st.markdown("""
    <style>
    /* Practice Exam White Font Styling */
    div[data-testid="stSelectbox"] label,
    div[data-testid="stSelectbox"] label p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* Radio button options styling: pure white text */
    div[data-testid="stForm"] div[data-testid="stRadio"] {
        background: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-top: none !important;
        border-radius: 0 0 12px 12px !important;
        padding: 10px 20px 18px 20px !important;
        margin-bottom: 24px !important;
    }

    div[data-testid="stForm"] div[data-testid="stRadio"] label,
    div[data-testid="stForm"] div[data-testid="stRadio"] label p,
    div[data-testid="stForm"] div[data-testid="stRadio"] label span,
    div[data-testid="stForm"] div[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] p {
        color: #ffffff !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        line-height: 1.55 !important;
    }

    div[data-testid="stForm"] div[data-testid="stRadio"] label:hover p,
    div[data-testid="stForm"] div[data-testid="stRadio"] label:hover span {
        color: #38bdf8 !important;
    }

    div[data-testid="stForm"] div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 10px !important;
    }

    /* Form submission button */
    div[data-testid="stForm"] button[kind="primary"] {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 12px 24px !important;
        background: linear-gradient(135deg, #007ba7, #484eb2) !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(0, 123, 167, 0.35) !important;
    }

    /* Expander white text styling */
    div[data-testid="stExpander"] {
        background: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        margin-bottom: 12px !important;
    }

    div[data-testid="stExpander"] details summary {
        background: transparent !important;
    }

    div[data-testid="stExpander"] details summary span,
    div[data-testid="stExpander"] details summary p {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.98rem !important;
    }

    div[data-testid="stExpander"] details summary:hover span,
    div[data-testid="stExpander"] details summary:hover p {
        color: #38bdf8 !important;
    }

    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] li,
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] span,
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] strong {
        color: #ffffff !important;
    }

    /* Selectbox input field white styling */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        background-color: #111827 !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
        color: #ffffff !important;
    }

    /* Draw new button white text */
    button[kind="secondary"] {
        background-color: #111827 !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        font-weight: 600 !important;
    }
    button[kind="secondary"]:hover {
        border-color: #38bdf8 !important;
        color: #38bdf8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header in a sleek dark banner with pure white text
    st.markdown("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0; letter-spacing: -0.01em;">
            Pan-Canadian & NCCAOM Board Exam Simulator
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            800+ authentic board-style multiple choice questions spanning Pan-Canadian CARB-TCMPA clinical cases and NCCAOM core domains. Complete 10 questions at a time with instant grading, textbook explanations, and automated Mistake Notebook tracking.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Mode Selector: Standard Practice Exam vs Mistake Notebook
    mistake_stats = get_mistake_stats()
    unmastered_count = mistake_stats.get("unmastered", 0)
    badge_label = f" ({unmastered_count} to review)" if unmastered_count > 0 else " (Empty)"

    if "exam_view_mode" not in st.session_state:
        st.session_state.exam_view_mode = "📝 10-Question Exam Simulator"

    col_mode_sel, _ = st.columns([2.5, 1])
    with col_mode_sel:
        exam_view = st.radio(
            "Select Mode:",
            options=[
                "📝 10-Question Exam Simulator",
                f"🎯 Mistake Notebook / 错题本{badge_label}"
            ],
            index=0 if st.session_state.exam_view_mode.startswith("📝") else 1,
            horizontal=True,
            key="exam_mode_radio"
        )
        st.session_state.exam_view_mode = exam_view

    st.write("")

    # =========================================================================
    # VIEW A: MISTAKE NOTEBOOK (错题本)
    # =========================================================================
    if exam_view.startswith("🎯 Mistake Notebook"):
        st.markdown(f"""
        <div style="background: #111827; border: 1.5px solid rgba(248, 113, 113, 0.4); border-radius: 12px; padding: 18px 22px; margin-bottom: 18px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                <div>
                    <span style="font-size: 1.25rem; font-weight: 800; color: #f87171;">🎯 个人错题本与弱项强化 (Mistake Notebook)</span>
                    <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                        Automatically archives all questions you missed during Practice Exams and Clinical Case Simulations for targeted re-testing until 100% mastery.
                    </div>
                </div>
                <div style="display: flex; gap: 10px;">
                    <div style="background: rgba(239, 68, 68, 0.2); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 8px; padding: 6px 14px; text-align: center;">
                        <div style="font-size: 1.25rem; font-weight: 900; color: #fca5a5;">{unmastered_count}</div>
                        <div style="font-size: 0.7rem; font-weight: 700; color: #f87171; text-transform: uppercase;">Unmastered</div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 8px; padding: 6px 14px; text-align: center;">
                        <div style="font-size: 1.25rem; font-weight: 900; color: #a7f3d0;">{mistake_stats.get('mastered', 0)}</div>
                        <div style="font-size: 0.7rem; font-weight: 700; color: #34d399; text-transform: uppercase;">Mastered</div>
                    </div>
                    <div style="background: rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 8px; padding: 6px 14px; text-align: center;">
                        <div style="font-size: 1.25rem; font-weight: 900; color: #bae6fd;">{mistake_stats.get('total', 0)}</div>
                        <div style="font-size: 0.7rem; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Total Saved</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if mistake_stats.get("total", 0) == 0:
            st.info("🎉 **Your Mistake Notebook is currently empty!** Any questions you miss in the Practice Exam Simulator or Case Simulator will automatically appear here for review.")
            return

        col_act1, col_act2, col_act3 = st.columns([1.5, 1.2, 1.0], vertical_alignment="bottom")
        with col_act1:
            if unmastered_count > 0:
                if st.button("🚀 Start Mistake Drill (Test 10 Missed Qs)", type="primary", use_container_width=True, key="start_mistake_drill_btn"):
                    unmastered_qs = get_all_missed_questions(only_unmastered=True)
                    drill_sample = random.sample(unmastered_qs, min(10, len(unmastered_qs)))
                    # Format as exam questions
                    st.session_state.current_exam_questions = drill_sample
                    st.session_state.exam_submitted = False
                    st.session_state.exam_user_answers = {}
                    st.session_state.exam_seed = random.randint(1, 999999)
                    st.session_state.exam_view_mode = "📝 10-Question Exam Simulator"
                    st.rerun()
            else:
                st.success("🏆 You have mastered all saved missed questions!")

        with col_act2:
            show_only_unmastered = st.checkbox("Show Unmastered Only", value=True, key="filter_unmastered_cb")

        with col_act3:
            if st.button("🗑️ Clear All Records", type="secondary", use_container_width=True, key="clear_all_mistakes_btn"):
                clear_all_missed_questions()
                st.rerun()

        # Load missed questions
        missed_list = get_all_missed_questions(only_unmastered=show_only_unmastered)
        st.caption(f"Displaying **{len(missed_list)}** saved questions in Mistake Notebook:")

        for idx, item in enumerate(missed_list, start=1):
            q_id = item["question_id"]
            is_mastered = item.get("mastered", False)
            times_missed = item.get("missed_count", 1)
            source_tag = "Clinical Case" if item.get("source") == "case_simulator" else "Practice Exam"
            status_badge = "✅ Mastered" if is_mastered else f"❌ Missed {times_missed}x"
            status_bg = "rgba(16, 185, 129, 0.2)" if is_mastered else "rgba(239, 68, 68, 0.2)"
            status_color = "#34d399" if is_mastered else "#f87171"

            with st.expander(f"Q{idx} [{status_badge}] — {item['question'][:75]}...", expanded=False):
                st.markdown(f"""
                <div style="display: flex; gap: 8px; margin-bottom: 8px; flex-wrap: wrap;">
                    <span style="background: {status_bg}; color: {status_color}; font-size: 0.74rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
                        {status_badge}
                    </span>
                    <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 0.74rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
                        {source_tag}
                    </span>
                    <span style="background: rgba(167, 139, 250, 0.2); color: #c4b5fd; font-size: 0.74rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
                        {item.get('category', 'Domain')}
                    </span>
                    <span style="background: rgba(251, 191, 36, 0.2); color: #fde68a; font-size: 0.74rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
                        {item.get('difficulty', 'Medium')}
                    </span>
                </div>
                <div style="font-size: 1.05rem; font-weight: 600; color: #ffffff !important; line-height: 1.55; margin-bottom: 12px;">
                    {item['question']}
                </div>
                """, unsafe_allow_html=True)

                opts = item["options"]
                correct_idx = item["answer"]
                user_idx = item.get("user_answer")

                for opt_i, opt_text in enumerate(opts):
                    opt_letter = chr(65 + opt_i)
                    if opt_i == correct_idx:
                        st.markdown(f"""
                        <div style="background: rgba(16, 185, 129, 0.15); border-left: 4px solid #10b981; padding: 8px 12px; border-radius: 4px; margin-bottom: 6px; color: #a7f3d0; font-weight: 700;">
                            ✓ {opt_letter}. {opt_text} (Correct Answer)
                        </div>
                        """, unsafe_allow_html=True)
                    elif user_idx is not None and opt_i == user_idx:
                        st.markdown(f"""
                        <div style="background: rgba(239, 68, 68, 0.15); border-left: 4px solid #ef4444; padding: 8px 12px; border-radius: 4px; margin-bottom: 6px; color: #fca5a5; font-weight: 600;">
                            ✗ {opt_letter}. {opt_text} (Your Previous Choice)
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="padding: 6px 12px; color: #cbd5e1; margin-bottom: 4px;">
                            &nbsp;&nbsp;&nbsp;{opt_letter}. {opt_text}
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown(f"""
                <div style="background: rgba(0, 0, 0, 0.4); border-left: 4px solid #38bdf8; padding: 12px 16px; border-radius: 6px; margin: 12px 0;">
                    <div style="font-weight: 800; font-size: 0.8rem; text-transform: uppercase; color: #38bdf8; margin-bottom: 4px;">
                        Official Textbook Rationale
                    </div>
                    <div style="font-size: 0.92rem; line-height: 1.55; color: #ffffff !important;">
                        {item.get('explanation', 'No explanation provided.')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                c_m1, c_m2, _ = st.columns([1.2, 1.0, 2.0])
                with c_m1:
                    if not is_mastered:
                        if st.button("✅ Mark as Mastered", key=f"btn_master_{q_id}"):
                            mark_question_mastered(q_id, mastered=True)
                            st.rerun()
                    else:
                        if st.button("🔄 Move to Review", key=f"btn_unmaster_{q_id}"):
                            mark_question_mastered(q_id, mastered=False)
                            st.rerun()
                with c_m2:
                    if st.button("🗑️ Remove", key=f"btn_del_{q_id}"):
                        delete_missed_question(q_id)
                        st.rerun()

        return

    # =========================================================================
    # VIEW B: STANDARD 10-QUESTION EXAM SIMULATOR
    # =========================================================================
    stats = get_bank_stats()
    exam_boards = [
        "All Exam Boards (Pan-Canadian & NCCAOM)",
        "Pan-Canadian Board Exam",
        "NCCAOM & National Domains"
    ]
    difficulties = ["All Difficulties (Mixed)", "Easy", "Medium", "Hard"]

    # Filter & Session Controls Bar
    with st.container():
        col_exam, col_diff, col_cat, col_btn = st.columns([1.3, 1.0, 1.4, 1.1], vertical_alignment="bottom")
        with col_exam:
            sel_exam = st.selectbox(
                "Exam Board",
                options=exam_boards,
                index=0,
                key="exam_board_select"
            )
        with col_diff:
            sel_diff = st.selectbox(
                "Difficulty Tier",
                options=difficulties,
                index=0,
                key="exam_diff_select"
            )
        with col_cat:
            all_qs = load_all_questions()
            if sel_exam == "Pan-Canadian Board Exam":
                cat_pool = sorted(list(set(q.get("category", "") for q in all_qs if q.get("exam") == "Pan-Canadian Board Exam")))
            elif sel_exam == "NCCAOM & National Domains":
                cat_pool = sorted(list(set(q.get("category", "") for q in all_qs if q.get("exam") != "Pan-Canadian Board Exam")))
            else:
                cat_pool = sorted(list(stats["categories"].keys()))
            all_categories = ["All Topics"] + cat_pool
            sel_cat = st.selectbox(
                "Clinical Domain",
                options=all_categories,
                index=0,
                key="exam_cat_select"
            )
        with col_btn:
            if st.button("🔄 Draw 10 New Questions", type="secondary", use_container_width=True, key="exam_draw_new_btn"):
                st.session_state.current_exam_questions = sample_exam_questions(
                    count=10,
                    difficulty=sel_diff,
                    category=sel_cat,
                    exam=sel_exam
                )
                st.session_state.exam_submitted = False
                st.session_state.exam_user_answers = {}
                st.session_state.exam_seed = random.randint(1, 999999)
                st.session_state.exam_last_filters = (sel_exam, sel_diff, sel_cat)
                st.rerun()

    # If filters changed, auto-sample new batch matching active filters
    active_filters = (sel_exam, sel_diff, sel_cat)
    if "exam_last_filters" in st.session_state and st.session_state.exam_last_filters != active_filters:
        st.session_state.exam_last_filters = active_filters
        st.session_state.current_exam_questions = sample_exam_questions(
            count=10,
            difficulty=sel_diff,
            category=sel_cat,
            exam=sel_exam
        )
        st.session_state.exam_submitted = False
        st.session_state.exam_user_answers = {}
        st.session_state.exam_seed = random.randint(1, 999999)
    elif "exam_last_filters" not in st.session_state:
        st.session_state.exam_last_filters = active_filters

    # Initialize 10-question session in session_state if not present
    if "current_exam_questions" not in st.session_state or not st.session_state.current_exam_questions:
        st.session_state.current_exam_questions = sample_exam_questions(
            count=10,
            difficulty=sel_diff,
            category=sel_cat,
            exam=sel_exam
        )
        st.session_state.exam_submitted = False
        st.session_state.exam_user_answers = {}
        st.session_state.exam_seed = random.randint(1, 999999)

    current_q_list = st.session_state.current_exam_questions
    is_submitted = st.session_state.get("exam_submitted", False)

    # Exam Info Pill Bar
    if not is_submitted:
        session_badge = "📝 10-Question Mock Exam Session — In Progress"
    else:
        session_badge = "📊 Exam Results & Clinical Review — 10 Questions Evaluated"

    total_pan = stats.get('exams', {}).get('Pan-Canadian Board Exam', 0)
    total_nccaom = stats.get('exams', {}).get('NCCAOM & National Domains', 0)

    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; background: #0f172a; border: 1.5px solid #007ba7; border-radius: 10px; padding: 12px 18px; margin: 16px 0 20px 0; flex-wrap: wrap; gap: 8px;">
        <div style="font-size: 0.92rem; font-weight: 700; color: #ffffff !important;">
            {session_badge}
        </div>
        <div style="font-size: 0.85rem; font-weight: 600; color: #e2e8f0 !important; font-family: ui-monospace, monospace;">
            Question Pool: {stats['total']} Total ({total_pan} Pan-Canadian · {total_nccaom} NCCAOM)
        </div>
    </div>
    """, unsafe_allow_html=True)

    # MODE 1: EXAM IN PROGRESS (Active 10 Questions)
    if not is_submitted:
        with st.form("practice_exam_form", clear_on_submit=False):
            user_selections = {}

            for idx, q in enumerate(current_q_list, start=1):
                q_id = q.get("id") or q.get("question_id")
                diff = q.get("difficulty", "Medium")
                diff_badge_color = "#34d399" if diff == "Easy" else ("#fbbf24" if diff == "Medium" else "#f87171")
                diff_bg_color = "rgba(16, 185, 129, 0.2)" if diff == "Easy" else ("rgba(200, 150, 102, 0.25)" if diff == "Medium" else "rgba(239, 68, 68, 0.2)")

                st.markdown(f"""
                <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px 12px 0 0; padding: 16px 20px 14px 20px; margin-top: 18px;">
                    <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px; flex-wrap: wrap;">
                        <span style="font-weight: 800; font-size: 0.95rem; color: #38bdf8;">Question {idx} of {len(current_q_list)}</span>
                        <span style="background: {diff_bg_color}; color: {diff_badge_color}; font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
                            {diff}
                        </span>
                        <span style="background: rgba(14, 165, 233, 0.2); color: #38bdf8; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(14, 165, 233, 0.3);">
                            {q.get('exam', 'Board Exam')}
                        </span>
                        <span style="background: rgba(72, 78, 178, 0.35); color: #c7d2fe; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(72, 78, 178, 0.4);">
                            {q.get('category', 'General')}
                        </span>
                    </div>
                    <div style="font-size: 1.05rem; font-weight: 600; color: #ffffff !important; line-height: 1.55;">
                        {q['question']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # 4 Options Radio Group
                opts = q["options"]
                formatted_opts = [f"{chr(65+i)}. {opt}" for i, opt in enumerate(opts)]
                prev_answer = st.session_state.exam_user_answers.get(q_id, None)
                default_idx = None
                if prev_answer is not None and prev_answer in range(len(formatted_opts)):
                    default_idx = prev_answer

                selected_str = st.radio(
                    f"Select answer for Q{idx}",
                    options=formatted_opts,
                    index=default_idx,
                    key=f"exam_q_{q_id}_{st.session_state.get('exam_seed', 0)}",
                    label_visibility="collapsed"
                )
                user_selections[q_id] = formatted_opts.index(selected_str) if selected_str in formatted_opts else None

            submit_btn = st.form_submit_button(
                "📝 Submit Exam & Grade Answers",
                type="primary",
                use_container_width=True
            )

            if submit_btn:
                st.session_state.exam_submitted = True
                st.session_state.exam_user_answers = user_selections

                # Automatically record missed questions to Mistake Notebook
                for q in current_q_list:
                    q_id = q.get("id") or q.get("question_id")
                    chosen = user_selections.get(q_id)
                    correct = q.get("answer") if "answer" in q else q.get("correct_index", 0)
                    if chosen != correct:
                        add_missed_question(q, source="practice_exam", user_answer=chosen)
                    else:
                        mark_question_mastered(str(q_id), mastered=True)

                st.rerun()

    # MODE 2: EVALUATION & REVIEW MODE (Active when Submitted)
    else:
        user_answers = st.session_state.get("exam_user_answers", {})
        score = 0
        total = len(current_q_list)

        for q in current_q_list:
            q_id = q.get("id") or q.get("question_id")
            correct = q.get("answer") if "answer" in q else q.get("correct_index", 0)
            if user_answers.get(q_id) == correct:
                score += 1

        percent = round((score / total) * 100) if total > 0 else 0
        passed = percent >= 70

        status_color = "#10b981" if passed else "#ef4444"
        verdict_text = "PASS — Board Standard Met (≥ 70%)" if passed else "NEEDS REVIEW — Standard is ≥ 70%"
        missed_count = total - score

        # Score Summary Card
        st.markdown(f"""
        <div style="background: #111827; border: 2px solid {status_color}; border-radius: 12px; padding: 22px 24px; margin: 12px 0 16px 0; text-align: center; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);">
            <div style="font-size: 0.88rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: {status_color};">
                {verdict_text}
            </div>
            <div style="font-size: 2.6rem; font-weight: 900; color: #ffffff !important; margin: 6px 0;">
                {score} / {total} <span style="font-size: 1.3rem; color: #94a3b8;">({percent}%)</span>
            </div>
            <div style="font-size: 0.95rem; color: #cbd5e1 !important;">
                Review each question below with detailed textbook citations and rationale.
            </div>
            {f'<div style="font-size: 0.88rem; color: #f87171; margin-top: 8px; font-weight: 700;">💡 {missed_count} missed questions have been automatically saved to your Mistake Notebook (错题本) for focused re-testing!</div>' if missed_count > 0 else '<div style="font-size: 0.88rem; color: #34d399; margin-top: 8px; font-weight: 700;">🌟 Flawless score! All questions marked as Mastered.</div>'}
        </div>
        """, unsafe_allow_html=True)

        # Prominent Action Bar above detailed explanations
        col_top_act1, col_top_act2, col_top_act3 = st.columns([1.5, 1.2, 1.3])
        with col_top_act1:
            if st.button("⏩ Next Questions (New Set)", type="primary", use_container_width=True, key="exam_next_set_top_btn"):
                st.session_state.current_exam_questions = sample_exam_questions(
                    count=10,
                    difficulty=sel_diff,
                    category=sel_cat,
                    exam=sel_exam
                )
                st.session_state.exam_submitted = False
                st.session_state.exam_user_answers = {}
                st.session_state.exam_seed = random.randint(1, 999999)
                st.rerun()
        with col_top_act2:
            if st.button("🔄 Retake This Set", type="secondary", use_container_width=True, key="exam_retake_top_btn"):
                st.session_state.exam_submitted = False
                st.session_state.exam_user_answers = {}
                st.session_state.exam_seed = random.randint(1, 999999)
                st.rerun()
        with col_top_act3:
            if missed_count > 0:
                if st.button("🎯 Open Mistake Notebook", type="secondary", use_container_width=True, key="open_mistake_nb_btn"):
                    st.session_state.exam_view_mode = "🎯 Mistake Notebook / 错题本"
                    st.rerun()

        if passed and percent >= 90:
            st.balloons()

        # Detailed Question Breakdown
        st.markdown("""
        <h3 style="color: #ffffff !important; font-size: 1.3rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px;">
            📋 Detailed Answer Key & Clinical Explanations
        </h3>
        """, unsafe_allow_html=True)

        for idx, q in enumerate(current_q_list, start=1):
            q_id = q.get("id") or q.get("question_id")
            chosen = user_answers.get(q_id)
            correct = q.get("answer") if "answer" in q else q.get("correct_index", 0)
            is_correct = (chosen == correct)
            opts = q["options"]

            banner_border = "#10b981" if is_correct else "#ef4444"
            icon = "✅ Correct" if is_correct else "❌ Incorrect"

            exam_tag = q.get('exam', 'Board Exam')
            with st.expander(f"Question {idx}: {icon} — [{exam_tag}] {q['question'][:65]}...", expanded=not is_correct):
                st.markdown(f"""
                <div style="color: #ffffff !important; font-size: 1.02rem; font-weight: 600; margin-bottom: 10px;">
                    <span style="color: #38bdf8; font-weight: 800;">Question {idx} ({exam_tag} · {q.get('category', 'Domain')}):</span> {q['question']}
                </div>
                """, unsafe_allow_html=True)

                if chosen is not None:
                    ans_color = "#34d399" if is_correct else "#f87171"
                    st.markdown(f"""
                    <div style="color: #ffffff !important; font-size: 0.95rem; margin-bottom: 6px;">
                        <strong>Your Answer:</strong> <span style="color: {ans_color}; font-weight: 700;">{chr(65+chosen)}. {opts[chosen]}</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="color: #ffffff !important; font-size: 0.95rem; margin-bottom: 6px;">
                        <strong>Your Answer:</strong> <span style="color: #f87171; font-style: italic;">Not Answered</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                <div style="color: #ffffff !important; font-size: 0.95rem; margin-bottom: 14px;">
                    <strong>Correct Answer:</strong> <span style="color: #34d399; font-weight: 700;">{chr(65+correct)}. {opts[correct]}</span>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style="background: rgba(0, 0, 0, 0.4); border-left: 4px solid {banner_border}; padding: 14px 18px; border-radius: 6px; margin: 12px 0;">
                    <div style="font-weight: 800; font-size: 0.82rem; text-transform: uppercase; color: {banner_border}; margin-bottom: 6px; letter-spacing: 0.05em;">
                        Official Board Rationale & Clinical Reference
                    </div>
                    <div style="font-size: 0.95rem; line-height: 1.6; color: #ffffff !important;">
                        {q.get('explanation', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Bottom Next Questions Button
        st.write("")
        col_bot_act1, col_bot_act2, _ = st.columns([1.6, 1.2, 1.2])
        with col_bot_act1:
            if st.button("⏩ Next Questions (New Set)", type="primary", use_container_width=True, key="exam_next_set_bottom_btn"):
                st.session_state.current_exam_questions = sample_exam_questions(
                    count=10,
                    difficulty=sel_diff,
                    category=sel_cat,
                    exam=sel_exam
                )
                st.session_state.exam_submitted = False
                st.session_state.exam_user_answers = {}
                st.session_state.exam_seed = random.randint(1, 999999)
                st.rerun()
        with col_bot_act2:
            if st.button("🔄 Retake This Set", type="secondary", use_container_width=True, key="exam_retake_bottom_btn"):
                st.session_state.exam_submitted = False
                st.session_state.exam_user_answers = {}
                st.session_state.exam_seed = random.randint(1, 999999)
                st.rerun()
'''

with open(EXAM_BANK_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {EXAM_BANK_PATH} with Mistake Notebook integration!")

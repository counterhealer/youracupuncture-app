# -*- coding: utf-8 -*-
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
"""

import json
import random
from pathlib import Path
from typing import List, Dict, Any, Optional

import streamlit as st

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
    """Render the 10-Question Board Exam Simulator tab."""
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
            800+ authentic board-style multiple choice questions spanning Pan-Canadian CARB-TCMPA clinical cases and NCCAOM core domains. Complete 10 questions at a time with instant grading and textbook explanations.
        </p>
    </div>
    """, unsafe_allow_html=True)

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
                # Reset exam session
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

    # MODE A: EXAM IN PROGRESS (Active 10 Questions)
    if not is_submitted:
        with st.form("practice_exam_form", clear_on_submit=False):
            user_selections = {}

            for idx, q in enumerate(current_q_list, start=1):
                q_id = q["id"]
                diff_badge_color = "#34d399" if q["difficulty"] == "Easy" else ("#fbbf24" if q["difficulty"] == "Medium" else "#f87171")
                diff_bg_color = "rgba(16, 185, 129, 0.2)" if q["difficulty"] == "Easy" else ("rgba(200, 150, 102, 0.25)" if q["difficulty"] == "Medium" else "rgba(239, 68, 68, 0.2)")

                st.markdown(f"""
                <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px 12px 0 0; padding: 16px 20px 14px 20px; margin-top: 18px;">
                    <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 8px; flex-wrap: wrap;">
                        <span style="font-weight: 800; font-size: 0.95rem; color: #38bdf8;">Question {idx} of 10</span>
                        <span style="background: {diff_bg_color}; color: {diff_badge_color}; font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
                            {q['difficulty']}
                        </span>
                        <span style="background: rgba(14, 165, 233, 0.2); color: #38bdf8; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(14, 165, 233, 0.3);">
                            {q.get('exam', 'Board Exam')}
                        </span>
                        <span style="background: rgba(72, 78, 178, 0.35); color: #c7d2fe; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(72, 78, 178, 0.4);">
                            {q['category']}
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
                "📝 Submit 10-Question Exam & Grade Answers",
                type="primary",
                use_container_width=True
            )

            if submit_btn:
                st.session_state.exam_submitted = True
                st.session_state.exam_user_answers = user_selections
                st.rerun()

    # MODE B: EVALUATION & REVIEW MODE (Active when Submitted)
    else:
        user_answers = st.session_state.get("exam_user_answers", {})
        score = 0
        total = len(current_q_list)

        for q in current_q_list:
            if user_answers.get(q["id"]) == q["answer"]:
                score += 1

        percent = round((score / total) * 100) if total > 0 else 0
        passed = percent >= 70

        status_color = "#10b981" if passed else "#ef4444"
        verdict_text = "PASS — Board Standard Met (≥ 70%)" if passed else "NEEDS REVIEW — Standard is ≥ 70%"

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
                Review each question below with detailed textbook citations and rationale. Click <strong>Next Questions</strong> below when ready for a new set.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Prominent Action Bar above detailed explanations
        col_top_act1, col_top_act2, _ = st.columns([1.6, 1.2, 1.2])
        with col_top_act1:
            if st.button("⏩ Next Questions (New 10 Set)", type="primary", use_container_width=True, key="exam_next_set_top_btn"):
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

        if passed and percent >= 90:
            st.balloons()

        # Detailed Question Breakdown
        st.markdown("""
        <h3 style="color: #ffffff !important; font-size: 1.3rem; font-weight: 800; margin-top: 24px; margin-bottom: 12px;">
            📋 Detailed Answer Key & Clinical Explanations
        </h3>
        """, unsafe_allow_html=True)

        for idx, q in enumerate(current_q_list, start=1):
            q_id = q["id"]
            chosen = user_answers.get(q_id)
            correct = q["answer"]
            is_correct = (chosen == correct)
            opts = q["options"]

            banner_border = "#10b981" if is_correct else "#ef4444"
            icon = "✅ Correct" if is_correct else "❌ Incorrect"

            exam_tag = q.get('exam', 'Board Exam')
            with st.expander(f"Question {idx}: {icon} — [{exam_tag}] {q['question'][:65]}...", expanded=not is_correct):
                st.markdown(f"""
                <div style="color: #ffffff !important; font-size: 1.02rem; font-weight: 600; margin-bottom: 10px;">
                    <span style="color: #38bdf8; font-weight: 800;">Question {idx} ({exam_tag} · {q['category']}):</span> {q['question']}
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
                        {q['explanation']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Bottom Next 10 Questions Button
        st.write("")
        col_bot_act1, col_bot_act2, _ = st.columns([1.6, 1.2, 1.2])
        with col_bot_act1:
            if st.button("⏩ Next Questions (New 10 Set)", type="primary", use_container_width=True, key="exam_next_set_bottom_btn"):
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

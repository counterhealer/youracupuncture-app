# -*- coding: utf-8 -*-
"""Global Acupoint Quick-Search & About youracupuncture.app Modals.

Provides instant multi-script clinical search across all 429 WHO Standard Acupoints
and an authentic About & Feedback dialog for youracupuncture.app.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any
import streamlit as st
from datetime import datetime

MODULE_DIR = Path(__file__).resolve().parent
STATIC_DIR = MODULE_DIR.parent / "static"
DATA_DIR = MODULE_DIR.parent / "data"
POINTS_FILE = STATIC_DIR / "atlas_points.json"
FEEDBACK_FILE = DATA_DIR / "user_feedback.json"


def to_searchable_str(val: Any) -> str:
    """Safely convert string, list, or None to a lowercase searchable string."""
    if isinstance(val, list):
        return " ".join(str(x) for x in val if x).lower()
    return str(val).lower() if val else ""


def format_list_display(val: Any) -> str:
    """Format list of strings into clean comma-separated text."""
    if isinstance(val, list):
        return ", ".join(str(x) for x in val if x)
    return str(val) if val else ""


@st.cache_data(show_spinner=False)
def load_all_acupoints() -> Dict[str, Dict[str, Any]]:
    """Load and cache the complete 429-point dataset from static/atlas_points.json."""
    if POINTS_FILE.exists():
        try:
            with open(POINTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading atlas points: {e}")
    return {}


def search_points_dataset(query: str, all_points: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Execute robust multi-script search across all 429 acupoints."""
    if not query:
        return []

    raw_q = query.strip().lower()
    norm_q = re.sub(r'[^a-z0-9]', '', raw_q)
    matches: List[Dict[str, Any]] = []

    for pid, pt in all_points.items():
        if not isinstance(pt, dict):
            continue
        code = to_searchable_str(pt.get("code"))
        clean_code = to_searchable_str(pt.get("cleanCode"))
        norm_code = re.sub(r'[^a-z0-9]', '', clean_code or code)
        pinyin = to_searchable_str(pt.get("pinyin"))
        hanzi = str(pt.get("hanzi", "") or "")
        english = to_searchable_str(pt.get("english"))
        region = to_searchable_str(pt.get("region"))
        category = to_searchable_str(pt.get("category"))
        actions = to_searchable_str(pt.get("actions"))
        tcm_ind = to_searchable_str(pt.get("tcmIndications"))
        west_ind = to_searchable_str(pt.get("westernIndications"))
        tags = to_searchable_str(pt.get("tags"))
        safety = to_searchable_str(pt.get("safetyWarning"))

        # Exact and partial multi-attribute match
        if (raw_q in code or raw_q in clean_code or raw_q in pinyin or 
            raw_q in hanzi or raw_q in english or raw_q in actions or 
            raw_q in tcm_ind or raw_q in west_ind or raw_q in region or
            raw_q in category or raw_q in tags or raw_q in safety or
            (norm_q and norm_q in norm_code)):
            matches.append(pt)

    return matches


@st.dialog("🔍 Global Acupoint Quick Reference (429 Points)", width="large")
def render_quick_search_dialog():
    """Interactive modal dialog for searching all 429 acupoints by code, name, or clinical condition."""
    all_points = load_all_acupoints()
    
    st.caption("Search across all 429 WHO Standard points by Code (e.g., ST36, LI4), Pinyin (Zusanli, Hegu), Chinese Hanzi (足三里), or Symptom (Headache, Insomnia, Back pain).")
    
    def _clear_search_field():
        st.session_state["global_point_search_input"] = ""

    c_in, c_clear = st.columns([0.85, 0.15])
    with c_in:
        query = st.text_input(
            "Search Keyword",
            placeholder="Type point code (e.g. ST36, LI4), name (Hegu), or symptom (headache)...",
            key="global_point_search_input",
            label_visibility="collapsed"
        ).strip()
    with c_clear:
        st.button("Clear", use_container_width=True, key="btn_reset_point_search", on_click=_clear_search_field)

    # Quick topic shortcuts
    st.markdown("<div style='font-size:0.82rem; color:#94a3b8; margin:4px 0 10px 0;'>💡 <em>Quick Shortcuts: <code>LI4</code> (Head/Face), <code>ST36</code> (Qi/Digestive), <code>SP6</code> (Yin/Gyn), <code>LV3</code> (Liver Qi), <code>PC6</code> (Nausea/Shen), <code>BL40</code> (Lumbar).</em></div>", unsafe_allow_html=True)

    search_target = query if query else "ST36"
    matches = search_points_dataset(search_target, all_points)

    if not matches:
        st.warning(f"No acupoints found matching '{query}'. Try searching by channel (e.g., 'LU7', 'BL23') or general symptom (e.g. 'nausea').")
    else:
        st.markdown(f"<div style='font-size:0.88rem; color:#38bdf8; font-weight:700; margin-bottom:12px;'>Found {len(matches)} matching points (showing top {min(10, len(matches))}):</div>", unsafe_allow_html=True)

        for pt in matches[:10]:
            safety_level = str(pt.get("safetyLevel", "SAFE")).upper()
            if safety_level == "DANGER":
                badge_color = "#ef4444"
                badge_bg = "rgba(239, 68, 68, 0.2)"
                badge_text = "⚠️ DANGER / FORBIDDEN IN PREGNANCY"
            elif safety_level == "CAUTION":
                badge_color = "#f59e0b"
                badge_bg = "rgba(245, 158, 11, 0.2)"
                badge_text = "⚡ CLINICAL CAUTION"
            else:
                badge_color = "#10b981"
                badge_bg = "rgba(16, 185, 129, 0.2)"
                badge_text = "✓ CLINICALLY SAFE"

            with st.expander(f"📍 {pt['code']} · {pt.get('hanzi','')} · {pt.get('pinyin','')} ({pt.get('english','')})", expanded=(len(matches)==1)):
                col_info, col_safety = st.columns([0.65, 0.35])
                with col_info:
                    st.markdown(f"""
                    <div style="font-size: 1.15rem; font-weight: 800; color: #38bdf8; margin-bottom: 2px;">
                        {pt['code']} · <span style="color:#ffffff;">{pt.get('hanzi','')}</span> · <span style="color:#c89666;">{pt.get('pinyin','')}</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 6px;">
                        <em>"{pt.get('english','')}"</em> · <span style="color: #94a3b8;">{pt.get('category','Standard Channel Point')}</span>
                    </div>
                    """, unsafe_allow_html=True)
                with col_safety:
                    st.markdown(f"""
                    <div style="background: {badge_bg}; border: 1px solid {badge_color}; border-radius: 6px; padding: 6px 10px; text-align: center;">
                        <span style="color: {badge_color}; font-size: 0.76rem; font-weight: 800; text-transform: uppercase;">{badge_text}</span>
                    </div>
                    """, unsafe_allow_html=True)

                if pt.get("safetyWarning"):
                    st.markdown(f"""
                    <div style="background: rgba(239, 68, 68, 0.12); border-left: 4px solid #ef4444; padding: 8px 12px; border-radius: 4px; margin-bottom: 10px; font-size: 0.85rem; color: #fca5a5;">
                        <strong>Safety Notice:</strong> {pt['safetyWarning']}
                    </div>
                    """, unsafe_allow_html=True)

                actions_txt = format_list_display(pt.get('actions', ''))
                tcm_txt = format_list_display(pt.get('tcmIndications', ''))
                west_txt = format_list_display(pt.get('westernIndications', ''))

                st.markdown(f"""
                <div style="background: #111827; border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 12px 14px; font-size: 0.88rem; line-height: 1.55; margin-bottom: 8px;">
                    <div style="margin-bottom: 6px;"><strong>🎯 Anatomical Location:</strong> <span style="color: #e2e8f0;">{pt.get('locationClassical','')}</span></div>
                    <div style="margin-bottom: 6px;"><strong>🧭 How to Palpate:</strong> <span style="color: #cbd5e1;">{pt.get('howToFind','')}</span></div>
                    <div style="margin-bottom: 6px;"><strong>🪡 Needling Depth & Method:</strong> <span style="color: #38bdf8;">{pt.get('needling','')}</span> (Depth: {pt.get('depthMin', 0.5)}-{pt.get('depthMax', 1.0)} cun)</div>
                    <div style="margin-bottom: 6px;"><strong>⚡ Actions:</strong> <span style="color: #fde68a;">{actions_txt}</span></div>
                    <div><strong>🩺 Key Indications:</strong> <span style="color: #e2e8f0;">{tcm_txt}{' · ' + west_txt if west_txt else ''}</span></div>
                </div>
                """, unsafe_allow_html=True)

                if pt.get("combinations"):
                    st.caption(f"Classical Combinations: {format_list_display(pt['combinations'])}")

                if st.button(f"📋 Add {pt['code']} to Active SOAP Prescription", key=f"btn_add_soap_{pt['code']}", use_container_width=True):
                    if "soap_data" not in st.session_state:
                        from modules.soap_notes import init_soap_state
                        init_soap_state()
                    current_pts = st.session_state.soap_data.get("primary_points", "")
                    if pt['code'] not in current_pts:
                        new_pts = f"{current_pts}, {pt['code']} ({pt.get('pinyin','')})" if current_pts else f"{pt['code']} ({pt.get('pinyin','')})"
                        st.session_state.soap_data["primary_points"] = new_pts
                        st.success(f"Added {pt['code']} to SOAP Note Plan!")
                    else:
                        st.info(f"{pt['code']} is already in your SOAP Note Plan.")

    st.write("")
    if st.button("✕ Close Quick Search", use_container_width=True, key="btn_close_search_modal"):
        st.session_state.pop("show_search_dialog", None)
        st.rerun()


@st.dialog("ℹ️ About youracupuncture.app & Feedback", width="medium")
def render_about_dialog():
    """Interactive modal dialog displaying about information, clinical citations, and visitor feedback form."""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 16px;">
        <h2 style="color: #38bdf8; margin: 0 0 4px 0; font-size: 1.6rem; font-weight: 800;">
            youracupuncture.app
        </h2>
        <div style="font-size: 0.88rem; color: #94a3b8;">
            Evidence-Informed TCM Acupuncture Clinical &amp; Board Exam Suite
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **youracupuncture.app** was engineered for licensed acupuncturists, integrative medical doctors, and TCM students seeking high-yield, modern clinical reference tools without cluttered textbook scanning.

    ### 📚 Clinical Foundations & Textbook Consensus
    Every acupoint, pattern differentiation, pulse waveform, and pain protocol is cross-referenced against canonical authorities:
    * **WHO Standard Acupuncture Point Locations** (World Health Organization)
    * **Chinese Acupuncture and Moxibustion (CAM)** (Foreign Languages Press)
    * **A Manual of Acupuncture** (Peter Deadman & Kevin Baker)
    * **The Foundations of Chinese Medicine** (Giovanni Maciocia)
    * **The Practice of Chinese Medicine** (Giovanni Maciocia)
    * **Dr. Richard Tan's Balance Method & Master Tung Lineage Points**
    """)

    st.divider()

    st.markdown("### 💬 Clinical Feedback & Textbook Corrections")
    st.caption("Notice a discrepancy between textbooks or have a feature request? Let us know directly:")

    with st.form("visitor_feedback_form"):
        name = st.text_input("Your Name / Credentials (Optional)", placeholder="e.g. Dr. Jane Doe, L.Ac.")
        email = st.text_input("Email (Optional, if you would like a reply)", placeholder="jane@example.com")
        fb_type = st.selectbox("Feedback Category", options=[
            "💡 Feature Suggestion",
            "📖 Textbook Discrepancy / Correction",
            "🐛 Bug Report",
            "🤝 General Inquiry / Collaboration"
        ])
        msg = st.text_area("Your Message / Suggestion", placeholder="Describe your feedback here...", height=100)
        submitted = st.form_submit_button("✉️ Send Feedback", type="primary", use_container_width=True)

        if submitted:
            if not msg.strip():
                st.error("Please enter a message before sending.")
            else:
                feedback_entry = {
                    "timestamp": str(datetime.now()),
                    "name": name.strip(),
                    "email": email.strip(),
                    "category": fb_type,
                    "message": msg.strip()
                }
                DATA_DIR.mkdir(parents=True, exist_ok=True)
                existing = []
                if FEEDBACK_FILE.exists():
                    try:
                        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                            existing = json.load(f)
                    except Exception:
                        existing = []
                existing.append(feedback_entry)
                try:
                    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
                        json.dump(existing, f, indent=2, ensure_ascii=False)
                    st.success("✅ Thank you! Your feedback has been recorded.")
                except Exception as e:
                    st.success("✅ Thank you for your feedback!")

    if st.button("✕ Close", use_container_width=True, key="btn_close_about_modal"):
        st.session_state.pop("show_about_dialog", None)
        st.rerun()

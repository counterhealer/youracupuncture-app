"""Acupuncture Study & Clinical Case Review App.

A clean, mobile-first Streamlit application for reviewing acupuncture, cross-referencing
competing textbooks (CAM, Deadman, Maciocia), practicing interactive flashcards
(with NotebookLM-style click-to-flip cards), and simulating clinical patient cases
with multiple choice and open diagnostic modes.
All acupuncture points feature bilingual nomenclature (Code, Pinyin, Hanzi, English).
"""

import os
import random
import streamlit as st
from pathlib import Path
from typing import Optional

# Local modules
from modules.config_manager import get_setting, save_setting, remove_setting
from modules.tcm_points import get_point_bilingual_name, format_point_bilingual
from modules.rag_engine import (
    BASE_DIR,
    MATERIALS_DIR,
    DATA_DIR,
    is_index_built,
    get_indexed_files_info,
    build_or_load_index,
    add_uploaded_file,
    query_textbooks,
    retrieve_context,
    get_vector_index
)
from modules.flashcards import (
    init_db,
    get_flashcards,
    update_card_mastery,
    generate_synthesized_flashcard,
    get_flashcard_stats,
    delete_flashcard,
    FLASHCARD_CATEGORIES
)
from modules.diagnostics import (
    get_all_cases,
    get_case_by_id,
    grade_clinical_case,
    grade_multiple_choice,
    get_case_history
)
from modules.atlas import generate_atlas_html
from modules.concepts import render_concepts_tab
from modules.exam_bank import render_practice_exam_tab
from modules.internal_diagnostics import render_internal_diagnostics_tab
from modules.pain_map import render_pain_map_tab
from modules.point_pairs import render_point_pairs_tab
from modules.tongue_pulse_atlas import render_tongue_pulse_atlas_tab
from modules.soap_notes import render_soap_notes_tab
from modules.study_guides import render_study_guides_tab
from modules.global_search import render_quick_search_dialog, render_about_dialog


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Streamlit App Configuration (Responsive Desktop & Mobile)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="youracupuncture.app — TCM Clinical & Study Suite",
    page_icon="🪡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize SQLite database
init_db()

# Desktop-Optimized & Mobile-Responsive CSS Injection
st.markdown("""
<style>
    /* Hide Streamlit default chrome & deploy buttons */
    #MainMenu { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }
    .stDeployButton { display: none !important; }

    /* Completely hide sidebar and all sidebar expand/collapse controls */
    [data-testid="stSidebar"],
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Disable default streamlit transparent header bar so it never intercepts clicks */
    header[data-testid="stHeader"] {
        display: none !important;
        height: 0px !important;
        pointer-events: none !important;
        visibility: hidden !important;
        z-index: -1 !important;
    }

    /* ==========================================================================
       DESIGN SYSTEM PALETTE: CERULEAN BLUE, FAWN & VIOLET BLUE
       ========================================================================== */
    :root {
        --cerulean: #007ba7;
        --cerulean-deep: #005a7a;
        --cerulean-light: #e0f2fe;
        --cerulean-subtle: #f0f9ff;
        
        --fawn: #c89666;
        --fawn-deep: #8c5e35;
        --fawn-light: #faf6f0;
        --fawn-border: #e8ded2;
        --fawn-badge: #d4a373;

        --violet-blue: #484eb2;
        --violet-blue-deep: #32367d;
        --violet-blue-light: #eef0fb;
        --violet-blue-subtle: #f6f7fd;
    }

    /* Entire website atmosphere: Warm luxury linen/fawn canvas */
    .stApp {
        background-color: #fbf9f6 !important;
        color: #0f172a !important;
    }
    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #0b0f19 !important;
            color: #f8fafc !important;
        }
    }

    /* Responsive viewport container */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 3.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1560px !important;
        margin: 0 auto !important;
    }
    
    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
            max-width: 100% !important;
        }
    }

    /* Top Navigation Row - Clean bar running across the top */
    div[data-testid="stHorizontalBlock"]:has(.top-nav-brand) {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 1.5px solid var(--fawn-border) !important;
        border-radius: 0 !important;
        padding: 4px 0 16px 0 !important;
        margin-bottom: 24px !important;
        box-shadow: none !important;
        position: relative !important;
        z-index: 10 !important;
        width: 100% !important;
    }
    @media (prefers-color-scheme: dark) {
        div[data-testid="stHorizontalBlock"]:has(.top-nav-brand) {
            background: transparent !important;
            border-bottom-color: #1f2937 !important;
            box-shadow: none !important;
        }
    }

    div[data-testid="stHorizontalBlock"]:has(.top-nav-brand) > div[data-testid="column"]:first-child {
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 44px !important;
    }

    div[data-testid="stHorizontalBlock"]:has(.top-nav-brand) > div[data-testid="column"]:last-child {
        flex: 1 1 auto !important;
        width: auto !important;
    }

    /* Clean Modern Brand Logo */
    .top-nav-brand {
        display: inline-flex !important;
        align-items: center !important;
        gap: 12px !important;
        user-select: none !important;
        text-decoration: none !important;
        padding: 2px 0 !important;
    }

    .brand-logo-mark {
        flex-shrink: 0 !important;
        box-shadow: 0 3px 10px rgba(0, 123, 167, 0.22) !important;
        border-radius: 10px !important;
    }

    .brand-text-block {
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
    }

    .brand-title-main {
        font-size: 1.25rem !important;
        font-weight: 900 !important;
        letter-spacing: 0.08em !important;
        color: #0f172a !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    @media (prefers-color-scheme: dark) {
        .brand-title-main {
            color: #f8fafc !important;
        }
    }

    .brand-badge-pill {
        font-size: 0.68rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        background: #faf6f0 !important;
        color: #8c5e35 !important;
        border: 1px solid #e8ded2 !important;
        padding: 2px 8px !important;
        border-radius: 6px !important;
    }
    @media (prefers-color-scheme: dark) {
        .brand-badge-pill {
            background: #231e18 !important;
            color: #deb887 !important;
            border-color: #4a3b2c !important;
        }
    }
    
    /* Seamless iframe container for Acupuncture Atlas & dynamic embeds */
    div[data-testid="stCustomComponentV1"],
    div[data-testid="stIFrame"],
    div:has(> iframe.stIFrame),
    div:has(> iframe[data-testid="stIFrame"]) {
        width: 100% !important;
        height: auto !important;
        min-height: 0px !important;
        overflow: visible !important;
    }
    div[data-testid="stCustomComponentV1"] iframe,
    iframe[data-testid="stIFrame"],
    iframe.stIFrame {
        width: 100% !important;
        border: none !important;
        display: block !important;
    }
    iframe[height="0"] {
        display: none !important;
        height: 0px !important;
        min-height: 0px !important;
    }
    div:has(> iframe[height="0"]) {
        display: none !important;
        height: 0px !important;
        min-height: 0px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Column boundaries to prevent any child element from forcing horizontal expansion */
    [data-testid="column"] {
        min-width: 0 !important;
    }

    /* Alert boxes (Blue Chief Complaint box, warnings, successes) wrap text properly */
    div[data-testid="stAlert"] {
        overflow-wrap: break-word !important;
        word-break: break-word !important;
        white-space: normal !important;
    }
    div[data-testid="stAlert"] div[data-testid="stMarkdownContainer"] p {
        white-space: normal !important;
        overflow-wrap: break-word !important;
        word-break: break-word !important;
        line-height: 1.55 !important;
    }
    
    /* --------------------------------------------------------------------------
       1. MAIN TOP NAVIGATION (2-Tier Core Pillars & Sub-Navigation Toolbar)
       -------------------------------------------------------------------------- */
    .st-key-main_pillar_control,
    .st-key-main_pillar_control > div,
    div[class*="st-key-sub_nav_"],
    div[class*="st-key-sub_nav_"] > div,
    .st-key-main_nav_seg_control,
    .st-key-main_nav_seg_control > div,
    .st-key-main_nav_radio,
    .st-key-main_nav_radio > div {
        display: flex !important;
        justify-content: flex-end !important;
        width: 100% !important;
    }

    /* Native Segmented Control Buttons (ButtonGroup) */
    div[data-testid="stButtonGroup"] {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: flex-end !important;
        background-color: var(--fawn-light) !important;
        border: 1.5px solid var(--fawn-border) !important;
        border-radius: 12px !important;
        padding: 3px !important;
        gap: 3px !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.03) !important;
    }
    @media (prefers-color-scheme: dark) {
        div[data-testid="stButtonGroup"] {
            background-color: #111827 !important;
            border-color: #1f2937 !important;
        }
    }

    div[data-testid="stButtonGroup"] button {
        border: 1px solid transparent !important;
        border-radius: 8px !important;
        padding: 7px 16px !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        color: #475569 !important;
        background: transparent !important;
        transition: all 0.16s ease !important;
        cursor: pointer !important;
        line-height: 1.4 !important;
        min-height: 36px !important;
    }

    div[data-testid="stButtonGroup"] button:hover {
        color: var(--cerulean) !important;
        background: #ffffff !important;
        border-color: var(--fawn-border) !important;
    }

    /* Active Segmented Button - Vibrant Cerulean Blue */
    div[data-testid="stButtonGroup"] button[aria-checked="true"],
    div[data-testid="stButtonGroup"] button[data-checked="true"],
    div[data-testid="stButtonGroup"] button.active {
        background: var(--cerulean) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid var(--cerulean-deep) !important;
        box-shadow: 0 2px 8px rgba(0, 123, 167, 0.35) !important;
    }
    @media (prefers-color-scheme: dark) {
        div[data-testid="stButtonGroup"] button[aria-checked="true"],
        div[data-testid="stButtonGroup"] button[data-checked="true"] {
            background: #0284c7 !important;
            color: #ffffff !important;
            border-color: #0369a1 !important;
        }
    }

    /* Row 2: Sub-Navigation Toolbar Customization (Sleeker Pill Design) */
    div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] {
        background-color: rgba(241, 245, 249, 0.9) !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 10px !important;
        padding: 2px !important;
        gap: 2px !important;
        margin-top: 3px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    }
    @media (prefers-color-scheme: dark) {
        div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] {
            background-color: #172033 !important;
            border-color: #334155 !important;
        }
    }
    div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button {
        padding: 5px 14px !important;
        font-size: 0.82rem !important;
        min-height: 31px !important;
        border-radius: 7px !important;
        font-weight: 600 !important;
        color: #64748b !important;
    }
    div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button:hover {
        color: var(--violet-blue) !important;
        background: #ffffff !important;
    }
    div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button[aria-checked="true"],
    div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button[data-checked="true"] {
        background: var(--violet-blue) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid var(--violet-blue-deep) !important;
        box-shadow: 0 2px 6px rgba(72, 78, 178, 0.3) !important;
    }
    @media (prefers-color-scheme: dark) {
        div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button[aria-checked="true"],
        div[class*="st-key-sub_nav_"] div[data-testid="stButtonGroup"] button[data-checked="true"] {
            background: #6366f1 !important;
            border-color: #4f46e5 !important;
            color: #ffffff !important;
        }
    }

    div[data-testid="stButtonGroup"] button div[data-testid="stMarkdownContainer"] p {
        margin: 0 !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        color: inherit !important;
        white-space: nowrap !important;
    }

    /* Fallback / Radio segment support without disabling click event dispatch */
    .st-key-main_nav_radio div[role="radiogroup"],
    div[role="radiogroup"][aria-label="Navigation"] {
        display: inline-flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        justify-content: flex-end !important;
        gap: 4px !important;
        background-color: var(--fawn-light) !important;
        padding: 4px !important;
        border-radius: 12px !important;
        border: 1.5px solid var(--fawn-border) !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.03) !important;
        margin: 0 !important;
        width: auto !important;
    }

    .st-key-main_nav_radio input[type="radio"] {
        position: absolute !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        pointer-events: none !important;
    }
    .st-key-main_nav_radio label > div:first-child:not([data-testid="stMarkdownContainer"]) {
        display: none !important;
    }

    .st-key-main_nav_radio label,
    div[role="radiogroup"][aria-label="Navigation"] label {
        display: inline-flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 7px 15px !important;
        border-radius: 8px !important;
        border: 1px solid transparent !important;
        cursor: pointer !important;
        color: #475569 !important;
        background: transparent !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
        transition: all 0.16s ease !important;
        user-select: none !important;
        margin: 0 !important;
        white-space: nowrap !important;
    }

    .st-key-main_nav_radio label:hover,
    div[role="radiogroup"][aria-label="Navigation"] label:hover {
        color: var(--cerulean) !important;
        background: #ffffff !important;
        border-color: var(--fawn-border) !important;
    }

    .st-key-main_nav_radio label:has(input:checked),
    div[role="radiogroup"][aria-label="Navigation"] label:has(input:checked) {
        background: var(--cerulean) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: 1px solid var(--cerulean-deep) !important;
        box-shadow: 0 2px 8px rgba(0, 123, 167, 0.35) !important;
    }

    .st-key-main_nav_radio label div[data-testid="stMarkdownContainer"] p,
    div[role="radiogroup"][aria-label="Navigation"] label div[data-testid="stMarkdownContainer"] p {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 0.88rem !important;
        font-weight: inherit !important;
        color: inherit !important;
        white-space: nowrap !important;
    }

    @media (max-width: 960px) {
        div[data-testid="stHorizontalBlock"]:has(.top-nav-brand) {
            flex-direction: column !important;
            align-items: flex-start !important;
            gap: 12px !important;
            padding: 4px 0 14px 0 !important;
        }
        .st-key-main_pillar_control,
        .st-key-main_pillar_control > div,
        div[class*="st-key-sub_nav_"],
        div[class*="st-key-sub_nav_"] > div,
        .st-key-main_nav_seg_control,
        .st-key-main_nav_seg_control > div,
        .st-key-main_nav_radio,
        .st-key-main_nav_radio > div,
        .st-key-main_nav_radio div[role="radiogroup"] {
            justify-content: flex-start !important;
            width: 100% !important;
        }
        .st-key-main_nav_radio label,
        div[role="radiogroup"][aria-label="Navigation"] label {
            padding: 6px 12px !important;
            font-size: 0.82rem !important;
        }
        .st-key-main_nav_radio label div[data-testid="stMarkdownContainer"] p,
        div[role="radiogroup"][aria-label="Navigation"] label div[data-testid="stMarkdownContainer"] p {
            font-size: 0.82rem !important;
        }
    }

    /* --------------------------------------------------------------------------
       2. MODE TOGGLES (Flashcard Mode & Case Simulator Mode)
       -------------------------------------------------------------------------- */
    div[role="radiogroup"][aria-label="Flashcard Mode"],
    div[role="radiogroup"][aria-label="Simulator Mode"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
        background: #f1f5f9 !important;
        padding: 4px !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        margin-bottom: 14px !important;
    }
    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label="Flashcard Mode"],
        div[role="radiogroup"][aria-label="Simulator Mode"] {
            background: #0f172a !important;
            border-color: #1e293b !important;
        }
    }
    div[role="radiogroup"][aria-label="Flashcard Mode"] label,
    div[role="radiogroup"][aria-label="Simulator Mode"] label {
        display: inline-flex !important;
        flex-direction: row !important;
        align-items: center !important;
        padding: 7px 14px !important;
        border-radius: 8px !important;
        border: 1px solid transparent !important;
        cursor: pointer !important;
        font-size: 0.88rem !important;
        font-weight: 600 !important;
        color: #475569 !important;
        background: transparent !important;
        transition: all 0.15s ease !important;
    }
    div[role="radiogroup"][aria-label="Flashcard Mode"] label:has(input:checked),
    div[role="radiogroup"][aria-label="Simulator Mode"] label:has(input:checked) {
        background: #ffffff !important;
        color: var(--cerulean) !important;
        font-weight: 700 !important;
        border-color: #cbd5e1 !important;
        box-shadow: 0 2px 6px rgba(0, 123, 167, 0.08) !important;
    }
    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label="Flashcard Mode"] label:has(input:checked),
        div[role="radiogroup"][aria-label="Simulator Mode"] label:has(input:checked) {
            background: #1e293b !important;
            color: #38bdf8 !important;
            border-color: #334155 !important;
        }
    }
    div[role="radiogroup"][aria-label="Flashcard Mode"] label > div:first-child:not([data-testid="stMarkdownContainer"]),
    div[role="radiogroup"][aria-label="Simulator Mode"] label > div:first-child:not([data-testid="stMarkdownContainer"]) {
        display: none !important;
    }
    div[role="radiogroup"][aria-label="Flashcard Mode"] input[type="radio"],
    div[role="radiogroup"][aria-label="Simulator Mode"] input[type="radio"] {
        display: none !important;
    }
    div[role="radiogroup"][aria-label="Flashcard Mode"] label div[data-testid="stMarkdownContainer"] p,
    div[role="radiogroup"][aria-label="Simulator Mode"] label div[data-testid="stMarkdownContainer"] p {
        margin: 0 !important;
        white-space: nowrap !important;
    }

    /* --------------------------------------------------------------------------
       3. CASE SIMULATOR MCQ QUESTIONS & OPTIONS (Violet Blue Theme)
       -------------------------------------------------------------------------- */
    div[role="radiogroup"][aria-label^="Options for"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
        width: 100% !important;
        background: transparent !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        margin-bottom: 12px !important;
    }

    div[role="radiogroup"][aria-label^="Options for"] label {
        display: flex !important;
        flex-direction: row !important;
        align-items: flex-start !important;
        gap: 12px !important;
        padding: 11px 16px !important;
        border-radius: 10px !important;
        border: 1.5px solid #e2e8f0 !important;
        background: #ffffff !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02) !important;
    }

    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label^="Options for"] label {
            background: #1e293b !important;
            border-color: #334155 !important;
        }
    }

    div[role="radiogroup"][aria-label^="Options for"] label > div:first-child {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-top: 3px !important;
        flex-shrink: 0 !important;
    }

    div[role="radiogroup"][aria-label^="Options for"] label:hover {
        background: #f8fafc !important;
        border-color: #94a3b8 !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
        transform: translateY(-1px) !important;
    }

    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label^="Options for"] label:hover {
            background: #334155 !important;
            border-color: #64748b !important;
        }
    }

    /* Selected option card state - Violet Blue Accent */
    div[role="radiogroup"][aria-label^="Options for"] label:has(input:checked) {
        background: var(--violet-blue-light) !important;
        border-color: var(--violet-blue) !important;
        box-shadow: 0 0 0 1.5px var(--violet-blue), 0 2px 8px rgba(72, 78, 178, 0.12) !important;
        transform: translateY(0) !important;
    }

    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label^="Options for"] label:has(input:checked) {
            background: #181938 !important;
            border-color: #7b80d9 !important;
            box-shadow: 0 0 0 1.5px #7b80d9, 0 2px 8px rgba(0, 0, 0, 0.3) !important;
        }
    }

    div[role="radiogroup"][aria-label^="Options for"] label div[data-testid="stMarkdownContainer"] {
        flex: 1 1 auto !important;
        min-width: 0 !important;
        overflow-wrap: break-word !important;
        word-break: break-word !important;
    }

    div[role="radiogroup"][aria-label^="Options for"] label div[data-testid="stMarkdownContainer"] p {
        white-space: normal !important;
        overflow-wrap: break-word !important;
        word-break: break-word !important;
        line-height: 1.55 !important;
        font-size: 0.92rem !important;
        color: #1e293b !important;
        margin: 0 !important;
    }

    @media (prefers-color-scheme: dark) {
        div[role="radiogroup"][aria-label^="Options for"] label div[data-testid="stMarkdownContainer"] p {
            color: #f1f5f9 !important;
        }
    }
    
    /* Touch-friendly buttons - Cerulean Blue Primary */
    div.stButton > button {
        min-height: 44px;
        font-size: 0.95rem;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.5rem 1.2rem;
        transition: all 0.15s ease-in-out;
        width: 100%;
        touch-action: manipulation;
    }
    
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--cerulean) 0%, #00668a 100%);
        color: white;
        border: none;
        box-shadow: 0 2px 6px rgba(0, 123, 167, 0.25);
    }
    div.stButton > button[kind="primary"]:hover {
        background: var(--cerulean-deep);
        box-shadow: 0 4px 12px rgba(0, 123, 167, 0.35);
        transform: translateY(-1px);
    }
    
    /* NotebookLM Flashcard & Swiss Card Design */
    .nlm-card {
        background-color: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 16px;
        padding: 22px 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        margin-bottom: 0.8rem;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .nlm-card:hover {
        box-shadow: 0 8px 24px rgba(0, 123, 167, 0.09);
        border-color: var(--cerulean);
    }
    
    @media (prefers-color-scheme: dark) {
        .nlm-card {
            background-color: #1e293b;
            border-color: #475569;
            color: #f8fafc;
        }
    }

    /* Native Interactive Click-to-Flip Flashcard */
    details.flashcard-interactive {
        width: 100%;
        margin-bottom: 0.8rem;
    }
    details.flashcard-interactive summary {
        list-style: none !important;
        list-style-type: none !important;
        cursor: pointer;
        outline: none;
        user-select: text;
        -webkit-tap-highlight-color: transparent;
    }
    details.flashcard-interactive summary::-webkit-details-marker {
        display: none !important;
    }
    details.flashcard-interactive summary::marker {
        display: none !important;
    }

    details.flashcard-interactive .fc-front-view {
        display: block;
        background-color: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 16px;
        padding: 24px 22px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    details.flashcard-interactive .fc-front-view:hover {
        border-color: #007ba7;
        box-shadow: 0 8px 24px rgba(0, 123, 167, 0.12);
        transform: translateY(-1px);
    }

    details.flashcard-interactive .fc-back-view {
        display: none;
        background-color: #ffffff;
        border: 1.5px solid #007ba7;
        border-top: 5px solid #007ba7;
        border-radius: 16px;
        padding: 24px 22px;
        box-shadow: 0 6px 20px rgba(0, 123, 167, 0.14);
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    details.flashcard-interactive .fc-back-view:hover {
        box-shadow: 0 8px 26px rgba(0, 123, 167, 0.22);
        transform: translateY(-1px);
    }

    /* Flip between Front and Back when details is opened/closed */
    details.flashcard-interactive[open] .fc-front-view {
        display: none !important;
    }
    details.flashcard-interactive[open] .fc-back-view {
        display: block !important;
        animation: fcCardFadeIn 0.22s ease-out;
    }

    @keyframes fcCardFadeIn {
        from {
            opacity: 0.5;
            transform: scale(0.99);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    @media (prefers-color-scheme: dark) {
        details.flashcard-interactive .fc-front-view {
            background-color: #1e293b !important;
            border-color: #475569 !important;
            color: #f8fafc !important;
        }
        details.flashcard-interactive .fc-back-view {
            background-color: #1e293b !important;
            border-color: #007ba7 !important;
            color: #f8fafc !important;
        }
    }
    
    /* Variation & Discrepancy Callout - Fawn Warm Accent */
    .variation-callout {
        background-color: var(--fawn-light);
        border-left: 5px solid var(--fawn);
        border-radius: 12px;
        padding: 14px 16px;
        margin: 14px 0;
        color: #6e4522;
        border: 1px solid var(--fawn-border);
        border-left-width: 5px;
    }
    @media (prefers-color-scheme: dark) {
        .variation-callout {
            background-color: #231e18;
            color: #deb887;
            border-color: #4a3b2c;
            border-left-color: var(--fawn);
        }
    }
    
    /* Clinical EHR Patient Chart */
    .ehr-chart-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        padding-bottom: 10px;
        border-bottom: 1px solid #e2e8f0;
        flex-wrap: wrap;
        gap: 8px;
    }
    @media (prefers-color-scheme: dark) {
        .ehr-chart-header {
            border-bottom-color: #334155;
        }
    }
    .ehr-badge-id {
        font-family: ui-monospace, monospace;
        font-size: 0.75rem;
        font-weight: 800;
        background: var(--cerulean);
        color: white;
        padding: 2px 8px;
        border-radius: 6px;
    }
    .ehr-chief-complaint {
        background: var(--violet-blue-light);
        border-left: 4px solid var(--violet-blue);
        border-radius: 6px;
        padding: 10px 14px;
        margin: 10px 0;
        font-weight: 500;
        color: #1e2260;
    }
    .ehr-four-exams-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-top: 12px;
    }
    @media (max-width: 600px) {
        .ehr-four-exams-grid {
            grid-template-columns: 1fr;
        }
    }
    .ehr-exam-box {
        background: var(--fawn-light);
        border: 1px solid var(--fawn-border);
        border-radius: 8px;
        padding: 10px 12px;
    }
    @media (prefers-color-scheme: dark) {
        .ehr-chief-complaint {
            background: #181938;
            color: #d5d8f6;
            border-left-color: #7b80d9;
        }
        .ehr-exam-box {
            background: #1c1815;
            border-color: #3b322a;
        }
    }
    .ehr-exam-title {
        font-size: 0.76rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--fawn-deep);
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    @media (prefers-color-scheme: dark) {
        .ehr-exam-title {
            color: #deb887;
        }
    }

    /* Mobile font readability */
    @media (max-width: 640px) {
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        .stMarkdown p { font-size: 1rem !important; }
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Session State Management
# -----------------------------------------------------------------------------
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "card_flipped" not in st.session_state:
    st.session_state.card_flipped = False
if "selected_case_id" not in st.session_state:
    _all_c = get_all_cases()
    st.session_state.selected_case_id = random.choice([c["id"] for c in _all_c]) if _all_c else "CASE-001"
if "last_graded_result" not in st.session_state:
    st.session_state.last_graded_result = None
if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "shuffled_cards" not in st.session_state:
    st.session_state.shuffled_cards = []
if "prev_filter_selection" not in st.session_state:
    st.session_state.prev_filter_selection = None
if "mcq_answers" not in st.session_state:
    st.session_state.mcq_answers = {}


# -----------------------------------------------------------------------------
# Configuration, Provider & Credentials Resolution
# -----------------------------------------------------------------------------
saved_gemini_key = get_setting("GEMINI_API_KEY", "")
saved_openai_key = get_setting("OPENAI_API_KEY", "")
saved_provider_pref = get_setting("LAST_PROVIDER", "Google Gemini (Recommended)")

provider_options = [
    "Google Gemini (Recommended)",
    "Offline / Built-in TCM Engine",
    "OpenAI",
    "Ollama (Local)"
]

if "provider_choice" not in st.session_state:
    st.session_state.provider_choice = saved_provider_pref if saved_provider_pref in provider_options else "Google Gemini (Recommended)"

active_provider = st.session_state.provider_choice
api_key = None
engine_provider = "demo"
selected_model = None

if active_provider == "Google Gemini (Recommended)":
    if saved_gemini_key:
        api_key = saved_gemini_key
        engine_provider = "gemini"
elif active_provider == "OpenAI":
    if saved_openai_key:
        api_key = saved_openai_key
        engine_provider = "openai"
elif active_provider == "Ollama (Local)":
    engine_provider = "ollama"
else:
    engine_provider = "demo"

# Materials & indexing stats
files_info = get_indexed_files_info()
indexed_count = sum(1 for f in files_info if f["indexed"])
folders_map = {}
for f in files_info:
    folders_map.setdefault(f.get("folder", "Root"), []).append(f)

@st.cache_resource(show_spinner=False)
def load_shared_vector_index():
    """Keep vector index warm in memory across all user interactions."""
    return get_vector_index()


# -----------------------------------------------------------------------------
# Main Top Navbar & 2-Tier Pillar Navigation
# -----------------------------------------------------------------------------
PILLARS = [
    "🗺️ Visual Atlases",
    "🩺 Clinical Practice",
    "🎓 Study & Exam Prep",
    "⚙️ Progress & Settings"
]

PILLAR_SUBS = {
    "🗺️ Visual Atlases": [
        "Atlas",
        "Pain Map",
        "Tongue & Pulse",
        "Point Pairs"
    ],
    "🩺 Clinical Practice": [
        "Diagnostics",
        "Case Simulator",
        "SOAP Notes"
    ],
    "🎓 Study & Exam Prep": [
        "Practice Exam",
        "Flashcards",
        "Concepts",
        "Study Guides",
        "Cross-Reference"
    ],
    "⚙️ Progress & Settings": [
        "Progress & Settings"
    ]
}

# Reverse mapping for 1-click cross-tab redirections (e.g. from Diagnostics to SOAP Notes)
TOOL_TO_PILLAR = {
    "Atlas": "🗺️ Visual Atlases",
    "Acupuncture Atlas": "🗺️ Visual Atlases",
    "Pain Map": "🗺️ Visual Atlases",
    "Tongue & Pulse": "🗺️ Visual Atlases",
    "Point Pairs": "🗺️ Visual Atlases",
    "Diagnostics": "🩺 Clinical Practice",
    "Case Simulator": "🩺 Clinical Practice",
    "SOAP Notes": "🩺 Clinical Practice",
    "Practice Exam": "🎓 Study & Exam Prep",
    "Flashcards": "🎓 Study & Exam Prep",
    "Concepts": "🎓 Study & Exam Prep",
    "Study Guides": "🎓 Study & Exam Prep",
    "Cross-Reference": "🎓 Study & Exam Prep",
    "Progress & Settings": "⚙️ Progress & Settings",
    "Settings": "⚙️ Progress & Settings",
    "Progress": "⚙️ Progress & Settings"
}

# Handle browser URL query parameters for browser Back / Forward history & deep links
query_tool = st.query_params.get("tool")
if query_tool and query_tool in TOOL_TO_PILLAR:
    expected_pillar = TOOL_TO_PILLAR[query_tool]
    expected_sub = query_tool if query_tool != "Acupuncture Atlas" else "Atlas"
    if st.session_state.get("main_nav_radio") != expected_sub:
        st.session_state.main_pillar_control = expected_pillar
        st.session_state[f"sub_nav_{expected_pillar}"] = expected_sub

# Handle cross-tab redirections (from Diagnostics, Pain Map, etc.)
if "target_nav_tab" in st.session_state and st.session_state.target_nav_tab:
    target = st.session_state.target_nav_tab
    del st.session_state.target_nav_tab
    if target in TOOL_TO_PILLAR:
        target_pillar = TOOL_TO_PILLAR[target]
        target_sub = target if target != "Acupuncture Atlas" else "Atlas"
        st.session_state.main_pillar_control = target_pillar
        st.session_state[f"sub_nav_{target_pillar}"] = target_sub
        st.query_params["tool"] = target_sub

# Ensure valid initial pillar state
if "main_pillar_control" not in st.session_state or st.session_state.main_pillar_control not in PILLARS:
    st.session_state.main_pillar_control = PILLARS[0]

# Render Row 1: Brand (youracupuncture.app) + 4 Core Pillars + Quick Tools
col_brand, col_nav, col_tools = st.columns([0.22, 0.58, 0.20], vertical_alignment="center")

with col_brand:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-right: 8px;">
        <svg class="brand-logo-mark" width="34" height="34" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="40" height="40" rx="10" fill="url(#brandGrad)"/>
            <path d="M20 7V33" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
            <circle cx="20" cy="18" r="8" stroke="rgba(255,255,255,0.45)" stroke-width="1.6" stroke-dasharray="2.5 3"/>
            <circle cx="20" cy="18" r="4" fill="#C89666" stroke="#FFFFFF" stroke-width="1.8"/>
            <defs>
                <linearGradient id="brandGrad" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#007BA7"/>
                    <stop offset="100%" stop-color="#484EB2"/>
                </linearGradient>
            </defs>
        </svg>
        <div>
            <div style="font-weight: 800; font-size: 1.05rem; letter-spacing: -0.02em; color: #38bdf8; line-height: 1.1;">
                youracupuncture<span style="color: #c89666;">.app</span>
            </div>
            <div style="font-size: 0.66rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">
                Clinical &amp; Board Suite
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_nav:
    selected_pillar = st.segmented_control(
        "Core Pillars",
        options=PILLARS,
        required=True,
        key="main_pillar_control",
        label_visibility="collapsed"
    )

with col_tools:
    c_srch, c_abt = st.columns(2)
    with c_srch:
        if st.button("🔍 Search", use_container_width=True, key="top_bar_btn_search", help="Instant Acupoint Quick Reference (429 Points)"):
            render_quick_search_dialog()
    with c_abt:
        if st.button("ℹ️ About", use_container_width=True, key="top_bar_btn_about", help="About youracupuncture.app & Feedback"):
            render_about_dialog()

active_pillar = selected_pillar or st.session_state.main_pillar_control

# Render Row 2: Secondary Tool Navigation Bar (if pillar has multiple sub-tools)
sub_options = PILLAR_SUBS.get(active_pillar, [])
if len(sub_options) > 1:
    sub_key = f"sub_nav_{active_pillar}"
    if sub_key not in st.session_state or st.session_state[sub_key] not in sub_options:
        st.session_state[sub_key] = sub_options[0]

    _, col_sub = st.columns([0.22, 0.78], vertical_alignment="center")
    with col_sub:
        selected_sub = st.segmented_control(
            f"SubNav_{active_pillar}",
            options=sub_options,
            required=True,
            key=sub_key,
            label_visibility="collapsed"
        )
        nav_choice = selected_sub or st.session_state[sub_key]
else:
    nav_choice = sub_options[0] if sub_options else "Progress & Settings"

st.session_state.main_nav_radio = nav_choice

# Sync browser URL query parameter for browser Back / Forward history
if st.query_params.get("tool") != nav_choice:
    st.query_params["tool"] = nav_choice

# Reset parent window scroll position when switching tabs to eliminate empty gaps
if "prev_active_nav" not in st.session_state:
    st.session_state.prev_active_nav = nav_choice
elif st.session_state.prev_active_nav != nav_choice:
    st.session_state.prev_active_nav = nav_choice
    st.html("""
    <script>
        try {
            window.scrollTo(0, 0);
            const main = document.querySelector('section.main') || document.querySelector('.main') || document.documentElement;
            if (main) main.scrollTo(0, 0);
            if (window.parent) {
                window.parent.scrollTo(0, 0);
                const pmain = window.parent.document.querySelector('section.main') || window.parent.document.querySelector('.main') || window.parent.document.documentElement;
                if (pmain) pmain.scrollTo(0, 0);
            }
        } catch(e) {}
    </script>
    """, unsafe_allow_javascript=True)

st.write("")


# =============================================================================
# TAB 1: Cross-Reference & Study
# =============================================================================
if nav_choice == "Cross-Reference":
    st.subheader("Textbook Cross-Reference & Search")
    st.caption("Search acupoints across competing textbooks. Displays both Chinese (Pinyin / Hanzi) and English names.")
    
    # Pre-warm vector index in memory
    load_shared_vector_index()
    
    # Bilingual quick suggestion pills
    st.markdown("**Quick Topics:**")
    quick_cols = st.columns(4)
    if quick_cols[0].button("ST36 (Zusanli / 足三里)", use_container_width=True, key="quick_btn_st36"):
        st.session_state.search_query = "ST36 Zusanli needling depth and actions"
        st.session_state.run_cross_ref_search = True
    if quick_cols[1].button("LI4 (Hegu / 合谷)", use_container_width=True, key="quick_btn_li4"):
        st.session_state.search_query = "LI4 Hegu pregnancy contraindication"
        st.session_state.run_cross_ref_search = True
    if quick_cols[2].button("SP6 (Sanyinjiao / 三阴交)", use_container_width=True, key="quick_btn_sp6"):
        st.session_state.search_query = "SP6 Sanyinjiao indications and depth"
        st.session_state.run_cross_ref_search = True
    if quick_cols[3].button("BL1 (Jingming / 睛明)", use_container_width=True, key="quick_btn_bl1"):
        st.session_state.search_query = "BL1 Jingming needling technique precautions"
        st.session_state.run_cross_ref_search = True
        
    # Search Bar with Form to avoid unwanted rerun cycles
    with st.form("cross_ref_search_form", clear_on_submit=False):
        col_input, col_btn = st.columns([4, 1])
        with col_input:
            search_input = st.text_input(
                "Search Topic or Acupoint",
                value=st.session_state.get("search_query", ""),
                placeholder="e.g. ST36 depth, Four Gates, Liver Qi Stagnation...",
                label_visibility="collapsed"
            )
        with col_btn:
            search_submitted = st.form_submit_button("🔍 Search", type="primary", use_container_width=True)

    # Trigger search if button clicked or quick pill pressed
    should_run = search_submitted or st.session_state.get("run_cross_ref_search", False)
    if should_run:
        st.session_state.run_cross_ref_search = False
        target_query = search_input.strip() if search_submitted else st.session_state.get("search_query", "").strip()
        if target_query:
            st.session_state.search_query = target_query
            with st.spinner("Retrieving and cross-referencing textbook passages..."):
                results = query_textbooks(target_query, provider=engine_provider, api_key=api_key)
            st.session_state.last_cross_ref_result = results

    # Render results from session state
    if "last_cross_ref_result" in st.session_state and st.session_state.last_cross_ref_result:
        results = st.session_state.last_cross_ref_result
        
        # 1. High-Yield Variations Callout
        variations = results.get("variations", [])
        if variations:
            st.markdown("""
            <div class="variation-callout">
                <h4 style="margin: 0 0 8px 0; color: inherit;">⚠️ Cross-Textbook Discrepancies Detected</h4>
            """, unsafe_allow_html=True)
            for var in variations:
                st.markdown(f"**Topic:** {var['topic']}")
                st.markdown(f"- {format_point_bilingual(var['textbook_a'])}")
                st.markdown(f"- {format_point_bilingual(var['textbook_b'])}")
                st.markdown(f"**Clinical Significance:** *{format_point_bilingual(var['clinical_significance'])}*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # 2. Synthesized Knowledge Answer with Bilingual Formatting
        formatted_answer = format_point_bilingual(results.get("answer", ""))
        st.markdown(f"""
        <div class="nlm-card" style="border-top: 4px solid #484eb2; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; flex-wrap: wrap; gap: 8px;">
                <div style="font-size: 0.8rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #484eb2;">
                    Multi-Textbook Consensus · Evidence Synthesis
                </div>
                <div style="font-size: 0.72rem; font-weight: 600; color: #64748b; font-family: ui-monospace, monospace;">
                    CAM · Deadman · Maciocia
                </div>
            </div>
            <div style="font-size: 1.02rem; line-height: 1.65;">
                {formatted_answer}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 3. Source Passages Expander
        contexts = results.get("contexts", [])
        with st.expander(f"View {len(contexts)} Direct Textbook Excerpts"):
            for idx, ctx in enumerate(contexts, 1):
                st.markdown(f"**{idx}. Source: `{ctx['source']}`** (Page/Ref: {ctx['page']})")
                st.info(format_point_bilingual(ctx["text"]))


# =============================================================================
# TAB 2: Flashcards
# =============================================================================
elif nav_choice == "Flashcards":
    st.subheader("Interactive Flashcards")
    
    # Review vs Generator toggle
    mode = st.radio(
        "Flashcard Mode",
        options=["Review Deck", "Generate New Flashcard"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if mode == "Review Deck":
        stats = get_flashcard_stats()
        all_categories = stats["categories"]
        cat_counts = stats.get("category_counts", {})
        
        # Initialize checkbox states in session_state if not present
        for cat in all_categories:
            cb_key = f"cat_cb_{cat}"
            if cb_key not in st.session_state:
                st.session_state[cb_key] = True  # Checked by default
                
        # Multi-Category Checkbox Controls & Filters
        with st.container(border=True):
            f_hdr_col1, f_hdr_col2 = st.columns([1, 1])
            with f_hdr_col1:
                st.markdown("##### 🗂️ Categories to Study")
            with f_hdr_col2:
                selected_count = sum(1 for c in all_categories if st.session_state.get(f"cat_cb_{c}", True))
                st.caption(f"**{selected_count} of {len(all_categories)}** categories checked")

            # Checkboxes in 2 touch-friendly columns
            c_cols = st.columns(2)
            selected_categories = []
            half = (len(all_categories) + 1) // 2
            
            for col_idx, cat_group in enumerate([all_categories[:half], all_categories[half:]]):
                with c_cols[col_idx]:
                    for cat in cat_group:
                        cb_key = f"cat_cb_{cat}"
                        count_label = cat_counts.get(cat, 0)
                        checked = st.checkbox(
                            f"{cat} ({count_label})",
                            key=cb_key
                        )
                        if checked:
                            selected_categories.append(cat)

            st.write("")
            # Filters Row: Importance Tier & Mastery Level
            f_row1, f_row2 = st.columns(2)
            with f_row1:
                tier_filter = st.selectbox(
                    "Exam Importance Tier",
                    options=[
                        f"All Tiers ({stats['total']} cards)",
                        f"🔥 Tier 1: High Yield (Must-Know) ({stats.get('tier1', 0)})",
                        f"⭐ Tier 2: Core Clinical ({stats.get('tier2', 0)})",
                        f"💡 Tier 3: Foundation & Nuance ({stats.get('tier3', 0)})"
                    ]
                )
            with f_row2:
                mastery_filter = st.selectbox(
                    "Mastery Level",
                    options=["All Levels", "New (0)", "Learning (1-2)", "Mastered (3)"]
                )

            # Quick Action Buttons
            b_col1, b_col2, b_col3 = st.columns(3)
            with b_col1:
                if st.button("✓ Select All", use_container_width=True, key="btn_sel_all_cats"):
                    for cat in all_categories:
                        st.session_state[f"cat_cb_{cat}"] = True
                    st.rerun()
            with b_col2:
                if st.button("✗ Clear All", use_container_width=True, key="btn_clear_all_cats"):
                    for cat in all_categories:
                        st.session_state[f"cat_cb_{cat}"] = False
                    st.rerun()
            with b_col3:
                if st.button("🔀 Reshuffle", use_container_width=True, key="btn_reshuffle_deck"):
                    if st.session_state.get("shuffled_cards"):
                        random.shuffle(st.session_state.shuffled_cards)
                        st.session_state.card_index = 0
                        st.session_state.card_flipped = False
                        st.rerun()

        # Parse filter selections
        importance_val = None
        if "Tier 1" in tier_filter:
            importance_val = 1
        elif "Tier 2" in tier_filter:
            importance_val = 2
        elif "Tier 3" in tier_filter:
            importance_val = 3

        mastery_val = None
        if mastery_filter == "New (0)":
            mastery_val = 0
        elif mastery_filter == "Learning (1-2)":
            mastery_val = 1
        elif mastery_filter == "Mastered (3)":
            mastery_val = 3

        # Detect filter changes or fresh session, and load with randomized order
        current_selection_key = (
            tuple(sorted(selected_categories)),
            importance_val,
            mastery_val
        )

        if st.session_state.get("prev_filter_selection") != current_selection_key:
            if not selected_categories:
                st.session_state.shuffled_cards = []
            else:
                raw_cards = get_flashcards(
                    category=selected_categories,
                    mastery_level=mastery_val,
                    importance_level=importance_val
                )
                random.shuffle(raw_cards)
                st.session_state.shuffled_cards = raw_cards
            st.session_state.card_index = 0
            st.session_state.card_flipped = False
            st.session_state.prev_filter_selection = current_selection_key

        cards = st.session_state.get("shuffled_cards", [])

        if not selected_categories:
            st.warning("⚠️ No categories selected. Please check one or more categories above to study.")
            if st.button("✓ Select All Categories", type="primary", use_container_width=True):
                for cat in all_categories:
                    st.session_state[f"cat_cb_{cat}"] = True
                st.rerun()
        elif not cards:
            st.info("No flashcards match the selected filters. Try choosing 'All Tiers' or adjusting your mastery level.")
        else:
            if st.session_state.card_index >= len(cards):
                st.session_state.card_index = 0
            current_card = cards[st.session_state.card_index]
            
            # Progress indicator
            st.progress((st.session_state.card_index + 1) / len(cards))

            # Tier Badge & Label
            importance_tier = current_card.get("importance_level", 2)
            if importance_tier == 1:
                tier_badge = '<span style="font-size: 0.82rem; font-weight: 700; padding: 3px 9px; border-radius: 6px; background-color: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5;">🔥 Tier 1: High Yield (Must-Know)</span>'
                tier_caption = "🔥 High Yield (Must-Know)"
            elif importance_tier == 2:
                tier_badge = '<span style="font-size: 0.82rem; font-weight: 600; padding: 3px 9px; border-radius: 6px; background-color: #fef3c7; color: #b45309; border: 1px solid #fde68a;">⭐ Tier 2: Core Clinical</span>'
                tier_caption = "⭐ Core Clinical"
            else:
                tier_badge = '<span style="font-size: 0.82rem; font-weight: 500; padding: 3px 9px; border-radius: 6px; background-color: #f1f5f9; color: #475569; border: 1px solid #cbd5e1;">💡 Tier 3: Foundation & Nuance</span>'
                tier_caption = "💡 Foundation & Nuance"

            st.caption(f"Card {st.session_state.card_index + 1} of {len(cards)} | Category: **{current_card['category']}** | Exam Weight: **{tier_caption}** | 🔀 Shuffled Order")
            
            mastery_badges = ["⚪ New", "🟡 Learning", "🟠 Reviewing", "🟢 Mastered"]
            badge_text = mastery_badges[min(3, current_card.get("mastery_level", 0))]
            
            # -------------------------------------------------------------
            # Click-to-Flip 3D Flashcard Component
            # -------------------------------------------------------------
            bilingual_title = format_point_bilingual(current_card['title'])
            bilingual_front = format_point_bilingual(current_card['front'])
            bilingual_back = format_point_bilingual(current_card['back'])
            bilingual_variations = format_point_bilingual(current_card.get('variations', ''))
            bilingual_consensus = format_point_bilingual(current_card.get('consensus', ''))

            variations_html = ""
            if bilingual_variations:
                variations_html = f"""
                <div class="variation-callout" style="margin-top: 12px; margin-bottom: 6px;">
                    <strong style="display: block; margin-bottom: 4px;">⚠️ Textbook Variations & Discrepancies:</strong>
                    <div style="white-space: pre-line; line-height: 1.5;">{bilingual_variations}</div>
                </div>
                """

            consensus_html = ""
            if bilingual_consensus:
                consensus_html = f"""
                <div style="font-size: 0.88rem; color: #64748b; margin-top: 8px; font-style: italic;">
                    <strong>Consensus:</strong> {bilingual_consensus}
                </div>
                """

            card_html = f"""
            <details class="flashcard-interactive" id="fc_{current_card['id']}_{st.session_state.card_index}">
                <summary>
                    <!-- FRONT FACE -->
                    <div class="fc-front-view">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                            <span style="font-weight: 800; font-size: 1.2rem; color: #007ba7;">{bilingual_title}</span>
                            <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
                                {tier_badge}
                                <span style="font-size: 0.82rem; padding: 3px 8px; border-radius: 6px; background-color: #faf6f0; color: #8c5e35; border: 1px solid #e8ded2;">{badge_text}</span>
                            </div>
                        </div>
                        <div style="font-size: 1.1rem; line-height: 1.6; min-height: 80px;">
                            <strong>Question:</strong><br>{bilingual_front}
                        </div>
                        <div style="text-align: center; margin-top: 18px; font-size: 0.88rem; color: #007ba7; font-weight: 700; padding: 8px 12px; background: rgba(0, 123, 167, 0.08); border-radius: 8px; border: 1px dashed rgba(0, 123, 167, 0.35);">
                            👆 Click or tap card to reveal answer 🔄
                        </div>
                    </div>
                    <!-- BACK FACE -->
                    <div class="fc-back-view">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                            <span style="font-weight: 800; font-size: 1.2rem; color: #007ba7;">{bilingual_title}</span>
                            <div style="display: flex; gap: 6px; align-items: center; flex-wrap: wrap;">
                                {tier_badge}
                                <span style="font-size: 0.82rem; padding: 3px 8px; border-radius: 6px; background-color: #eef0fb; color: #484eb2; font-weight: 700; border: 1px solid #dcdff9;">Answer Revealed</span>
                            </div>
                        </div>
                        <div style="font-size: 1.05rem; line-height: 1.6; white-space: pre-line; margin-bottom: 8px;">
                            <strong>Answer:</strong><br>{bilingual_back}
                        </div>
                        {variations_html}
                        {consensus_html}
                        <div style="text-align: center; margin-top: 18px; font-size: 0.88rem; color: #64748b; font-weight: 700; padding: 8px 12px; background: rgba(100, 116, 139, 0.08); border-radius: 8px; border: 1px dashed rgba(100, 116, 139, 0.35);">
                            👆 Click or tap card to flip back to question 🔄
                        </div>
                    </div>
                </summary>
            </details>
            """
            st.markdown(card_html, unsafe_allow_html=True)

            # Retention Rating Buttons
            st.write("")
            st.markdown("**Rate Your Retention:**")
            rate_col1, rate_col2, rate_col3 = st.columns(3)
            if rate_col1.button("🔴 Again", use_container_width=True):
                update_card_mastery(current_card["id"], "again")
                current_card["mastery_level"] = 0
                st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
                st.rerun()
            if rate_col2.button("🟡 Good", use_container_width=True):
                update_card_mastery(current_card["id"], "good")
                current_card["mastery_level"] = min(3, current_card.get("mastery_level", 0) + 1)
                st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
                st.rerun()
            if rate_col3.button("🟢 Mastered", use_container_width=True):
                update_card_mastery(current_card["id"], "mastered")
                current_card["mastery_level"] = 3
                st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
                st.rerun()
                    
            # Navigation Controls
            st.write("")
            nav_col1, nav_col2 = st.columns(2)
            if nav_col1.button("⬅️ Previous Card", use_container_width=True):
                st.session_state.card_flipped = False
                st.session_state.card_index = (st.session_state.card_index - 1) % len(cards)
                st.rerun()
            if nav_col2.button("Next Card ➡️", use_container_width=True):
                st.session_state.card_flipped = False
                st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
                st.rerun()
                
    elif mode == "Generate New Flashcard":
        st.subheader("➕ Synthesize New Flashcard from Textbooks")
        st.caption("Cross-references all indexed sources and synthesizes consensus + variations with bilingual names.")
        
        gen_cat = st.selectbox("Category for Card", options=FLASHCARD_CATEGORIES[1:])
        topic_input = st.text_input(
            "Topic or Point Name",
            placeholder="e.g. BL1 Jingming, PC6 Neiguan, Four Gates, Pregnancy Contraindications"
        )
        
        if st.button("⚡ Generate Synthesized Flashcard", type="primary", use_container_width=True):
            if not topic_input:
                st.error("Please enter a topic or acupoint name.")
            else:
                with st.spinner(f"Analyzing textbook sources for '{topic_input}'..."):
                    success, msg, card_data = generate_synthesized_flashcard(
                        topic=topic_input,
                        provider=engine_provider,
                        api_key=api_key
                    )
                    if success and card_data:
                        st.success(msg)
                        st.markdown(f"**Title:** {format_point_bilingual(card_data['title'])}")
                        st.markdown(f"**Front:** {format_point_bilingual(card_data['front'])}")
                        st.markdown(f"**Back:** {format_point_bilingual(card_data['back'])}")
                        if card_data.get("variations"):
                            st.warning(f"Variations: {format_point_bilingual(card_data['variations'])}")
                    else:
                        st.error(msg)


# =============================================================================
# TAB 3: Atlas
# =============================================================================
elif nav_choice == "Atlas":
    # Interactive Acupuncture Atlas Component (Seamlessly Integrated)
    html_atlas = generate_atlas_html()
    st.iframe(html_atlas, height="content")


# =============================================================================
# TAB: Diagnostics for Internal Illness
# =============================================================================
elif nav_choice == "Diagnostics":
    render_internal_diagnostics_tab()


# =============================================================================
# TAB: Visual Tongue & Pulse Clinical Atlas
# =============================================================================
elif nav_choice == "Tongue & Pulse":
    render_tongue_pulse_atlas_tab()


# =============================================================================
# TAB: Classical Point Combinations Engine
# =============================================================================
elif nav_choice == "Point Pairs":
    render_point_pairs_tab()


# =============================================================================
# TAB: Patient Treatment Plan & SOAP Note Generator
# =============================================================================
elif nav_choice == "SOAP Notes":
    render_soap_notes_tab()


# =============================================================================
# TAB: Interactive 2D Pain Map (External Pain)
# =============================================================================
elif nav_choice == "Pain Map":
    render_pain_map_tab()


# =============================================================================
# TAB: TCM Core Concepts & Memory Aids
# =============================================================================
elif nav_choice == "Concepts":
    render_concepts_tab()


# =============================================================================
# TAB: Printable Study Guides & Pocket Cheat Sheets
# =============================================================================
elif nav_choice == "Study Guides":
    render_study_guides_tab()


# =============================================================================
# TAB: NCCAOM Practice Exam Simulator (300 Questions)
# =============================================================================
elif nav_choice == "Practice Exam":
    render_practice_exam_tab()


# =============================================================================
# TAB 4: Clinical Case Simulator
# =============================================================================
elif nav_choice == "Case Simulator":
    st.subheader("Clinical Patient Case Simulator")
    st.caption("Simulate real patient cases. Choose between Multiple Choice (with full rationale for each choice) or Open Diagnostic entry.")
    
    cases = get_all_cases()
    case_titles = {c["id"]: f"{c['id']}: {c['title']}" for c in cases}
    case_ids = list(case_titles.keys())
    
    if "selected_case_id" not in st.session_state or st.session_state.selected_case_id not in case_ids:
        st.session_state.selected_case_id = random.choice(case_ids) if case_ids else "CASE-001"
    
    if "case_simulator_selectbox" not in st.session_state or st.session_state.case_simulator_selectbox not in case_ids:
        st.session_state.case_simulator_selectbox = st.session_state.selected_case_id

    def on_case_change():
        st.session_state.selected_case_id = st.session_state.case_simulator_selectbox
        st.session_state.current_case_id = st.session_state.case_simulator_selectbox
        st.session_state.last_graded_result = None

    def on_random_case_click():
        other_cases = [cid for cid in case_ids if cid != st.session_state.selected_case_id]
        new_choice = random.choice(other_cases) if other_cases else st.session_state.selected_case_id
        st.session_state.selected_case_id = new_choice
        st.session_state.case_simulator_selectbox = new_choice
        st.session_state.current_case_id = new_choice
        st.session_state.last_graded_result = None

    c_sel, c_rand = st.columns([4, 1])
    with c_sel:
        selected_id = st.selectbox(
            "Select Clinical Case",
            options=case_ids,
            format_func=lambda x: case_titles[x],
            key="case_simulator_selectbox",
            on_change=on_case_change
        )
    with c_rand:
        st.write("")
        st.write("")
        st.button("🎲 Random Case", on_click=on_random_case_click, use_container_width=True, help="Load a random patient case")

    active_case = get_case_by_id(st.session_state.selected_case_id)
    
    # Two-column layout on desktop: Left = Patient Chart, Right = Interactive Simulator
    col_chart, col_sim = st.columns([1, 1], gap="large")
    
    with col_chart:
        # Patient Chart Presentation (Clean Native Streamlit Elements - No raw code blocks)
        p = active_case["patient"]
        exams = p["four_examinations"]
        category_label = active_case.get("category", "General Clinical")
        
        with st.container(border=True):
            # Patient Header
            c_h1, c_h2 = st.columns([3, 2])
            with c_h1:
                st.markdown(f"### 📋 {active_case['id']}")
                st.markdown(f"**{active_case['title']}**")
            with c_h2:
                st.caption(f"🏷️ **Exam Category:** {category_label}")
                st.caption(f"👤 **Patient:** {p['gender']}, {p['age']}y • {p['occupation']}")
            
            st.divider()

            # Chief Complaint Callout
            st.info(f"**Chief Complaint (主诉):**\n\n{p['chief_complaint']}")
            
            # History of Present Illness
            st.markdown(f"**History of Present Illness (现病史):**\n\n{p['history']}")
            
            st.write("")
            st.markdown("##### 🩺 Four Examinations (四诊)")
            
            r1_c1, r1_c2 = st.columns(2)
            with r1_c1:
                with st.container(border=True):
                    st.markdown("**👁️ 望 (Inspection / Tongue)**")
                    st.write(exams["inspection"])
            with r1_c2:
                with st.container(border=True):
                    st.markdown("**👂 闻 (Auscultation & Olfaction)**")
                    st.write(exams["auscultation_olfaction"])
                    
            r2_c1, r2_c2 = st.columns(2)
            with r2_c1:
                with st.container(border=True):
                    st.markdown("**🗣️ 问 (Inquiry / Symptoms)**")
                    st.write(exams["inquiry"])
            with r2_c2:
                with st.container(border=True):
                    st.markdown("**✋ 切 (Palpation / Pulse)**")
                    st.write(exams["palpation"])
        
        # Past Case History Expander
        history = get_case_history()
        if history:
            with st.expander(f"📜 View Past Case Attempts ({len(history)} recorded)"):
                for h in history[:5]:
                    st.markdown(f"**{h['case_title']}** - Score: `{h['score']}/100` on *{h['created_at'][:16]}*")
                    st.caption(f"Diagnosis: {h['user_diagnosis']} | Points: {format_point_bilingual(h['user_prescription'])}")
                    st.divider()

    with col_sim:
        # Simulator Mode Selector
        sim_mode = st.radio(
            "Simulator Mode",
            options=["🎯 Multiple Choice Challenge (Board Exam Style)", "✍️ Open Clinical Entry (AI Graded)"],
            horizontal=True
        )
        
        # -------------------------------------------------------------
        # MODE 1: Multiple Choice with Full Explanation for Each Choice
        # -------------------------------------------------------------
        if sim_mode == "🎯 Multiple Choice Challenge (Board Exam Style)":
            st.markdown("### 🎯 Board Examination Multiple Choice Questions")
            st.caption("Select your answers. Each choice includes an exhaustive textbook explanation.")
            
            mcqs = active_case.get("multiple_choice_questions", [])
            total_mcqs = len(mcqs)
            answered_count = sum(1 for q in mcqs if f"mcq_{selected_id}_{q['question_id']}" in st.session_state.mcq_answers)
            correct_count = 0
            for q in mcqs:
                k = f"mcq_{selected_id}_{q['question_id']}"
                if k in st.session_state.mcq_answers:
                    c_letter = st.session_state.mcq_answers[k][:1] if st.session_state.mcq_answers[k] else ""
                    corr_letter = ["A", "B", "C", "D"][q["correct_index"]]
                    if c_letter == corr_letter:
                        correct_count += 1

            # Progress tracker banner
            score_color = "#16a34a" if (answered_count == total_mcqs and correct_count == total_mcqs and total_mcqs > 0) else ("#007ba7" if answered_count > 0 else "#64748b")
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 10px; padding: 10px 16px; margin: 12px 0 18px 0;">
                <div style="font-size: 0.88rem; font-weight: 700; color: #334155;">
                    📋 Case Progress: <span style="color: #007ba7;">{answered_count} of {total_mcqs} answered</span>
                </div>
                <div style="font-size: 0.88rem; font-weight: 700; color: {score_color};">
                    🏆 Score: {correct_count}/{answered_count} correct
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            for idx, q in enumerate(mcqs):
                st.markdown(f"#### {q['title']}")
                st.write(q["prompt"])
                
                # Format options with bilingual acupoints
                formatted_options = [format_point_bilingual(opt) for opt in q["options"]]
                
                q_state_key = f"mcq_{selected_id}_{q['question_id']}"
                radio_key = f"radio_{q_state_key}"
                
                choice = st.radio(
                    f"Options for {q['title']}",
                    options=formatted_options,
                    index=None,
                    key=radio_key,
                    label_visibility="collapsed"
                )
                
                c_chk, c_retry = st.columns([3, 1])
                with c_chk:
                    check_btn = st.button(f"🔍 Check Answer ({q['question_id']})", key=f"btn_{q_state_key}", use_container_width=True)
                with c_retry:
                    retry_btn = st.button("🔄 Retry", key=f"retry_{q_state_key}", use_container_width=True)

                if retry_btn:
                    if q_state_key in st.session_state.mcq_answers:
                        del st.session_state.mcq_answers[q_state_key]
                    if radio_key in st.session_state:
                        st.session_state[radio_key] = None
                    st.rerun()
                
                if check_btn:
                    if choice is None:
                        st.warning("⚠️ Please select an option above before checking your answer.")
                    else:
                        st.session_state.mcq_answers[q_state_key] = choice
                        st.rerun()
                    
                if q_state_key in st.session_state.mcq_answers:
                    chosen_opt = st.session_state.mcq_answers[q_state_key]
                    chosen_letter = chosen_opt[:1] if chosen_opt else ""
                    correct_letter = ["A", "B", "C", "D"][q["correct_index"]]
                    
                    if chosen_letter == correct_letter:
                        st.success(f"🎉 **Correct!** You chose **{chosen_letter}**.")
                    else:
                        st.error(f"❌ **Incorrect.** You selected **{chosen_letter}**. The textbook standard is **{correct_letter}**.")
                        
                    # EXPLANATION OF EVERY SINGLE CHOICE
                    with st.expander(f"📖 In-Depth Explanation of Each Choice ({q['question_id']})", expanded=True):
                        for opt_key, explanation in q["explanations"].items():
                            st.markdown(f"**Choice {opt_key}:**\n{format_point_bilingual(explanation)}")
                            st.write("")
                st.divider()

        # -------------------------------------------------------------
        # MODE 2: Open Clinical Entry (AI Textbook Graded)
        # -------------------------------------------------------------
        else:
            st.markdown("### ✍️ Open Clinical Diagnostic Entry")
            st.caption("Formulate your diagnosis and point prescription. The engine grades it against combined textbook data.")
            
            with st.form(f"clinical_evaluation_form_{selected_id}"):
                user_diag = st.text_input(
                    "1. TCM Pattern Diagnosis",
                    placeholder="e.g. Liver Qi Stagnation transforming into Fire",
                    help="Specify the Zang-Fu organ pattern and pathology."
                )
                user_presc = st.text_input(
                    "2. Point Prescription (Codes or Names)",
                    placeholder="e.g. LV3, LI4, GB20, Taiyang, SP6",
                    help="Enter primary acupoints separated by commas."
                )
                user_rationale = st.text_area(
                    "3. Clinical Rationale & Needling Techniques",
                    placeholder="e.g. Four Gates to move stagnant Qi, GB20 oblique towards opposite eye to extinguish wind. Reducing method on LV3, tonifying on SP6. Moxa contraindicated.",
                    help="Explain point combination synergy, depths, needle manipulation, or pregnancy precautions."
                )
                
                submit_btn = st.form_submit_button("📋 Submit for Textbook Grading", type="primary", use_container_width=True)
                
            if submit_btn:
                if not user_diag.strip() or not user_presc.strip():
                    st.error("Please fill in both your TCM Pattern Diagnosis and Point Prescription.")
                else:
                    with st.spinner("Grading clinical submission against combined textbooks..."):
                        grading_result = grade_clinical_case(
                            case_id=selected_id,
                            user_diagnosis=user_diag,
                            user_prescription=user_presc,
                            user_rationale=user_rationale,
                            provider=engine_provider,
                            api_key=api_key
                        )
                        st.session_state.last_graded_result = {
                            "case_id": selected_id,
                            "result": grading_result
                        }
                        st.rerun()
                        
            # Display Evaluation Report only if it matches current case
            if st.session_state.last_graded_result and st.session_state.last_graded_result.get("case_id") == selected_id:
                res = st.session_state.last_graded_result["result"]
                st.markdown(res["feedback_markdown"])
                if st.button("🗑️ Clear Evaluation Report", key=f"clear_eval_{selected_id}"):
                    st.session_state.last_graded_result = None
                    st.rerun()


# =============================================================================
# TAB: Progress & Settings
# =============================================================================
elif nav_choice == "Progress & Settings":
    # -------------------------------------------------------------------------
    # Administrator Authentication Gate
    # -------------------------------------------------------------------------
    admin_authed = st.session_state.get("admin_authenticated", False)
    admin_pwd_target = get_setting("ADMIN_PASSWORD", "admin123")

    if not admin_authed:
        st.markdown("""
        <div style="background: #111827; border: 1.5px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 22px 24px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="font-size: 1.8rem;">🔒</span>
                <div>
                    <h3 style="color: #ffffff !important; margin: 0; font-size: 1.35rem; font-weight: 800;">
                        System Administration &amp; Security Gate
                    </h3>
                    <div style="color: #94a3b8; font-size: 0.88rem; margin-top: 3px;">
                        Access to AI Intelligence Engine credentials, API keys, and textbook vector indexes is restricted.
                    </div>
                </div>
            </div>
            <div style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.55; margin-top: 10px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 12px;">
                Please enter your administrator passcode below to unlock system settings and AI configuration.
            </div>
        </div>
        """, unsafe_allow_html=True)

        c_lock_col, _ = st.columns([1.2, 0.8])
        with c_lock_col:
            with st.form("admin_login_form"):
                entered_pwd = st.text_input(
                    "Administrator Passcode",
                    type="password",
                    placeholder="Enter admin passcode...",
                    help="Default passcode is 'admin123'. You can change it once logged in."
                )
                c_btn1, _ = st.columns([1, 1])
                with c_btn1:
                    submit_auth = st.form_submit_button("🔓 Unlock Settings", type="primary", use_container_width=True)

                if submit_auth:
                    if entered_pwd == admin_pwd_target:
                        st.session_state.admin_authenticated = True
                        st.toast("✅ Admin authentication successful!", icon="🔓")
                        st.rerun()
                    else:
                        st.error("❌ Incorrect administrator passcode. Please try again.")

        if admin_pwd_target == "admin123":
            st.caption("💡 *First time logging in? Default passcode is `admin123`. You can customize it inside after unlocking.*")
        
        st.stop()

    # Authenticated Admin Header Row
    c_title, c_lock = st.columns([0.78, 0.22], vertical_alignment="center")
    with c_title:
        st.subheader("⚙️ Progress Analytics & System Settings (Admin Mode Active)")
        st.caption("Review clinical study analytics, configure AI intelligence providers, manage reference textbooks, and manage security.")
    with c_lock:
        if st.button("🔒 Lock Admin Session", use_container_width=True, key="btn_admin_logout"):
            st.session_state.admin_authenticated = False
            st.toast("Admin mode locked.", icon="🔒")
            st.rerun()

    stats = get_flashcard_stats()
    cases_logged = get_case_history()

    # Top Status Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Mastered Flashcards", f"{stats['mastered']} / {stats['total']}", help="Number of mastered cards vs total cards in your deck")
    with m2:
        avg_score = round(sum(c["score"] for c in cases_logged) / len(cases_logged), 1) if cases_logged else "N/A"
        st.metric("Clinical Cases Logged", len(cases_logged), delta=f"Avg {avg_score}%" if avg_score != "N/A" else None, help="Total clinical patient cases simulated")
    with m3:
        st.metric("Active AI Provider", active_provider.replace(" (Recommended)", "").replace(" / Built-in TCM Engine", ""))
    with m4:
        st.metric("Vector Store Status", "✅ Ready" if is_index_built() else "⚠️ Needs Build", delta=f"{indexed_count} / {len(files_info)} indexed")

    st.write("")

    sub_tab_analytics, sub_tab_engine, sub_tab_library, sub_tab_mobile, sub_tab_security = st.tabs([
        "📊 Study Analytics & Logs",
        "🤖 AI Engine & Credentials",
        "📚 Textbook Library & Vector Store (RAG)",
        "📱 Mobile App Setup",
        "🔐 Admin Security & Passcode"
    ])

    # -------------------------------------------------------------------------
    # Subtab 1: Study Analytics & Performance Logs
    # -------------------------------------------------------------------------
    with sub_tab_analytics:
        col_fc, col_cs = st.columns([1, 1], gap="large")
        with col_fc:
            st.markdown("""
            <div style="font-weight: 800; font-size: 1.1rem; color: #007ba7; margin-bottom: 6px;">
                🗂️ Flashcard Deck Retention Breakdown
            </div>
            """, unsafe_allow_html=True)
            total_fc = stats["total"]
            mast_fc = stats["mastered"]
            pct = int((mast_fc / total_fc) * 100) if total_fc > 0 else 0
            st.progress(pct / 100, text=f"Deck Mastery: {pct}% ({mast_fc} / {total_fc} cards)")

            st.markdown(f"""
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 16px 18px; margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.95rem;">
                    <span>🟢 <strong>Mastered (Retention Level 3):</strong></span>
                    <span style="font-weight: 700; color: #059669;">{mast_fc}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.95rem;">
                    <span>🟡 <strong>In Progress / Reviewing (Levels 1-2):</strong></span>
                    <span style="font-weight: 700; color: #d97706;">{total_fc - mast_fc}</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.95rem; border-top: 1px solid #e2e8f0; padding-top: 8px;">
                    <span>📚 <strong>Total Flashcards in Deck:</strong></span>
                    <span style="font-weight: 700; color: #007ba7;">{total_fc}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_cs:
            st.markdown("""
            <div style="font-weight: 800; font-size: 1.1rem; color: #484eb2; margin-bottom: 6px;">
                🩺 Clinical Case Simulator Log
            </div>
            """, unsafe_allow_html=True)
            if not cases_logged:
                st.info("No clinical cases evaluated yet. Practice patient cases in the **Case Simulator** tab to record your diagnostic evaluations here!")
            else:
                st.caption(f"Showing {min(15, len(cases_logged))} most recent patient encounters:")
                for c in cases_logged[:15]:
                    score_val = c.get("score", 0)
                    badge_bg = "#ecfdf5" if score_val >= 80 else ("#fffbeb" if score_val >= 65 else "#fef2f2")
                    badge_color = "#059669" if score_val >= 80 else ("#d97706" if score_val >= 65 else "#dc2626")
                    with st.expander(f"Case {c.get('case_id', '')} · {c.get('case_title', 'Case Study')} — Score: {score_val}%", expanded=False):
                        st.write(f"**Patient:** {c.get('patient_profile', 'N/A')}")
                        st.write(f"**Your Diagnosis:** {c.get('user_diagnosis', 'N/A')}")
                        st.write(f"**Your Prescription:** {c.get('user_prescription', 'N/A')}")
                        st.markdown(f"**Score:** <span style='font-size: 1.1rem; font-weight: 800; color: {badge_color}; background: {badge_bg}; padding: 2px 8px; border-radius: 6px;'>{score_val}%</span>", unsafe_allow_html=True)
                        if c.get("feedback_markdown"):
                            st.markdown("---")
                            st.markdown(c["feedback_markdown"])

    # -------------------------------------------------------------------------
    # Subtab 2: AI Engine & Provider Credentials
    # -------------------------------------------------------------------------
    with sub_tab_engine:
        st.markdown("""
        <div style="font-weight: 800; font-size: 1.15rem; color: #484eb2; margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
            🤖 Clinical AI Engine & Intelligence Provider
        </div>
        <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 14px;">
            Select between Google Gemini, OpenAI, local Ollama, or the built-in offline TCM engine.
        </div>
        """, unsafe_allow_html=True)

        selected_provider_tab = st.selectbox(
            "Select Intelligence Engine",
            options=provider_options,
            index=provider_options.index(active_provider) if active_provider in provider_options else 0,
            key="tab_settings_provider_select"
        )
        if selected_provider_tab != active_provider:
            st.session_state.provider_choice = selected_provider_tab
            save_setting("LAST_PROVIDER", selected_provider_tab)
            st.rerun()

        st.write("")

        # Provider specific settings
        if selected_provider_tab == "Google Gemini (Recommended)":
            if saved_gemini_key:
                masked = f"{saved_gemini_key[:6]}...{saved_gemini_key[-4:]}" if len(saved_gemini_key) > 10 else "••••••••"
                st.success(f"🔑 **Gemini API Key Active & Stored:** `{masked}`")

                with st.expander("✏️ Update or Change Gemini API Key", expanded=False):
                    new_gemini_key = st.text_input(
                        "Replace Gemini API Key",
                        value=saved_gemini_key,
                        type="password",
                        key="settings_tab_gemini_edit",
                        help="Update your saved Google Gemini API key"
                    )
                    c_up, c_del = st.columns(2)
                    with c_up:
                        if st.button("💾 Save Updated Key", type="primary", use_container_width=True, key="settings_tab_gemini_save_edit"):
                            if new_gemini_key.strip():
                                save_setting("GEMINI_API_KEY", new_gemini_key.strip())
                                st.success("Gemini API key updated and saved permanently!")
                                st.rerun()
                    with c_del:
                        if st.button("🗑️ Remove Key", use_container_width=True, key="settings_tab_gemini_del"):
                            remove_setting("GEMINI_API_KEY")
                            st.info("Key removed.")
                            st.rerun()
            else:
                st.warning("⚠️ No Gemini API key saved yet. Enter your key below to unlock AI multi-textbook synthesis and clinical case grading.")
                new_gemini_key = st.text_input(
                    "Gemini API Key",
                    type="password",
                    placeholder="Paste AIzaSy... here",
                    key="settings_tab_gemini_new",
                    help="Your API key is saved locally in data/settings.json and loads automatically."
                )
                if st.button("💾 Save Key Permanently", type="primary", use_container_width=True, key="settings_tab_gemini_save_new"):
                    if new_gemini_key.strip():
                        save_setting("GEMINI_API_KEY", new_gemini_key.strip())
                        st.success("Gemini API Key saved permanently! It will load on every launch.")
                        st.rerun()
                    else:
                        st.error("Please enter a valid API key.")

            st.selectbox(
                "Gemini Model Architecture",
                options=["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-flash-latest"],
                index=0,
                key="settings_tab_gemini_model_select",
                help="Gemini Flash Lite is Google's recommended model for ultra-fast multi-textbook synthesis and clinical case reasoning."
            )

            if saved_gemini_key:
                st.write("")
                if st.button("🧪 Test Gemini Connection & Ping Engine", use_container_width=True, key="settings_tab_gemini_test_btn"):
                    with st.spinner("Pinging Google Gemini API..."):
                        try:
                            from google import genai
                            client = genai.Client(api_key=saved_gemini_key)
                            test_res = None
                            for m in ["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-flash-latest"]:
                                try:
                                    response = client.models.generate_content(
                                        model=m,
                                        contents="Confirm TCM Engine connection in 5 words."
                                    )
                                    if response and response.text:
                                        test_res = response.text.strip()
                                        break
                                except Exception:
                                    continue
                            if test_res:
                                st.success(f"✅ Connection Verified! Model response: *{test_res}*")
                            else:
                                st.error("❌ Connection failed across fallback models.")
                        except Exception as e:
                            st.error(f"❌ Connection test failed: {e}")

        elif selected_provider_tab == "OpenAI":
            if saved_openai_key:
                masked = f"{saved_openai_key[:7]}...{saved_openai_key[-4:]}" if len(saved_openai_key) > 11 else "••••••••"
                st.success(f"🔑 **OpenAI Key Active & Stored:** `{masked}`")
                with st.expander("✏️ Update or Change OpenAI API Key", expanded=False):
                    new_openai_key = st.text_input(
                        "Replace OpenAI API Key",
                        value=saved_openai_key,
                        type="password",
                        key="settings_tab_openai_edit"
                    )
                    c_up, c_del = st.columns(2)
                    with c_up:
                        if st.button("💾 Save Updated Key", type="primary", use_container_width=True, key="settings_tab_openai_save_edit"):
                            if new_openai_key.strip():
                                save_setting("OPENAI_API_KEY", new_openai_key.strip())
                                st.success("OpenAI Key saved!")
                                st.rerun()
                    with c_del:
                        if st.button("🗑️ Remove Key", use_container_width=True, key="settings_tab_openai_del"):
                            remove_setting("OPENAI_API_KEY")
                            st.info("Key removed.")
                            st.rerun()
            else:
                st.warning("⚠️ No OpenAI API key saved yet.")
                new_openai_key = st.text_input(
                    "OpenAI API Key",
                    type="password",
                    placeholder="Paste sk-... here",
                    key="settings_tab_openai_new"
                )
                if st.button("💾 Save Key Permanently", type="primary", use_container_width=True, key="settings_tab_openai_save_new"):
                    if new_openai_key.strip():
                        save_setting("OPENAI_API_KEY", new_openai_key.strip())
                        st.success("OpenAI Key saved!")
                        st.rerun()

            st.selectbox(
                "OpenAI Model",
                options=["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
                index=0,
                key="settings_tab_openai_model_select"
            )

        elif selected_provider_tab == "Ollama (Local)":
            st.text_input("Ollama Base URL", value="http://localhost:11434", key="settings_tab_ollama_url")
            st.text_input("Model Identifier", value="llama3", key="settings_tab_ollama_model")
            st.info("Ensure Ollama daemon is running locally (`ollama serve`).")

        else: # Offline / Built-in TCM Engine
            st.markdown("""
            <div class="nlm-card" style="border-left: 5px solid #c89666; margin-top: 8px;">
                <h4 style="margin: 0 0 8px 0; color: #8c5e35;">🛡️ 100% Offline & Private TCM Engine</h4>
                <p style="font-size: 0.9rem; line-height: 1.5; color: #475569; margin-bottom: 10px;">
                    This mode uses the embedded WHO acupoint database, classical point combinations, and built-in heuristics. 
                    No network calls are made, and no API keys are required.
                </p>
                <div style="font-size: 0.85rem; display: flex; flex-direction: column; gap: 6px;">
                    <span>✓ Complete 429 point WHO standard database</span>
                    <span>✓ Multi-textbook variation detection (CAM / Deadman / Maciocia)</span>
                    <span>✓ Clinical case grading heuristics</span>
                    <span>✓ Zero external latency, works completely without internet</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # Subtab 3: Textbook Library & Vector Store (RAG)
    # -------------------------------------------------------------------------
    with sub_tab_library:
        st.markdown("""
        <div style="font-weight: 800; font-size: 1.15rem; color: #007ba7; margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
            📚 Textbook Library & Vector Store (RAG)
        </div>
        <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 14px;">
            Upload textbooks, lecture notes, or reference PDFs to index them for clinical search and flashcard generation.
        </div>
        """, unsafe_allow_html=True)

        col_up, col_idx_action = st.columns([2, 1], vertical_alignment="top")
        with col_up:
            # File Uploader
            uploaded_files = st.file_uploader(
                "Upload Textbook or Study Material",
                type=["pdf", "txt", "md"],
                accept_multiple_files=True,
                key="settings_tab_uploader",
                help="Upload PDF, TXT, or Markdown documents to include them in the clinical search and vector store."
            )
            if uploaded_files:
                uploaded_count = 0
                for uploaded_file in uploaded_files:
                    success, msg = add_uploaded_file(uploaded_file)
                    if success:
                        uploaded_count += 1
                        st.success(f"✓ Saved: {uploaded_file.name}")
                    else:
                        st.error(msg)
                if uploaded_count > 0:
                    st.info("💡 Files saved to `materials/`! Click 'Rebuild Vector Index' below to update embeddings.")

        with col_idx_action:
            st.markdown("##### ⚡ Semantic Vector Store")
            idx_built = is_index_built()
            if idx_built:
                st.success("✅ **Vector Store Active**")
            else:
                st.warning("⚠️ **Needs Build**")
            st.caption(f"Storage: `{DATA_DIR / 'vector_store'}`")
            if st.button("⚡ Rebuild Vector Index Now", type="primary", use_container_width=True, key="settings_tab_rebuild_btn"):
                progress_bar = st.progress(0, text="Initializing textbook indexer...")
                progress_bar.progress(25, text="Parsing study textbooks & safety documents...")
                idx, status_msg = build_or_load_index(force_rebuild=True, provider=engine_provider, api_key=api_key)
                progress_bar.progress(100, text="Indexing complete!")
                if idx is not None:
                    st.success(status_msg)
                    st.toast("✅ Vector store rebuilt and persisted!", icon="⚡")
                else:
                    st.warning(status_msg)

        st.write("")
        st.markdown(f"**Textbook Files by Folder ({len(folders_map)} folders):**")

        st.markdown("""
        <div style="font-size: 0.82rem; color: #475569; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; line-height: 1.6;">
            <strong>📖 Document Status Legend:</strong><br/>
            • <strong>🟢 Vectored:</strong> The file's text is parsed and indexed in the persistent vector store. Ready for instant AI semantic citations.<br/>
            • <strong>📷 Scanned (No Text Layer):</strong> Scanned bitmap/photograph book (e.g. <em>Handbook of Oriental Medicine</em>). Its core acupoints and safety rules are pre-compiled into the Atlas & Cases!<br/>
            • <strong>📄 Cataloged:</strong> Readable text document in library awaiting vector rebuild.
        </div>
        """, unsafe_allow_html=True)

        vector_ready = is_index_built()
        for folder_name, folder_files in sorted(folders_map.items()):
            status_text = "Vectored" if vector_ready else "Cataloged · Awaiting Build"
            icon = "🟢" if vector_ready else "📄"
            with st.expander(f"{icon} 📂 {folder_name} ({len(folder_files)} files | {status_text})", expanded=False):
                for f in folder_files:
                    if f.get("is_scanned"):
                        badge = "📷 Scanned (Bitmap Only)"
                        note = " *(Image scan — atlas points built-in)*"
                    elif vector_ready and f.get("indexed"):
                        badge = "🟢 Vectored"
                        note = ""
                    elif f.get("indexed"):
                        badge = "📄 Cataloged"
                        note = ""
                    else:
                        badge = "⚪ Pending"
                        note = ""
                    st.write(f"- **{badge}**: **{f['filename']}** ({f['size_kb']} KB){note}")

    # -------------------------------------------------------------------------
    # Subtab 4: Mobile App Setup
    # -------------------------------------------------------------------------
    with sub_tab_mobile:
        st.markdown("""
        <div style="font-weight: 800; font-size: 1.15rem; color: #007ba7; margin-bottom: 4px;">
            📱 Install as Mobile Study App (iOS & Android)
        </div>
        <p style="font-size: 0.9rem; color: #64748b;">
            Run this app as a native, full-screen mobile app on your iPhone, iPad, or Android phone without an app store download.
        </p>
        """, unsafe_allow_html=True)

        col_ios, col_and = st.columns(2, gap="large")
        with col_ios:
            st.markdown("""
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px 20px;">
                <h4 style="margin: 0 0 10px 0; color: #007ba7;">🍏 iPhone & iPad (Safari)</h4>
                <ol style="font-size: 0.9rem; line-height: 1.7; padding-left: 20px; color: #334155; margin: 0;">
                    <li>Ensure your computer and iPhone are on the same Wi-Fi network.</li>
                    <li>Start Streamlit with: <code>streamlit run app.py --server.address 0.0.0.0</code></li>
                    <li>Open <strong>Safari</strong> on iPhone and navigate to <code>http://&lt;your-computer-ip&gt;:8501</code></li>
                    <li>Tap the <strong>Share</strong> button (box with upward arrow) at the bottom.</li>
                    <li>Scroll down and tap <strong>"Add to Home Screen"</strong> (➕).</li>
                    <li>Launch the app from your home screen for a full-screen, native experience!</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col_and:
            st.markdown("""
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px 20px;">
                <h4 style="margin: 0 0 10px 0; color: #484eb2;">🤖 Android (Chrome)</h4>
                <ol style="font-size: 0.9rem; line-height: 1.7; padding-left: 20px; color: #334155; margin: 0;">
                    <li>Connect your Android device to the same Wi-Fi network.</li>
                    <li>Start Streamlit with: <code>streamlit run app.py --server.address 0.0.0.0</code></li>
                    <li>Open <strong>Google Chrome</strong> and enter <code>http://&lt;your-computer-ip&gt;:8501</code></li>
                    <li>Tap the <strong>Three Dots (⋮)</strong> menu in the upper right.</li>
                    <li>Tap <strong>"Install app"</strong> or <strong>"Add to Home screen"</strong>.</li>
                    <li>Enjoy fullscreen offline-capable study access on the go!</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # Subtab 5: Administrator Security & Passcode Management
    # -------------------------------------------------------------------------
    with sub_tab_security:
        st.markdown("""
        <div style="font-weight: 800; font-size: 1.15rem; color: #484eb2; margin-bottom: 4px;">
            🔐 Administrator Security &amp; Access Control
        </div>
        <div style="font-size: 0.85rem; color: #64748b; margin-bottom: 14px;">
            Configure the administrator passcode required to unlock system settings, protect AI credentials, and manage textbook vector data.
        </div>
        """, unsafe_allow_html=True)

        current_admin_pwd = get_setting("ADMIN_PASSWORD", "admin123")
        is_default = (current_admin_pwd == "admin123")

        if is_default:
            st.warning("⚠️ **Security Warning**: You are currently using the default passcode (`admin123`). Before publishing this website publicly, please set a custom strong passcode below.")
        else:
            st.success("✅ **Custom Admin Passcode Active**: Your settings and API keys are protected against unauthorized visitors.")

        with st.form("change_admin_pwd_form"):
            st.markdown("##### Update Administrator Passcode")
            new_pwd = st.text_input("New Passcode", type="password", key="input_new_admin_pwd", placeholder="Enter new passcode...")
            confirm_pwd = st.text_input("Confirm New Passcode", type="password", key="input_confirm_admin_pwd", placeholder="Confirm new passcode...")
            save_pwd_btn = st.form_submit_button("💾 Save New Passcode", type="primary")

            if save_pwd_btn:
                if not new_pwd.strip():
                    st.error("Passcode cannot be blank.")
                elif len(new_pwd.strip()) < 4:
                    st.error("Passcode must be at least 4 characters long.")
                elif new_pwd.strip() != confirm_pwd.strip():
                    st.error("Passcodes do not match.")
                else:
                    save_setting("ADMIN_PASSWORD", new_pwd.strip())
                    st.success("✅ Administrator passcode updated and saved permanently!")
                    st.rerun()


# =============================================================================
# SITE-WIDE MEDICAL & LEGAL DISCLAIMER FOOTER
# =============================================================================
st.write("")
st.write("")
st.markdown("""
<div class="site-disclaimer-footer" style="clear: both; width: 100%; position: relative; margin-top: 56px; border-top: 1.5px solid rgba(255, 255, 255, 0.1); padding-top: 28px; padding-bottom: 28px;">
    <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.1); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
        <div style="display: flex; align-items: flex-start; gap: 12px;">
            <span style="font-size: 1.5rem; line-height: 1;">⚖️</span>
            <div>
                <div style="font-weight: 800; font-size: 0.95rem; color: #fde68a; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em;">
                    Medical &amp; Clinical Decision Support Disclaimer
                </div>
                <div style="font-size: 0.84rem; color: #cbd5e1; line-height: 1.6;">
                    <strong>youracupuncture.app</strong> is an evidence-informed educational and clinical decision-support reference intended strictly for licensed acupuncturists, integrative medical professionals, and accredited TCM students. 
                    The diagnostic differentials, needling depths, electro-acupuncture frequencies, point combinations, and herbal formulas provided within this suite do <strong>not</strong> constitute medical diagnosis, formal healthcare examination, or patient self-treatment recommendations. 
                    Licensed healthcare practitioners must independently evaluate patient history, vital signs, contraindications (including pregnancy, anatomical risk zones, and pacemaker precautions), and verify safety standards prior to clinical execution.
                </div>
            </div>
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; font-size: 0.82rem; color: #94a3b8; padding: 0 4px;">
        <div>
            © 2026 <strong>youracupuncture.app</strong> · Evidence-Informed TCM Acupuncture Suite · All Rights Reserved.
        </div>
        <div style="display: flex; gap: 16px;">
            <span style="color: #38bdf8;">WHO Standard (429 Points)</span>
            <span>•</span>
            <span style="color: #c89666;">CAM · Deadman · Maciocia Consensus</span>
            <span>•</span>
            <span style="color: #a5b4fc;">Dr. Tan Balance Method</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)




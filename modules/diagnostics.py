"""Clinical Patient Case Study Simulator and Grading Module.

Simulates authentic TCM clinical patient encounters where the student can practice:
1. Multiple Choice Questions with comprehensive explanations for every choice.
2. Open Clinical Entry graded against combined textbook standards (CAM, Deadman, Maciocia).
Includes bilingual point naming (Code, Pinyin, Hanzi, and English).
"""

import sqlite3
import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

from modules.rag_engine import DATA_DIR, retrieve_context, detect_variations_and_conflicts
from modules.flashcards import get_db_connection, init_db
from modules.tcm_points import get_point_bilingual_name, format_point_bilingual

from modules.cases_bank import CLINICAL_CASES


def get_all_cases() -> List[Dict[str, Any]]:
    """Return all available clinical case studies."""
    return CLINICAL_CASES


def get_case_by_id(case_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve a specific case by its unique ID."""
    for case in CLINICAL_CASES:
        if case["id"] == case_id:
            return case
    return CLINICAL_CASES[0] if CLINICAL_CASES else None


def grade_multiple_choice(case_id: str, question_id: str, selected_option_text: str) -> Dict[str, Any]:
    """Grade a multiple choice question and return rich explanations for all options."""
    case = get_case_by_id(case_id)
    if not case:
        return {"error": "Case not found"}
        
    mcqs = case.get("multiple_choice_questions", [])
    target_q = None
    for q in mcqs:
        if q["question_id"] == question_id:
            target_q = q
            break
            
    if not target_q:
        return {"error": "Question not found"}
        
    selected_letter = selected_option_text.strip()[:1].upper()
    correct_idx = target_q["correct_index"]
    correct_letter = ["A", "B", "C", "D"][correct_idx]
    is_correct = (selected_letter == correct_letter)
    
    return {
        "is_correct": is_correct,
        "selected_letter": selected_letter,
        "correct_letter": correct_letter,
        "question_title": target_q["title"],
        "prompt": target_q["prompt"],
        "explanations": target_q["explanations"],
        "all_options": target_q["options"]
    }


def grade_clinical_case(
    case_id: str,
    user_diagnosis: str,
    user_prescription: str,
    user_rationale: str = "",
    provider: str = "demo",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """Grade student's open clinical diagnosis and point prescription against textbook standards.
    
    Evaluates:
    1. Pattern Diagnostic Accuracy (0-30 pts)
    2. Point Selection Appropriateness (0-40 pts)
    3. Channel Theory & Synergy (0-20 pts)
    4. Precautions & Textbook Variations (0-10 pts)
    Optionally calls Gemini 3.8/3.5 Flash for dynamic clinical feedback when connected.
    """
    case = get_case_by_id(case_id)
    if not case:
        return {"error": "Case not found"}
        
    std_diag = case["standard_diagnosis"]
    
    # 1. Evaluate Diagnosis
    diag_clean = user_diagnosis.lower()
    matched_patterns = []
    diag_score = 10
    for p in std_diag["patterns"]:
        words = [w.lower() for w in p.split() if len(w) > 3]
        match_count = sum(1 for w in words if w in diag_clean)
        if match_count >= 2 or p.lower() in diag_clean:
            matched_patterns.append(p)
            diag_score += 10
    diag_score = min(30, max(12, diag_score))
    
    # 2. Evaluate Point Prescription
    presc_clean = user_prescription.upper().replace(" ", "").replace("，", ",").replace("、", ",")
    presc_points = re.findall(r'[A-Z]{1,3}\d{1,2}|TAIYANG|YINTANG|JIANNEILING|YAOTONGXUE|HEDING|XIYAN', presc_clean)
    if not presc_points:
        presc_points = [p.strip().upper() for p in user_prescription.split(",") if p.strip()]
        
    matched_points = []
    missing_cardinal = []
    for card_pt in std_diag["cardinal_points"]:
        pt_code = card_pt.upper().split()[0]
        if any(pt_code in user_pt for user_pt in presc_points):
            matched_points.append(card_pt)
        else:
            missing_cardinal.append(card_pt)
            
    point_ratio = len(matched_points) / max(1, len(std_diag["cardinal_points"]))
    point_score = int(point_ratio * 35) + (5 if len(presc_points) >= 3 else 2)
    point_score = min(40, max(15, point_score))
    
    # 3. Synergy & Channel Theory
    synergy_score = 12
    synergy_notes = []
    for syn in std_diag["synergies"]:
        syn_words = [w.lower() for w in syn.replace("(", "").replace(")", "").replace("+", "").split() if len(w) > 2]
        if any(w in presc_clean.lower() or w in user_rationale.lower() for w in syn_words):
            synergy_score += 4
            synergy_notes.append(syn)
    synergy_score = min(20, synergy_score)
    
    # 4. Precautions & Textbook Variations
    caution_score = 8
    if "pregnancy" in case["patient"]["chief_complaint"].lower() or case["patient"]["age"] < 50 and case["patient"]["gender"] == "Female":
        if any(p in ["LI4", "SP6", "BL60", "GB21"] for p in presc_points):
            if "pregnancy" not in user_rationale.lower() and "contraindicat" not in user_rationale.lower():
                caution_score -= 3
                
    total_score = diag_score + point_score + synergy_score + caution_score
    total_score = min(100, max(40, total_score))
    
    if total_score >= 90:
        grade = "A+ (Master Acupuncturist Level)"
        verdict = "Outstanding clinical acumen! Your diagnosis aligns precisely with core curriculum and your point prescription exhibits master-level channel synergy."
    elif total_score >= 80:
        grade = "A (Clinically Proficient)"
        verdict = "Excellent clinical reasoning. Solid pattern identification with well-targeted primary acupoints."
    elif total_score >= 70:
        grade = "B (Competent / Board Ready)"
        verdict = "Good overall grasp of the TCM pattern. Review the complementary and empirical distal points below to optimize clinical results."
    else:
        grade = "C (Needs Review)"
        verdict = "Foundational concepts detected, but key cardinal textbook points or pattern subtleties were omitted."
        
    # Format points bilingually
    bilingual_matched = [get_point_bilingual_name(p) for p in matched_points]
    bilingual_missing = [get_point_bilingual_name(p) for p in missing_cardinal[:3]]
    
    # Optional Gemini AI clinical evaluation
    ai_critique_section = ""
    if provider == "gemini" and api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt = f"""You are a master TCM clinical board exam examiner and professor.
Evaluate this student's diagnosis and prescription for the following patient case:

[Case: {case['title']}]
Patient: {case['patient']['gender']}, {case['patient']['age']}yo, {case['patient']['occupation']}
Chief Complaint: {case['patient']['chief_complaint']}
Four Examinations:
- Tongue: {case['patient']['four_examinations']['inspection']}
- Auscultation: {case['patient']['four_examinations']['auscultation_olfaction']}
- Inquiry: {case['patient']['four_examinations']['inquiry']}
- Pulse: {case['patient']['four_examinations']['palpation']}

[Textbook Benchmark Standard]
Consensus Patterns: {', '.join(std_diag['patterns'])}
Treatment Principles: {', '.join(std_diag['treatment_principles'])}
Cardinal Points: {', '.join(std_diag['cardinal_points'])}
Synergies: {', '.join(std_diag['synergies'])}
Precautions: {std_diag['cautions']}

[Student Submission]
Diagnosis: {user_diagnosis}
Point Prescription: {user_prescription}
Clinical Rationale & Technique: {user_rationale}

Provide a concise, expert TCM clinical critique in 2 paragraphs covering:
1. Diagnosis accuracy and pathology assessment.
2. Point prescription synergy, missing cardinal points, needle depths, or precautions (e.g. pregnancy or anatomical hazards).
Be clinically rigorous, constructive, and direct."""

            for model_name in ["gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-flash-latest"]:
                try:
                    resp = client.models.generate_content(model=model_name, contents=prompt)
                    if resp and resp.text:
                        ai_critique_section = f"""
#### 🤖 Gemini Clinical AI Professor Evaluation
> {resp.text.strip()}

---
"""
                        break
                except Exception:
                    continue
        except Exception:
            ai_critique_section = ""
    
    feedback_markdown = f"""
### 📊 Clinical Case Evaluation: **{case['title']}**

**Overall Score: `{total_score}/100` | Grade: `{grade}`**

> **Clinical Verdict:** {verdict}

---
{ai_critique_section}
#### 1. Pattern Diagnosis Analysis (`{diag_score}/30 pts`)
- **Your Input:** *"{user_diagnosis}"*
- **Textbook Consensus Patterns:** {', '.join(std_diag['patterns'])}
- **Recommended Principles:** {', '.join(std_diag['treatment_principles'])}

#### 2. Point Prescription Breakdown (`{point_score}/40 pts`)
- **Points Selected:** `{'`, `'.join([get_point_bilingual_name(p) for p in presc_points]) if presc_points else 'None recognized'}`
- **✅ Cardinal Points Included:** {', '.join(bilingual_matched) if bilingual_matched else 'None'}
- **💡 Key Points to Consider Adding:** {', '.join(bilingual_missing) if bilingual_missing else 'All core points covered!'}

#### 3. Channel Theory & Synergy (`{synergy_score}/20 pts`)
- **Recognized Synergies:** {', '.join(synergy_notes) if synergy_notes else 'Standard point compilation'}
- **Textbook Point Pairing Pearls:**
{chr(10).join([f"  • {format_point_bilingual(s)}" for s in std_diag['synergies']])}

#### 4. Safety & Textbook Variations (`{caution_score}/10 pts`)
- **Clinical Precautions:** {format_point_bilingual(std_diag['cautions'])}
- **📚 Multi-Textbook Variations:**
  • **CAM:** Prioritizes classical channel pairs and standard needle depths for tonification vs dispersal.
  • **Deadman:** Highlights precise anatomical dangers, safe needle angles, and distal empirical combinations.
  • **Maciocia:** Emphasizes treating the underlying root (Ben) vs acute manifestation (Biao).
"""

    # Save to SQLite Case History
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO case_history (case_id, case_title, patient_profile, user_diagnosis, user_prescription, score, feedback_markdown)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        case_id,
        case["title"],
        f"{case['patient']['gender']}, {case['patient']['age']}yo - {case['patient']['chief_complaint']}",
        user_diagnosis,
        user_prescription,
        total_score,
        feedback_markdown
    ))
    conn.commit()
    conn.close()
    
    return {
        "score": total_score,
        "grade": grade,
        "verdict": verdict,
        "diag_score": diag_score,
        "point_score": point_score,
        "synergy_score": synergy_score,
        "caution_score": caution_score,
        "matched_points": matched_points,
        "missing_cardinal": missing_cardinal,
        "feedback_markdown": feedback_markdown
    }


def get_case_history() -> List[Dict[str, Any]]:
    """Retrieve past clinical case study evaluations from SQLite."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM case_history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

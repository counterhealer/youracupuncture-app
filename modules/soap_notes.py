"""1-Click Patient SOAP Note & Treatment Plan Generator (临床病历与SOAP记录生成).

Enables students and clinicians to rapidly synthesize patient presentation, Four Examinations,
TCM pattern differentiation, and clinical prescriptions into standard medical SOAP charts.
Includes live export, printable medical chart views, and 1-click pre-fills from Diagnostics and Pain Map.
"""

from typing import Dict, Any
from datetime import date
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def init_soap_state():
    """Ensure session state keys for SOAP note exist."""
    if "soap_data" not in st.session_state:
        st.session_state.soap_data = {
            "patient_name": "Patient #1042",
            "patient_age": 38,
            "patient_gender": "Female",
            "visit_date": str(date.today()),
            "chief_complaint": "Persistent occipital headache and stiff neck with chills for 3 days following cold wind exposure.",
            "duration": "3 days",
            "modalities": "Worse with cold drafts and air conditioning; relieved by warm shower and hot tea.",
            "secondary_symptoms": "Aversion to cold, clear runny nose, absence of sweating, slight cough with white watery phlegm.",
            "tongue_body": "Normal Pale Red",
            "tongue_coat": "Thin White, slightly moist",
            "pulse_qualities": "Floating and Tight (浮紧)",
            "palpation_findings": "Marked tenderness at bilateral GB20 (Fengchi) and upper trapezius; no swelling.",
            "tcm_diagnosis": "Acute Wind-Cold Invading Exterior (风寒束表证)",
            "eight_principles": "Exterior, Excess, Cold, Yang",
            "pathogenesis": "Exogenous Wind-Cold pathogen constricting Wei Qi and binding Lung protective circulation.",
            "western_correlate": "Acute viral upper respiratory infection / Occipital tension cervicogenic headache.",
            "primary_points": "LI4 (Hegu), LU7 (Lieque), GB20 (Fengchi), BL10 (Tianzhu), BL12 (Fengmen)",
            "needle_technique": "Sedating (Xie Fa) on LI4 & GB20; even method on LU7. Needle depth 0.5-1.0 cun. De Qi sensation obtained.",
            "retention_time": "25 minutes",
            "adjunctive_modalities": "Indirect Moxibustion to BL12 (Fengmen) & GV14 (Dazhui) for 10 minutes. Auricular seeds on Shen Men & Ear Lung.",
            "herbal_formula": "Jing Fang Bai Du San (荆防败毒散) or Gui Zhi Tang (桂枝汤)",
            "lifestyle_diet": "Dress warmly around the cervical spine, drink warm ginger-scallion decoction, avoid cold drinks and raw salads for 5 days.",
            "treatment_course": "2 sessions per week for 1-2 weeks; re-evaluate in 3 days."
        }


def format_soap_text(data: Dict[str, Any]) -> str:
    """Format SOAP note into clean medical markdown text."""
    return f"""# ACUPUNCTURE & TCM CLINICAL SOAP NOTE
**Date:** {data.get('visit_date', '')} | **Patient ID:** {data.get('patient_name', '')} | **Age/Gender:** {data.get('patient_age', '')} y/o {data.get('patient_gender', '')}

---

### S - SUBJECTIVE (主诉与问诊)
* **Chief Complaint:** {data.get('chief_complaint', '')}
* **Onset & Duration:** {data.get('duration', '')}
* **Aggravating / Relieving Factors:** {data.get('modalities', '')}
* **Associated Secondary Symptoms:** {data.get('secondary_symptoms', '')}

---

### O - OBJECTIVE (望闻问切 - 四诊体征)
* **Tongue Examination:** Body: {data.get('tongue_body', '')} | Coating: {data.get('tongue_coat', '')}
* **Pulse Examination:** {data.get('pulse_qualities', '')}
* **Physical & Palpatory Examination:** {data.get('palpation_findings', '')}

---

### A - ASSESSMENT (辨证论治与病机分析)
* **TCM Pattern Differentiation:** {data.get('tcm_diagnosis', '')}
* **Eight Principles Analysis:** {data.get('eight_principles', '')}
* **Pathogenesis Mechanism:** {data.get('pathogenesis', '')}
* **Western Clinical Correlation:** {data.get('western_correlate', '')}

---

### P - PLAN (针灸处方与综合治疗方案)
* **Primary Acupoints Prescribed:** {data.get('primary_points', '')}
* **Needle Manipulation & Technique:** {data.get('needle_technique', '')}
* **Needle Retention Time:** {data.get('retention_time', '')}
* **Adjunctive Therapies:** {data.get('adjunctive_modalities', '')}
* **Canonical Herbal Formula:** {data.get('herbal_formula', '')}
* **Dietary & Lifestyle Advice:** {data.get('lifestyle_diet', '')}
* **Treatment Course & Follow-up Cadence:** {data.get('treatment_course', '')}

*Attending Acupuncturist / Clinician Signature: __________________________ L.Ac., Dipl. Ac.*
"""


def format_ehr_plain_text(data: Dict[str, Any]) -> str:
    """Format SOAP note into standard plain text ready for 1-click clipboard paste into EHR systems (Jane, Unified Practice, Charm)."""
    p_name = data.get('patient_name', 'Patient')
    p_age = data.get('patient_age', '')
    p_gender = data.get('patient_gender', '')
    p_info = f"({p_age}yo {p_gender})" if (p_age or p_gender) else ""
    return f"""PATIENT: {p_name} {p_info}
DATE: {data.get('visit_date', '')}

[S - SUBJECTIVE]
Chief Complaint: {data.get('chief_complaint', '')}
Onset & Duration: {data.get('duration', '')}
Aggravating/Relieving: {data.get('modalities', '')}
Secondary Symptoms: {data.get('secondary_symptoms', '')}

[O - OBJECTIVE]
Tongue: Body: {data.get('tongue_body', '')} | Coating: {data.get('tongue_coat', '')}
Pulse: {data.get('pulse_qualities', '')}
Palpation/Physical Exam: {data.get('palpation_findings', '')}

[A - ASSESSMENT]
TCM Pattern Differentiation: {data.get('tcm_diagnosis', '')}
Eight Principles: {data.get('eight_principles', '')}
Pathogenesis: {data.get('pathogenesis', '')}
Western Clinical Correlation: {data.get('western_correlate', '')}

[P - PLAN]
Acupoint Prescription: {data.get('primary_points', '')}
Needle Manipulation: {data.get('needle_technique', '')}
Retention Time: {data.get('retention_time', '')}
Adjunctive Therapies: {data.get('adjunctive_modalities', '')}
Herbal Formula: {data.get('herbal_formula', '')}
Diet & Lifestyle Guidance: {data.get('lifestyle_diet', '')}
Treatment Course & Cadence: {data.get('treatment_course', '')}

Signed: Licensed Acupuncturist (L.Ac. / Dipl. Ac.)
"""


def render_soap_notes_tab():
    """Render the SOAP Note Generator tab."""
    init_soap_state()

    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #38bdf8; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            📋 Patient Treatment Plan & SOAP Note Generator (临床病历与SOAP记录)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Standard clinical documentation engine for TCM practitioners and students. Synthesizes Subjective complaints, Objective Four Examinations, Assessment pattern differentiation, and Plan prescriptions into clean, printable charts.
        </p>
    </div>
    """)

    data = st.session_state.soap_data

    tab_edit, tab_preview = st.tabs(["✏️ Edit Clinical Case Records", "📄 Formatted Clinical Chart & Export"])

    with tab_edit:
        st.markdown("<h4 style='color: #ffffff !important; margin: 6px 0 12px 0;'>Patient Demographics & Encounter</h4>", unsafe_allow_html=True)
        c_p1, c_p2, c_p3, c_p4 = st.columns(4)
        with c_p1:
            data["patient_name"] = st.text_input("Patient Identifier / Name", value=data["patient_name"])
        with c_p2:
            data["patient_age"] = st.number_input("Age", min_value=1, max_value=120, value=int(data["patient_age"]))
        with c_p3:
            data["patient_gender"] = st.selectbox("Gender", options=["Female", "Male", "Other"], index=0 if data["patient_gender"]=="Female" else 1)
        with c_p4:
            data["visit_date"] = st.text_input("Encounter Date", value=data["visit_date"])

        # SECTION S
        render_clean_html("""
        <div style="background: rgba(0, 123, 167, 0.15); border-left: 4px solid #007ba7; padding: 8px 14px; border-radius: 4px; margin: 16px 0 10px 0;">
            <strong style="color: #38bdf8; font-size: 1.05rem;">S - SUBJECTIVE (主诉与病史)</strong>
        </div>
        """)
        data["chief_complaint"] = st.text_area("Chief Complaint (主诉)", value=data["chief_complaint"], height=68)
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            data["duration"] = st.text_input("Onset & Duration (病程)", value=data["duration"])
            data["modalities"] = st.text_input("Aggravating / Relieving Factors (加重/缓解因素)", value=data["modalities"])
        with col_s2:
            data["secondary_symptoms"] = st.text_area("Secondary Review of Systems (伴随症状)", value=data["secondary_symptoms"], height=95)

        # SECTION O
        render_clean_html("""
        <div style="background: rgba(200, 150, 102, 0.15); border-left: 4px solid #c89666; padding: 8px 14px; border-radius: 4px; margin: 16px 0 10px 0;">
            <strong style="color: #fde68a; font-size: 1.05rem;">O - OBJECTIVE (望闻问切四诊体征)</strong>
        </div>
        """)
        col_o1, col_o2 = st.columns(2)
        with col_o1:
            data["tongue_body"] = st.text_input("Tongue Body (舌质)", value=data["tongue_body"])
            data["tongue_coat"] = st.text_input("Tongue Coating (舌苔)", value=data["tongue_coat"])
        with col_o2:
            data["pulse_qualities"] = st.text_input("Pulse Qualities (脉象)", value=data["pulse_qualities"])
            data["palpation_findings"] = st.text_input("Palpation & Physical Exam (触诊/阿是穴)", value=data["palpation_findings"])

        # SECTION A
        render_clean_html("""
        <div style="background: rgba(72, 78, 178, 0.15); border-left: 4px solid #484eb2; padding: 8px 14px; border-radius: 4px; margin: 16px 0 10px 0;">
            <strong style="color: #c7d2fe; font-size: 1.05rem;">A - ASSESSMENT (辨证论治与病机)</strong>
        </div>
        """)
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            data["tcm_diagnosis"] = st.text_input("TCM Pattern Differentiation (中医辨证)", value=data["tcm_diagnosis"])
            data["eight_principles"] = st.text_input("Eight Principles (八纲)", value=data["eight_principles"])
        with col_a2:
            data["western_correlate"] = st.text_input("Western Medical Correlation (西医鉴别)", value=data["western_correlate"])
            data["pathogenesis"] = st.text_input("Pathogenesis Mechanism (病机分析)", value=data["pathogenesis"])

        # SECTION P
        render_clean_html("""
        <div style="background: rgba(16, 185, 129, 0.15); border-left: 4px solid #10b981; padding: 8px 14px; border-radius: 4px; margin: 16px 0 10px 0;">
            <strong style="color: #34d399; font-size: 1.05rem;">P - PLAN (治疗方案与针灸处方)</strong>
        </div>
        """)
        data["primary_points"] = st.text_area("Primary Acupoint Prescription (针灸处方)", value=data["primary_points"], height=68)
        col_p_a, col_p_b = st.columns(2)
        with col_p_a:
            data["needle_technique"] = st.text_input("Needle Technique & Manipulation (针刺手法)", value=data["needle_technique"])
            data["retention_time"] = st.text_input("Retention Time (留针时间)", value=data["retention_time"])
            data["adjunctive_modalities"] = st.text_input("Adjunctive Therapies (艾灸/拔罐/耳穴)", value=data["adjunctive_modalities"])
        with col_p_b:
            data["herbal_formula"] = st.text_input("Canonical Herbal Formula (中药方剂)", value=data["herbal_formula"])
            data["lifestyle_diet"] = st.text_input("Dietary & Lifestyle Advice (食疗起居指导)", value=data["lifestyle_diet"])
            data["treatment_course"] = st.text_input("Treatment Cadence (疗程规划)", value=data["treatment_course"])

    with tab_preview:
        soap_markdown = format_soap_text(data)
        ehr_plain = format_ehr_plain_text(data)

        col_dl, col_ehr = st.columns([1, 1], vertical_alignment="center")
        with col_dl:
            st.download_button(
                label="💾 Download Clinical SOAP Note (.md)",
                data=soap_markdown,
                file_name=f"SOAP_Note_{data['patient_name'].replace(' ', '_')}_{data['visit_date']}.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col_ehr:
            with st.popover("📋 Copy for EHR (Jane / Charm / Unified)", use_container_width=True):
                st.caption("Click the copy icon in the top right of this box to copy clean formatted text into your clinic EHR system:")
                st.code(ehr_plain, language="text")

        # Print-ready medical chart badge
        render_clean_html("""
        <div style="background: rgba(0, 123, 167, 0.12); border: 1px solid rgba(0, 123, 167, 0.3); border-radius: 8px; padding: 10px 16px; margin: 10px 0 16px 0; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 0.88rem; color: #38bdf8; font-weight: 600;">
                🖨️ <strong>Print-Ready Medical Chart:</strong> Press <code>Ctrl+P</code> (Windows) or <code>⌘+P</code> (Mac) to print or save as an official medical PDF chart.
            </span>
            <span style="font-size: 0.78rem; background: #007ba7; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-weight: 700;">
                EHR Standard
            </span>
        </div>
        """)

        # Render Clinical Card Preview
        render_clean_html(f"""
        <div style="background: #ffffff; color: #1e293b; border-radius: 8px; padding: 32px 36px; margin-top: 14px; box-shadow: 0 8px 30px rgba(0,0,0,0.5); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
            <div style="border-bottom: 2px solid #007ba7; padding-bottom: 12px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: flex-end;">
                <div>
                    <h2 style="margin: 0; color: #007ba7; font-size: 1.5rem; font-weight: 800;">CLINICAL ENCOUNTER & SOAP RECORD</h2>
                    <div style="font-size: 0.85rem; color: #64748b; margin-top: 3px;">TCM Acupuncture & Integrative Medicine Clinical Notes</div>
                </div>
                <div style="text-align: right; font-size: 0.88rem; color: #334155;">
                    <div><strong>Date:</strong> {data['visit_date']}</div>
                    <div><strong>Patient:</strong> {data['patient_name']} ({data['patient_age']} y/o {data['patient_gender']})</div>
                </div>
            </div>

            <!-- S -->
            <div style="margin-bottom: 18px;">
                <div style="font-weight: 800; font-size: 1.05rem; color: #007ba7; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; margin-bottom: 6px;">
                    S · SUBJECTIVE
                </div>
                <div style="font-size: 0.92rem; line-height: 1.5;">
                    <strong>Chief Complaint:</strong> {data['chief_complaint']}<br/>
                    <strong>Duration:</strong> {data['duration']} | <strong>Modalities:</strong> {data['modalities']}<br/>
                    <strong>Associated Review of Systems:</strong> {data['secondary_symptoms']}
                </div>
            </div>

            <!-- O -->
            <div style="margin-bottom: 18px;">
                <div style="font-weight: 800; font-size: 1.05rem; color: #c89666; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; margin-bottom: 6px;">
                    O · OBJECTIVE
                </div>
                <div style="font-size: 0.92rem; line-height: 1.5;">
                    <strong>Tongue:</strong> Body: {data['tongue_body']} · Coating: {data['tongue_coat']}<br/>
                    <strong>Pulse Qualities:</strong> {data['pulse_qualities']}<br/>
                    <strong>Palpation:</strong> {data['palpation_findings']}
                </div>
            </div>

            <!-- A -->
            <div style="margin-bottom: 18px;">
                <div style="font-weight: 800; font-size: 1.05rem; color: #484eb2; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; margin-bottom: 6px;">
                    A · ASSESSMENT
                </div>
                <div style="font-size: 0.92rem; line-height: 1.5;">
                    <strong>TCM Pattern Differentiation:</strong> <span style="font-weight: 700; color: #007ba7;">{data['tcm_diagnosis']}</span> ({data['eight_principles']})<br/>
                    <strong>Pathogenesis:</strong> {data['pathogenesis']}<br/>
                    <strong>Western Clinical Correlation:</strong> {data['western_correlate']}
                </div>
            </div>

            <!-- P -->
            <div style="margin-bottom: 18px;">
                <div style="font-weight: 800; font-size: 1.05rem; color: #10b981; border-bottom: 1px solid #cbd5e1; padding-bottom: 3px; margin-bottom: 6px;">
                    P · PLAN
                </div>
                <div style="font-size: 0.92rem; line-height: 1.55;">
                    <strong>Acupoint Prescription:</strong> <span style="font-weight: 700; color: #007ba7;">{data['primary_points']}</span><br/>
                    <strong>Needle Manipulation:</strong> {data['needle_technique']} | <strong>Retention:</strong> {data['retention_time']}<br/>
                    <strong>Adjunctive Therapies:</strong> {data['adjunctive_modalities']}<br/>
                    <strong>Herbal Prescription:</strong> {data['herbal_formula']}<br/>
                    <strong>Dietary / Lifestyle Advice:</strong> {data['lifestyle_diet']}<br/>
                    <strong>Treatment Schedule:</strong> {data['treatment_course']}
                </div>
            </div>

            <div style="border-top: 1px solid #cbd5e1; padding-top: 14px; margin-top: 24px; display: flex; justify-content: space-between; font-size: 0.85rem; color: #64748b;">
                <div>Confidential Medical Record · Licensed Acupuncturist Clinical Documentation</div>
                <div>Signed: __________________________ L.Ac.</div>
            </div>
        </div>
        """)

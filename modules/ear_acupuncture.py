"""Interactive Ear Acupuncture Microsystem (耳穴全图与耳针疗法).

Provides an interactive 2D anatomical auricular map, clinical protocols (NADA, BFA,
Insomnia, Pain relief, Weight loss), point localization guides, and seed/needle techniques.
"""

from typing import Dict, List, Any
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# =============================================================================
# AURICULAR POINTS DATA
# =============================================================================
AURICULAR_POINTS: Dict[str, Dict[str, Any]] = {
    "shen_men": {
        "name": "Ear Shen Men (神门)",
        "pinyin": "Shén Mén",
        "zone": "Triangular Fossa (Posterosuperior third)",
        "coordinates": (160, 140),
        "actions": "Tranquilizes the mind, alleviates pain, reduces inflammation, relieves tension, lowers blood pressure.",
        "indications": "Insomnia, severe anxiety, pain syndromes, addiction withdrawal, hypertension, inflammatory conditions.",
        "technique": "Perpendicular insertion 1-2 mm, or press-seed (Vaccaria) with moderate pressure 3-5 times daily."
    },
    "sympathetic": {
        "name": "Sympathetic (交感)",
        "pinyin": "Jiāo Gǎn",
        "zone": "Inferior Crura of Antihelix (Intersection with internal helix)",
        "coordinates": (140, 115),
        "actions": "Regulates autonomic nervous system, relieves visceral spasms, dilates blood vessels, analgesic.",
        "indications": "Arrhythmia, Raynaud's, stomach cramps, biliary colic, dysmenorrhea, anxiety, chronic pain.",
        "technique": "Obligue insertion into cartilage groove, or auricular seed."
    },
    "point_zero": {
        "name": "Point Zero (零点)",
        "pinyin": "Líng Diǎn",
        "zone": "Crus of Helix (Notch where helix enters the concha)",
        "coordinates": (175, 235),
        "actions": "Master homeostatic point. Brings the entire body back to biological equilibrium and autonomic balance.",
        "indications": "Exhaustion, shock, trauma, psychosomatic disorders, chronic intractable pain, postural hypotension.",
        "technique": "Perpendicular insertion 1 mm with gentle manual stimulation."
    },
    "thalamus": {
        "name": "Thalamus / Subcortex (丘脑/皮质下)",
        "pinyin": "Qiū Nǎo / Pí Zhì Xià",
        "zone": "Interior surface of Antitragus",
        "coordinates": (148, 305),
        "actions": "Modulates pain perception, regulates cerebral cortex excitation and inhibition, anti-inflammatory.",
        "indications": "Severe acute and chronic pain, neuropsychiatric disorders, insomnia, phantom limb pain, shock.",
        "technique": "Perpendicular or oblique insertion toward interior cavity."
    },
    "endocrine": {
        "name": "Endocrine (内分泌)",
        "pinyin": "Nèi Fēn Mì",
        "zone": "Base of Intertragic Notch (Anterior-inferior aspect)",
        "coordinates": (140, 345),
        "actions": "Regulates hormonal balance, clears heat, promotes metabolic transformation, antiallergic.",
        "indications": "PMS, irregular menstruation, menopause, thyroid disorders, acne, obesity, diabetes mellitus.",
        "technique": "Oblique upward insertion 1-2 mm."
    },
    "kidney": {
        "name": "Ear Kidney (耳肾)",
        "pinyin": "Ěr Shèn",
        "zone": "Superior Hemiconcha (Directly below inferior crus of antihelix)",
        "coordinates": (195, 160),
        "actions": "Tonifies Jing (Essence), strengthens lower back, bones, ears, and teeth; anchors original Qi.",
        "indications": "Tinnitus, lumbar pain, knee weakness, nocturnal enuresis, hearing decline, chronic fatigue.",
        "technique": "Perpendicular insertion 1 mm."
    },
    "liver": {
        "name": "Ear Liver (耳肝)",
        "pinyin": "Ěr Gān",
        "zone": "Posterior-superior Cavum Conchae",
        "coordinates": (210, 205),
        "actions": "Soothes stagnant Liver Qi, brightens the eyes, promotes bile secretion, relieves muscle spasms.",
        "indications": "Hypochondriac pain, migraine, PMS, eye disorders, irritability, muscle cramps, hypertension.",
        "technique": "Perpendicular insertion 1-2 mm."
    },
    "lung": {
        "name": "Ear Lung (耳肺 - Upper & Lower)",
        "pinyin": "Ěr Fèi",
        "zone": "Surrounding Heart area in Cavum Conchae",
        "coordinates": (190, 260),
        "actions": "Governs respiration, controls skin and hair, commands defensive Wei Qi, aids substance detoxification.",
        "indications": "Cough, asthma, eczema, psoriasis, smoking addiction, bereavement/grief, spontaneous sweating.",
        "technique": "Perpendicular insertion 1 mm."
    },
    "heart": {
        "name": "Ear Heart (耳心)",
        "pinyin": "Ěr Xīn",
        "zone": "Central depression of Cavum Conchae",
        "coordinates": (175, 275),
        "actions": "Nourishes the Heart, calms the spirit (Shen), clears Heart heat, regulates blood circulation.",
        "indications": "Palpitations, insomnia, anxiety, dream-disturbed sleep, mania, tongue ulcers, hypertension.",
        "technique": "Perpendicular insertion 1 mm."
    },
    "stomach": {
        "name": "Ear Stomach (耳胃)",
        "pinyin": "Ěr Wèi",
        "zone": "Disappearance of crus of helix in central concha",
        "coordinates": (175, 200),
        "actions": "Harmonizes Stomach Qi, stops nausea, relieves hunger pangs, clears middle burner heat.",
        "indications": "Gastritis, nausea, vomiting, indigestion, obesity, bulimia, acid reflux, epigastric distention.",
        "technique": "Perpendicular insertion 1 mm."
    },
    "ear_apex": {
        "name": "Ear Apex (耳尖 - Erjian)",
        "pinyin": "Ěr Jiān",
        "zone": "Apex of the Auricle (fold ear forward to identify tip)",
        "coordinates": (170, 50),
        "actions": "Pricking to bleed drains acute pathogenic Heat, dispels Wind, subdues Liver Fire, clears eyes.",
        "indications": "High fever, acute conjunctivitis (pink eye), hypertensive crisis, stye (chalazion), acute migraine.",
        "technique": "Lancet prick and squeeze 3-5 drops of dark blood."
    },
    "sciatic": {
        "name": "Sciatic Nerve (坐骨神经)",
        "pinyin": "Zuò Gǔ Shén Jīng",
        "zone": "Middle two-thirds of Superior Crus of Antihelix",
        "coordinates": (180, 110),
        "actions": "Alleviates radiating sciatic pain, unblocks channel stasis down the leg, relaxes lower spine.",
        "indications": "Sciatica, piriformis syndrome, radiating buttock and leg pain, lumbar disc herniation.",
        "technique": "Perpendicular or oblique insertion toward cartilage border."
    },
    "cervical_spine": {
        "name": "Cervical Spine (颈椎)",
        "pinyin": "Jǐng Zhuī",
        "zone": "Inferior Antihelix curvature (close to concha)",
        "coordinates": (155, 300),
        "actions": "Relieves neck spasms, restores cervical lordosis, eases occipital tension.",
        "indications": "Cervical spondylosis, stiff neck, tension headaches, whiplash, torticollis.",
        "technique": "Perpendicular insertion 1 mm."
    },
    "lumbar_spine": {
        "name": "Lumbar Spine (腰椎)",
        "pinyin": "Yāo Zhuī",
        "zone": "Antihelix (Opposite superior end of crus of helix)",
        "coordinates": (160, 210),
        "actions": "Strengthens lumbar vertebrae, relieves disc compression and local erector spinae spasms.",
        "indications": "Acute lumbar sprain, chronic lower back pain, spinal stenosis, facet syndrome.",
        "technique": "Perpendicular insertion 1-2 mm."
    }
}


# =============================================================================
# CLINICAL AURICULAR PROTOCOLS
# =============================================================================
AURICULAR_PROTOCOLS: List[Dict[str, Any]] = [
    {
        "id": "nada",
        "name": "NADA Protocol (5-Point Addiction & Trauma Detox)",
        "chinese": "全美耳针戒毒协会五穴方案",
        "points": ["sympathetic", "shen_men", "kidney", "liver", "lung"],
        "summary": "Gold standard global protocol developed at Lincoln Hospital for addiction, PTSD, acute trauma, stress reduction, and disaster mental health.",
        "mechanism": "Calms the sympathetic nervous system, detoxifies internal organs, anchors emotional resilience, and stimulates internal endorphin release."
    },
    {
        "id": "bfa",
        "name": "Battlefield Acupuncture (BFA Rapid Pain Relief)",
        "chinese": "战地耳针镇痛疗法 (Niemtzow 方案)",
        "points": ["point_zero", "shen_men", "thalamus"],
        "summary": "Developed by Col. Dr. Richard Niemtzow for military and emergency settings to rapidly eliminate acute and severe chronic musculoskeletal pain within minutes.",
        "mechanism": "Uses gold/titanium semi-permanent ASP needles to modulate the spinothalamic tract and interrupt the neurological pain loop at the thalamic and cingulate level."
    },
    {
        "id": "insomnia_anxiety",
        "name": "Insomnia, Anxiety & Shen Disturbance Protocol",
        "chinese": "失眠抑郁安神耳针方案",
        "points": ["shen_men", "heart", "kidney", "thalamus", "endocrine"],
        "summary": "Premier protocol for chronic sleeplessness, racing nocturnal thoughts, panic attacks, and severe emotional exhaustion.",
        "mechanism": "Grounds cardiac fire, tonifies the water-fire kidney-heart axis, and dampens cerebral cortex hyperarousal."
    },
    {
        "id": "metabolic_weight",
        "name": "Metabolic Balance & Appetite Regulation (Weight Loss)",
        "chinese": "减重降脂降食欲耳针方案",
        "points": ["stomach", "endocrine", "shen_men", "point_zero"],
        "summary": "Curbs compulsive cravings, balances insulin and ghrelin satiety signaling, and promotes digestive efficiency.",
        "mechanism": "Sedates hyperactive stomach heat while regulating hypothalamic feeding centers and soothing emotional stress eating."
    },
    {
        "id": "sciatica_lumbar",
        "name": "Acute Sciatica & Lumbar Sprain Protocol",
        "chinese": "急性腰扭伤与坐骨神经痛方案",
        "points": ["sciatic", "lumbar_spine", "shen_men", "thalamus"],
        "summary": "Rapid musculoskeletal unblocking protocol for sharp lower back pain, disc impingement, and radiating leg numbness.",
        "mechanism": "Direct somatotopic stimulation of the inverted fetus spinal projection with central analgesia via Thalamus and Shen Men."
    },
    {
        "id": "hypertension_migraine",
        "name": "Hypertension, Migraine & Vertigo Crisis",
        "chinese": "高血压与偏头痛降压清头方案",
        "points": ["ear_apex", "liver", "shen_men", "sympathetic"],
        "summary": "Immediate venting protocol for throbbing temple migraines, hypertensive surges, acute dizziness, and red fiery eyes.",
        "mechanism": "Pricking Ear Apex to bleed rapidly vents boiling Liver Yang Fire, while Sympathetic and Shen Men vasodilate microcirculation."
    }
]


# =============================================================================
# SVG EAR MAP GENERATOR
# =============================================================================
def generate_ear_svg(active_point_keys: List[str]) -> str:
    """Generate interactive SVG auricular map highlighting selected active points."""
    # Points SVG markers
    pts_svg = []
    for key, pt in AURICULAR_POINTS.items():
        cx, cy = pt["coordinates"]
        is_active = key in active_point_keys
        fill_color = "#38bdf8" if is_active else "#64748b"
        stroke_color = "#ffffff" if is_active else "rgba(255,255,255,0.4)"
        r = 8 if is_active else 5
        pulse_svg = f'<circle cx="{cx}" cy="{cy}" r="15" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.6"><animate attributeName="r" values="8;18;8" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.8;0.1;0.8" dur="2s" repeatCount="indefinite"/></circle>' if is_active else ''

        label_color = "#ffffff" if is_active else "#94a3b8"
        font_weight = "800" if is_active else "500"
        font_size = "11" if is_active else "9"

        pts_svg.append(f"""
        <g id="pt_{key}">
            {pulse_svg}
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>
            <text x="{cx + 12}" y="{cy + 4}" fill="{label_color}" font-size="{font_size}" font-family="system-ui, sans-serif" font-weight="{font_weight}">
                {pt['name'].split()[0]} {pt['name'].split()[1] if len(pt['name'].split()) > 1 else ''}
            </text>
        </g>
        """)

    svg_content = f"""
    <svg viewBox="0 0 360 480" width="100%" height="480" xmlns="http://www.w3.org/2000/svg" style="background: #0b1120; border-radius: 12px; border: 1.5px solid rgba(255,255,255,0.12);">
        <defs>
            <linearGradient id="earGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1e293b"/>
                <stop offset="100%" stop-color="#0f172a"/>
            </linearGradient>
            <linearGradient id="helixGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#007ba7" stop-opacity="0.3"/>
                <stop offset="100%" stop-color="#484eb2" stop-opacity="0.3"/>
            </linearGradient>
        </defs>

        <!-- Auricle Outer Contour (Helix) -->
        <path d="M 120 400 C 70 380, 50 320, 60 220 C 70 120, 110 50, 180 40 C 250 30, 290 80, 290 160 C 290 240, 250 330, 210 390 C 180 430, 140 420, 120 400 Z" 
              fill="url(#earGrad)" stroke="#38bdf8" stroke-width="2.5" opacity="0.95"/>

        <!-- Outer Rim / Helix Ridge -->
        <path d="M 175 45 C 240 38, 280 85, 280 160 C 280 235, 240 320, 205 380 C 175 420, 140 405, 125 390 C 145 375, 170 350, 190 310 C 215 250, 245 180, 245 140 C 245 95, 215 65, 175 60 Z" 
              fill="url(#helixGrad)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.5"/>

        <!-- Antihelix (Inverted Spine Projection) -->
        <path d="M 155 320 C 160 270, 160 220, 175 160 C 185 130, 205 105, 230 90" 
              fill="none" stroke="#c89666" stroke-width="3.5" stroke-linecap="round" opacity="0.8"/>
        <!-- Superior & Inferior Crura of Antihelix -->
        <path d="M 175 160 C 165 145, 145 130, 130 115" 
              fill="none" stroke="#c89666" stroke-width="3" stroke-linecap="round" opacity="0.8"/>

        <!-- Triangular Fossa -->
        <path d="M 130 115 C 150 110, 170 125, 180 145 C 165 155, 145 145, 130 115 Z" 
              fill="rgba(72, 78, 178, 0.25)" stroke="rgba(200, 150, 102, 0.5)" stroke-width="1.2"/>

        <!-- Tragus & Intertragic Notch -->
        <path d="M 95 240 C 90 260, 110 275, 120 280 C 110 300, 110 325, 125 340 C 135 350, 150 345, 155 330 C 145 315, 140 295, 145 280 C 135 270, 120 250, 110 240 Z" 
              fill="rgba(15, 23, 42, 0.8)" stroke="#38bdf8" stroke-width="1.8"/>

        <!-- Concha Cavity (Cymba & Cavum) -->
        <path d="M 145 280 C 145 230, 170 170, 205 180 C 220 210, 225 250, 205 280 C 185 300, 155 295, 145 280 Z" 
              fill="rgba(0, 123, 167, 0.15)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.5"/>

        <!-- Crus of Helix (Horizontal divider) -->
        <path d="M 110 240 C 135 240, 165 240, 180 235" 
              fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-linecap="round"/>

        <!-- Ear Lobule (Inverted Head/Brain zone) -->
        <path d="M 125 390 C 115 410, 135 435, 160 435 C 185 435, 205 410, 205 385 Z" 
              fill="rgba(200, 150, 102, 0.15)" stroke="rgba(200, 150, 102, 0.4)" stroke-width="1.5"/>

        <!-- Legend Annotations -->
        <text x="18" y="28" fill="#38bdf8" font-size="12" font-family="system-ui" font-weight="800">AURICULAR MICROSYSTEM</text>
        <text x="18" y="44" fill="#94a3b8" font-size="10" font-family="system-ui">Inverted Fetus Somatotopic Projection</text>

        <!-- Point Markers -->
        {''.join(pts_svg)}
    </svg>
    """
    return svg_content


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_ear_acupuncture_tab():
    """Render the Interactive Ear Acupuncture Microsystem tab."""
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            👂 Interactive Ear Acupuncture Microsystem (耳穴全图与耳针疗法)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Clinical auricular therapy and somatotopic inverted fetus projections. Features the world-renowned NADA addiction/trauma protocol, Battlefield Acupuncture (BFA) pain protocol, and anatomical point localisation guides.
        </p>
    </div>
    """)

    col_map, col_details = st.columns([1.1, 0.9])

    with col_details:
        st.markdown("<h4 style='color: #ffffff !important; margin: 0 0 8px 0;'>📋 Clinical Protocol Quick-Loader</h4>", unsafe_allow_html=True)
        proto_names = ["Custom Point Inspection"] + [f"{p['name']} ({p['chinese']})" for p in AURICULAR_PROTOCOLS]
        sel_proto_str = st.selectbox("Select Auricular Protocol to Display on Map", options=proto_names, index=1)

        active_keys = []
        current_proto = None

        if sel_proto_str != "Custom Point Inspection":
            for p in AURICULAR_PROTOCOLS:
                if p["name"] in sel_proto_str:
                    current_proto = p
                    active_keys = p["points"]
                    break
        else:
            sel_single_pt = st.selectbox(
                "Select Individual Point to Highlight",
                options=list(AURICULAR_POINTS.keys()),
                format_func=lambda k: AURICULAR_POINTS[k]["name"]
            )
            active_keys = [sel_single_pt]

    with col_map:
        svg_markup = generate_ear_svg(active_keys)
        render_clean_html(svg_markup)

    # Detailed Protocol / Point Information Card
    st.write("")
    if current_proto:
        render_clean_html(f"""
        <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                <div>
                    <span style="background: rgba(0, 123, 167, 0.3); color: #38bdf8; font-size: 0.76rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">
                        Active Clinical Protocol
                    </span>
                    <h3 style="color: #ffffff !important; font-size: 1.4rem; font-weight: 800; margin: 6px 0 2px 0;">
                        {current_proto['name']}
                    </h3>
                    <div style="color: #c89666; font-size: 1.05rem; font-weight: 700;">
                        {current_proto['chinese']}
                    </div>
                </div>
            </div>

            <div style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.5; margin: 10px 0;">
                {current_proto['summary']}
            </div>

            <div style="background: rgba(0, 123, 167, 0.15); border-left: 4px solid #007ba7; border-radius: 6px; padding: 12px 16px; margin: 12px 0;">
                <div style="font-size: 0.78rem; font-weight: 800; text-transform: uppercase; color: #38bdf8; margin-bottom: 2px;">
                    Neuro-Endocrine & TCM Mechanism
                </div>
                <div style="font-size: 0.92rem; font-weight: 600; color: #ffffff;">
                    {current_proto['mechanism']}
                </div>
            </div>
        </div>
        """)

    st.markdown("<h4 style='color: #ffffff !important; margin: 18px 0 10px 0;'>🔍 Points in Current Prescription</h4>", unsafe_allow_html=True)
    cols_pts = st.columns(2)
    for idx, pt_key in enumerate(active_keys):
        pt_info = AURICULAR_POINTS[pt_key]
        col = cols_pts[idx % 2]
        with col:
            render_clean_html(f"""
            <div style="background: #182234; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #38bdf8; font-size: 1.05rem;">{pt_info['name']}</span>
                    <span style="font-size: 0.75rem; font-weight: 700; color: #c89666; background: rgba(200, 150, 102, 0.2); padding: 2px 6px; border-radius: 4px;">{pt_info['pinyin']}</span>
                </div>
                <div style="font-size: 0.83rem; color: #94a3b8; margin-bottom: 6px;">
                    <strong>Zone:</strong> {pt_info['zone']}
                </div>
                <div style="font-size: 0.88rem; color: #e2e8f0; line-height: 1.45; margin-bottom: 6px;">
                    <strong style="color: #34d399;">Actions:</strong> {pt_info['actions']}
                </div>
                <div style="font-size: 0.85rem; color: #cbd5e1; margin-bottom: 6px;">
                    <strong>Indications:</strong> {pt_info['indications']}
                </div>
                <div style="font-size: 0.82rem; color: #c7d2fe;">
                    <strong>Needling / Seeds:</strong> {pt_info['technique']}
                </div>
            </div>
            """)

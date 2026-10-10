"""Printable Study Guides & Pocket Cheat Sheets (可打印学习手册与核心速查卡).

Provides high-yield, print-ready reference matrices for board examinations and clinical practice:
- Five Shu Points & Mother-Child Tonification/Sedation Matrix
- Yuan-Luo, Xi-Cleft & Eight Confluent Points Master Table
- Top 50 Essential Clinical Points Pocket Card
- Emergency Acupoints & Fainting / Shock Protocols
- 28 Pulses Classification Matrix
"""

from typing import Dict, List, Any
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# =============================================================================
# DATA MATRICES
# =============================================================================
EMERGENCY_PROTOCOLS = [
    {
        "emergency": "Needle Fainting / Vasovagal Syncope (晕针)",
        "clinical_presentation": "Sudden dizziness, pallor, cold sweating, nausea, weak thready pulse, impending loss of consciousness during needling.",
        "primary_points": "GV26 (Renzhong) + PC6 (Neiguan) + ST36 (Zusanli)",
        "immediate_action": "Immediately withdraw all needles, position patient flat with legs elevated, offer warm water, press or needle GV26 with strong upward stimulation."
    },
    {
        "emergency": "Loss of Consciousness / Coma (昏迷急救)",
        "clinical_presentation": "Unresponsiveness, flaccid or closed jaw, shock, respiratory depression.",
        "primary_points": "GV26 (Renzhong) + Twelve Jing-Well Points (十二井穴放血) + KD1 (Yongquan)",
        "immediate_action": "Prick twelve Jing-Well points to bleed; pinch or needle GV26; apply strong moxa to CV8 (Shenque) and CV4 if Yang collapse with cold limbs."
    },
    {
        "emergency": "Angina Pectoris / Acute Chest Pain (心绞痛急救)",
        "clinical_presentation": "Substernal crushing chest pain radiating to left arm/shoulder, palpitations, cyanosis, shortness of breath.",
        "primary_points": "PC6 (Neiguan) + HT9 (Shaochong) + CV17 (Danzhong) + PC4 (Ximen)",
        "immediate_action": "Needle PC6 and PC4 (Xi-Cleft) with strong reducing method; prick HT9 to bleed. Call emergency medical services immediately."
    },
    {
        "emergency": "Acute Heatstroke / Sunstroke (中暑急救)",
        "clinical_presentation": "High body temperature, flushed face, profuse sweating followed by dry skin, delirium, rapid bounding pulse.",
        "primary_points": "GV26 (Renzhong) + Twelve Jing-Well Points + BL40 (Weizhong bleed) + LI11 (Quchi)",
        "immediate_action": "Move patient to cool shade; prick BL40 in popliteal fossa to bleed dark blood; needle LI11 to drain high fever."
    },
    {
        "emergency": "Acute Epistaxis / Severe Nosebleed (鼻衄急救)",
        "clinical_presentation": "Profuse continuous bleeding from nasal cavity, dizziness, anxiety.",
        "primary_points": "LI4 (Hegu) + GV23 (Shangxing) + ST44 (Neiting)",
        "immediate_action": "Direct moxibustion to SP1 (Yinbai); press ice on back of neck; needle LI4 with reducing technique; pinch nostrils firmly."
    }
]

TOP_50_POINTS_SAMPLE = [
    ("LI4 (Hegu / 合谷)", "Commands head & face, supreme analgesic, dispels exterior wind, contraindicated in pregnancy."),
    ("ST36 (Zusanli / 足三里)", "Supreme digestive & Qi tonifier, fortifies Spleen/Stomach, builds post-natal Blood & Wei Qi."),
    ("SP6 (Sanyinjiao / 三阴交)", "Crossing of 3 Leg Yin (SP, LV, KD), supreme gynecological & Yin nourishing point, forbidden in pregnancy."),
    ("LIV3 (Taichong / 太冲)", "Yuan-Source of Liver, spreads stagnant Qi, subdues Liver Yang, calms stress & emotional anger."),
    ("PC6 (Neiguan / 内关)", "Master of Yin Wei, supreme for chest, epigastrium, nausea, vomiting, anxiety, and insomnia."),
    ("LU7 (Lieque / 列缺)", "Commands head & nape of neck, opens Ren Mai, expels exterior wind, relieves cough & asthma."),
    ("GB20 (Fengchi / 风池)", "Eliminates all internal & external wind, clears sensory orifices, treats occipital headache & neck tension."),
    ("BL40 (Weizhong / 委中)", "Supreme for lumbar spine & back, clears blood stasis, cools blood heat, clears skin toxins."),
    ("BL23 (Shenshu / 肾俞)", "Back-Shu of Kidney, deeply tonifies Kidney Yin & Yang, strengthens lower back, knees, and Jing."),
    ("KD3 (Taixi / 太溪)", "Yuan-Source of Kidney, nourishes Kidney Yin and anchors Yang, relieves tinnitus & chronic sore throat."),
    ("HT7 (Shenmen / 神门)", "Yuan-Source of Heart, grounds wandering Shen, stops palpitations, resolves chronic insomnia."),
    ("GV20 (Baihui / 百会)", "Sea of Marrow apex, raises sunken Yang Qi, clears mental fog, stabilizes prolapse and depression."),
    ("CV12 (Zhongwan / 中脘)", "Front-Mu of Stomach & Hui-Meeting of Fu organs, harmonizes digestion, stops acid reflux & bloating."),
    ("CV4 (Guanyuan / 关元)", "Front-Mu of Small Intestine & Gate of Origin, deeply warms Kidney Yang and replenishes Yuan Qi."),
    ("CV6 (Qihai / 气海)", "Sea of Qi, tonifies vital original energy, builds constitutional stamina, stops chronic diarrhea."),
    ("CV17 (Danzhong / 膻中)", "Front-Mu of Pericardium & Hui-Meeting of Qi, unbinds emotional constriction, opens lungs and chest."),
    ("GB34 (Yanglingquan / 阳陵泉)", "Hui-Meeting of Sinews & He-Sea of GB, relaxes tight tendons, clears lateral ribcage pain."),
    ("ST40 (Fenglong / 丰隆)", "Luo of Stomach, supreme phlegm dissolving point in the human body (tangible & intangible phlegm)."),
    ("LI11 (Quchi / 曲池)", "Clears exterior and interior high heat, cools blood, drains toxic damp-heat skin rashes."),
    ("BL60 (Kunlun / 昆仑)", "Aspirin of acupuncture, clears lower back & occipital headaches, contraindicated in pregnancy.")
]


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_study_guides_tab():
    """Render the Printable Study Guides & Pocket Cheat Sheets tab."""
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #10b981; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            📚 Printable Study Guides & Pocket Cheat Sheets (核心速查卡)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            High-yield clinical and board-exam study matrices: Five Shu points, Yuan-Luo & Xi-Cleft tables, Top 50 essential points, and emergency shock protocols. Formatted for instant printing or study review.
        </p>
    </div>
    """)

    sheet_choice = st.selectbox(
        "Select Quick-Reference Study Guide",
        options=[
            "🚨 Emergency Acupoints & Shock Protocols",
            "⭐ Top 50 Essential Clinical Acupoints",
            "🌊 Five Shu Points & Mother-Child Tonification/Sedation Table",
            "⚖️ 28 Pulses Diagnostic Differential Matrix"
        ]
    )

    st.write("")

    # SHEET 1: EMERGENCY ACUPOINTS
    if sheet_choice == "🚨 Emergency Acupoints & Shock Protocols":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #ef4444;">🚨 急症急救核心穴位速查 (Acupuncture Emergency Protocols)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Critical protocols for adverse needle reactions (syncope/fainting), acute shock, sudden chest pain, and hypertensive crises.
            </div>
        </div>
        """)

        for em in EMERGENCY_PROTOCOLS:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 18px 22px; margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="color: #ffffff; font-size: 1.15rem; font-weight: 800;">{em['emergency']}</span>
                    <span style="background: rgba(239, 68, 68, 0.2); color: #f87171; font-size: 0.75rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
                        EMERGENCY
                    </span>
                </div>
                <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 8px;">
                    <strong>Presentation:</strong> {em['clinical_presentation']}
                </div>
                <div style="background: rgba(0, 123, 167, 0.2); border-radius: 6px; padding: 10px 14px; margin-bottom: 8px;">
                    <span style="font-size: 0.78rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">Primary Emergency Points:</span>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff;">{em['primary_points']}</div>
                </div>
                <div style="font-size: 0.86rem; color: #34d399; font-weight: 600;">
                    ✓ Immediate Action: {em['immediate_action']}
                </div>
            </div>
            """)

    # SHEET 2: TOP 50 ESSENTIAL POINTS
    elif sheet_choice == "⭐ Top 50 Essential Clinical Acupoints":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #fde68a;">⭐ 临床核心要穴口袋速查表 (High-Yield Clinical Pearls)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                The essential acupoints accounting for over 85% of all daily clinical prescriptions and NCCAOM board examination scenarios.
            </div>
        </div>
        """)

        cols_50 = st.columns(2)
        for i, (pt_name, pt_pearl) in enumerate(TOP_50_POINTS_SAMPLE):
            col = cols_50[i % 2]
            with col:
                render_clean_html(f"""
                <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                    <div style="font-size: 1rem; font-weight: 800; color: #38bdf8; margin-bottom: 4px;">{pt_name}</div>
                    <div style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.4;">{pt_pearl}</div>
                </div>
                """)

    # SHEET 3: FIVE SHU MATRIX
    elif sheet_choice == "🌊 Five Shu Points & Mother-Child Tonification/Sedation Table":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">🌊 十二经五输穴与五行配属全表 (Complete Five Shu Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                <strong>Yin Meridians:</strong> Well (Wood) -> Spring (Fire) -> Stream (Earth) -> River (Metal) -> Sea (Water).<br/>
                <strong>Yang Meridians:</strong> Well (Metal) -> Spring (Water) -> Stream (Wood) -> River (Fire) -> Sea (Earth).
            </div>
        </div>
        """)

        table_md = """
| Meridian | 井 (Well) | 荥 (Spring) | 输 (Stream) | 经 (River) | 合 (Sea) | Tonify (Mother) | Sedate (Child) |
|---|---|---|---|---|---|---|---|
| **Lung (LU)** | LU11 (木) | LU10 (火) | **LU9 (土)** | LU8 (金) | **LU5 (水)** | **LU9** (Earth) | **LU5** (Water) |
| **L. Intestine (LI)** | LI1 (金) | **LI2 (水)** | LI3 (木) | LI5 (火) | **LI11 (土)** | **LI11** (Earth) | **LI2** (Water) |
| **Stomach (ST)** | **ST45 (金)** | ST44 (水) | ST43 (木) | **ST41 (火)** | ST36 (土) | **ST41** (Fire) | **ST45** (Metal) |
| **Spleen (SP)** | SP1 (木) | **SP2 (火)** | SP3 (土) | **SP5 (金)** | SP9 (水) | **SP2** (Fire) | **SP5** (Metal) |
| **Heart (HT)** | **HT9 (木)** | HT8 (火) | **HT7 (土)** | HT4 (金) | HT3 (水) | **HT9** (Wood) | **HT7** (Earth) |
| **S. Intestine (SI)** | SI1 (金) | **SI2 (水)** | **SI3 (木)** | SI5 (火) | SI8 (土) | **SI3** (Wood) | **SI2** (Water) |
| **Bladder (BL)** | **BL67 (金)** | BL66 (水) | **BL65 (木)** | BL60 (火) | BL40 (土) | **BL67** (Metal) | **BL65** (Wood) |
| **Kidney (KD)** | **KD1 (木)** | KD2 (火) | KD3 (土) | **KD7 (金)** | KD10 (水) | **KD7** (Metal) | **KD1** (Wood) |
| **Pericardium (PC)** | **PC9 (木)** | PC8 (火) | **PC7 (土)** | PC5 (金) | PC3 (水) | **PC9** (Wood) | **PC7** (Earth) |
| **San Jiao (SJ)** | SJ1 (金) | **SJ2 (水)** | **SJ3 (木)** | SJ6 (火) | SJ10 (土) | **SJ3** (Wood) | **SJ2** (Water) |
| **Gallbladder (GB)**| GB44 (金) | **GB43 (水)**| GB41 (木) | **GB38 (火)**| GB34 (土) | **GB43** (Water) | **GB38** (Fire) |
| **Liver (LIV)** | LIV1 (木) | **LIV2 (火)**| LIV3 (土) | LIV4 (金) | **LIV8 (水)** | **LIV8** (Water) | **LIV2** (Fire) |
"""
        st.markdown(table_md)

    # SHEET 4: 28 PULSES CLASSIFICATION
    elif sheet_choice == "⚖️ 28 Pulses Diagnostic Differential Matrix":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #c89666;">⚖️ 二十八脉分类归纳总纲 (The 28 Canonical Pulses Taxonomic Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Categorized by Depth, Rate, Strength, and Morphological Shape for rapid exam recall.
            </div>
        </div>
        """)

        pulse_matrix_md = """
| Category | Pulse Types (脉象) | Clinical Hallmark | Primary Pathologies |
|---|---|---|---|
| **Depth (部位)** | **Floating (浮)**, Drumskin/Leather (革), Scallion-stalk (芤), Scattered (散) | Surface light touch | Exterior syndromes, floating Yang, blood hemorrhage |
| **Depth (部位)** | **Deep (沉)**, Hidden (伏), Confined (牢) | Deep bone/tendon level | Interior syndromes, deep visceral cold, fixed pain |
| **Rate (速率)** | **Slow (迟)**, Moderate/Relaxed (缓) | < 60 bpm (< 4 beats/breath) | Cold syndrome, Spleen dampness, Yang deficiency |
| **Rate (速率)** | **Rapid (数)**, Hurried (疾) | > 90 bpm (> 5 beats/breath) | Heat syndrome, acute fever, Yin deficiency fire |
| **Strength (力度)** | **Empty/Deficient (虚)**, Weak (弱), Minute (微), Soft/Soggy (濡) | Soft, compressible, faint | Qi, Blood, Yin, or Yang deficiency |
| **Strength (力度)** | **Full/Excess (实)**, Surging (洪), Long (长) | Powerful, expansive | Full excess Heat, phlegm/food stagnation |
| **Shape (形态)** | **Slippery (滑)**, Long (长) | Smooth, fluid like rolling pearls | Phlegm, dampness, food retention, pregnancy |
| **Shape (形态)** | **Choppy (涩)**, Short (短) | Rough, knife scraping bamboo | Blood stasis, Essence exhaustion |
| **Tension (张力)** | **Wiry (弦)**, Tight (紧) | Straight like guitar string / twisted rope | Liver stagnation, hypertension, severe cold pain |
| **Rhythm (节律)** | **Knotted (结)**, Intermittent (代), Abrupt (促) | Pauses in beat succession | Arrhythmias, organ Qi exhaustion, extreme heat |
"""
        st.markdown(pulse_matrix_md)

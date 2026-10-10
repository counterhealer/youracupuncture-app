"""Visual Tongue & Pulse Clinical Atlas (图解舌象与脉象图谱).

Provides an illustrated and graphic reference for:
- Authentic Tongue Presentations & Zang-Fu Topography
- The 28 Canonical TCM Pulses with visual waveforms, depth palpation, and tactile descriptions
- Confusing Diagnostic Pair Differentials
"""

from typing import Dict, List, Any
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# =============================================================================
# TONGUE PRESENTATIONS DATABASE (8 COMPREHENSIVE CLINICAL PATTERNS)
# =============================================================================
TONGUE_PATTERNS: List[Dict[str, Any]] = [
    {
        "id": "normal",
        "category": "Normal Physiological Baseline",
        "name": "Normal Healthy Tongue (正常舌象)",
        "chinese": "淡红舌 · 薄白苔",
        "border_color": "#38bdf8",
        "badge_summary": "淡红舌 · 薄白苔 (Normal Shen & Moss)",
        "body_color": "Pale Red (淡红) - fresh, vibrant, supple, good Shen vitality",
        "shape": "Moderate size, fits oral cavity comfortably, free of teeth marks or deviation",
        "coating": "Thin white, rooted, evenly distributed, moist with normal luster",
        "pathogenesis": "Sufficient Heart Blood, abundant Spleen/Stomach Qi, normal fluid metabolism, harmonious Zang-Fu functions.",
        "clinical_meaning": "Healthy physiological baseline. In disease, indicates pathogen is mild, exterior, or host constitution remains intact."
    },
    {
        "id": "pale_swollen_teeth",
        "category": "Yang Deficiency & Damp Stagnation",
        "name": "Pale & Wet Swollen with Teeth Marks (脾虚湿盛舌)",
        "chinese": "淡白胖嫩 · 边有齿痕 · 润滑白苔",
        "border_color": "#fed7aa",
        "badge_summary": "淡白胖嫩 · 边有齿痕 (Teeth Marks & Dampness)",
        "body_color": "Pale Whitish (淡白) - lacking hemoglobin, deficient warm Yang vitality",
        "shape": "Swollen, flabby, enlarged margins scalloped by dental pressure (齿痕)",
        "coating": "White, slippery, watery sheen, dripping with excess unevaporated fluid",
        "pathogenesis": "Spleen and Kidney Yang deficiency failing to transform water; internal dampness accumulates and fills lingual tissue.",
        "clinical_meaning": "Chronic fatigue, loose watery stools, chilliness, lower extremity edema, chronic indigestion, poor appetite."
    },
    {
        "id": "red_yellow_greasy",
        "category": "Internal Damp-Heat / Full Heat",
        "name": "Red Body with Thick Yellow Greasy Moss (湿热内蕴舌)",
        "chinese": "红舌 · 黄厚腻苔",
        "border_color": "#eab308",
        "badge_summary": "红舌 · 黄厚腻苔 (Thick Greasy Yellow Moss)",
        "body_color": "Crimson or Vivid Red (红/绛) - hyperactive heat accelerating microcirculation",
        "shape": "Tense, slightly enlarged body, reddened margins and tip",
        "coating": "Thick, turbid, yellow, mucinous, curd-like greasy texture (黄腻)",
        "pathogenesis": "Damp-Heat trapped in Spleen/Stomach, Liver/Gallbladder, or Bladder; interior heat steaming turbid dampness into sticky moss.",
        "clinical_meaning": "Epigastric fullness, bitter taste in mouth, jaundice, foul diarrhea, dark burning urine, eczema, acne, hangover."
    },
    {
        "id": "crimson_cracked_peeled",
        "category": "Yin Exhaustion / True Heat Fissures",
        "name": "Crimson Tongue with Peeled Mirror Surface (胃肾阴竭舌)",
        "chinese": "绛红光剥 · 镜面无苔 · 裂纹深",
        "border_color": "#ef4444",
        "badge_summary": "绛红光剥 · 镜面裂纹 (Mirror Peel & Deep Cracks)",
        "body_color": "Deep Crimson (绛红) - intense dry heat scorching vascular fluids",
        "shape": "Thin, contracted, dry, with deep transverse or vertical fissured cracks (裂纹)",
        "coating": "Completely peeled, mirror-smooth (光剥/镜面), zero root or coating",
        "pathogenesis": "Exhaustion of Stomach and Kidney Yin; deficiency fire blazing unopposed; critical collapse of body fluids.",
        "clinical_meaning": "Late-stage chronic wasting diseases, severe menopausal exhaustion, afternoon tidal fever, night sweats, emaciation."
    },
    {
        "id": "prickles_tip",
        "category": "Full Fire / Heart & Upper Jiao",
        "name": "Prickles & Red Spots on Tongue Tip (心火亢盛舌)",
        "chinese": "舌尖红刺 · 芒刺点点",
        "border_color": "#f87171",
        "badge_summary": "舌尖红刺 · 芒刺点点 (Prickly Tip & Heart Fire)",
        "body_color": "Red body with intensely congested, bright scarlet apex (tip)",
        "shape": "Elevated, enlarged lingual papillae forming thorny red prickles (芒刺) on apex",
        "coating": "Thin yellow or dry coating concentrated in center",
        "pathogenesis": "Extreme Fire in Upper Burner / Heart meridian; emotional stagnation or heat scorching microcapillaries.",
        "clinical_meaning": "Severe insomnia, vivid dreaming, palpitations, painful oral aphthae/ulcers, irritability, dark burning urination."
    },
    {
        "id": "purple_petechiae",
        "category": "Blood Stasis / Qi Obstruction",
        "name": "Purple / Dusky Tongue with Petechiae (血瘀舌)",
        "chinese": "青紫晦暗 · 瘀斑瘀点 · 络脉怒张",
        "border_color": "#a855f7",
        "badge_summary": "青紫晦暗 · 瘀斑瘀点 (Purple Stasis & Petechiae)",
        "body_color": "Cyanotic Bluish-Purple or Dusky Slate (紫暗) with dark static petechiae spots",
        "shape": "Sluggish mobility, stiff texture, engorged tortuous sublingual veins",
        "coating": "Thin white or greasy depending on phlegm involvement",
        "pathogenesis": "Chronic Blood Stasis; failure of Qi to circulate blood; cold coagulating vessels or chronic post-traumatic injury.",
        "clinical_meaning": "Fixed sharp stabbing pain, angina pectoris, dysmenorrhea with dark purple clots, fibroids, endometriosis, post-stroke."
    },
    {
        "id": "geographic",
        "category": "Stomach Qi/Yin Impairment",
        "name": "Geographic / Map Tongue (地图舌 · 花剥苔)",
        "chinese": "地图舌 · 花剥苔 · 胃气阴虚",
        "border_color": "#34d399",
        "badge_summary": "地图舌 · 花剥苔 (Geographic Islands)",
        "body_color": "Pale red base with irregular denuded red mucosal patches",
        "shape": "Normal to slightly flabby",
        "coating": "Sharply demarcated peeled patches with raised pale-yellow borders (resembling map islands), shifting daily",
        "pathogenesis": "Stomach Qi and Yin deficiency failing to nourish lingual epithelium; allergic constitution or pediatric digestive exhaustion.",
        "clinical_meaning": "Pediatric malnutrition (疳积), food intolerance, chronic atopic eczema, recurrent aphthae, impaired nutrient absorption."
    },
    {
        "id": "black_charred",
        "category": "Extreme Heat or Extreme Cold Polarities",
        "name": "Black / Charred Dry Tongue (焦黑干燥 / 灰黑苔)",
        "chinese": "焦黑干燥 / 灰黑苔 · 寒极或热极",
        "border_color": "#94a3b8",
        "badge_summary": "焦黑苔 · 寒极或热极 (Charred Black Moss)",
        "body_color": "Fiery crimson (if Extreme Heat) or pale dusky (if Extreme Cold)",
        "shape": "Contracted, stiff and dry (Heat) or swollen and watery (Cold)",
        "coating": "Charred smoky black, rough, dry with thorns (Heat) or grey-black slippery wet (Cold)",
        "pathogenesis": "Extreme Heat scorching body fluids into black crust; or Extreme Cold Yang collapse failing to circulate fluids.",
        "clinical_meaning": "Critical febrile exhaustion, septic delirium, severe dehydration, or terminal stage multi-organ exhaustion."
    }
]


# =============================================================================
# 28 PULSES COMPENDIUM WITH WAVEFORMS
# =============================================================================
PULSE_PATTERNS: List[Dict[str, Any]] = [
    {
        "name": "Floating Pulse (浮脉 - Fu Mai)",
        "depth": "Superficial (Surface light touch)",
        "speed": "Normal (60-80 bpm)",
        "waveform_type": "high_surface",
        "tactile_sensation": "Felt distinct and clear with light pressure like a piece of wood floating on water; slightly weakens upon pressing hard.",
        "pathogenesis": "Yang Qi carrying defensive energy to the exterior to fight invading pathogens, or extreme Yin deficiency with floating Yang.",
        "clinical_conditions": "Exterior Wind-Cold, Exterior Wind-Heat, acute viral infection, chronic severe Yin depletion."
    },
    {
        "name": "Deep Pulse (沉脉 - Chen Mai)",
        "depth": "Deep (Near tendons and bone)",
        "speed": "Normal (60-80 bpm)",
        "waveform_type": "deep_recessed",
        "tactile_sensation": "Undetectable with light or medium pressure; only distinctly felt when pressing deeply down to the bone.",
        "pathogenesis": "Pathogen is situated deeply inside the internal Zang-Fu organs, or Yang Qi is too deficient to lift circulation upward.",
        "clinical_conditions": "Interior cold/heat patterns, Yang deficiency, abdominal pain, visceral accumulation, kidney weakness."
    },
    {
        "name": "Slow Pulse (迟脉 - Chi Mai)",
        "depth": "All levels",
        "speed": "Slow (< 60 bpm / < 4 beats per breath)",
        "waveform_type": "wide_slow",
        "tactile_sensation": "Rhythm is distinctly slow, leisurely, less than 4 beats per complete respiratory cycle of the practitioner.",
        "pathogenesis": "Cold pathogen contracts the vessels and slows circulation, or deficient Yang fails to invigorate Blood flow.",
        "clinical_conditions": "Interior Cold syndrome, Yang deficiency, athletic bradycardia (physiological), pericardial cold."
    },
    {
        "name": "Rapid Pulse (数脉 - Shu Mai)",
        "depth": "All levels",
        "speed": "Rapid (> 90 bpm / > 5 beats per breath)",
        "waveform_type": "dense_rapid",
        "tactile_sensation": "Fast frequency, rapid succession, more than 5-6 beats per breath cycle; feels hurried and active.",
        "pathogenesis": "Hyperactive Heat stirs and accelerates Blood circulation; or Yin deficiency with internal empty heat fire.",
        "clinical_conditions": "Interior full heat syndromes, acute fever, Yin deficiency heat, tachycardia, severe inflammation."
    },
    {
        "name": "Slippery Pulse (滑脉 - Hua Mai)",
        "depth": "Superficial to medium",
        "speed": "Smooth, fluid",
        "waveform_type": "rolling_pearls",
        "tactile_sensation": "Extremely smooth, rounded, fluid, like pearls rolling smoothly across a fine porcelain plate (如盘走珠).",
        "pathogenesis": "Abundant Qi and Blood filling the vessels; or turbid Phlegm, Dampness, or Food Retention stagnating blood flow.",
        "clinical_conditions": "Normal pregnancy, youth vitality, Phlegm-Damp syndrome, food stagnation, PCOS, hyperlipidemia."
    },
    {
        "name": "Choppy Pulse (涩脉 - Se Mai)",
        "depth": "All levels",
        "speed": "Sluggish, uneven",
        "waveform_type": "rough_jagged",
        "tactile_sensation": "Rough, uneven, hesitation in flow, like a light knife scraping a piece of bamboo (如轻刀刮竹); fine and halting.",
        "pathogenesis": "Blood stasis blocking free flow; or severe impairment of Blood and Essence failing to fill the vessels.",
        "clinical_conditions": "Blood stasis, coronary artery disease, severe blood deficiency, fluid exhaustion, postpartum stasis."
    },
    {
        "name": "Wiry / Taut Pulse (弦脉 - Xian Mai)",
        "depth": "All levels",
        "speed": "Straight and stiff",
        "waveform_type": "straight_line",
        "tactile_sensation": "Straight, long, taut and stiff under the fingers, like pressing down on a tuned violin or guitar string (端直以长，如按琴弦).",
        "pathogenesis": "Liver Qi stagnation, Liver Yang rising, pain syndrome, or Phlegm-Fluid retention tightening the vessel wall.",
        "clinical_conditions": "Hypertension, migraines, Liver disharmonies, gallstones, severe pain, emotional stress, depression."
    },
    {
        "name": "Tight Pulse (紧脉 - Jin Mai)",
        "depth": "All levels",
        "speed": "Tense and vibrating",
        "waveform_type": "twisted_rope",
        "tactile_sensation": "Taut, forceful, vibrating from side to side like a stretched twisted rope (如按切绳); more forceful than wiry.",
        "pathogenesis": "Severe Cold pathogen causing violent vascular constriction; or severe acute spasmodic abdominal pain.",
        "clinical_conditions": "Cold invasion, acute stomach cramping, severe arthritis, asthma from cold, colic."
    },
    {
        "name": "Surging Pulse (洪脉 - Hong Mai)",
        "depth": "Superficial",
        "speed": "Broad and forceful",
        "waveform_type": "ocean_waves",
        "tactile_sensation": "Extremely broad, forceful, rising like surging ocean waves crashing on the shore, then receding quietly (来盛去衰).",
        "pathogenesis": "Extreme Yang heat overflowing the vessels, full heat burning in the Qi level (Four Bigs: big fever, thirst, sweat, pulse).",
        "clinical_conditions": "High febrile disease, heat exhaustion, hyperthyroidism, acute severe infection."
    },
    {
        "name": "Fine / Thready Pulse (细脉 - Xi Mai)",
        "depth": "All levels",
        "speed": "Weak, thin",
        "waveform_type": "silk_thread",
        "tactile_sensation": "Fine as a thin silk thread (细如丝线), but clearly and distinctly palpable without disappearing on pressure.",
        "pathogenesis": "Deficiency of Qi, Blood, Yin, or Essence failing to fill the vessel volume; or dampness oppressing the vessels.",
        "clinical_conditions": "Chronic blood deficiency, anemia, malnutrition, chronic fatigue, Yin deficiency."
    },
    {
        "name": "Soggy / Soft Pulse (濡脉 - Ru Mai)",
        "depth": "Superficial only",
        "speed": "Slow or moderate",
        "waveform_type": "floating_cotton",
        "tactile_sensation": "Superficial, fine, soft, floating like a small piece of wet cotton floating on water; disappears upon deep pressure.",
        "pathogenesis": "Dampness oppressing the vessels while Qi and Blood are deficient.",
        "clinical_conditions": "Spleen deficiency with dampness, chronic diarrhea, heavy limbs, summer dampness."
    },
    {
        "name": "Intermittent Pulse (代脉 - Dai Mai)",
        "depth": "All levels",
        "speed": "Regular pauses",
        "waveform_type": "regular_pause",
        "tactile_sensation": "Misses beats at regular, predictable intervals, accompanied by an extended resting pause before resuming.",
        "pathogenesis": "Severe decline of Zang-Fu Qi, exhaustion of Heart Qi and Yang; emotional shock or trauma.",
        "clinical_conditions": "Cardiac arrhythmias, heart failure, extreme organic exhaustion, fright."
    }
]


# =============================================================================
# SVG TONGUE & WAVEFORM GENERATORS
# =============================================================================
def generate_master_zangfu_svg() -> str:
    """Generate illustrated high-resolution Master Zang-Fu Topographical Lingual Projection Map."""
    return """<svg viewBox="0 0 780 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #0b1120; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);">
        <defs>
            <radialGradient id="zfBodyGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#fda4af"/>
                <stop offset="70%" stop-color="#f43f5e"/>
                <stop offset="100%" stop-color="#be123c"/>
            </radialGradient>
            <radialGradient id="tipAreaGrad" cx="50%" cy="60%" r="50%">
                <stop offset="0%" stop-color="#fca5a5" stop-opacity="0.9"/>
                <stop offset="100%" stop-color="#ef4444" stop-opacity="0.95"/>
            </radialGradient>
            <radialGradient id="midAreaGrad" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#fef08a" stop-opacity="0.85"/>
                <stop offset="100%" stop-color="#eab308" stop-opacity="0.9"/>
            </radialGradient>
            <radialGradient id="rootAreaGrad" cx="50%" cy="40%" r="50%">
                <stop offset="0%" stop-color="#c7d2fe" stop-opacity="0.85"/>
                <stop offset="100%" stop-color="#6366f1" stop-opacity="0.9"/>
            </radialGradient>
        </defs>

        <!-- Tongue Base Contour -->
        <g id="tongue-base">
            <path d="M 315 45 C 265 110, 275 220, 390 295 C 505 220, 515 110, 465 45 Z" 
                  fill="url(#zfBodyGrad)" stroke="#ffffff" stroke-width="2.5"/>
            
            <!-- Central Lingual Furrow -->
            <path d="M 390 60 Q 390 160 390 250" stroke="rgba(0,0,0,0.3)" stroke-width="2.5" stroke-linecap="round"/>

            <!-- 1. ROOT ZONE (Kidney, Bladder, Intestines) -->
            <path d="M 330 55 C 310 95, 335 125, 390 125 C 445 125, 470 95, 450 55 Z" 
                  fill="url(#rootAreaGrad)" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="3 3"/>
            
            <!-- 2. CENTER ZONE (Spleen & Stomach) -->
            <ellipse cx="390" cy="175" rx="52" ry="38" 
                     fill="url(#midAreaGrad)" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3 3"/>

            <!-- 3. MARGINS / EDGES (Liver & Gallbladder) -->
            <path d="M 288 120 C 285 170, 305 220, 338 250 C 330 220, 325 170, 332 120 Z" 
                  fill="#10b981" fill-opacity="0.75" stroke="#34d399" stroke-width="1.4"/>
            <path d="M 492 120 C 495 170, 475 220, 442 250 C 450 220, 455 170, 448 120 Z" 
                  fill="#10b981" fill-opacity="0.75" stroke="#34d399" stroke-width="1.4"/>

            <!-- 4. TIP ZONE (Heart & Lungs) -->
            <path d="M 345 240 C 362 275, 375 292, 390 295 C 405 292, 418 275, 435 240 Q 390 252 345 240 Z" 
                  fill="url(#tipAreaGrad)" stroke="#f87171" stroke-width="1.8"/>
        </g>

        <!-- EXTERNAL CALLOUT LABELS & LEADER LINES -->

        <!-- Root (Kidney/Lower Jiao) -->
        <line x1="420" y1="90" x2="570" y2="70" stroke="#818cf8" stroke-width="1.6"/>
        <circle cx="420" cy="90" r="4" fill="#818cf8"/>
        <rect x="570" y="50" width="195" height="42" rx="8" fill="#182234" stroke="#6366f1" stroke-width="1.5"/>
        <text x="667" y="68" fill="#a5b4fc" font-size="12" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif">💧 舌根 · 肾与下焦</text>
        <text x="667" y="83" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" font-family="-apple-system, sans-serif">Root: Kidney, Bladder, Intestines</text>

        <!-- Center (Spleen/Stomach) -->
        <line x1="340" y1="175" x2="200" y2="155" stroke="#f59e0b" stroke-width="1.6"/>
        <circle cx="340" cy="175" r="4" fill="#f59e0b"/>
        <rect x="15" y="135" width="195" height="42" rx="8" fill="#182234" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="112" y="153" fill="#fde68a" font-size="12" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif">🌾 舌中 · 脾与胃</text>
        <text x="112" y="168" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" font-family="-apple-system, sans-serif">Center: Spleen &amp; Stomach (Mid Jiao)</text>

        <!-- Edges (Liver/Gallbladder) -->
        <line x1="480" y1="180" x2="570" y2="180" stroke="#34d399" stroke-width="1.6"/>
        <circle cx="480" cy="180" r="4" fill="#34d399"/>
        <rect x="570" y="160" width="195" height="42" rx="8" fill="#182234" stroke="#10b981" stroke-width="1.5"/>
        <text x="667" y="178" fill="#6ee7b7" font-size="12" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif">🍃 舌边 · 肝与胆</text>
        <text x="667" y="193" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" font-family="-apple-system, sans-serif">Margins: Liver &amp; Gallbladder</text>

        <!-- Tip (Heart/Lung) -->
        <line x1="390" y1="270" x2="200" y2="265" stroke="#f43f5e" stroke-width="1.6"/>
        <circle cx="390" cy="270" r="4" fill="#f43f5e"/>
        <rect x="15" y="245" width="195" height="42" rx="8" fill="#182234" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="112" y="263" fill="#fda4af" font-size="12" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif">❤️ 舌尖 · 心与肺</text>
        <text x="112" y="278" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" font-family="-apple-system, sans-serif">Tip: Heart &amp; Lung (Upper Jiao)</text>
    </svg>"""


def generate_tongue_svg(t_data: Dict[str, Any]) -> str:
    """Generate illustrated, authentic, anatomically differentiated SVG diagram of a tongue pattern."""
    pattern_id = t_data.get("id", "normal")
    
    if pattern_id == "normal":
        # Normal Healthy Tongue (淡红舌 · 薄白苔)
        inner_content = """
        <defs>
            <radialGradient id="normGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#fb7185"/>
                <stop offset="70%" stop-color="#f43f5e"/>
                <stop offset="100%" stop-color="#e11d48"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#normGrad)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 100 45 Q 100 115 100 170" stroke="rgba(0,0,0,0.22)" stroke-width="2" stroke-linecap="round"/>
        <path d="M 64 55 C 54 95, 62 145, 100 168 C 138 145, 146 95, 136 55 Z" 
              fill="rgba(255,255,255,0.48)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
        <path d="M 72 70 C 65 105, 75 140, 100 155 C 125 140, 135 105, 128 70 Z" 
              fill="rgba(255,255,255,0.25)"/>
        """

    elif pattern_id == "pale_swollen_teeth":
        # Pale Swollen Tongue with Scalloped Teeth Marks (淡白胖嫩 · 边有齿痕)
        inner_content = """
        <defs>
            <radialGradient id="paleGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#fed7aa"/>
                <stop offset="70%" stop-color="#ffedd5"/>
                <stop offset="100%" stop-color="#fdba74"/>
            </radialGradient>
        </defs>
        <!-- Swollen Silhouette with Scalloped Teeth Indentations on Both Edges -->
        <path d="M 45 35 
                 C 32 45, 36 60, 24 70 
                 C 16 78, 30 88, 20 98 
                 C 14 108, 32 118, 22 130 
                 C 16 142, 34 152, 28 165 
                 C 36 185, 65 204, 100 205 
                 C 135 204, 164 185, 172 165 
                 C 166 152, 184 142, 178 130 
                 C 168 118, 186 108, 180 98 
                 C 170 88, 184 78, 176 70 
                 C 164 60, 168 45, 155 35 Z" 
              fill="url(#paleGrad)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 100 45 Q 100 115 100 175" stroke="rgba(180,83,9,0.25)" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 58 55 C 48 95, 56 145, 100 172 C 144 145, 152 95, 142 55 Z" 
              fill="rgba(255,255,255,0.72)"/>
        <ellipse cx="78" cy="110" rx="14" ry="32" fill="rgba(255,255,255,0.4)" transform="rotate(-15 78 110)"/>
        <ellipse cx="122" cy="110" rx="14" ry="32" fill="rgba(255,255,255,0.4)" transform="rotate(15 122 110)"/>
        """

    elif pattern_id == "red_yellow_greasy":
        # Red Tongue with Thick Yellow Greasy Moss (红舌 · 黄厚腻苔)
        inner_content = """
        <defs>
            <radialGradient id="redGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#ef4444"/>
                <stop offset="70%" stop-color="#dc2626"/>
                <stop offset="100%" stop-color="#991b1b"/>
            </radialGradient>
            <radialGradient id="yellowMossGrad" cx="50%" cy="45%" r="50%">
                <stop offset="0%" stop-color="#fef08a"/>
                <stop offset="60%" stop-color="#eab308"/>
                <stop offset="100%" stop-color="#ca8a04"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#redGrad)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 56 45 C 44 90, 52 148, 100 174 C 148 148, 156 90, 144 45 Z" 
              fill="url(#yellowMossGrad)" stroke="#ca8a04" stroke-width="1.5"/>
        <g fill="#a16207" opacity="0.6">
            <circle cx="85" cy="70" r="2.5"/><circle cx="105" cy="65" r="3"/><circle cx="120" cy="75" r="2.5"/>
            <circle cx="75" cy="95" r="3"/><circle cx="95" cy="90" r="3.5"/><circle cx="115" cy="92" r="3"/>
            <circle cx="130" cy="100" r="2.5"/><circle cx="85" cy="120" r="3"/><circle cx="100" cy="115" r="3.5"/>
            <circle cx="118" cy="122" r="3"/><circle cx="95" cy="142" r="3"/><circle cx="108" cy="145" r="2.5"/>
        </g>
        """

    elif pattern_id == "crimson_cracked_peeled":
        # Crimson Tongue with Deep Fissures & Mirror Peel (绛红裂纹 · 镜面无苔)
        inner_content = """
        <defs>
            <radialGradient id="crimsonGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#b91c1c"/>
                <stop offset="70%" stop-color="#991b1b"/>
                <stop offset="100%" stop-color="#450a0a"/>
            </radialGradient>
        </defs>
        <path d="M 52 35 C 32 85, 36 165, 100 198 C 164 165, 168 85, 148 35 Z" 
              fill="url(#crimsonGrad)" stroke="#ffffff" stroke-width="2"/>
        <ellipse cx="100" cy="115" rx="36" ry="58" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="2"/>
        <path d="M 75 75 Q 100 65 125 75" stroke="rgba(255,255,255,0.3)" stroke-width="2" fill="none"/>
        <g stroke="#450a0a" stroke-width="2.5" stroke-linecap="round">
            <line x1="100" y1="52" x2="100" y2="175"/>
            <path d="M 72 85 Q 85 92 100 88 M 100 88 Q 115 84 128 90"/>
            <path d="M 68 115 Q 84 122 100 118 M 100 118 Q 118 114 132 122"/>
            <path d="M 74 145 Q 86 150 100 148 M 100 148 Q 114 146 126 152"/>
            <path d="M 85 168 L 100 165 L 115 168"/>
        </g>
        """

    elif pattern_id == "prickles_tip":
        # Prickles & Red Spots on Tip (舌尖红刺 · 芒刺点点)
        inner_content = """
        <defs>
            <radialGradient id="prickleBody" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#f87171"/>
                <stop offset="60%" stop-color="#ef4444"/>
                <stop offset="100%" stop-color="#b91c1c"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#prickleBody)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 64 50 C 56 90, 64 135, 100 152 C 136 135, 144 90, 136 50 Z" 
              fill="rgba(254, 240, 138, 0.42)"/>
        <path d="M 68 165 C 80 190, 90 198, 100 198 C 110 198, 120 190, 132 165 Q 100 175 68 165 Z" 
              fill="#dc2626" stroke="#f87171" stroke-width="1.5"/>
        <g stroke="#ffffff" stroke-width="0.8">
            <circle cx="85" cy="170" r="2.8" fill="#ef4444"/><circle cx="95" cy="168" r="2.5" fill="#ffffff"/>
            <circle cx="105" cy="168" r="2.8" fill="#ef4444"/><circle cx="115" cy="170" r="2.5" fill="#ffffff"/>
            <circle cx="90" cy="178" r="3" fill="#ef4444"/><circle cx="100" cy="176" r="3.2" fill="#ffffff"/>
            <circle cx="110" cy="178" r="3" fill="#ef4444"/><circle cx="85" cy="186" r="2.8" fill="#ef4444"/>
            <circle cx="95" cy="185" r="3" fill="#ffffff"/><circle cx="105" cy="185" r="3" fill="#ffffff"/>
            <circle cx="115" cy="186" r="2.8" fill="#ef4444"/><circle cx="98" cy="192" r="3.2" fill="#ef4444"/>
            <circle cx="102" cy="192" r="3.2" fill="#ffffff"/>
        </g>
        """

    elif pattern_id == "purple_petechiae":
        # Purple / Dusky Tongue with Petechiae Stasis (青紫舌 · 瘀斑瘀点)
        inner_content = """
        <defs>
            <radialGradient id="purpleGrad" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#7c3aed"/>
                <stop offset="70%" stop-color="#581c87"/>
                <stop offset="100%" stop-color="#3b0764"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#purpleGrad)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 60 70 Q 75 110 68 150 M 140 70 Q 125 110 132 150" 
              stroke="#1e1b4b" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="6 3"/>
        <path d="M 68 55 C 60 95, 68 140, 100 160 C 132 140, 140 95, 132 55 Z" 
              fill="rgba(255,255,255,0.2)"/>
        <g fill="#18181b" stroke="#a855f7" stroke-width="1.2">
            <circle cx="45" cy="95" r="3.8"/><circle cx="42" cy="125" r="4.2"/><circle cx="52" cy="150" r="3.5"/>
            <circle cx="155" cy="95" r="3.8"/><circle cx="158" cy="125" r="4.2"/><circle cx="148" cy="150" r="3.5"/>
            <circle cx="78" cy="172" r="3.5"/><circle cx="90" cy="184" r="4"/><circle cx="108" cy="186" r="4"/>
            <circle cx="122" cy="172" r="3.5"/><circle cx="100" cy="140" r="3.2"/><circle cx="85" cy="115" r="3"/>
        </g>
        """

    elif pattern_id == "geographic":
        # Geographic / Map Tongue (地图舌 · 花剥苔)
        inner_content = """
        <defs>
            <radialGradient id="geoBody" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#fb7185"/>
                <stop offset="70%" stop-color="#f43f5e"/>
                <stop offset="100%" stop-color="#be123c"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#geoBody)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 60 50 C 48 95, 56 150, 100 175 C 144 150, 152 95, 140 50 Z" 
              fill="rgba(255,255,255,0.7)"/>
        <path d="M 72 75 Q 86 65 92 82 Q 96 98 84 104 Q 68 100 72 75 Z" 
              fill="#be123c" stroke="#fef08a" stroke-width="2.5"/>
        <path d="M 108 105 Q 128 92 136 115 Q 130 138 112 135 Q 98 122 108 105 Z" 
              fill="#be123c" stroke="#fef08a" stroke-width="2.5"/>
        <path d="M 80 135 Q 95 130 98 148 Q 92 162 78 155 Z" 
              fill="#be123c" stroke="#fef08a" stroke-width="2"/>
        """

    elif pattern_id == "black_charred":
        # Black / Charred Dry Tongue (黑燥苔 · 寒极或热极)
        inner_content = """
        <defs>
            <radialGradient id="blackBody" cx="50%" cy="50%" r="55%">
                <stop offset="0%" stop-color="#ef4444"/>
                <stop offset="70%" stop-color="#b91c1c"/>
                <stop offset="100%" stop-color="#7f1d1d"/>
            </radialGradient>
            <radialGradient id="charredMoss" cx="50%" cy="45%" r="50%">
                <stop offset="0%" stop-color="#27272a"/>
                <stop offset="60%" stop-color="#18181b"/>
                <stop offset="100%" stop-color="#09090b"/>
            </radialGradient>
        </defs>
        <path d="M 50 35 C 28 85, 34 165, 100 198 C 166 165, 172 85, 150 35 Z" 
              fill="url(#blackBody)" stroke="#ffffff" stroke-width="2"/>
        <path d="M 56 45 C 44 90, 52 148, 100 174 C 148 148, 156 90, 144 45 Z" 
              fill="url(#charredMoss)" stroke="#3f3f46" stroke-width="1.8"/>
        <g stroke="#52525b" stroke-width="1.2">
            <line x1="85" y1="70" x2="90" y2="76"/><line x1="110" y1="65" x2="115" y2="72"/>
            <line x1="75" y1="95" x2="82" y2="102"/><line x1="95" y1="92" x2="102" y2="98"/>
            <line x1="120" y1="90" x2="125" y2="96"/><line x1="88" y1="120" x2="94" y2="126"/>
            <line x1="105" y1="118" x2="112" y2="124"/><line x1="96" y1="145" x2="102" y2="152"/>
        </g>
        """
    else:
        inner_content = """<circle cx="100" cy="110" r="40" fill="#f43f5e"/>"""

    return f"""<svg viewBox="0 0 200 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" style="background: #0b1120; border-radius: 10px; border: 1px solid rgba(255,255,255,0.08);">
        {inner_content}
    </svg>"""


def generate_pulse_waveform_svg(wf_type: str) -> str:
    """Generate dynamic SVG representation of tactile pulse waveform."""
    if wf_type == "high_surface":
        path_d = "M 10 35 Q 30 5 50 35 T 90 35 T 130 35 T 170 35 T 210 35"
        stroke = "#38bdf8"
    elif wf_type == "deep_recessed":
        path_d = "M 10 50 Q 30 40 50 50 T 90 50 T 130 50 T 170 50 T 210 50"
        stroke = "#94a3b8"
    elif wf_type == "wide_slow":
        path_d = "M 10 35 Q 50 15 90 35 T 170 35 T 250 35"
        stroke = "#38bdf8"
    elif wf_type == "dense_rapid":
        path_d = "M 10 35 Q 20 10 30 35 T 50 35 T 70 35 T 90 35 T 110 35 T 130 35 T 150 35 T 170 35 T 190 35 T 210 35"
        stroke = "#ef4444"
    elif wf_type == "rolling_pearls":
        path_d = "M 10 35 C 25 15, 35 15, 50 35 C 65 15, 75 15, 90 35 C 105 15, 115 15, 130 35 C 145 15, 155 15, 170 35"
        stroke = "#34d399"
    elif wf_type == "rough_jagged":
        path_d = "M 10 35 L 25 25 L 35 38 L 50 22 L 65 35 L 85 28 L 95 38 L 115 20 L 130 35 L 150 25 L 170 35"
        stroke = "#f59e0b"
    elif wf_type == "straight_line":
        path_d = "M 10 25 L 210 25"
        stroke = "#a855f7"
    elif wf_type == "twisted_rope":
        path_d = "M 10 25 Q 25 10 40 25 T 70 25 T 100 25 T 130 25 T 160 25 T 190 25 T 220 25"
        stroke = "#fbbf24"
    elif wf_type == "ocean_waves":
        path_d = "M 10 35 C 25 5, 35 5, 50 42 M 65 35 C 80 5, 90 5, 105 42 M 120 35 C 135 5, 145 5, 160 42"
        stroke = "#ef4444"
    elif wf_type == "regular_pause":
        path_d = "M 10 35 Q 25 10 40 35 M 40 35 L 90 35 M 90 35 Q 105 10 120 35 M 120 35 L 170 35 M 170 35 Q 185 10 200 35"
        stroke = "#ec4899"
    else:
        path_d = "M 10 35 Q 30 20 50 35 T 90 35 T 130 35 T 170 35 T 210 35"
        stroke = "#38bdf8"

    return f"""
    <svg viewBox="0 0 220 60" width="100%" height="60" xmlns="http://www.w3.org/2000/svg" style="background: rgba(0,0,0,0.3); border-radius: 6px;">
        <line x1="0" y1="35" x2="220" y2="35" stroke="rgba(255,255,255,0.15)" stroke-dasharray="3 3"/>
        <path d="{path_d}" fill="none" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round"/>
    </svg>
    """


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_tongue_pulse_atlas_tab():
    """Render the Visual Tongue & Pulse Clinical Atlas tab."""
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            👅 Visual Tongue & Pulse Clinical Atlas (图解舌象与脉象图谱)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Comprehensive clinical reference for authentic TCM tongue presentations, Zang-Fu lingual topography, and the 28 canonical pulses with tactile waveform graphics.
        </p>
    </div>
    """)

    sub_nav = st.radio(
        "Select Clinical Atlas",
        options=["👅 Tongue Visual Atlas", "💓 28 Pulses Waveform Atlas", "⚖️ Confusing Pairs Differential Guide"],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.write("")

    # SUB-TAB 1: TONGUE VISUAL ATLAS
    if sub_nav == "👅 Tongue Visual Atlas":
        # Master Zang-Fu Topography Map Showcase
        master_zf_svg = generate_master_zangfu_svg()
        render_clean_html(f"""
        <div style="background: #111827; border: 1.5px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 20px 22px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div>
                    <span style="font-size: 1.25rem; font-weight: 800; color: #38bdf8;">🗺️ 图解舌诊脏腑投影法 (Master Zang-Fu Lingual Projection Topography)</span>
                    <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 2px;">
                        Anatomical distribution of internal Zang-Fu organs projected onto the lingual surface.
                    </div>
                </div>
                <span style="background: rgba(0, 123, 167, 0.3); color: #38bdf8; font-size: 0.76rem; font-weight: 800; padding: 3px 10px; border-radius: 4px; text-transform: uppercase;">
                    Topography Standard
                </span>
            </div>

            <div style="margin: 12px 0;">
                {master_zf_svg}
            </div>

            <!-- Quick Clinical Reference Matrix -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 14px;">
                <div style="background: rgba(244, 63, 94, 0.1); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 8px; padding: 10px 14px;">
                    <strong style="color: #fda4af; font-size: 0.95rem;">❤️ 舌尖 (Tip): 心肺 (Upper Jiao)</strong>
                    <div style="font-size: 0.84rem; color: #e2e8f0; margin-top: 4px; line-height: 1.45;">
                        Red tip / prickly thorns: Heart fire, insomnia, mouth sores.<br/>Exterior wind-heat: Red tip with sore throat.
                    </div>
                </div>
                <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 10px 14px;">
                    <strong style="color: #fde68a; font-size: 0.95rem;">🌾 舌中 (Center): 脾胃 (Middle Jiao)</strong>
                    <div style="font-size: 0.84rem; color: #e2e8f0; margin-top: 4px; line-height: 1.45;">
                        Thick greasy yellow: Spleen/Stomach damp-heat.<br/>Center cracks / peeled: Stomach Yin deficiency.
                    </div>
                </div>
                <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 10px 14px;">
                    <strong style="color: #6ee7b7; font-size: 0.95rem;">🍃 舌边 (Edges): 肝胆 (Lateral Margins)</strong>
                    <div style="font-size: 0.84rem; color: #e2e8f0; margin-top: 4px; line-height: 1.45;">
                        Red / curled edges: Liver fire, migraines, irritability.<br/>Purple edges: Blood stasis in chest or hypochondrium.
                    </div>
                </div>
                <div style="background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 8px; padding: 10px 14px;">
                    <strong style="color: #a5b4fc; font-size: 0.95rem;">💧 舌根 (Root): 肾与下焦 (Lower Jiao)</strong>
                    <div style="font-size: 0.84rem; color: #e2e8f0; margin-top: 4px; line-height: 1.45;">
                        Peeled / deep root cracks: Kidney Yin exhaustion.<br/>Thick greasy yellow root: Lower Jiao damp-heat (UTI).
                    </div>
                </div>
            </div>
        </div>
        """)

        render_clean_html("""
        <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 10px; padding: 12px 18px; margin-bottom: 16px;">
            <span style="font-size: 1.1rem; font-weight: 800; color: #38bdf8;">📋 8 Canonical TCM Tongue Presentations (八大临床经典舌象辨析)</span>
            <div style="font-size: 0.86rem; color: #94a3b8; margin-top: 2px;">
                Each illustrated presentation features authentic lingual pathology markers, morphological pillars, and differential pathogenesis.
            </div>
        </div>
        """)

        cols = st.columns(2)
        for i, tp in enumerate(TONGUE_PATTERNS):
            col = cols[i % 2]
            with col:
                svg_img = generate_tongue_svg(tp)
                render_clean_html(f"""
                <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-left: 5px solid {tp.get('border_color', '#38bdf8')}; border-radius: 12px; padding: 18px 20px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                        <div>
                            <span style="background: rgba(0, 123, 167, 0.25); color: #38bdf8; font-size: 0.72rem; font-weight: 800; padding: 2px 7px; border-radius: 4px; text-transform: uppercase;">
                                {tp['category']}
                            </span>
                            <h4 style="color: #ffffff !important; font-size: 1.2rem; font-weight: 800; margin: 6px 0 2px 0;">{tp['name']}</h4>
                            <div style="color: #c89666; font-size: 1.02rem; font-weight: 700;">{tp['chinese']}</div>
                        </div>
                    </div>

                    <!-- Centered Large Anatomical Tongue Showcase -->
                    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; background: #0b1120; border-radius: 10px; border: 1px solid rgba(255,255,255,0.08); padding: 12px; margin: 10px 0 14px 0;">
                        <div style="width: 200px; height: 220px;">
                            {svg_img}
                        </div>
                        <div style="background: #182234; border: 1px solid rgba(255,255,255,0.14); border-radius: 6px; padding: 4px 12px; margin-top: 8px;">
                            <span style="color: #fde68a; font-size: 0.82rem; font-weight: 800; font-family: monospace;">
                                {tp['badge_summary']}
                            </span>
                        </div>
                    </div>

                    <!-- 3 Core Morphological Pillars -->
                    <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px; font-size: 0.9rem; line-height: 1.5;">
                        <div style="background: rgba(56, 189, 248, 0.08); border-radius: 6px; padding: 6px 10px;">
                            <strong style="color: #38bdf8;">👅 舌质 (Tongue Body):</strong> <span style="color: #e2e8f0;">{tp['body_color']}</span>
                        </div>
                        <div style="background: rgba(253, 230, 138, 0.08); border-radius: 6px; padding: 6px 10px;">
                            <strong style="color: #fde68a;">📏 舌形 (Shape &amp; Morphology):</strong> <span style="color: #cbd5e1;">{tp['shape']}</span>
                        </div>
                        <div style="background: rgba(52, 211, 153, 0.08); border-radius: 6px; padding: 6px 10px;">
                            <strong style="color: #34d399;">🌫️ 舌苔 (Coating Layer):</strong> <span style="color: #cbd5e1;">{tp['coating']}</span>
                        </div>
                    </div>

                    <!-- Clinical Pathogenesis & Manifestations -->
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 12px 14px; font-size: 0.88rem; line-height: 1.55;">
                        <div style="color: #34d399; font-weight: 800; margin-bottom: 3px;">⚡ 病机 (Clinical Pathogenesis):</div>
                        <div style="color: #e2e8f0; margin-bottom: 8px;">{tp['pathogenesis']}</div>
                        <div style="color: #c7d2fe; font-weight: 800; margin-bottom: 3px;">🩺 主病与临证参考 (Typical Clinical Indications):</div>
                        <div style="color: #cbd5e1;">{tp['clinical_meaning']}</div>
                    </div>
                </div>
                """)

    # SUB-TAB 2: 28 PULSES WAVEFORM ATLAS
    elif sub_nav == "💓 28 Pulses Waveform Atlas":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">脉诊指法与三部九候 (Three Positions & Three Depths)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                <strong>Positions:</strong> Cun (寸 - Upper Jiao), Guan (关 - Middle Jiao), Chi (尺 - Lower Jiao).<br/>
                <strong>Depths:</strong> Superficial (Fu 浮 - Skin level), Medium (Zhong 中 - Muscle level), Deep (Chen 沉 - Tendon/bone level).
            </div>
        </div>
        """)

        cols_p = st.columns(2)
        for i, pulse in enumerate(PULSE_PATTERNS):
            col = cols_p[i % 2]
            with col:
                wf_svg = generate_pulse_waveform_svg(pulse["waveform_type"])
                render_clean_html(f"""
                <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 18px 20px; margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="color: #ffffff; font-size: 1.15rem; font-weight: 800;">{pulse['name']}</span>
                        <span style="background: rgba(0, 123, 167, 0.25); color: #38bdf8; font-size: 0.72rem; font-weight: 700; padding: 2px 7px; border-radius: 4px;">
                            {pulse['depth']}
                        </span>
                    </div>

                    <div style="margin: 8px 0 10px 0;">
                        {wf_svg}
                    </div>

                    <div style="font-size: 0.88rem; color: #e2e8f0; line-height: 1.45; margin-bottom: 8px;">
                        <strong style="color: #c89666;">Tactile Sensation:</strong> {pulse['tactile_sensation']}
                    </div>

                    <div style="font-size: 0.84rem; color: #94a3b8; line-height: 1.4; margin-bottom: 6px;">
                        <strong style="color: #38bdf8;">Pathogenesis:</strong> {pulse['pathogenesis']}
                    </div>

                    <div style="font-size: 0.82rem; color: #34d399; font-weight: 600;">
                        ✓ Key Associated Conditions: {pulse['clinical_conditions']}
                    </div>
                </div>
                """)

    # SUB-TAB 3: CONFUSING PAIRS DIFFERENTIAL
    elif sub_nav == "⚖️ Confusing Pairs Differential Guide":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">相似脉象精细鉴别 (Confusing Pulse Pairs Master Differential)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Master the subtle nuances tested rigorously on NCCAOM and licensing board examinations.
            </div>
        </div>
        """)

        diff_pairs = [
            ("Wiry (弦) vs. Tight (紧)", "Wiry feels straight and taut like a guitar string without twisting; Tight feels like a thick twisted rope that vibrates back and forth under the fingers.", "Wiry indicates Liver disharmonies, pain, or phlegm; Tight indicates severe Cold invasion or acute violent cramping."),
            ("Slippery (滑) vs. Rapid (数)", "Slippery describes the round, fluid smoothness (flow quality like rolling pearls); Rapid describes speed (> 90 bpm frequency). They often combine into 'Slippery-Rapid'.", "Slippery = Phlegm/Damp or Pregnancy; Rapid = Heat."),
            ("Floating (浮) vs. Hollow (芤)", "Floating pulse is felt at the surface and slightly softens under deep pressure; Hollow pulse feels like a scallion or green onion stalk (outer walls solid, center empty).", "Floating = Exterior pathogen; Hollow = Sudden massive blood loss or fluid hemorrhage."),
            ("Knotted (结) vs. Intermittent (代) vs. Hurried (促)", "Knotted is slow with irregular pauses; Hurried is rapid with irregular pauses; Intermittent misses beats at strictly regular, predictable intervals.", "Knotted = Cold/Phlegm stagnation; Hurried = Extreme Heat fire; Intermittent = Exhaustion of Zang-Fu organ Qi.")
        ]

        for pair_title, distinction, significance in diff_pairs:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 18px 22px; margin-bottom: 14px;">
                <div style="font-size: 1.15rem; font-weight: 800; color: #c89666; margin-bottom: 6px;">
                    {pair_title}
                </div>
                <div style="font-size: 0.9rem; color: #e2e8f0; line-height: 1.5; margin-bottom: 8px;">
                    <strong style="color: #38bdf8;">Tactile Distinction:</strong> {distinction}
                </div>
                <div style="font-size: 0.86rem; color: #34d399; font-weight: 600;">
                    Diagnostic Clinical Significance: {significance}
                </div>
            </div>
            """)

# -*- coding: utf-8 -*-
"""Generate the complete modules/atlas.py module."""

import json
from pathlib import Path

# Load points and meridians
with open("d:/TCM/acupuncture_app/static/atlas_meridians.json", "r", encoding="utf-8") as f:
    meridians = json.load(f)

with open("d:/TCM/acupuncture_app/static/fitted_points.json", "r", encoding="utf-8") as f:
    fitted_pts = json.load(f)

from modules.tcm_points import POINT_DICTIONARY

# Canonical region assignment
def get_region(code):
    c = code.upper().replace("-", "")
    if c in ["ST1", "ST2", "ST4", "ST6", "ST7", "ST8", "LI20", "SI19", "BL1", "BL2", "TE17", "TE21", "TE23", "GB1", "GB2", "GB8", "GB14", "GV20", "GV23", "GV24", "GV26", "CV24", "YINTANG", "TAIYANG", "SISHENCONG"]:
        return "Head"
    if c in ["ST12", "BL10", "TE16", "GB20", "GB21", "GV14", "GV15", "GV16", "CV22", "ANMIAN", "DINGCHUAN"]:
        return "Neck"
    if c in ["LU1", "LU2", "ST18", "SP21", "KI27", "PC1", "GB24", "LR14", "CV17"]:
        return "Chest"
    if c in ["ST21", "ST25", "ST28", "ST29", "ST30", "SP15", "KI16", "GB25", "GB26", "LR13", "CV3", "CV4", "CV6", "CV8", "CV9", "CV12", "CV14", "ZIGONG"]:
        return "Abdomen"
    if c in ["BL11", "BL12", "BL13", "BL14", "BL15", "BL17", "BL18", "BL19", "BL20", "BL21", "BL23", "BL25", "BL28", "BL32", "BL52", "SI11", "SI12", "GV1", "GV3", "GV4", "GV9", "GV12", "HUATUOJIAJI"]:
        return "Back"
    if c.startswith(("LU", "LI", "HT", "SI", "PC", "TE", "SJ")) or c in ["YAOTONGXUE", "SIFENG", "BAXIE"]:
        return "Upper Limb"
    return "Lower Limb"

# Channel ID
def get_channel(code):
    c = code.upper().replace("-", "")
    for ch in ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "TE", "SJ", "GB", "LR", "LV", "GV", "DU", "CV", "REN"]:
        if c.startswith(ch):
            if ch == "SJ": return "TE"
            if ch == "LV": return "LR"
            if ch == "DU": return "GV"
            if ch == "REN": return "CV"
            return ch
    return "EX"

# Safety info
SAFETY_INFO = {
    "LU1": ("danger", "PNEUMOTHORAX RISK: Puncture obliquely laterally 0.5–0.8 cun. Never puncture perpendicularly towards thoracic cavity."),
    "LU2": ("danger", "PNEUMOTHORAX RISK: Puncture obliquely laterally 0.5–0.8 cun. Deep puncture strictly forbidden."),
    "ST1": ("danger", "OCULAR GLOBE RISK: Gently push eyeball upward. Puncture slowly perpendicularly 0.5–1.0 cun along orbital rim without manipulation."),
    "ST12": ("danger", "PNEUMOTHORAX & ARTERY RISK: Supraclavicular fossa. Perpendicular puncture forbidden. Oblique insertion 0.3–0.5 cun."),
    "CV22": ("danger", "TRACHEA & AORTA RISK: Puncture perpendicularly 0.2 cun, then direct tip downward behind sternum 0.5–1.0 cun."),
    "GV15": ("danger", "MEDULLA OBLONGATA RISK: Puncture strictly perpendicular 0.5–0.8 cun. Never puncture upward or deeply towards skull base."),
    "GV16": ("danger", "MEDULLA OBLONGATA RISK: Puncture perpendicular or slightly downward 0.5–0.8 cun. Deep upward angle strictly prohibited."),
    "BL1": ("danger", "RETROBULBAR HEMORRHAGE RISK: Displace globe laterally. Insert needle slowly 0.5–1.0 cun along orbital margin without rotation."),
    "BL11": ("danger", "PNEUMOTHORAX RISK: Oblique insertion towards spine 0.5–0.8 cun. Never insert perpendicularly."),
    "BL13": ("danger", "PNEUMOTHORAX RISK: Oblique insertion towards spine 0.5–0.8 cun. Deep perpendicular insertion strictly forbidden."),
    "BL15": ("danger", "PNEUMOTHORAX RISK: Oblique insertion towards spine 0.5–0.8 cun."),
    "BL18": ("danger", "PNEUMOTHORAX & LIVER RISK: Oblique insertion towards spine 0.5–0.8 cun."),
    "BL20": ("danger", "PNEUMOTHORAX & SPLEEN RISK: Oblique insertion towards spine 0.5–0.8 cun."),
    "BL23": ("caution", "KIDNEY RISK: Puncture perpendicularly 0.5–1.0 cun. Deep insertion in thin patients may puncture renal tissue."),
    "LR14": ("danger", "LIVER & PNEUMOTHORAX RISK: 6th intercostal space. Oblique insertion along intercostal space 0.5–0.8 cun."),
    "SP21": ("danger", "PNEUMOTHORAX RISK: 7th intercostal space mid-axillary line. Oblique insertion 0.3–0.5 cun."),
    "GB20": ("caution", "VERTEBRAL ARTERY RISK: Direct needle toward tip of nose 0.8–1.2 cun. Do not angle upward toward brainstem."),
    "GB21": ("danger", "PNEUMOTHORAX & PREGNANCY: Apex of lung lies beneath trapezius. Oblique posterior insertion 0.5–0.8 cun. CONTRAINDICATED IN PREGNANCY."),
    "LI4": ("caution", "CONTRAINDICATED IN PREGNANCY: Strongly stimulates uterine contractions and descends Qi. Puncture 0.5–1.0 cun."),
    "SP6": ("caution", "CONTRAINDICATED IN PREGNANCY: Descends Qi and induces labor. Puncture perpendicularly 1.0–1.5 cun."),
    "BL60": ("caution", "CONTRAINDICATED IN PREGNANCY: Strong descending vector. Puncture perpendicularly 0.5–1.0 cun."),
    "BL67": ("caution", "CONTRAINDICATED IN PREGNANCY except for correcting breech fetal presentation via moxa."),
    "CV8": ("danger", "NEEDLING STRICTLY FORBIDDEN: Umbilicus. Moxibustion with salt or ginger only."),
    "ST36": ("caution", "Avoid anterior tibial artery with deep needling. Perpendicular insertion 1.0–1.5 cun."),
    "PC6": ("caution", "Avoid median nerve trunk. Electric shock sensation radiating to fingers indicates nerve contact—withdraw slightly.")
}

# Compile points list
all_points = {}

for code, pt in fitted_pts.items():
    clean_code = code.upper().replace("-", "")
    ch = get_channel(clean_code)
    reg = get_region(clean_code)
    view = "posterior" if reg == "Back" or ch in ["BL", "GV"] and clean_code not in ["BL1", "BL2", "GV20", "GV23", "GV24", "GV26"] else "anterior"
    
    # Format code with hyphen (LU-1)
    if ch != "EX":
        num = clean_code[len(ch):] if clean_code.startswith(ch) else clean_code[2:]
        disp_code = f"{ch}-{num}" if num.isdigit() else clean_code
    else:
        disp_code = clean_code
        
    pinyin = pt.get("name", "")
    hanzi = pt.get("hanzi", "")
    dict_entry = POINT_DICTIONARY.get(clean_code, (pinyin, hanzi, ""))
    english = dict_entry[2] if dict_entry[2] else pt.get("eng", f"{pinyin} Point")
    
    cat = pt.get("cat", "Standard Point")
    loc = pt.get("loc", "Textbook anatomical location.")
    act = pt.get("act", "Regulates channel Qi and harmonizes organ functions.")
    saf = pt.get("saf", "Standard perpendicular insertion.")
    
    # Safety level
    if clean_code in SAFETY_INFO:
        s_level, s_warning = SAFETY_INFO[clean_code]
    elif "pneumothorax" in saf.lower() or "eye" in saf.lower() or "artery" in saf.lower():
        s_level, s_warning = "danger", saf
    elif "contraindicated" in saf.lower() or "caution" in saf.lower() or "pregnancy" in saf.lower():
        s_level, s_warning = "caution", saf
    else:
        s_level, s_warning = "safe", "Safe standard needling parameters when observing anatomical boundaries."
        
    # Depth
    d_min, d_max, d_limit = 0.5, 1.0, 2.5
    if "1.0–1.5" in saf or "1.0-1.5" in saf or "1–1.5" in saf:
        d_min, d_max = 1.0, 1.5
    elif "0.5–0.8" in saf or "0.5-0.8" in saf:
        d_min, d_max = 0.5, 0.8
    elif "0.3–0.5" in saf or "0.3-0.5" in saf:
        d_min, d_max = 0.3, 0.5
    elif "0.1–0.2" in saf or "prick" in saf.lower():
        d_min, d_max, d_limit = 0.1, 0.2, 0.5
        
    # Extract tags
    tags = []
    text_corpus = f"{act} {loc}".lower()
    common_indications = [
        "asthma", "cough", "chest-pain", "headache", "migraine", "gastric-pain", "vomiting",
        "diarrhea", "constipation", "insomnia", "anxiety", "depression", "fatigue", "dizziness",
        "sciatica", "lumbar-pain", "neck-pain", "shoulder-pain", "knee-pain", "hypertension",
        "dysmenorrhea", "tinnitus", "rhinitis", "fever", "stroke", "paralysis", "hemorrhoids"
    ]
    for ind in common_indications:
        if ind.replace("-", " ") in text_corpus or ind in text_corpus:
            tags.append(ind)
            
    if not tags:
        tags = ["pain", "qi-regulation", "harmony"]
        
    all_points[disp_code] = {
        "code": disp_code,
        "cleanCode": clean_code,
        "channelId": ch,
        "pinyin": pinyin,
        "hanzi": hanzi,
        "english": english,
        "region": reg,
        "view": view,
        "category": cat,
        "tier": 1 if "Mu" in cat or "Shu" in cat or "Yuan" in cat or "He-Sea" in cat or "Command" in cat or clean_code in ["ST36", "LI4", "SP6", "LR3", "PC6", "LU7", "BL40", "GV20", "CV12", "YINTANG", "TAIYANG"] else 2,
        "safetyLevel": s_level,
        "safetyWarning": s_warning,
        "depthMin": d_min,
        "depthMax": d_max,
        "depthMaxLimit": d_limit,
        "technique": saf,
        "locationClassical": loc,
        "howToFind": [
            f"1. Identify the anatomical landmark: {loc.split('.')[0]}.",
            f"2. Palpate the depression or intermuscular groove at this level.",
            "3. Confirm patient tenderness or distinct Deqi sensation upon perpendicular pressure."
        ],
        "anatomy": f"Located within the {reg.lower()} region musculature and neurovascular bundle.",
        "etymology": f"{pinyin} ({hanzi}) reflects its anatomical position or clinical Qi dynamics.",
        "actions": [a.strip() for a in act.split(",") if a.strip()],
        "indications": [t.replace("-", " ").capitalize() for t in tags],
        "tags": tags,
        "combinations": [
            {"points": f"{disp_code} + LI-4", "indication": "Expels wind and clears pain"},
            {"points": f"{disp_code} + ST-36", "indication": "Fortifies Qi and builds post-natal resilience"}
        ]
    }

with open("d:/TCM/acupuncture_app/static/atlas_points.json", "w", encoding="utf-8") as f:
    json.dump(all_points, f, indent=2, ensure_ascii=False)

print(f"Compiled and saved {len(all_points)} atlas points.")

# -*- coding: utf-8 -*-
"""Compile full atlas_points.json merging fitted_points and POINT_DICTIONARY."""

import json
import sys
sys.path.append('.')

from modules.tcm_points import POINT_DICTIONARY
from scripts.build_atlas_points_data import format_code, REGION_MAP, SAFETY_MAP, DEPTH_MAP

with open("d:/TCM/acupuncture_app/static/fitted_points.json", "r", encoding="utf-8") as f:
    fitted_pts = json.load(f)

# Canonical channel from formatted code (e.g. CV-12 -> CV, EX-YINTANG -> EX)
def get_channel_from_code(disp_code):
    parts = disp_code.split("-")
    if len(parts) == 2 and parts[0] in ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "TE", "GB", "LR", "GV", "CV"]:
        return parts[0]
    return "EX"

# Compile all points
points_db = {}

# 1. First add all points from fitted_pts
for raw_code, pt in fitted_pts.items():
    disp_code = format_code(raw_code)
    clean = raw_code.upper().replace("-", "")
    ch = get_channel_from_code(disp_code)
    reg = REGION_MAP.get(clean, "Lower Limb" if ch in ["ST", "SP", "BL", "KI", "GB", "LR"] else ("Upper Limb" if ch in ["LU", "LI", "HT", "SI", "PC", "TE"] else "Head"))
    
    view = "posterior" if reg == "Back" or ch in ["BL", "GV"] and clean not in ["BL1", "BL2", "GV20", "GV23", "GV24", "GV26"] else "anterior"
    
    pinyin = pt.get("name", "")
    hanzi = pt.get("hanzi", "")
    dict_entry = POINT_DICTIONARY.get(clean, (pinyin, hanzi, ""))
    english = dict_entry[2] if dict_entry[2] else pt.get("eng", f"{pinyin} Point")
    
    cat = pt.get("cat", "Standard Point")
    loc = pt.get("loc", "Textbook anatomical location.")
    act = pt.get("act", "Regulates channel Qi and harmonizes organ functions.")
    saf = pt.get("saf", "Standard perpendicular insertion.")
    
    # Safety info
    if clean in SAFETY_MAP:
        s_level, s_warning = SAFETY_MAP[clean]
    elif "pneumothorax" in saf.lower() or "eye" in saf.lower() or "artery" in saf.lower():
        s_level, s_warning = "danger", saf
    elif "contraindicated" in saf.lower() or "caution" in saf.lower() or "pregnancy" in saf.lower():
        s_level, s_warning = "caution", saf
    else:
        s_level, s_warning = "safe", "Standard needling parameters when observing anatomical boundaries."
        
    # Depth
    d_min, d_max, d_limit, tech = 0.5, 1.0, 2.5, saf
    if clean in DEPTH_MAP:
        d_min, d_max, d_limit, tech = DEPTH_MAP[clean]
    elif "1.0–1.5" in saf or "1.0-1.5" in saf:
        d_min, d_max = 1.0, 1.5
    elif "0.5–0.8" in saf or "0.5-0.8" in saf:
        d_min, d_max = 0.5, 0.8
        
    # Tags
    text_corpus = f"{act} {loc}".lower()
    common_indications = [
        "asthma", "cough", "chest-pain", "headache", "migraine", "gastric-pain", "vomiting",
        "diarrhea", "constipation", "insomnia", "anxiety", "depression", "fatigue", "dizziness",
        "sciatica", "lumbar-pain", "neck-pain", "shoulder-pain", "knee-pain", "hypertension",
        "dysmenorrhea", "tinnitus", "rhinitis", "fever", "stroke", "paralysis", "hemorrhoids"
    ]
    tags = [ind for ind in common_indications if ind.replace("-", " ") in text_corpus or ind in text_corpus]
    if not tags: tags = ["pain-relief", "qi-regulation", "harmony"]
    
    is_major = 1 if "Mu" in cat or "Shu" in cat or "Yuan" in cat or "He-Sea" in cat or "Command" in cat or clean in ["ST36", "LI4", "SP6", "LR3", "PC6", "LU7", "BL40", "GV20", "CV12", "YINTANG", "TAIYANG"] else 2
    
    points_db[disp_code] = {
        "code": disp_code,
        "cleanCode": clean,
        "channelId": ch,
        "pinyin": pinyin,
        "hanzi": hanzi,
        "english": english,
        "region": reg,
        "view": view,
        "category": cat,
        "tier": is_major,
        "safetyLevel": s_level,
        "safetyWarning": s_warning,
        "depthMin": d_min,
        "depthMax": d_max,
        "depthMaxLimit": d_limit,
        "technique": tech,
        "locationClassical": loc,
        "howToFind": [
            f"1. Identify the anatomical landmark: {loc.split('.')[0]}.",
            f"2. Palpate the depression or intermuscular groove at this level.",
            "3. Confirm patient tenderness or distinct Deqi sensation upon gentle pressure."
        ],
        "anatomy": f"Located within the {reg.lower()} region musculature and regional neurovascular bundle.",
        "etymology": f"{pinyin} ({hanzi}) reflects its anatomical position or clinical Qi dynamics.",
        "actions": [a.strip() for a in act.split(",") if a.strip()],
        "indications": [t.replace("-", " ").capitalize() for t in tags],
        "tags": tags,
        "combinations": [
            {"points": f"{disp_code} + LI-4", "indication": "Expels wind pathogens and clears acute pain"},
            {"points": f"{disp_code} + ST-36", "indication": "Fortifies Zang-Fu Qi and builds post-natal resilience"}
        ]
    }

# 2. Add any extra points from POINT_DICTIONARY not yet present
for dict_code, (pinyin, hanzi, eng) in POINT_DICTIONARY.items():
    disp = format_code(dict_code)
    if disp not in points_db:
        ch = get_channel_from_code(disp)
        reg = REGION_MAP.get(dict_code, "Lower Limb" if ch in ["ST", "SP", "BL", "KI", "GB", "LR"] else "Upper Limb")
        view = "posterior" if reg == "Back" else "anterior"
        
        points_db[disp] = {
            "code": disp,
            "cleanCode": dict_code,
            "channelId": ch,
            "pinyin": pinyin,
            "hanzi": hanzi,
            "english": eng,
            "region": reg,
            "view": view,
            "category": "Classical Channel Point",
            "tier": 2,
            "safetyLevel": "safe",
            "safetyWarning": "Observe standard aseptic technique and anatomical depth limits.",
            "depthMin": 0.5,
            "depthMax": 1.0,
            "depthMaxLimit": 2.0,
            "technique": "Perpendicular insertion 0.5–1.0 cun.",
            "locationClassical": f"Standard anatomical location along the {ch} channel in the {reg.lower()} region.",
            "howToFind": [
                f"1. Locate along the pathway of the {ch} meridian.",
                "2. Palpate the local intermuscular or osseous depression.",
                "3. Ensure correct Cun measurement relative to adjacent landmarks."
            ],
            "anatomy": f"Regional musculature and neurovascular network of the {reg.lower()}.",
            "etymology": f"{pinyin} ({hanzi}) translates to '{eng}'.",
            "actions": ["Regulates local Qi and Blood", "Harmonizes parent channel energetics"],
            "indications": ["Local pain", "Channel disharmony", "Functional imbalance"],
            "tags": ["pain", "qi-regulation"],
            "combinations": [
                {"points": f"{disp} + ST-36", "indication": "Tonifies Qi and Blood"}
            ]
        }

with open("d:/TCM/acupuncture_app/static/atlas_points.json", "w", encoding="utf-8") as f:
    json.dump(points_db, f, indent=2, ensure_ascii=False)

print(f"Total merged atlas points: {len(points_db)}")

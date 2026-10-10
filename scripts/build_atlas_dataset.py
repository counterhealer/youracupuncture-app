# -*- coding: utf-8 -*-
"""Process all 429 points from acupuntura.com and produce clean static/atlas_points.json."""
import json
import re

with open("static/atlas_points_all.json", "r", encoding="utf-8") as f:
    raw_points = json.load(f)

print(f"Loaded {len(raw_points)} raw points.")

# Meridian mapping
MERIDIAN_NAMES = {
    "LU": ("Lung", "手太阴肺经", "Shou Taiyin Fei Jing", "Metal", "金", "Yin", "#94a3b8", "肺", "3:00 AM – 5:00 AM", 11, "Upper Limb"),
    "LI": ("Large Intestine", "手阳明大肠经", "Shou Yangming Dachang Jing", "Metal", "金", "Yang", "#fb923c", "肠", "5:00 AM – 7:00 AM", 20, "Upper Limb"),
    "ST": ("Stomach", "足阳明胃经", "Zu Yangming Wei Jing", "Earth", "土", "Yang", "#d97706", "胃", "7:00 AM – 9:00 AM", 45, "Lower Limb"),
    "SP": ("Spleen", "足太阴脾经", "Zu Taiyin Pi Jing", "Earth", "土", "Yin", "#f59e0b", "脾", "9:00 AM – 11:00 AM", 21, "Lower Limb"),
    "HT": ("Heart", "手少阴心经", "Shou Shaoyin Xin Jing", "Fire", "火", "Yin", "#ef4444", "心", "11:00 AM – 1:00 PM", 9, "Upper Limb"),
    "SI": ("Small Intestine", "手太阳小肠经", "Shou Taiyang Xiaochang Jing", "Fire", "火", "Yang", "#f87171", "肠", "1:00 PM – 3:00 PM", 19, "Upper Limb"),
    "BL": ("Bladder", "足太阳膀胱经", "Zu Taiyang Pangguang Jing", "Water", "水", "Yang", "#3b82f6", "胱", "3:00 PM – 5:00 PM", 67, "Back"),
    "KI": ("Kidney", "足少阴肾经", "Zu Shaoyin Shen Jing", "Water", "水", "Yin", "#60a5fa", "肾", "5:00 PM – 7:00 PM", 27, "Lower Limb"),
    "PC": ("Pericardium", "手厥阴心包经", "Shou Jueyin Xinbao Jing", "Fire", "火", "Yin", "#ec4899", "包", "7:00 PM – 9:00 PM", 9, "Upper Limb"),
    "TE": ("Triple Burner", "手少阳三焦经", "Shou Shaoyang Sanjiao Jing", "Fire", "火", "Yang", "#f97316", "焦", "9:00 PM – 11:00 PM", 23, "Upper Limb"),
    "GB": ("Gallbladder", "足少阳胆经", "Zu Shaoyang Dan Jing", "Wood", "木", "Yang", "#22c55e", "胆", "11:00 PM – 1:00 AM", 44, "Head"),
    "LR": ("Liver", "足厥阴肝经", "Zu Jueyin Gan Jing", "Wood", "木", "Yin", "#10b981", "肝", "1:00 AM – 3:00 AM", 14, "Lower Limb"),
    "GV": ("Governing Vessel (Du Mai)", "督脉 (Du Mai)", "Du Mai", "Yang Sea", "阳", "Yang", "#8b5cf6", "督", "Circulation", 28, "Back"),
    "CV": ("Conception Vessel (Ren Mai)", "任脉 (Ren Mai)", "Ren Mai", "Yin Sea", "阴", "Yin", "#14b8a6", "任", "Circulation", 24, "Abdomen"),
    "EX": ("Extraordinary Points", "经外奇穴 (Qi Xue)", "Jingwai Qixue", "Special", "奇", "Special", "#e11d48", "奇", "Empirical", 48, "Head"),
    "HP": ("Huatuojiaji Points", "华佗夹脊 (Jiaji)", "Huatuojiaji", "Special", "脊", "Special", "#6366f1", "华", "Empirical", 20, "Back")
}

# Clean meridians list
meridians_out = []
for m_id, m_info in MERIDIAN_NAMES.items():
    meridians_out.append({
        "id": m_id,
        "name": m_info[0],
        "chinese": m_info[1],
        "pinyin": m_info[2],
        "element": m_info[3],
        "elementChinese": m_info[4],
        "polarity": m_info[5],
        "color": m_info[6],
        "watermark": m_info[7],
        "organTime": m_info[8],
        "totalPoints": m_info[9],
        "primaryRegion": m_info[10]
    })

# Clean points dict: id -> point
clean_points = {}
for p in raw_points:
    pid = p.get("id")
    if not pid:
        continue
    
    m_id = p.get("meridian", "EX")
    trans_en = p.get("translations", {}).get("en", {})
    
    # English name
    eng_name = trans_en.get("englishName") or p.get("englishName") or pid
    
    # Chinese and Pinyin
    pinyin = p.get("pinyin", "")
    hanzi = p.get("chineseCharacters", "")
    
    # Categories and special groups
    cats = p.get("categories", [])
    special = p.get("specialGroups", [])
    five_shu = p.get("fiveShuType")
    cat_str = ""
    if five_shu:
        f_type = five_shu.get("type", "")
        f_elem = five_shu.get("element", "")
        cat_str = f"{f_type} ({f_elem})" if f_elem else f_type
    elif cats:
        cat_str = cats[0]
    elif special:
        cat_str = special[0]
    else:
        cat_str = "Channel Point"
        
    is_major = p.get("clinicalImportance") == "major" or "Command Points" in special or "Yuan-Source Points" in special or "Master Points" in special or pid in ["ST-36", "LI-4", "SP-6", "HT-7", "BL-23", "BL-40", "KI-3", "PC-6", "LR-3", "GV-20", "CV-12", "CV-4", "CV-6", "LU-7", "GB-34", "GB-20"]
    
    # Location
    loc_classical = trans_en.get("location") or p.get("location") or "Refer to standard anatomical landmarks."
    
    # Localization / Palpation steps
    loc_practical = trans_en.get("localization") or ""
    if loc_practical:
        # Split by numbered points or double newlines
        parts = [s.strip() for s in re.split(r'\n{2,}|\d+\.\s*', loc_practical) if s.strip()]
        steps = parts if parts else [loc_practical]
    else:
        steps = [
            f"1. Palpate the anatomical landmarks for {pid} along the {MERIDIAN_NAMES.get(m_id, ('Channel',))[0]} meridian.",
            f"2. Feel for the characteristic depression or inter-muscular groove at the specified Cun measurement.",
            f"3. Verify patient sensation (De Qi — soreness, numbness, distention, or heaviness upon palpation)."
        ]
        
    # Anatomy
    anatomy = trans_en.get("anatomy") or p.get("anatomy") or "Skin, subcutaneous tissue, regional muscles, nerves, and vascular branch."
    
    # Needling and depth
    needling = trans_en.get("needling") or p.get("needling") or "Perpendicular or oblique insertion according to regional anatomy."
    depth_obj = p.get("depth") or {}
    depth_min = depth_obj.get("min", 0.5)
    depth_max = depth_obj.get("max", 1.0)
    depth_max_limit = 3.0 if depth_max <= 2.5 else 4.0
    technique = depth_obj.get("method", "Perpendicular") + " insertion"
    
    # Precautions and safety level
    precautions = trans_en.get("precautions") or p.get("precautions") or "Standard sterile clean needle technique."
    safety_level = p.get("safetyLevel", "safe").lower()
    if safety_level not in ["danger", "caution", "safe"]:
        safety_level = "caution" if ("risk" in precautions.lower() or "artery" in precautions.lower()) else "safe"
        
    # TCM Actions
    actions = trans_en.get("tcmActions") or p.get("tcmActions") or []
    if not actions:
        actions = ["Regulates Qi and Blood circulation", "Restores organ homeostasis", "Opens the channel and alleviates pain"]
        
    # TCM Indications
    tcm_ind = trans_en.get("tcmIndications") or p.get("tcmIndications") or []
    western_ind = trans_en.get("westernIndications") or p.get("westernIndications") or []
    symptom_tags = p.get("symptomTags") or []
    all_tags = []
    for t in symptom_tags:
        all_tags.append(t.replace("-", " "))
    for w in western_ind[:5]:
        if w not in all_tags and len(w) < 30:
            all_tags.append(w)
            
    # Etymology and Clinical Notes
    etymology = trans_en.get("etymology") or p.get("etymology") or f"{pinyin}: Classical nomenclature reflects anatomical topography and therapeutic function."
    clinical_notes = trans_en.get("clinicalNotes") or ""
    
    # Combinations
    combinations = []
    raw_combos = p.get("commonCombinations") or []
    for c in raw_combos:
        c_pt = c.get("pointId") or c.get("points") or ""
        c_ind = c.get("indication") or ""
        if c_pt:
            combinations.append({"points": f"{pid} + {c_pt}", "indication": c_ind})
    if not combinations:
        combinations = [
            {"points": f"{pid} + Source/Luo pair", "indication": "Synergistic reinforcement of channel regulation and targeted pain relief."}
        ]
        
    # Adjacent points
    adj = p.get("adjacentPoints") or {}
    prev_pt = adj.get("prev")
    next_pt = adj.get("next")
    
    # Region
    region_val = p.get("bodyRegion", "Upper Limb").replace("-", " ").title()
    
    clean_points[pid] = {
        "code": pid,
        "channelId": m_id,
        "number": p.get("number", 1),
        "cleanCode": pid.replace("-", ""),
        "pinyin": pinyin,
        "hanzi": hanzi,
        "english": eng_name,
        "category": cat_str,
        "tier": 1 if is_major else 2,
        "region": region_val,
        "locationClassical": loc_classical,
        "howToFind": steps,
        "anatomy": anatomy,
        "needling": needling,
        "depthMin": depth_min,
        "depthMax": depth_max,
        "depthMaxLimit": depth_max_limit,
        "technique": technique,
        "safetyWarning": precautions,
        "safetyLevel": safety_level,
        "actions": actions,
        "tcmIndications": tcm_ind,
        "westernIndications": western_ind,
        "tags": all_tags[:8],
        "etymology": etymology,
        "clinicalNotes": clinical_notes,
        "combinations": combinations,
        "prevPoint": prev_pt,
        "nextPoint": next_pt,
        "image": f"/app/static/atlas_images/{m_id}/{pid.replace('-', '')}.jpg" if p.get("image") else "",
        "remoteImage": f"https://acupuntura.com/atlas-images/{m_id}/{pid.replace('-', '')}.jpg" if p.get("image") else "",
        "hasImage": bool(p.get("image"))
    }


print(f"Processed {len(clean_points)} clean points.")

# Save both json files
with open("static/atlas_meridians.json", "w", encoding="utf-8") as f_m:
    json.dump(meridians_out, f_m, ensure_ascii=False, indent=2)

with open("static/atlas_points.json", "w", encoding="utf-8") as f_p:
    json.dump(clean_points, f_p, ensure_ascii=False, indent=2)

print("Saved static/atlas_meridians.json and static/atlas_points.json successfully!")

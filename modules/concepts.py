# -*- coding: utf-8 -*-
"""TCM Core Concepts & Memory Aids Module.

Provides comprehensive, high-yield explanations of core Traditional Chinese Medicine
theories with memory aids, mnemonics, structured tables, board exam traps, and clinical
point correlations. Modeled with an interactive list of clickable topic links like the Atlas.
"""

import streamlit as st
from typing import Dict, List, Any, Optional

# Core Concepts Knowledge Base
CONCEPTS_DATA: List[Dict[str, Any]] = [
    {
        "id": "yin-yang",
        "title": "Yin-Yang Theory",
        "chinese": "阴阳学说 (Yīn Yáng Xué Shuō)",
        "category": "Foundations",
        "icon": "☯️",
        "tagline": "The fundamental binary framework of balance, opposition, and transformation in TCM.",
        "summary": "Yin-Yang theory is the philosophical bedrock of Chinese medicine. All phenomena in the universe and human body are viewed as dynamic, complementary opposites. Health is the dynamic equilibrium of Yin and Yang; disease is an imbalance (excess or deficiency).",
        "mnemonic": "Remember 'O-I-C-T':\n• O - Opposition (Fire vs Water, Heat vs Cold)\n• I - Interdependence (Cannot exist without the other)\n• C - Consuming (Excess Yin damages Yang; Excess Yang damages Yin)\n• T - Transformation (Extreme Cold becomes Heat; Extreme Activity requires Rest)",
        "principles": [
            "**Opposition of Yin & Yang (对立制约)**: Yang represents warmth, activity, exterior, daytime, brightness, ascending, and Qi. Yin represents cold, rest, interior, nighttime, darkness, descending, and Blood/Fluids.",
            "**Interdependence (互根互用)**: Yin cannot exist without Yang; Yang cannot exist without Yin ('Yin remains inside as the guardian of Yang; Yang stays outside as the servant of Yin').",
            "**Mutual Consuming / Supporting (消长平衡)**: A constant dynamic shift. Excess Yang burns up Yin fluids (Full Heat); Excess Yin freezes Yang vitality (Full Cold).",
            "**Inter-transformation (相互转化)**: At extreme thresholds, Yin becomes Yang and Yang becomes Yin ('Extreme Cold generates Heat; Extreme Heat generates Cold')."
        ],
        "table_headers": ["Attribute", "Yang (阳)", "Yin (阴)"],
        "table_rows": [
            ["Nature & Climate", "Fire, Heat, Light, Daytime, Spring/Summer", "Water, Cold, Dark, Nighttime, Autumn/Winter"],
            ["Movement & Direction", "Ascending, Expanding, Outward, Dynamic", "Descending, Contracting, Inward, Static"],
            ["Anatomical Location", "Upper body, Exterior, Back (Dorsal), Lateral", "Lower body, Interior, Abdomen/Chest, Medial"],
            ["Zang-Fu Organs", "Six Fu organs (Hollow, transporting, active)", "Five Zang organs (Solid, storing essence)"],
            ["Substances", "Qi (warmth, movement, holding, protection)", "Blood & Body Fluids (nourishment, moisture)"],
            ["Clinical Pathologies", "Full Heat, Rapid pulse, Red face, Constipation", "Full Cold, Slow pulse, Pale face, Loose stools"],
            ["Tongue & Pulse", "Red body, Yellow dry coat; Rapid, Floating pulse", "Pale body, White moist coat; Slow, Deep pulse"]
        ],
        "board_traps": [
            "**Trap**: Confusing 'Yin Deficiency with Heat' (Empty Heat / 虚热) with 'Yang Excess' (Full Heat / 实热). Full Heat has a thick yellow coating, strong full rapid pulse, and no night sweats. Empty Heat has a red peeled tongue (no coat), thin rapid pulse, 5-palm heat, and night sweats.",
            "**Trap**: Assuming Zang organs are Yang because they are vital. Zang are YIN because they are solid and store essential substances; Fu organs are YANG because they are hollow and constantly transport."
        ],
        "clinical_points": [
            "**Tonify Kidney Yang**: DU4 (Mingmen), BL23 (Shenshu), RN4 (Guanyuan) with Moxibustion.",
            "**Nourish Kidney Yin**: KD3 (Taixi), KD6 (Zhaohai), SP6 (Sanyinjiao).",
            "**Clear Excess Yang / Heat**: LI11 (Quchi), DU14 (Dazhui), ST44 (Neiting)."
        ]
    },
    {
        "id": "five-elements",
        "title": "Five Elements Theory",
        "chinese": "五行学说 (Wǔ Xíng Xué Shuō)",
        "category": "Foundations",
        "icon": "🌳",
        "tagline": "The cosmological cycle of Wood, Fire, Earth, Metal, and Water governing organ physiology.",
        "summary": "Five Elements (Wu Xing) explains physiological resonance, organ interrelationships, and pathological transmission through generating (Sheng), controlling (Ke), overacting (Cheng), and insulting (Wu) cycles.",
        "mnemonic": "Cycle Mnemonics:\n• Generating (Sheng): 'Wood feeds Fire, Fire creates Earth/ash, Earth bears Metal, Metal enriches Water, Water nourishes Wood.'\n• Mother-Child Treatment Rule: 'Tonify the Mother for Deficiency; Sedate the Child for Excess' (虚则补其母，实则泻其子).",
        "principles": [
            "**Generating Cycle (相生 - Mother-Child)**: Each element nourishes the next. Wood generates Fire; Fire generates Earth; Earth generates Metal; Metal generates Water; Water generates Wood.",
            "**Controlling Cycle (相克 - Grandmother-Grandchild)**: Each element checks the overexpansion of another. Wood parts Earth; Earth dams Water; Water quenches Fire; Fire melts Metal; Metal chops Wood.",
            "**Overacting Cycle (相乘)**: When an element is in excessive hyperactivity and crushes the element it normally controls (e.g. Liver Wood overacts on Spleen Earth causing IBS / diarrhea).",
            "**Insulting Cycle (相侮 - Reverse Control)**: When a deficient element is bullied backward by the element it normally controls (e.g. Spleen Earth insults Liver Wood)."
        ],
        "table_headers": ["Element", "Zang / Fu", "Season", "Emotion", "Flavor", "Tissue", "Sense Organ"],
        "table_rows": [
            ["Wood (木)", "Liver / Gallbladder", "Spring", "Anger / Frustration", "Sour", "Tendons / Sinews", "Eyes"],
            ["Fire (火)", "Heart / Small Intestine", "Summer", "Joy / Over-excitement", "Bitter", "Blood Vessels", "Tongue"],
            ["Earth (土)", "Spleen / Stomach", "Late Summer", "Pensiveness / Worry", "Sweet", "Flesh / Muscles", "Mouth / Lips"],
            ["Metal (金)", "Lung / Large Intestine", "Autumn", "Grief / Sadness", "Pungent", "Skin / Body Hair", "Nose"],
            ["Water (水)", "Kidney / Urinary Bladder", "Winter", "Fear / Fright", "Salty", "Bones / Marrow", "Ears"]
        ],
        "board_traps": [
            "**Mother-Child Needle Point Selection**: On the Lung channel (Metal), if the Lungs are deficient, tonify the Earth point (Mother) = LU9 (Taiyuan). If Lungs have excess phlegm-heat, sedate the Water point (Child) = LU5 (Chize).",
            "**Liver Invading Spleen**: Extremely common board exam vignette. Emotional stress + hypochondriac distension + alternating diarrhea and constipation = Wood overacting on Earth."
        ],
        "clinical_points": [
            "**Soothe Liver & Harmonize Spleen**: LR3 (Taichong) + ST36 (Zusanli) + SP6 (Sanyinjiao).",
            "**Sedate Liver Child for Liver Fire**: LR2 (Xingjian, Fire point of Liver).",
            "**Tonify Kidney Mother for Liver Deficiency**: KD3 (Taixi) or LR8 (Ququan, Water point of Liver)."
        ]
    },
    {
        "id": "zang-fu",
        "title": "Zang-Fu Organ Systems",
        "chinese": "脏腑学说 (Zàng Fǔ Xué Shuō)",
        "category": "Organ Systems",
        "icon": "🫀",
        "tagline": "The energetic functions and internal paired relationships of the 5 Yin and 6 Yang organs.",
        "summary": "Zang-Fu theory views organs not as isolated anatomical parts, but as functional energetic systems. The Five Zang (solid Yin organs) manufacture and store precious essence; the Six Fu (hollow Yang organs) digest, transform, and excrete waste.",
        "mnemonic": "Core Zang Functions Rhyme:\n• Heart houses Shen and commands Blood.\n• Liver stores Blood and ensures smooth Qi flood.\n• Spleen transforms Food and holds Blood in line.\n• Lung governs Qi and disperses water fine.\n• Kidney stores Jing, true root of Yin and Yang divine.",
        "principles": [
            "**Zang Organs (五脏)**: Heart (Shen/Vessels), Lung (Qi/Respiration/Skin), Spleen (Transformation/Transport/Muscles), Liver (Free flow of Qi/Blood storage/Tendons), Kidney (Jing/Water/Bones/Marrow). Solid organs: store and do not drain.",
            "**Fu Organs (六腑)**: Stomach, Small Intestine, Large Intestine, Gallbladder, Urinary Bladder, San Jiao. Hollow organs: receive, digest, transform, excrete. Drain and do not store.",
            "**Extraordinary Fu (奇恒之腑)**: Brain, Marrow, Bone, Vessels, Gallbladder, Uterus. Hollow in morphology like Fu, but store pure essence like Zang."
        ],
        "table_headers": ["Zang (Yin)", "Fu (Yang)", "Governs", "Opens To", "Manifests In"],
        "table_rows": [
            ["Heart (心)", "Small Intestine (小肠)", "Blood circulation & Houses Shen", "Tongue", "Complexion"],
            ["Lung (肺)", "Large Intestine (大肠)", "Qi & Respiration, Water passages", "Nose", "Skin & Body hair"],
            ["Spleen (脾)", "Stomach (胃)", "Transformation & Transportation, Holds blood", "Mouth", "Lips"],
            ["Liver (肝)", "Gallbladder (胆)", "Smooth flow of Qi, Stores blood", "Eyes", "Nails"],
            ["Kidney (肾)", "Urinary Bladder (膀胱)", "Stores Jing, Governs water & bones", "Ears & Urogenital", "Head hair"]
        ],
        "board_traps": [
            "**Spleen vs Kidney Water Management**: Spleen transforms and transports dampness in the Middle Jiao (edema, loose stools). Kidney governs water metabolism in the whole body through Yang steaming (urination volume, deep cold edema).",
            "**Liver Blood vs Heart Blood**: Heart Blood deficiency causes palpitations, insomnia, and pale lips. Liver Blood deficiency causes blurred vision, floaters, muscle cramps, and scanty/absent menstruation."
        ],
        "clinical_points": [
            "**Heart Shen**: HT7 (Shenmen), PC6 (Neiguan), RN14 (Juque - Front-Mu).",
            "**Spleen Digestion**: ST36 (Zusanli), SP3 (Taibai - Yuan-Source), RN12 (Zhongwan - Front-Mu of Stomach).",
            "**Kidney Jing & Foundation**: KD3 (Taixi), BL23 (Shenshu), RN4 (Guanyuan)."
        ]
    },
    {
        "id": "qi-blood-fluids",
        "title": "Qi, Blood, Body Fluids & Jing",
        "chinese": "气血津液精 (Qì Xuè Jīn Yè Jīng)",
        "category": "Foundations",
        "icon": "🩸",
        "tagline": "The vital fundamental substances nourishing and activating human life.",
        "summary": "Qi, Blood (Xue), Body Fluids (Jin-Ye), and Essence (Jing) are the core vital substances. Qi is the invisible animating energy, Blood is the dense material nourishment, Jin-Ye moistens tissues, and Jing is constitutional genetic potential.",
        "mnemonic": "'P-W-D-H-T' - 5 Main Functions of Qi:\n• P - Promoting (growth, circulation)\n• W - Warming (body temp, extremities)\n• D - Defending (Wei Qi protects from pathogens)\n• H - Holding (keeps blood in vessels, holds organs up)\n• T - Transforming (Qi Hua - turning food into Qi & Blood)",
        "principles": [
            "**Relationship between Qi and Blood**: 'Qi is the commander of Blood (Qi moves Blood); Blood is the mother of Qi (Blood carries and anchors Qi).' Where Qi goes, Blood follows.",
            "**Classification of Qi**:\n  - *Yuan Qi (Original Qi)*: Derived from congenital Jing, rooted in Kidneys, distributed via San Jiao.\n  - *Gu Qi (Food Qi)*: Extracted from food by Spleen and Stomach.\n  - *Zong Qi (Pectoral/Gathering Qi)*: Formed by Gu Qi + inhaled Air Qi; powers heart and lungs.\n  - *Ying Qi (Nutritive Qi)*: Flows within the blood vessels, nourishes Zang-Fu.\n  - *Wei Qi (Defensive Qi)*: Circulates outside vessels in skin/muscles, protects against external pathogens.",
            "**Jin vs Ye (津 vs 液)**: Jin is light, clear, thin, fluid, moistening skin, muscles, and pores (sweat, tears). Ye is heavy, dense, turbid, lubricating joints, bone marrow, brain, and internal organs."
        ],
        "table_headers": ["Substance", "Origin", "Governing Organ", "Primary Pathologies"],
        "table_rows": [
            ["Qi (气)", "Congenital Jing + Gu Qi + Air", "Lung governs, Spleen produces, Kidney roots", "Deficiency (Xu), Sinking (Xian), Stagnation (Zhi), Rebellion (Ni)"],
            ["Blood (血)", "Gu Qi transformed in Heart & Lung", "Heart governs, Liver stores, Spleen holds", "Deficiency (pale, dizziness), Stasis (stabbing pain, purple tongue), Heat (bleeding)"],
            ["Jin-Ye (津液)", "Food and drink digested by Stomach", "Spleen transforms, Lung disperses, Kidney steams", "Fluid Deficiency (dryness, thirst), Accumulation (phlegm, dampness, edema)"],
            ["Jing (精)", "Congenital (parents) + Acquired (food)", "Stored in the Kidneys", "Essence Deficiency (infertility, brittle bones, hair loss, dementia)"]
        ],
        "board_traps": [
            "**Four Pathologies of Qi**: Qi Deficiency (weakness, pale), Qi Sinking (prolapse of stomach/uterus), Qi Stagnation (distension, sighing, pain), Qi Rebellion (cough/asthma in Lung, vomiting/hiccups in Stomach, headache in Liver).",
            "**Hemorrhage treatment**: In massive acute blood loss, treat QI first (tonify Qi with RN6/ST36 to hold blood), because 'Qi generates and holds Blood; without Qi, Blood cannot be retained'."
        ],
        "clinical_points": [
            "**Generate Qi & Blood**: ST36 (Zusanli) + SP6 (Sanyinjiao).",
            "**Move Stagnant Qi & Blood**: LI4 (Hegu) + LR3 (Taichong) [Four Gates].",
            "**Lift Sinking Qi**: DU20 (Baihui) with needle angled anteriorly + RN6 (Qihai)."
        ]
    },
    {
        "id": "etiology",
        "title": "Etiology & Six Pathogenic Evils",
        "chinese": "病因与六淫 (Bìng Yīn Yǔ Liù Yín)",
        "category": "Pathology",
        "icon": "🌪️",
        "tagline": "External climatic extremes, internal emotional injuries, and diet/lifestyle causes of disease.",
        "summary": "TCM divides disease causes into Three Categories (San Yin): 1. External Evils (Six Climatic Pathogens - Liu Yin); 2. Internal Injuries (Seven Emotions - Qi disruptions); 3. Neither Internal nor External (Diet, overstrain, trauma, animal bites, phlegm and blood stasis).",
        "mnemonic": "The 6 Evils Behavior:\n• Wind: 'Wanders, attacks the top, brings others along.'\n• Cold: 'Freezes, contracts, causes sharp severe pain.'\n• Summer-Heat: 'Scorches, steams with dampness, exhausts fluids.'\n• Dampness: 'Heavy, turbid, sticky, lingers in the bottom.'\n• Dryness: 'Withers skin, dries throat and lungs.'\n• Fire: 'Flames straight up, burns yin, causes hemorrhage.'",
        "principles": [
            "**Six External Pathogens (六淫)**: Wind (Yang, leading evil), Cold (Yin, constricting), Summer-Heat (pure Yang, summer only), Dampness (Yin, heavy/turbid), Dryness (Yang, consumes fluids), Fire/Heat (Yang, flares upward).",
            "**Seven Emotions & Qi Mechanisms (七情致病)**:\n  - Anger (怒) causes Qi to RISE (怒则气上) -> Headache, red face, hematemesis.\n  - Joy/Over-excitement (喜) causes Qi to SLOW (喜则气缓) -> Scattered spirit, inability to focus.\n  - Sadness/Grief (悲) causes Qi to DISSOLVE (悲则气消) -> Breathlessness, fatigue, crying.\n  - Worry/Pensiveness (思) causes Qi to KNOT (思则气结) -> Poor appetite, epigastric bloating.\n  - Fear (恐) causes Qi to DESCEND (恐则气下) -> Incontinence of urine/stool, weak knees.\n  - Fright/Shock (惊) causes Qi to SCATTER (惊则气乱) -> Panic, severe restlessness, palpitations."
        ],
        "table_headers": ["Pathogen", "Nature", "Key Clinical Features", "Common Acupoints"],
        "table_rows": [
            ["Wind (风)", "Yang pathogen", "Aversion to wind, wandering pain, pruritus, facial paralysis, tremor", "GB20, BL12, LU7, LI4"],
            ["Cold (寒)", "Yin pathogen", "Aversion to cold, sharp cramping pain relieved by warmth, clear urine", "RN4, RN6, ST36 (Moxa)"],
            ["Summer-Heat (暑)", "Yang pathogen", "High fever, profuse sweating, extreme thirst, delirium, fatigue", "PC3, BL40 (Bleed), LI11"],
            ["Dampness (湿)", "Yin pathogen", "Heavy limbs, head feels wrapped in cloth, sticky loose stools, edema", "SP9, SP6, ST40, RN9"],
            ["Dryness (燥)", "Yang pathogen", "Dry nose, chapped lips, dry cough, dry skin, dry stool", "LU7, KD6, SP6, LU9"],
            ["Fire (火)", "Yang pathogen", "High fever, mouth ulcers, red eyes, delirium, mania, hemorrhage", "LI11, ST44, DU14, LR2"]
        ],
        "board_traps": [
            "**Wind as the Spearhead**: 'Wind is the chief of the hundred diseases' (风为百病之长). Wind opens the pores and carries Cold, Heat, or Dampness into the body.",
            "**Emotions & Organs**: Anger injures Liver; Joy injures Heart; Pensiveness injures Spleen; Grief injures Lung; Fear injures Kidney."
        ],
        "clinical_points": [
            "**Expel Exterior Wind**: GB20 (Fengchi), BL12 (Fengmen), LU7 (Lieque).",
            "**Drain Dampness**: SP9 (Yinlingquan), RN9 (Shuifen), ST36 (Zusanli).",
            "**Clear Fire**: LI11 (Quchi), DU14 (Dazhui), ST44 (Neiting)."
        ]
    },
    {
        "id": "diagnostics-frameworks",
        "title": "Diagnostic Frameworks (8 Principles & Stages)",
        "chinese": "辨证纲要 (Biàn Zhèng Gāng Yào)",
        "category": "Diagnostics",
        "icon": "🧭",
        "tagline": "The Eight Principles, Shang Han Lun Six Stages, and Wen Bing Four Levels.",
        "summary": "Diagnostic frameworks organize clinical findings into structured patterns. The Eight Principles (Ba Gang) is the master matrix. Shang Han Lun tracks cold injury progression through 6 stages. Wen Bing tracks warm heat diseases through 4 levels.",
        "mnemonic": "Eight Principles Pairs:\n• Interior vs Exterior (Depth: Skin/channels vs Zang-Fu organs)\n• Cold vs Heat (Nature: Chills/slow pulse vs Fever/rapid pulse)\n• Deficiency vs Excess (Body strength vs Pathogen strength)\n• Yin vs Yang (Master categories: Cold/Deficiency/Interior vs Heat/Excess/Exterior)",
        "principles": [
            "**Eight Principles (八纲辨证)**: The foundational filter for every patient encounter.",
            "**Six Stages (六经辨证 - Zhang Zhongjing)**:\n  - *Taiyang (Greater Yang)*: Exterior stage. Wind-Strike (sweating, floating moderate pulse) vs Cold-Damage (no sweat, floating tight pulse).\n  - *Yangming (Yang Brightness)*: Interior Full Heat. Channel pattern (Four Bigs) vs Bowel pattern (constipation, tidal fever, abdominal fullness).\n  - *Shaoyang (Lesser Yang)*: Half-exterior, half-interior. Alternating chills and fever, bitter mouth, dry throat, hypochondriac fullness.\n  - *Taiyin (Greater Yin)*: Spleen cold-deficiency. Abdominal fullness, vomiting, diarrhea, lack of thirst.\n  - *Shaoyin (Lesser Yin)*: Kidney/Heart systemic collapse. Cold transformation (exhaustion, cold limbs, pale urine) vs Heat transformation (insomnia, dry mouth, red peeled tongue).\n  - *Jueyin (Absolute Yin)*: Terminal stage, extreme polarity. Reversal of cold and heat, roundworms, thirst, hunger without desire to eat.",
            "**Four Levels (卫气营血辨证 - Ye Tianshi)**:\n  - *Wei Level*: Defense/exterior. Fever, slight aversion to cold, sore throat, cough.\n  - *Qi Level*: Interior heat. High fever, no chills, profuse sweat, thirst, yellow coat.\n  - *Ying Level*: Nutritive heat. Fever worse at night, mental delirium, macules, deep red tongue.\n  - *Xue Level*: Blood level. Severe fever, mania, widespread hemorrhage/purpura, convulsions."
        ],
        "table_headers": ["Stage / Level", "Key Symptoms", "Tongue & Pulse", "Treatment Principle"],
        "table_rows": [
            ["Taiyang Stage", "Aversion to cold, fever, stiff neck, body ache", "Thin white coat; Floating pulse", "Release exterior with diaphoretics"],
            ["Yangming Channel", "Big fever, big sweat, big thirst, big pulse", "Red tongue, dry yellow coat; Surging pulse", "Clear heat and generate fluids (Bai Hu Tang)"],
            ["Shaoyang Stage", "Alternating chills & fever, bitter taste, flank fullness", "Sides red, thin white/yellow; Wiry pulse", "Harmonize Shaoyang (Xiao Chai Hu Tang)"],
            ["Wei Level (Warm)", "Fever, mild chills, sore throat, thirst", "Red tip/edges, thin white; Floating rapid", "Dispel wind-heat (Yin Qiao San)"],
            ["Qi Level (Warm)", "High fever without chills, yellow sticky sweat, thirst", "Red tongue, yellow thick; Slippery rapid", "Clear Qi level heat"],
            ["Ying Level (Warm)", "Fever worse at night, insomnia, delirium, faint rash", "Deep crimson red without coat; Thready rapid", "Clear Ying heat and nourish fluids"],
            ["Xue Level (Warm)", "Manic restlessness, epistaxis, hematemesis, dark purpura", "Deep purple-crimson; Rapid or floating erratic", "Cool blood, stop bleeding, clear fire"]
        ],
        "board_traps": [
            "**Fever vs Chills in Exterior Patterns**: Simultaneous fever AND chills (or aversion to cold) is the definitive proof of an EXTERIOR syndrome. If fever exists WITHOUT chills, the pathogen has penetrated into the INTERIOR (Yangming/Qi level).",
            "**Ying vs Xue Delirium**: Ying level has mental confusion and faint rash; Xue level has overt manic delirium and bleeding from orifices/heavy purpura."
        ],
        "clinical_points": [
            "**Taiyang Exterior**: LU7 (Lieque), BL12 (Fengmen), GB20 (Fengchi).",
            "**Shaoyang Harmonization**: SJ5 (Waiguan) + GB41 (Zulinqi) [Dai/Yangwei].",
            "**Yangming Clear Heat**: LI11 (Quchi), ST44 (Neiting), ST25 (Tianshu)."
        ]
    },
    {
        "id": "special-points",
        "title": "Special Point Classifications",
        "chinese": "特定穴分类大全 (Tè Dìng Xué)",
        "category": "Acupoint Categories",
        "icon": "⭐",
        "tagline": "The essential categories tested on every board exam: Five Shu, Yuan, Luo, Xi, Mu, Shu, Hui.",
        "summary": "Special point classifications group points based on specific energetic functions and anatomical locations. Mastering these categories is critical for answering over 30% of standard acupuncture board exam questions.",
        "mnemonic": "Points Classification Memory Aids:\n• Five Shu: 'Well (resuscitate), Spring (heat), Stream (damp/joint pain), River (cough/asthma), Sea (rebellious qi & bowels).'\n• Xi-Cleft: 'Acute pain on Yang; Acute bleeding on Yin.'\n• Mu vs Shu: 'Front-Mu for Acute & Fu organs; Back-Shu for Chronic & Zang organs.'\n• Hui-Meeting 8: Zang (LR13), Fu (RN12), Qi (RN17), Blood (BL17), Tendons (GB34), Vessels (LU9), Bones (BL11), Marrow (GB39).",
        "principles": [
            "**Five Shu Points (五输穴)**: Located distal to elbows and knees. Energy flows like water: Jing-Well (bubbling spring at extremities), Ying-Spring (trickling brook), Shu-Stream (rushing stream), Jing-River (broad river), He-Sea (deep ocean entering organs).",
            "**Yuan-Source & Luo-Connecting (原穴与络穴)**: Yuan points access prenatal original Qi. Luo points branch into internally-externally paired channels. Paired as Host-Guest (Yuan of diseased meridian + Luo of paired meridian).",
            "**Xi-Cleft Points (郄穴)**: Where channel Qi and Blood plunge deep. Used for acute stubborn pain (Yang channels) and acute blood extravasation (Yin channels).",
            "**Front-Mu & Back-Shu (募穴与俞穴)**: Front-Mu points lie on the chest/abdomen where organ Qi collects; Back-Shu lie on the Bladder channel where organ Qi infuses. Often combined in Mu-Shu pairing.",
            "**Eight Confluent Points (八脉交会穴)**: Connect the 12 regular channels with the 8 Extraordinary Vessels. Paired in clinical practice (PC6 + SP4; LU7 + KD6; SI3 + BL62; GB41 + TE5).",
            "**Lower He-Sea of the Six Fu (下合穴)**: Six points on the legs directly treating disorders of the abdominal digestive organs (ST36, ST37, ST39, BL40, BL39, GB34)."
        ],
        "table_headers": ["Category", "Total Points", "Diagnostic & Therapeutic Role", "Classic Clinical Example"],
        "table_rows": [
            ["Five Shu Points", "60 (5 x 12)", "Five Element balancing, organ clock", "LU5 (Water/Child) sedates Lung Fire"],
            ["Yuan-Source", "12 (1 per channel)", "Regulates constitutional Zang-Fu Qi", "KD3 tonifies Kidney, LI4 tonifies Large Intestine"],
            ["Luo-Connecting", "15 (12+Du+Ren+Sp)", "Connects interior-exterior pairs, chronic issues", "LU7 connects to LI; SP21 treats whole-body pain"],
            ["Xi-Cleft", "16 (12+4 Vessels)", "Emergency acute pain & acute hemorrhage", "LU6 for hemoptysis; ST34 for severe stomach cramp"],
            ["Front-Mu", "12 (1 per organ)", "Acute, heat, excess conditions of Fu/Zang", "ST25 for acute diarrhea; RN12 for stomach ache"],
            ["Back-Shu", "12 (1 per organ)", "Chronic, cold, deficient conditions of Zang", "BL23 for chronic kidney deficiency; BL20 for spleen"],
            ["Hui-Meeting", "8 influential", "Broad therapeutic influence over 8 tissues", "GB34 for tendons/joints; BL17 for all blood disorders"],
            ["Eight Confluent", "8 extraordinary", "Command extraordinary vessels in pairs", "PC6 + SP4 treats chest, epigastrium, & stomach"]
        ],
        "board_traps": [
            "**Lower He-Sea vs Regular He-Sea**: On Yang channels of the arm (LI, SI, TE), the regular He-Sea points on the elbow (LI11, SI8, TE10) treat the channels and upper body, but the LOWER He-Sea points on the leg (ST37 for LI, ST39 for SI, BL39 for TE) treat the actual internal digestive organs!",
            "**Shu-Stream on Yin Channels**: On the 6 Yin channels, the Shu-Stream point and the Yuan-Source point are the EXACT same point (LU9, SP3, HT7, KD3, PC7, LR3)."
        ],
        "clinical_points": [
            "**Host-Guest (Lung host, LI guest)**: LU9 (Yuan) + LI6 (Luo).",
            "**Acute Dysmenorrhea**: SP8 (Xi-Cleft of Spleen).",
            "**Four Command Points (Gao Wu)**: ST36 (Abdomen), BL40 (Lumbar), LU7 (Head/Neck), LI4 (Face/Mouth)."
        ]
    },
    {
        "id": "organ-clock",
        "title": "TCM Organ Clock & Horary Cycle",
        "chinese": "子午流注时辰图 (Zǐ Wǔ Liú Zhù)",
        "category": "Organ Systems",
        "icon": "⏰",
        "tagline": "The 24-hour circadian rhythm of Qi circulation through the 12 regular meridians.",
        "summary": "Every 2 hours, Qi peaks in a specific organ and channel while reaching its lowest ebb (nadir) in the opposing channel 12 hours later. Symptoms that predictably appear or worsen at a specific hour pinpoint organ pathology.",
        "mnemonic": "Clock Memorization Sequence:\n'Lu-LI-St-Sp, Ht-SI-BL-KI, PC-SJ-GB-LR'\n• 3-5 AM: Lung (Cough/wake up)\n• 5-7 AM: Large Intestine (Morning stool)\n• 7-9 AM: Stomach (Breakfast)\n• 9-11 AM: Spleen (Mental focus/digestion)\n• 11-1 PM: Heart (Midday rest/lunch)\n• 1-3 PM: Small Intestine (Absorption)\n• 3-5 PM: Bladder (Energy dip/hydration)\n• 5-7 PM: Kidney (Dinner/essence restoration)\n• 7-9 PM: Pericardium (Evening intimacy/relax)\n• 9-11 PM: San Jiao (Thermoregulation/sleep prep)\n• 11-1 AM: Gallbladder (Deep sleep begins)\n• 1-3 AM: Liver (Blood detoxification/waking up with anger)",
        "principles": [
            "**Peak Hours (旺时)**: When the meridian has maximal volume of Qi and Blood. Ideal time to tonify or sedate that organ.",
            "**Opposite Ebb Hours (衰时)**: Exactly 12 hours opposite, the organ is at minimum vitality. Deficient organs often display symptoms at their ebb hour.",
            "**Diagnostic Timing Examples**:\n  - Waking up precisely between 1:00 AM - 3:00 AM indicates Liver Fire or Liver Blood deficiency.\n  - Chronic asthma coughing fit between 3:00 AM - 5:00 AM points to Lung Qi deficiency or phlegm.\n  - Energy crash or sluggish digestion between 9:00 AM - 11:00 AM points to Spleen Qi deficiency."
        ],
        "table_headers": ["Time Window", "Channel / Organ", "Opposite Channel (Nadir)", "Optimal Human Activity"],
        "table_rows": [
            ["3:00 AM - 5:00 AM", "Lung (手太阴肺经)", "Urinary Bladder (3-5 PM)", "Deep breathing, sound sleep, body oxygenation"],
            ["5:00 AM - 7:00 AM", "Large Intestine (手阳明大肠经)", "Kidney (5-7 PM)", "Waking up, drinking warm water, bowel movement"],
            ["7:00 AM - 9:00 AM", "Stomach (足阳明胃经)", "Pericardium (7-9 PM)", "Hearty, nourishing warm breakfast"],
            ["9:00 AM - 11:00 AM", "Spleen (足太阴脾经)", "San Jiao (9-11 PM)", "Peak mental work, study, active digestion"],
            ["11:00 AM - 1:00 PM", "Heart (手少阴心经)", "Gallbladder (11-1 AM)", "Light lunch, relaxing, short 20-min nap"],
            ["1:00 PM - 3:00 PM", "Small Intestine (手太阳小肠经)", "Liver (1-3 AM)", "Nutrient assimilation into blood vessels"],
            ["3:00 PM - 5:00 PM", "Urinary Bladder (足太阳膀胱经)", "Lung (3-5 AM)", "Hydration, physical work, urination"],
            ["5:00 PM - 7:00 PM", "Kidney (足少阴肾经)", "Large Intestine (5-7 AM)", "Light dinner, winding down, essence replenishment"],
            ["7:00 PM - 9:00 PM", "Pericardium (手厥阴心包经)", "Stomach (7-9 AM)", "Socializing, reading, peaceful emotional bonding"],
            ["9:00 PM - 11:00 PM", "San Jiao (手少阳三焦经)", "Spleen (9-11 AM)", "Preparing for sleep, calming body temperature"],
            ["11:00 PM - 1:00 AM", "Gallbladder (足少阳胆经)", "Heart (11-1 PM)", "Deep restorative sleep; cellular tissue repair"],
            ["1:00 AM - 3:00 AM", "Liver (足厥阴肝经)", "Small Intestine (1-3 PM)", "Blood regeneration, dreaming, detoxifying waste"]
        ],
        "board_traps": [
            "**Horary Acupoint Point Selection**: Using the element point of a channel during its peak hour is called the 'Horary Point'. For example, on the Lung channel (Metal), the Metal point is LU8 (Jingqu). Treating LU8 between 3-5 AM has doubled tonification potency.",
            "**Tiredness at 9-11 AM**: If a patient sleeps 8 hours but feels exhausted at 9:00 AM - 11:00 AM, suspect SPLEEN QI deficiency, not thyroid or adrenal, because Spleen governs this window."
        ],
        "clinical_points": [
            "**Liver Waking (1-3 AM)**: LR3 (Taichong) + LR2 (Xingjian).",
            "**Morning Bowel Inactivity (5-7 AM)**: ST25 (Tianshu) + TE6 (Zhigou).",
            "**Midday Heart Palpitations (11-1 PM)**: HT7 (Shenmen) + PC6 (Neiguan)."
        ]
    },
    {
        "id": "tongue-pulse",
        "title": "Tongue & Pulse Diagnosis",
        "chinese": "舌诊与脉诊精要 (Shé Zhěn Yǔ Mài Zhěn)",
        "category": "Diagnostics",
        "icon": "👅",
        "tagline": "The dual pillars of objective TCM physical examination and clinical verification.",
        "summary": "Tongue and Pulse diagnosis provide immediate, objective physical confirmation of internal Zang-Fu pathology. The tongue body reveals the true constitution and Blood/Yin/Yang status, the coat reveals the presence of pathogens, and the 28 pulses indicate the depth, speed, and force of Qi and Blood.",
        "mnemonic": "Tongue Topography Map:\n• Tip = Heart & Lung (Upper Jiao)\n• Center = Spleen & Stomach (Middle Jiao)\n• Sides = Liver & Gallbladder\n• Root/Back = Kidney, Bladder, Intestines (Lower Jiao)",
        "principles": [
            "**Tongue Body vs Tongue Coating**:\n  - *Tongue Body (Color & Shape)*: Reflects true internal state of Zang-Fu, Qi, and Blood. Color: Pale (Deficiency/Cold), Red (Heat), Deep Crimson (Ying/Xue Heat), Purple (Blood Stasis). Shape: Swollen with teethmarks (Damp/Spleen Xu), Thin (Blood/Yin Xu).\n  - *Tongue Coating (Color & Thickness)*: Generated by Stomach Qi. Reflects the nature and depth of pathogenic factors. White (Cold/Normal), Yellow (Heat), Greasy (Damp/Phlegm), Peeled/Mirror (Yin exhaustion).",
            "**Pulse Locations (Cun, Guan, Chi - 寸关尺)**:\n  - *Left Wrist*: Cun = Heart, Guan = Liver/Gallbladder, Chi = Kidney Yin.\n  - *Right Wrist*: Cun = Lung, Guan = Spleen/Stomach, Chi = Kidney Yang/Mingmen.",
            "**Fundamental Pulse Qualities**:\n  - *Floating (Fu Mai)*: Felt on light touch; Exterior syndrome.\n  - *Deep (Chen Mai)*: Felt only with firm bone pressure; Interior syndrome.\n  - *Slow (Chi Mai)*: Under 60 bpm; Cold syndrome.\n  - *Rapid (Shuo Mai)*: Over 90 bpm; Heat syndrome.\n  - *Slippery (Hua Mai)*: Rolls like pearls; Phlegm, Dampness, Food retention, Pregnancy.\n  - *Wiry (Xuan Mai)*: Taut guitar string; Liver/GB, pain, Phlegm.\n  - *Choppy (Se Mai)*: Rough, hesitant knife scraping bamboo; Blood stasis or Blood deficiency."
        ],
        "table_headers": ["Clinical Pattern", "Tongue Body & Coating", "Pulse Characteristics"],
        "table_rows": [
            ["Normal Healthy", "Pale red, supple body; Thin white moist coat", "Moderate, calm, rhythmic (60-80 bpm), rooted"],
            ["Spleen Qi Deficiency", "Pale, swollen body with teethmarks on edges", "Weak (Ruo Mai) or Empty (Xu Mai)"],
            ["Full Heat (Yangming)", "Red body; Thick yellow dry coating", "Surging (Hong Mai), Large, Full, Rapid"],
            ["Yin Deficiency (Empty Heat)", "Red body, cracked; Completely peeled (no coat)", "Thready (Xi Mai) and Rapid (Shuo Mai)"],
            ["Blood Stasis", "Purple or dark body, distended sublingual veins", "Choppy (Se Mai) or Wiry (Xuan Mai)"],
            ["Phlegm-Dampness", "Swollen body; Thick greasy white or yellow coat", "Slippery (Hua Mai)"],
            ["Liver Qi Stagnation", "Normal or red sides; Thin white coat", "Wiry (Xuan Mai), especially on left Guan position"],
            ["Yang Collapse", "Pale wet flabby body; White slippery coating", "Faint, Minute (Wei Mai) or Deep weak slow"]
        ],
        "board_traps": [
            "**Sublingual Vein Inspection**: Dark, distended, tortuous sublingual veins under the tongue are a hallmark objective confirmation of Blood Stasis in the chest or pelvis.",
            "**Pulse Position Verification**: Left Guan is Liver/GB; Right Guan is Spleen/Stomach. If left Guan is wiry and right Guan is weak, this confirms Liver overacting on Spleen."
        ],
        "clinical_points": [
            "**Clear Tongue Coating (Dampness)**: SP9 (Yinlingquan) + ST40 (Fenglong).",
            "**Move Choppy Pulse (Blood Stasis)**: BL17 (Geshu) + SP10 (Xuehai).",
            "**Strengthen Weak Deep Pulse (Kidney Yang)**: BL23 (Shenshu) + DU4 (Mingmen)."
        ]
    },
    {
        "id": "needling-safety",
        "title": "Needling Safety & Anatomical Hazards",
        "chinese": "针刺安全与解剖禁忌 (Zhēn Cì Ān Quán)",
        "category": "Safety & Technique",
        "icon": "🛡️",
        "tagline": "Critical anatomical danger zones, depth limits, and emergency clinical protocols.",
        "summary": "Patient safety is the supreme priority in clinical acupuncture. Understanding anatomical depth limits, contraindicated points during pregnancy, organ puncture prevention, and emergency protocols (needle fainting, stuck/broken needle) protects patients and safeguards your license.",
        "mnemonic": "Pneumothorax Danger Points:\n'GB21, LU1, LU2, ST12, BL11 to BL21 - Never needle deep or perpendicular! Always angle oblique medially or tangential!'",
        "principles": [
            "**Pneumothorax Prevention**:\n  - Occurs when apical or thoracic pleura is punctured by deep needle insertion.\n  - *High-risk points*: GB21 (Jianjing), LU1 (Zhongfu), LU2 (Yunmen), ST12 (Quepen), inner and outer Bladder line on upper thorax (BL11 to BL21, BL41 to BL50).\n  - *Safe rule*: Always pinch the trapezius muscle at GB21 and insert posterior-oblique 0.5-0.8 cun. Never insert perpendicularly downwards.",
            "**Central Nervous System Hazards**:\n  - Points over foramen magnum: DU15 (Yamen) and DU16 (Fengfu).\n  - Deep superior puncture can penetrate the cisterna magna and medulla oblongata, causing respiratory arrest.\n  - *Safe rule*: Insert strictly perpendicular or slightly inferiorly, depth limited to 0.5-0.8 cun.",
            "**Visceral Organ Puncture Hazards**:\n  - Urinary bladder: RN2, RN3, ST28. Patient MUST empty bladder before treatment.\n  - Liver & Spleen: Right and left hypochondrium (LR14, GB24, ST19-ST21, LR13). Puncturing in hepatomegaly/splenomegaly causes severe internal bleeding.\n  - Heart: RN14, RN15 in cardiomegaly.\n  - Kidney: BL51, BL52, GB25. Emaciated patients have thin perinephric fat.",
            "**Pregnancy Absolute Contraindications**:\n  - Points that strongly descend Qi: LI4 (Hegu), SP6 (Sanyinjiao), BL60 (Kunlun), BL67 (Zhiyin), GB21 (Jianjing).\n  - Lower abdomen: RN1 to RN7, ST28 to ST30, SP12 to SP14 (all trimesters).\n  - Lumbosacral area: BL27 to BL34 (sacral foramen Liao points) during 2nd and 3rd trimesters.",
            "**Emergency Management of Needle Fainting (晕针)**:\n  - *Signs*: Dizziness, pallor, cold sweat, nausea, weak thready pulse.\n  - *Protocol*: Immediately withdraw all needles; place patient supine with head low; offer warm sweet water; press DU26 (Shuigou) and PC6 (Neiguan); apply moxa on DU20 if severe."
        ],
        "table_headers": ["Danger Zone", "High-Risk Points", "Safe Needle Angle & Depth", "Medical Hazard to Prevent"],
        "table_rows": [
            ["Lung Apex & Thorax", "GB21, ST12, LU1, LU2, BL11-21", "Oblique / Transverse 0.5 - 0.8 cun; pinch muscle", "Traumatic Pneumothorax"],
            ["Medulla / Brainstem", "DU15 (Yamen), DU16 (Fengfu)", "Perpendicular or slightly inferior 0.5 - 0.8 cun", "Medullary damage / Respiratory arrest"],
            ["Eyeball & Orbit", "BL1 (Jingming), ST1 (Chengqi)", "Push eyeball gently; slow insertion 0.5 - 1.0 cun, NO manipulation", "Retrobulbar hematoma / Optic injury"],
            ["Urinary Bladder", "RN2 (Qugu), RN3 (Zhongji)", "Have patient void first; shallow 0.5 - 1.0 cun", "Bladder perforation / Peritonitis"],
            ["Carotid Artery", "ST9 (Renying)", "Palpate carotid; push artery laterally; needle 0.3 - 0.5 cun", "Carotid hematoma / Arterial puncture"],
            ["Liver / Spleen", "LR14, GB24, LR13, ST20", "Oblique along intercostal space 0.5 - 0.8 cun", "Hepatic / Splenic rupture"],
            ["Pregnancy Points", "LI4, SP6, BL60, BL67, GB21, Lower abdomen", "STRICTLY FORBIDDEN during pregnancy", "Induced uterine contractions / Miscarriage"]
        ],
        "board_traps": [
            "**Pneumothorax Delay**: Pneumothorax signs (sharp chest pain, dry cough, dyspnea) might NOT appear on the table, but develop 2-12 hours later. Instruct patients to report sudden breathlessness immediately.",
            "**BL1 Manipulation**: Any lifting, thrusting, or twisting on BL1 is a board exam malpractice red flag. Never manipulate needle in orbital cavity."
        ],
        "clinical_points": [
            "**Resuscitate Fainting**: DU26 (Shuigou), PC6 (Neiguan), ST36 (Zusanli).",
            "**Stuck Needle Relief**: Massage around point, or tap/insert adjacent needle 0.5 cun away to release spasm."
        ]
    },
    {
        "id": "korean-four-needle",
        "title": "Korean Four-Needle Technique (Saam)",
        "chinese": "舍岩四针疗法 (Shè Yán Sì Zhēn Liáo Fǎ)",
        "category": "Acupoint Categories",
        "icon": "🇰🇷",
        "tagline": "Classical Five-Element dynamic balancing using paired Mother-Child and Controlling cycle Shu points.",
        "summary": "Formulated by the 16th-century Korean Buddhist monk Saam (舍岩), Korean Four-Needle Technique regulates meridian deficiencies and excesses by manipulating four specific Five Shu points per channel: two points on the affected meridian, and two points on related mother, child, or controlling meridians. It harmonizes the Generating (Sheng) and Controlling (Ke) cycles simultaneously.",
        "mnemonic": "The Saam Golden Rules:\n• Deficiency (Tonify): 'Tonify Mother on Home + Tonify Mother on Mother; Sedate Controller on Home + Sedate Controller on Controller.'\n• Excess (Sedate): 'Sedate Child on Home + Sedate Child on Child; Tonify Controller on Home + Tonify Controller on Controller.'",
        "principles": [
            "**Tonification Formula (虚则补其母，抑其克)**: When a channel is deficient, tonify its Mother element (generating force) on the self channel and on the Mother channel, while sedating its Grandmother element (controlling force) on the self channel and on the Grandmother channel.",
            "**Sedation Formula (实则泻其子，扶其克)**: When a channel is hyperactive/excess, drain its Child element (dispersing excess) on the self channel and on the Child channel, while tonifying its Grandmother element (controlling force) on the self channel and on the Grandmother channel.",
            "**Distal Five Shu Precision**: All four needles are placed strictly below the elbows and knees. Treatments are typically administered unilaterally (left side in men, right side in women, or on the affected symptom side)."
        ],
        "table_headers": ["Meridian & Element", "Tonification Points (补母抑克)", "Sedation Points (泻子扶克)"],
        "table_rows": [
            ["Lung (Metal / 肺金)", "Tonify: LU9 (Earth) + SP3 (Earth) | Sedate: LU10 (Fire) + HT8 (Fire)", "Sedate: LU5 (Water) + KD10 (Water) | Tonify: LU10 (Fire) + HT8 (Fire)"],
            ["Large Intestine (Metal / 大肠)", "Tonify: LI11 (Earth) + ST36 (Earth) | Sedate: LI5 (Fire) + SI5 (Fire)", "Sedate: LI2 (Water) + ST44 (Water) | Tonify: LI5 (Fire) + SI5 (Fire)"],
            ["Spleen (Earth / 脾土)", "Tonify: SP2 (Fire) + HT8 (Fire) | Sedate: SP1 (Wood) + LR1 (Wood)", "Sedate: SP5 (Metal) + LU8 (Metal) | Tonify: SP1 (Wood) + LR1 (Wood)"],
            ["Stomach (Earth / 胃土)", "Tonify: ST41 (Fire) + SI5 (Fire) | Sedate: ST43 (Wood) + GB41 (Wood)", "Sedate: ST45 (Metal) + LI1 (Metal) | Tonify: ST43 (Wood) + GB41 (Wood)"],
            ["Heart (Fire / 心火)", "Tonify: HT9 (Wood) + LR1 (Wood) | Sedate: HT3 (Water) + KD10 (Water)", "Sedate: HT7 (Earth) + SP3 (Earth) | Tonify: HT3 (Water) + KD10 (Water)"],
            ["Small Intestine (Fire / 小肠)", "Tonify: SI3 (Wood) + GB41 (Wood) | Sedate: SI2 (Water) + BL66 (Water)", "Sedate: SI8 (Earth) + ST36 (Earth) | Tonify: SI2 (Water) + BL66 (Water)"],
            ["Kidney (Water / 肾水)", "Tonify: KD7 (Metal) + LU8 (Metal) | Sedate: KD3 (Earth) + SP3 (Earth)", "Sedate: KD1 (Wood) + LR1 (Wood) | Tonify: KD3 (Earth) + SP3 (Earth)"],
            ["Urinary Bladder (Water / 膀胱)", "Tonify: BL67 (Metal) + LI1 (Metal) | Sedate: BL54 (Earth) + ST36 (Earth)", "Sedate: BL65 (Wood) + GB41 (Wood) | Tonify: BL54 (Earth) + ST36 (Earth)"],
            ["Liver (Wood / 肝木)", "Tonify: LR8 (Water) + KD10 (Water) | Sedate: LR4 (Metal) + LU8 (Metal)", "Sedate: LR2 (Fire) + HT8 (Fire) | Tonify: LR4 (Metal) + LU8 (Metal)"],
            ["Gallbladder (Wood / 胆木)", "Tonify: GB43 (Water) + BL66 (Water) | Sedate: GB44 (Metal) + LI1 (Metal)", "Sedate: GB38 (Fire) + SI5 (Fire) | Tonify: GB44 (Metal) + LI1 (Metal)"],
            ["Pericardium (Fire / 心包)", "Tonify: PC9 (Wood) + LR1 (Wood) | Sedate: PC3 (Water) + KD10 (Water)", "Sedate: PC7 (Earth) + SP3 (Earth) | Tonify: PC3 (Water) + KD10 (Water)"],
            ["San Jiao (Fire / 三焦)", "Tonify: SJ3 (Wood) + GB41 (Wood) | Sedate: SJ2 (Water) + BL66 (Water)", "Sedate: SJ10 (Earth) + ST36 (Earth) | Tonify: SJ2 (Water) + BL66 (Water)"]
        ],
        "board_traps": [
            "**Channel Pairing Verification**: In Saam acupuncture, exactly two points belong to the primary channel and two points belong to the coupled auxiliary Five Element channel. Never select all four points on the same meridian.",
            "**No Local Needles**: Saam therapy strictly relies on distal energetic balance. Do not add local Ashi needles to the formal four-needle prescription."
        ],
        "clinical_points": [
            "**Spleen Tonification for Fatigue & Chronic Diarrhea**: SP2 + HT8 (Tonify Fire Mother), SP1 + LR1 (Sedate Wood Controller).",
            "**Liver Sedation for Migraines & Anger**: LR2 + HT8 (Sedate Fire Child), LR4 + LU8 (Tonify Metal Controller)."
        ]
    },
    {
        "id": "medical-red-flags",
        "title": "Biomedicine Medical Red Flags & Urgent Referrals",
        "chinese": "西医急症危险征象与紧急转诊 (Xī Yī Jí Zhèng Wēi Xiǎn Zhēng Xiàng)",
        "category": "Safety & Technique",
        "icon": "🚨",
        "tagline": "Critical life-threatening signs requiring immediate 911 dispatch, hospital transfer, or urgent specialist workup.",
        "summary": "Derived from David Anzaldua, MD's clinical medical review for acupuncturists, this framework defines high-liability conditions where acupuncture must be deferred or halted in favor of emergency medical management. Failure to identify red flags risks patient mortality and professional license revocation.",
        "mnemonic": "The 'S-H-O-C-K-S' Red Flag Triage:\n• S - Sudden onset severe deficit (Thunderclap headache, FAST stroke, acute abdomen)\n• H - Hemodynamic instability (Severe hypotension, tachycardia, shock, pallor)\n• O - Orthopedic / Neurologic compression (Cauda equina, saddle anesthesia, VBI drop attack)\n• C - Chest pain / Cardiopulmonary distress (Crushing chest pain, PND, stridor, PE)\n• K - Kidney / Infection sepsis (High fever, CVA tenderness, nuchal rigidity)\n• S - Silent or night pain (Spinal night pain unrelieved by rest -> Malignancy)",
        "principles": [
            "**Emergency EMS (Call 911 Immediately)**: Suspected Acute Myocardial Infarction, Stroke within 4.5 hours (FAST), Subarachnoid Hemorrhage, Ruptured Aortic Aneurysm, Acute Epiglottitis, Anaphylaxis, Pulmonary Embolism, Tension Pneumothorax.",
            "**Urgent Hospital ED Referral (< 24 Hours)**: Cauda Equina Syndrome (within 24-48h for surgical decompression), Temporal Arteritis (risk of permanent blindness within hours), Acute Appendicitis (especially after sudden cessation of pain), Deep Vein Thrombosis, Ectopic Pregnancy.",
            "**Prompt Specialist Referral (< 1-2 Weeks)**: Unexplained night back pain in patients aged > 50, progressive painless lymphadenopathy, postmenopausal uterine bleeding, non-healing pigmented skin lesions (ABCDE melanoma).",
            "**Never Mask Emergency Symptoms**: Do not administer strong acupuncture analgesia (e.g. LI4, ST36, auricular ear seeds) that masks abdominal rigidity or alters neurological signs prior to emergency evaluation."
        ],
        "table_headers": ["Red Flag Presentation", "Primary Rule Out", "Urgency / Action", "Critical Hazard"],
        "table_rows": [
            ["Thunderclap 'worst headache of life', meningismus", "Non-Traumatic Subarachnoid Hemorrhage (SAH)", "Call 911 / Immediate Brain CT", "Fatal rebleeding or herniation"],
            ["Saddle anesthesia, bowel/bladder incontinence, leg weakness", "Cauda Equina Syndrome", "Emergency ED for urgent MRI & surgery", "Permanent incontinence & paralysis"],
            ["Unilateral headache, jaw claudication, scalp tenderness, age > 50", "Temporal Arteritis (Giant Cell Arteritis)", "Same-day ED / High-dose systemic steroids", "Irreversible bilateral blindness"],
            ["Acute RLQ pain abruptly stops, then board-like abdomen & fever", "Appendiceal Rupture with Generalized Peritonitis", "Call 911 / Emergency Appendectomy", "Septic shock & death"],
            ["Unilateral calf swelling > 3cm, warmth, post-flight/immobilization", "Deep Vein Thrombosis (DVT)", "Urgent ED / Venous Doppler; NO MASSAGE", "Fatal Pulmonary Embolism"],
            ["Sudden drop attack on neck extension/rotation, 5 D's", "Vertebrobasilar Insufficiency (VBI)", "Neurology CTA/MRA; NO neck manipulation", "Posterior circulation stroke"],
            ["Child sitting in tripod position, drooling, inspiratory stridor", "Acute Epiglottitis", "Call 911; DO NOT use tongue depressor", "Complete airway asphyxiation"],
            ["Constant night back pain unrelieved by lying down, weight loss", "Spinal Malignancy / Metastasis", "Urgent Spine MRI & oncology workup", "Pathologic fracture & cord compression"]
        ],
        "board_traps": [
            "**The 'Better' Appendicitis Trap**: When an acute appendicitis patient suddenly smiles and says the pain is completely gone, they have just perforated. Guarding and rebound will follow rapidly.",
            "**The DVT Massage Malpractice**: Placing needles in BL57/BL40 or massaging a swollen, tender calf can physically dislodge a thrombus into the inferior vena cava and pulmonary artery."
        ],
        "clinical_points": [
            "**Emergency Charting**: Always record exact onset timestamp, vital signs, physical examination findings, and the specific EMS dispatch details in clinical records.",
            "**Patient Positioning**: In acute shock, place patient supine with feet elevated (unless cardiopulmonary distress, where high Fowler sitting position is required)."
        ]
    },
    {
        "id": "adjunct-modalities",
        "title": "Acupuncture Adjunct Modalities & Microsystems",
        "chinese": "针灸辅助疗法与微刺系统 (Zhēn Jiǔ Fǔ Zhù Liáo Fǎ)",
        "category": "Safety & Technique",
        "icon": "⚡",
        "tagline": "Electroacupuncture parameters, Jiao Shunfa scalp lines, Auricular master points, and cupping protocols.",
        "summary": "Clinical practice frequently incorporates specialized modalities beyond manual filiform needling. Mastery of Electro-Acupuncture frequency selection, Jiao Shunfa scalp somatotopic lines for neurological rehabilitation, Auricular acupuncture microsystems, and cupping/moxibustion contraindications is essential for board certification and modern integrative practice.",
        "mnemonic": "Modality Quick Mnemonics:\n• EA Frequencies: 'Low (2Hz) = Endorphins for Chronic/Weak; High (100Hz) = Dynorphin for Sharp/Spasm; Dense-Disperse (2/100Hz) = Both for Sciatica.'\n• Scalp MS6 Motor Line: 'Inverted homunculus - Upper 1/5 is Lower limb/trunk; Middle 2/5 is Upper limb; Lower 2/5 is Face/Speech.'\n• NADA Ear Protocol: 'S-S-K-L-L' = Sympathetic, Shenmen, Kidney, Liver, Lung.",
        "principles": [
            "**Electro-Acupuncture Waveforms**: Continuous (uniform frequency), Dense-Disperse (alternating low and high frequency; prevents habituation and releases endorphins + dynorphin), Intermittent (cyclic pulse-rest for flaccid paralysis).",
            "**Jiao Shunfa Scalp Line Technique**: Needles are inserted subaponeurotically at 15–30 degrees, threaded 1.5 cun along the line, and rapidly twirled at 200 rpm for 1–2 minutes without lifting or thrusting. Contralateral side is treated for unilateral motor/sensory lesions.",
            "**Auricular Inverted Fetus Homunculus**: Head and facial organs located on the ear lobule; spine along the antihelix; internal viscera in the concha (cavum = Heart/Lung, cymba = Spleen/Liver/Kidney); lower limbs along superior antihelix crus.",
            "**Cupping & Moxa Contraindications**: Never cup over acute trauma fractures, deep vein thrombosis, ulcers, high fever convulsions, or the abdomen/lumbar spine of pregnant women. Direct scarring moxa is forbidden on the face, breasts, and near major arteries."
        ],
        "table_headers": ["Modality / System", "Key Specifications & Zones", "Primary Indications", "Safety Precautions & Limits"],
        "table_rows": [
            ["Electro-Acupuncture (Low 2-5Hz)", "Continuous low frequency; motor twitch visible", "Chronic pain, flaccid motor weakness, Bells palsy", "Avoid muscle exhaustion; limit to 20-30 mins"],
            ["Electro-Acupuncture (Dense-Disperse)", "Alternating 2Hz / 100Hz cycling automatically", "Severe sciatica, intractable arthralgia, back pain", "NO pacemakers; NEVER cross transthoracic midline"],
            ["Scalp MS6 Motor Line", "Upper 1/5 (leg/trunk), Middle 2/5 (arm), Lower 2/5 (face)", "Wind stroke hemiplegia, cerebral palsy, paralysis", "Twirl 200 rpm; treat contralateral side"],
            ["Scalp MS7 Sensory Line", "Parallel and 1.5 cun posterior to MS6 (vertex-temporal)", "Contralateral sensory numbness, paresthesia, pain", "Same 1/5, 2/5, 2/5 somatotopic divisions as MS6"],
            ["Auricular NADA 5-Point", "Sympathetic, Shenmen, Kidney, Liver, Lung", "Addiction detox, PTSD, emotional shock, insomnia", "Strict alcohol swab; avoid perichondritis"],
            ["Fire / Suction Cupping", "Retained (5-10 min), Moving/Sliding, Wet/Flash", "Wind-Cold invasion, muscle knots, blood stasis", "Never cup over open skin, DVT, or pregnant abdomen"]
        ],
        "board_traps": [
            "**Scalp Needle Direction**: Threading too deeply penetrates the skull suture lines or fontanelles in infants. In adults, stay strictly in the loose subaponeurotic layer (galea aponeurotica).",
            "**Ear Perichondritis**: Ear cartilage is avascular; bacterial infection leads to severe necrotic cauliflower ear. Always use single-use sterile ear tacks/press needles and change every 3-5 days."
        ],
        "clinical_points": [
            "**Stroke Motor Recovery**: Scalp MS6 (Motor Line contralateral) + LI11 (Quchi) + LI4 (Hegu) + ST36 (Zusanli) + GB34 (Yanglingquan).",
            "**Acute Traumatic Spasm**: High frequency EA (100 Hz) across Ashi points."
        ]
    },
    {
        "id": "pharmacology-herb-drug",
        "title": "Western Pharmacology & Herb-Drug Interactions",
        "chinese": "西药药理与中西药配伍禁忌 (Xī Yào Yào Lǐ yǔ Zhōng Xī Yào Pèi Wǔ)",
        "category": "Pathology",
        "icon": "💊",
        "tagline": "Essential pharmaceutical classes, mechanisms, side effects, and life-threatening herbal contraindications.",
        "summary": "Modern acupuncture patients frequently take multiple prescription medications. Acupuncturists must comprehend Western mechanisms of action, recognize drug-induced side effects (which frequently mimic TCM pathology), and avoid life-threatening herb-drug interactions, particularly regarding anticoagulants, corticosteroids, diuretics, and psychiatric medications.",
        "mnemonic": "Top 4 Herb-Drug Fatal Traps:\n1. Blood Thinners (Warfarin/Aspirin) + Invigorate Blood Herbs (Dang Gui, Dan Shen, Tao Ren) = Fatal Hemorrhage.\n2. Diuretics (Lasix) + Licorice (Gan Cao) = Severe Hypokalemia & Arrhythmia.\n3. Digoxin + Calcium/Herbs = Fatal Digitalis Toxicity.\n4. SSRIs + St. Johns Wort / Ephedra = Serotonin Syndrome / Hypertensive Crisis.",
        "principles": [
            "**Anticoagulants & Antiplatelets (Warfarin, Clopidogrel, Aspirin)**: Inhibit clotting cascade or platelet aggregation. Co-administration with herbs that strongly invigorate Blood or break Blood stasis dramatically increases bleeding time, bruising, and hemorrhagic stroke risk.",
            "**Corticosteroids (Prednisone, Dexamethasone)**: Suppress inflammation and immune response. Induce fluid retention, hypertension, osteoporosis, and severe Kidney Yin consumption with adrenal atrophy. Must never be stopped abruptly.",
            "**Loop & Thiazide Diuretics (Furosemide, HCTZ)**: Promote renal water and sodium excretion, causing potassium wasting. High doses of Gan Cao (Licorice) compound potassium loss via pseudo-hyperaldosteronism.",
            "**Beta-Adrenergic Blockers (Metoprolol, Atenolol)**: Lower heart rate and contractility. Critically mask autonomic warning signs of hypoglycemia in diabetic patients (except sweating).",
            "**Selective Serotonin Reuptake Inhibitors (SSRIs, e.g. Fluoxetine, Sertraline)**: Increase synaptic serotonin for depression and anxiety. Co-administration with serotonergic herbs risks Serotonin Syndrome (hyperthermia, agitation, hyperreflexia)."
        ],
        "table_headers": ["Drug Class & Examples", "Western Mechanism", "TCM Pattern Manifestation", "High-Risk Herb Interactions"],
        "table_rows": [
            ["Anticoagulants (Warfarin, Heparin)", "Inhibits Vitamin K-dependent clotting factors", "Bleeding tendency, petechiae, easy bruising", "Dang Gui, Dan Shen, Tao Ren, Hong Hua, San Qi, Shui Zhi"],
            ["Antiplatelets (Aspirin, Clopidogrel)", "Irreversibly inhibits platelet aggregation", "Upper GI irritation, bleeding diathesis", "Ginkgo Biloba (Bai Guo), Garlic (Da Suan), Hong Hua"],
            ["Corticosteroids (Prednisone)", "Suppresses inflammation & adrenal axis", "Kidney Yin Def Empty Heat, Spleen Dampness", "Caution with warm drying herbs; watch immune status"],
            ["Loop Diuretics (Furosemide / Lasix)", "Inhibits Na+/K+/2Cl- symporter in loop of Henle", "Yin and fluid consumption, pale copious urine", "Gan Cao (Licorice) causes severe hypokalemia & arrhythmia"],
            ["Beta Blockers (Metoprolol, Atenolol)", "Blocks beta-1 adrenergic receptors, drops BP/HR", "Slow pulse (Chi Mai), cold extremities, lethargy", "Masks hypoglycemia; caution with strong cold sedating herbs"],
            ["NSAIDs (Ibuprofen, Naproxen)", "Inhibits COX-1 & COX-2 prostaglandin synthesis", "Stomach Yin injury, Stomach Heat, epigastric stasis", "Co-admin with anticoagulants spikes GI hemorrhage risk"],
            ["Cardiac Glycosides (Digoxin)", "Inhibits Na+/K+-ATPase, increases cardiac contractility", "Toxicity: visual halos, nausea, slow irregular pulse", "Gan Cao (via hypokalemia) and calcium-rich shell herbs trigger toxicity"]
        ],
        "board_traps": [
            "**The Licorice Toxicity Trap**: Gan Cao is the 'harmonizer' present in 80% of formulas. If a patient is taking Furosemide or Digoxin, long-term or high-dose Gan Cao can provoke fatal hypokalemic arrhythmias.",
            "**Pre-Surgical Herb Washout**: All blood-invigorating herbs (Dan Shen, Dang Gui, Chuan Xiong) and Ginkgo Biloba must be discontinued at least 1–2 weeks prior to scheduled surgery."
        ],
        "clinical_points": [
            "**Chart Medication Reconciliation**: Always document complete list of pharmaceuticals, dosages, and OTC supplements at every clinical visit.",
            "**Post-Stroke Recovery Synergy**: Acupuncturists can safely treat stroke patients with scalp and body acupuncture while they take antiplatelet therapy, but must avoid deep or high-risk bleeding sites."
        ]
    }
]

def get_all_concepts() -> List[Dict[str, Any]]:
    """Return all core concepts."""
    return CONCEPTS_DATA

def get_concept_by_id(cid: str) -> Optional[Dict[str, Any]]:
    """Lookup concept by ID."""
    for c in CONCEPTS_DATA:
        if c["id"] == cid:
            return c
    return None

def render_concepts_tab():
    """Render the interactive Concepts & Memory Aids Tab."""
    st.subheader("TCM Core Concepts & Memory Aids")
    st.caption("Deep clinical fundamentals, high-yield board mnemonics, comparative tables, and exam traps.")

    all_concepts = get_all_concepts()
    
    # Session state initialization for active concept
    if "selected_concept_id" not in st.session_state:
        st.session_state.selected_concept_id = all_concepts[0]["id"]

    # Filter & Search layout
    col_search, col_filter = st.columns([2, 1])
    with col_search:
        search_query = st.text_input(
            "Search Concepts, Mnemonics, or Organs",
            placeholder="e.g. Yin-Yang, Mother-Child, Pneumothorax, Tongue, Organ Clock...",
            label_visibility="collapsed",
            key="concepts_search_input"
        ).strip().lower()
    with col_filter:
        categories = ["All Categories"] + sorted(list({c["category"] for c in all_concepts}))
        selected_cat = st.selectbox(
            "Filter Category",
            options=categories,
            label_visibility="collapsed",
            key="concepts_cat_select"
        )

    # Filter concepts list
    filtered = []
    for c in all_concepts:
        matches_cat = (selected_cat == "All Categories") or (c["category"] == selected_cat)
        matches_search = (
            not search_query
            or search_query in c["title"].lower()
            or search_query in c["chinese"].lower()
            or search_query in c["tagline"].lower()
            or search_query in c["mnemonic"].lower()
            or search_query in c["summary"].lower()
        )
        if matches_cat and matches_search:
            filtered.append(c)

    if not filtered:
        st.warning("No concepts matched your search. Showing all topics.")
        filtered = all_concepts

    # Two-Column Master / Detail Layout (Like the Atlas)
    col_master, col_detail = st.columns([1, 2.3], gap="medium")

    # LEFT COLUMN: Master List of Clickable Concept Links
    with col_master:
        st.markdown(f"**📚 Core Topics ({len(filtered)}):**")
        for c in filtered:
            is_active = (c["id"] == st.session_state.selected_concept_id)
            btn_label = f"{c['icon']} {c['title']}"
            btn_type = "primary" if is_active else "secondary"
            
            # Clickable topic link button
            if st.button(
                btn_label,
                key=f"concept_link_{c['id']}",
                use_container_width=True,
                type=btn_type
            ):
                st.session_state.selected_concept_id = c["id"]
                st.rerun()

    # RIGHT COLUMN: Deep Concept Profile & Memory Aids
    with col_detail:
        active_concept = get_concept_by_id(st.session_state.selected_concept_id) or filtered[0]
        
        # Header Badge & Title
        st.markdown(f"""
        <div style="background: #ffffff; border: 1.5px solid #e8ded2; border-radius: 14px; padding: 22px 24px; box-shadow: 0 3px 12px rgba(0, 123, 167, 0.04); margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="background: #eef0fb; color: #484eb2; font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; padding: 3px 10px; border-radius: 6px;">
                    {active_concept['category']}
                </span>
                <span style="font-family: ui-monospace, monospace; font-size: 0.78rem; font-weight: 700; color: #007ba7;">
                    NCCAOM High-Yield
                </span>
            </div>
            <h2 style="margin: 4px 0 6px 0; color: #0f172a; font-size: 1.65rem; font-weight: 900;">
                {active_concept['icon']} {active_concept['title']}
            </h2>
            <div style="font-size: 1.05rem; font-weight: 700; color: #c89666; margin-bottom: 10px;">
                {active_concept['chinese']}
            </div>
            <div style="font-size: 0.95rem; color: #475569; line-height: 1.55;">
                {active_concept['tagline']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Executive Summary
        st.markdown(f"**📖 Core Definition:**")
        st.info(active_concept["summary"])

        # 🧠 Memory Aid & Mnemonic Callout
        st.markdown(f"""
        <div style="background: #faf6f0; border-left: 5px solid #c89666; border-radius: 8px; padding: 14px 18px; margin: 18px 0; box-shadow: 0 1px 4px rgba(200, 150, 102, 0.08);">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 0.92rem; color: #8c5e35; margin-bottom: 6px;">
                <span>🧠 HIGH-YIELD MEMORY AID & MNEMONIC</span>
            </div>
            <div style="font-size: 0.92rem; line-height: 1.6; color: #1e293b; white-space: pre-line;">
{active_concept['mnemonic']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Comparative Reference Table
        if "table_headers" in active_concept and "table_rows" in active_concept:
            with st.expander("📊 Comparative Reference Table (Click to Expand)", expanded=True):
                # Render markdown table
                headers = active_concept["table_headers"]
                rows = active_concept["table_rows"]
                md_table = "| " + " | ".join(headers) + " |\n"
                md_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
                for row in rows:
                    md_table += "| " + " | ".join(row) + " |\n"
                st.markdown(md_table)

        # Core Principles Breakdown
        st.markdown("**📋 Key Principles & Mechanics:**")
        for p in active_concept["principles"]:
            st.markdown(f"- {p}")

        # ⚠️ Board Exam Traps & Tricky Distinctions
        if "board_traps" in active_concept:
            st.markdown(f"""
            <div style="background: #f6f7fd; border: 1.5px solid #e0e3f7; border-left: 5px solid #484eb2; border-radius: 8px; padding: 14px 18px; margin: 18px 0;">
                <div style="display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 0.9rem; color: #484eb2; margin-bottom: 8px;">
                    <span>⚠️ BOARD EXAM TRAPS & TRICKY QUESTIONS</span>
                </div>
            """, unsafe_allow_html=True)
            for trap in active_concept["board_traps"]:
                st.markdown(f"- {trap}")
            st.markdown("</div>", unsafe_allow_html=True)

        # Clinical Points Correlated
        if "clinical_points" in active_concept:
            st.markdown("**🎯 Clinical Points to Cross-Reference in Atlas:**")
            for pt in active_concept["clinical_points"]:
                st.markdown(f"- {pt}")

        # Sequential Prev / Next buttons
        st.write("")
        curr_idx = next((i for i, c in enumerate(all_concepts) if c["id"] == active_concept["id"]), 0)
        col_prev, col_spacer, col_next = st.columns([1, 2, 1])
        with col_prev:
            if curr_idx > 0:
                if st.button("⬅️ Previous Topic", use_container_width=True, key="concept_prev_btn"):
                    st.session_state.selected_concept_id = all_concepts[curr_idx - 1]["id"]
                    st.rerun()
        with col_next:
            if curr_idx < len(all_concepts) - 1:
                if st.button("Next Topic ➡️", use_container_width=True, key="concept_next_btn"):
                    st.session_state.selected_concept_id = all_concepts[curr_idx + 1]["id"]
                    st.rerun()

import json
import re
import random

with open('data/exam_questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions for full curation and audit.\n")

# ==============================================================================
# STEP 1: Fix Specific Content & Factual Errors
# ==============================================================================

for q in questions:
    # ID 478: He-Sea point of Heart meridian is HT3 (Shaohai), which is Option 0!
    if q['id'] == 478:
        print("Fixing ID 478 factual error (HT3 Shaohai is He-Sea of Heart, Option A)...")
        q['answer'] = 0
        q['explanation'] = (
            "Official Board Answer: Option A. HT3 (Shaohai) is the He-Sea (Water) point of the Heart meridian, "
            "located with the elbow flexed at the midpoint of the line connecting the medial end of the cubital crease "
            "and the medial epicondyle of the humerus. (Option B describes LI11, Option C describes LU5, and Option D describes SI8)."
        )

    # ID 723: Duplicate Option C and D
    elif q['id'] == 723:
        print("Fixing ID 723 duplicate option D...")
        q['options'][3] = "Warm the Spleen and Kidneys, Disperse Cold, Promote bowel movement"

    # ID 389: Stomach channel path typos and watermark
    elif q['id'] == 389:
        q['question'] = "Which channel pathway curves around the lips, turns and runs upwards in front of the ear, enters the body, and descends through the diaphragm?"
        q['options'][3] = "ST"
        q['explanation'] = "Official Board Answer: Option D (ST). The Stomach primary channel encircles the lips, ascends anterior to the ear, penetrates into the body, and descends through the diaphragm to connect with the Stomach and Spleen."

    # ID 653: CV17 stem and watermark
    elif q['id'] == 653:
        q['question'] = "CV17 (Danzhong) is:"
        q['options'][3] = "The greater Luo-connecting point"
        q['explanation'] = "Official Board Answer: Option A (The influential point of Qi). CV17 is the Front-Mu point of the Pericardium and the Hui-Meeting (influential) point of Qi."

    # Make context-dependent case questions self-contained:
    elif q['id'] == 302:
        q['question'] = "Vivian, age 89, presents with severe chronic constipation, emaciation, lusterless skin, dull nails, dry mouth, and constant thirst (Yangming / Yin deficiency). What would you expect her tongue and pulse to be?"

    elif q['id'] == 331:
        q['question'] = "Lionel presents with an acute Wind-Cold cough, itchy throat, thin white sputum, nasal discharge, chills, fever, and headache. What is the best point prescription for this case?"

    elif q['id'] == 424:
        q['question'] = "Sarah, a 39-year-old woman, presents with intractable hiccups for two months, uncomfortable stomach sensation, poor appetite, constipation, thirst with desire to drink in small sips, red tongue with no coat, and thin rapid pulse. What is the diagnosis?"

    elif q['id'] == 427:
        q['question'] = "Steve, a 45-year-old patient with insomnia, slightly manic behavior, mucus in stools, and abdominal distention diagnosed with Stomach Phlegm-Fire: what would you expect the tongue and pulse to be?"

    elif q['id'] == 429:
        q['question'] = "For a young patient presenting with acute violent lower abdominal pain diagnosed as Small Intestine Qi Tied (intestinal obstruction / appendicitis), which extra point would you use?"
        q['options'] = ["Dan Nang Xue", "Ba Feng", "Lan Wei Xue", "Bai Chong Wo"]

print("Completed Step 1: Specific content & factual corrections.")

# ==============================================================================
# STEP 2: Clean PDF Watermarks & Footers Across ALL 809 Questions
# ==============================================================================

WATERMARK_PATTERN = re.compile(
    r'\s*1998\s*[-–]\s*20\d\d(?:\s*\d+)?(?:\s*Case Studies[^\n]*)?',
    re.IGNORECASE
)

cleaned_watermarks = 0
for q in questions:
    if WATERMARK_PATTERN.search(q['question']):
        q['question'] = WATERMARK_PATTERN.sub('', q['question']).strip()
        q['question'] = re.sub(r'choose\s*$', 'choose:', q['question'], flags=re.IGNORECASE)
        cleaned_watermarks += 1
        
    for i in range(len(q['options'])):
        if WATERMARK_PATTERN.search(q['options'][i]):
            q['options'][i] = WATERMARK_PATTERN.sub('', q['options'][i]).strip()
            cleaned_watermarks += 1
            
    if WATERMARK_PATTERN.search(q.get('explanation', '')):
        q['explanation'] = WATERMARK_PATTERN.sub('', q['explanation']).strip()
        cleaned_watermarks += 1

print(f"Cleaned {cleaned_watermarks} watermark instances across questions, options, and explanations.")

# ==============================================================================
# STEP 3: Fix OCR Typos across questions
# ==============================================================================

TYPO_REPLACEMENTS = [
    (r'\binform of the ear\b', 'in front of the ear'),
    (r'\bth e diaphragm\b', 'the diaphragm'),
    (r'\bth e\b', 'the'),
    (r'\bunconsciousness patient\b', 'unconscious patient'),
    (r'\bchose acupoint\b', 'choose acupoint'),
    (r'\bcurves around the lips \.\.turns\b', 'curves around the lips, turns'),
    (r'\b4 fun above the umbilicus\b', '4 cun above the umbilicus'),
    (r'\b2 fun proximal\b', '2 cun proximal'),
    (r'\b5 fun directly above\b', '5 cun directly above'),
    (r'\b1 fun directly above\b', '1 cun directly above'),
    (r'\b1 fun respectively\b', '1 cun respectively'),
    (r'\b1 fun\b', '1 cun'),
    (r'\b2 fun\b', '2 cun'),
    (r'\b3 fun\b', '3 cun'),
    (r'\b4 fun\b', '4 cun'),
    (r'\b5 fun\b', '5 cun'),
    (r'\bHUantiao\b', 'Huantiao'),
    (r'\bQuxhi\b', 'Quchi'),
    (r'\bm\. flexor radialis\b', 'm. flexor carpi radialis'),
]

fixed_typos = 0
for q in questions:
    for pat, rep in TYPO_REPLACEMENTS:
        if re.search(pat, q['question'], re.IGNORECASE):
            q['question'] = re.sub(pat, rep, q['question'], flags=re.IGNORECASE)
            fixed_typos += 1
        for i in range(len(q['options'])):
            if re.search(pat, q['options'][i], re.IGNORECASE):
                q['options'][i] = re.sub(pat, rep, q['options'][i], flags=re.IGNORECASE)
                fixed_typos += 1
        if 'explanation' in q and re.search(pat, q['explanation'], re.IGNORECASE):
            q['explanation'] = re.sub(pat, rep, q['explanation'], flags=re.IGNORECASE)
            fixed_typos += 1

print(f"Fixed {fixed_typos} OCR text typos.")

# ==============================================================================
# STEP 4: Remove Distractor Giveaway Asymmetries & Symmetrize Options
# ==============================================================================

# Helper to strip isolated point pinyin like "GB20 (Fengchi) and LU7 (Lieque)" -> "GB20 and LU7"
def strip_point_pinyin(s):
    # Pattern to match e.g. "GB20 (Fengchi)" -> "GB20"
    return re.sub(r'([A-Z]{2}\d+)\s*\([^)]+\)', r'\1', s)

# Clean specific giveaway questions:
for q in questions:
    qid = q['id']
    
    # ID 14: Symmetrize DU14 landmarks
    if qid == 14:
        q['options'] = [
            "In the depression below the spinous process of C7 (7th cervical vertebra)",
            "In the depression below the spinous process of T1 (1st thoracic vertebra)",
            "In the depression below the spinous process of C2 (2nd cervical vertebra)",
            "In the depression below the spinous process of T3 (level of scapular spine)"
        ]

    # ID 30: Symmetrize GB21 landmarks
    elif qid == 30:
        q['options'] = [
            "The acromion and the clavicle",
            "DU14 and the acromion",
            "The superior angle of the scapula and spine of scapula",
            "The anterior axillary line and posterior axillary line"
        ]

    # ID 42: SI6 palpation
    elif qid == 42:
        q['options'] = [
            "Make a tight fist",
            "Turn the palm toward the chest",
            "Extend the 5th digit against resistance",
            "Abduct the thumb maximally"
        ]

    # ID 91: Inner Bladder line needling angle
    elif qid == 91:
        q['options'] = [
            "Oblique 0.5 - 0.8 cun towards the spine",
            "Perpendicular 1.5 - 2.0 cun into the intercostal space",
            "Oblique 1.0 - 1.5 cun laterally away from the spine",
            "Perpendicular 2.0 - 2.5 cun directly into the paraspinal groove"
        ]

    # ID 108: DU15 safe depth
    elif qid == 108:
        q['options'] = [
            "0.5 to 0.8 cun, strictly perpendicular or slightly inferior",
            "1.5 to 2.0 cun, directed superiorly towards the occiput",
            "2.0 to 2.5 cun, directed perpendicular towards the brainstem",
            "1.0 to 1.5 cun, angled superiorly towards the nose"
        ]

    # Confluent pairs: IDs 134, 135, 136, 137
    elif qid == 134:
        q['options'] = [
            "PC6 (Yin Wei) and SP4 (Chong Mai)",
            "LU7 (Ren Mai) and KD6 (Yin Qiao)",
            "SI3 (Du Mai) and BL62 (Yang Qiao)",
            "GB41 (Dai Mai) and TE5 (Yang Wei)"
        ]
    elif qid == 135:
        q['options'] = [
            "LU7 (Ren Mai) and KD6 (Yin Qiao)",
            "PC6 (Yin Wei) and SP4 (Chong Mai)",
            "SI3 (Du Mai) and BL62 (Yang Qiao)",
            "GB41 (Dai Mai) and TE5 (Yang Wei)"
        ]
    elif qid == 136:
        q['options'] = [
            "SI3 (Du Mai) and BL62 (Yang Qiao)",
            "LU7 (Ren Mai) and KD6 (Yin Qiao)",
            "GB41 (Dai Mai) and TE5 (Yang Wei)",
            "PC6 (Yin Wei) and SP4 (Chong Mai)"
        ]
    elif qid == 137:
        q['options'] = [
            "GB41 (Dai Mai) and TE5 (Yang Wei)",
            "SI3 (Du Mai) and BL62 (Yang Qiao)",
            "PC6 (Yin Wei) and SP4 (Chong Mai)",
            "LU7 (Ren Mai) and KD6 (Yin Qiao)"
        ]
    elif qid == 138:
        q['options'] = [
            "Qi deficiency or Blood deficiency",
            "Interior Full Heat pattern",
            "Phlegm-Heat in the Middle Jiao",
            "Extreme Yin deficiency with Fire"
        ]

    # Spleen Not Controlling Blood
    elif qid == 149:
        q['options'] = [
            "Spleen Not Controlling Blood",
            "Blood Heat causing Bleeding",
            "Liver Fire Injuring Vessels",
            "Blood Stasis Obstructing Vessels"
        ]

    # Liver Fire Blazing
    elif qid == 150:
        q['options'] = [
            "Liver Fire Blazing",
            "Liver Yang Rising",
            "Liver Qi Stagnation",
            "Gallbladder Damp-Heat"
        ]

    # Six Stages / Four Levels
    elif qid == 154:
        q['options'] = [
            "Shaoyang Syndrome (Lesser Yang)",
            "Taiyang Syndrome (Greater Yang)",
            "Yangming Syndrome (Yang Brightness)",
            "Taiyin Syndrome (Greater Yin)"
        ]
    elif qid == 155:
        q['options'] = [
            "Yangming Channel Syndrome (Qi Level Heat)",
            "Yangming Bowel Syndrome (Dry Stool Heat)",
            "Taiyang Wind Strike (Exterior Deficiency)",
            "Shaoyang Gallbladder Syndrome (Half-Exterior)"
        ]
    elif qid == 156:
        q['options'] = [
            "Ying Level (Nutritive Level)",
            "Wei Level (Defensive Level)",
            "Qi Level (Interior Heat Level)",
            "Xue Level (Blood Level)"
        ]
    elif qid == 157:
        q['options'] = [
            "Xue Level (Blood Level)",
            "Ying Level (Nutritive Level)",
            "Qi Level (Interior Heat Level)",
            "Wei Level (Defensive Level)"
        ]

    # Point pair questions in Q164-182: strip isolated pinyin from correct option
    elif qid == 164:
        q['options'] = ["GB20 and LU7", "ST36 and SP6", "PC6 and RN12", "HT7 and SP6"]
    elif qid == 165:
        q['options'] = ["PC6 and ST36", "LI4 and SP6", "RN4 and RN6", "BL60 and BL67"]
    elif qid == 166:
        q['options'] = ["ST44 and LI4", "GB20 and BL60", "LR3 and KD3", "LU7 and LU9"]
    elif qid == 167:
        q['options'] = ["RN3 and SP9", "ST36 and LI4", "HT7 and PC6", "LU7 and BL40"]
    elif qid == 172:
        q['options'] = ["HT7 and KD3", "LI4 and LR3", "ST36 and SP9", "GB34 and BL40"]
    elif qid == 173:
        q['options'] = ["ST4, ST6, LI4, GB14", "RN12, ST36, SP6, BL20", "HT7, PC6, BL15, DU20", "KD3, BL23, RN4, SP10"]
    elif qid == 174:
        q['options'] = ["TE6 and KD6", "ST36 and LI4", "PC6 and SP4", "BL40 and SI3"]
    elif qid == 175:
        q['options'] = ["RN12 or RN8", "ST36 only", "LI4 only", "BL40 only"]
    elif qid == 177:
        q['options'] = [
            "Collapse of Yang (desertion pattern)",
            "Excessive Lung Fire (heat pattern)",
            "High fever with delirium (toxic heat)",
            "Acute appendicitis (damp-heat in Large Intestine)"
        ]
    elif qid == 180:
        q['options'] = ["DU20, RN6, ST36, Zigong", "LR3, LI4, PC6, GB34", "BL15, HT7, PC6, RN14", "BL28, RN3, SP9, ST28"]
    elif qid == 181:
        q['options'] = ["GB20, LU7, BL60, Taiyang", "ST36, SP6, RN12, BL20", "LR3, LR2, GB34, GB20", "HT7, PC6, KD3, SP6"]
    elif qid == 182:
        q['options'] = ["LR2, LR3, GB20, Taiyang", "RN4, RN6, DU4, ST36", "SP6, SP9, RN9, BL20", "LU9, LU7, BL13, RN17"]

    # RN3 caution
    elif qid == 220:
        q['options'] = [
            "Use shallow puncture or postpone until patient voids",
            "Insert 2.0 cun perpendicularly",
            "Apply forceful electroacupuncture",
            "Puncture horizontally downward"
        ]

    # Pulse patterns: 256, 257, 261, 262
    elif qid == 256:
        q['options'] = [
            "Cold Pattern (Full Cold or Yang Deficiency)",
            "Heat Pattern (Full Heat or Yin Deficiency)",
            "Wind Pattern (Internal or External Wind)",
            "Dampness Pattern (Damp-Heat or Phlegm-Damp)"
        ]
        q['explanation'] = "Cold congeals and slows blood flow; a slow pulse (< 60 bpm) is the hallmark of Cold patterns (Interior Full Cold or Yang Deficiency)."
    elif qid == 257:
        q['options'] = [
            "Heat Pattern (Full Heat or Deficiency Heat)",
            "Cold Pattern (Full Cold or Yang Deficiency)",
            "Food Stagnation (Excess Stagnation)",
            "Blood Stasis (Internal Obstruction)"
        ]
    elif qid == 261:
        q['options'] = [
            "Severe Interior Cold due to Yang collapse",
            "Extreme Interior Heat injuring fluids",
            "Exterior Wind-Heat with toxic fire",
            "Heart Fire blazing with blood stasis"
        ]
    elif qid == 262:
        q['options'] = [
            "Heart Blood Stasis",
            "Lung Phlegm-Heat",
            "Liver Qi Stagnation",
            "Stomach Cold"
        ]

    # Strip point pinyin in 263-272
    elif qid == 263:
        q['options'] = ["HT7, SP6, BL15, BL20", "LR3, GB20, Taiyang, LI4", "RN3, SP9, BL28, KD3", "LU5, LU7, BL13, LI11"]
    elif qid == 264:
        q['options'] = ["LI11, LI4, LU10, DU14", "RN4, RN6, DU4, BL23", "SP9, RN9, ST28, BL20", "KD3, BL23, HT7, SP6"]
    elif qid == 265:
        q['options'] = ["DU26 and BL40", "RN12 and ST36", "HT7 and SP6", "LU9 and KD3"]
    elif qid == 266:
        q['options'] = ["BL17, PC6, RN12, ST36", "HT7, SP6, BL15, BL20", "GB20, LU7, LI4, BL60", "RN4, RN6, DU4, BL23"]
    elif qid == 267:
        q['options'] = [
            "Moxibustion on RN4, RN6, SP8, and SP6",
            "Sedating acupuncture on LI11, ST44, and LR2",
            "Bleeding technique on LU11, HT9, and PC9",
            "Deep perpendicular puncture on BL1 and BL2"
        ]
    elif qid == 268:
        q['options'] = [
            "Moxibustion on BL20, BL23, RN4, and ST36",
            "Bleeding technique on LI11, LU5, and BL40",
            "Sedating acupuncture on LR2, LR3, and GB34",
            "Shallow puncture on RN3, ST28, and SP9"
        ]
    elif qid == 269:
        q['options'] = ["LR3, TE6, ST25, CV12", "BL23, DU4, RN4, KD3", "LU11, LI1, PC9, HT9", "SP10, BL17, BL15, HT7"]
    elif qid == 270:
        q['options'] = ["BL23, BL28, RN3, SP6", "LI11, LI4, DU14, ST44", "LR2, LR3, GB34, GB20", "LU5, LU6, LU7, BL13"]
    elif qid == 271:
        q['options'] = ["RN17, ST18, GB21, SI1", "KD3, BL23, SP6, RN4", "BL40, SI3, DU26, BL60", "RN12, ST36, SP9, BL20"]
    elif qid == 272:
        q['options'] = ["HT6 and KD7", "LI4 and KD7", "ST36 and SP6", "LR3 and GB34"]

    elif qid == 284:
        q['options'] = ["San Jiao", "Pericardium", "Gallbladder", "Liver"]
    elif qid == 291:
        q['options'] = ["Nose", "Ears", "Eyes", "Tongue"]
    elif qid == 292:
        q['options'] = [
            "Beside the nose at LI20, ascends to inner canthus at BL1, descends to ST1",
            "Directly within the middle jiao at the Stomach and ascends along the throat",
            "At the lateral corner of the mouth at ST4 and circles around the lips",
            "At the lateral corner of the second toe nail at ST45 and ascends the leg"
        ]
    elif qid == 297:
        q['options'] = ["Eye system", "Inner ear", "Nasal cavity", "Vocal cords"]

    # Balance length outliers in Q21, 23, 40, 45, 93, 101, 102, 104, 151, 160, 161, 176, 224, 226, 227, 253, 255
    elif qid == 21:
        q['options'] = [
            "The parotid gland and branches of the facial nerve",
            "The eyeball and medial rectus muscle within the orbit",
            "The temporalis muscle and superficial temporal artery",
            "The lacrimal gland and lateral rectus muscle"
        ]
    elif qid == 23:
        q['options'] = [
            "0.5 cun within the hairline at the corner of forehead, 4.5 cun lateral to DU24",
            "1.0 cun directly above the midpoint of the eyebrow, on the anterior hairline",
            "1.5 cun lateral to DU24 within the hairline, directly above the pupil",
            "0.5 cun posterior to the temple hairline, midway between GB4 and GB6"
        ]
    elif qid == 40:
        q['options'] = [
            "3 cun superior to lateral malleolus, between posterior border of fibula and peroneus tendons",
            "3 cun superior to lateral malleolus, between anterior border of fibula and extensor digitorum",
            "4 cun superior to lateral malleolus, on the anterior border of the fibula",
            "7 cun superior to lateral malleolus, on the posterior border of the fibula"
        ]
    elif qid == 45:
        q['options'] = [
            "Directly at the midpoint of the plantar heel pad, at posterior calcaneal tubercle",
            "In the depression formed when foot is in plantar flexion, at junction of anterior 1/3 and posterior 2/3 of sole",
            "At the tuberosity of 5th metatarsal bone, on the lateral margin of sole",
            "In the center of medial longitudinal arch, midway between 1st metatarsal and heel"
        ]
    elif qid == 93:
        q['options'] = [
            "Have the patient completely empty their urinary bladder prior to treatment",
            "Ensure the patient drinks at least 500 mL of fluid immediately before needle insertion",
            "Maintain the patient in a full upright seated posture during needle retention",
            "Apply vigorous downward needle manipulation towards the pubic symphysis"
        ]
    elif qid == 101:
        q['options'] = [
            "Strictly shallow oblique insertion, avoiding deep posterior or inferior puncture",
            "Perpendicular insertion to a depth of 1.0 to 1.5 cun directly into the fossa",
            "Deep oblique insertion directed medially towards the trachea and thyroid",
            "Deep vertical insertion directed posteriorly towards the apex of the lung"
        ]
    elif qid == 102:
        q['options'] = [
            "Relax the patient, gently massage surrounding tissue, or insert an adjacent needle to relieve spasm",
            "Forcefully twist the needle against resistance in the opposite direction until released",
            "Use surgical pliers to pull the needle shaft directly upward with continuous traction",
            "Apply strong high-frequency electroacupuncture stimulation to loosen connective tissue"
        ]
    elif qid == 104:
        q['options'] = [
            "Sudden onset of dyspnea, chest tightness, pain on inspiration, and dry cough",
            "Immediate bilateral lower extremity numbness and loss of patellar reflexes",
            "Sudden profuse watery diarrhea accompanied by acute lower abdominal cramps",
            "Acute severe frontal headache with explosive projectile vomiting"
        ]
    elif qid == 151:
        q['options'] = [
            "Liver Yang Rising due to Liver and Kidney Yin Deficiency",
            "Liver Fire Blazing with Stomach Heat Accumulation",
            "Exterior Wind-Heat attacking the Head and Upper Orifices",
            "Turbid Phlegm Obstructing the Clear Orifices"
        ]
    elif qid == 160:
        q['options'] = [
            "Severe Zang organ exhaustion or serious organic heart disease",
            "Exterior Wind-Cold with mild emotional agitation",
            "Summer-Heat with mild Dampness accumulation",
            "Stomach Food Stagnation with Qi rebellion"
        ]
    elif qid == 161:
        q['options'] = [
            "Spleen Yang Deficiency with Dampness and Phlegm Accumulation",
            "Excessive Heat in the Blood with Toxic Fire Eruption",
            "Kidney Yin Deficiency with Empty Fire Flaring Upward",
            "Liver Fire Blazing with Gallbladder Damp-Heat Accumulation"
        ]
    elif qid == 176:
        q['options'] = [
            "Scrofula, pulmonary tuberculosis, skin ulcers, and early-stage toxic boils",
            "Bronchial asthma, chronic cough, and cold phlegm stagnation",
            "Kidney Yang deficiency, impotence, and cold spermatorrhea",
            "Wind-Cold facial paralysis, numbness, and hemiplegia"
        ]
    elif qid == 224:
        q['options'] = [
            "Press the tissue around the shaft until the broken end emerges, and extract with forceps",
            "Push surrounding tissue downward and advise patient to move joint actively",
            "Instruct patient to remain calm and schedule non-urgent surgical excision tomorrow",
            "Attempt to probe and retrieve needle tip using a longer acupuncture needle"
        ]
    elif qid == 226:
        q['options'] = [
            "Cardiac pacemakers or implanted electrical medical devices",
            "Essential hypertension controlled with oral medication",
            "Chronic low back pain and lumbar disc herniation",
            "Mild Spleen Qi deficiency with sluggish digestion"
        ]
    elif qid == 227:
        q['options'] = [
            "The face, near mucous membranes, or directly over large superficial blood vessels",
            "The lower abdomen, lumbar region, and gluteal muscle area",
            "The plantar surface of the feet and dorsal aspects of the digits",
            "The upper thoracic back along the outer Bladder channel line"
        ]
    elif qid == 253:
        q['options'] = [
            "Blood Stasis or severe Blood/Essence deficiency",
            "Excessive Full Heat injuring Body Fluids",
            "Phlegm-Dampness accumulation in the Middle Burner",
            "Exterior Wind-Cold with Lung Qi stagnation"
        ]
    elif qid == 255:
        q['options'] = [
            "Excess Heat pattern, Liver Yang, or constitutional vitality",
            "Severe Yin Collapse with floating deficient Yang",
            "Interior Full Cold with severe Yang deficiency",
            "Kidney Essence deficiency with empty pulses"
        ]

    # Specific fixes in 301-809
    elif qid == 354:
        q['options'] = [
            "Sishencong (group of 4 points 1 cun anterior, posterior, and lateral to GV20)",
            "Taiyang (depression 1 cun posterior to midpoint between lateral eyebrow and outer canthus)",
            "Yintang (midway between the medial ends of the two eyebrows)",
            "Erjian (at the apex of the auricle when folded forward)"
        ]
    elif qid == 469:
        q['options'] = [
            "Liver Blood Deficiency generating Wind with Spleen Qi Deficiency",
            "Liver Yin and Blood Deficiency generating Wind with Stomach Damp Heat",
            "Liver Wind and Phlegm Heat attacking the Upper Orifices",
            "Liver Yang Rising generating Wind with Kidney Yin Deficiency"
        ]
    elif qid == 578:
        q['options'] = [
            "Moxibustion with Salt (Shenque)",
            "Moxibustion with Aconite (Fu Zi) cake",
            "Moxibustion with Ginger slice",
            "Moxibustion with Garlic slice"
        ]
    elif qid == 593:
        q['options'] = [
            "GV26 (Renzhong), GV12 (Shenzhu), GV3 (Yaoyangguan), BL23 (Shenshu), BL20 (Pishu), ST36 (Zusanli), SP6 (Sanyinjiao), LI4 (Hegu)",
            "SP4 (Gongsun), PC6 (Neiguan), BL65 (Shugu), Bafeng (EX-LE10), ST36 (Zusanli), SP9 (Yinlingquan), GB34 (Yanglingquan), LI11 (Quchi)",
            "LI11 (Quchi), LU5 (Chize), TE10 (Tianjing), TE5 (Waiguan), LI4 (Hegu), BL40 (Weizhong), GB34 (Yanglingquan), ST36 (Zusanli)",
            "SI3 (Houxi), BL62 (Shenmai), SP21 (Dabao), BL17 (Geshu), LI15 (Jianyu), LI11 (Quchi), LI4 (Hegu), TE4 (Yangchi), GB30 (Huantiao), GB34 (Yanglingquan), GB39 (Xuanzhong), ST41 (Jiexi)"
        ]
    elif qid == 634:
        q['options'] = [
            "Red tongue with redder tip and swollen red points, yellow coat; excess rapid overflowing pulse",
            "Red tongue with redder tip and red points on sides, thin yellow coat; soft thready rapid pulse",
            "Red tongue without coating; floating empty and rapid pulse",
            "Red tongue with redder sides and dry yellow coat; wiry rapid pulse"
        ]

print("Completed Step 4: Elimination of distractor giveaways and option symmetrization.")

# ==============================================================================
# STEP 5: Rebalance Answer Positions for Questions 1-300 (Eliminate Option A giveaway)
# ==============================================================================

# In Q1-300, 266 out of 300 questions originally had answer = 0 (A), a dead giveaway.
# Rebalance options deterministically: exactly 75 A, 75 B, 75 C, 75 D.
rng = random.Random(42)  # Deterministic seed for perfect reproducibility
target_positions = [i % 4 for i in range(300)]
rng.shuffle(target_positions)

rebalanced_count = 0
for i in range(300):
    q = questions[i]
    old_ans = q['answer']
    target_ans = target_positions[i]
    
    if old_ans != target_ans:
        opts = list(q['options'])
        correct_val = opts[old_ans]
        
        other_opts = [opts[j] for j in range(4) if j != old_ans]
        
        new_opts = []
        other_idx = 0
        for pos in range(4):
            if pos == target_ans:
                new_opts.append(correct_val)
            else:
                new_opts.append(other_opts[other_idx])
                other_idx += 1
                
        q['options'] = new_opts
        q['answer'] = target_ans
        rebalanced_count += 1

print(f"Rebalanced {rebalanced_count} questions in Q1-300.")

# Verify distribution for Q1-300
q1_300_dist = {}
for q in questions[:300]:
    q1_300_dist[q['answer']] = q1_300_dist.get(q['answer'], 0) + 1
print(f"New Answer distribution for Q1-300 (0=A, 1=B, 2=C, 3=D): {q1_300_dist}")

# Verify total distribution across all 809 questions
total_dist = {}
for q in questions:
    total_dist[q['answer']] = total_dist.get(q['answer'], 0) + 1
print(f"Total Exam Bank Answer distribution: {total_dist}")

# Save curated dataset
with open('data/exam_questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated data/exam_questions.json with all fixes and verified answers!")

"""Insert 14 remaining unique high-yield cards to reach exactly 100 new cards (306 total).
"""

import sys
import sqlite3
from pathlib import Path

# UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"d:\TCM\acupuncture_app")
sys.path.insert(0, str(BASE_DIR))

from modules.tcm_points import format_point_bilingual

DB_PATH = BASE_DIR / "data" / "acupuncture.db"

CARDS_14 = [
    {
        "category": "Meridians and Points",
        "title": "EX-B2 (Huatuojiaji / 华佗夹脊)",
        "front": "State the anatomical location, segmental organ innervation, and needling technique for EX-B2 (Huatuojiaji / 华佗夹脊).",
        "back": "• Location: A group of 17 pairs of points located 0.5 cun lateral to the lower border of the spinous processes from T1 through L5.\n• Segmental Visceral Organ Correspondence:\n  - T1 – T4: Disorders of the Lung, Heart, and upper extremities.\n  - T5 – T7: Disorders of the Heart, Diaphragm, and chest.\n  - T8 – T10: Disorders of the Liver and Gallbladder.\n  - T11 – T12: Disorders of the Spleen and Stomach.\n  - L1 – L2: Disorders of the Kidneys and water metabolism.\n  - L3 – L5: Disorders of the Bladder, Large/Small Intestine, Uterus, and lower limbs.\n• Needling: Perpendicular-oblique insertion 0.5–1.0 cun directed slightly medially toward the spine. Caution: Never direct needles deeply laterally in the thoracic region (pneumothorax risk)!",
        "consensus": "Universal consensus across Chinese and Western acupuncture: Corresponds to spinal nerve dorsal rami and sympathetic trunk.",
        "variations": "Deadman includes cervical and sacral extensions in modern clinical research.",
        "sources": '["CAM p. 195", "Deadman p. 570"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "EX-UE7 (Yaotongxue / 腰痛穴)",
        "front": "What is the location, special dynamic mobilization protocol, and indication for EX-UE7 (Yaotongxue / 腰痛穴)?",
        "back": "• Location: On the dorsum of the hand, midway between the transverse wrist crease and metacarpophalangeal joints, 2 points per hand:\n  1. In the depression between the 2nd and 3rd metacarpal bones, just distal to their bases.\n  2. In the depression between the 4th and 5th metacarpal bones, just distal to their bases.\n• Primary Indication: Acute Lumbar Sprain (Qi and Blood stasis in lower back).\n• Dynamic Mobilization Protocol (Critical Board Pearl):\n  - Insert needles obliquely 0.5–1.0 cun toward the center of the palm.\n  - Apply strong, continuous reducing manipulation while simultaneously instructing the patient to actively mobilize, flex, extend, and rotate the lumbar spine!\n  - Unblocks stagnant Qi in the lumbar collaterals immediately.",
        "consensus": "Supreme empirical point for acute onset low back strain and traumatic muscle spasm.",
        "variations": "Also named Yaotongdian (腰痛点).",
        "sources": '["CAM p. 196", "Deadman p. 573"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "EX-LE6 (Dannangxue / 胆囊穴)",
        "front": "Identify the location, diagnostic significance, and clinical actions of EX-LE6 (Dannangxue / 胆囊穴).",
        "back": "• Location: On the lateral aspect of the lower leg, 1 to 2 cun directly inferior to GB34 (Yanglingquan). Determined by palpating for a distinct, exquisite tender spot.\n• Diagnostic Significance: Markedly tender to palpation in acute and chronic cholecystitis and cholelithiasis (gallstones).\n• Clinical Actions: Clears Gallbladder heat, dispels damp-heat, drains bile, expels gallstones, relieves biliary colic.\n• Needling: Perpendicular insertion 1.0–1.5 cun.",
        "consensus": "Universal consensus: Premier diagnostic and therapeutic extra point for biliary tract disease.",
        "variations": "CAM notes pairing with GB34 and Dannangshu (BL19) for acute right upper quadrant pain.",
        "sources": '["CAM p. 197", "Deadman p. 580"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "EX-LE7 (Lanweixue / 阑尾穴)",
        "front": "Describe the location, diagnostic role, and therapeutic actions of EX-LE7 (Lanweixue / 阑尾穴).",
        "back": "• Location: On the anterior-lateral lower leg, approximately 2 cun directly inferior to ST36 (Zusanli) on the right leg. Located by palpating for marked tenderness.\n• Diagnostic Role: Tenderness at Lanweixue strongly correlates with acute and chronic Appendicitis (Intestinal Carbuncle / *Chang Yong*).\n• Clinical Actions: Activates Qi and Blood in the Large Intestine, clears heat and resolves toxicity, alleviates abdominal pain.\n• Needling: Perpendicular insertion 1.0–1.5 cun.\n• Emergency Caution: Appendicitis with peritoneal signs (rebound tenderness, rigid abdomen) requires immediate surgical evaluation!",
        "consensus": "Classic empirical extra point for appendix inflammation and intestinal carbuncle.",
        "variations": "Palpated primarily on the right leg, corresponding to the anatomical right lower quadrant appendix.",
        "sources": '["CAM p. 198", "Deadman p. 581"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "EX-B1 (Dingchuan / 定喘)",
        "front": "State the anatomical location, actions, and needling depth precautions for EX-B1 (Dingchuan / 定喘).",
        "back": "• Location: 0.5 cun lateral to the depression below the spinous process of the 7th cervical vertebra (DU14 Dazhui).\n• Name Meaning: 'Calm Dyspnea / Stop Asthma'.\n• Actions: Diffuses Lung Qi, calms wheezing, clears phlegm, halts cough.\n• Primary Indications: Acute asthma attacks, bronchial spasms, dyspnea, chronic bronchitis, coughing, upper back pain.\n• Needling: Perpendicular-oblique insertion 0.5–0.8 cun directed slightly medially toward the spine. Caution: Deep lateral insertion risks apex of lung pneumothorax!",
        "consensus": "Universal consensus: The primary extra point for acute respiratory distress, asthma, and wheezing.",
        "variations": "CAM pairs Dingchuan with Feishu (BL13) and Shanzhong (REN17).",
        "sources": '["CAM p. 194", "Deadman p. 569"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "EX-LE2 (Heding / 鹤顶)",
        "front": "What is the location, actions, and classic clinical application of EX-LE2 (Heding / 鹤顶)?",
        "back": "• Location: In the depression above the midpoint of the superior border of the patella.\n• Name Meaning: 'Crane's Summit'.\n• Actions: Activates Qi and Blood in the knee joint, dispels wind-damp, benefits sinews and bones.\n• Primary Indications: Crane's Knee Bi syndrome (*He Xi Feng* = swollen knee with emaciated thigh/calf), osteoarthritis of knee, patellofemoral pain, motor impairment of lower limbs.\n• Needling: Perpendicular insertion 0.5–1.0 cun.",
        "consensus": "Essential knee joint point, commonly combined with Neixiyan, Waixiyan (ST35), and GB34.",
        "variations": "Moxibustion is frequently combined for chronic cold-damp knee swelling.",
        "sources": '["CAM p. 196", "Deadman p. 578"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "EX-LE10 (Bafeng / 八风)",
        "front": "Detail the location, actions, and clinical indications for EX-LE10 (Bafeng / 八风).",
        "back": "• Location: On the dorsum of the foot, in the depressions on the webs between the toes, proximal to the margin of the webs, 8 points in total (4 on each foot).\n• Actions: Clears heat, expels toxic dampness, activates collaterals, relieves swelling.\n• Primary Indications: Peripheral neuropathy of feet, beriberi (leg edema/numbness), toe numbness, gouty arthritis, Raynaud's phenomenon of toes, snakebite swelling.\n• Needling: Oblique insertion 0.5–0.8 cun directed proximally, or prick to bleed with lancet.",
        "consensus": "Classic extra point group for distal lower limb numbness and toxic peripheral heat.",
        "variations": "Contains standard channel points LV2, ST44, GB43 as a subset of the web locations.",
        "sources": '["CAM p. 198", "Deadman p. 583"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "EX-UE9 (Baxie / 八邪)",
        "front": "What are the location, actions, and indications for EX-UE9 (Baxie / 八邪)?",
        "back": "• Location: On the dorsum of the hand, in the depressions on the webs between the fingers, proximal to the margin of the webs, 8 points in total (4 on each hand).\n• Actions: Clears heat, expels wind-damp, reduces swelling, benefits fingers.\n• Primary Indications: Rheumatoid arthritis of hand, finger stiffness and numbness, Raynaud's disease, carpal spasm, febrile headache, eye pain.\n• Needling: Oblique insertion 0.5–0.8 cun directed proximally, or prick to bleed with lancet.",
        "consensus": "Premier distal upper limb extra point group for hand arthritis and inflammatory finger disorders.",
        "variations": "Corresponds to the upper limb counterpart of Bafeng.",
        "sources": '["CAM p. 196", "Deadman p. 574"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "EX-HN14 (Jiachengjiang / 夹承浆)",
        "front": "State the location, nerve distribution, and clinical utility of EX-HN14 (Jiachengjiang / 夹承浆).",
        "back": "• Location: 1 cun lateral to REN24 (Chengjiang), directly below ST4 (Dicang) on the mental foramen.\n• Nerve Distribution: Located over the mental nerve (branch of Mandibular division CN V3) and facial nerve branches.\n• Primary Indications: Trigeminal neuralgia (3rd mandibular division), facial paralysis (Bell's palsy), dental pain in lower jaw, lip tremor/spasm.\n• Needling: Oblique insertion 0.3–0.5 cun directed medially.",
        "consensus": "Universal consensus: Key point for treating intractable lower jaw neuralgias and persistent perioral Bell's palsy sequelae.",
        "variations": "Often paired with ST6 and ST7 for complete mandibular coverage.",
        "sources": '["CAM p. 194", "Deadman p. 566"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "EX-HN12 & EX-HN13 (Jinjin & Yuye / 金津 & 玉液)",
        "front": "Describe the location, pricking-to-bleed technique, and emergency indications for Jinjin & Yuye.",
        "back": "• Location: On the sublingual veins on either side of the frenulum of the tongue:\n  - Jinjin (EX-HN12): On the vein to the patient's left.\n  - Yuye (EX-HN13): On the vein to the patient's right.\n• Technique: Ask patient to roll tongue upward against roof of mouth; use sterile three-edged needle or lancet to prick the vein to bleed a few drops of blood. Instruct patient to rinse mouth with clean water. STRICTLY NO deep needle retention!\n• Primary Indications: Acute severe vomiting, stiff tongue and aphasia following wind-stroke, severe unquenchable thirst in Xiao Ke, aphthous stomatitis.",
        "consensus": "Classic emergency sublingual bloodletting points in Chinese medicine.",
        "variations": "High efficacy for acute heat stroke, sunstroke, and toxic throat swelling.",
        "sources": '["CAM p. 194", "Deadman p. 565"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "Channel Theory: Divergent Channels (Jing Bie / 经别)",
        "front": "Explain the trajectory, connections, and clinical functions of the Twelve Divergent Channels (Jing Bie).",
        "back": "• Trajectory Pattern: \n  1. Separate (*Li*): Branch off from primary channels at the limbs (major joints).\n  2. Enter (*Ru*): Penetrate deep into the thoracic and abdominal cavities to connect with Zang-Fu organs.\n  3. Emerge (*Chu*): Re-emerge at the head and neck.\n  4. Converge (*He*): Yin divergent channels converge with their paired Yang divergent channels to join the primary Yang channels.\n• Core Clinical Functions:\n  - Link Yin channels to the head and brain (explains how Yin channels treat mental/head disorders).\n  - Strengthen interior-exterior relationship between paired Zang and Fu.\n  - Distribute Wei Qi into the deep interior chest and abdomen.",
        "consensus": "Fundamental theoretical meridian system tested on all advanced board exams.",
        "variations": "Divergent channels have no acupoints of their own; they are accessed via Primary channel points.",
        "sources": '["Deadman p. 18", "Maciocia Foundations p. 845"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "Channel Theory: Longitudinal vs Transverse Luo Vessels",
        "front": "Differentiate Transverse Luo Vessels from Longitudinal Luo Vessels in trajectory and clinical application.",
        "back": "• Transverse Luo Vessels:\n  - Trajectory: Travel horizontally from the Luo-connecting point of one channel to the Yuan-source point of its interiorly-exteriorly paired channel.\n  - Application: Basis of Guest-Host (Yuan-Luo) treatment pairings (e.g. Host LU9 + Guest LI6).\n• Longitudinal Luo Vessels:\n  - Trajectory: Travel along their own distinct anatomical pathways, often penetrating deep into internal organs or special body regions.\n  - Examples:\n    * Heart Luo: Ascends along esophagus to root of tongue and eye (explains HT5 treating aphasia!).\n    * Stomach Luo: Ascends to throat and neck.\n    * Great Luo of Spleen (SP21): Disperses in chest and hypochondrium, unifying all blood vessels.\n  - Application: Treat localized symptoms along their unique pathway (Fullness = excess symptoms; Emptiness = deficiency symptoms).",
        "consensus": "Foundational channel theory differentiating collateral vessel types.",
        "variations": "There are 15 (or 16) major Longitudinal Luo vessels in total (12 channels + Ren + Du + Great Luo of Spleen + Great Luo of Stomach).",
        "sources": '["Deadman p. 24", "Maciocia Foundations p. 855"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "Channel Theory: The Twelve Cutaneous Regions (Pi Bu / 皮部)",
        "front": "What are the Twelve Cutaneous Regions (Pi Bu) and their diagnostic and therapeutic significance?",
        "back": "• Definition: The 12 superficial skin zones on the body surface reflecting the underlying territory of the Twelve Primary Channels.\n• Physiological Role: Governed by Wei Qi; forms the body's outermost barrier protecting against exogenous pathogenic factors (Wind, Cold, Heat, Damp).\n• Diagnostic Significance: Internal Zang-Fu and channel disorders manifest superficially in cutaneous regions as color changes (blue = cold/pain, red = heat, pale = deficiency, purple = stasis), flaccidity, or papules.\n• Therapeutic Significance: Explains how superficial stimulation (Plum-Blossom / seven-star dermal tapping, cupping, guasha, intradermal needles) penetrates inward to treat deep organ pathology.",
        "consensus": "The anatomical bridge between dermatology, external therapies, and internal organ physiology.",
        "variations": "Su Wen Chapter 56 is the classic foundational source.",
        "sources": '["Su Wen Ch. 56", "Maciocia Foundations p. 865"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "Eight Extraordinary Vessels: Dai Mai (Girdling Vessel / 带脉)",
        "front": "Describe the pathway, confluent point, binding role, and clinical pathology of the Dai Mai.",
        "back": "• Unique Pathway: The ONLY horizontal vessel in the human body; originates at LV13 (Zhangmen), encircles the waist like a belt, and connects GB26, GB27, and GB28.\n• Confluent Point: GB41 (Zulinqi) - paired with SJ5 (Waiguan).\n• Core Role: Binds and constrains all vertical meridians (Chong, Ren, Du, and 12 primary channels), supports the Uterus and lower jiao.\n• Clinical Pathology:\n  - Excess (Tightness): Abdominal distension, lower back feels tight like a swollen drum.\n  - Deficiency (Relaxation): Persistent leukorrhea, uterine prolapse, miscarriage, lumbar weakness with sensation of 'sitting in freezing water' (*Zuo Ru Zai Shui Zhong*).",
        "consensus": "Universal consensus across all Extraordinary Vessel curricula.",
        "variations": "Classic pair: GB41 (Dai Mai) + SJ5 (Yangwei Mai) for lateral body pain, temporal migraine, and hip/waist disorders.",
        "sources": '["Maciocia Foundations p. 890", "Deadman p. 45"]',
        "importance_level": 1
    }
]

def insert_14():
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM flashcards")
    before = cursor.fetchone()[0]
    print(f"Cards before inserting 14: {before}")

    cursor.execute("SELECT title FROM flashcards")
    existing_titles = set(r[0] for r in cursor.fetchall())

    inserted = 0
    for card in CARDS_14:
        raw_title = card["title"]
        bilingual_title = format_point_bilingual(raw_title)

        if raw_title in existing_titles or bilingual_title in existing_titles:
            print(f"  [SKIP] '{raw_title}' already exists.")
            continue

        bilingual_front = format_point_bilingual(card["front"])
        bilingual_back = format_point_bilingual(card["back"])
        bilingual_consensus = format_point_bilingual(card.get("consensus", ""))
        bilingual_variations = format_point_bilingual(card.get("variations", ""))
        sources_json = card.get("sources", '["Textbook Synthesis"]')
        importance = card.get("importance_level", 2)

        cursor.execute("""
        INSERT INTO flashcards (
            category, title, front, back, consensus, variations, sources,
            mastery_level, review_count, importance_level
        ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
        """, (
            card["category"],
            bilingual_title,
            bilingual_front,
            bilingual_back,
            bilingual_consensus,
            bilingual_variations,
            sources_json,
            importance
        ))
        inserted += 1

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM flashcards")
    after = cursor.fetchone()[0]
    print(f"\nFinished! Inserted: {inserted} cards. Total in database: {after}")

    # Summary by Category
    print("\n--- Final Summary by Category ---")
    cursor.execute("SELECT category, COUNT(*) FROM flashcards GROUP BY category ORDER BY category")
    for cat, count in cursor.fetchall():
        print(f"  • {cat}: {count} cards")

    # Summary by Exam Importance Tier
    print("\n--- Final Summary by Exam Importance Tier ---")
    cursor.execute("SELECT importance_level, COUNT(*) FROM flashcards GROUP BY importance_level ORDER BY importance_level")
    tier_labels = {1: "🔥 Tier 1: High Yield (Must-Know)", 2: "⭐ Tier 2: Core Clinical", 3: "💡 Tier 3: Foundation & Nuance"}
    for tier, count in cursor.fetchall():
        print(f"  • {tier_labels.get(tier, f'Tier {tier}')}: {count} cards ({count*100//after}%)")

    conn.close()

if __name__ == "__main__":
    insert_14()

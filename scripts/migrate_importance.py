"""Migration Script: Assign Board Exam Importance Levels (Tier 1, 2, 3) to all 206 Flashcards.

Tiers:
1 = Tier 1: High Yield (Must-Know) - Guaranteed board exam material (Pan-Canadian / NCCAOM).
2 = Tier 2: Core Clinical - Frequently tested clinical scenarios and patterns.
3 = Tier 3: Foundation & Nuance - Detailed variations, textbook nuances, and secondary points.
"""

import sys
import sqlite3
from pathlib import Path

# UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"d:\TCM\acupuncture_app")
DB_PATH = BASE_DIR / "data" / "acupuncture.db"

# Explicit mapping of card title substrings / patterns to importance levels
TIER_1_KEYWORDS = [
    # Safety & Emergencies
    "cauda equina", "stroke recognition: fast", "myocardial infarction", "deep vein thrombosis",
    "clean needle technique", "pneumothorax", "cns danger points", "visceral puncture",
    "needle fainting", "broken needle", "pregnancy contraindicated", "informed consent",
    "professional boundaries: dual", "electroacupuncture (ea): cardiac", "mandatory reporting of sexual",
    "pediatric record retention", "appendicitis", "bloodborne pathogens", "orthostatic hypotension",
    "diabetes mellitus: diagnostic", "pharmacology: anticoagulants", "pharmacology: corticosteroids",
    # Acupoint Essentials
    "five shu points: theory", "five shu points: mother-child", "yuan-source and luo",
    "xi-cleft points", "back-shu and front-mu", "eight confluent points", "eight hui-meeting",
    "four command points", "the four gates", "lu7 (lieque", "lu11 (shaoshang", "li4 (hegu",
    "li11 (quchi", "st36 (zusanli", "sp6 (sanyinjiao", "sp9 (yinlingquan", "ht7 (shenmen",
    "si3 (houxi", "bl23 (shenshu", "bl40 (weizhong", "bl67 (zhiyin", "ki1 (yongquan",
    "ki3 (taixi", "pc6 (neiguan", "sj5 (waiguan", "gb20 (fengchi", "gb21 (jianjing",
    "gb34 (yanglingquan", "lv3 (taichong", "ren4 (guanyuan", "ren12 (zhongwan", "du14 (dazhui",
    "du20 (baihui", "du26 (shuigou",
    # Core Diagnosis
    "observation of shen", "tongue body color: pale", "tongue coating: thickness",
    "classic pulses: floating", "classic pulses: slow", "classic pulses: slippery",
    "classic pulses: tight", "eight principles (ba gang", "liver patterns: qi stagnation",
    "spleen patterns: qi deficiency", "kidney patterns: kidney yin", "heart patterns: heart blood",
    "radial pulse positions",
    # Illness & Clinical Emergencies
    "bi syndrome: four classic", "wei syndrome (flaccidity)", "xiao ke (wasting",
    "headache: channel differentiation", "insomnia: four major", "zhong feng (wind-stroke): tense",
    "asthma and wheezing: excess", "cough: wind-cold vs wind-heat", "acute lumbar sprain",
    "hypertension (gao xue ya)",
    # Gynecology High-Yield
    "gynecological physiology: tian gui", "four phases of the menstrual cycle",
    "dysmenorrhea (tong jing): excess", "beng lou (flooding", "breech presentation",
    "menopausal syndrome", "threatened miscarriage", "amenorrhea (bi jing): depletion",
    # Paediatrics High-Yield
    "pediatric physiology: 'pure yang'", "pediatric pathology: 'rapid onset",
    "acute infantile convulsions", "malnutrition (gan ji", "pediatric needling safety"
]

TIER_3_KEYWORDS = [
    # Nuances, textbook discrepancies, rare pulses, and secondary details
    "upper vs lower motor neuron", "gastroesophageal reflux", "osteoarthritis vs rheumatoid",
    "neurological examination: deep tendon", "urinalysis: key dipstick",
    "lu9 (taiyuan", "li10 (shousanli", "st8 (touwei", "ht3 (shaohai", "si19 (tinggong",
    "tongue cracks: heart fire", "classic pulses: leather", "classic pulses: scattered",
    "dysentery (li ji)", "tinnitus and deafness: sudden", "jaundice (huang dan)",
    "edema (shui zhong)", "hiccup (e ni)", "manic-depression (dian kuang)",
    "uterine prolapse", "pediatric night crying", "patient positioning: fall",
    "professional boundaries: social media"
]

def determine_tier(title: str, category: str) -> int:
    title_lower = title.lower()
    for kw in TIER_1_KEYWORDS:
        if kw in title_lower:
            return 1
    for kw in TIER_3_KEYWORDS:
        if kw in title_lower:
            return 3
    # Default is Tier 2 (Core Clinical)
    return 2


def run_migration():
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    # Ensure importance_level column exists
    cursor.execute("PRAGMA table_info(flashcards)")
    columns = [row[1] for row in cursor.fetchall()]
    if "importance_level" not in columns:
        print("Adding column 'importance_level' to table flashcards...")
        cursor.execute("ALTER TABLE flashcards ADD COLUMN importance_level INTEGER DEFAULT 2")
        conn.commit()
    else:
        print("Column 'importance_level' already exists.")

    # Retrieve all cards
    cursor.execute("SELECT id, title, category FROM flashcards")
    cards = cursor.fetchall()
    print(f"Total cards found in database: {len(cards)}")

    tier_counts = {1: 0, 2: 0, 3: 0}
    for card_id, title, category in cards:
        tier = determine_tier(title, category)
        cursor.execute("UPDATE flashcards SET importance_level = ? WHERE id = ?", (tier, card_id))
        tier_counts[tier] += 1

    conn.commit()

    print("\n--- Migration Complete: Flashcard Importance Tiers ---")
    print(f"  🔥 Tier 1 (High Yield / Must-Know):       {tier_counts[1]} cards ({tier_counts[1]*100//len(cards)}%)")
    print(f"  ⭐ Tier 2 (Core Clinical / Frequent):     {tier_counts[2]} cards ({tier_counts[2]*100//len(cards)}%)")
    print(f"  💡 Tier 3 (Foundation & Nuance):          {tier_counts[3]} cards ({tier_counts[3]*100//len(cards)}%)")
    print(f"  Total:                                     {len(cards)} cards")

    conn.close()

if __name__ == "__main__":
    run_migration()

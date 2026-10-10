# -*- coding: utf-8 -*-
"""Execute Full Clinical Practice Update: Diagnostics & Case Simulator."""

import sys
import pprint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Import existing bank and new cases
from modules.cases_bank import CLINICAL_CASES as OLD_CASES
from scripts.generate_35_cases import NEW_CASES
from scripts.expand_cases_and_diagnostics import (
    NEW_DIAGNOSTIC_PATTERNS,
    NEW_SYMPTOMS_TO_INJECT,
    NEW_PRESETS
)

# -----------------------------------------------------------------------------
# STEP 1: Update modules/cases_bank.py to 35 Cases
# -----------------------------------------------------------------------------
print(f"Current cases count: {len(OLD_CASES)}")
print(f"New cases to add: {len(NEW_CASES)}")

existing_ids = {c["id"] for c in OLD_CASES}
combined_cases = list(OLD_CASES)

for nc in NEW_CASES:
    if nc["id"] not in existing_ids:
        combined_cases.append(nc)
        existing_ids.add(nc["id"])

print(f"Combined total cases: {len(combined_cases)}")

cases_bank_path = BASE_DIR / "modules" / "cases_bank.py"
header_cases = '''"""Pan-Canadian Examination Clinical Case Bank for Acupuncturists.

Curated cases conforming to the CARB-TCMPA (Canadian Alliance of Regulatory Bodies of
Traditional Chinese Medicine Practitioners and Acupuncturists) Examination Blueprint.
Contains 35 comprehensive patient cases:
- Musculoskeletal & Pain Syndromes (Bi Syndromes, Stiff Neck, Lumbago, Sciatica, Frozen Shoulder, Knee Bi, Tennis Elbow, Fibromyalgia, Cervical Radiculopathy)
- Neurological & Sensory (Bell's Palsy, Stroke Sequelae, Trigeminal Neuralgia, Insomnia, Vertigo, Facial Hemispasm)
- Internal Medicine (Asthma, Chronic Cough, GERD/Epigastric Pain, Daybreak Diarrhea, Diabetes Xiao Ke, Bronchiectasis, Cholecystitis, Geriatric Constipation)
- Urogenital & Nephrology (Acute Xue Lin / UTI with Hematuria, Kidney Yang/Yin Decline)
- Gynecology & Obstetrics (Dysmenorrhea, PMS Migraines, Morning Sickness, Menopause, Uterine Bleeding / Beng Lou)
- Psychiatric & Mental Health (Manic Disorder / Phlegm-Fire Agitating Shen)
- Pediatrics (Infantile Malnutrition / Gan Ji with Sifeng Pricking)
- Dermatology & External (Herpes Zoster, Urticaria)
- Clean Needle Technique, High-Risk Anatomy & Clinical Emergency Protocols (Needle Shock, Pneumothorax, Acute Coronary Syndrome Red Flag)
"""

from typing import List, Dict, Any

CLINICAL_CASES: List[Dict[str, Any]] = '''

formatted_cases = pprint.pformat(combined_cases, indent=4, width=120, sort_dicts=False)

with open(cases_bank_path, "w", encoding="utf-8") as f:
    f.write(header_cases + formatted_cases + "\n")

print(f"Successfully wrote {len(combined_cases)} cases to modules/cases_bank.py")

# -----------------------------------------------------------------------------
# STEP 2: Update modules/internal_diagnostics.py
# -----------------------------------------------------------------------------
diagnostics_path = BASE_DIR / "modules" / "internal_diagnostics.py"
with open(diagnostics_path, "r", encoding="utf-8") as f:
    diag_code = f.read()

import modules.internal_diagnostics as idia
old_patterns = idia.DIAGNOSTIC_PATTERNS
existing_pattern_ids = {p["id"] for p in old_patterns}

combined_patterns = list(old_patterns)
for np in NEW_DIAGNOSTIC_PATTERNS:
    if np["id"] not in existing_pattern_ids:
        combined_patterns.append(np)
        existing_pattern_ids.add(np["id"])

print(f"Old diagnostic patterns: {len(old_patterns)} -> New total: {len(combined_patterns)}")

# Format patterns block
patterns_str = "DIAGNOSTIC_PATTERNS: List[Dict[str, Any]] = " + pprint.pformat(
    combined_patterns, indent=4, width=120, sort_dicts=False
)

# Replace DIAGNOSTIC_PATTERNS block in file
# Find where DIAGNOSTIC_PATTERNS starts and where CLINICAL_PRESETS starts
start_tag = "DIAGNOSTIC_PATTERNS: List[Dict[str, Any]] = ["
end_tag = "\n# =============================================================================\n# CLINICAL PRESET QUICK LOADERS"

idx_start = diag_code.find(start_tag)
idx_end = diag_code.find(end_tag)

if idx_start != -1 and idx_end != -1:
    diag_code = diag_code[:idx_start] + patterns_str + "\n\n" + diag_code[idx_end:]
    print("Replaced DIAGNOSTIC_PATTERNS block successfully.")
else:
    print(f"Warning: Could not find exact tags: idx_start={idx_start}, idx_end={idx_end}")

# Update CLINICAL_PRESETS in file
old_presets = idia.CLINICAL_PRESETS
combined_presets = dict(old_presets)
combined_presets.update(NEW_PRESETS)

presets_str = "CLINICAL_PRESETS = " + pprint.pformat(
    combined_presets, indent=4, width=120, sort_dicts=False
)

p_start_tag = "CLINICAL_PRESETS = {"
p_end_tag = "\n# =============================================================================\n# SCORING & PATTERN DIFFERENTIATION ENGINE"

p_idx_start = diag_code.find(p_start_tag)
p_idx_end = diag_code.find(p_end_tag)

if p_idx_start != -1 and p_idx_end != -1:
    diag_code = diag_code[:p_idx_start] + presets_str + "\n\n" + diag_code[p_idx_end:]
    print("Replaced CLINICAL_PRESETS block successfully.")
else:
    print(f"Warning: Could not find preset tags: p_idx_start={p_idx_start}, p_idx_end={p_idx_end}")

# Update SYMPTOM_GROUPS
old_groups = idia.SYMPTOM_GROUPS
combined_groups = {}
for g_name, items in old_groups.items():
    cur_items = list(items)
    cur_keys = {k for k, _ in cur_items}
    if g_name in NEW_SYMPTOMS_TO_INJECT:
        for new_k, new_label in NEW_SYMPTOMS_TO_INJECT[g_name]:
            if new_k not in cur_keys:
                cur_items.append((new_k, new_label))
                cur_keys.add(new_k)
    combined_groups[g_name] = cur_items

groups_str = "SYMPTOM_GROUPS = " + pprint.pformat(
    combined_groups, indent=4, width=120, sort_dicts=False
)

g_start_tag = "SYMPTOM_GROUPS = {"
g_end_tag = "\nALL_SYMPTOM_KEYS = [k for sym_items in SYMPTOM_GROUPS.values() for k, _ in sym_items]"

g_idx_start = diag_code.find(g_start_tag)
g_idx_end = diag_code.find(g_end_tag)

if g_idx_start != -1 and g_idx_end != -1:
    diag_code = diag_code[:g_idx_start] + groups_str + "\n\n" + diag_code[g_idx_end:]
    print("Replaced SYMPTOM_GROUPS block successfully.")
else:
    print(f"Warning: Could not find symptom tags: g_idx_start={g_idx_start}, g_idx_end={g_idx_end}")

with open(diagnostics_path, "w", encoding="utf-8") as f:
    f.write(diag_code)

print("Successfully wrote updated modules/internal_diagnostics.py")
print("ALL CLINICAL UPDATES COMPLETED!")

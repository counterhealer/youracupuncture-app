import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from modules.cases_bank import CLINICAL_CASES

print(f"Total clinical cases: {len(CLINICAL_CASES)}")
for c in CLINICAL_CASES:
    qs = c.get('multiple_choice_questions', [])
    q_titles = [q.get('title', '') for q in qs]
    diag = c.get('standard_diagnosis', {})
    patterns = diag.get('patterns', [])
    principles = diag.get('treatment_principles', [])
    print(f"{c['id']} | {c['category']} | {c['title'][:40]}")
    print(f"   Pattern: {patterns}")
    print(f"   Principles: {principles}")
    print(f"   Current Qs: {len(qs)}")

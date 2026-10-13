import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules.exam_bank import load_all_questions, get_bank_stats, sample_exam_questions

questions = load_all_questions()
print(f"Total questions loaded: {len(questions)}")
assert len(questions) == 809, f"Expected 809 questions, got {len(questions)}"

stats = get_bank_stats()
print("\n--- Exam Bank Stats ---")
print(f"Total: {stats['total']}")
print(f"Categories ({len(stats['categories'])}): {stats['categories']}")
print(f"Difficulties: {stats['difficulties']}")
print(f"Exams: {stats['exams']}")

# Validate every single question schema
errors = []
for i, q in enumerate(questions):
    if not isinstance(q.get('id'), int):
        errors.append(f"Row {i} invalid ID: {q.get('id')}")
    if not q.get('question') or not isinstance(q['question'], str):
        errors.append(f"ID {q.get('id')} missing/invalid question string")
    if not isinstance(q.get('options'), list) or len(q['options']) != 4:
        errors.append(f"ID {q.get('id')} invalid options length: {len(q.get('options', []))}")
    if any(not opt or not isinstance(opt, str) for opt in q.get('options', [])):
        errors.append(f"ID {q.get('id')} has empty or non-string option")
    if q.get('answer') not in [0, 1, 2, 3]:
        errors.append(f"ID {q.get('id')} invalid answer index: {q.get('answer')}")
    if not q.get('explanation') or not isinstance(q['explanation'], str):
        errors.append(f"ID {q.get('id')} missing/invalid explanation")

if errors:
    print(f"\nFOUND {len(errors)} SCHEMA ERRORS:")
    for err in errors[:10]:
        print("  -", err)
    sys.exit(1)
else:
    print("\nAll 809 questions passed 100% schema validation!")

# Test sampling across multiple difficulties and categories
for diff in ["Easy", "Medium", "Hard"]:
    sampled = sample_exam_questions(count=10, difficulty=diff, seed=123)
    print(f"Sampled {len(sampled)} questions for difficulty '{diff}'")
    assert len(sampled) == 10

# Test sampling with categories
sample_cat = list(stats['categories'].keys())[0]
sampled_cat = sample_exam_questions(count=10, category=sample_cat, seed=123)
print(f"Sampled {len(sampled_cat)} questions for category '{sample_cat}'")

print("\nAll smoke tests PASSED successfully!")

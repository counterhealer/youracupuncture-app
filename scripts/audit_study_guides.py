import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from modules.study_guides import EMERGENCY_PROTOCOLS, TOP_50_POINTS_SAMPLE

print(f"Emergency protocols: {len(EMERGENCY_PROTOCOLS)}")
print(f"Top 50 points sample: {len(TOP_50_POINTS_SAMPLE)}")

# Check for typos
for em in EMERGENCY_PROTOCOLS:
    txt = " ".join(em.values())
    for typo in [r'\bth e\b', r'\binform of\b', r'\b1 fun\b', r'\b2 fun\b', r'\b4 fun\b', r'\bunconsciousness\b']:
        if re.search(typo, txt, re.IGNORECASE):
            print(f"Found typo {typo} in emergency protocol {em['emergency']}")

for pt, pearl in TOP_50_POINTS_SAMPLE:
    for typo in [r'\bth e\b', r'\binform of\b', r'\b1 fun\b', r'\b2 fun\b', r'\b4 fun\b']:
        if re.search(typo, pt + " " + pearl, re.IGNORECASE):
            print(f"Found typo {typo} in point {pt}")

print("Study guides text scan complete.")

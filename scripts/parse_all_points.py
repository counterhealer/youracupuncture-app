# -*- coding: utf-8 -*-
import json
import re

with open("static/acupoints_full.js", "r", encoding="utf-8") as f:
    text = f.read()

# It has JSON.parse(`[...]`)
idx1 = text.find("JSON.parse(`") + len("JSON.parse(`")
idx2 = text.rfind("`)")
raw_json = text[idx1:idx2]

print(f"Raw string length: {len(raw_json)}")

# Clean escapes that were in the JS template literal
# \\" -> \", \\n -> \n, etc.
cleaned = raw_json.replace('\\\\"', '\\"').replace('\\\\n', '\\n').replace('\\\\t', '\\t').replace('\\\\\\\\', '\\\\')

try:
    pts = json.loads(cleaned)
    print(f"Successfully loaded {len(pts)} points from acupuntura.com database!")
    with open("static/atlas_points_all.json", "w", encoding="utf-8") as out:
        json.dump(pts, out, ensure_ascii=False, indent=2)
    
    # Check meridians and counts
    from collections import Counter
    counts = Counter(p.get("meridian") for p in pts)
    print("Point counts per meridian:", dict(counts))
except Exception as e:
    print("Parse error:", e)
    pos = getattr(e, "pos", 0)
    print("Around error:", repr(cleaned[max(0, pos-50):min(len(cleaned), pos+50)]))

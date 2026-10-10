# -*- coding: utf-8 -*-
import json
import re

path = r"C:\Users\lingh\.gemini\antigravity\brain\1ec668e3-dfb3-44df-aca2-b468efdae81d\.system_generated\steps\1520\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find('[{"id":')
# find the ending }]
end_idx = text.rfind('}]')
if start_idx != -1 and end_idx != -1:
    json_chunk = text[start_idx : end_idx + 2]
    print(f"Extracted chunk length: {len(json_chunk)}")
    try:
        pts = json.loads(json_chunk)
        print(f"Direct parse successful! Loaded {len(pts)} points.")
        with open("static/raw_scraped_points.json", "w", encoding="utf-8") as f_out:
            json.dump(pts, f_out, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Initial parse error:", e)
        # JS template string evaluates \\ to \ and \" to " etc.
        # Let's decode unicode-escape or process string replacement:
        cleaned = json_chunk.replace('\\\\"', '\\"').replace('\\\\n', '\\n').replace('\\\\t', '\\t').replace('\\\\\\\\', '\\\\')
        try:
            pts = json.loads(cleaned)
            print(f"Cleaned parse successful! Loaded {len(pts)} points.")
            with open("static/raw_scraped_points.json", "w", encoding="utf-8") as f_out:
                json.dump(pts, f_out, ensure_ascii=False, indent=2)
        except Exception as e2:
            print("Second parse error:", e2)
            err_pos = getattr(e2, 'pos', 0)
            print("Around err_pos (-100 to +100):")
            print(repr(cleaned[max(0, err_pos-50) : min(len(cleaned), err_pos+100)]))
            print("Tail of cleaned:")
            print(repr(cleaned[-200:]))


else:
    print("Could not find start or end bracket.")

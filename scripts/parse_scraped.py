import re
with open(r"C:\Users\lingh\.gemini\antigravity\brain\1ec668e3-dfb3-44df-aca2-b468efdae81d\.system_generated\steps\1492\content.md", "r", encoding="utf-8") as f:
    text = f.read()

links = set(re.findall(r'href="(/assets/[^"]+)"', text))
for l in sorted(links):
    print(l)


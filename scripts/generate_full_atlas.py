# -*- coding: utf-8 -*-
"""Builder for modules/atlas.py implementing the Swiss-style Acupuncture Atlas from acupuntura.com/en/atlas/"""

import json
from pathlib import Path

# Load points from static/fitted_points.json and POINT_DICTIONARY from modules/tcm_points.py
with open("d:/TCM/acupuncture_app/static/fitted_points.json", "r", encoding="utf-8") as f:
    fitted_pts = json.load(f)

from modules.tcm_points import POINT_DICTIONARY

# We will build a comprehensive dictionary of 160+ points
# Map channel prefixes to canonical channel IDs
def get_channel_id(code):
    c = code.upper()
    if c.startswith("LU"): return "LU"
    if c.startswith("LI"): return "LI"
    if c.startswith("ST"): return "ST"
    if c.startswith("SP"): return "SP"
    if c.startswith("HT"): return "HT"
    if c.startswith("SI"): return "SI"
    if c.startswith("BL"): return "BL"
    if c.startswith("KI"): return "KI"
    if c.startswith("PC"): return "PC"
    if c.startswith(("TE", "SJ")): return "TE"
    if c.startswith("GB"): return "GB"
    if c.startswith(("LR", "LV")): return "LR"
    if c.startswith(("GV", "DU")): return "GV"
    if c.startswith(("CV", "REN")): return "CV"
    return "EX"

def format_code(code):
    c = code.upper()
    for ch in ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "TE", "SJ", "GB", "LR", "LV", "GV", "DU", "CV", "REN"]:
        if c.startswith(ch):
            num = c[len(ch):]
            if num.isdigit():
                norm_ch = "TE" if ch == "SJ" else ("LR" if ch == "LV" else ("GV" if ch == "DU" else ("CV" if ch == "REN" else ch)))
                return f"{norm_ch}-{num}"
    return c

print(f"Loaded {len(fitted_pts)} fitted points and {len(POINT_DICTIONARY)} dict points.")

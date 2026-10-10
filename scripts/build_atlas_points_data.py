# -*- coding: utf-8 -*-
"""Generate rich atlas_points.json from fitted_points.json and TCM clinical standards."""

import json
from pathlib import Path
from modules.tcm_points import POINT_DICTIONARY

with open("d:/TCM/acupuncture_app/static/fitted_points.json", "r", encoding="utf-8") as f:
    fitted = json.load(f)

# Anatomical regions mapping
REGION_MAP = {
    # Head & Neck
    "ST1": "Head", "ST2": "Head", "ST4": "Head", "ST6": "Head", "ST7": "Head", "ST8": "Head", "ST12": "Neck",
    "LI20": "Head", "LI15": "Upper Limb", "LI14": "Upper Limb", "LI11": "Upper Limb", "LI10": "Upper Limb", "LI4": "Upper Limb",
    "SI19": "Head", "SI12": "Back", "SI11": "Back", "SI8": "Upper Limb", "SI3": "Upper Limb", "SI1": "Upper Limb",
    "BL1": "Head", "BL2": "Head", "BL10": "Neck", "BL11": "Back", "BL12": "Back", "BL13": "Back", "BL14": "Back", "BL15": "Back", "BL17": "Back", "BL18": "Back", "BL20": "Back", "BL23": "Back", "BL25": "Back", "BL28": "Back", "BL32": "Back", "BL40": "Lower Limb", "BL52": "Back", "BL57": "Lower Limb", "BL60": "Lower Limb", "BL62": "Lower Limb", "BL67": "Lower Limb",
    "TE17": "Head", "TE21": "Head", "TE23": "Head", "TE14": "Upper Limb", "TE10": "Upper Limb", "TE5": "Upper Limb", "TE3": "Upper Limb", "TE4": "Upper Limb", "TE6": "Upper Limb",
    "GB1": "Head", "GB2": "Head", "GB8": "Head", "GB14": "Head", "GB20": "Neck", "GB21": "Neck", "GB24": "Chest", "GB25": "Abdomen", "GB30": "Lower Limb", "GB31": "Lower Limb", "GB34": "Lower Limb", "GB37": "Lower Limb", "GB39": "Lower Limb", "GB40": "Lower Limb", "GB41": "Lower Limb", "GB44": "Lower Limb",
    "GV14": "Neck", "GV15": "Neck", "GV16": "Neck", "GV20": "Head", "GV23": "Head", "GV24": "Head", "GV26": "Head", "GV9": "Back", "GV4": "Back", "GV1": "Back",
    "CV24": "Head", "CV22": "Neck", "CV17": "Chest", "CV14": "Abdomen", "CV12": "Abdomen", "CV9": "Abdomen", "CV8": "Abdomen", "CV6": "Abdomen", "CV4": "Abdomen", "CV3": "Abdomen",
    "LU1": "Chest", "LU2": "Chest", "LU5": "Upper Limb", "LU7": "Upper Limb", "LU9": "Upper Limb", "LU11": "Upper Limb",
    "HT1": "Upper Limb", "HT3": "Upper Limb", "HT5": "Upper Limb", "HT7": "Upper Limb", "HT9": "Upper Limb",
    "PC3": "Upper Limb", "PC6": "Upper Limb", "PC7": "Upper Limb", "PC8": "Upper Limb",
    "SP1": "Lower Limb", "SP3": "Lower Limb", "SP4": "Lower Limb", "SP6": "Lower Limb", "SP9": "Lower Limb", "SP10": "Lower Limb", "SP15": "Abdomen", "SP21": "Chest",
    "LR1": "Lower Limb", "LR2": "Lower Limb", "LR3": "Lower Limb", "LR5": "Lower Limb", "LR8": "Lower Limb", "LR13": "Abdomen", "LR14": "Chest",
    "KI1": "Lower Limb", "KI3": "Lower Limb", "KI6": "Lower Limb", "KI7": "Lower Limb", "KI10": "Lower Limb", "KI16": "Abdomen", "KI27": "Chest",
    "ST18": "Chest", "ST25": "Abdomen", "ST28": "Abdomen", "ST30": "Abdomen", "ST35": "Lower Limb", "ST36": "Lower Limb", "ST37": "Lower Limb", "ST38": "Lower Limb", "ST40": "Lower Limb", "ST44": "Lower Limb", "ST45": "Lower Limb",
    "YINTANG": "Head", "TAIYANG": "Head", "SISHENCONG": "Head", "ANMIAN": "Neck", "DINGCHUAN": "Neck", "HUATUOJIAJI": "Back", "YAOTONGXUE": "Upper Limb", "SIFENG": "Upper Limb", "HEDING": "Lower Limb", "DANNANGXUE": "Lower Limb", "LANWEIXUE": "Lower Limb", "ZIGONG": "Abdomen"
}

# Safety Level mapping
SAFETY_MAP = {
    # High danger points
    "LU1": ("danger", "PNEUMOTHORAX RISK: Puncture obliquely towards lateral chest 0.5–0.8 cun. Never puncture perpendicularly towards thoracic cavity."),
    "LU2": ("danger", "PNEUMOTHORAX RISK: Infraclavicular fossa. Oblique insertion laterally 0.5–0.8 cun. Do not puncture deeply."),
    "ST1": ("danger", "OCULAR PERFORATION RISK: Ask patient to look upwards. Push eyeball upward gently and insert needle perpendicularly slowly 0.5–1.0 cun along infraorbital ridge without thrusting or rotating."),
    "ST12": ("danger", "PNEUMOTHORAX & ARTERY RISK: Supraclavicular fossa. Perpendicular insertion strictly forbidden. Insert perpendicularly 0.3–0.5 cun along posterior border of clavicle."),
    "CV22": ("danger", "TRACHEA & AORTIC ARCH RISK: Puncture perpendicularly 0.2 cun, then direct needle tip downward along posterior sternum 0.5–1.0 cun. Do not insert deeply or laterally."),
    "GV15": ("danger", "MEDULLA OBLONGATA RISK: Puncture strictly perpendicular 0.5–0.8 cun. Never puncture upward or deeply towards foramen magnum!"),
    "GV16": ("danger", "MEDULLA OBLONGATA RISK: Puncture strictly perpendicular or slightly downward 0.5–0.8 cun. Deep upward needle angle strictly prohibited."),
    "BL1": ("danger", "RETROBULBAR HEMORRHAGE RISK: Ask patient to look laterally. Gently displace eyeball laterally with finger, puncture slowly along orbital wall 0.5–1.0 cun without manipulating."),
    "BL11": ("danger", "PNEUMOTHORAX RISK: Puncture obliquely towards spine 0.5–0.8 cun. Never puncture perpendicularly."),
    "BL13": ("danger", "PNEUMOTHORAX RISK: Puncture obliquely towards spine 0.5–0.8 cun. Deep perpendicular insertion strictly forbidden."),
    "BL15": ("danger", "PNEUMOTHORAX RISK: Oblique insertion towards vertebral column 0.5–0.8 cun."),
    "BL18": ("danger", "PNEUMOTHORAX & LIVER RISK: Oblique insertion towards spine 0.5–0.8 cun."),
    "BL20": ("danger", "PNEUMOTHORAX & SPLEEN RISK: Oblique insertion towards spine 0.5–0.8 cun."),
    "BL23": ("caution", "KIDNEY RISK: Puncture perpendicularly 0.5–1.0 cun. Deep perpendicular insertion in thin patients may puncture renal parenchyma."),
    "LR14": ("danger", "LIVER & PNEUMOTHORAX RISK: 6th intercostal space. Puncture obliquely along intercostal space 0.5–0.8 cun. Perpendicular insertion forbidden."),
    "SP21": ("danger", "PNEUMOTHORAX RISK: Mid-axillary line, 7th intercostal space. Oblique insertion 0.3–0.5 cun. Deep insertion risks pleura."),
    "GB20": ("caution", "VERTEBRAL ARTERY RISK: Direct needle tip toward opposite eye or tip of nose 0.8–1.2 cun. Do not angle upward toward brainstem."),
    "GB21": ("danger", "PNEUMOTHORAX & PREGNANCY: Apex of lung lies beneath trapezius. Oblique posterior insertion 0.5–0.8 cun. CONTRAINDICATED IN PREGNANCY (induces labor)."),
    "LI4": ("caution", "CONTRAINDICATED IN PREGNANCY: Strongly stimulates uterine contractions and descends Qi. Deep insertion 0.5–1.0 cun."),
    "SP6": ("caution", "CONTRAINDICATED IN PREGNANCY: Descends Qi and induces labor. Perpendicular insertion 1.0–1.5 cun."),
    "BL60": ("caution", "CONTRAINDICATED IN PREGNANCY: Strong descending action. Perpendicular insertion 0.5–1.0 cun."),
    "BL67": ("caution", "CONTRAINDICATED IN PREGNANCY except for correcting breech presentation with moxibustion."),
    "CV8": ("danger", "NEEDLING STRICTLY FORBIDDEN: Umbilicus. Moxibustion with salt or ginger only."),
    "ST36": ("caution", "Avoid anterior tibial artery with deep insertion. Perpendicular insertion 1.0–1.5 cun."),
    "PC6": ("caution", "Avoid median nerve trunk. Puncture perpendicularly 0.5–1.0 cun. Electric sensation into fingers indicates nerve contact—withdraw slightly.")
}

# Standard needle depths
DEPTH_MAP = {
    "LU1": (0.5, 0.8, 2.0, "Oblique lateral insertion 0.5–0.8 cun."),
    "LU5": (0.5, 1.0, 2.0, "Perpendicular insertion 0.5–1.0 cun."),
    "LU7": (0.5, 0.8, 1.5, "Oblique proximal insertion 0.5–0.8 cun."),
    "LU9": (0.3, 0.5, 1.0, "Perpendicular insertion 0.3–0.5 cun, avoid radial artery."),
    "LU11": (0.1, 0.2, 0.5, "Prick for bleeding or shallow puncture 0.1 cun."),
    "LI4": (0.5, 1.0, 2.0, "Perpendicular insertion 0.5–1.0 cun."),
    "LI11": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "LI15": (0.8, 1.5, 2.5, "Perpendicular or oblique-inferior insertion 0.8–1.5 cun."),
    "LI20": (0.3, 0.5, 1.0, "Oblique upward or transverse insertion 0.3–0.5 cun."),
    "ST36": (1.0, 1.5, 3.0, "Perpendicular insertion 1.0–1.5 cun."),
    "ST40": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "ST44": (0.3, 0.5, 1.0, "Perpendicular or oblique insertion 0.3–0.5 cun."),
    "SP6": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "SP9": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "SP10": (1.0, 1.5, 2.5, "Perpendicular or oblique insertion 1.0–1.5 cun."),
    "HT7": (0.3, 0.5, 1.0, "Perpendicular insertion 0.3–0.5 cun."),
    "SI3": (0.5, 0.8, 1.5, "Perpendicular insertion 0.5–0.8 cun towards heart of palm."),
    "BL23": (0.8, 1.2, 2.5, "Perpendicular or slightly oblique insertion 0.8–1.2 cun."),
    "BL40": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun, or prick to bleed."),
    "KI3": (0.5, 1.0, 1.8, "Perpendicular insertion 0.5–1.0 cun."),
    "PC6": (0.5, 1.0, 2.0, "Perpendicular insertion 0.5–1.0 cun."),
    "TE5": (0.5, 1.0, 2.0, "Perpendicular insertion 0.5–1.0 cun."),
    "GB20": (0.8, 1.2, 2.5, "Puncture toward opposite eye or tip of nose 0.8–1.2 cun."),
    "GB34": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "LR3": (0.5, 0.8, 1.5, "Perpendicular or oblique proximal insertion 0.5–0.8 cun."),
    "GV14": (0.5, 1.0, 2.0, "Puncture obliquely upward 0.5–1.0 cun."),
    "GV20": (0.5, 0.8, 1.5, "Subcutaneous transverse insertion 0.5–0.8 cun."),
    "CV4": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun after emptying bladder."),
    "CV12": (1.0, 1.5, 2.5, "Perpendicular insertion 1.0–1.5 cun."),
    "YINTANG": (0.3, 0.5, 1.0, "Transverse downward pinch-skin puncture 0.3–0.5 cun."),
    "TAIYANG": (0.3, 0.5, 1.0, "Perpendicular or transverse posterior insertion 0.3–0.5 cun, or prick to bleed.")
}

# Format code to include hyphen (LU1 -> LU-1)
def format_code(c):
    c = c.upper()
    for prefix in ["LU", "LI", "ST", "SP", "HT", "SI", "BL", "KI", "PC", "TE", "SJ", "GB", "LR", "LV", "GV", "DU", "CV", "REN"]:
        if c.startswith(prefix):
            num = c[len(prefix):]
            if num.isdigit():
                norm = "TE" if prefix == "SJ" else ("LR" if prefix == "LV" else ("GV" if prefix == "DU" else ("CV" if prefix == "REN" else prefix)))
                return f"{norm}-{num}"
    return c

print("Helper dictionaries ready.")

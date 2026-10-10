"""Interactive 3D Acupuncture Meridian and Acupoint Medical Statue Viewer.

Renders an authentic, continuous 3D sculpted medical human statue (inspired by
the classical Song Dynasty Imperial Acupuncture Bronze Statue / 针灸铜人,
Zhenjiu Tongren) with:
- Seamless, organic 3D anatomical human mesh loaded via WebGL & GLTF (zero blocky shapes)
- Fine, crisp, diagram-like meridian lines (0.015 radius) and pinpoint acupoint markers (0.038 radius)
- Authentic medical statue finishes:
  1. 🥉 Imperial Cast Bronze (针灸铜人) - Classic TCM bronze statue with warm metallic patina
  2. 🏛️ Medical Alabaster / Ivory - Museum anatomical sculpture
  3. 🧑 Anatomical Flesh Silicone - Medical training mannequin
  4. 🌑 Obsidian Museum Plinth - Sleek high-contrast dark sculpture
- Classical multi-tiered museum plinth/pedestal with engraved plaque:
  '北宋天圣针灸铜人 • Imperial Medical Statue'
- Complete 14 major meridians with canonical Six-Channel nomenclature:
  e.g. Lung Channel of Hand-Taiyin (手太阴肺经), Stomach Channel of Foot-Yangming (足阳明胃经)
- All 122 high-yield acupoints mapped precisely to the surface of the statue
- Orbit, zoom, pan, and spin controls
- Interactive meridian highlighting on click and dropdown
- Click-to-inspect point cards with bilingual names, Cun locations, actions, and safety cautions
- Instant search bar and standard anatomical camera presets
"""

import json
import base64
from pathlib import Path
from typing import Dict, Any

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
GLB_PATH = STATIC_DIR / "mannequin.glb"
FITTED_POINTS_PATH = STATIC_DIR / "fitted_points.json"

_CACHED_GLB_B64 = None

def get_glb_base64() -> str:
    """Read and cache mannequin.glb as base64 string."""
    global _CACHED_GLB_B64
    if _CACHED_GLB_B64 is None:
        if GLB_PATH.exists():
            with open(GLB_PATH, "rb") as f:
                _CACHED_GLB_B64 = base64.b64encode(f.read()).decode("ascii")
        else:
            _CACHED_GLB_B64 = ""
    return _CACHED_GLB_B64


def get_meridians_data() -> Dict[str, Any]:
    """Return complete dataset of 14 meridians, extra points, and surface-fitted coordinates."""
    points_dict = {}
    if FITTED_POINTS_PATH.exists():
        try:
            with open(FITTED_POINTS_PATH, "r", encoding="utf-8") as f:
                points_dict = json.load(f)
        except Exception:
            pass

    return {
        "meridians": [
            {
                "id": "LU",
                "name": "Lung Channel of Hand-Taiyin",
                "chinese": "手太阴肺经",
                "division": "Hand-Taiyin (手太阴)",
                "fullName": "Lung Channel of Hand-Taiyin (手太阴肺经)",
                "element": "Metal",
                "time": "3:00 AM – 5:00 AM",
                "color": "#38bdf8",
                "description": "Originates in middle burner, descends to connect with Large Intestine, ascends through Lung, emerges at LU1 (Zhongfu), runs down antero-lateral arm to radial tip of thumb (LU11 Shaoshang).",
                "points": ["LU1", "LU5", "LU7", "LU9", "LU11"]
            },
            {
                "id": "LI",
                "name": "Large Intestine Channel of Hand-Yangming",
                "chinese": "手阳明大肠经",
                "division": "Hand-Yangming (手阳明)",
                "fullName": "Large Intestine Channel of Hand-Yangming (手阳明大肠经)",
                "element": "Metal",
                "time": "5:00 AM – 7:00 AM",
                "color": "#fb923c",
                "description": "Originates at radial tip of index finger (LI1 Shangyang), ascends lateral border of arm through LI4 Hegu and LI11 Quchi, crosses shoulder at LI15, traverses neck to opposite ala nasi at LI20 Yingxiang.",
                "points": ["LI1", "LI4", "LI10", "LI11", "LI15", "LI20"]
            },
            {
                "id": "ST",
                "name": "Stomach Channel of Foot-Yangming",
                "chinese": "足阳明胃经",
                "division": "Foot-Yangming (足阳明)",
                "fullName": "Stomach Channel of Foot-Yangming (足阳明胃经)",
                "element": "Earth",
                "time": "7:00 AM – 9:00 AM",
                "color": "#eab308",
                "description": "Originates infraorbital rim at ST1 Chengqi, circles mouth, ascends to forehead corner ST8 Touwei, descends neck (ST12 Quepen), chest along mamillary line (ST18 Rugen), anterior abdomen 2 cun lateral to midline (ST25 Tianshu, ST28 Shuidao, ST30 Qichong), down anterolateral leg through ST36 Zusanli and ST40 Fenglong, terminates at lateral 2nd toe (ST45 Lidui).",
                "points": ["ST1", "ST2", "ST6", "ST7", "ST8", "ST12", "ST18", "ST25", "ST28", "ST30", "ST35", "ST36", "ST38", "ST40", "ST44", "ST45"]
            },
            {
                "id": "SP",
                "name": "Spleen Channel of Foot-Taiyin",
                "chinese": "足太阴脾经",
                "division": "Foot-Taiyin (足太阴)",
                "fullName": "Spleen Channel of Foot-Taiyin (足太阴脾经)",
                "element": "Earth",
                "time": "9:00 AM – 11:00 AM",
                "color": "#f59e0b",
                "description": "Originates medial big toe (SP1 Yinbai), runs along medial foot and leg through SP4 Gongsun, SP6 Sanyinjiao, SP9 Yinlingquan, crosses inner thigh at SP10 Xuehai, enters abdomen (4 cun lateral at SP15), terminates at SP21 Dabao on mid-axillary line.",
                "points": ["SP1", "SP3", "SP4", "SP6", "SP9", "SP10", "SP15", "SP21"]
            },
            {
                "id": "HT",
                "name": "Heart Channel of Hand-Shaoyin",
                "chinese": "手少阴心经",
                "division": "Hand-Shaoyin (手少阴)",
                "fullName": "Heart Channel of Hand-Shaoyin (手少阴心经)",
                "element": "Fire",
                "time": "11:00 AM – 1:00 PM",
                "color": "#ef4444",
                "description": "Originates in Heart, emerges from axilla at HT1 Jiquan, travels down medial-posterior arm through HT3 Shaohai, transverse wrist crease at HT7 Shenmen, terminates at radial corner of little finger nail (HT9 Shaochong).",
                "points": ["HT1", "HT3", "HT5", "HT6", "HT7", "HT9"]
            },
            {
                "id": "SI",
                "name": "Small Intestine Channel of Hand-Taiyang",
                "chinese": "手太阳小肠经",
                "division": "Hand-Taiyang (手太阳)",
                "fullName": "Small Intestine Channel of Hand-Taiyang (手太阳小肠经)",
                "element": "Fire",
                "time": "1:00 PM – 3:00 PM",
                "color": "#f43f5e",
                "description": "Originates at ulnar little finger (SI1 Shaoze), travels ulnar hand (SI3 Houxi), elbow groove (SI8 Xiaohai), posterior shoulder (SI9, SI11 Tianzong), ascends lateral neck (SI16 Tianchuang) to enter anterior tragus of ear at SI19 Tinggong.",
                "points": ["SI1", "SI3", "SI8", "SI9", "SI11", "SI16", "SI19"]
            },
            {
                "id": "BL",
                "name": "Bladder Channel of Foot-Taiyang",
                "chinese": "足太阳膀胱经",
                "division": "Foot-Taiyang (足太阳)",
                "fullName": "Bladder Channel of Foot-Taiyang (足太阳膀胱经)",
                "element": "Water",
                "time": "3:00 PM – 5:00 PM",
                "color": "#2563eb",
                "description": "Longest channel in body (67 points). Originates inner canthus (BL1 Jingming), crosses vertex, descends down occiput (BL10), splits into inner 1.5 cun line (Back-Shu points BL11-BL23) and outer 3.0 cun line (BL52), down posterior leg (BL40 Weizhong, BL57 Chengshan, BL60 Kunlun) to little toe (BL67 Zhiyin).",
                "points": ["BL1", "BL2", "BL10", "BL11", "BL13", "BL15", "BL18", "BL20", "BL23", "BL52", "BL40", "BL57", "BL60", "BL62", "BL67"]
            },
            {
                "id": "KI",
                "name": "Kidney Channel of Foot-Shaoyin",
                "chinese": "足少阴肾经",
                "division": "Foot-Shaoyin (足少阴)",
                "fullName": "Kidney Channel of Foot-Shaoyin (足少阴肾经)",
                "element": "Water",
                "time": "5:00 PM – 7:00 PM",
                "color": "#6366f1",
                "description": "Originates under sole of foot (KI1 Yongquan), circles medial malleolus (KI3 Taixi, KI6 Zhaohai), ascends posterior-medial lower leg (KI7 Fuliu), inner knee (KI10), up lower abdomen (0.5 cun lateral to midline) and chest.",
                "points": ["KI1", "KI3", "KI6", "KI7", "KI10"]
            },
            {
                "id": "PC",
                "name": "Pericardium Channel of Hand-Jueyin",
                "chinese": "手厥阴心包经",
                "division": "Hand-Jueyin (手厥阴)",
                "fullName": "Pericardium Channel of Hand-Jueyin (手厥阴心包经)",
                "element": "Fire",
                "time": "7:00 PM – 9:00 PM",
                "color": "#ec4899",
                "description": "Originates in chest, descends across diaphragm, emerges at PC1 near nipple, descends down middle anterior arm through PC3 Quze, forearm between tendons (PC6 Neiguan), wrist crease (PC7 Daling), palm (PC8 Laogong) to middle finger tip (PC9 Zhongchong).",
                "points": ["PC3", "PC6", "PC7", "PC8", "PC9"]
            },
            {
                "id": "SJ",
                "name": "San Jiao Channel of Hand-Shaoyang",
                "chinese": "手少阳三焦经",
                "division": "Hand-Shaoyang (手少阳)",
                "fullName": "San Jiao (Triple Energizer) Channel of Hand-Shaoyang (手少阳三焦经)",
                "element": "Fire",
                "time": "9:00 PM – 11:00 PM",
                "color": "#f97316",
                "description": "Originates at ulnar ring finger (SJ1 Guanchong), travels dorsum of hand (SJ3 Zhongzhu), dorsal forearm between bones (SJ5 Waiguan, SJ6 Zhigou), lateral shoulder (SJ14 Jianliao), behind ear (SJ17 Yifeng), encircles ear to lateral end of eyebrow (SJ23 Sizhukong).",
                "points": ["SJ1", "SJ3", "SJ5", "SJ6", "SJ14", "SJ17", "SJ21"]
            },
            {
                "id": "GB",
                "name": "Gallbladder Channel of Foot-Shaoyang",
                "chinese": "足少阳胆经",
                "division": "Foot-Shaoyang (足少阳)",
                "fullName": "Gallbladder Channel of Foot-Shaoyang (足少阳胆经)",
                "element": "Wood",
                "time": "11:00 PM – 1:00 AM",
                "color": "#10b981",
                "description": "Originates outer canthus (GB1 Tongziliao), zigzags across temple and skull (GB8, GB14, GB20 Fengchi), traverses trapezius (GB21 Jianjing), lateral flank (GB26 Daimai), buttock (GB30 Huantiao), down lateral thigh and leg (GB34 Yanglingquan, GB39 Xuanzhong), terminates at 4th toe (GB44 Zuqiaoyin).",
                "points": ["GB1", "GB2", "GB8", "GB14", "GB20", "GB21", "GB26", "GB30", "GB34", "GB39", "GB41", "GB44"]
            },
            {
                "id": "LV",
                "name": "Liver Channel of Foot-Jueyin",
                "chinese": "足厥阴肝经",
                "division": "Foot-Jueyin (足厥阴)",
                "fullName": "Liver Channel of Foot-Jueyin (足厥阴肝经)",
                "element": "Wood",
                "time": "1:00 AM – 3:00 AM",
                "color": "#059669",
                "description": "Originates lateral big toe (LV1 Dadun), ascends dorsum of foot (LV2 Xingjian, LV3 Taichong), medial lower leg (LV5 Ligou, LV8 Ququan), circles external genitalia, enters lower abdomen to tip of 11th rib (LV13 Zhangmen) and 6th intercostal space (LV14 Qimen).",
                "points": ["LV1", "LV2", "LV3", "LV5", "LV8", "LV13", "LV14"]
            },
            {
                "id": "DU",
                "name": "Governing Vessel • Du Mai",
                "chinese": "督脉",
                "division": "Sea of Yang Vessels (阳脉之海)",
                "fullName": "Governing Vessel • Du Mai (督脉)",
                "element": "Yang",
                "time": "Flows continuously",
                "color": "#8b5cf6",
                "description": "Originates in pelvic cavity, emerges at perineum (DU1 Changqiang), ascends posterior midline of spine through DU4 Mingmen, DU9 Zhiyang, DU14 Dazhui, crosses nape (DU15, DU16 Fengfu), over skull vertex (DU20 Baihui), down forehead to philtrum (DU26 Shuigou).",
                "points": ["DU1", "DU4", "DU9", "DU14", "DU15", "DU16", "DU20", "DU24", "DU26"]
            },
            {
                "id": "REN",
                "name": "Conception Vessel • Ren Mai",
                "chinese": "任脉",
                "division": "Sea of Yin Vessels (阴脉之海)",
                "fullName": "Conception Vessel • Ren Mai (任脉)",
                "element": "Yin",
                "time": "Flows continuously",
                "color": "#14b8a6",
                "description": "Originates in pelvic cavity, emerges at perineum, ascends anterior midline of abdomen through REN3 Zhongji, REN4 Guanyuan, REN6 Qihai, umbilicus (REN8 Shenque), middle cavity (REN12 Zhongwan), chest center (REN17 Shanzhong), throat (REN22 Tiantu) to chin groove (REN24 Chengjiang).",
                "points": ["REN3", "REN4", "REN6", "REN8", "REN12", "REN17", "REN22", "REN24"]
            },
            {
                "id": "EX",
                "name": "Extraordinary Acupoints (Qi Xue)",
                "chinese": "经外奇穴",
                "division": "Special Empirical Points (经外奇穴)",
                "fullName": "Extraordinary Acupoints (经外奇穴)",
                "element": "Special",
                "time": "High clinical yield",
                "color": "#e11d48",
                "description": "Specific classical empirical acupoints not situated on the 14 primary channels, possessing profound therapeutic actions confirmed through clinical history.",
                "points": ["YINTANG", "TAIYANG", "SISHENCONG", "DINGCHUAN", "HUATUOJIAJI", "YAOTONGXUE", "SIFENG", "HEDING", "DANNANGXUE", "LANWEIXUE", "ZIGONG"]
            }
        ],
        "points": points_dict
    }


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>3D Acupuncture Meridian & Acupoint Medical Statue</title>
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    body, html {
        width: 100%;
        height: 100%;
        overflow: hidden;
        background: #090d16;
        color: #f8fafc;
    }
    #canvas-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }
    /* Top Toolbar */
    .top-toolbar {
        position: absolute;
        top: 10px;
        left: 10px;
        right: 10px;
        z-index: 10;
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
        background: rgba(15, 23, 42, 0.94);
        backdrop-filter: blur(12px);
        padding: 8px 12px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
    }
    .select-label {
        font-size: 0.82rem;
        font-weight: 700;
        color: #0f766e;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    select, input {
        background: #1e293b;
        color: #f8fafc;
        border: 1px solid #334155;
        padding: 6px 10px;
        border-radius: 8px;
        font-size: 0.80rem;
        outline: none;
        transition: border 0.15s ease;
    }
    select:focus, input:focus {
        border-color: #0f766e;
    }
    .btn {
        background: #1e293b;
        color: #f1f5f9;
        border: 1px solid #334155;
        padding: 6px 10px;
        border-radius: 8px;
        font-size: 0.80rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s ease;
    }
    .btn:hover {
        background: #334155;
        border-color: #64748b;
    }
    /* Statue Plaque on Pedestal */
    .statue-plaque {
        position: absolute;
        bottom: 12px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
        background: rgba(24, 24, 27, 0.88);
        border: 1px solid rgba(217, 119, 6, 0.4);
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.74rem;
        color: #fcd34d;
        letter-spacing: 0.5px;
        pointer-events: none;
        box-shadow: 0 4px 14px rgba(0,0,0,0.4);
    }
    /* Point Info Drawer */
    #info-card {
        position: absolute;
        bottom: 14px;
        left: 14px;
        width: 380px;
        max-width: calc(100% - 28px);
        max-height: 52%;
        overflow-y: auto;
        background: rgba(15, 23, 42, 0.96);
        backdrop-filter: blur(14px);
        border: 1.5px solid rgba(15, 118, 110, 0.55);
        border-radius: 14px;
        padding: 16px 18px;
        z-index: 20;
        box-shadow: 0 12px 40px rgba(0,0,0,0.65);
        display: none;
    }
    #info-card.visible {
        display: block;
        animation: slideUp 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(16px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .close-btn {
        position: absolute;
        top: 10px;
        right: 12px;
        background: none;
        border: none;
        color: #94a3b8;
        font-size: 1.25rem;
        cursor: pointer;
        padding: 4px;
        line-height: 1;
    }
    .close-btn:hover {
        color: #f8fafc;
    }
    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 700;
        margin-right: 4px;
        margin-bottom: 6px;
    }
    .badge-cat {
        background: #0f766e;
        color: #ccfbf1;
    }
    .badge-meridian {
        background: #1e293b;
        color: #38bdf8;
        border: 1px solid #0284c7;
    }
    .info-title {
        font-size: 1.12rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 6px;
        padding-right: 24px;
    }
    .info-section {
        margin-top: 8px;
        font-size: 0.82rem;
        line-height: 1.45;
        color: #cbd5e1;
    }
    .info-label {
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        color: #94a3b8;
        letter-spacing: 0.5px;
        margin-bottom: 2px;
    }
    .caution-box {
        margin-top: 10px;
        background: rgba(185, 28, 28, 0.18);
        border: 1px solid #ef4444;
        border-radius: 8px;
        padding: 8px 10px;
        color: #fca5a5;
        font-size: 0.78rem;
        line-height: 1.4;
    }
    /* Hover Tooltip */
    #tooltip {
        position: absolute;
        z-index: 30;
        background: rgba(15, 23, 42, 0.94);
        color: #38bdf8;
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
        pointer-events: none;
        border: 1px solid rgba(56, 189, 248, 0.45);
        display: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }
    /* Quick Legend Overlay */
    .legend-box {
        position: absolute;
        top: 72px;
        right: 12px;
        z-index: 10;
        background: rgba(15, 23, 42, 0.88);
        backdrop-filter: blur(8px);
        padding: 10px 12px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.78rem;
        max-width: 250px;
        display: none;
    }
    @media (min-width: 760px) {
        .legend-box { display: block; }
    }
    /* Controls hint */
    .controls-hint {
        position: absolute;
        bottom: 12px;
        right: 12px;
        z-index: 10;
        background: rgba(15, 23, 42, 0.80);
        padding: 5px 10px;
        border-radius: 8px;
        font-size: 0.72rem;
        color: #94a3b8;
        pointer-events: none;
    }
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
</head>
<body>

<div id="canvas-container"></div>

<!-- Top Navigation Toolbar -->
<div class="top-toolbar">
    <span class="select-label">⚡ Meridian:</span>
    <select id="meridian-select" style="max-width: 230px;">
        <option value="ALL">✨ All 14 Meridians & Extra Points</option>
    </select>

    <span class="select-label" style="margin-left: 4px;">🗿 Statue:</span>
    <select id="statue-select">
        <option value="bronze">🥉 Imperial Bronze (针灸铜人)</option>
        <option value="alabaster">🏛️ Medical Alabaster / Ivory</option>
        <option value="flesh">🧑 Anatomical Flesh</option>
        <option value="obsidian">🌑 Museum Obsidian</option>
    </select>

    <span class="select-label" style="margin-left: 4px;">📏 Size:</span>
    <select id="size-select">
        <option value="fine" selected>✨ Diagram (Fine)</option>
        <option value="compact">📍 Compact</option>
        <option value="bold">🔴 Bold</option>
    </select>

    <span class="select-label" style="margin-left: 4px;">🔍 Jump:</span>
    <input type="text" id="point-search" placeholder="e.g. ST36, LI4, Hegu..." style="width: 120px;">

    <div style="display: flex; gap: 4px; margin-left: auto;">
        <button class="btn" id="btn-front" title="Front View">Front</button>
        <button class="btn" id="btn-back" title="Back View">Back</button>
        <button class="btn" id="btn-left" title="Left Lateral">Left</button>
        <button class="btn" id="btn-right" title="Right Lateral">Right</button>
        <button class="btn" id="btn-reset" title="Reset View">🔄 Reset</button>
    </div>
</div>

<!-- Statue Museum Plaque -->
<div class="statue-plaque">
    🏛️ 北宋天圣针灸铜人 • Zhenjiu Tongren Medical Statue
</div>

<!-- Hover Tooltip -->
<div id="tooltip"></div>

<!-- Point Information Card Drawer -->
<div id="info-card">
    <button class="close-btn" id="close-card-btn">&times;</button>
    <div id="card-badges"></div>
    <div class="info-title" id="card-title">Point Name</div>
    <div class="info-section">
        <div class="info-label">📍 Precise Location</div>
        <div id="card-location">Location text</div>
    </div>
    <div class="info-section">
        <div class="info-label">🩺 Clinical Actions & Indications</div>
        <div id="card-actions">Actions text</div>
    </div>
    <div class="caution-box" id="card-caution">
        <strong>⚠️ Needling & Safety Caution:</strong><br>
        <span id="card-caution-text">Safety text</span>
    </div>
</div>

<!-- Quick Legend / Meridian Info -->
<div class="legend-box" id="meridian-info-panel">
    <strong style="color: #38bdf8;" id="meridian-panel-name">14 Meridians Active</strong>
    <p style="font-size: 0.74rem; color: #94a3b8; margin-top: 4px;" id="meridian-panel-desc">
        All 12 primary channels (Hand/Foot Yin/Yang) + Du Mai & Ren Mai active. Click any point marker or meridian pathway to inspect.
    </p>
</div>

<!-- Touch & Orbit Hint -->
<div class="controls-hint">
    🖱️ Drag: Rotate • Scroll: Zoom • Click: Inspect Points & Meridians
</div>

<script>
// Load Datasets
const TCM_DATA = __TCM_DATA_JSON__;
const GLB_BASE64 = "__GLB_BASE64__";

// Three.js Core Variables
let scene, camera, renderer, controls;
let container = document.getElementById('canvas-container');
let pointMeshes = {};
let meridianLines = {};
let statueGroup;
let statueMeshes = [];
let raycaster = new THREE.Raycaster();
let mouse = new THREE.Vector2();
let selectedPointCode = null;
let currentMeridianFilter = 'ALL';
let currentScaleFactor = 1.0;

// Statue Finish Palettes (Genuine Classical Medical Statue Materials)
const STATUE_PALETTES = {
    bronze: {
        color: 0xb87333,       // Antique Imperial Cast Bronze (针灸铜人)
        roughness: 0.35,
        metalness: 0.75,
        emissive: 0x241406,
        emissiveIntensity: 0.22
    },
    alabaster: {
        color: 0xf4ece1,       // Classic Medical School Alabaster / Ivory Anatomical Model
        roughness: 0.48,
        metalness: 0.06,
        emissive: 0x1a1815,
        emissiveIntensity: 0.15
    },
    flesh: {
        color: 0xdca882,       // Anatomical Silicone Medical Training Mannequin
        roughness: 0.62,
        metalness: 0.04,
        emissive: 0x180f08,
        emissiveIntensity: 0.12
    },
    obsidian: {
        color: 0x27272a,       // Museum Dark Obsidian Display Finish
        roughness: 0.65,
        metalness: 0.25,
        emissive: 0x09090b,
        emissiveIntensity: 0.10
    }
};

let currentStatueMat = new THREE.MeshStandardMaterial({
    color: STATUE_PALETTES.bronze.color,
    roughness: STATUE_PALETTES.bronze.roughness,
    metalness: STATUE_PALETTES.bronze.metalness,
    emissive: STATUE_PALETTES.bronze.emissive,
    emissiveIntensity: STATUE_PALETTES.bronze.emissiveIntensity,
    transparent: false,
    opacity: 1.0,
    side: THREE.FrontSide
});

function setStatueStyle(type) {
    const pal = STATUE_PALETTES[type] || STATUE_PALETTES.bronze;
    currentStatueMat.color.setHex(pal.color);
    currentStatueMat.roughness = pal.roughness;
    currentStatueMat.metalness = pal.metalness;
    currentStatueMat.emissive.setHex(pal.emissive);
    currentStatueMat.emissiveIntensity = pal.emissiveIntensity;
    currentStatueMat.needsUpdate = true;
    statueMeshes.forEach(m => {
        m.material = currentStatueMat;
    });
}

function setSizeScale(mode) {
    if (mode === 'fine') {
        currentScaleFactor = 1.0;
    } else if (mode === 'compact') {
        currentScaleFactor = 1.35;
    } else if (mode === 'bold') {
        currentScaleFactor = 1.85;
    }

    scene.traverse(obj => {
        if (obj.userData.isPoint) {
            obj.scale.set(currentScaleFactor, currentScaleFactor, currentScaleFactor);
        }
        if (obj.userData.isMeridian) {
            const s = currentScaleFactor;
            obj.scale.set(s, s, s);
        }
    });
}

function base64ToArrayBuffer(base64) {
    const binaryString = window.atob(base64);
    const len = binaryString.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
        bytes[i] = binaryString.charCodeAt(i);
    }
    return bytes.buffer;
}

// Initialize Three.js Scene
function initScene() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x090d16);
    scene.fog = new THREE.FogExp2(0x090d16, 0.035);

    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 0, 15);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(renderer.domElement);

    // Orbit Controls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.minDistance = 3.0;
    controls.maxDistance = 25;
    controls.target.set(0, 0, 0);

    // Museum Studio Lighting
    const ambientLight = new THREE.HemisphereLight(0xffedd5, 0x1e293b, 0.70);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xfff7ed, 1.25);
    keyLight.position.set(6, 14, 10);
    keyLight.castShadow = true;
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0xdbeafe, 0.65);
    fillLight.position.set(-8, 6, 8);
    scene.add(fillLight);

    const rimLight = new THREE.DirectionalLight(0xfef3c7, 0.90);
    rimLight.position.set(0, 10, -12);
    scene.add(rimLight);

    // Build Statue and Acupoint Networks
    createMedicalStatue();
    createMeridiansAndPoints();
    populateUI();

    // Event Listeners
    window.addEventListener('resize', onWindowResize);
    renderer.domElement.addEventListener('mousemove', onMouseMove);
    renderer.domElement.addEventListener('click', onClick);
    renderer.domElement.addEventListener('touchstart', onTouchStart, { passive: false });

    animate();
}

// Build Continuous 3D Sculpted Medical Statue & Plinth
function createMedicalStatue() {
    statueGroup = new THREE.Group();

    // Multi-tiered Classical Museum Pedestal Plinth
    const pedestalMat = new THREE.MeshStandardMaterial({
        color: 0x18181b,
        roughness: 0.65,
        metalness: 0.35
    });
    // Lower Base
    const base1 = new THREE.Mesh(new THREE.CylinderGeometry(2.3, 2.5, 0.22, 48), pedestalMat);
    base1.position.set(0, -6.36, 0);
    base1.receiveShadow = true;
    statueGroup.add(base1);
    // Upper Tier
    const base2 = new THREE.Mesh(new THREE.CylinderGeometry(2.0, 2.2, 0.16, 48), pedestalMat);
    base2.position.set(0, -6.18, 0);
    base2.receiveShadow = true;
    statueGroup.add(base2);

    // Load Seamless Sculpted Human Mannequin Mesh via GLTFLoader
    try {
        const buffer = base64ToArrayBuffer(GLB_BASE64);
        const loader = new THREE.GLTFLoader();
        loader.parse(buffer, '', function(gltf) {
            const model = gltf.scene;
            model.scale.set(6.46, 6.46, 6.46);
            model.position.set(0, -6.25, -0.18);

            model.traverse(function(child) {
                if (child.isMesh) {
                    child.material = currentStatueMat;
                    child.castShadow = true;
                    child.receiveShadow = true;
                    child.renderOrder = 0;
                    child.userData = { isStatueBody: true };
                    statueMeshes.push(child);
                }
            });
            statueGroup.add(model);
        }, function(error) {
            console.error('Error parsing 3D statue GLB:', error);
        });
    } catch (err) {
        console.error('Error decoding statue base64:', err);
    }

    scene.add(statueGroup);
}

// Build 3D Meridians and Points from Dataset (Fine Diagram Sizing)
function createMeridiansAndPoints() {
    // Crisp, small diagram point geometry (0.038 radius)
    const pointGeom = new THREE.SphereGeometry(0.038, 16, 16);
    // Invisible hit proxy sphere (0.12 radius) so clicking tiny dots remains easy
    const hitGeom = new THREE.SphereGeometry(0.12, 8, 8);
    const hitMat = new THREE.MeshBasicMaterial({ visible: false });

    // Create Points
    for (const [key, pt] of Object.entries(TCM_DATA.points)) {
        const [x, y, z] = pt.pos;
        
        // Find parent meridian color
        let merColor = 0x38bdf8;
        for (const m of TCM_DATA.meridians) {
            if (m.points.includes(key)) {
                merColor = parseInt(m.color.replace('#', '0x'));
                break;
            }
        }

        const mat = new THREE.MeshStandardMaterial({
            color: merColor,
            emissive: merColor,
            emissiveIntensity: 0.95,
            roughness: 0.15,
            metalness: 0.25,
            polygonOffset: true,
            polygonOffsetFactor: -1.0,
            polygonOffsetUnits: -2.0
        });

        const mesh = new THREE.Mesh(pointGeom, mat);
        mesh.position.set(x, y, z);
        mesh.renderOrder = 2;
        mesh.userData = {
            isPoint: true,
            code: key,
            data: pt,
            defaultColor: merColor
        };

        // Add invisible hit target child for easy mouse & touch clicking
        const hitTarget = new THREE.Mesh(hitGeom, hitMat);
        hitTarget.userData = { isHitProxy: true, parentCode: key };
        mesh.add(hitTarget);

        scene.add(mesh);
        pointMeshes[key] = mesh;

        // If lateral point on arm or leg and not midline, create symmetric opposite side
        if (Math.abs(x) > 0.25 && !key.startsWith('DU') && !key.startsWith('REN') && !key.startsWith('YIN')) {
            const symMesh = new THREE.Mesh(pointGeom, mat.clone());
            symMesh.position.set(-x, y, z);
            symMesh.renderOrder = 2;
            symMesh.userData = {
                isPoint: true,
                code: key,
                data: pt,
                defaultColor: merColor,
                isSymmetric: true
            };
            const symHitTarget = new THREE.Mesh(hitGeom, hitMat);
            symHitTarget.userData = { isHitProxy: true, parentCode: key };
            symMesh.add(symHitTarget);

            scene.add(symMesh);
        }
    }

    // Create 3D Meridian Curves (Fine Hairline Trace: 0.015 radius)
    TCM_DATA.meridians.forEach(m => {
        // Do not draw a connecting channel tube for Extraordinary Points (EX),
        // as they are disparate empirical points across head, hands, abdomen, and legs.
        if (m.id === 'EX') return;

        const coords = [];
        m.points.forEach(pKey => {
            if (TCM_DATA.points[pKey]) {
                const [x, y, z] = TCM_DATA.points[pKey].pos;
                coords.push(new THREE.Vector3(x, y, z));
            }
        });

        if (coords.length >= 2) {
            const curve = new THREE.CatmullRomCurve3(coords);
            const tubeGeom = new THREE.TubeGeometry(curve, coords.length * 8, 0.015, 8, false);
            const hexColor = parseInt(m.color.replace('#', '0x'));
            
            const lineMat = new THREE.MeshStandardMaterial({
                color: hexColor,
                emissive: hexColor,
                emissiveIntensity: 0.82,
                roughness: 0.2,
                metalness: 0.1,
                polygonOffset: true,
                polygonOffsetFactor: -1.0,
                polygonOffsetUnits: -2.0
            });

            const tubeMesh = new THREE.Mesh(tubeGeom, lineMat);
            tubeMesh.renderOrder = 1;
            tubeMesh.userData = {
                isMeridian: true,
                meridianId: m.id,
                defaultColor: hexColor,
                defaultRadius: 0.015
            };
            scene.add(tubeMesh);
            meridianLines[m.id] = tubeMesh;

            // Symmetrical opposite line for bilateral channels
            if (m.id !== 'DU' && m.id !== 'REN' && m.id !== 'EX') {
                const symCoords = coords.map(v => new THREE.Vector3(-v.x, v.y, v.z));
                const symCurve = new THREE.CatmullRomCurve3(symCoords);
                const symTubeGeom = new THREE.TubeGeometry(symCurve, symCoords.length * 8, 0.015, 8, false);
                const symTubeMesh = new THREE.Mesh(symTubeGeom, lineMat.clone());
                symTubeMesh.renderOrder = 1;
                symTubeMesh.userData = {
                    isMeridian: true,
                    meridianId: m.id,
                    defaultColor: hexColor,
                    isSymmetric: true
                };
                scene.add(symTubeMesh);
            }
        }
    });
}

// Initialize UI Elements
function populateUI() {
    // Statue Finish Select
    const statueSelect = document.getElementById('statue-select');
    if (statueSelect) {
        statueSelect.addEventListener('change', (e) => {
            setStatueStyle(e.target.value);
        });
    }

    // Size Select
    const sizeSelect = document.getElementById('size-select');
    if (sizeSelect) {
        sizeSelect.addEventListener('change', (e) => {
            setSizeScale(e.target.value);
        });
    }

    // Populate Meridian Select
    const select = document.getElementById('meridian-select');
    select.innerHTML = '<option value="ALL">✨ All 14 Meridians & Extra Points</option>';
    TCM_DATA.meridians.forEach(m => {
        const opt = document.createElement('option');
        opt.value = m.id;
        opt.textContent = `${m.id}: ${m.fullName || m.name} [${m.element}]`;
        select.appendChild(opt);
    });

    select.addEventListener('change', (e) => {
        filterMeridian(e.target.value);
    });

    // Preset View Buttons
    document.getElementById('btn-front').onclick = () => setCameraView(0, 0, 15, [0, 0, 0]);
    document.getElementById('btn-back').onclick = () => setCameraView(0, 0, -15, [0, 0, 0]);
    document.getElementById('btn-left').onclick = () => setCameraView(-15, 0, 0, [0, 0, 0]);
    document.getElementById('btn-right').onclick = () => setCameraView(15, 0, 0, [0, 0, 0]);
    document.getElementById('btn-reset').onclick = () => {
        filterMeridian('ALL');
        select.value = 'ALL';
        setCameraView(0, 0, 15, [0, 0, 0]);
        hideInfoCard();
    };

    document.getElementById('close-card-btn').onclick = hideInfoCard;

    // Search Box
    const searchInput = document.getElementById('point-search');
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.trim().toUpperCase();
        if (query.length >= 2 || (query.length >= 1 && /[\u4e00-\u9fff]/.test(query))) {
            for (const [code, pt] of Object.entries(TCM_DATA.points)) {
                if (code.includes(query) || 
                    (pt.name && pt.name.toUpperCase().includes(query)) ||
                    (pt.hanzi && pt.hanzi.includes(query))) {
                    selectPoint(code);
                    break;
                }
            }
        }
    });
}

// Filter and Highlight Meridian
function filterMeridian(meridianId) {
    currentMeridianFilter = meridianId;
    const panelName = document.getElementById('meridian-panel-name');
    const panelDesc = document.getElementById('meridian-panel-desc');

    if (meridianId === 'ALL') {
        panelName.textContent = '14 Meridians Active';
        panelDesc.textContent = 'All 12 Primary channels (Hand/Foot Yin/Yang) + Du Mai, Ren Mai & Extra Points visible. Click any point for board exam details.';

        // Reset all lines and points to normal
        scene.traverse(obj => {
            if (obj.userData.isMeridian) {
                obj.material.emissiveIntensity = 0.82;
                obj.scale.set(currentScaleFactor, currentScaleFactor, currentScaleFactor);
                obj.visible = true;
            }
            if (obj.userData.isPoint) {
                obj.material.emissiveIntensity = 0.95;
                obj.scale.set(currentScaleFactor, currentScaleFactor, currentScaleFactor);
                obj.visible = true;
            }
        });
    } else {
        const m = TCM_DATA.meridians.find(item => item.id === meridianId);
        if (m) {
            panelName.textContent = m.fullName || `${m.name} (${m.chinese})`;
            panelDesc.innerHTML = `<strong>⚡ Six Divisions:</strong> ${m.division}<br><strong>🌿 Element:</strong> ${m.element} | <strong>⏰ Clock Flow:</strong> ${m.time}<br><span style="color:#cbd5e1; margin-top:4px; display:inline-block;">${m.description}</span>`;

            // Highlight chosen meridian; strongly dim / declutter non-matching
            scene.traverse(obj => {
                if (obj.userData.isMeridian) {
                    if (obj.userData.meridianId === meridianId) {
                        obj.material.emissiveIntensity = 1.4;
                        obj.scale.set(currentScaleFactor * 1.35, currentScaleFactor * 1.35, currentScaleFactor * 1.35);
                        obj.visible = true;
                    } else {
                        obj.material.emissiveIntensity = 0.05;
                    }
                }
                if (obj.userData.isPoint) {
                    const belongs = m.points.includes(obj.userData.code);
                    if (belongs) {
                        obj.material.emissiveIntensity = 1.4;
                        obj.scale.set(currentScaleFactor * 1.35, currentScaleFactor * 1.35, currentScaleFactor * 1.35);
                        obj.visible = true;
                    } else {
                        obj.material.emissiveIntensity = 0.08;
                        obj.scale.set(currentScaleFactor * 0.5, currentScaleFactor * 0.5, currentScaleFactor * 0.5);
                    }
                }
            });
        }
    }
}

// Camera View Animator
function setCameraView(x, y, z, target = [0,0,0]) {
    const startPos = camera.position.clone();
    const endPos = new THREE.Vector3(x, y, z);
    const startTarget = controls.target.clone();
    const endTarget = new THREE.Vector3(...target);
    const duration = 600;
    const startTime = performance.now();

    function updateCam(now) {
        const progress = Math.min((now - startTime) / duration, 1);
        const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
        camera.position.lerpVectors(startPos, endPos, ease);
        controls.target.lerpVectors(startTarget, endTarget, ease);
        controls.update();
        if (progress < 1) requestAnimationFrame(updateCam);
    }
    requestAnimationFrame(updateCam);
}

// Helper: Resolve hit proxy to actual point object
function resolvePointHit(intersects) {
    for (const hit of intersects) {
        if (hit.object.userData.isPoint) {
            return hit.object;
        }
        if (hit.object.userData.isHitProxy) {
            return hit.object.parent;
        }
    }
    return null;
}

// Mouse & Raycasting
function onMouseMove(event) {
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(scene.children, true);
    const pointHit = resolvePointHit(intersects);

    const tooltip = document.getElementById('tooltip');

    if (pointHit) {
        document.body.style.cursor = 'pointer';
        const pt = pointHit.userData.data;
        const code = pointHit.userData.code;
        tooltip.style.display = 'block';
        tooltip.style.left = (event.clientX + 14) + 'px';
        tooltip.style.top = (event.clientY - 12) + 'px';
        tooltip.textContent = `${code} (${pt.name} / ${pt.hanzi})`;
    } else {
        document.body.style.cursor = 'default';
        tooltip.style.display = 'none';
    }
}

function onClick(event) {
    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(scene.children, true);
    const pointHit = resolvePointHit(intersects);
    const lineHit = intersects.find(hit => hit.object.userData.isMeridian);

    if (pointHit) {
        const code = pointHit.userData.code;
        selectPoint(code);
    } else if (lineHit) {
        const mId = lineHit.object.userData.meridianId;
        document.getElementById('meridian-select').value = mId;
        filterMeridian(mId);
    }
}

function onTouchStart(event) {
    if (event.touches.length === 1) {
        const touch = event.touches[0];
        mouse.x = (touch.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(touch.clientY / window.innerHeight) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(scene.children, true);
        const pointHit = resolvePointHit(intersects);
        if (pointHit) {
            selectPoint(pointHit.userData.code);
        }
    }
}

// Select and Display Acupoint Information
function selectPoint(code) {
    selectedPointCode = code;
    const pt = TCM_DATA.points[code];
    if (!pt) return;

    // Smoothly fly camera to point location (close-up to declutter clusters)
    const [px, py, pz] = pt.pos;
    const camDist = 3.8;
    const norm = new THREE.Vector3(px, py * 0.35, pz + 1.0).normalize();
    setCameraView(px + norm.x * camDist, py + 0.2, pz + norm.z * camDist, [px, py, pz]);

    // Highlight Point Mesh
    scene.traverse(obj => {
        if (obj.userData.isPoint) {
            if (obj.userData.code === code) {
                obj.material.emissiveIntensity = 1.6;
                obj.scale.set(currentScaleFactor * 1.8, currentScaleFactor * 1.8, currentScaleFactor * 1.8);
            } else {
                obj.material.emissiveIntensity = 0.5;
                obj.scale.set(currentScaleFactor, currentScaleFactor, currentScaleFactor);
            }
        }
    });

    // Find parent meridian full name
    let meridianTitle = code;
    for (const m of TCM_DATA.meridians) {
        if (m.points.includes(code)) {
            meridianTitle = `${m.id} • ${m.fullName || m.name}`;
            break;
        }
    }

    // Populate Info Card
    const card = document.getElementById('info-card');
    const badgesDiv = document.getElementById('card-badges');
    const title = document.getElementById('card-title');
    const location = document.getElementById('card-location');
    const actions = document.getElementById('card-actions');
    const cautionText = document.getElementById('card-caution-text');

    badgesDiv.innerHTML = `
        <span class="badge badge-meridian">${meridianTitle}</span>
        <span class="badge badge-cat">${pt.cat}</span>
    `;

    title.textContent = `${code} (${pt.name} / ${pt.hanzi})`;
    location.textContent = pt.loc;
    actions.textContent = pt.act;
    cautionText.textContent = pt.saf;

    card.classList.add('visible');
}

function hideInfoCard() {
    const card = document.getElementById('info-card');
    card.classList.remove('visible');
    // Restore point scale
    scene.traverse(obj => {
        if (obj.userData.isPoint) {
            obj.scale.set(currentScaleFactor, currentScaleFactor, currentScaleFactor);
            obj.material.emissiveIntensity = 0.95;
        }
    });
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Animation Loop
function animate() {
    requestAnimationFrame(animate);
    controls.update();

    // Gentle breathing pulse on acupoint markers
    const time = performance.now() * 0.003;
    for (const [code, mesh] of Object.entries(pointMeshes)) {
        if (code !== selectedPointCode) {
            mesh.material.emissiveIntensity = 0.85 + Math.sin(time + mesh.position.y) * 0.15;
        }
    }

    renderer.render(scene, camera);
}

window.addEventListener('DOMContentLoaded', initScene);
</script>
</body>
</html>
"""

def generate_3d_viewer_html() -> str:
    """Generate standalone HTML with Three.js rendering seamless sculpted medical statue."""
    data = get_meridians_data()
    data_json = json.dumps(data)
    glb_b64 = get_glb_base64()

    html = HTML_TEMPLATE.replace("__TCM_DATA_JSON__", data_json).replace("__GLB_BASE64__", glb_b64)
    return html

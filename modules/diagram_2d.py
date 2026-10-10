"""Interactive 2D Acupuncture Meridian and Acupoint Chart Viewer.

Built completely from scratch with pure, native SVG vector graphics modeled after
classical National Standard Acupoint Wall Charts (GB/T 12346):
- Three complete anatomical human figures standing side-by-side:
  1. Anterior View (Front) with muscular contouring and split-anatomy skeletal landmarks (ribs, clavicle, pelvis, patella)
  2. Posterior View (Back) with spine, scapulae, Back-Shu lines, popliteal crease, calves
  3. Lateral View (Side Profile) with the iconic raised-arm posture revealing the full Gallbladder zigzag and Hand-Yang channels
- Smooth Catmull-Rom vector meridian curves with official Six-Division colors and glowing illumination
- Interactive acupoints with generous hit areas, hover tooltips, and click-to-inspect clinical detail cards
- Real-time multi-script search (Code, Pinyin, or Hanzi) with auto-pan & auto-zoom to the point on the chart
- Pure SVG camera zoom & pan engine: figures, bones, meridians, points, and labels scale and move together as ONE unified coordinate space
- English-first interface with standardized bilingual TCM terminology: CODE (Pinyin / Hanzi)
"""

import json
from pathlib import Path
from typing import Dict, Any

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
FITTED_POINTS_PATH = STATIC_DIR / "fitted_points.json"


def get_diagram_dataset() -> Dict[str, Any]:
    """Load canonical points and meridian definitions structured for the 1600x1000 SVG canvas."""
    points_dict = {}
    if FITTED_POINTS_PATH.exists():
        try:
            with open(FITTED_POINTS_PATH, "r", encoding="utf-8") as f:
                points_dict = json.load(f)
        except Exception:
            pass

    # 14 Major Meridians + Extra Points with official Six-Division names
    meridians = [
        {
            "id": "LU",
            "name": "Lung Channel of Hand-Taiyin",
            "chinese": "手太阴肺经",
            "division": "Hand-Taiyin (手太阴)",
            "fullName": "Lung Channel of Hand-Taiyin (手太阴肺经)",
            "element": "Metal",
            "time": "3:00 AM – 5:00 AM",
            "color": "#38bdf8",
            "primaryView": "front",
            "description": "Originates in middle burner, descends to Large Intestine, ascends through Lung, emerges at LU1 (Zhongfu), runs down anterolateral arm to radial tip of thumb (LU11 Shaoshang).",
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
            "primaryView": "side",
            "description": "Originates radial index fingertip (LI1 Shangyang), ascends lateral border of forearm through LI4 Hegu and LI11 Quchi, traverses shoulder at LI15, neck to opposite ala nasi (LI20 Yingxiang).",
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
            "primaryView": "front",
            "description": "Originates infraorbital rim (ST1 Chengqi), circles mouth, ascends to forehead corner (ST8 Touwei), descends neck (ST12 Quepen), chest mamillary line (ST18 Rugen), abdomen 2 cun lateral to midline (ST25, ST28, ST30), anterolateral leg through ST36 Zusanli and ST40 Fenglong, to lateral 2nd toe (ST45 Lidui).",
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
            "primaryView": "front",
            "description": "Originates medial big toe (SP1 Yinbai), ascends medial foot and leg through SP4 Gongsun, SP6 Sanyinjiao, SP9 Yinlingquan, inner thigh SP10 Xuehai, abdomen 4 cun lateral (SP15), terminates at SP21 Dabao on mid-axillary line.",
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
            "primaryView": "front",
            "description": "Originates in Heart, emerges from axilla at HT1 Jiquan, descends medial-posterior arm through HT3 Shaohai, transverse wrist crease at HT7 Shenmen, terminates at radial little fingertip (HT9 Shaochong).",
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
            "primaryView": "back",
            "description": "Originates ulnar little finger (SI1 Shaoze), travels ulnar hand (SI3 Houxi), elbow groove (SI8 Xiaohai), posterior shoulder (SI9, SI11 Tianzong), ascends neck (SI16 Tianchuang) to anterior tragus of ear (SI19 Tinggong).",
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
            "primaryView": "back",
            "description": "Longest channel in body (67 points). Originates inner canthus (BL1 Jingming), crosses vertex, occiput (BL10), splits into inner 1.5 cun line (Back-Shu points BL11-BL23) and outer 3.0 cun line (BL52 Zhishi), down posterior leg (BL40 Weizhong, BL57 Chengshan, BL60 Kunlun) to little toe (BL67 Zhiyin).",
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
            "primaryView": "front",
            "description": "Originates sole of foot (KI1 Yongquan), circles medial malleolus (KI3 Taixi, KI6 Zhaohai), ascends posteromedial lower leg (KI7 Fuliu), inner knee (KI10), lower abdomen 0.5 cun lateral to midline and chest.",
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
            "primaryView": "front",
            "description": "Originates in chest, emerges near nipple, descends middle anterior arm through PC3 Quze, between forearm tendons (PC6 Neiguan), wrist crease (PC7 Daling), palm (PC8 Laogong) to middle fingertip (PC9 Zhongchong).",
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
            "primaryView": "side",
            "description": "Originates ulnar ring finger (SJ1 Guanchong), dorsum of hand (SJ3 Zhongzhu), dorsal forearm between bones (SJ5 Waiguan, SJ6 Zhigou), shoulder depression (SJ14 Jianliao), behind ear (SJ17 Yifeng), encircles ear to lateral eyebrow (SJ23).",
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
            "primaryView": "side",
            "description": "Originates outer canthus (GB1 Tongziliao), zigzags temple and skull (GB8, GB14, GB20 Fengchi), shoulder top (GB21 Jianjing), lateral flank (GB26 Daimai), buttock (GB30 Huantiao), lateral thigh and leg (GB34, GB39), terminates at 4th toe (GB44 Zuqiaoyin).",
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
            "primaryView": "front",
            "description": "Originates lateral big toe (LV1 Dadun), ascends dorsum of foot (LV2, LV3 Taichong), medial lower leg (LV5 Ligou, LV8 Ququan), enters lower abdomen to tip of 11th rib (LV13 Zhangmen) and 6th intercostal space (LV14 Qimen).",
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
            "primaryView": "back",
            "description": "Emerges at perineum (DU1 Changqiang), ascends posterior midline of spine through DU4 Mingmen, DU9 Zhiyang, DU14 Dazhui, nape (DU15, DU16 Fengfu), skull vertex (DU20 Baihui), over forehead (DU24) to philtrum (DU26 Shuigou).",
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
            "primaryView": "front",
            "description": "Emerges at perineum, ascends anterior midline through lower abdomen (REN3 Zhongji, REN4 Guanyuan, REN6 Qihai), umbilicus (REN8 Shenque), epigastrium (REN12 Zhongwan), chest center (REN17 Shanzhong), throat (REN22 Tiantu) to chin groove (REN24 Chengjiang).",
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
            "primaryView": "front",
            "description": "Specific classical empirical acupoints not situated on the 14 primary channels, possessing profound therapeutic actions confirmed through clinical history.",
            "points": ["YINTANG", "TAIYANG", "SISHENCONG", "DINGCHUAN", "HUATUOJIAJI", "YAOTONGXUE", "SIFENG", "HEDING", "DANNANGXUE", "LANWEIXUE", "ZIGONG"]
        }
    ]

    # Precalculate exact coordinates mapping to the 1600x1000 native SVG canvas:
    # Figure 1 (Front): Center 280
    # Figure 2 (Back): Center 780
    # Figure 3 (Side with raised arm): Center 1280
    def get_y(y):
        if y >= 0.05:
            return 460.0 - (y - 0.05) / 5.2 * (460.0 - 75.0)
        elif y >= -1.2:
            return 460.0 + (0.05 - y) / 1.25 * (560.0 - 460.0)
        elif y >= -3.65:
            return 560.0 + (-1.2 - y) / 2.45 * (710.0 - 560.0)
        else:
            return 710.0 + (-3.65 - y) / 2.67 * (920.0 - 710.0)

    for code, pt in points_dict.items():
        x, y, z = pt["pos"]
        sy = get_y(y)

        # 1. Front Figure Mapping (Center 280)
        if y > -1.2 and x < 1.3:
            fx_r = 280.0 + x * 36.0
            fx_l = 280.0 - x * 36.0
        elif y <= -1.2 and x < 1.3:
            fx_r = 280.0 + 20.0 + x * 22.0
            fx_l = 280.0 - 20.0 - x * 22.0
        else:
            # Arm
            fx_r = 280.0 + 40.0 + x * 44.0
            fx_l = 280.0 - 40.0 - x * 44.0

        # 2. Back Figure Mapping (Center 780)
        if y > -1.2 and x < 1.3:
            bx_r = 780.0 + x * 55.0
            bx_l = 780.0 - x * 55.0
        elif y <= -1.2 and x < 1.3:
            bx_r = 780.0 + 20.0 + x * 22.0
            bx_l = 780.0 - 20.0 - x * 22.0
        else:
            # Arm
            bx_r = 780.0 + 40.0 + x * 44.0
            bx_l = 780.0 - 40.0 - x * 44.0

        # 3. Side Profile Figure Mapping (Raised arm posture, Center 1280)
        if x > 1.3 and y > -1.0:
            # Points on the raised right arm
            t = (2.58 - x) / (2.58 - 1.45)
            lat_x = 1190.0 + t * 55.0
            lat_y = 45.0 + t * 215.0
        elif y <= -1.2:
            lat_x = 1240.0 + z * 35.0
            lat_y = sy
        else:
            lat_x = 1270.0 + z * 50.0
            lat_y = sy

        # Find parent meridian
        parent_m = "EX"
        for m in meridians:
            if code in m["points"]:
                parent_m = m["id"]
                break

        # Primary figure recommendation
        primary_f = "front"
        if parent_m in ["DU", "BL"] and code not in ["BL1", "BL2", "DU24", "DU26"]:
            primary_f = "back"
        elif parent_m in ["GB", "SJ", "LI"]:
            primary_f = "side"

        pt["pos_2d"] = {
            "front": {"x": round(fx_r, 1), "xl": round(fx_l, 1), "y": round(sy, 1)},
            "back": {"x": round(bx_r, 1), "xl": round(bx_l, 1), "y": round(sy, 1)},
            "side": {"x": round(lat_x, 1), "y": round(lat_y, 1)},
            "primary": primary_f,
            "channel": parent_m
        }

    return {
        "meridians": meridians,
        "points": points_dict
    }


def generate_2d_diagram_html() -> str:
    """Generate self-contained HTML/CSS/JS for the pure vector National Standard Chart Viewer."""
    data = get_diagram_dataset()
    data_json = json.dumps(data, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0, user-scalable=yes">
<title>Acupuncture Meridian & Acupoint Anatomical Wall Chart</title>
<style>
:root {{
    --bg-page: #fbf5eb;
    --border-color: #d1bfa7;
    --text-primary: #2c1810;
    --text-secondary: #6e5041;
    --text-muted: #9e7f6e;
    --accent: #b91c1c;
    --accent-glow: rgba(185, 28, 28, 0.45);
    --card-bg: rgba(254, 250, 242, 0.97);
}}

[data-theme="dark"] {{
    --bg-page: #090d16;
    --border-color: #334155;
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent: #38bdf8;
    --accent-glow: rgba(56, 189, 248, 0.45);
    --card-bg: rgba(15, 23, 42, 0.97);
}}

* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
}}

body {{
    background-color: var(--bg-page);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", Arial, sans-serif;
    overflow-x: hidden;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}}

/* Header Toolbar */
.chart-header {{
    background: var(--card-bg);
    border-bottom: 2px solid var(--border-color);
    padding: 10px 16px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(12px);
    display: flex;
    flex-direction: column;
    gap: 8px;
}}

.header-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}}

.brand-title {{
    display: flex;
    align-items: center;
    gap: 8px;
}}

.brand-title h1 {{
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: 0.8px;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 6px;
}}

.std-tag {{
    font-size: 0.70rem;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    background: rgba(185, 28, 28, 0.12);
    border: 1px solid rgba(185, 28, 28, 0.35);
    color: var(--accent);
}}

/* View Selector Buttons */
.view-btn-group {{
    display: inline-flex;
    background: rgba(0,0,0,0.05);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 2px;
    gap: 2px;
}}

.v-btn {{
    background: transparent;
    border: none;
    color: var(--text-secondary);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.78rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.18s ease;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}}

.v-btn:hover {{
    color: var(--text-primary);
    background: rgba(0,0,0,0.06);
}}

.v-btn.active {{
    background: var(--accent);
    color: #ffffff !important;
    box-shadow: 0 2px 8px var(--accent-glow);
}}

/* Search Input */
.search-wrapper {{
    position: relative;
    flex: 1 1 200px;
    min-width: 180px;
    max-width: 380px;
}}

.search-input {{
    width: 100%;
    background: rgba(0, 0, 0, 0.05);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    padding: 7px 32px 7px 32px;
    border-radius: 8px;
    font-size: 0.82rem;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
}}

.search-input:focus {{
    border-color: var(--accent);
    box-shadow: 0 0 0 2px var(--accent-glow);
}}

.search-icon {{
    position: absolute;
    left: 9px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 0.85rem;
    color: var(--text-muted);
    pointer-events: none;
}}

.clear-search-btn {{
    position: absolute;
    right: 8px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--text-muted);
    cursor: pointer;
    font-size: 0.85rem;
    display: none;
}}

/* Quick Meridian Pills */
.meridian-pills-bar {{
    display: flex;
    overflow-x: auto;
    padding-bottom: 2px;
    gap: 5px;
    scrollbar-width: thin;
}}

.m-pill {{
    background: rgba(0,0,0,0.04);
    border: 1px solid var(--border-color);
    color: var(--text-secondary);
    padding: 4px 10px;
    border-radius: 14px;
    font-size: 0.74rem;
    font-weight: 700;
    white-space: nowrap;
    cursor: pointer;
    transition: all 0.15s ease;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}}

.m-pill .dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    display: inline-block;
}}

.m-pill:hover {{
    color: var(--text-primary);
    border-color: var(--accent);
}}

.m-pill.active {{
    background: var(--accent);
    border-color: var(--accent);
    color: #ffffff;
    box-shadow: 0 2px 8px var(--accent-glow);
}}

/* Meridian Information Ribbon */
.meridian-ribbon {{
    background: rgba(0,0,0,0.03);
    border-bottom: 1px solid var(--border-color);
    padding: 7px 16px;
    font-size: 0.78rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
}}

.meridian-ribbon .m-title {{
    font-weight: 800;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 6px;
}}

.meridian-ribbon .m-meta {{
    color: var(--text-secondary);
    display: flex;
    gap: 12px;
    font-size: 0.74rem;
}}

/* Main Interactive SVG Stage */
.stage-container {{
    flex: 1;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--bg-page);
    min-height: 650px;
    cursor: grab;
}}

.stage-container.panning {{
    cursor: grabbing;
}}

.svg-diagram {{
    width: 100%;
    height: 100%;
    max-height: 880px;
    user-select: none;
}}

/* Floating Zoom & Tool Controls */
.floating-controls {{
    position: absolute;
    right: 16px;
    bottom: 20px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    z-index: 50;
}}

.f-btn {{
    width: 38px;
    height: 38px;
    border-radius: 8px;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    font-size: 1.05rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    transition: all 0.15s;
}}

.f-btn:hover {{
    background: var(--accent);
    color: #fff;
    transform: translateY(-1px);
}}

/* Point Detail Card */
.point-detail-card {{
    position: fixed;
    right: 18px;
    bottom: 18px;
    width: 360px;
    max-width: calc(100vw - 36px);
    background: var(--card-bg);
    backdrop-filter: blur(16px);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25);
    padding: 16px;
    z-index: 150;
    display: none;
    animation: slideUp 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}}

@keyframes slideUp {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.card-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 8px;
}}

.card-title {{
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
}}

.card-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-bottom: 10px;
}}

.badge {{
    font-size: 0.70rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 5px;
    letter-spacing: 0.3px;
}}

.badge-channel {{
    background: rgba(185, 28, 28, 0.12);
    color: var(--accent);
    border: 1px solid rgba(185, 28, 28, 0.35);
}}

.badge-category {{
    background: rgba(234, 179, 8, 0.15);
    color: #b45309;
    border: 1px solid rgba(234, 179, 8, 0.35);
}}

.card-section {{
    margin-bottom: 8px;
    font-size: 0.78rem;
    line-height: 1.45;
}}

.card-section-label {{
    font-weight: 800;
    color: var(--text-secondary);
    text-transform: uppercase;
    font-size: 0.66rem;
    margin-bottom: 2px;
}}

.card-close {{
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 1.2rem;
    cursor: pointer;
    padding: 2px 6px;
    border-radius: 4px;
}}

.card-close:hover {{
    color: var(--text-primary);
    background: rgba(0, 0, 0, 0.08);
}}

.card-caution {{
    background: rgba(239, 68, 68, 0.08);
    border-left: 3px solid #dc2626;
    padding: 6px 9px;
    border-radius: 4px;
    font-size: 0.74rem;
    color: #991b1b;
    margin-top: 6px;
}}

/* Acupoint Markers */
.point-group {{
    cursor: pointer;
    transition: transform 0.15s ease;
}}

.point-group:hover .point-circle {{
    transform: scale(1.6);
}}

.point-circle {{
    transition: all 0.15s ease;
    transform-origin: center;
}}

.point-pulse {{
    animation: radarPulse 1.8s infinite ease-out;
    pointer-events: none;
}}

@keyframes radarPulse {{
    0% {{ r: 5px; opacity: 0.95; stroke-width: 2.5px; }}
    100% {{ r: 24px; opacity: 0; stroke-width: 0.5px; }}
}}

.point-label {{
    font-size: 9px;
    font-weight: 800;
    fill: #2c1810;
    pointer-events: none;
    display: none;
    text-shadow: 0 1px 3px rgba(255,255,255,0.9);
}}

.show-labels .point-label {{
    display: block;
}}

/* Meridian Vector Lines */
.meridian-path {{
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    transition: opacity 0.22s, stroke-width 0.22s, filter 0.22s;
}}

.meridian-path.dimmed {{
    opacity: 0.08 !important;
}}

.meridian-path.highlighted {{
    opacity: 1.0 !important;
    stroke-width: 4.5px !important;
    filter: drop-shadow(0 0 6px var(--path-color));
}}

/* Tooltip */
.hover-tooltip {{
    position: absolute;
    display: none;
    background: rgba(24, 24, 27, 0.94);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 5px 10px;
    color: #ffffff;
    font-size: 0.76rem;
    font-weight: 700;
    pointer-events: none;
    z-index: 120;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    white-space: nowrap;
}}

/* Section Titles on SVG */
.fig-title {{
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 1px;
    fill: var(--text-secondary);
    text-anchor: middle;
}}
</style>
</head>
<body>

<!-- Header Toolbar -->
<header class="chart-header">
    <div class="header-row">
        <div class="brand-title">
            <h1>National Standard Acupuncture Chart</h1>
            <span class="std-tag">GB/T 12346 • WHO Standard</span>
        </div>

        <!-- View Switcher -->
        <div class="view-btn-group" id="view-selector">
            <button class="v-btn active" data-view="full">🖼️ Full 3-Panel Chart</button>
            <button class="v-btn" data-view="front">👤 Anterior (Front)</button>
            <button class="v-btn" data-view="back">🔙 Posterior (Back)</button>
            <button class="v-btn" data-view="side">🧍 Lateral (Side)</button>
        </div>

        <!-- Search Input -->
        <div class="search-wrapper">
            <span class="search-icon">🔍</span>
            <input type="text" id="point-search" class="search-input" placeholder="Search code (ST36), Pinyin (Zusanli), or Chinese (足三里)..." autocomplete="off" spellcheck="false">
            <button class="clear-search-btn" id="clear-search">✕</button>
        </div>

        <!-- Tools: Labels & Theme -->
        <div style="display: flex; gap: 6px; align-items: center;">
            <button class="v-btn" id="toggle-labels-btn" title="Toggle Point Labels">🏷️ Labels</button>
            <button class="v-btn" id="toggle-tier1-btn" title="Highlight High-Yield Exam Points">🔥 Tier 1</button>
            <select id="theme-select" style="background: rgba(0,0,0,0.05); border: 1px solid var(--border-color); color: var(--text-primary); border-radius: 6px; padding: 5px 8px; font-size: 0.78rem; outline: none; cursor: pointer;">
                <option value="parchment">📜 Authentic Parchment</option>
                <option value="dark">🌑 Modern Dark Studio</option>
            </select>
        </div>
    </div>

    <!-- Quick Meridian Pills -->
    <div class="meridian-pills-bar" id="pills-bar">
        <button class="m-pill active" data-mid="ALL">✨ All Channels</button>
        <!-- Populated via JS -->
    </div>
</header>

<!-- Meridian Info Ribbon -->
<div class="meridian-ribbon" id="meridian-ribbon">
    <div class="m-title" id="ribbon-title">
        <span>⚡ All 14 Primary Channels Active</span>
    </div>
    <div class="m-meta" id="ribbon-meta">
        <span>Click any meridian or point marker to inspect Six-Division pathways, Cun landmarks, and clinical actions.</span>
    </div>
</div>

<!-- Main Interactive Canvas Stage -->
<main class="stage-container" id="stage">
    <svg id="main-svg" class="svg-diagram show-labels" viewBox="0 0 1600 1000">
        <defs>
            <!-- Luminous Blur Glow Filter -->
            <filter id="glow" x="-25%" y="-25%" width="150%" height="150%">
                <feGaussianBlur stdDeviation="3.8" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>

            <!-- Warm Anatomical Skin Gradients (Matching National Standard Chart) -->
            <radialGradient id="skinGradFront" cx="45%" cy="35%" r="65%">
                <stop offset="0%" stop-color="#fee6d3" />
                <stop offset="55%" stop-color="#f8cfae" />
                <stop offset="85%" stop-color="#e9a47c" />
                <stop offset="100%" stop-color="#cb7e54" />
            </radialGradient>

            <radialGradient id="skinGradBack" cx="50%" cy="35%" r="65%">
                <stop offset="0%" stop-color="#fee6d3" />
                <stop offset="60%" stop-color="#f8cfae" />
                <stop offset="90%" stop-color="#e79f75" />
                <stop offset="100%" stop-color="#c8794f" />
            </radialGradient>

            <radialGradient id="skinGradSide" cx="45%" cy="30%" r="65%">
                <stop offset="0%" stop-color="#fee6d3" />
                <stop offset="60%" stop-color="#f8cfae" />
                <stop offset="90%" stop-color="#e79f75" />
                <stop offset="100%" stop-color="#c8794f" />
            </radialGradient>
        </defs>

        <!-- Entire Scene in ONE Unified Canvas Space (Zero drift on pan/zoom) -->
        <g id="scene-layer">
            <!-- 1. Anatomical Figures Layer -->
            <g id="figures-layer"></g>
            <!-- 2. Skeletal & Landmark Layer (Split-Anatomy) -->
            <g id="landmarks-layer"></g>
            <!-- 3. Meridian Vector Splines Layer -->
            <g id="meridians-layer"></g>
            <!-- 4. Interactive Acupoint Markers Layer -->
            <g id="points-layer"></g>
        </g>
    </svg>

    <!-- Floating Zoom Controls -->
    <div class="floating-controls">
        <button class="f-btn" id="zoom-in" title="Zoom In">+</button>
        <button class="f-btn" id="zoom-out" title="Zoom Out">−</button>
        <button class="f-btn" id="zoom-reset" title="Reset View">↺</button>
    </div>

    <!-- Mouse Hover Tooltip -->
    <div class="hover-tooltip" id="tooltip"></div>

    <!-- Point Detailed Clinical Information Card -->
    <aside class="point-detail-card" id="point-card">
        <div class="card-header">
            <div>
                <div class="card-title" id="c-title">ST36 (Zusanli / 足三里)</div>
                <div style="font-size: 0.74rem; color: var(--text-secondary); margin-top: 1px;" id="c-eng">Leg Three Miles</div>
            </div>
            <button class="card-close" id="c-close" title="Close">✕</button>
        </div>

        <div class="card-badges" id="c-badges"></div>

        <div class="card-section">
            <div class="card-section-label">📍 Anatomical Location & Cun</div>
            <div id="c-loc" style="color: var(--text-primary);"></div>
        </div>

        <div class="card-section">
            <div class="card-section-label">⚡ Clinical Actions & Indications</div>
            <div id="c-act" style="color: var(--text-primary);"></div>
        </div>

        <div class="card-caution" id="c-saf-box">
            <div style="font-weight: 700; margin-bottom: 2px;">⚠️ Needling Depth & Safety Precautions:</div>
            <div id="c-saf"></div>
        </div>
    </aside>
</main>

<script>
// Load Dataset
const DATA = {data_json};

// State Variables
let currentView = 'full';
let currentMeridian = 'ALL';
let showLabels = true;
let tier1Only = false;
let selectedPoint = null;

// Native SVG ViewBox Camera States
const VIEW_PRESETS = {{
    full: {{ x: 0, y: 0, w: 1600, h: 1000 }},
    front: {{ x: 50, y: 30, w: 460, h: 940 }},
    back: {{ x: 550, y: 30, w: 460, h: 940 }},
    side: {{ x: 1060, y: 20, w: 490, h: 950 }}
}};

let vb = {{ x: 0, y: 0, w: 1600, h: 1000 }};
let isPanning = false;
let startX = 0, startY = 0;
let startVbX = 0, startVbY = 0;

// DOM References
const svg = document.getElementById('main-svg');
const figuresLayer = document.getElementById('figures-layer');
const landmarksLayer = document.getElementById('landmarks-layer');
const meridiansLayer = document.getElementById('meridians-layer');
const pointsLayer = document.getElementById('points-layer');
const stage = document.getElementById('stage');
const tooltip = document.getElementById('tooltip');
const pointCard = document.getElementById('point-card');
const searchInput = document.getElementById('point-search');
const clearSearchBtn = document.getElementById('clear-search');
const ribbonTitle = document.getElementById('ribbon-title');
const ribbonMeta = document.getElementById('ribbon-meta');

function updateViewBox() {{
    svg.setAttribute('viewBox', `${{vb.x.toFixed(1)}} ${{vb.y.toFixed(1)}} ${{vb.w.toFixed(1)}} ${{vb.h.toFixed(1)}}`);
}}

// Build Anatomical Human Body Figures (Pure Native SVG with Authentic Shading)
function renderBodyFigures() {{
    let html = `
    <!-- Poster Top Titles -->
    <text x="800" y="38" font-size="20" font-weight="800" letter-spacing="3" fill="var(--accent)" text-anchor="middle">
        国家标准经穴部位挂图 • NATIONAL STANDARD ACUPUNCTURE MERIDIAN CHART
    </text>

    <!-- Section Labels -->
    <text x="280" y="62" class="fig-title">ANTERIOR VIEW (前面观)</text>
    <text x="780" y="62" class="fig-title">POSTERIOR VIEW (背面观)</text>
    <text x="1300" y="42" class="fig-title">LATERAL PROFILE VIEW (侧面观)</text>

    <!-- ========================================== -->
    <!-- 1. ANTERIOR FIGURE (Front, Center 280)    -->
    <!-- ========================================== -->
    <g id="figure-front">
        <!-- Body Flesh Silhouette -->
        <path d="
            M 280,75
            C 315,75 330,105 330,150
            C 338,155 340,170 335,185
            C 330,205 308,228 300,235
            C 302,245 304,260 308,270
            C 325,275 360,282 390,290
            C 410,300 430,340 435,380
            C 440,410 455,455 465,485
            C 470,500 482,520 486,545
            C 478,555 468,540 458,520
            C 448,490 435,450 425,420
            C 415,390 390,350 365,340
            C 360,360 355,400 355,440
            C 355,465 348,485 348,510
            C 348,540 365,570 375,610
            C 380,640 375,680 360,725
            C 350,750 345,790 338,840
            C 332,875 325,905 322,925
            C 320,940 328,960 332,975
            C 328,985 310,985 295,980
            C 285,965 290,935 295,920
            C 298,890 302,840 302,790
            C 302,750 298,730 295,720
            C 292,690 285,660 280,635
            C 275,660 268,690 265,720
            C 262,730 258,750 258,790
            C 258,840 262,890 265,920
            C 270,935 275,965 265,980
            C 250,985 232,985 228,975
            C 232,960 240,940 238,925
            C 235,905 228,875 222,840
            C 215,790 210,750 200,725
            C 185,680 180,640 185,610
            C 195,570 212,540 212,510
            C 212,485 205,465 205,440
            C 205,400 200,360 195,340
            C 165,350 140,390 130,420
            C 120,450 105,490 95,520
            C 85,540 75,555 68,545
            C 72,520 85,500 90,485
            C 100,455 115,410 120,380
            C 125,340 145,300 165,290
            C 195,282 235,275 252,270
            C 254,260 256,245 260,235
            C 252,228 230,205 225,185
            C 220,170 222,155 230,150
            C 230,105 245,75 280,75 Z"
            fill="url(#skinGradFront)" stroke="#a35f37" stroke-width="1.8" />

        <!-- Hair Cap -->
        <path d="M 280,75 C 245,75 230,105 230,135 C 245,130 265,120 280,120 C 295,120 315,130 330,135 C 330,105 315,75 280,75 Z" fill="#24150c" />

        <!-- Facial Features -->
        <ellipse cx="260" cy="145" rx="4" ry="2" fill="#4a2e1d" />
        <ellipse cx="300" cy="145" rx="4" ry="2" fill="#4a2e1d" />
        <path d="M 276,145 L 280,165 L 284,165" fill="none" stroke="#7a482b" stroke-width="1.2" />
        <path d="M 272,180 Q 280,185 288,180" fill="none" stroke="#993d3d" stroke-width="1.6" />
    </g>

    <!-- ========================================== -->
    <!-- 2. POSTERIOR FIGURE (Back, Center 780)    -->
    <!-- ========================================== -->
    <g id="figure-back">
        <!-- Body Flesh Silhouette -->
        <path d="
            M 780,75
            C 815,75 830,105 830,150
            C 838,155 840,170 835,185
            C 830,205 808,228 800,235
            C 802,245 804,260 808,270
            C 825,275 860,282 890,290
            C 910,300 930,340 935,380
            C 940,410 955,455 965,485
            C 970,500 982,520 986,545
            C 978,555 968,540 958,520
            C 948,490 935,450 925,420
            C 915,390 890,350 865,340
            C 860,360 855,400 855,440
            C 855,465 848,485 848,510
            C 848,540 865,570 875,610
            C 880,640 875,680 860,725
            C 850,750 845,790 838,840
            C 832,875 825,905 822,925
            C 820,940 828,960 832,975
            C 828,985 810,985 795,980
            C 785,965 790,935 795,920
            C 798,890 802,840 802,790
            C 802,750 798,730 795,720
            C 792,690 785,660 780,635
            C 775,660 768,690 765,720
            C 762,730 758,750 758,790
            C 758,840 762,890 765,920
            C 770,935 775,965 765,980
            C 750,985 732,985 728,975
            C 732,960 740,940 738,925
            C 735,905 728,875 722,840
            C 715,790 710,750 700,725
            C 685,680 680,640 685,610
            C 695,570 712,540 712,510
            C 712,485 705,465 705,440
            C 705,400 700,360 695,340
            C 665,350 640,390 630,420
            C 620,450 605,490 595,520
            C 585,540 575,555 568,545
            C 572,520 585,500 590,485
            C 600,455 615,410 620,380
            C 625,340 645,300 665,290
            C 695,282 735,275 752,270
            C 754,260 756,245 760,235
            C 752,228 730,205 725,185
            C 720,170 722,155 730,150
            C 730,105 745,75 780,75 Z"
            fill="url(#skinGradBack)" stroke="#a35f37" stroke-width="1.8" />

        <!-- Back Hair -->
        <path d="M 780,75 C 745,75 730,105 730,145 C 745,175 815,175 830,145 C 830,105 815,75 780,75 Z" fill="#24150c" />
    </g>

    <!-- ============================================================== -->
    <!-- 3. LATERAL PROFILE FIGURE (Raised Arm Stance, Center 1280)     -->
    <!-- ============================================================== -->
    <g id="figure-side">
        <!-- Profile Silhouette (Iconic National Standard Pose with Raised Right Arm) -->
        <path d="
            M 1270,110
            C 1300,110 1320,125 1322,145
            C 1325,152 1342,160 1342,168
            C 1342,174 1332,180 1334,188
            C 1334,195 1336,202 1330,212
            C 1324,220 1300,228 1290,235
            C 1282,245 1282,260 1280,270
            C 1295,290 1305,320 1305,360
            C 1305,410 1290,450 1290,480
            C 1290,520 1280,560 1260,600
            C 1265,630 1280,660 1275,705
            C 1270,735 1255,780 1250,810
            C 1245,845 1240,880 1235,905
            C 1235,920 1255,935 1270,950
            C 1270,960 1255,960 1235,955
            C 1215,955 1205,950 1205,940
            C 1205,920 1210,880 1215,860
            C 1215,830 1205,800 1205,780
            C 1205,750 1215,720 1215,695
            C 1215,665 1205,640 1205,610
            C 1200,580 1180,560 1180,530
            C 1180,480 1200,460 1200,450
            C 1200,410 1195,370 1195,350
            C 1195,300 1205,270 1205,250
            <!-- Upper Raised Right Arm Transition -->
            C 1205,220 1195,190 1195,180
            C 1190,140 1185,100 1185,85
            C 1185,60 1180,40 1190,35
            C 1200,35 1205,50 1210,75
            C 1215,105 1220,150 1225,185
            C 1230,215 1240,245 1245,260
            <!-- Back to Neck & Skull Profile -->
            C 1240,240 1230,220 1230,205
            C 1220,185 1210,165 1210,140
            C 1210,115 1235,110 1270,110 Z"
            fill="url(#skinGradSide)" stroke="#a35f37" stroke-width="1.8" />

        <!-- Side Hair Profile -->
        <path d="M 1270,110 C 1240,110 1225,125 1220,155 C 1240,150 1260,135 1275,135 C 1285,135 1300,140 1315,145 C 1315,125 1295,110 1270,110 Z" fill="#24150c" />

        <!-- Ear Profile -->
        <path d="M 1265,160 C 1278,155 1282,175 1272,185 C 1266,190 1262,182 1265,160 Z" fill="none" stroke="#7a482b" stroke-width="1.4" />
    </g>`;

    figuresLayer.innerHTML = html;
}}

// Build Split-Anatomy Skeletal Landmark References (Matching Reference Chart)
function renderLandmarks() {{
    let html = `
    <!-- Front View Split Skeletal Landmark Underlay (Left Half of Front Figure) -->
    <g class="landmarks-group" opacity="0.48">
        <!-- Clavicle -->
        <path d="M 280,245 Q 220,245 170,260" fill="none" stroke="#8a4d29" stroke-width="2.2" />
        <path d="M 280,245 Q 340,245 390,260" fill="none" stroke="#8a4d29" stroke-width="2.2" />

        <!-- Sternal Plate & Rib Cage Contours (Ribs 1 to 10 on screen left) -->
        <line x1="280" y1="245" x2="280" y2="390" stroke="#8a4d29" stroke-width="2.5" />
        <path d="M 280,265 Q 235,275 200,290" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,285 Q 230,295 195,315" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,305 Q 225,320 192,340" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,325 Q 225,345 190,365" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,345 Q 225,370 190,390" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,365 Q 230,395 195,415" fill="none" stroke="#8a4d29" stroke-width="1.5" />
        <path d="M 280,390 Q 235,420 205,450" fill="none" stroke="#8a4d29" stroke-width="2.0" />

        <!-- Pelvic Girdle & Iliac Crest on screen left -->
        <path d="M 280,520 Q 220,510 195,545 C 190,575 205,605 240,620" fill="none" stroke="#8a4d29" stroke-width="2.0" />
        <!-- Patella (Kneecap) -->
        <ellipse cx="225" cy="710" rx="14" ry="16" fill="none" stroke="#8a4d29" stroke-width="1.8" />
        <ellipse cx="335" cy="710" rx="14" ry="16" fill="none" stroke="#8a4d29" stroke-width="1.8" />
    </g>

    <!-- Back View Split Skeletal Landmark Underlay (Left Half of Back Figure) -->
    <g class="landmarks-group" opacity="0.48">
        <!-- Vertebral Spine Column (Du Mai Line) -->
        <line x1="780" y1="235" x2="780" y2="560" stroke="#8a4d29" stroke-width="2.6" stroke-dasharray="4 3" />
        <!-- C7 Prominence (Dazhui / DU14) -->
        <circle cx="780" cy="263" r="5" fill="none" stroke="#8a4d29" stroke-width="2" />
        <!-- Scapula (Shoulder Blade T2-T7 on screen left) -->
        <path d="M 755,275 L 705,290 L 735,345 Z" fill="none" stroke="#8a4d29" stroke-width="2.0" />
        <!-- Posterior Ribs on screen left -->
        <path d="M 780,285 Q 735,295 700,315" fill="none" stroke="#8a4d29" stroke-width="1.4" />
        <path d="M 780,310 Q 730,325 695,350" fill="none" stroke="#8a4d29" stroke-width="1.4" />
        <path d="M 780,335 Q 730,355 690,380" fill="none" stroke="#8a4d29" stroke-width="1.4" />
        <path d="M 780,360 Q 730,385 690,410" fill="none" stroke="#8a4d29" stroke-width="1.4" />
        <!-- Posterior Iliac Crest (L4 level) -->
        <path d="M 780,485 Q 720,480 690,510" fill="none" stroke="#8a4d29" stroke-width="2.0" />
        <!-- Dimple of Venus (S2) -->
        <circle cx="762" cy="515" r="3" fill="none" stroke="#8a4d29" stroke-width="1.6" />
        <!-- Popliteal Knee Crease (BL40) -->
        <line x1="710" y1="676" x2="745" y2="676" stroke="#8a4d29" stroke-width="2" />
        <line x1="815" y1="676" x2="850" y2="676" stroke="#8a4d29" stroke-width="2" />
    </g>`;

    landmarksLayer.innerHTML = html;
}}

// Catmull-Rom to Cubic Bezier Curve Math
function catmullRomToBezier(points) {{
    if (!points || points.length < 2) return '';
    if (points.length === 2) {{
        return `M ${{points[0].x}},${{points[0].y}} L ${{points[1].x}},${{points[1].y}}`;
    }}
    let d = `M ${{points[0].x.toFixed(1)}},${{points[0].y.toFixed(1)}}`;
    for (let i = 0; i < points.length - 1; i++) {{
        const p0 = i > 0 ? points[i - 1] : points[i];
        const p1 = points[i];
        const p2 = points[i + 1];
        const p3 = i < points.length - 2 ? points[i + 2] : p2;

        const cp1x = p1.x + (p2.x - p0.x) / 6;
        const cp1y = p1.y + (p2.y - p0.y) / 6;
        const cp2x = p2.x - (p3.x - p1.x) / 6;
        const cp2y = p2.y - (p3.y - p1.y) / 6;

        d += ` C ${{cp1x.toFixed(1)}},${{cp1y.toFixed(1)}} ${{cp2x.toFixed(1)}},${{cp2y.toFixed(1)}} ${{p2.x.toFixed(1)}},${{p2.y.toFixed(1)}}`;
    }}
    return d;
}}

// Render Vector Splines for all 14 Meridians across Front, Back, and Side figures
function renderMeridians() {{
    let html = '';

    DATA.meridians.forEach(m => {{
        if (m.id === 'EX') return; // Extraordinary points are empirical without continuous channel

        const isTarget = (currentMeridian === 'ALL' || currentMeridian === m.id);
        const hex = m.color;
        const strokeW = isTarget && currentMeridian !== 'ALL' ? '4.5' : '2.2';
        const opacity = (currentMeridian === 'ALL') ? '0.78' : (isTarget ? '1.0' : '0.08');
        const filterStr = (isTarget && currentMeridian !== 'ALL') ? 'url(#glow)' : 'none';

        // 1. Front Figure Path (Right & Left)
        if (['LU', 'ST', 'SP', 'HT', 'PC', 'LV', 'REN', 'KI'].includes(m.id)) {{
            const ptsR = [];
            const ptsL = [];
            m.points.forEach(pk => {{
                const pt = DATA.points[pk];
                if (pt) {{
                    ptsR.push({{ x: pt.pos_2d.front.x, y: pt.pos_2d.front.y }});
                    if (pt.pos_2d.front.x !== pt.pos_2d.front.xl) {{
                        ptsL.push({{ x: pt.pos_2d.front.xl, y: pt.pos_2d.front.y }});
                    }}
                }}
            }});
            if (ptsR.length >= 2) {{
                html += `<path d="${{catmullRomToBezier(ptsR)}}" stroke="${{hex}}" stroke-width="${{strokeW}}" opacity="${{opacity}}" filter="${{filterStr}}" class="meridian-path ${{isTarget ? 'highlighted' : 'dimmed'}}" data-mid="${{m.id}}" style="--path-color: ${{hex}};" />`;
            }}
            if (ptsL.length >= 2 && m.id !== 'REN') {{
                html += `<path d="${{catmullRomToBezier(ptsL)}}" stroke="${{hex}}" stroke-width="${{strokeW}}" opacity="${{opacity}}" filter="${{filterStr}}" class="meridian-path ${{isTarget ? 'highlighted' : 'dimmed'}}" data-mid="${{m.id}}" style="--path-color: ${{hex}};" />`;
            }}
        }}

        // 2. Back Figure Path (Right & Left)
        if (['DU', 'BL', 'SI', 'SJ'].includes(m.id)) {{
            const ptsR = [];
            const ptsL = [];
            m.points.forEach(pk => {{
                const pt = DATA.points[pk];
                if (pt) {{
                    ptsR.push({{ x: pt.pos_2d.back.x, y: pt.pos_2d.back.y }});
                    if (pt.pos_2d.back.x !== pt.pos_2d.back.xl) {{
                        ptsL.push({{ x: pt.pos_2d.back.xl, y: pt.pos_2d.back.y }});
                    }}
                }}
            }});
            if (ptsR.length >= 2) {{
                html += `<path d="${{catmullRomToBezier(ptsR)}}" stroke="${{hex}}" stroke-width="${{strokeW}}" opacity="${{opacity}}" filter="${{filterStr}}" class="meridian-path ${{isTarget ? 'highlighted' : 'dimmed'}}" data-mid="${{m.id}}" style="--path-color: ${{hex}};" />`;
            }}
            if (ptsL.length >= 2 && m.id !== 'DU') {{
                html += `<path d="${{catmullRomToBezier(ptsL)}}" stroke="${{hex}}" stroke-width="${{strokeW}}" opacity="${{opacity}}" filter="${{filterStr}}" class="meridian-path ${{isTarget ? 'highlighted' : 'dimmed'}}" data-mid="${{m.id}}" style="--path-color: ${{hex}};" />`;
            }}
        }}

        // 3. Side Profile Figure Path (Gallbladder & Hand Yang on raised arm)
        if (['GB', 'SJ', 'LI'].includes(m.id)) {{
            const sidePts = [];
            m.points.forEach(pk => {{
                const pt = DATA.points[pk];
                if (pt) sidePts.push({{ x: pt.pos_2d.side.x, y: pt.pos_2d.side.y }});
            }});
            if (sidePts.length >= 2) {{
                html += `<path d="${{catmullRomToBezier(sidePts)}}" stroke="${{hex}}" stroke-width="${{strokeW}}" opacity="${{opacity}}" filter="${{filterStr}}" class="meridian-path ${{isTarget ? 'highlighted' : 'dimmed'}}" data-mid="${{m.id}}" style="--path-color: ${{hex}};" />`;
            }}
        }}
    }});

    meridiansLayer.innerHTML = html;
}}

// Render Interactive Acupoint Dots
function renderPoints() {{
    let html = '';

    for (const [code, pt] of Object.entries(DATA.points)) {{
        const belongsToMeridian = (currentMeridian === 'ALL' || currentMeridian === pt.pos_2d.channel);
        if (tier1Only && pt.importance_level !== 1) continue;

        let color = '#b91c1c';
        for (const m of DATA.meridians) {{
            if (m.points.includes(code)) {{
                color = m.color;
                break;
            }}
        }}

        const isSelected = (selectedPoint === code);
        const opacity = belongsToMeridian ? '1.0' : '0.12';
        const r = isSelected ? '6.0' : '4.2';

        // Front Figure Points
        if (['front', 'all'].includes(pt.pos_2d.primary) || ['REN', 'ST', 'SP', 'LU', 'HT', 'PC', 'LV'].includes(pt.pos_2d.channel)) {{
            html += renderPointElement(code, pt, pt.pos_2d.front.x, pt.pos_2d.front.y, color, r, opacity, isSelected);
        }}

        // Back Figure Points
        if (['back', 'all'].includes(pt.pos_2d.primary) || ['DU', 'BL', 'SI'].includes(pt.pos_2d.channel)) {{
            html += renderPointElement(code, pt, pt.pos_2d.back.x, pt.pos_2d.back.y, color, r, opacity, isSelected);
        }}

        // Side Figure Points
        if (['side', 'all'].includes(pt.pos_2d.primary) || ['GB', 'SJ', 'LI'].includes(pt.pos_2d.channel)) {{
            html += renderPointElement(code, pt, pt.pos_2d.side.x, pt.pos_2d.side.y, color, r, opacity, isSelected);
        }}
    }}

    pointsLayer.innerHTML = html;
    attachEventListeners();
}}

// Helper: Render individual point element
function renderPointElement(code, pt, x, y, color, r, opacity, isSelected) {{
    const label = `${{code}} ${{pt.hanzi || ''}}`;
    return `
    <g class="point-group" data-code="${{code}}" opacity="${{opacity}}" transform="translate(${{x}}, ${{y}})">
        <circle cx="0" cy="0" r="14" fill="transparent" />
        ${{isSelected ? `<circle cx="0" cy="0" r="16" fill="none" stroke="${{color}}" class="point-pulse" />` : ''}}
        <circle cx="0" cy="0" r="${{parseFloat(r) + 1.2}}" fill="#ffffff" opacity="0.9" />
        <circle cx="0" cy="0" r="${{r}}" fill="${{color}}" class="point-circle" />
        <text x="8" y="3.5" class="point-label">${{label}}</text>
    </g>`;
}}

// Attach Mouse and Touch Event Listeners
function attachEventListeners() {{
    document.querySelectorAll('.point-group').forEach(el => {{
        const code = el.getAttribute('data-code');
        const pt = DATA.points[code];

        el.addEventListener('click', (e) => {{
            e.stopPropagation();
            selectPoint(code);
        }});

        el.addEventListener('mouseenter', (e) => {{
            if (!pt) return;
            tooltip.style.display = 'block';
            tooltip.textContent = `${{code}} (${{pt.name}} / ${{pt.hanzi}}) • ${{pt.cat || ''}}`;
            moveTooltip(e);
        }});

        el.addEventListener('mousemove', moveTooltip);

        el.addEventListener('mouseleave', () => {{
            tooltip.style.display = 'none';
        }});
    }});

    document.querySelectorAll('.meridian-path').forEach(el => {{
        el.addEventListener('click', (e) => {{
            e.stopPropagation();
            const mid = el.getAttribute('data-mid');
            setMeridian(mid);
        }});
    }});
}}

function moveTooltip(e) {{
    const rect = stage.getBoundingClientRect();
    const x = e.clientX - rect.left + 14;
    const y = e.clientY - rect.top - 28;
    tooltip.style.left = `${{x}}px`;
    tooltip.style.top = `${{y}}px`;
}}

// Select and Display Acupoint Information
function selectPoint(code) {{
    selectedPoint = code;
    const pt = DATA.points[code];
    if (!pt) return;

    // Auto-focus view on the figure where the point appears
    if (currentView === 'full') {{
        setView(pt.pos_2d.primary);
    }}

    let meridianTitle = pt.pos_2d.channel;
    let mColor = '#b91c1c';
    for (const m of DATA.meridians) {{
        if (m.id === pt.pos_2d.channel) {{
            meridianTitle = `${{m.id}} • ${{m.fullName || m.name}}`;
            mColor = m.color;
            break;
        }}
    }}

    // Populate Info Card
    document.getElementById('c-title').textContent = `${{code}} (${{pt.name}} / ${{pt.hanzi}})`;
    document.getElementById('c-eng').textContent = pt.eng || 'National Standard Acupoint Landmark';

    const badgesDiv = document.getElementById('c-badges');
    badgesDiv.innerHTML = `
        <span class="badge badge-channel" style="color: ${{mColor}}; border-color: ${{mColor}};">${{meridianTitle}}</span>
        <span class="badge badge-category">${{pt.cat || 'Standard Point'}}</span>
        ${{pt.importance_level === 1 ? '<span class="badge" style="background:#fee2e2; color:#b91c1c; border:1px solid #f87171;">🔥 Tier 1 High Yield (Must-Know)</span>' : ''}}
    `;

    document.getElementById('c-loc').textContent = pt.loc || 'Official GB/T 12346 location.';
    document.getElementById('c-act').textContent = pt.act || 'Regulates Qi and Blood, harmonizes organ systems.';
    document.getElementById('c-saf').textContent = pt.saf || 'Perpendicular insertion according to textbook standard.';

    pointCard.style.display = 'block';

    renderPoints();
}}

// Select Active Meridian Filter
function setMeridian(mid) {{
    currentMeridian = mid;

    document.querySelectorAll('.m-pill').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('data-mid') === mid);
    }});

    if (mid === 'ALL') {{
        ribbonTitle.innerHTML = '<span>⚡ All 14 Primary Channels Active</span>';
        ribbonMeta.innerHTML = '<span>Click any meridian or point marker to inspect Six-Division pathways, Cun landmarks, and clinical actions.</span>';
    }} else {{
        const m = DATA.meridians.find(item => item.id === mid);
        if (m) {{
            ribbonTitle.innerHTML = `<span style="color: ${{m.color}};">⚡ ${{m.fullName || m.name}}</span>`;
            ribbonMeta.innerHTML = `<span><strong>Division:</strong> ${{m.division}} | <strong>Element:</strong> ${{m.element}} | <strong>Organ Clock:</strong> ${{m.time}}</span>`;

            // Auto-switch view to primary figure for this channel
            if (currentView !== 'full' && m.primaryView) {{
                setView(m.primaryView);
            }}
        }}
    }}

    renderMeridians();
    renderPoints();
}}

// Switch View Camera with smooth animated viewBox transition
function setView(viewMode) {{
    currentView = viewMode;
    document.querySelectorAll('#view-selector .v-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('data-view') === viewMode);
    }});

    const preset = VIEW_PRESETS[viewMode] || VIEW_PRESETS.full;
    animateViewBox(preset.x, preset.y, preset.w, preset.h);
}}

function animateViewBox(targetX, targetY, targetW, targetH) {{
    const startX = vb.x, startY = vb.y, startW = vb.w, startH = vb.h;
    const duration = 320;
    const startTime = performance.now();

    function step(now) {{
        const progress = Math.min((now - startTime) / duration, 1);
        const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
        vb.x = startX + (targetX - startX) * ease;
        vb.y = startY + (targetY - startY) * ease;
        vb.w = startW + (targetW - startW) * ease;
        vb.h = startH + (targetH - startH) * ease;

        updateViewBox();
        if (progress < 1) requestAnimationFrame(step);
    }}
    requestAnimationFrame(step);
}}

// Initialize Meridian Filter Pills Bar
function initPillsBar() {{
    const bar = document.getElementById('pills-bar');
    DATA.meridians.forEach(m => {{
        const btn = document.createElement('button');
        btn.className = 'm-pill';
        btn.setAttribute('data-mid', m.id);
        btn.innerHTML = `<span class="dot" style="background: ${{m.color}};"></span>${{m.id}}: ${{m.name.split(' ')[0]}} (${{m.chinese}})`;
        btn.onclick = () => setMeridian(m.id);
        bar.appendChild(btn);
    }});
}}

// Search Filter Handler
function handleSearch(query) {{
    query = query.trim().toUpperCase();
    if (!query) {{
        clearSearchBtn.style.display = 'none';
        return;
    }}
    clearSearchBtn.style.display = 'block';

    let matchedCode = null;
    for (const [code, pt] of Object.entries(DATA.points)) {{
        if (code === query ||
            (pt.name && pt.name.toUpperCase() === query) ||
            (pt.hanzi && pt.hanzi === query)) {{
            matchedCode = code;
            break;
        }}
    }}

    if (!matchedCode && query.length >= 2) {{
        for (const [code, pt] of Object.entries(DATA.points)) {{
            if (code.includes(query) ||
                (pt.name && pt.name.toUpperCase().includes(query)) ||
                (pt.hanzi && pt.hanzi.includes(query))) {{
                matchedCode = code;
                break;
            }}
        }}
    }}

    if (matchedCode) {{
        selectPoint(matchedCode);
    }}
}}

// Native SVG Camera Pan & Zoom Engine (Zero drift, 100% unified)
stage.addEventListener('wheel', (e) => {{
    e.preventDefault();
    const factor = e.deltaY < 0 ? 0.86 : 1.16;
    const rect = svg.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    const newW = Math.min(Math.max(vb.w * factor, 250), 2200);
    const newH = Math.min(Math.max(vb.h * factor, 156), 1375);

    const mouseRatioX = mouseX / rect.width;
    const mouseRatioY = mouseY / rect.height;

    vb.x += (vb.w - newW) * mouseRatioX;
    vb.y += (vb.h - newH) * mouseRatioY;
    vb.w = newW;
    vb.h = newH;

    updateViewBox();
}}, {{ passive: false }});

stage.addEventListener('mousedown', (e) => {{
    if (e.target.closest('.point-group') || e.target.closest('.floating-controls') || e.target.closest('.point-detail-card')) return;
    isPanning = true;
    startX = e.clientX;
    startY = e.clientY;
    startVbX = vb.x;
    startVbY = vb.y;
    stage.classList.add('panning');
}});

window.addEventListener('mousemove', (e) => {{
    if (!isPanning) return;
    const rect = svg.getBoundingClientRect();
    const dx = (e.clientX - startX) * (vb.w / rect.width);
    const dy = (e.clientY - startY) * (vb.h / rect.height);
    vb.x = startVbX - dx;
    vb.y = startVbY - dy;
    updateViewBox();
}});

window.addEventListener('mouseup', () => {{
    isPanning = false;
    stage.classList.remove('panning');
}});

// Touch Events for Mobile (Pinch-to-zoom & pan)
let initialTouchDist = 0;
let initialVbW = 0, initialVbH = 0;

stage.addEventListener('touchstart', (e) => {{
    if (e.touches.length === 1) {{
        isPanning = true;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        startVbX = vb.x;
        startVbY = vb.y;
    }} else if (e.touches.length === 2) {{
        isPanning = false;
        initialTouchDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
        );
        initialVbW = vb.w;
        initialVbH = vb.h;
    }}
}}, {{ passive: true }});

stage.addEventListener('touchmove', (e) => {{
    const rect = svg.getBoundingClientRect();
    if (isPanning && e.touches.length === 1) {{
        const dx = (e.touches[0].clientX - startX) * (vb.w / rect.width);
        const dy = (e.touches[0].clientY - startY) * (vb.h / rect.height);
        vb.x = startVbX - dx;
        vb.y = startVbY - dy;
        updateViewBox();
    }} else if (e.touches.length === 2 && initialTouchDist > 0) {{
        const dist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
        );
        const factor = initialTouchDist / dist;
        vb.w = Math.min(Math.max(initialVbW * factor, 250), 2200);
        vb.h = Math.min(Math.max(initialVbH * factor, 156), 1375);
        updateViewBox();
    }}
}}, {{ passive: true }});

stage.addEventListener('touchend', () => {{
    isPanning = false;
    initialTouchDist = 0;
}});

// Event Listeners for UI Controls
document.getElementById('view-selector').addEventListener('click', (e) => {{
    const btn = e.target.closest('.v-btn');
    if (btn) setView(btn.getAttribute('data-view'));
}});

searchInput.addEventListener('input', (e) => handleSearch(e.target.value));

clearSearchBtn.addEventListener('click', () => {{
    searchInput.value = '';
    clearSearchBtn.style.display = 'none';
}});

document.getElementById('toggle-labels-btn').addEventListener('click', function() {{
    showLabels = !showLabels;
    this.classList.toggle('active', showLabels);
    svg.classList.toggle('show-labels', showLabels);
}});

document.getElementById('toggle-tier1-btn').addEventListener('click', function() {{
    tier1Only = !tier1Only;
    this.classList.toggle('active', tier1Only);
    renderPoints();
}});

document.getElementById('theme-select').addEventListener('change', (e) => {{
    document.documentElement.setAttribute('data-theme', e.target.value);
}});

document.getElementById('c-close').addEventListener('click', () => {{
    pointCard.style.display = 'none';
    selectedPoint = null;
    renderPoints();
}});

document.getElementById('zoom-in').onclick = () => {{
    vb.w *= 0.8;
    vb.h *= 0.8;
    updateViewBox();
}};

document.getElementById('zoom-out').onclick = () => {{
    vb.w *= 1.25;
    vb.h *= 1.25;
    updateViewBox();
}};

document.getElementById('zoom-reset').onclick = () => {{
    setView('full');
}};

window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') {{
        pointCard.style.display = 'none';
        selectedPoint = null;
        renderPoints();
    }}
}});

// Initialize
initPillsBar();
renderBodyFigures();
renderLandmarks();
renderMeridians();
renderPoints();
updateViewBox();
</script>
</body>
</html>"""

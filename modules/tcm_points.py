"""TCM Point Nomenclature & Bilingual Formatter.

Provides standardized bilingual representations for acupuncture points, including:
- Alphanumeric Code (e.g. ST36)
- Pinyin Name (e.g. Zusanli)
- Chinese Hanzi (e.g. 足三里)
- English Translation (e.g. Leg Three Miles)
"""

import re
from typing import Dict, Tuple

# Comprehensive Acupuncture Points Dictionary: Code -> (Pinyin, Hanzi, English)
POINT_DICTIONARY: Dict[str, Tuple[str, str, str]] = {
    # Stomach Channel (Foot-Yangming)
    "ST36": ("Zusanli", "足三里", "Leg Three Miles"),
    "ST35": ("Dubi", "犊鼻", "Calf's Nose"),
    "ST38": ("Tiaokou", "条口", "Ribbon Opening"),
    "ST25": ("Tianshu", "天枢", "Heaven's Pivot"),
    "ST40": ("Fenglong", "丰隆", "Abundant Bulge"),
    "ST44": ("Neiting", "内庭", "Inner Courtyard"),
    "ST8": ("Touwei", "头维", "Head Corner"),
    
    # Large Intestine Channel (Hand-Yangming)
    "LI4": ("Hegu", "合谷", "Joining Valley"),
    "LI11": ("Quchi", "曲池", "Pool at the Crook"),
    "LI15": ("Jianyu", "肩髃", "Shoulder Bone"),
    "LI20": ("Yingxiang", "迎香", "Welcome Fragrance"),
    "LI10": ("Shousanli", "手三里", "Arm Three Miles"),
    
    # Spleen Channel (Foot-Taiyin)
    "SP6": ("Sanyinjiao", "三阴交", "Three Yin Intersection"),
    "SP9": ("Yinlingquan", "阴陵泉", "Yin Mound Spring"),
    "SP10": ("Xuehai", "血海", "Sea of Blood"),
    "SP3": ("Taibai", "太白", "Supreme White"),
    "SP4": ("Gongsun", "公孙", "Yellow Emperor / Grandfather-Grandson"),
    
    # Bladder Channel (Foot-Taiyang)
    "BL1": ("Jingming", "睛明", "Bright Eyes"),
    "BL2": ("Zanzhu", "攒竹", "Gathered Bamboo"),
    "BL10": ("Tianzhu", "天柱", "Celestial Pillar"),
    "BL13": ("Feishu", "肺俞", "Lung Shu"),
    "BL15": ("Xinshu", "心俞", "Heart Shu"),
    "BL18": ("Ganshu", "肝俞", "Liver Shu"),
    "BL20": ("Pishu", "脾俞", "Spleen Shu"),
    "BL23": ("Shenshu", "肾俞", "Kidney Shu"),
    "BL40": ("Weizhong", "委中", "Middle of the Crease"),
    "BL52": ("Zhishi", "志室", "Residence of the Will"),
    "BL60": ("Kunlun", "昆仑", "Kunlun Mountains"),
    "BL67": ("Zhiyin", "至阴", "Reaching Yin"),
    
    # Kidney Channel (Foot-Shaoyin)
    "KI1": ("Yongquan", "涌泉", "Gushing Spring"),
    "KI3": ("Taixi", "太溪", "Supreme Stream"),
    "KI6": ("Zhaohai", "照海", "Shining Sea"),
    "KI7": ("Fuliu", "复溜", "Recover Flow"),
    
    # Liver Channel (Foot-Jueyin)
    "LV3": ("Taichong", "太冲", "Great Surge"),
    "LV2": ("Xingjian", "行间", "Moving Between"),
    "LV8": ("Ququan", "曲泉", "Spring at the Crook"),
    "LV14": ("Qimen", "期门", "Cycle Gate"),
    
    # Gallbladder Channel (Foot-Shaoyang)
    "GB20": ("Fengchi", "风池", "Wind Pool"),
    "GB21": ("Jianjing", "肩井", "Shoulder Well"),
    "GB30": ("Huantiao", "环跳", "Jumping Circle"),
    "GB34": ("Yanglingquan", "阳陵泉", "Yang Mound Spring"),
    "GB41": ("Zulinqi", "足临泣", "Foot Overlooking Tears"),
    
    # Lung Channel (Hand-Taiyin)
    "LU1": ("Zhongfu", "中府", "Middle Palace"),
    "LU5": ("Chize", "尺泽", "Cubit Marsh"),
    "LU7": ("Lieque", "列缺", "Broken Sequence"),
    "LU9": ("Taiyuan", "太渊", "Supreme Abyss"),
    "LU11": ("Shaoshang", "少商", "Lesser Shang"),
    
    # Heart Channel (Hand-Shaoyin)
    "HT3": ("Shaohai", "少海", "Lesser Sea"),
    "HT7": ("Shenmen", "神门", "Spirit Gate"),
    "HT8": ("Shaofu", "少府", "Lesser Mansion"),
    
    # Small Intestine Channel (Hand-Taiyang)
    "SI3": ("Houxi", "后溪", "Back Stream"),
    "SI9": ("Jianzhen", "肩贞", "True Shoulder"),
    "SI19": ("Tinggong", "听宫", "Palace of Hearing"),
    
    # Pericardium Channel (Hand-Jueyin)
    "PC6": ("Neiguan", "内关", "Inner Pass"),
    "PC7": ("Daling", "大陵", "Great Mound"),
    "PC8": ("Laogong", "劳宫", "Palace of Toil"),
    
    # San Jiao / Triple Energizer Channel (Hand-Shaoyang)
    "TE5": ("Waiguan", "外关", "Outer Pass"),
    "SJ5": ("Waiguan", "外关", "Outer Pass"),
    "TE14": ("Jianliao", "肩髎", "Shoulder Crevice"),
    "SJ14": ("Jianliao", "肩髎", "Shoulder Crevice"),
    "TE17": ("Yifeng", "翳风", "Wind Screen"),
    "SJ17": ("Yifeng", "翳风", "Wind Screen"),
    
    # Du Vessel (Governing Vessel)
    "DU4": ("Mingmen", "命门", "Gate of Life"),
    "DU14": ("Dazhui", "大椎", "Great Vertebra"),
    "DU20": ("Baihui", "百会", "Hundred Convergences"),
    "DU24": ("Shenting", "神庭", "Courtyard of the Spirit"),
    "GV4": ("Mingmen", "命门", "Gate of Life"),
    "GV14": ("Dazhui", "大椎", "Great Vertebra"),
    "GV20": ("Baihui", "百会", "Hundred Convergences"),
    
    # Ren Vessel (Conception Vessel)
    "CV4": ("Guanyuan", "关元", "Gate of Origin"),
    "CV6": ("Qihai", "气海", "Sea of Qi"),
    "CV8": ("Shenque", "神阙", "Spirit Gate / Umbilicus"),
    "CV12": ("Zhongwan", "中脘", "Middle Cavity"),
    "CV17": ("Danzhong", "膻中", "Chest Center / Sea of Qi"),
    "RN4": ("Guanyuan", "关元", "Gate of Origin"),
    "RN6": ("Qihai", "气海", "Sea of Qi"),
    "RN12": ("Zhongwan", "中脘", "Middle Cavity"),
    
    # Extra Points (奇穴)
    "YINTANG": ("Yintang", "印堂", "Hall of Impression"),
    "TAIYANG": ("Taiyang", "太阳", "Greater Yang"),
    "ANMIAN": ("Anmian", "安眠", "Peaceful Sleep"),
    "JIANNEILING": ("Jianneiling", "肩内陵", "Inner Shoulder Mound"),
    "YAOTONGXUE": ("Yaotongxue", "腰痛穴", "Lumbar Pain Point"),
    "BAXIE": ("Baxie", "八邪", "Eight Pathogens"),
    "BAFENG": ("Bafeng", "八风", "Eight Winds"),
    "SIFENG": ("Sifeng", "四缝", "Four Seams"),
    "SHIXUAN": ("Shixuan", "十宣", "Ten Diffusions"),
    "HEDING": ("Heding", "鹤顶", "Crane's Crown"),
    "XIYAN": ("Xiyan", "膝眼", "Eyes of the Knee")
}

# Auto-enrich POINT_DICTIONARY with canonical dataset from fitted_points.json
from pathlib import Path
import json

_fitted_json = Path(__file__).resolve().parent.parent / "static" / "fitted_points.json"
if _fitted_json.exists():
    try:
        with open(_fitted_json, "r", encoding="utf-8") as _f:
            _pts_data = json.load(_f)
            for _k, _v in _pts_data.items():
                if _k not in POINT_DICTIONARY and "name" in _v and "hanzi" in _v:
                    POINT_DICTIONARY[_k] = (_v["name"], _v["hanzi"], _v.get("cat", ""))
    except Exception:
        pass


def get_point_bilingual_name(point_code: str) -> str:
    """Format an acupuncture point code into bilingual name (Code, Pinyin & Hanzi).
    
    Example: 'ST36' -> 'ST36 (Zusanli / 足三里)'
    """
    clean_code = point_code.strip().upper()
    if clean_code in POINT_DICTIONARY:
        pinyin, hanzi, _ = POINT_DICTIONARY[clean_code]
        return f"{clean_code} ({pinyin} / {hanzi})"
    return clean_code


def format_point_bilingual(text: str) -> str:
    """Scan text and replace occurrences of acupuncture point codes with bilingual names (Pinyin & Hanzi), stripping any English translation suffixes."""
    if not text:
        return text
        
    # First, strip any existing English translations inside parentheses:
    # e.g. ST36 (Zusanli / 足三里 - Leg Three Miles) -> ST36 (Zusanli / 足三里)
    text = re.sub(r'(\([A-Za-z0-9\s/]+/\s*[\u4e00-\u9fff]+)\s*-\s*[A-Za-z0-9\s\'\-/]+(\))', r'\1\2', text)
    
    # Match point code NOT already followed by a parenthetical name
    pattern = r'\b(ST\d{1,2}|LI\d{1,2}|SP\d{1,2}|BL\d{1,2}|KI\d{1,2}|LV\d{1,2}|LR\d{1,2}|GB\d{1,2}|LU\d{1,2}|HT\d{1,2}|SI\d{1,2}|PC\d{1,2}|TE\d{1,2}|SJ\d{1,2}|DU\d{1,2}|GV\d{1,2}|CV\d{1,2}|RN\d{1,2}|YINTANG|TAIYANG|ANMIAN|JIANNEILING|YAOTONGXUE|HEDING|XIYAN|SISHENCONG|DINGCHUAN|HUATUOJIAJI|SIFENG|SHIXUAN|BAXIE|BAFENG|DANNANGXUE|LANWEIXUE|ZIGONG)\b(?!\s*\([A-Za-z\s/]+/\s*[\u4e00-\u9fff]+)'
    
    def replace_match(match):
        code = match.group(1).upper()
        return get_point_bilingual_name(code)
        
    formatted = re.sub(pattern, replace_match, text, flags=re.IGNORECASE)
    # Clean up double expansions if text was already partially expanded
    formatted = re.sub(r'(\([^\)]+\))\s*\1', r'\1', formatted)
    return formatted

# -*- coding: utf-8 -*-
"""TCM Internal Illness Diagnostics Module.

Comprehensive clinical diagnostic engine for internal diseases based on the Four
Examinations (Inspection, Auscultation/Olfaction, Inquiry, Palpation - 望闻问切).
Allows practitioners to select presenting symptoms across body systems, pulse qualities,
and tongue characteristics to calculate pattern differentiation (辨证) with treatment principles,
cardinal acupuncture prescriptions, herbal formulas (方剂), and dietary/lifestyle guidance.
"""

import streamlit as st
from typing import Dict, List, Any, Tuple
from datetime import date


# =============================================================================
# KNOWLEDGE BASE: 26 CANONICAL TCM ZANG-FU & EIGHT PRINCIPLES PATTERNS
# =============================================================================
DIAGNOSTIC_PATTERNS: List[Dict[str, Any]] = [
    # --- EXTERIOR / RESPIRATORY PATTERNS ---
    {
        "id": "wind-cold-lung",
        "name": "Wind-Cold Invading Lung",
        "chinese": "风寒束肺 (Fēng Hán Shù Fèi)",
        "organ": "Lung (肺)",
        "category": "Exterior / Respiratory",
        "nature": "Exterior Cold (表寒)",
        "description": "Exogenous pathogenic Wind and Cold invade the skin and defensive Qi, impairing the Lung's dispersing and descending functions.",
        "key_symptoms": [
            "aversion_to_cold", "runny_nose_clear", "cough_clear_white",
            "absence_of_sweat", "headache_occipital", "body_aches"
        ],
        "secondary_symptoms": [
            "nasal_congestion", "stiff_neck", "low_fever", "dry_itchy_throat"
        ],
        "tongue_body": ["Normal Pale Red", "Pale / Whitish"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist", "Wet / Moist / Slippery"],
        "pulses": ["Floating (浮)", "Tight (紧)"],
        "pathomechanism": "Wind-Cold constricts the pores and impedes Wei Qi circulation, causing chills and absence of sweat. Lung Qi fails to descend, creating cough with thin white mucus.",
        "treatment_principle": "Release the exterior, dispel Cold, and restore the dispersing and descending functions of the Lung (辛温解表，宣肺止咳).",
        "acupuncture_points": [
            {"code": "LU7", "name": "Lieque (列缺)", "role": "Cardinal Luo-Connecting Point", "technique": "Reducing (泻法)", "rationale": "Opens the Ren channel, releases exterior wind, restores Lung descending function."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Dispels wind, induces sweating, relieves facial/head discomfort."},
            {"code": "BL12", "name": "Fengmen (风门)", "role": "Gate of Wind", "technique": "Reducing / Cupping", "rationale": "Expels pathogenic exterior wind from the upper back."},
            {"code": "BL13", "name": "Feishu (肺俞)", "role": "Lung Back-Shu Point", "technique": "Reinforcing or Moxa", "rationale": "Regulates Lung Qi and stops cough."},
            {"code": "GB20", "name": "Fengchi (风池)", "role": "Wind Pool", "technique": "Reducing (泻法)", "rationale": "Clears occipital headache and dispels exterior wind."}
        ],
        "herbal_formula": {
            "name": "Jing Fang Bai Du San / Ma Huang Tang",
            "chinese": "荆防败毒散 / 麻黄汤",
            "key_herbs": "Jing Jie, Fang Feng, Qiang Huo, Du Huo, Chai Hu, Qian Hu, Jie Geng, Zhi Ke, Fu Ling, Chuan Xiong, Gan Cao",
            "action": "Induces diaphoresis to release the exterior, disperses pathogenic Wind-Cold, and diffuses Lung Qi."
        },
        "lifestyle_diet": {
            "recommended": "Warm scallion and ginger broth, fresh peppermint tea, garlic, warming soups, adequate hydration.",
            "avoid": "Cold drinks, ice cream, raw salads, greasy foods, dairy.",
            "advice": "Rest in a warm draft-free room. Wear a scarf to protect the back of the neck (Fengchi GB20)."
        }
    },
    {
        "id": "wind-heat-lung",
        "name": "Wind-Heat Invading Lung",
        "chinese": "风热犯肺 (Fēng Rè Fàn Fèi)",
        "organ": "Lung (肺)",
        "category": "Exterior / Respiratory",
        "nature": "Exterior Heat (表热)",
        "description": "Exogenous pathogenic Wind-Heat attacks the exterior and the Lung orifice, producing fever, sore throat, and yellow discharge.",
        "key_symptoms": [
            "high_fever", "sore_swollen_throat", "cough_yellow_sticky",
            "runny_nose_yellow", "slight_sweat", "thirst_cold"
        ],
        "secondary_symptoms": [
            "headache_frontal", "red_irritated_eyes", "slight_chills", "nasal_congestion"
        ],
        "tongue_body": ["Normal Pale Red", "Red / Scarlet (Tip/Edges)"],
        "tongue_coat": ["Thin Yellow", "Thick Yellow"],
        "tongue_moisture": ["Dry / Lack of Fluids", "Normal Moist"],
        "pulses": ["Floating (浮)", "Rapid (数)"],
        "pathomechanism": "Wind-Heat invades via mouth and nose. Heat burns body fluids, transforming mucus into thick yellow phlegm and inflaming the throat.",
        "treatment_principle": "Dispel Wind, clear Heat, and soothe the throat (辛凉解表，清热宣肺).",
        "acupuncture_points": [
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point (Earth)", "technique": "Reducing (泻法)", "rationale": "Potent systemic point for clearing interior and exterior heat."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Dispels wind-heat from the head, face, and respiratory tract."},
            {"code": "LU11", "name": "Shaoshang (少商)", "role": "Jing-Well Point", "technique": "Bleeding (刺络放血)", "rationale": "Puncture to bleed 1-2 drops for severe sore, swollen throat."},
            {"code": "LU5", "name": "Chize (尺泽)", "role": "He-Sea Point (Water)", "technique": "Reducing (泻法)", "rationale": "Clears heat from Lung and descends rebellious cough."},
            {"code": "DU14", "name": "Dazhui (大椎)", "role": "Meeting of Yang Channels", "technique": "Reducing / Cupping", "rationale": "Reduces high fever and dispels pathogenic heat."}
        ],
        "herbal_formula": {
            "name": "Yin Qiao San (Lonicera and Forsythia Powder)",
            "chinese": "银翘散",
            "key_herbs": "Jin Yin Hua, Lian Qiao, Bo He, Niu Bang Zi, Jie Geng, Dan Dou Chi, Jing Jie Sui, Dan Zhu Ye, Lu Gen, Gan Cao",
            "action": "Dispels wind-heat, clears toxins, and soothes the throat."
        },
        "lifestyle_diet": {
            "recommended": "Chrysanthemum tea, peppermint tea, pear juice, watermelon, mung bean soup, daikon radish.",
            "avoid": "Spicy food, deep-fried food, alcohol, lamb, heavy meats.",
            "advice": "Hydrate frequently with lukewarm or cooling fluids. Gargle with saltwater."
        }
    },
    {
        "id": "lung-qi-deficiency",
        "name": "Lung Qi Deficiency",
        "chinese": "肺气虚 (Fèi Qì Xū)",
        "organ": "Lung (肺)",
        "category": "Deficiency Patterns",
        "nature": "Interior Deficiency (里虚)",
        "description": "Chronic illness, constitutional weakness, or prolonged coughing depletes Lung Qi, weakening respiration and Defensive (Wei) Qi.",
        "key_symptoms": [
            "shortness_of_breath", "weak_low_voice", "spontaneous_sweating",
            "fatigue_exhaustion", "aversion_to_cold", "cough_weak"
        ],
        "secondary_symptoms": [
            "frequent_colds", "pale_complexion", "daytime_drowsiness"
        ],
        "tongue_body": ["Pale / Whitish"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Weak / Empty (弱/虚)", "Fine / Thready (细)"],
        "pathomechanism": "Lung governs Qi and respiration while dispersing defensive Qi to the skin. Deficiency produces weak breathing, soft speech, and spontaneous sweat due to unstable pores.",
        "treatment_principle": "Tonify Lung Qi, strengthen Defensive Qi, and secure the exterior (补益肺气，固表止汗).",
        "acupuncture_points": [
            {"code": "BL13", "name": "Feishu (肺俞)", "role": "Lung Back-Shu Point", "technique": "Reinforcing + Moxa (补法灸)", "rationale": "Directly supplements and nourishes Lung organ Qi."},
            {"code": "LU9", "name": "Taiyuan (太渊)", "role": "Yuan-Source / Hui-Meeting for Vessels", "technique": "Reinforcing (补法)", "rationale": "Earth point of Lung channel; tonifies mother to tonify child."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Reinforcing + Moxa", "rationale": "Tonifies Spleen Earth to generate Lung Metal."},
            {"code": "RN6", "name": "Qihai (气海)", "role": "Sea of Qi", "technique": "Reinforcing + Moxa", "rationale": "Strengthens systemic Qi and builds constitutional resistance."},
            {"code": "RN12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Reinforcing (补法)", "rationale": "Builds postnatal root to support respiratory vitality."}
        ],
        "herbal_formula": {
            "name": "Yu Ping Feng San (Jade Windscreen Powder)",
            "chinese": "玉屏风散",
            "key_herbs": "Huang Qi (Astragalus), Bai Zhu (Atractylodes), Fang Feng (Saposhnikovia)",
            "action": "Fortifies defensive Qi, stops spontaneous perspiration, and builds immunity."
        },
        "lifestyle_diet": {
            "recommended": "Sweet potato, oats, astragalus broth, chicken broth, cooked carrots, chestnuts, jujube dates.",
            "avoid": "Cold raw foods, iced drinks, dairy, excessive physical exhaustion.",
            "advice": "Practice deep diaphragmatic breathing and gentle Qi Gong exercises. Avoid cold drafts."
        }
    },
    {
        "id": "phlegm-damp-lung",
        "name": "Phlegm-Damp Obstructing Lung",
        "chinese": "痰湿阻肺 (Tán Shī Zǔ Fèi)",
        "organ": "Lung (肺)",
        "category": "Exterior / Respiratory",
        "nature": "Interior Excess (里实)",
        "description": "Spleen fails to transform fluids, generating phlegm that ascends and accumulates in the Lung, creating chronic productive cough and chest fullness.",
        "key_symptoms": [
            "cough_clear_white", "chest_fullness", "heaviness_limbs",
            "poor_appetite", "bloating_after_eating"
        ],
        "secondary_symptoms": [
            "shortness_of_breath", "nausea_vomiting", "fatigue_exhaustion", "loose_stools"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thick White", "Greasy / Turbid"],
        "tongue_moisture": ["Wet / Moist / Slippery"],
        "pulses": ["Slippery (滑)", "Soggy / Soft (濡)"],
        "pathomechanism": "'Spleen is the mother of phlegm; Lung is the reservoir of phlegm.' Excess mucus blocks airway pathways, causing wheezing, rattling sputum, and chest oppression.",
        "treatment_principle": "Strengthen Spleen to dry Dampness, transform Phlegm, and descend Lung Qi (健脾燥湿，化痰止咳).",
        "acupuncture_points": [
            {"code": "ST40", "name": "Fenglong (丰隆)", "role": "Luo-Connecting Point", "technique": "Reducing / Harmonizing", "rationale": "The single most famous empirical point in TCM for resolving all phlegm."},
            {"code": "LU5", "name": "Chize (尺泽)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Descends rebellious Lung Qi and opens the airway."},
            {"code": "BL13", "name": "Feishu (肺俞)", "role": "Lung Back-Shu Point", "technique": "Harmonizing (平补平泻)", "rationale": "Regulates Lung Qi exchange."},
            {"code": "BL20", "name": "Pishu (脾俞)", "role": "Spleen Back-Shu Point", "technique": "Reinforcing + Moxa", "rationale": "Strengthens fluid metabolism at the source in the Spleen."},
            {"code": "RN12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Reinforcing + Moxa", "rationale": "Transforms Middle Burner dampness and phlegm."}
        ],
        "herbal_formula": {
            "name": "Er Chen Tang (Two-Cured Decoction)",
            "chinese": "二陈汤",
            "key_herbs": "Ban Xia, Chen Pi, Fu Ling, Zhi Gan Cao, Sheng Jiang, Wu Mei",
            "action": "Dries dampness, transforms phlegm, regulates Qi, and harmonizes the middle burner."
        },
        "lifestyle_diet": {
            "recommended": "Barley tea, Job's tears (Yi Yi Ren), cooked daikon, ginger, tangerine peel, cardamom.",
            "avoid": "Dairy, cheese, bananas, deep-fried food, refined sugar, cold/raw food.",
            "advice": "Keep the abdomen and chest warm. Avoid damp living environments."
        }
    },

    # --- DIGESTIVE / SPLEEN & STOMACH PATTERNS ---
    {
        "id": "spleen-qi-deficiency",
        "name": "Spleen Qi Deficiency",
        "chinese": "脾气虚 (Pí Qì Xū)",
        "organ": "Spleen (脾)",
        "category": "Deficiency Patterns",
        "nature": "Interior Deficiency (里虚)",
        "description": "Weakness of the Spleen's transformation and transportation function, leading to chronic digestive sluggishness, muscle weakness, and fatigue.",
        "key_symptoms": [
            "poor_appetite", "bloating_after_eating", "loose_stools",
            "fatigue_exhaustion", "weak_limbs"
        ],
        "secondary_symptoms": [
            "shortness_of_breath", "pale_complexion", "daytime_drowsiness", "dizziness_vertigo"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist", "Wet / Moist / Slippery"],
        "pulses": ["Weak / Empty (弱/虚)", "Soggy / Soft (濡)"],
        "pathomechanism": "Spleen governs digestion and the four limbs. When Spleen Qi is deficient, grain food cannot be transformed, causing postprandial fullness, loose stools, and lack of energy.",
        "treatment_principle": "Tonify Spleen Qi and strengthen transformation and transportation (健脾益气，和胃消胀).",
        "acupuncture_points": [
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point (Earth)", "technique": "Reinforcing + Moxa", "rationale": "Primary point in the body to tonify Qi, Blood, and Middle Jiao."},
            {"code": "SP3", "name": "Taibai (太白)", "role": "Yuan-Source / Shu-Stream (Earth)", "technique": "Reinforcing (补法)", "rationale": "Source point on Earth channel; directly tonifies Spleen."},
            {"code": "BL20", "name": "Pishu (脾俞)", "role": "Spleen Back-Shu Point", "technique": "Reinforcing + Moxa", "rationale": "Infuses Yang Qi into the Spleen."},
            {"code": "RN12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Reinforcing + Moxa", "rationale": "Harmonizes Stomach Qi and stimulates digestion."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Strengthens Spleen, resolves dampness, nourishes blood."}
        ],
        "herbal_formula": {
            "name": "Si Jun Zi Tang (Four Gentlemen Decoction)",
            "chinese": "四君子汤",
            "key_herbs": "Ren Shen (or Dang Shen), Bai Zhu, Fu Ling, Zhi Gan Cao",
            "action": "Tonifies Spleen and Stomach Qi without cloying."
        },
        "lifestyle_diet": {
            "recommended": "Warm cooked rice, millet congee, pumpkin, yams, oats, ginger, lean meats, stewed apples.",
            "avoid": "Cold salads, iced drinks, raw vegetables, excessive dairy, greasy fried foods.",
            "advice": "Eat small, frequent, warm meals. Chew thoroughly in a calm dining environment."
        }
    },
    {
        "id": "spleen-yang-deficiency",
        "name": "Spleen Yang Deficiency",
        "chinese": "脾阳虚 (Pí Yáng Xū)",
        "organ": "Spleen (脾)",
        "category": "Deficiency Patterns",
        "nature": "Interior Cold / Deficiency (里虚寒)",
        "description": "Progressive progression of Spleen Qi deficiency with deficiency of physiological warmth, resulting in internal Cold, watery diarrhea, and cold limbs.",
        "key_symptoms": [
            "cold_limbs", "watery_diarrhea", "dull_abdominal_pain_warmth",
            "poor_appetite", "bloating_after_eating", "fatigue_exhaustion"
        ],
        "secondary_symptoms": [
            "edema_swelling", "pale_profuse_urine", "chilled_abdomen"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thin White", "Thick White"],
        "tongue_moisture": ["Wet / Moist / Slippery"],
        "pulses": ["Deep (沉)", "Slow (迟)", "Weak / Empty (弱/虚)"],
        "pathomechanism": "Deficient Yang fails to warm the Middle Jiao, creating internal cold. Digestive fire is diminished, causing water and food to pass out unabsorbed.",
        "treatment_principle": "Warm Middle Jiao Yang, dispel internal cold, and strengthen the Spleen (温中健脾，祛寒止泻).",
        "acupuncture_points": [
            {"code": "RN12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Heavy Moxa (艾灸)", "rationale": "Warms Middle Burner internal cold."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Reinforcing + Moxa", "rationale": "Generates vital fire and strengthens digestive absorption."},
            {"code": "BL20", "name": "Pishu (脾俞)", "role": "Spleen Back-Shu Point", "technique": "Moxibustion (灸法)", "rationale": "Directly warms Spleen Yang."},
            {"code": "RN8", "name": "Shenque (神阙)", "role": "Umbilicus", "technique": "Salt-separated Moxa (隔盐灸)", "rationale": "Rescue Yang point; stops persistent watery cold diarrhea."},
            {"code": "SP3", "name": "Taibai (太白)", "role": "Yuan-Source Point", "technique": "Reinforcing (补法)", "rationale": "Tonifies Spleen root."}
        ],
        "herbal_formula": {
            "name": "Li Zhong Wan (Regulate the Middle Pill)",
            "chinese": "理中丸",
            "key_herbs": "Gan Jiang (Dried Ginger), Ren Shen (or Dang Shen), Bai Zhu, Zhi Gan Cao",
            "action": "Warms the Middle Burner, dispels Cold, and tonifies Spleen and Stomach."
        },
        "lifestyle_diet": {
            "recommended": "Dried ginger tea, black pepper, mutton broth, bone broth, cinnamon, cooked parsnips, cloves.",
            "avoid": "Cold food, iced water, watermelon, cucumber, dairy, raw fruit.",
            "advice": "Keep abdomen warm with a heating pad or moxa. Never eat food straight from the refrigerator."
        }
    },
    {
        "id": "stomach-fire",
        "name": "Stomach Fire / Stomach Heat",
        "chinese": "胃热炽盛 (Wèi Rè Chì Shèng)",
        "organ": "Stomach (胃)",
        "category": "Digestive",
        "nature": "Interior Full Heat (里实热)",
        "description": "Excess heat blazes in the Stomach, speeding up gastric breakdown, causing excessive thirst, ravenous hunger, burning epigastric pain, and foul breath.",
        "key_symptoms": [
            "epigastric_burning", "excessive_hunger", "thirst_cold",
            "dry_constipation", "bad_breath_halitosis", "bleeding_swollen_gums"
        ],
        "secondary_symptoms": [
            "acid_reflux", "nausea_vomiting", "restlessness_agitation"
        ],
        "tongue_body": ["Red / Scarlet (Body/Center)"],
        "tongue_coat": ["Thick Yellow", "Dry / Rough"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Surging / Overflowing (洪)", "Rapid (数)"],
        "pathomechanism": "Stomach fire roasts foods rapidly (excessive hunger) and consumes body fluids (severe thirst, dry stools). Heat flares upward along the Yangming channel to the mouth and gums.",
        "treatment_principle": "Clear Stomach Heat, purge fire, and protect body fluids (清胃泻火，生津止渴).",
        "acupuncture_points": [
            {"code": "ST44", "name": "Neiting (内庭)", "role": "Ying-Spring Point (Water)", "technique": "Reducing (泻法)", "rationale": "Primary point to clear and drain Stomach heat and toothache."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Harmonizing / Reducing", "rationale": "Descends rebellious Stomach fire and acid."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Clears Yangming fire affecting face, mouth, and gums."},
            {"code": "ST25", "name": "Tianshu (天枢)", "role": "Front-Mu of Large Intestine", "technique": "Reducing (泻法)", "rationale": "Drains intestinal heat and relieves constipation."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Systemic heat-clearing point."}
        ],
        "herbal_formula": {
            "name": "Qing Wei San (Clear the Stomach Powder)",
            "chinese": "清胃散",
            "key_herbs": "Huang Lian, Sheng Di Huang, Mu Dan Pi, Dang Gui, Sheng Ma",
            "action": "Drains Stomach fire, cools blood, and relieves pain in teeth and mouth."
        },
        "lifestyle_diet": {
            "recommended": "Cucumber, watermelon, celery juice, lotus root, tofu, mung beans, mint tea, pears.",
            "avoid": "Alcohol, chili peppers, garlic, ginger, barbecued meats, coffee, cigarettes.",
            "advice": "Eat smaller, lighter meals. Avoid eating late at night or rushing meals."
        }
    },
    {
        "id": "food-stagnation",
        "name": "Food Stagnation in Stomach",
        "chinese": "食积胃肠 (Shí Jī Wèi Cháng)",
        "organ": "Stomach (胃)",
        "category": "Digestive",
        "nature": "Interior Excess (里实)",
        "description": "Overeating or eating indigestible food obstructs the descending motion of the Stomach, causing foul belching, severe bloating, and food repulsion.",
        "key_symptoms": [
            "foul_belching", "bloating_after_eating", "repulsion_food",
            "acid_reflux", "sharp_abdominal_pain_pressure", "foul_smelling_diarrhea"
        ],
        "secondary_symptoms": [
            "nausea_vomiting", "insomnia_restless"
        ],
        "tongue_body": ["Normal Pale Red"],
        "tongue_coat": ["Thick White", "Thick Yellow", "Greasy / Turbid"],
        "tongue_moisture": ["Wet / Moist / Slippery", "Normal Moist"],
        "pulses": ["Slippery (滑)", "Full / Strong (实)"],
        "pathomechanism": "Undigested food stays in the stomach and ferments, creating foul acid gas. 'When the stomach is in disharmony, sleep is restless.'",
        "treatment_principle": "Resolve food stagnation, harmonize the Stomach, and descend turbidity (消食导滞，和胃降逆).",
        "acupuncture_points": [
            {"code": "RN12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Reducing (泻法)", "rationale": "Directly moves stagnated food in Middle Jiao."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Restores peristalsis and descends Stomach Qi."},
            {"code": "ST25", "name": "Tianshu (天枢)", "role": "Front-Mu of Large Intestine", "technique": "Reducing (泻法)", "rationale": "Promotes bowel evacuation of stagnated materials."},
            {"code": "PC6", "name": "Neiguan (内关)", "role": "Luo-Connecting Point", "technique": "Reducing (泻法)", "rationale": "Stops nausea, vomiting, and acid regurgitation."},
            {"code": "SP4", "name": "Gongsun (公孙)", "role": "Luo-Connecting / Chong Confluent", "technique": "Harmonizing (平补平泻)", "rationale": "Relieves acute abdominal distention and cramps."}
        ],
        "herbal_formula": {
            "name": "Bao He Wan (Preserve Harmony Pill)",
            "chinese": "保和丸",
            "key_herbs": "Shan Zha (Hawthorn), Shen Qu, Lai Fu Zi, Ban Xia, Chen Pi, Fu Ling, Lian Qiao",
            "action": "Digests all forms of meat, grain, and greasy stagnation."
        },
        "lifestyle_diet": {
            "recommended": "Fast or eat very light plain congee; hawthorn tea, radish soup, warm water with lemon.",
            "avoid": "Heavy meats, rich sauces, large portions, alcohol, dairy.",
            "advice": "Take a 20-minute gentle walk after eating. Never eat immediately before sleeping."
        }
    },

    # --- LIVER & GALLBLADDER PATTERNS ---
    {
        "id": "liver-qi-stagnation",
        "name": "Liver Qi Stagnation",
        "chinese": "肝郁气滞 (Gān Yù Qì Zhì)",
        "organ": "Liver (肝)",
        "category": "Emotional / Liver",
        "nature": "Interior Excess / Stagnation (里实气滞)",
        "description": "Emotional stress, frustration, or unexpressed anger constrains the Liver's free-coursing function, causing pain in the hypochondrium, sighing, and emotional lability.",
        "key_symptoms": [
            "hypochondriac_distention", "frequent_sighing", "irritability_mood_swings",
            "plum_pit_throat", "alternating_stools"
        ],
        "secondary_symptoms": [
            "poor_appetite", "bloating_after_eating", "breast_distention_pms", "dysmenorrhea"
        ],
        "tongue_body": ["Normal Pale Red", "Red / Scarlet (Edges)"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Wiry / Taut (弦)"],
        "pathomechanism": "Liver oversees smooth flow of Qi. Emotional repression prevents smooth circulation, accumulating tension along the ribcage, throat (plum pit sensation), and digestive system.",
        "treatment_principle": "Soothe the Liver, regulate Qi circulation, and harmonize emotional spirit (疏肝理气，解郁调经).",
        "acupuncture_points": [
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source / Shu-Stream (Earth)", "technique": "Reducing (泻法)", "rationale": "Primary point to dredge Liver Qi and release physical and emotional tension."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Four Gates Synergy", "technique": "Reducing (泻法)", "rationale": "Paired with LR3 as 'Four Gates' (Si Guan) to open circulation throughout the entire body."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "He-Sea / Hui-Meeting for Sinews", "technique": "Harmonizing (平补平泻)", "rationale": "Relieves hypochondriac distention and smooths gallbladder channel."},
            {"code": "PC6", "name": "Neiguan (内关)", "role": "Luo-Connecting Point", "technique": "Harmonizing (平补平泻)", "rationale": "Relieves emotional constriction, chest tightness, and nausea."},
            {"code": "LR14", "name": "Qimen (期门)", "role": "Front-Mu of Liver", "technique": "Oblique Reducing", "rationale": "Directly relieves ribcage discomfort and liver enlargement."}
        ],
        "herbal_formula": {
            "name": "Xiao Yao San (Free and Easy Wanderer)",
            "chinese": "逍遥散",
            "key_herbs": "Chai Hu, Dang Gui, Bai Shao, Bai Zhu, Fu Ling, Zhi Gan Cao, Bo He, Sheng Jiang",
            "action": "Spreads Liver Qi, strengthens Spleen, and nourishes Blood."
        },
        "lifestyle_diet": {
            "recommended": "Rosebud tea, jasmine tea, mint tea, citrus peels, dark leafy greens, daikon.",
            "avoid": "Alcohol, excessively greasy food, coffee, heavy spices.",
            "advice": "Engage in cardiovascular exercise, outdoors walking, artistic expression, or vocal release (singing)."
        }
    },
    {
        "id": "liver-fire-blazing",
        "name": "Liver Fire Blazing",
        "chinese": "肝火上炎 (Gān Huǒ Shàng Yán)",
        "organ": "Liver (肝)",
        "category": "Emotional / Liver",
        "nature": "Interior Full Heat (里实热)",
        "description": "Prolonged Liver Qi stagnation transforms into virulent Fire, ascending aggressively to the head and sensory orifices.",
        "key_symptoms": [
            "severe_headache_temporal", "red_irritated_eyes", "bitter_taste",
            "irritability_mood_swings", "tinnitus_loud", "dream_disturbed_sleep"
        ],
        "secondary_symptoms": [
            "dry_constipation", "dark_scanty_urine", "facial_flushing", "nosebleeds"
        ],
        "tongue_body": ["Red / Scarlet (Edges)", "Deep Red / Crimson"],
        "tongue_coat": ["Thick Yellow", "Dry / Rough"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Wiry / Taut (弦)", "Rapid (数)"],
        "pathomechanism": "Extreme Liver Fire surges upward to the eyes (red eyes), ears (loud high-pitched ringing), and head (throbbing migraine), causing explosive anger and restless sleep.",
        "treatment_principle": "Clear and purge Liver Fire, pacify the head, and cool Blood (清肝泻火，镇静安神).",
        "acupuncture_points": [
            {"code": "LR2", "name": "Xingjian (行间)", "role": "Ying-Spring Point (Fire)", "technique": "Reducing (泻法)", "rationale": "Fire point of the Liver channel; sedating child point clears excess Liver Fire."},
            {"code": "GB20", "name": "Fengchi (风池)", "role": "Wind Pool", "technique": "Reducing (泻法)", "rationale": "Subdues ascending head fire and relieves migraine."},
            {"code": "GB43", "name": "Xiaxi (侠溪)", "role": "Ying-Spring Point (Water)", "technique": "Reducing (泻法)", "rationale": "Water point of Gallbladder; clears heat from ears and eyes."},
            {"code": "Taiyang", "name": "Taiyang (太阳)", "role": "Extra Head Point", "technique": "Pricking to bleed (刺血)", "rationale": "Bleed 1-2 drops for acute throbbing temple headache."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Cools systemic heat."}
        ],
        "herbal_formula": {
            "name": "Long Dan Xie Gan Tang (Gentiana Decoction to Drain the Liver)",
            "chinese": "龙胆泻肝汤",
            "key_herbs": "Long Dan Cao, Huang Qin, Zhi Zi, Ze Xie, Mu Tong, Che Qian Zi, Sheng Di, Dang Gui, Chai Hu, Gan Cao",
            "action": "Drains excess Liver and Gallbladder fire, clears lower jiao damp-heat."
        },
        "lifestyle_diet": {
            "recommended": "Dandelion greens, celery, cucumber, mung beans, green tea, bitter melon, chrysanthemum tea.",
            "avoid": "Alcohol, red meat, hot chilies, deep-fried foods, stimulants, coffee.",
            "advice": "Practice cooling meditation, reduce stress triggers, avoid heated confrontations."
        }
    },
    {
        "id": "liver-blood-deficiency",
        "name": "Liver Blood Deficiency",
        "chinese": "肝血虚 (Gān Xuè Xū)",
        "organ": "Liver (肝)",
        "category": "Deficiency Patterns",
        "nature": "Interior Deficiency (里虚)",
        "description": "Deficiency of Liver Blood fails to nourish the eyes, sinews, nails, and uterus, leading to floaters, muscle cramps, and scanty menses.",
        "key_symptoms": [
            "dizziness_vertigo", "blurred_vision_floaters", "muscle_cramps_spasms",
            "scanty_pale_menses", "brittle_pale_nails", "insomnia_dreamy"
        ],
        "secondary_symptoms": [
            "pale_complexion", "numbness_limbs", "dry_dull_skin"
        ],
        "tongue_body": ["Pale / Whitish"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Fine / Thready (细)", "Wiry / Taut (弦)"],
        "pathomechanism": "Liver stores Blood and moistens sinews. Insufficient Blood fails to lubricate tendons (cramps), nourish eyes (visual floaters/dry eyes), or fill the Chong/Ren channels (scanty menses).",
        "treatment_principle": "Nourish Blood, tonify the Liver, and moisten sinews (补血养肝，濡养筋脉).",
        "acupuncture_points": [
            {"code": "BL18", "name": "Ganshu (肝俞)", "role": "Liver Back-Shu Point", "technique": "Reinforcing (补法)", "rationale": "Directly tonifies Liver organ and replenishes stored Blood."},
            {"code": "BL17", "name": "Geshu (膈俞)", "role": "Hui-Meeting for Blood", "technique": "Reinforcing (补法)", "rationale": "Primary point in TCM to generate and nourish Blood."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Nourishes Liver, Spleen, and Kidney Yin and Blood."},
            {"code": "LR8", "name": "Ququan (曲泉)", "role": "He-Sea Point (Water)", "technique": "Reinforcing (补法)", "rationale": "Water generates Wood; tonifies Liver Blood and Yin."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Reinforcing + Moxa", "rationale": "Generates source of Blood from Middle Burner."}
        ],
        "herbal_formula": {
            "name": "Si Wu Tang (Four Substances Decoction)",
            "chinese": "四物汤",
            "key_herbs": "Shu Di Huang, Bai Shao, Dang Gui, Chuan Xiong",
            "action": "Nourishes Blood, regulates the Liver, and harmonizes menstruation."
        },
        "lifestyle_diet": {
            "recommended": "Spinach, beets, black sesame, goji berries, beef bone broth, liver, dark cherries, black beans.",
            "avoid": "Overworking, late-night screen time, excessive physical strain during menses.",
            "advice": "Sleep before 11:00 PM (Gallbladder/Liver time) to permit Blood to return and regenerate in the Liver."
        }
    },

    # --- KIDNEY PATTERNS ---
    {
        "id": "kidney-yang-deficiency",
        "name": "Kidney Yang Deficiency",
        "chinese": "肾阳虚 (Shèn Yáng Xū)",
        "organ": "Kidney (肾)",
        "category": "Deficiency Patterns",
        "nature": "Interior Deficiency Cold (里虚寒)",
        "description": "Deficiency of the primary Yang fire of the body (Mingmen Fire), producing widespread systemic coldness, lumbar weakness, and nocturnal polyuria.",
        "key_symptoms": [
            "cold_limbs", "soreness_lower_back_knees", "pale_profuse_urine",
            "aversion_to_cold", "cock_crow_diarrhea", "low_libido_impotence"
        ],
        "secondary_symptoms": [
            "edema_lower_limbs", "fatigue_exhaustion", "pale_dull_complexion"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thin White", "Thick White"],
        "tongue_moisture": ["Wet / Moist / Slippery"],
        "pulses": ["Deep (沉)", "Slow (迟)", "Weak / Empty (弱/虚)"],
        "pathomechanism": "Kidney Yang is the root of warmth for all organs. Deficiency causes failure to warm the lower back and legs, failure to transform water fluids (frequent pale urination), and early morning diarrhea.",
        "treatment_principle": "Warm and tonify Kidney Yang, invigorate the Mingmen Gate of Vitality (温补肾阳，固摄下元).",
        "acupuncture_points": [
            {"code": "DU4", "name": "Mingmen (命门)", "role": "Gate of Life", "technique": "Moxibustion (艾灸)", "rationale": "Primary point to reignite primordial Mingmen Yang fire."},
            {"code": "BL23", "name": "Shenshu (肾俞)", "role": "Kidney Back-Shu Point", "technique": "Reinforcing + Moxa", "rationale": "Directly supplements Kidney essence and Yang warmth."},
            {"code": "RN4", "name": "Guanyuan (关元)", "role": "Front-Mu of Small Intestine", "technique": "Heavy Moxa (艾灸)", "rationale": "Deep tonification of Original Qi (Yuan Qi) and lower burner fire."},
            {"code": "KD3", "name": "Taixi (太溪)", "role": "Yuan-Source Point", "technique": "Reinforcing + Moxa", "rationale": "Tonifies Kidney root."},
            {"code": "BL40", "name": "Weizhong (委中)", "role": "He-Sea Point", "technique": "Harmonizing", "rationale": "Commands the lumbar spine and relieves lower back weakness."}
        ],
        "herbal_formula": {
            "name": "Jin Gui Shen Qi Wan (Golden Book Kidney Qi Pill)",
            "chinese": "金匮肾气丸",
            "key_herbs": "Fu Zi, Gui Zhi, Shu Di Huang, Shan Zhu Yu, Shan Yao, Fu Ling, Ze Xie, Mu Dan Pi",
            "action": "Warms and supplements Kidney Yang, transforms water fluids."
        },
        "lifestyle_diet": {
            "recommended": "Walnuts, black sesame, lamb, bone broths, cloves, cinnamon, chestnuts, ginger.",
            "avoid": "Cold food, iced water, excessive salt, raw salads, cold environmental exposure.",
            "advice": "Keep feet and lumbar region warm at all times. Avoid excessive sexual exhaustion."
        }
    },
    {
        "id": "kidney-yin-deficiency",
        "name": "Kidney Yin Deficiency",
        "chinese": "肾阴虚 (Shèn Yīn Xū)",
        "organ": "Kidney (肾)",
        "category": "Deficiency Patterns",
        "nature": "Interior Deficiency Heat (里虚热)",
        "description": "Depletion of Kidney water and essence leads to hyperactive Empty Heat, presenting with night sweats, five-palm heat, and dry throat.",
        "key_symptoms": [
            "night_sweating", "five_palm_heat", "soreness_lower_back_knees",
            "tinnitus_low_pitch", "dizziness_vertigo", "dry_throat_night"
        ],
        "secondary_symptoms": [
            "insomnia_dreamy", "scanty_dark_urine", "dry_constipation", "emaciation"
        ],
        "tongue_body": ["Red / Scarlet (Body/Center)", "Deep Red / Crimson"],
        "tongue_coat": ["Peeled / Geographic / Mirror", "None / Barely Any"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Fine / Thready (细)", "Rapid (数)"],
        "pathomechanism": "Kidney Yin fails to moisten and anchor Yang. Empty Heat burns internally, producing night sweating (when Yin is at peak vulnerability), hot soles and palms, and a peeled mirror tongue.",
        "treatment_principle": "Nourish Kidney Yin, enrich True Essence, and clear deficiency Heat (滋补肾阴，填精清热).",
        "acupuncture_points": [
            {"code": "KD3", "name": "Taixi (太溪)", "role": "Yuan-Source Point (Earth)", "technique": "Reinforcing (补法 - No Moxa)", "rationale": "Primary point to replenish Kidney Yin and Water."},
            {"code": "KD6", "name": "Zhaohai (照海)", "role": "Confluent Yin Qiao Point", "technique": "Reinforcing (补法)", "rationale": "Nourishes Yin fluids, moistens dry throat, calms the spirit."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Nourishes the Yin of Kidney, Liver, and Spleen."},
            {"code": "BL23", "name": "Shenshu (肾俞)", "role": "Kidney Back-Shu Point", "technique": "Reinforcing (No Moxa)", "rationale": "Replenishes Kidney water reserve."},
            {"code": "RN4", "name": "Guanyuan (关元)", "role": "Front-Mu Point", "technique": "Reinforcing (补法)", "rationale": "Nourishes Yin and essence at Dan Tian."}
        ],
        "herbal_formula": {
            "name": "Liu Wei Di Huang Wan (Six-Ingredient Pill with Rehmannia)",
            "chinese": "六味地黄丸",
            "key_herbs": "Shu Di Huang, Shan Zhu Yu, Shan Yao, Fu Ling, Ze Xie, Mu Dan Pi",
            "action": "Enriches Kidney Yin, tonifies Spleen, and clears deficiency Fire."
        },
        "lifestyle_diet": {
            "recommended": "Black beans, goji berries, mulberries, black sesame, duck, seaweed, pears, tremella mushroom soup.",
            "avoid": "Spicy foods, hot peppers, coffee, alcohol, dry baked crackers, excessive sauna.",
            "advice": "Prioritize restorative rest. Practice gentle Yin yoga and quiet mindfulness."
        }
    },

    # --- HEART PATTERNS ---
    {
        "id": "heart-blood-deficiency",
        "name": "Heart Blood Deficiency",
        "chinese": "心血虚 (Xīn Xuè Xū)",
        "organ": "Heart (心)",
        "category": "Emotional / Sleep",
        "nature": "Interior Deficiency (里虚)",
        "description": "Insufficient Heart Blood fails to shelter the Shen (Mind), causing palpitations, severe insomnia, poor memory, and a pale complexion.",
        "key_symptoms": [
            "palpitations", "insomnia_difficulty_falling_asleep", "dream_disturbed_sleep",
            "poor_memory", "dizziness_vertigo", "pale_complexion"
        ],
        "secondary_symptoms": [
            "fatigue_exhaustion", "anxiety_restlessness", "pale_lips_nails"
        ],
        "tongue_body": ["Pale / Whitish"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Fine / Thready (细)", "Weak / Empty (弱/虚)"],
        "pathomechanism": "'The Heart stores the Shen; Blood is the material foundation of the Shen.' When Blood is scanty, the spirit has no residence and floats at night, causing insomnia and anxiety.",
        "treatment_principle": "Nourish Blood, tonify the Heart, and anchor the Shen (补血养心，益智安神).",
        "acupuncture_points": [
            {"code": "HT7", "name": "Shenmen (神门)", "role": "Yuan-Source / Shu-Stream (Earth)", "technique": "Reinforcing (补法)", "rationale": "Primary point to calm Shen and tonify Heart Blood and Qi."},
            {"code": "PC6", "name": "Neiguan (内关)", "role": "Luo-Connecting Point", "technique": "Harmonizing (平补平泻)", "rationale": "Relieves chest palpitations and harmonizes the heart rhythm."},
            {"code": "BL15", "name": "Xinshu (心俞)", "role": "Heart Back-Shu Point", "technique": "Reinforcing (补法)", "rationale": "Directly tonifies Heart organ and stabilizes the spirit."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Generates Blood from Spleen to nourish the Heart."},
            {"code": "BL17", "name": "Geshu (膈俞)", "role": "Hui-Meeting for Blood", "technique": "Reinforcing (补法)", "rationale": "Supplements systemic Blood generation."}
        ],
        "herbal_formula": {
            "name": "Gui Pi Tang (Restore the Spleen Decoction)",
            "chinese": "归脾汤",
            "key_herbs": "Huang Qi, Ren Shen, Bai Zhu, Fu Ling, Suan Zao Ren, Long Yan Rou, Dang Gui, Yuan Zhi, Mu Xiang, Zhi Gan Cao",
            "action": "Tonifies Spleen Qi to generate Blood, anchors the Heart Shen, and cures insomnia."
        },
        "lifestyle_diet": {
            "recommended": "Longan fruit, jujube dates, lotus seeds, egg yolks, spinach, red dates, bone broth.",
            "avoid": "Caffeine, energy drinks, late-night mentally demanding work, exciting media before bed.",
            "advice": "Establish a calming evening bedtime routine with warm foot soaks."
        }
    },
    {
        "id": "heart-fire-blazing",
        "name": "Heart Fire Blazing",
        "chinese": "心火炽盛 (Xīn Huǒ Chì Shèng)",
        "organ": "Heart (心)",
        "category": "Emotional / Sleep",
        "nature": "Interior Full Heat (里实热)",
        "description": "Extreme emotional agitation or prolonged heat accumulation turns into Heart Fire, disturbing the Shen and inflaming the tongue tip.",
        "key_symptoms": [
            "mouth_tongue_ulcers", "palpitations", "anxiety_restlessness",
            "insomnia_difficulty_falling_asleep", "dark_burning_urine", "thirst_cold"
        ],
        "secondary_symptoms": [
            "red_face", "bitter_taste"
        ],
        "tongue_body": ["Red / Scarlet (Tip/Edges)", "Deep Red / Crimson"],
        "tongue_coat": ["Thin Yellow", "Thick Yellow"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Rapid (数)", "Surging / Overflowing (洪)"],
        "pathomechanism": "The tongue is the sprout of the Heart. Intense Fire burns upward to cause painful red tongue ulcers and descends to the Small Intestine causing burning yellow urination.",
        "treatment_principle": "Clear Heart Fire, drain heat through urine, and calm the Shen (清心泻火，导热下行，宁心安神).",
        "acupuncture_points": [
            {"code": "HT8", "name": "Shaofu (少府)", "role": "Ying-Spring Point (Fire)", "technique": "Reducing (泻法)", "rationale": "Directly drains excess blazing Fire from the Heart channel."},
            {"code": "HT7", "name": "Shenmen (神门)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Calms mental anxiety and agitation."},
            {"code": "RN15", "name": "Jiuwei (鸠尾)", "role": "Luo-Connecting of Ren", "technique": "Reducing (泻法)", "rationale": "Clears mental mania and heat in the chest."},
            {"code": "SI2", "name": "Qiangu (前谷)", "role": "Ying-Spring Point (Water)", "technique": "Reducing (泻法)", "rationale": "Clears Small Intestine heat, guiding fire downward."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Cools whole-body heat."}
        ],
        "herbal_formula": {
            "name": "Dao Chi San (Guide Out the Red Powder)",
            "chinese": "导赤散",
            "key_herbs": "Sheng Di Huang, Mu Tong, Dan Zhu Ye, Gan Cao Shao",
            "action": "Clears Heart Fire and drains it downward into the urinary bladder."
        },
        "lifestyle_diet": {
            "recommended": "Lotus plumule tea (Lian Zi Xin), watermelon, bamboo leaf tea, cucumber, mung bean congee.",
            "avoid": "Alcohol, coffee, spicy peppers, red meat, excessive heat, tobacco.",
            "advice": "Avoid intense emotional stimulation. Practice cooling breathwork."
        }
    }
]


# =============================================================================
# CLINICAL PRESET QUICK LOADERS
# =============================================================================
CLINICAL_PRESETS = {
    "Select a Clinical Scenario...": None,
    "Acute Wind-Cold Common Cold (风寒束肺)": {
        "symptoms": ["aversion_to_cold", "runny_nose_clear", "cough_clear_white", "absence_of_sweat", "headache_occipital", "body_aches", "nasal_congestion", "stiff_neck"],
        "tongue_body": "Pale / Whitish",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Normal Moist",
        "pulse": "Floating (浮)"
    },
    "Acute Wind-Heat Respiratory Infection (风热犯肺)": {
        "symptoms": ["high_fever", "sore_swollen_throat", "cough_yellow_sticky", "runny_nose_yellow", "slight_sweat", "thirst_cold", "headache_frontal", "red_irritated_eyes"],
        "tongue_body": "Red / Scarlet (Tip/Edges)",
        "tongue_coat": "Thin Yellow",
        "tongue_moisture": "Dry / Lack of Fluids",
        "pulse": "Rapid (数)"
    },
    "Liver Qi Stagnation with Spleen Deficiency (肝郁脾虚 - PMS / IBS)": {
        "symptoms": ["hypochondriac_distention", "frequent_sighing", "irritability_mood_swings", "poor_appetite", "bloating_after_eating", "alternating_stools", "fatigue_exhaustion"],
        "tongue_body": "Swollen with Teeth Marks",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Normal Moist",
        "pulse": "Wiry / Taut (弦)"
    },
    "Kidney Yang Deficiency with Cold Limbs & Back Weakness (肾阳虚)": {
        "symptoms": ["cold_limbs", "soreness_lower_back_knees", "pale_profuse_urine", "aversion_to_cold", "fatigue_exhaustion", "low_libido_impotence", "cock_crow_diarrhea"],
        "tongue_body": "Pale / Whitish",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Wet / Moist / Slippery",
        "pulse": "Deep (沉)"
    },
    "Kidney Yin Deficiency with Night Sweats & 5-Palm Heat (肾阴虚)": {
        "symptoms": ["night_sweating", "five_palm_heat", "soreness_lower_back_knees", "tinnitus_low_pitch", "dizziness_vertigo", "dry_throat_night", "insomnia_dreamy"],
        "tongue_body": "Deep Red / Crimson",
        "tongue_coat": "Peeled / Geographic / Mirror",
        "tongue_moisture": "Dry / Lack of Fluids",
        "pulse": "Fine / Thready (细)"
    },
    "Stomach Fire with Epigastric Burning & Constipation (胃火炽盛)": {
        "symptoms": ["epigastric_burning", "excessive_hunger", "thirst_cold", "dry_constipation", "bad_breath_halitosis", "bleeding_swollen_gums", "acid_reflux"],
        "tongue_body": "Red / Scarlet (Body/Center)",
        "tongue_coat": "Thick Yellow",
        "tongue_moisture": "Dry / Lack of Fluids",
        "pulse": "Surging / Overflowing (洪)"
    },
    "Heart Blood Deficiency with Insomnia & Palpitations (心血虚)": {
        "symptoms": ["palpitations", "insomnia_difficulty_falling_asleep", "dream_disturbed_sleep", "poor_memory", "dizziness_vertigo", "pale_complexion", "fatigue_exhaustion"],
        "tongue_body": "Pale / Whitish",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Normal Moist",
        "pulse": "Fine / Thready (细)"
    }
}


# =============================================================================
# SCORING & PATTERN DIFFERENTIATION ENGINE
# =============================================================================
def match_tcm_patterns(
    selected_symptoms: List[str],
    sel_tongue_body: str,
    sel_tongue_coat: str,
    sel_tongue_moisture: str,
    sel_pulses: List[str]
) -> List[Dict[str, Any]]:
    """Match user selected symptoms, tongue, and pulse against canonical TCM patterns."""
    if not selected_symptoms and not sel_pulses and not sel_tongue_body:
        return []

    results = []

    for pat in DIAGNOSTIC_PATTERNS:
        # 1. Symptom matching
        key_matches = [s for s in pat["key_symptoms"] if s in selected_symptoms]
        sec_matches = [s for s in pat["secondary_symptoms"] if s in selected_symptoms]

        # Weights: key symptoms 3.0 pts, secondary symptoms 1.5 pts
        sym_score = (len(key_matches) * 3.0) + (len(sec_matches) * 1.5)
        max_possible_sym = (len(pat["key_symptoms"]) * 3.0) + (len(pat["secondary_symptoms"]) * 1.5)

        # 2. Tongue matching
        tongue_match_count = 0
        if sel_tongue_body in pat["tongue_body"]:
            tongue_match_count += 1.5
        if sel_tongue_coat in pat["tongue_coat"]:
            tongue_match_count += 1.5
        if sel_tongue_moisture in pat["tongue_moisture"]:
            tongue_match_count += 1.0

        # 3. Pulse matching
        pulse_matches = []
        for p in sel_pulses:
            for pat_p in pat["pulses"]:
                if p.split()[0] in pat_p:
                    pulse_matches.append(p)
                    break
        pulse_score = len(pulse_matches) * 2.5

        # Total Raw Score
        raw_score = sym_score + tongue_match_count + pulse_score
        max_benchmark = (max_possible_sym * 0.75) + 4.0 + 5.0
        confidence = min(99, int((raw_score / max(1.0, max_benchmark)) * 100))

        if len(key_matches) >= 1 or (len(key_matches) == 0 and len(sec_matches) >= 2 and (tongue_match_count >= 1.5 or pulse_score >= 2.5)):
            results.append({
                "pattern": pat,
                "confidence": confidence,
                "key_matches": key_matches,
                "sec_matches": sec_matches,
                "pulse_matches": pulse_matches,
                "raw_score": raw_score
            })

    results.sort(key=lambda x: (x["confidence"], x["raw_score"]), reverse=True)
    return results


# =============================================================================
# SYMPTOM DEFINITIONS & CATEGORIES
# =============================================================================
SYMPTOM_GROUPS = {
    "🌡️ Chills, Fever & Sweating": [
        ("aversion_to_cold", "Aversion to cold / Chills (畏寒/恶寒)"),
        ("high_fever", "High fever / Severe heat (高热)"),
        ("low_fever", "Low-grade fever or afternoon tidal heat (潮热/微热)"),
        ("absence_of_sweat", "Absence of sweat with cold (无汗)"),
        ("spontaneous_sweating", "Spontaneous sweating on exertion (自汗)"),
        ("night_sweating", "Night sweats during sleep (盗汗)"),
        ("slight_sweat", "Slight sweating with fever (微汗)")
    ],
    "🗣️ Head, Face & Sensory": [
        ("runny_nose_clear", "Runny nose with clear watery mucus (流清涕)"),
        ("runny_nose_yellow", "Runny nose with thick yellow mucus (流黄浊涕)"),
        ("nasal_congestion", "Nasal congestion & sneezing (鼻塞喷嚏)"),
        ("sore_swollen_throat", "Sore, red, swollen throat (咽喉红肿剧痛)"),
        ("dry_itchy_throat", "Dry, itchy or scratchy throat (咽痒干咳)"),
        ("dry_throat_night", "Dry mouth and throat, worse at night (咽干口燥夜甚)"),
        ("headache_occipital", "Occipital headache / back of neck pain (后头痛)"),
        ("headache_frontal", "Frontal headache / sinus pain (前额头痛)"),
        ("severe_headache_temporal", "Temporal throbbing migraine / temple pain (偏头痛/太阳穴跳痛)"),
        ("dizziness_vertigo", "Dizziness / Vertigo (头晕目眩)"),
        ("red_irritated_eyes", "Red, dry, bloodshot eyes (目赤干涩)"),
        ("blurred_vision_floaters", "Blurred vision / Eye floaters (视物昏花/飞蚊症)"),
        ("tinnitus_loud", "Loud, sudden, high-pitched tinnitus (耳鸣暴发如潮声)"),
        ("tinnitus_low_pitch", "Low-pitched, gradual tinnitus relieved by pressure (耳鸣如蝉喜按)"),
        ("bitter_taste", "Bitter taste in mouth (口苦)"),
        ("mouth_tongue_ulcers", "Painful red ulcers on mouth or tongue (口舌生疮)")
    ],
    "🫁 Respiration, Chest & Heart": [
        ("cough_clear_white", "Cough with thin, clear or white watery phlegm (咳白稀痰)"),
        ("cough_yellow_sticky", "Cough with thick, sticky yellow phlegm (咳黄稠痰)"),
        ("cough_weak", "Weak, feeble, chronic cough (咳嗽无力)"),
        ("shortness_of_breath", "Shortness of breath / rapid shallow breathing (气短喘促)"),
        ("chest_fullness", "Chest tightness or oppression (胸闷痞满)"),
        ("palpitations", "Palpitations / irregular fluttering heartbeat (心悸怔忡)"),
        ("hypochondriac_distention", "Hypochondriac / ribcage distention or discomfort (胁肋胀痛)"),
        ("frequent_sighing", "Frequent involuntary sighing (善太息/叹气)")
    ],
    "🍲 Digestion, Thirst & Abdomen": [
        ("thirst_cold", "Thirst with craving for cold drinks (大渴喜冷饮)"),
        ("poor_appetite", "Poor appetite / Early satiety (食少纳呆)"),
        ("bloating_after_eating", "Abdominal fullness & bloating after meals (食后腹胀)"),
        ("excessive_hunger", "Ravenous hunger with rapid digestion (消谷善饥)"),
        ("epigastric_burning", "Burning pain in epigastrium (胃脘灼痛)"),
        ("dull_abdominal_pain_warmth", "Dull abdominal pain relieved by warmth/pressure (腹痛喜温喜按)"),
        ("sharp_abdominal_pain_pressure", "Sharp/stabbing abdominal pain worse on pressure (腹痛拒按)"),
        ("acid_reflux", "Acid reflux / Heartburn / Belching (泛酸嗳气)"),
        ("nausea_vomiting", "Nausea or vomiting (恶心呕吐)"),
        ("foul_belching", "Foul belching with rotten food smell (嗳腐吞酸)"),
        ("repulsion_food", "Aversion to food / Food repulsion (厌食/恶食)"),
        ("bad_breath_halitosis", "Severe bad breath / Halitosis (口臭)"),
        ("bleeding_swollen_gums", "Swollen, bleeding, painful gums (齿龈肿痛出血)")
    ],
    "🚽 Bowels & Urination": [
        ("loose_stools", "Loose, soft, watery stools (便溏)"),
        ("watery_diarrhea", "Watery diarrhea with undigested grain (泄泻完谷不化)"),
        ("cock_crow_diarrhea", "Early morning diarrhea / Cock-crow diarrhea (五更泻)"),
        ("dry_constipation", "Dry, hard, difficult constipation (大便干结/秘结)"),
        ("alternating_stools", "Alternating diarrhea and constipation (便秘与腹泻交替)"),
        ("foul_smelling_diarrhea", "Foul, burning diarrhea with anal burning (便溏臭秽肛门灼热)"),
        ("pale_profuse_urine", "Clear, copious, frequent pale urination (小便清长夜尿多)"),
        ("dark_burning_urine", "Scanty, dark yellow, burning urination (小便短赤灼热)")
    ],
    "🧠 Mind, Emotion & Sleep": [
        ("insomnia_difficulty_falling_asleep", "Difficulty falling asleep / Tossing and turning (入睡困难)"),
        ("insomnia_dreamy", "Frequent waking with vivid dreaming (多梦易醒)"),
        ("irritability_mood_swings", "Irritability, mood swings, quick anger (急躁易怒)"),
        ("anxiety_restlessness", "Restlessness, mental agitation, anxiety (心烦躁动)"),
        ("poor_memory", "Poor memory / Mental fatigue (健忘失神)"),
        ("plum_pit_throat", "Plum-pit sensation in throat (梅核气 - 咽中如有物)"),
        ("five_palm_heat", "Five-palm heat (hot sensation in palms, soles, chest) (五心烦热)")
    ],
    "💪 Body, Limbs & Vitality": [
        ("fatigue_exhaustion", "Chronic fatigue / Physical exhaustion (神疲乏力)"),
        ("body_aches", "Whole body aches and soreness (周身酸痛)"),
        ("stiff_neck", "Stiff neck and upper back tension (项背拘急)"),
        ("cold_limbs", "Cold hands and feet / intolerance to cold (四肢厥冷/畏寒)"),
        ("weak_limbs", "Weakness and heaviness in arms and legs (四肢软弱无力)"),
        ("heaviness_limbs", "Heaviness of the whole body and head (肢体困重如裹)"),
        ("soreness_lower_back_knees", "Soreness and weakness of lower back and knees (腰膝酸软)"),
        ("muscle_cramps_spasms", "Muscle spasms, cramps, and twitching (手足抽搐/肌肉拘急)"),
        ("edema_lower_limbs", "Pitting edema / Swelling of ankles and legs (下肢浮肿)"),
        ("pale_complexion", "Pale, sallow, bloodless complexion (面色苍白/萎黄)"),
        ("low_libido_impotence", "Decreased libido / Sexual fatigue (性欲减退/阳痿遗精)")
    ]
}

ALL_SYMPTOM_KEYS = [k for sym_items in SYMPTOM_GROUPS.values() for k, _ in sym_items]
SYMPTOM_LABEL_MAP = {k: label for sym_items in SYMPTOM_GROUPS.values() for k, label in sym_items}


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


def render_internal_diagnostics_tab():
    """Render the Internal Illness Diagnostics & Pattern Differentiation tab."""
    # High contrast styles
    render_clean_html("""
    <style>
    .diag-card {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 18px;
    }
    .diag-header-title {
        color: #ffffff !important;
        font-size: 1.55rem !important;
        font-weight: 800 !important;
        margin: 0 0 4px 0 !important;
    }
    .diag-subtext {
        color: #cbd5e1 !important;
        font-size: 0.95rem !important;
        margin-bottom: 16px !important;
    }
    div[data-testid="stCheckbox"] label p {
        color: #ffffff !important;
        font-size: 0.92rem !important;
    }
    div[data-testid="stSelectbox"] label p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMultiselect"] label p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    </style>
    """)

    # Initialize all symptom checkbox states if not present
    for k in ALL_SYMPTOM_KEYS:
        if f"chk_sym_{k}" not in st.session_state:
            st.session_state[f"chk_sym_{k}"] = False

    if "diag_expand_version" not in st.session_state:
        st.session_state.diag_expand_version = 0

    if "diag_cat_expanded" not in st.session_state:
        st.session_state.diag_cat_expanded = {i: False for i in range(len(SYMPTOM_GROUPS))}

    if "sel_pulse_input" not in st.session_state:
        st.session_state.sel_pulse_input = []

    if "sel_tongue_body_input" not in st.session_state:
        st.session_state.sel_tongue_body_input = "Normal Pale Red"

    if "sel_tongue_coat_input" not in st.session_state:
        st.session_state.sel_tongue_coat_input = "Thin White"

    if "sel_tongue_moist_input" not in st.session_state:
        st.session_state.sel_tongue_moist_input = "Normal Moist"

    if "diag_preset_select" not in st.session_state:
        st.session_state.diag_preset_select = "Select a Clinical Scenario..."

    # Callbacks (run before widgets instantiate)
    def _cb_clear_all():
        for k in ALL_SYMPTOM_KEYS:
            st.session_state[f"chk_sym_{k}"] = False
        st.session_state["sel_pulse_input"] = []
        st.session_state["sel_tongue_body_input"] = "Normal Pale Red"
        st.session_state["sel_tongue_coat_input"] = "Thin White"
        st.session_state["sel_tongue_moist_input"] = "Normal Moist"
        st.session_state["diag_preset_select"] = "Select a Clinical Scenario..."
        for i in range(len(SYMPTOM_GROUPS)):
            st.session_state.diag_cat_expanded[i] = False
        st.session_state.diag_expand_version += 1

    def _cb_expand_all():
        for i in range(len(SYMPTOM_GROUPS)):
            st.session_state.diag_cat_expanded[i] = True
        st.session_state.diag_expand_version += 1

    def _cb_collapse_all():
        for i in range(len(SYMPTOM_GROUPS)):
            st.session_state.diag_cat_expanded[i] = False
        st.session_state.diag_expand_version += 1

    def _cb_preset_change():
        choice = st.session_state.diag_preset_select
        if choice and choice in CLINICAL_PRESETS and choice != "Select a Clinical Scenario...":
            pdata = CLINICAL_PRESETS[choice]
            target_syms = set(pdata["symptoms"])
            for k in ALL_SYMPTOM_KEYS:
                st.session_state[f"chk_sym_{k}"] = (k in target_syms)
            st.session_state["sel_pulse_input"] = [pdata["pulse"]]
            st.session_state["sel_tongue_body_input"] = pdata["tongue_body"]
            st.session_state["sel_tongue_coat_input"] = pdata["tongue_coat"]
            st.session_state["sel_tongue_moist_input"] = pdata["tongue_moisture"]
            for i, (grp_name, items) in enumerate(SYMPTOM_GROUPS.items()):
                st.session_state.diag_cat_expanded[i] = any(k in target_syms for k, _ in items)
            st.session_state.diag_expand_version += 1

    # Header Card
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            🩺 Internal Illness Diagnostics & Pattern Differentiation (辨证论治)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Comprehensive Four Examinations diagnostic engine. Check symptoms, tongue, and pulse qualities to differentiate authentic Zang-Fu disharmonies, treatment principles, acupuncture prescriptions, and classic formulas.
        </p>
    </div>
    """)

    # Preset Quick-Loader Row
    col_preset, col_clear = st.columns([3, 1], vertical_alignment="bottom")
    with col_preset:
        st.selectbox(
            "📋 Quick Clinical Scenarios (Pre-load Typical Cases)",
            options=list(CLINICAL_PRESETS.keys()),
            key="diag_preset_select",
            on_change=_cb_preset_change
        )
    with col_clear:
        st.button("🔄 Clear All Inputs", use_container_width=True, key="diag_clear_all_btn", on_click=_cb_clear_all)

    # Active selected symptoms computed directly from state
    active_symptoms = [k for k in ALL_SYMPTOM_KEYS if st.session_state.get(f"chk_sym_{k}", False)]

    # SECTION 1: CLINICAL SYMPTOMS CHECKLIST
    render_clean_html("""
    <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 10px; padding: 14px 18px; margin: 16px 0 12px 0;">
        <span style="font-size: 1.1rem; font-weight: 700; color: #38bdf8;">1. Clinical Symptoms Checklist (问诊 - Inquiry)</span>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-top: 2px;">Select all presenting signs and symptoms observed in the patient. Categories remain open while checking items.</div>
    </div>
    """)

    # Expand / Collapse All & Status Bar
    col_e1, col_e2, col_info = st.columns([1, 1, 3], vertical_alignment="center")
    with col_e1:
        st.button("📂 Expand All", use_container_width=True, on_click=_cb_expand_all, key="diag_exp_all_btn")
    with col_e2:
        st.button("📁 Collapse All", use_container_width=True, on_click=_cb_collapse_all, key="diag_col_all_btn")
    with col_info:
        if active_symptoms:
            st.caption(f"✨ **{len(active_symptoms)}** presenting symptom(s) currently active.")
        else:
            st.caption("ℹ️ Click any category below to expand and select presenting symptoms.")

    # Visual pill summary of currently active symptoms
    if active_symptoms:
        pills_html = "".join([
            f'<span style="background: rgba(56, 189, 248, 0.18); border: 1px solid rgba(56, 189, 248, 0.4); color: #7dd3fc; font-size: 0.8rem; font-weight: 600; padding: 3px 9px; border-radius: 6px; margin: 2px 4px 2px 0; display: inline-block;">✓ {SYMPTOM_LABEL_MAP.get(k, k).split(" / ")[0]}</span>'
            for k in active_symptoms
        ])
        render_clean_html(f"""
        <div style="background: rgba(17, 24, 39, 0.8); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 10px 14px; margin: 8px 0 14px 0;">
            <div style="font-size: 0.82rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; margin-bottom: 6px;">
                Active Patient Symptoms ({len(active_symptoms)} Selected):
            </div>
            <div>{pills_html}</div>
        </div>
        """)

    # Render Category Expanders (stable label and key ensure NO auto-collapse on checkbox selection)
    ver = st.session_state.diag_expand_version
    for i, (group_title, sym_items) in enumerate(SYMPTOM_GROUPS.items()):
        is_exp = st.session_state.diag_cat_expanded.get(i, False)
        with st.expander(group_title, expanded=is_exp, key=f"diag_cat_exp_{i}_{ver}"):
            cat_active = [k for k, _ in sym_items if st.session_state.get(f"chk_sym_{k}", False)]
            if cat_active:
                render_clean_html(f"""
                <div style="font-size: 0.82rem; color: #38bdf8; font-weight: 700; margin-bottom: 8px;">
                    ✓ {len(cat_active)} symptom(s) active in this category
                </div>
                """)

            cols = st.columns(2)
            for j, (k, label) in enumerate(sym_items):
                col = cols[j % 2]
                col.checkbox(label, key=f"chk_sym_{k}")

    # SECTION 2: TONGUE & PULSE EXAMINATION
    render_clean_html("""
    <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 10px; padding: 14px 18px; margin: 20px 0 12px 0;">
        <span style="font-size: 1.1rem; font-weight: 700; color: #c89666;">2. Tongue & Pulse Examination (舌诊 · 脉诊)</span>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-top: 2px;">Vital diagnostic pillars confirming internal Cold/Heat and Deficiency/Excess.</div>
    </div>
    """)

    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        sel_t_body = st.selectbox(
            "Tongue Body Color (舌质)",
            options=[
                "Normal Pale Red",
                "Pale / Whitish",
                "Red / Scarlet (Tip/Edges)",
                "Red / Scarlet (Body/Center)",
                "Deep Red / Crimson",
                "Swollen with Teeth Marks"
            ],
            key="sel_tongue_body_input"
        )
    with col_t2:
        sel_t_coat = st.selectbox(
            "Tongue Coating Color (舌苔颜色)",
            options=["Thin White", "Thick White", "Thin Yellow", "Thick Yellow", "Peeled / Geographic / Mirror", "None / Barely Any"],
            key="sel_tongue_coat_input"
        )
    with col_t3:
        sel_t_moist = st.selectbox(
            "Coating Moisture & Texture (舌面润燥)",
            options=["Normal Moist", "Dry / Lack of Fluids", "Wet / Moist / Slippery", "Greasy / Turbid", "Dry / Rough"],
            key="sel_tongue_moist_input"
        )

    # Pulse Quality Multiselect
    all_pulses = [
        "Floating (浮)", "Deep (沉)", "Rapid (数)", "Slow (迟)",
        "Slippery (滑)", "Wiry / Taut (弦)", "Weak / Empty (弱/虚)",
        "Fine / Thready (细)", "Tight (紧)", "Surging / Overflowing (洪)",
        "Soggy / Soft (濡)", "Full / Strong (实)"
    ]
    sel_pulses = st.multiselect(
        "Pulse Qualities (脉象 - Multiple Selection Supported)",
        options=all_pulses,
        key="sel_pulse_input"
    )

    st.write("")

    # RUN DIAGNOSTIC MATCHING
    diag_results = match_tcm_patterns(
        selected_symptoms=active_symptoms,
        sel_tongue_body=sel_t_body,
        sel_tongue_coat=sel_t_coat,
        sel_tongue_moisture=sel_t_moist,
        sel_pulses=sel_pulses
    )

    # SECTION 3: DIAGNOSTIC RESULTS & TREATMENT FORMULATION
    render_clean_html("""
    <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 10px; padding: 14px 18px; margin: 20px 0 16px 0;">
        <span style="font-size: 1.1rem; font-weight: 700; color: #484eb2;">3. Diagnostic Findings & Clinical Treatment Formulations (辩证论治)</span>
        <div style="font-size: 0.85rem; color: #cbd5e1; margin-top: 2px;">Ranked pattern differentiation with match confidence, points, herbal formulas, and advice.</div>
    </div>
    """)

    if not diag_results:
        render_clean_html("""
        <div style="background: #111827; border: 1px dashed rgba(255, 255, 255, 0.2); border-radius: 12px; padding: 28px 20px; text-align: center; margin: 12px 0;">
            <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
            <div style="font-size: 1.05rem; font-weight: 700; color: #ffffff;">No Symptoms Currently Selected</div>
            <div style="font-size: 0.9rem; color: #94a3b8; margin-top: 4px;">
                Check one or more symptoms above, or choose a quick scenario from the <strong>Quick Clinical Scenarios</strong> dropdown at the top.
            </div>
        </div>
        """)
    else:
        st.info(f"✨ Found **{len(diag_results)}** matching pattern(s) based on **{len(active_symptoms)}** symptoms, tongue presentation, and pulse characteristics.")

        # Display Top Diagnoses
        for rank, res in enumerate(diag_results[:4], start=1):
            pat = res["pattern"]
            conf = res["confidence"]
            key_m = res["key_matches"]
            sec_m = res["sec_matches"]
            pul_m = res["pulse_matches"]

            # Visual colors
            badge_color = "#10b981" if conf >= 75 else ("#38bdf8" if conf >= 55 else "#fbbf24")

            with st.container():
                render_clean_html(f"""
                <div style="background: #111827; border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
                        <div>
                            <span style="background: rgba(0, 123, 167, 0.35); color: #38bdf8; font-size: 0.76rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">
                                Rank #{rank} · {pat['category']}
                            </span>
                            <span style="background: rgba(72, 78, 178, 0.35); color: #c7d2fe; font-size: 0.76rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-left: 6px;">
                                {pat['nature']}
                            </span>
                            <h3 style="color: #ffffff !important; font-size: 1.4rem; font-weight: 800; margin: 8px 0 2px 0;">
                                {pat['name']}
                            </h3>
                            <div style="color: #c89666; font-size: 1.02rem; font-weight: 700;">
                                {pat['chinese']}
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 1.6rem; font-weight: 900; color: {badge_color};">
                                {conf}%
                            </div>
                            <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 600;">
                                MATCH CONFIDENCE
                            </div>
                        </div>
                    </div>
                    
                    <div style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.55; margin-top: 10px;">
                        {pat['description']}
                    </div>

                    <!-- Matched Elements Badges -->
                    <div style="display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0;">
                        <span style="font-size: 0.75rem; font-weight: 700; color: #94a3b8; align-self: center;">Matched Indicators:</span>
                        {''.join([f'<span style="background: rgba(16, 185, 129, 0.2); color: #34d399; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">✓ {m.replace("_", " ").title()}</span>' for m in key_m])}
                        {''.join([f'<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-size: 0.75rem; font-weight: 600; padding: 2px 8px; border-radius: 4px;">+ {m.replace("_", " ").title()}</span>' for m in sec_m])}
                        {''.join([f'<span style="background: rgba(200, 150, 102, 0.2); color: #fde68a; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">Pulse: {p}</span>' for p in pul_m])}
                    </div>

                    <!-- Treatment Principle Banner -->
                    <div style="background: rgba(0, 123, 167, 0.15); border-left: 4px solid #007ba7; border-radius: 6px; padding: 12px 16px; margin: 14px 0;">
                        <div style="font-size: 0.8rem; font-weight: 800; text-transform: uppercase; color: #38bdf8; margin-bottom: 2px;">
                            Treatment Principle (治法)
                        </div>
                        <div style="font-size: 0.95rem; font-weight: 600; color: #ffffff !important;">
                            {pat['treatment_principle']}
                        </div>
                    </div>
                </div>
                """)

                # Detailed Prescription and Modalities Expander
                with st.expander(f"📖 View Complete Treatment Prescription for {pat['name']}", expanded=(rank == 1)):
                    c_pt, c_herb = st.columns([1.1, 0.9])

                    with c_pt:
                        render_clean_html("<h4 style='color: #ffffff !important; margin-bottom: 8px;'>🎯 Primary Acupuncture Protocol</h4>")
                        for pt in pat["acupuncture_points"]:
                            render_clean_html(f"""
                            <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 10px 14px; margin-bottom: 8px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                    <span style="font-weight: 800; color: #38bdf8; font-size: 1rem;">{pt['code']} · {pt['name']}</span>
                                    <span style="font-size: 0.72rem; font-weight: 700; color: #c89666; background: rgba(200, 150, 102, 0.2); padding: 2px 6px; border-radius: 4px;">{pt['technique']}</span>
                                </div>
                                <div style="font-size: 0.85rem; font-weight: 600; color: #e2e8f0; margin-bottom: 2px;">
                                    <em>{pt['role']}</em>
                                </div>
                                <div style="font-size: 0.84rem; color: #94a3b8; line-height: 1.45;">
                                    {pt['rationale']}
                                </div>
                            </div>
                            """)

                    with c_herb:
                        render_clean_html("<h4 style='color: #ffffff !important; margin-bottom: 8px;'>🌿 Canonical Herbal Formula (方剂)</h4>")
                        herb = pat["herbal_formula"]
                        render_clean_html(f"""
                        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;">
                            <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff !important;">{herb['name']}</div>
                            <div style="font-size: 0.95rem; font-weight: 700; color: #c89666; margin-bottom: 8px;">{herb['chinese']}</div>
                            <div style="font-size: 0.82rem; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Key Ingredients:</div>
                            <div style="font-size: 0.85rem; color: #e2e8f0; margin-bottom: 8px;">{herb['key_herbs']}</div>
                            <div style="font-size: 0.82rem; font-weight: 700; color: #38bdf8; text-transform: uppercase;">Formula Action:</div>
                            <div style="font-size: 0.85rem; color: #cbd5e1;">{herb['action']}</div>
                        </div>
                        """)

                        render_clean_html("<h4 style='color: #ffffff !important; margin-bottom: 8px;'>🥗 Dietary & Lifestyle Guidance</h4>")
                        diet = pat["lifestyle_diet"]
                        render_clean_html(f"""
                        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 14px 16px;">
                            <div style="font-size: 0.85rem; margin-bottom: 6px;"><strong style="color: #34d399;">Recommended Foods:</strong> <span style="color: #e2e8f0;">{diet['recommended']}</span></div>
                            <div style="font-size: 0.85rem; margin-bottom: 6px;"><strong style="color: #f87171;">Foods to Avoid:</strong> <span style="color: #e2e8f0;">{diet['avoid']}</span></div>
                            <div style="font-size: 0.85rem;"><strong style="color: #c7d2fe;">Clinical Advice:</strong> <span style="color: #cbd5e1;">{diet['advice']}</span></div>
                        </div>
                        """)

                    st.write("")
                    if st.button(f"📋 Generate Clinical SOAP Note for {pat['name']}", key=f"btn_soap_diag_{rank}_{pat['id']}", use_container_width=True):
                        st.session_state.soap_data = {
                            "patient_name": "Encounter #" + pat['id'].upper()[:8],
                            "patient_age": 42,
                            "patient_gender": "Female",
                            "visit_date": str(date.today()),
                            "chief_complaint": f"Presenting with symptoms differentiated as {pat['name']} ({pat['chinese']}).",
                            "duration": "Subacute / Chronic presentation",
                            "modalities": "Worse with physical/emotional stress; relieved with rest and acupuncture.",
                            "secondary_symptoms": ", ".join([s.replace("_", " ").title() for s in key_m + sec_m]),
                            "tongue_body": sel_t_body,
                            "tongue_coat": f"{sel_t_coat}, {sel_t_moist}",
                            "pulse_qualities": ", ".join(sel_pulses) if sel_pulses else "Consistent with pattern",
                            "palpation_findings": "Reflex tenderness along matching channel and Back-Shu pathways.",
                            "tcm_diagnosis": f"{pat['name']} ({pat['chinese']})",
                            "eight_principles": pat['nature'],
                            "pathogenesis": pat['description'],
                            "western_correlate": pat['category'],
                            "primary_points": ", ".join([f"{pt['code']} ({pt['name']})" for pt in pat['acupuncture_points']]),
                            "needle_technique": "; ".join([f"{pt['code']}: {pt['technique']}" for pt in pat['acupuncture_points']]),
                            "retention_time": "25-30 minutes with De Qi sensation",
                            "adjunctive_modalities": "Ear seeds on Shen Men & organ reflex points. Moxibustion if cold.",
                            "herbal_formula": f"{pat['herbal_formula']['name']} ({pat['herbal_formula']['chinese']}) - {pat['herbal_formula']['action']}",
                            "lifestyle_diet": f"Eat: {pat['lifestyle_diet']['recommended']} | Avoid: {pat['lifestyle_diet']['avoid']}",
                            "treatment_course": "1-2 treatments per week for 4-6 weeks; re-evaluate in 2 weeks."
                        }
                        st.session_state.target_nav_tab = "SOAP Notes"
                        st.rerun()

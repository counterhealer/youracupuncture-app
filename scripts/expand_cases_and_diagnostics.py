# -*- coding: utf-8 -*-
"""Clinical Expansion Script: Diagnostics & Case Simulator.

Expands:
1. modules/internal_diagnostics.py:
   - Adds 12 canonical TCM patterns to DIAGNOSTIC_PATTERNS (reaching 27 patterns).
   - Adds new symptom keys to SYMPTOM_GROUPS.
   - Adds new clinical scenario presets to CLINICAL_PRESETS.

2. modules/cases_bank.py:
   - Adds 12 comprehensive board-exam patient cases (CASE-024 to CASE-035),
     reaching 35 clinical cases across Respiratory, Geriatrics, Digestion/Gallbladder,
     Urogenital Lin, Xiao Ke, Uterine Bleeding, Facial Spasms, Cardiac Red Flags,
     Psychiatric Phlegm-Fire, Pediatrics, Fibromyalgia, and Cervical Radiculopathy.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# =============================================================================
# PART 1: 12 NEW DIAGNOSTIC PATTERNS
# =============================================================================
NEW_DIAGNOSTIC_PATTERNS = [
    {
        "id": "kidney-jing-deficiency",
        "name": "Kidney Jing (Essence) Depletion",
        "chinese": "肾精不足 (Shèn Jīng Bù Zú)",
        "organ": "Kidney (肾)",
        "category": "Deficiency Patterns",
        "nature": "Essence Depletion (精亏)",
        "description": "Depletion of prenatal and postnatal Kidney Essence impairs marrow production, bone nourishment, brain function, and reproductive vitality.",
        "key_symptoms": [
            "soreness_lower_back_knees", "tinnitus_low_pitch", "developmental_delays_weak_bones",
            "poor_memory", "low_libido_impotence", "dizziness_vertigo"
        ],
        "secondary_symptoms": [
            "blurred_vision_floaters", "cold_limbs", "weak_limbs", "fatigue_exhaustion"
        ],
        "tongue_body": ["Pale / Whitish", "Red / Scarlet (Body/Center)"],
        "tongue_coat": ["Peeled / Geographic / Mirror", "Thin White"],
        "tongue_moisture": ["Dry / Lack of Fluids", "Normal Moist"],
        "pulses": ["Deep (沉)", "Weak / Frail (弱)", "Fine / Thready (细)"],
        "pathomechanism": "Kidney stores Jing and produces Marrow. Essence depletion leads to empty Marrow Sea (dizziness, tinnitus, poor memory), unanchored Yuan Qi, and brittle bones.",
        "treatment_principle": "Tonify Kidney Essence, nourish marrow, and strengthen Yuan Qi (补肾填精，充养骨髓).",
        "acupuncture_points": [
            {"code": "KI3", "name": "Taixi (太溪)", "role": "Yuan-Source Point", "technique": "Reinforcing (补法)", "rationale": "Premier point to nourish Kidney Yin, Yang, and Essence."},
            {"code": "BL23", "name": "Shenshu (肾俞)", "role": "Kidney Back-Shu", "technique": "Reinforcing / Moxa", "rationale": "Directly supplements Kidney prenatal Essence and lumbar strength."},
            {"code": "CV4", "name": "Guanyuan (关元)", "role": "Front-Mu of Small Intestine", "technique": "Reinforcing / Moxa", "rationale": "Roots Yuan Qi, nourishes Dan Tian, consolidates Essence."},
            {"code": "GB39", "name": "Xuanzhong (悬钟)", "role": "Hui-Meeting of Marrow", "technique": "Reinforcing (补法)", "rationale": "Directly benefits bone marrow, treats dizziness and bone weakness."},
            {"code": "GV20", "name": "Baihui (百会)", "role": "Sea of Marrow Summit", "technique": "Reinforcing (补法)", "rationale": "Raises clear Yang to the brain, clears memory fog."}
        ],
        "herbal_formula": {
            "name": "Zuo Gui Wan / He Che Da Zao Wan",
            "chinese": "左归丸 / 河车大造丸",
            "key_herbs": "Shu Di Huang, Shan Yao, Shan Zhu Yu, Gou Qi Zi, Lu Jiao Jiao, Gui Ban Jiao, Tu Si Zi, Niu Xi",
            "action": "Nourishes Kidney Essence, supplements bone marrow, and supports prenatal Yuan Qi."
        },
        "lifestyle_diet": {
            "recommended": "Black sesame seeds, walnuts, bone broth, goji berries, black beans, mulberry fruit.",
            "avoid": "Excessive sexual activity, extreme overwork, chronic sleep deprivation, excessive salt.",
            "advice": "Prioritize restorative deep sleep before 11 PM to replenish Kidney marrow."
        }
    },
    {
        "id": "heart-yang-deficiency",
        "name": "Heart Yang Deficiency",
        "chinese": "心阳虚 (Xīn Yáng Xū)",
        "organ": "Heart (心)",
        "category": "Emotional / Sleep",
        "nature": "Interior Cold Deficiency (里虚寒)",
        "description": "Deficiency of Heart Yang Qi leads to impaired blood circulation, cold extremities, chest oppression, and cardiac palpitation.",
        "key_symptoms": [
            "palpitations", "shortness_of_breath", "chest_fullness",
            "cold_limbs", "spontaneous_sweating", "fatigue_exhaustion"
        ],
        "secondary_symptoms": [
            "pale_complexion", "aversion_to_cold", "anxiety_restlessness", "weak_limbs"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thin White", "Thick White"],
        "tongue_moisture": ["Wet / Moist / Slippery"],
        "pulses": ["Deep (沉)", "Slow (迟)", "Knotted / Intermittent (结代)"],
        "pathomechanism": "Heart Yang fails to warm the chest and propel blood, causing palpitations, cold limbs, and spontaneous sweating.",
        "treatment_principle": "Warm and tonify Heart Yang, disperse cold, and calm the spirit (温补心阳，通脉安神).",
        "acupuncture_points": [
            {"code": "HT5", "name": "Tongli (通里)", "role": "Luo-Connecting Point", "technique": "Reinforcing (补法)", "rationale": "Regulates Heart rhythm, tonifies Heart Yang."},
            {"code": "PC6", "name": "Neiguan (内关)", "role": "Luo-Connecting Point", "technique": "Even or Reinforcing", "rationale": "Opens the chest, regulates coronary circulation, calms spirit."},
            {"code": "BL15", "name": "Xinshu (心俞)", "role": "Heart Back-Shu", "technique": "Reinforcing / Moxa", "rationale": "Infuses warming Yang directly into the Heart."},
            {"code": "CV17", "name": "Danzhong (膻中)", "role": "Hui-Meeting of Qi", "technique": "Moxibustion", "rationale": "Promotes circulation of Zong Qi and unbinds the chest."},
            {"code": "GV14", "name": "Dazhui (大椎)", "role": "Meeting of all Yang Channels", "technique": "Moxibustion", "rationale": "Boosts systemic Yang Qi and dispels cold."}
        ],
        "herbal_formula": {
            "name": "Bao Yuan Tang / Shen Fu Tang",
            "chinese": "保元汤 / 参附汤",
            "key_herbs": "Ren Shen, Fu Zi, Huang Qi, Rou Gui, Zhi Gan Cao",
            "action": "Rescues and warms Heart Yang, restores vascular tone, and halts spontaneous sweating."
        },
        "lifestyle_diet": {
            "recommended": "Warm cinnamon tea, ginger, stewed lamb, oats, walnuts, well-cooked warming broths.",
            "avoid": "Cold/raw foods, iced drinks, bitter cold herbs, exposure to drafts.",
            "advice": "Keep chest and upper back warm at all times. Avoid sudden extreme exertion."
        }
    },
    {
        "id": "heart-blood-stasis",
        "name": "Heart Blood Stasis / Chest Bi",
        "chinese": "心血瘀阻 (Xīn Xuè Yū Zǔ)",
        "organ": "Heart (心)",
        "category": "Emotional / Sleep",
        "nature": "Blood Stasis (血瘀)",
        "description": "Obstruction of Heart vessels by stagnant blood, manifesting as severe paroxysmal or stabbing chest pain radiating to the left shoulder and arm.",
        "key_symptoms": [
            "stabbing_chest_pain_radiating", "palpitations", "chest_fullness", "shortness_of_breath"
        ],
        "secondary_symptoms": [
            "cold_limbs", "anxiety_restlessness", "insomnia_dreamy", "pale_complexion"
        ],
        "tongue_body": ["Purple / Dusky / Petechiae", "Dark Crimson"],
        "tongue_coat": ["Thin White", "Thin Yellow"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Choppy / Hesitant (涩)", "Wiry / Taut (弦)", "Knotted / Intermittent (结代)"],
        "pathomechanism": "Stagnant blood blocks the Heart collaterals, impeding Yang Qi flow and producing sharp, localized ischemic chest pain.",
        "treatment_principle": "Invigorate blood, resolve stasis, open the chest, and stop pain (活血化瘀，通阳止痛).",
        "acupuncture_points": [
            {"code": "PC6", "name": "Neiguan (内关)", "role": "Master Point", "technique": "Reducing or Even", "rationale": "Opens the chest, invigorates coronary collaterals, relieves chest oppression."},
            {"code": "PC4", "name": "Ximen (郄门)", "role": "Xi-Cleft Point", "technique": "Reducing (泻法)", "rationale": "Premier point for acute blood stasis and severe cardiac chest pain."},
            {"code": "HT7", "name": "Shenmen (神门)", "role": "Yuan-Source Point", "technique": "Even Method", "rationale": "Nourishes Heart blood and stabilizes panic/anxiety."},
            {"code": "BL17", "name": "Geshu (膈俞)", "role": "Hui-Meeting of Blood", "technique": "Reducing (泻法)", "rationale": "Clears blood stasis and smooths circulation throughout the chest."},
            {"code": "SP10", "name": "Xuehai (血海)", "role": "Sea of Blood", "technique": "Reducing (泻法)", "rationale": "Invigorates blood and dispels systemic stasis."}
        ],
        "herbal_formula": {
            "name": "Xue Fu Zhu Yu Tang / Guan Xin Su He Wan",
            "chinese": "血府逐瘀汤 / 冠心苏合丸",
            "key_herbs": "Tao Ren, Hong Hua, Dang Gui, Chuan Xiong, Chi Shao, Dan Shen, Chai Hu, Zhi Ke, Niu Xi",
            "action": "Invigorates Blood, unblocks stagnant collaterals, and relieves angina pain."
        },
        "lifestyle_diet": {
            "recommended": "Hawthorn berry tea (Shan Zha), saffron, turmeric, brown rice, garlic, onions.",
            "avoid": "High-cholesterol greasy meats, smoking, heavy alcohol, sudden intense stress.",
            "advice": "EMERGENCY PROTOCOL: Crushing chest pain lasting > 15 mins with diaphoresis requires immediate 911 activation."
        }
    },
    {
        "id": "liver-yang-rising",
        "name": "Liver Yang Rising",
        "chinese": "肝阳上亢 (Gān Yáng Shàng Kàng)",
        "organ": "Liver (肝)",
        "category": "Emotional / Liver",
        "nature": "Excess Above, Deficiency Below (上盛下虚)",
        "description": "Deficiency of Kidney/Liver Yin fails to anchor Liver Yang, causing hyperactivity of Yang rushing upward to the head and temples.",
        "key_symptoms": [
            "severe_headache_temporal", "dizziness_vertigo", "tinnitus_loud",
            "irritability_mood_swings", "red_irritated_eyes"
        ],
        "secondary_symptoms": [
            "dry_throat_night", "insomnia_difficulty_falling_asleep",
            "soreness_lower_back_knees", "bitter_taste"
        ],
        "tongue_body": ["Red / Scarlet (Tip/Edges)", "Normal Pale Red"],
        "tongue_coat": ["Thin Yellow", "Peeled / Geographic / Mirror"],
        "tongue_moisture": ["Dry / Lack of Fluids", "Normal Moist"],
        "pulses": ["Wiry / Taut (弦)", "Rapid (数)"],
        "pathomechanism": "Water fails to nourish Wood. Liver Yang flares upward, creating throbbing temporal headaches, tinnitus like rushing waves, and red eyes.",
        "treatment_principle": "Subdue Liver Yang, nourish Yin, and anchor ascending hyperactivity (平肝潜阳，滋阴潜阳).",
        "acupuncture_points": [
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Clears ascending Liver Yang and subdues anger."},
            {"code": "GB20", "name": "Fengchi (风池)", "role": "Wind Pool", "technique": "Reducing (泻法)", "rationale": "Dispels local head wind, relieves temporal throbbing."},
            {"code": "KI3", "name": "Taixi (太溪)", "role": "Yuan-Source Point", "technique": "Reinforcing (补法)", "rationale": "Nourishes Kidney Water to anchor Liver Wood."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Supplements Yin fluids to pull upward Fire downward."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Pairs with LR3 (Four Gates) to open channels and stop pain."}
        ],
        "herbal_formula": {
            "name": "Tian Ma Gou Teng Yin",
            "chinese": "天麻钩藤饮",
            "key_herbs": "Tian Ma, Gou Teng, Shi Jue Ming, Zhi Zi, Huang Qin, Chuan Niu Xi, Du Zhong, Sang Ji Sheng, Ye Jiao Teng",
            "action": "Calms the Liver, extinguishes internal Wind, clears Heat, and nourishes the Kidneys."
        },
        "lifestyle_diet": {
            "recommended": "Chrysanthemum tea (Ju Hua), celery juice, mung bean soup, cucumber, pear.",
            "avoid": "Spicy foods, hot spirits, lamb, excessive coffee, emotional confrontation.",
            "advice": "Practice slow evening walks, meditation, and minimize late-night screen time."
        }
    },
    {
        "id": "liver-wind-extreme-heat",
        "name": "Extreme Heat Generating Liver Wind",
        "chinese": "热极生风 (Rè Jí Shēng Fēng)",
        "organ": "Liver (肝)",
        "category": "Emotional / Liver",
        "nature": "Internal Wind from Heat (热毒生风)",
        "description": "Blazing toxic heat scorches Liver Yin and burns the sinews, generating acute internal Wind with high fevers and convulsions.",
        "key_symptoms": [
            "high_fever", "tremors_convulsions", "stiff_neck", "anxiety_restlessness"
        ],
        "secondary_symptoms": [
            "severe_headache_temporal", "red_irritated_eyes", "thirst_cold", "dark_burning_urine"
        ],
        "tongue_body": ["Deep Red / Crimson", "Red / Scarlet (Tip/Edges)"],
        "tongue_coat": ["Thick Yellow", "Dry / Lack of Fluids"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Wiry / Taut (弦)", "Rapid (数)", "Surging / Overflowing (洪)"],
        "pathomechanism": "Extreme heat penetrates the Pericardium and Liver channels, scorching fluids and causing sinew spasms (opisthotonos, locked jaw, convulsions).",
        "treatment_principle": "Clear Heat, cool the Liver, extinguish Wind, and arrest convulsions (清热凉肝，息风止痉).",
        "acupuncture_points": [
            {"code": "GV20", "name": "Baihui (百会)", "role": "Sea of Marrow Summit", "technique": "Reducing (泻法)", "rationale": "Clears heat and pacifies internal wind."},
            {"code": "GV26", "name": "Renzhong (人中)", "role": "Emergency Resuscitation", "technique": "Firm Stimulation", "rationale": "Revives consciousness and stops acute convulsions."},
            {"code": "GV14", "name": "Dazhui (大椎)", "role": "Meeting of Yang", "technique": "Reducing / Cupping / Bleeding", "rationale": "Drains extreme pathogenic fire from all Yang meridians."},
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Sedates Liver Wind and calms spastic sinews."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Strongly clears toxic systemic heat."}
        ],
        "herbal_formula": {
            "name": "Ling Jiao Gou Teng Tang",
            "chinese": "羚角钩藤汤",
            "key_herbs": "Ling Yang Jiao, Gou Teng, Sang Ye, Ju Hua, Bai Shao, Sheng Di Huang, Chuan Bei Mu, Zhu Ru",
            "action": "Cool the Liver, extinguish internal Wind, augment Yin, and relax spastic sinews."
        },
        "lifestyle_diet": {
            "recommended": "Emergency medical stabilization; cool boiled water, electrolyte hydration.",
            "avoid": "All heating foods, physical restraint causing injury, drafts.",
            "advice": "RED FLAG: High-fever convulsions require immediate pediatric/emergency medical evaluation."
        }
    },
    {
        "id": "damp-heat-liver-gallbladder",
        "name": "Damp-Heat in Liver & Gallbladder",
        "chinese": "肝胆湿热 (Gān Dǎn Shī Rè)",
        "organ": "Liver (肝) / Gallbladder (胆)",
        "category": "Digestive",
        "nature": "Interior Damp-Heat (湿热)",
        "description": "Accumulation of pathogenic Dampness and Heat obstructs the Liver and Gallbladder, preventing free bile flow and causing hypochondriac distension and jaundice.",
        "key_symptoms": [
            "right_hypochondriac_pain_cramping", "jaundice_bright_yellow", "bitter_taste",
            "dark_burning_urine", "nausea_vomiting"
        ],
        "secondary_symptoms": [
            "poor_appetite", "bloating_after_eating", "foul_smelling_diarrhea", "low_fever"
        ],
        "tongue_body": ["Red / Scarlet (Tip/Edges)", "Red / Scarlet (Body/Center)"],
        "tongue_coat": ["Thick Yellow"],
        "tongue_moisture": ["Wet / Moist / Slippery", "Normal Moist"],
        "pulses": ["Slippery (滑)", "Rapid (数)", "Wiry / Taut (弦)"],
        "pathomechanism": "Damp-Heat steams the Liver and Gallbladder, forcing bile to spill into the bloodstream (jaundice) and tissues, and causing painful hypochondriac colic.",
        "treatment_principle": "Clear Heat, resolve Dampness, and soothe the Liver and Gallbladder (清利肝胆湿热).",
        "acupuncture_points": [
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "He-Sea / Hui of Sinews", "technique": "Reducing (泻法)", "rationale": "Unblocks Gallbladder channel, drains damp-heat, relieves biliary colic."},
            {"code": "GB24", "name": "Riyue (日月)", "role": "Gallbladder Front-Mu", "technique": "Reducing (泻法)", "rationale": "Directly clears local heat and distension in the Gallbladder."},
            {"code": "LR14", "name": "Qimen (期门)", "role": "Liver Front-Mu", "technique": "Reducing (泻法)", "rationale": "Regulates Liver Qi and resolves hypochondriac stasis."},
            {"code": "SP9", "name": "Yinlingquan (阴陵泉)", "role": "He-Sea Water Point", "technique": "Reducing (泻法)", "rationale": "Master point to drain dampness through urination."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Clears systemic heat and resolves toxins."}
        ],
        "herbal_formula": {
            "name": "Long Dan Xie Gan Tang / Yin Chen Hao Tang",
            "chinese": "龙胆泻肝汤 / 茵陈蒿汤",
            "key_herbs": "Long Dan Cao, Huang Qin, Zhi Zi, Ze Xie, Che Qian Zi, Chai Hu, Sheng Di Huang, Yin Chen, Da Huang",
            "action": "Drains Liver Fire, clears Lower Jiao Damp-Heat, and eliminates jaundice."
        },
        "lifestyle_diet": {
            "recommended": "Barley water, bitter melon, mung beans, dandelion greens, radishes, corn silk tea.",
            "avoid": "Alcohol, deep-fried food, cheese, greasy meats, chili, chocolate.",
            "advice": "RED FLAG: Check for Murphy's sign and Charcot's triad (RUQ pain, fever, jaundice)."
        }
    },
    {
        "id": "damp-heat-large-intestine",
        "name": "Damp-Heat in Large Intestine (Dysentery)",
        "chinese": "大肠湿热 (Dà Cháng Shī Rè)",
        "organ": "Large Intestine (大肠)",
        "category": "Digestive",
        "nature": "Interior Damp-Heat (湿热)",
        "description": "Pathogenic Damp-Heat brews in the Large Intestine, injuring the intestinal mucosa and causing tenesmus with bloody and mucous stools.",
        "key_symptoms": [
            "tenesmus_blood_mucus", "foul_smelling_diarrhea", "dark_burning_urine",
            "sharp_abdominal_pain_pressure"
        ],
        "secondary_symptoms": [
            "low_fever", "poor_appetite", "thirst_cold"
        ],
        "tongue_body": ["Red / Scarlet (Body/Center)", "Red / Scarlet (Tip/Edges)"],
        "tongue_coat": ["Thick Yellow"],
        "tongue_moisture": ["Wet / Moist / Slippery", "Normal Moist"],
        "pulses": ["Slippery (滑)", "Rapid (数)"],
        "pathomechanism": "Dampness and Heat injure the blood vessels of the bowel, leading to foul diarrhea with blood and pus, with tenesmus from Qi stagnation.",
        "treatment_principle": "Clear Heat, resolve Dampness, cool Blood, and stop dysenteric diarrhea (清热利湿，凉血止痢).",
        "acupuncture_points": [
            {"code": "ST25", "name": "Tianshu (天枢)", "role": "Front-Mu of Large Intestine", "technique": "Reducing (泻法)", "rationale": "Regulates bowel Qi, clears intestinal damp-heat, stops diarrhea."},
            {"code": "ST37", "name": "Shangjuxu (上巨虚)", "role": "Lower He-Sea of Large Intestine", "technique": "Reducing (泻法)", "rationale": "Premier distal point for all acute Large Intestine disorders."},
            {"code": "SP9", "name": "Yinlingquan (阴陵泉)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Promotes diuresis to drain Dampness downward."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Clears Yangming heat and toxic inflammation."},
            {"code": "CV12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Even or Reducing", "rationale": "Harmonizes the middle jiao and regulates digestion."}
        ],
        "herbal_formula": {
            "name": "Bai Tou Weng Tang / Shao Yao Tang",
            "chinese": "白头翁汤 / 芍药汤",
            "key_herbs": "Bai Tou Weng, Huang Lian, Huang Bo, Qin Pi, Shao Yao, Dang Gui, Mu Xiang, Bing Lang",
            "action": "Clears Heat, detoxifies, cools Blood, and resolves tenesmus."
        },
        "lifestyle_diet": {
            "recommended": "Electrolyte broths, congee with lotus seeds, purslane (Ma Chi Xian), plenty of boiled water.",
            "avoid": "Raw salads, spicy peppers, dairy, alcohol, cold drinks.",
            "advice": "Monitor hydration closely. Stool culture recommended to exclude bacterial infection."
        }
    },
    {
        "id": "damp-heat-urinary-bladder",
        "name": "Damp-Heat in Urinary Bladder (Lin Syndrome)",
        "chinese": "膀胱湿热 (Páng Guāng Shī Rè)",
        "organ": "Bladder (膀胱)",
        "category": "Digestive",
        "nature": "Interior Damp-Heat (湿热)",
        "description": "Damp-Heat accumulates in the lower burner, impairing the Bladder Qi transformation and producing painful, burning, urgent urination.",
        "key_symptoms": [
            "burning_dysuria_urgency", "bloody_urine", "dark_burning_urine",
            "sharp_abdominal_pain_pressure"
        ],
        "secondary_symptoms": [
            "low_fever", "thirst_cold", "bitter_taste"
        ],
        "tongue_body": ["Red / Scarlet (Tip/Edges)", "Red / Scarlet (Body/Center)"],
        "tongue_coat": ["Thick Yellow"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Slippery (滑)", "Rapid (数)"],
        "pathomechanism": "Damp-Heat constricts the urethral passages and injures local blood vessels, producing burning dysuria and hematuria.",
        "treatment_principle": "Clear Heat, drain Dampness, unblock the waterways, and relieve painful Lin (清热利湿，通淋止痛).",
        "acupuncture_points": [
            {"code": "BL28", "name": "Pangguangshu (膀胱俞)", "role": "Bladder Back-Shu", "technique": "Reducing (泻法)", "rationale": "Directly clears Heat and Dampness from the urinary bladder."},
            {"code": "CV3", "name": "Zhongji (中极)", "role": "Bladder Front-Mu", "technique": "Reducing (泻法)", "rationale": "Opens the lower burner waterways, stops dysuria pain."},
            {"code": "SP9", "name": "Yinlingquan (阴陵泉)", "role": "He-Sea Point", "technique": "Reducing (泻法)", "rationale": "Drains dampness through the urinary pathway."},
            {"code": "BL63", "name": "Jinmen (金门)", "role": "Bladder Xi-Cleft", "technique": "Reducing (泻法)", "rationale": "Relieves acute excruciating urinary spasms and pain."},
            {"code": "SP10", "name": "Xuehai (血海)", "role": "Sea of Blood", "technique": "Reducing (泻法)", "rationale": "Cools Blood and stops hematuria (blood in urine)."}
        ],
        "herbal_formula": {
            "name": "Ba Zheng San / Xiao Ji Yin Zi",
            "chinese": "八正散 / 小蓟饮子",
            "key_herbs": "Che Qian Zi, Qu Mai, Bian Xu, Hua Shi, Zhi Zi, Da Huang, Mu Tong, Xiao Ji, Pu Huang, Ou Jie",
            "action": "Clears Heat, purges Fire, drains Dampness, and stops hematuria."
        },
        "lifestyle_diet": {
            "recommended": "Cranberry tea, corn silk water, barley water, watermelon, plenty of pure warm water.",
            "avoid": "Coffee, alcohol, spicy seasonings, sugar, carbonated beverages.",
            "advice": "RED FLAG: Check for high fever and costovertebral tenderness (pyelonephritis)."
        }
    },
    {
        "id": "stomach-yin-deficiency",
        "name": "Stomach Yin Deficiency",
        "chinese": "胃阴虚 (Wèi Yīn Xū)",
        "organ": "Stomach (胃)",
        "category": "Digestive",
        "nature": "Yin Deficiency with Dryness (阴虚内热)",
        "description": "Deficiency of Stomach fluids impairs digestive moistening and descending, causing hunger without desire to eat, dry throat, and peeled tongue.",
        "key_symptoms": [
            "hunger_no_appetite", "dry_throat_night", "dry_constipation", "epigastric_burning"
        ],
        "secondary_symptoms": [
            "nausea_vomiting", "acid_reflux", "five_palm_heat", "low_fever"
        ],
        "tongue_body": ["Red / Scarlet (Body/Center)", "Deep Red / Crimson"],
        "tongue_coat": ["Peeled / Geographic / Mirror"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Fine / Thready (细)", "Rapid (数)"],
        "pathomechanism": "Stomach Yin fluids are consumed by chronic heat, irregular diet, or febrile disease, leaving the stomach mucosa dry and unlubricated.",
        "treatment_principle": "Nourish Stomach Yin, generate fluids, and harmonize the stomach (养阴益胃，生津止渴).",
        "acupuncture_points": [
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Reinforcing (补法)", "rationale": "Tonifies Stomach Qi and stimulates fluid generation."},
            {"code": "SP6", "name": "Sanyinjiao (三阴交)", "role": "Three Yin Crossing", "technique": "Reinforcing (补法)", "rationale": "Supplements systemic Yin fluids and soothes dryness."},
            {"code": "CV12", "name": "Zhongwan (中脘)", "role": "Stomach Front-Mu", "technique": "Even Method", "rationale": "Harmonizes Stomach Qi and nourishes middle burner."},
            {"code": "ST44", "name": "Neiting (内庭)", "role": "Ying-Spring Point", "technique": "Reducing (泻法)", "rationale": "Clears empty heat from the Stomach channel."},
            {"code": "KI6", "name": "Zhaohai (照海)", "role": "Yin Qiao Master", "technique": "Reinforcing (补法)", "rationale": "Generates throat and stomach fluids."}
        ],
        "herbal_formula": {
            "name": "Yi Wei Tang / Sha Shen Mai Dong Tang",
            "chinese": "益胃汤 / 沙参麦冬汤",
            "key_herbs": "Sha Shen, Mai Men Dong, Sheng Di Huang, Yu Zhu, Bing Tang",
            "action": "Nourishes Stomach Yin, generates body fluids, and moistens dryness."
        },
        "lifestyle_diet": {
            "recommended": "Pears, lily bulbs (Bai He), tremella fungus (Yin Er), apple sauce, barley congee.",
            "avoid": "Spicy seasonings, dry crackers, roasted nuts, coffee, alcohol.",
            "advice": "Eat small, moist, easily digestible meals at regular intervals."
        }
    },
    {
        "id": "lung-yin-deficiency",
        "name": "Lung Yin Deficiency",
        "chinese": "肺阴虚 (Fèi Yīn Xū)",
        "organ": "Lung (肺)",
        "category": "Exterior / Respiratory",
        "nature": "Yin Deficiency with Empty Fire (阴虚内燥)",
        "description": "Deficiency of Lung Yin leads to failure of moistening and descending, producing a dry hacking cough, blood-streaked sputum, and tidal heat.",
        "key_symptoms": [
            "dry_unproductive_cough", "cough_blood_streaked", "dry_throat_night",
            "night_sweating", "five_palm_heat", "low_fever"
        ],
        "secondary_symptoms": [
            "shortness_of_breath", "palpitations", "fatigue_exhaustion"
        ],
        "tongue_body": ["Red / Scarlet (Tip/Edges)", "Deep Red / Crimson"],
        "tongue_coat": ["Peeled / Geographic / Mirror", "Thin White"],
        "tongue_moisture": ["Dry / Lack of Fluids"],
        "pulses": ["Fine / Thready (细)", "Rapid (数)"],
        "pathomechanism": "Lung fluids are depleted, leaving the bronchial tree dry. Empty Fire flares upward, injuring delicate blood vessels and causing hemoptysis.",
        "treatment_principle": "Nourish Lung Yin, moisten dryness, clear empty fire, and stop cough (滋阴润肺，清虚热止咳).",
        "acupuncture_points": [
            {"code": "LU9", "name": "Taiyuan (太渊)", "role": "Yuan-Source / Hui of Vessels", "technique": "Reinforcing (补法)", "rationale": "Premier point to tonify Lung Yin and vessel integrity."},
            {"code": "LU7", "name": "Lieque (列缺)", "role": "Luo-Connecting Point", "technique": "Reinforcing (补法)", "rationale": "Opens Ren Mai, restores Lung descending function."},
            {"code": "BL13", "name": "Feishu (肺俞)", "role": "Lung Back-Shu", "technique": "Reinforcing (补法)", "rationale": "Directly nourishes Lung organ and calms cough."},
            {"code": "BL43", "name": "Gaohuangshu (膏肓俞)", "role": "Tonic Master Point", "technique": "Reinforcing (补法)", "rationale": "Renowned point for deep chronic Lung and Yin deficiency."},
            {"code": "KI6", "name": "Zhaohai (照海)", "role": "Confluent of Yin Qiao", "technique": "Reinforcing (补法)", "rationale": "Pairs with LU7 to nourish throat, chest, and lung fluids."}
        ],
        "herbal_formula": {
            "name": "Bai He Gu Jin Tang / Mai Wei Di Huang Wan",
            "chinese": "百合固金汤 / 麦味地黄丸",
            "key_herbs": "Bai He, Sheng Di Huang, Shu Di Huang, Mai Dong, Xuan Shen, Chuan Bei Mu, Jie Geng, Dang Gui, Bai Shao, Gan Cao",
            "action": "Nourishes Lung and Kidney Yin, moistens the lungs, transforms phlegm, and arrests bleeding."
        },
        "lifestyle_diet": {
            "recommended": "Steamed pear with honey and Chuan Bei Mu, almond milk, loquat, white fungus, lotus root.",
            "avoid": "Smoking, vaping, spicy peppers, deep-fried food, dry arid environments.",
            "advice": "Use a room humidifier during sleep. Avoid shouting or straining vocal cords."
        }
    },
    {
        "id": "spleen-not-controlling-blood",
        "name": "Spleen Failing to Control Blood",
        "chinese": "脾不统血 (Pí Bù Tǒng Xuè)",
        "organ": "Spleen (脾)",
        "category": "Deficiency Patterns",
        "nature": "Qi Deficiency with Hemorrhage (气虚失统)",
        "description": "Deficiency of Spleen Qi fails to keep Blood flowing within the vessels, resulting in chronic extravasation of blood (petechiae, purpura, menorrhagia).",
        "key_symptoms": [
            "petechiae_purpura_bleeding", "pale_complexion", "fatigue_exhaustion",
            "poor_appetite", "loose_stools"
        ],
        "secondary_symptoms": [
            "dizziness_vertigo", "shortness_of_breath", "cold_limbs", "palpitations"
        ],
        "tongue_body": ["Pale / Whitish", "Swollen with Teeth Marks"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Normal Moist"],
        "pulses": ["Weak / Frail (弱)", "Fine / Thready (细)"],
        "pathomechanism": "Spleen Qi is the commander of blood. When Spleen Qi is depleted, it loses its holding power, and blood leaks out of channels into skin, stool, or uterus.",
        "treatment_principle": "Tonify Spleen Qi, raise sunken Yang, and astringe blood vessels (健脾益气，摄血统血).",
        "acupuncture_points": [
            {"code": "SP1", "name": "Yinbai (隐白)", "role": "Jing-Well Wood Point", "technique": "Direct Moxibustion (艾灸)", "rationale": "Premier empirical master point to astringe hemorrhage and stop bleeding."},
            {"code": "SP10", "name": "Xuehai (血海)", "role": "Sea of Blood", "technique": "Reinforcing (补法)", "rationale": "Regulates and anchors blood within the vessels."},
            {"code": "BL20", "name": "Pishu (脾俞)", "role": "Spleen Back-Shu", "technique": "Reinforcing / Moxa", "rationale": "Tonifies Spleen Qi to restore blood-holding capacity."},
            {"code": "CV12", "name": "Zhongwan (中脘)", "role": "Front-Mu of Stomach", "technique": "Reinforcing (补法)", "rationale": "Strengthens source of Qi and Blood production."},
            {"code": "GV20", "name": "Baihui (百会)", "role": "Sea of Marrow Summit", "technique": "Moxibustion", "rationale": "Lifts sunken Qi and prevents downward blood collapse."}
        ],
        "herbal_formula": {
            "name": "Gui Pi Tang",
            "chinese": "归脾汤",
            "key_herbs": "Ren Shen, Huang Qi, Bai Zhu, Fu Shen, Dang Gui, Long Yan Rou, Suan Zao Ren, Yuan Zhi, Mu Xiang, Zhi Gan Cao",
            "action": "Tonifies Qi and Blood, strengthens the Spleen, nourishes the Heart, and holds Blood in vessels."
        },
        "lifestyle_diet": {
            "recommended": "Red dates (Da Zao), longan fruit, black rice congee, beetroot, chicken soup with astragalus.",
            "avoid": "Raw/cold food, iced beverages, excessive mental brooding, physical overexertion.",
            "advice": "Moxibustion on SP1 (Yinbai) for 10-15 minutes daily is clinically pivotal."
        }
    },
    {
        "id": "kidney-qi-not-firm",
        "name": "Kidney Qi Not Firm",
        "chinese": "肾气不固 (Shèn Qì Bù Gù)",
        "organ": "Kidney (肾)",
        "category": "Deficiency Patterns",
        "nature": "Qi Deficiency Failing to Consolidate (气虚失约)",
        "description": "Deficiency of Kidney Qi leads to failure of consolidating the lower gates, causing urinary incontinence, enuresis, nocturnal emissions, or chronic leukorrhea.",
        "key_symptoms": [
            "pale_profuse_urine", "turbid_urine_milky", "soreness_lower_back_knees",
            "low_libido_impotence", "cold_limbs"
        ],
        "secondary_symptoms": [
            "dizziness_vertigo", "tinnitus_low_pitch", "fatigue_exhaustion", "spontaneous_sweating"
        ],
        "tongue_body": ["Pale / Whitish"],
        "tongue_coat": ["Thin White"],
        "tongue_moisture": ["Wet / Moist / Slippery", "Normal Moist"],
        "pulses": ["Deep (沉)", "Weak / Frail (弱)"],
        "pathomechanism": "Kidney controls the two lower orifices. Depleted Kidney Qi cannot seal and consolidate, letting bodily fluids leak out unchecked.",
        "treatment_principle": "Tonify and consolidate Kidney Qi, secure lower gates (补肾益气，固精止遗).",
        "acupuncture_points": [
            {"code": "BL23", "name": "Shenshu (肾俞)", "role": "Kidney Back-Shu", "technique": "Reinforcing / Moxa", "rationale": "Strengthens Kidney Qi and consolidates the bladder sphincter."},
            {"code": "CV4", "name": "Guanyuan (关元)", "role": "Dan Tian Master", "technique": "Reinforcing / Moxa", "rationale": "Directly warms and binds the lower orifices."},
            {"code": "GV4", "name": "Mingmen (命门)", "role": "Gate of Life", "technique": "Moxibustion", "rationale": "Warms Yang to seal lower burner leakage."},
            {"code": "KI3", "name": "Taixi (太溪)", "role": "Yuan-Source Point", "technique": "Reinforcing (补法)", "rationale": "Tonifies Kidney Qi and nourishes essence."},
            {"code": "BL52", "name": "Zhishi (志室)", "role": "Residence of Will", "technique": "Reinforcing / Moxa", "rationale": "Empirical point to consolidate sexual and urinary essence."}
        ],
        "herbal_formula": {
            "name": "Jin Suo Gu Jing Wan / Su Quan Wan",
            "chinese": "金锁固精丸 / 缩泉丸",
            "key_herbs": "Sha Yuan Zi, Qian Shi, Lian Xu, Long Gu, Mu Li, Lian Zi, Yi Zhi Ren, Wu Yao, Shan Yao",
            "action": "Astringes Kidney Essence, tonifies Kidney Qi, and stops leakage from the lower burner."
        },
        "lifestyle_diet": {
            "recommended": "Walnuts, lotus seeds, Chinese yam (Shan Yao), black sesame, raspberry (Fu Pen Zi), chestnuts.",
            "avoid": "Cold melons, beer, iced drinks, diuretics, holding urine for too long.",
            "advice": "Kegel exercises and Dan Tian breathing exercises daily to restore pelvic floor tonicity."
        }
    }
]

# New symptoms to inject into SYMPTOM_GROUPS
NEW_SYMPTOMS_TO_INJECT = {
    "🫁 Respiration, Chest & Heart": [
        ("stabbing_chest_pain_radiating", "Stabbing chest pain radiating to left shoulder/arm (胸痹心痛彻背)"),
        ("cough_blood_streaked", "Cough with blood-streaked sputum / hemoptysis (咳血/痰中带血)"),
        ("dry_unproductive_cough", "Dry hacking cough with scanty sticky sputum (干咳无痰/少痰质粘)")
    ],
    "🚽 Bowels & Urination": [
        ("burning_dysuria_urgency", "Urgent, frequent, burning painful dysuria (小便频急淋漓涩痛)"),
        ("bloody_urine", "Hematuria / Blood in urine (尿血)"),
        ("tenesmus_blood_mucus", "Tenesmus with foul bloody mucous stools (下痢赤白/里急后重)"),
        ("turbid_urine_milky", "Turbid, milky or fatty urine (小便混浊如膏脂)")
    ],
    "🍲 Digestion, Thirst & Abdomen": [
        ("right_hypochondriac_pain_cramping", "Severe right hypochondriac colicky pain radiating to shoulder (右上腹胆区绞痛彻背)"),
        ("jaundice_bright_yellow", "Bright orange-yellow jaundice of eyes & skin (身目发黄鲜明如橘子色)"),
        ("hunger_no_appetite", "Hunger without desire to eat / dry mouth (消谷无欲/干呕口渴)")
    ],
    "💪 Body, Limbs & Vitality": [
        ("petechiae_purpura_bleeding", "Subcutaneous hemorrhages / purpura / easy bruising (皮下紫斑/衄血)"),
        ("developmental_delays_weak_bones", "Premature hair loss / loose teeth / weak brittle bones (发落齿摇/骨质脆弱)"),
        ("tremors_convulsions", "Involuntary facial or limb tremors / convulsions (震颤/四肢抽搐)")
    ]
}

# New presets to inject into CLINICAL_PRESETS
NEW_PRESETS = {
    "Acute Biliary Colic / Cholecystitis (肝胆湿热)": {
        "symptoms": ["right_hypochondriac_pain_cramping", "jaundice_bright_yellow", "bitter_taste", "dark_burning_urine", "nausea_vomiting", "poor_appetite"],
        "tongue_body": "Red / Scarlet (Tip/Edges)",
        "tongue_coat": "Thick Yellow",
        "tongue_moisture": "Normal Moist",
        "pulse": "Wiry / Taut (弦)"
    },
    "Acute Bloody Lin / UTI with Hematuria (膀胱湿热/血淋)": {
        "symptoms": ["burning_dysuria_urgency", "bloody_urine", "dark_burning_urine", "sharp_abdominal_pain_pressure"],
        "tongue_body": "Red / Scarlet (Body/Center)",
        "tongue_coat": "Thick Yellow",
        "tongue_moisture": "Normal Moist",
        "pulse": "Rapid (数)"
    },
    "Heart Blood Stasis / Angina Pectoris (心血瘀阻/胸痹)": {
        "symptoms": ["stabbing_chest_pain_radiating", "palpitations", "chest_fullness", "shortness_of_breath", "cold_limbs"],
        "tongue_body": "Purple / Dusky / Petechiae",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Normal Moist",
        "pulse": "Choppy / Hesitant (涩)"
    },
    "Lung Yin Deficiency with Hemoptysis (肺阴虚咳血)": {
        "symptoms": ["dry_unproductive_cough", "cough_blood_streaked", "dry_throat_night", "night_sweating", "five_palm_heat", "low_fever"],
        "tongue_body": "Deep Red / Crimson",
        "tongue_coat": "Peeled / Geographic / Mirror",
        "tongue_moisture": "Dry / Lack of Fluids",
        "pulse": "Fine / Thready (细)"
    },
    "Spleen Not Controlling Blood / Uterine Bleeding (脾不统血/崩漏)": {
        "symptoms": ["petechiae_purpura_bleeding", "pale_complexion", "fatigue_exhaustion", "poor_appetite", "loose_stools", "dizziness_vertigo"],
        "tongue_body": "Pale / Whitish",
        "tongue_coat": "Thin White",
        "tongue_moisture": "Normal Moist",
        "pulse": "Weak / Frail (弱)"
    }
}

print("Expansion definitions prepared successfully.")

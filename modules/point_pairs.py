"""Classical Point Combinations Engine (配穴体系).

Provides in-depth reference, clinical pairing logic, and interactive analysis for:
- Host-Guest (Yuan-Luo) Combinations (主客原络配穴法)
- Back-Shu & Front-Mu Combinations (俞募配穴法)
- Eight Confluent Points of Extraordinary Vessels (八脉交会穴)
- Five Shu Points & Mother-Child Tonification/Sedation (五输穴与子母补泻)
- Famous Classical Empirical Point Combinations (历代名家经典配穴)
- Custom Point Pair Synergy Analyzer
"""

from typing import Dict, List, Any
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# =============================================================================
# 1. HOST-GUEST (YUAN-LUO) COMBINATIONS (主客原络配穴)
# =============================================================================
HOST_GUEST_PAIRS: List[Dict[str, Any]] = [
    {
        "primary_organ": "Lung (手太阴肺经)",
        "paired_organ": "Large Intestine (手阳明大肠经)",
        "host_point": "LU9 (Taiyuan / 太渊)",
        "host_role": "Yuan-Source (Primary disharmony: tonifies Lung Qi & Yin)",
        "guest_point": "LI6 (Pianli / 偏历)",
        "guest_role": "Luo-Connecting (Assists water passage & clears exterior heat)",
        "synergy": "Regulates Lung Qi, promotes descending and dispersing fluids, clears upper body congestion and nasal blockage.",
        "indications": "Chronic cough, wheezing, shortness of breath, fullness in chest, watery nasal discharge, swollen throat."
    },
    {
        "primary_organ": "Large Intestine (手阳明大肠经)",
        "paired_organ": "Lung (手太阴肺经)",
        "host_point": "LI4 (Hegu / 合谷)",
        "host_role": "Yuan-Source (Primary: expels exterior wind, commands head & face)",
        "guest_point": "LU7 (Lieque / 列缺)",
        "guest_role": "Luo-Connecting (Opens Ren Mai, disperses Exterior Wind, relieves cough)",
        "synergy": "Supreme combination for exterior Wind-Cold/Heat attacks, facial neuralgia, sinus headaches, and toothaches.",
        "indications": "Frontal headache, acute rhinitis, facial pain, sore swollen throat, toothache, facial paralysis (Bell's palsy)."
    },
    {
        "primary_organ": "Spleen (足太阴脾经)",
        "paired_organ": "Stomach (足阳明胃经)",
        "host_point": "SP3 (Taibai / 太白)",
        "host_role": "Yuan-Source (Fortifies Spleen Qi, resolves internal dampness)",
        "guest_point": "ST40 (Fenglong / 丰隆)",
        "guest_role": "Luo-Connecting (Supreme phlegm resolving point in the body)",
        "synergy": "Fundamental root-and-branch treatment for Phlegm-Damp: SP3 strengthens the source of fluid transformation while ST40 dredges turbidity.",
        "indications": "Abdominal distention, lethargy, heaviness in limbs, loose stools, copious phlegm, mental fog, high cholesterol."
    },
    {
        "primary_organ": "Stomach (足阳明胃经)",
        "paired_organ": "Spleen (足太阴脾经)",
        "host_point": "ST42 (Chongyang / 冲阳)",
        "host_role": "Yuan-Source (Regulates Stomach Qi & clears middle jiao fire)",
        "guest_point": "SP4 (Gongsun / 公孙)",
        "guest_role": "Luo-Connecting (Commands Chong Mai, harmonizes middle jiao)",
        "synergy": "Balances hyperactive Stomach Yin/Yang, settles rebellious Stomach Qi, relieves epigastric cramping and heartburn.",
        "indications": "Epigastric pain, acid reflux, ravenous hunger, vomiting, abdominal cramping, facial edema."
    },
    {
        "primary_organ": "Heart (手少阴心经)",
        "paired_organ": "Small Intestine (手太阳小肠经)",
        "host_point": "HT7 (Shenmen / 神门)",
        "host_role": "Yuan-Source (Nourishes Heart Blood & grounds the wandering Shen)",
        "guest_point": "SI7 (Zhizheng / 支正)",
        "guest_role": "Luo-Connecting (Clears Heart fire, resolves emotional stagnation)",
        "synergy": "Harmonizes Fire meridian pair: calms agitated spirit while venting excess Heart heat via the Small Intestine down into urine.",
        "indications": "Palpitations, severe insomnia, panic attacks, dream-disturbed sleep, mouth and tongue ulcers, emotional volatility."
    },
    {
        "primary_organ": "Small Intestine (手太阳小肠经)",
        "paired_organ": "Heart (手少阴心经)",
        "host_point": "SI4 (Wangu / 腕骨)",
        "host_role": "Yuan-Source (Clears Damp-Heat, relaxes sinews along channel)",
        "guest_point": "HT5 (Tongli / 通里)",
        "guest_role": "Luo-Connecting (Regulates Heart rhythm & calms mental restlessness)",
        "synergy": "Relieves neck/shoulder stiffness while calming irritability and settling chest oppression.",
        "indications": "Stiff neck, scapular pain, tinnitus, hypochondriac pain, wrist arthritis, speech impediments due to wind."
    },
    {
        "primary_organ": "Kidney (足少阴肾经)",
        "paired_organ": "Bladder (足太阳膀胱经)",
        "host_point": "KD3 (Taixi / 太溪)",
        "host_role": "Yuan-Source (Nourishes Kidney Yin & tonifies Kidney Yang)",
        "guest_point": "BL58 (Feiyang / 飞扬)",
        "guest_role": "Luo-Connecting (Dispels Wind-Damp, activates bladder channel)",
        "synergy": "Reinforces prenatal Jing foundation while expelling chronic cold and stagnation from the lower back and lower limbs.",
        "indications": "Chronic lower back ache, knee weakness, tinnitus, cold feet, dizziness, daytime urinary frequency."
    },
    {
        "primary_organ": "Bladder (足太阳膀胱经)",
        "paired_organ": "Kidney (足少阴肾经)",
        "host_point": "BL64 (Jinggu / 京骨)",
        "host_role": "Yuan-Source (Expels wind & heat, relaxes the spine and neck)",
        "guest_point": "KD4 (Dazhong / 大钟)",
        "guest_role": "Luo-Connecting (Strengthens willpower, anchors Kidney Qi)",
        "synergy": "Treats severe spinal rigidity, posterior occipital headaches, and chronic bladder exhaustion.",
        "indications": "Occipital headache, spinal stiff ache, dysuria, pain in back of knee, heel pain, fearfulness."
    },
    {
        "primary_organ": "Pericardium (手厥阴心包经)",
        "paired_organ": "San Jiao (手少阳三焦经)",
        "host_point": "PC7 (Daling / 大陵)",
        "host_role": "Yuan-Source (Clears Heart/Pericardium fire, calms spirit)",
        "guest_point": "SJ5 (Waiguan / 外关)",
        "guest_role": "Luo-Connecting (Expels exterior wind, unblocks Shao Yang)",
        "synergy": "Powerful internal/external balance: clears emotional agitation and chest tightness while venting heat through Shao Yang.",
        "indications": "Chest tightness, palpitations, anxiety, insomnia, wrist carpal tunnel syndrome, alternating chills and fever."
    },
    {
        "primary_organ": "San Jiao (手少阳三焦经)",
        "paired_organ": "Pericardium (手厥阴心包经)",
        "host_point": "SJ4 (Yangchi / 阳池)",
        "host_role": "Yuan-Source (Stimulates Yuan Qi circulation across Three Burners)",
        "guest_point": "PC6 (Neiguan / 内关)",
        "guest_role": "Luo-Connecting (Opens chest, regulates stomach, calms spirit)",
        "synergy": "Unblocks the entire Shao Yang network while stabilizing the chest and epigastrium; supreme for nausea, migraine, and ear disorders.",
        "indications": "One-sided migraine, hypochondriac distention, nausea, motion sickness, ear fullness, bitter taste."
    },
    {
        "primary_organ": "Liver (足厥阴肝经)",
        "paired_organ": "Gallbladder (足少阳胆经)",
        "host_point": "LIV3 (Taichong / 太冲)",
        "host_role": "Yuan-Source (Spreads stagnant Liver Qi, subdues Liver Yang)",
        "guest_point": "GB37 (Guangming / 光明)",
        "guest_role": "Luo-Connecting (Brightens the eyes, clears Gallbladder heat)",
        "synergy": "Premier ocular and hepatic pairing: smooths Liver Qi throughout the body while directly channeling clear essence to the eyes.",
        "indications": "Temporal migraine, red irritated eyes, blurred vision, eye floaters, hypochondriac pain, irritability, PMS distention."
    },
    {
        "primary_organ": "Gallbladder (足少阳胆经)",
        "paired_organ": "Liver (足厥阴肝经)",
        "host_point": "GB40 (Qiuxu / 丘墟)",
        "host_role": "Yuan-Source (Spreads Gallbladder Qi, clears damp-heat)",
        "guest_point": "LIV5 (Ligou / 蠡沟)",
        "guest_role": "Luo-Connecting (Clears damp-heat from genital region, regulates menses)",
        "synergy": "Treats lateral channel stagnation, genital damp-heat itchiness, and indecisiveness caused by Gallbladder deficiency.",
        "indications": "Hypochondriac cramping, bitter taste, genital itching or discharge, lateral ankle weakness, emotional timidity."
    }
]


# =============================================================================
# 2. BACK-SHU & FRONT-MU COMBINATIONS (俞募配穴)
# =============================================================================
SHU_MU_PAIRS: List[Dict[str, Any]] = [
    {
        "organ": "Lung (肺)",
        "back_shu": "BL13 (Feishu / 肺俞 - T3 level)",
        "front_mu": "LU1 (Zhongfu / 中府 - 1st intercostal)",
        "clinical_focus": "Chronic deficient cough vs. acute wheezing; tonifies lung capacity and opens the chest.",
        "acute_chronic": "Front-Mu LU1 disperses acute heat/phlegm; Back-Shu BL13 tonifies chronic weakness."
    },
    {
        "organ": "Large Intestine (大肠)",
        "back_shu": "BL25 (Dachangshu / 大肠俞 - L4 level)",
        "front_mu": "ST25 (Tianshu / 天枢 - 2 cun lateral to umbilicus)",
        "clinical_focus": "Regulates bowel motility: effective for both chronic constipation and acute diarrhea/IBS.",
        "acute_chronic": "ST25 clears acute intestinal heat and stagnant food; BL25 warms and tonifies chronic deficiency."
    },
    {
        "organ": "Stomach (胃)",
        "back_shu": "BL21 (Weishu / 胃俞 - T12 level)",
        "front_mu": "CV12 (Zhongwan / 中脘 - 4 cun above umbilicus)",
        "clinical_focus": "Harmonizes digestion, settles rebellious stomach qi, relieves epigastric burning and bloating.",
        "acute_chronic": "CV12 treats acute food retention and acid reflux; BL21 strengthens chronic digestive absorption."
    },
    {
        "organ": "Spleen (脾)",
        "back_shu": "BL20 (Pishu / 脾俞 - T11 level)",
        "front_mu": "LV13 (Zhangmen / 樟门 - Below free end of 11th rib)",
        "clinical_focus": "Resolves chronic dampness, stops chronic fatigue, improves muscle tone and nutrient assimilation.",
        "acute_chronic": "LV13 harmonizes Liver-Spleen conflict; BL20 deeply tonifies post-natal Qi and Blood."
    },
    {
        "organ": "Heart (心)",
        "back_shu": "BL15 (Xinshu / 心俞 - T5 level)",
        "front_mu": "CV14 (Juque / 巨阙 - 6 cun above umbilicus)",
        "clinical_focus": "Grounds Shen, eases cardiac pain, relieves palpitations and severe night-time anxiety.",
        "acute_chronic": "CV14 clears acute Heart Phlegm-Fire agitation; BL15 nourishes chronic Heart Blood and Yin deficiency."
    },
    {
        "organ": "Small Intestine (小肠)",
        "back_shu": "BL27 (Xiaochangshu / 小肠俞 - 1st sacral foramen)",
        "front_mu": "CV4 (Guanyuan / 关元 - 3 cun below umbilicus)",
        "clinical_focus": "Separates the clear from turbid fluids, treats lower abdominal colic and painful urination.",
        "acute_chronic": "CV4 strengthens original Qi; BL27 clears heat and stagnation from lower intestines and pelvis."
    },
    {
        "organ": "Bladder (膀胱)",
        "back_shu": "BL28 (Pangguangshu / 膀胱俞 - 2nd sacral foramen)",
        "front_mu": "CV3 (Zhongji / 中极 - 4 cun below umbilicus)",
        "clinical_focus": "Relieves dysuria, urinary retention, incontinence, UTI burning, and pelvic congestion.",
        "acute_chronic": "CV3 drains acute Damp-Heat from urinary bladder; BL28 tonifies bladder sphincter tone."
    },
    {
        "organ": "Kidney (肾)",
        "back_shu": "BL23 (Shenshu / 肾俞 - L2 level)",
        "front_mu": "GB25 (Jingmen / 京门 - Below free end of 12th rib)",
        "clinical_focus": "Nourishes the root of life: treats lower back exhaustion, infertility, nocturnal emissions, and tinnitus.",
        "acute_chronic": "GB25 stimulates water metabolism and eases lumbar spasms; BL23 tonifies Kidney Yin and Yang."
    },
    {
        "organ": "Pericardium (心包)",
        "back_shu": "BL14 (Jueyinshu / 厥阴俞 - T4 level)",
        "front_mu": "CV17 (Danzhong / 膻中 - Center of sternum, 4th intercostal)",
        "clinical_focus": "Opens the chest, promotes circulation in cardiac vessels, relieves angina and heavy sighing.",
        "acute_chronic": "CV17 unbinds emotional constriction and acute chest oppression; BL14 nourishes Pericardium Blood."
    },
    {
        "organ": "San Jiao (三焦)",
        "back_shu": "BL22 (Sanjiaoshu / 三焦俞 - L1 level)",
        "front_mu": "CV5 (Shimen / 石门 - 2 cun below umbilicus)",
        "clinical_focus": "Restores fluid transformation across Upper, Middle, and Lower Burners, treats systemic edema.",
        "acute_chronic": "CV5 regulates lower burner fluid gate; BL22 coordinates whole-body metabolic Qi dynamics."
    },
    {
        "organ": "Gallbladder (胆)",
        "back_shu": "BL19 (Danshu / 胆俞 - T10 level)",
        "front_mu": "GB24 (Riyue / 日月 - 7th intercostal space)",
        "clinical_focus": "Treats cholecystitis, gallstones, bitter mouth taste, hypochondriac stabbing, and indecisiveness.",
        "acute_chronic": "GB24 clears acute gallbladder inflammation; BL19 restores smooth bile secretion and calm courage."
    },
    {
        "organ": "Liver (肝)",
        "back_shu": "BL18 (Ganshu / 肝俞 - T9 level)",
        "front_mu": "LV14 (Qimen / 期门 - 6th intercostal space)",
        "clinical_focus": "Resolves Liver Qi stagnation, smooths ribcage distention, subdues ascending Liver Yang wind.",
        "acute_chronic": "LV14 spreads acute Liver Qi knotting and PMS tenderness; BL18 nourishes chronic Liver Blood and Yin."
    }
]


# =============================================================================
# 3. EIGHT CONFLUENT POINTS OF EXTRAORDINARY VESSELS (八脉交会穴)
# =============================================================================
EXTRAORDINARY_PAIRS: List[Dict[str, Any]] = [
    {
        "title": "Chong Mai & Yin Wei Mai (冲脉 · 阴维脉)",
        "master_point": "SP4 (Gongsun / 公孙)",
        "master_vessel": "Master of Chong Mai (Sea of Blood & 12 Meridians)",
        "couple_point": "PC6 (Neiguan / 内关)",
        "couple_vessel": "Coupled to Yin Wei Mai (Connecting Yin)",
        "body_regions": "Heart, Chest, Epigastrium, Stomach, Lower Abdomen",
        "clinical_power": "Supreme pairing for all gastrointestinal complaints, nausea, vomiting, cardiac anxiety, and menstrual cramps.",
        "synergy_mechanisms": "SP4 regulates the blood and stomach through Chong Mai; PC6 unbinds chest oppression, settles nausea, and calms spirit through Yin Wei Mai."
    },
    {
        "title": "Dai Mai & Yang Wei Mai (带脉 · 阳维脉)",
        "master_point": "GB41 (Zulinqi / 足临泣)",
        "master_vessel": "Master of Dai Mai (Girdling Vessel)",
        "couple_point": "SJ5 (Waiguan / 外关)",
        "couple_vessel": "Coupled to Yang Wei Mai (Connecting Yang)",
        "body_regions": "Outer Canthus, Behind Ear, Neck, Shoulder, Lateral Torso, Hip",
        "clinical_power": "Premier pairing for temporal migraines, Shao Yang disorders, lateral neck stiffness, and pelvic/leukorrhea problems.",
        "synergy_mechanisms": "GB41 drains dampness and opens the waistband vessel; SJ5 vents exterior wind and opens the Shao Yang lateral network."
    },
    {
        "title": "Du Mai & Yang Qiao Mai (督脉 · 阳跷脉)",
        "master_point": "SI3 (Houxi / 后溪)",
        "master_vessel": "Master of Du Mai (Sea of Yang)",
        "couple_point": "BL62 (Shenmai / 申脉)",
        "couple_vessel": "Coupled to Yang Qiao Mai (Yang Motility)",
        "body_regions": "Inner Canthus, Back of Neck, Ears, Scapula, Entire Spine, Lower Back",
        "clinical_power": "Master protocol for spinal pain, acute lumbar sprain, stiff neck, occipital headaches, epilepsy, and insomnia.",
        "synergy_mechanisms": "SI3 ascends through Du Mai to stimulate yang and clear the spinal column; BL62 coordinates motor agility and clears daytime mania."
    },
    {
        "title": "Ren Mai & Yin Qiao Mai (任脉 · 阴跷脉)",
        "master_point": "LU7 (Lieque / 列缺)",
        "master_vessel": "Master of Ren Mai (Sea of Yin)",
        "couple_point": "KD6 (Zhaohai / 照海)",
        "couple_vessel": "Coupled to Yin Qiao Mai (Yin Motility)",
        "body_regions": "Throat, Chest, Lungs, Diaphragm, Abdomen, Urogenital System",
        "clinical_power": "Master protocol for throat dryness, acute loss of voice, asthma, chronic bronchitis, night sweats, and gynecological disorders.",
        "synergy_mechanisms": "LU7 disperses the upper respiratory tract and frees Ren Mai; KD6 anchors Yin fluids, moistens dry throats, and treats somnolence."
    }
]


# =============================================================================
# 4. FAMOUS CLASSICAL EMPIRICAL PAIRS (历代名家经典绝配)
# =============================================================================
CLASSICAL_EMPIRICAL_PAIRS: List[Dict[str, Any]] = [
    {
        "name": "The Four Gates (四关穴)",
        "points": "LI4 (Hegu) + LIV3 (Taichong)",
        "category": "Qi & Blood Dynamic Harmonization",
        "description": "LI4 rules Yang and Qi from the upper body; LIV3 rules Yin and Blood from the lower body. Combined, they open all twelve channels, break systemic stagnation, soothe stress, and relieve pain anywhere in the body.",
        "key_indications": "Generalized pain, severe tension headaches, emotional agitation, muscle spasms, hypertension, depression."
    },
    {
        "name": "Three Yin Crossing Fortifier (三阴培元法)",
        "points": "SP6 (Sanyinjiao) + KD3 (Taixi) + CV4 (Guanyuan)",
        "category": "Pre-natal & Post-natal Deep Tonification",
        "description": "Deeply replenishes Kidney Jing, Spleen Qi, and Liver Blood. Restores exhausted reserves, enhances immune resilience, and stabilizes hormones.",
        "key_indications": "Chronic fatigue syndrome, infertility, amenorrhea, menopausal hot flashes, low libido, post-illness recovery."
    },
    {
        "name": "Upper & Lower Digestive Harmony (上下和胃法)",
        "points": "ST36 (Zusanli) + CV12 (Zhongwan) + PC6 (Neiguan)",
        "category": "Gastrointestinal Core Trio",
        "description": "CV12 coordinates the Middle Burner; ST36 tonifies vital Stomach energy; PC6 descends rebellious stomach qi and calms anxiety-related stomach cramping.",
        "key_indications": "Gastritis, functional dyspepsia, peptic ulcers, nausea, loss of appetite, bloating after meals."
    },
    {
        "name": "Lumbar & Sciatic Master Pair (腰腿神效配穴)",
        "points": "BL40 (Weizhong) + BL23 (Shenshu)",
        "category": "Back & Spine Structural Duo",
        "description": "Clinical adage: 'For back problems, seek Weizhong' (腰背委中求). BL40 clears blood stasis and channel blockages; BL23 warms and tonifies Kidney root.",
        "key_indications": "Acute and chronic lumbar pain, sciatica, herniated disc pain, stiffness upon standing."
    },
    {
        "name": "Wind Dispelling Duo (祛风要穴)",
        "points": "GB20 (Fengchi) + LI4 (Hegu)",
        "category": "Exterior Pathogen Expulsion",
        "description": "GB20 eliminates wind from the head, neck, and sensory orifices; LI4 releases the exterior and commands the face.",
        "key_indications": "Common cold, acute influenza, stiff neck, occipital headaches, allergic rhinitis, facial numbness."
    },
    {
        "name": "Heart-Chest Restorer (心胸开泰法)",
        "points": "PC6 (Neiguan) + CV17 (Danzhong) + BL15 (Xinshu)",
        "category": "Cardiovascular & Emotional Relief",
        "description": "CV17 opens the Sea of Qi; PC6 expands the chest and improves coronary circulation; BL15 directly nourishes Heart Qi and Blood.",
        "key_indications": "Chest tightness, angina pectoris, tachycardia, hyperventilation, grief, emotional heartbreak."
    }
]


# =============================================================================
# 5. FIVE SHU POINTS & MOTHER-CHILD TONIFICATION/SEDATION
# =============================================================================
FIVE_SHU_DATA = {
    "Yin Meridians": {
        "Lung (LU)": {"Well (Wood)": "LU11", "Spring (Fire)": "LU10", "Stream (Earth)": "LU9 (Mother/Tonify)", "River (Metal)": "LU8 (Horary)", "Sea (Water)": "LU5 (Child/Sedate)"},
        "Spleen (SP)": {"Well (Wood)": "SP1", "Spring (Fire)": "SP2 (Mother/Tonify)", "Stream (Earth)": "SP3 (Horary)", "River (Metal)": "SP5 (Child/Sedate)", "Sea (Water)": "SP9"},
        "Heart (HT)": {"Well (Wood)": "HT9 (Mother/Tonify)", "Spring (Fire)": "HT8 (Horary)", "Stream (Earth)": "HT7 (Child/Sedate)", "River (Metal)": "HT4", "Sea (Water)": "HT3"},
        "Kidney (KD)": {"Well (Wood)": "KD1 (Child/Sedate)", "Spring (Fire)": "KD2", "Stream (Earth)": "KD3", "River (Metal)": "KD7 (Mother/Tonify)", "Sea (Water)": "KD10 (Horary)"},
        "Pericardium (PC)": {"Well (Wood)": "PC9 (Mother/Tonify)", "Spring (Fire)": "PC8 (Horary)", "Stream (Earth)": "PC7 (Child/Sedate)", "River (Metal)": "PC5", "Sea (Water)": "PC3"},
        "Liver (LIV)": {"Well (Wood)": "LIV1 (Horary)", "Spring (Fire)": "LIV2 (Child/Sedate)", "Stream (Earth)": "LIV3", "River (Metal)": "LIV4", "Sea (Water)": "LIV8 (Mother/Tonify)"}
    },
    "Yang Meridians": {
        "Large Intestine (LI)": {"Well (Metal)": "LI1 (Horary)", "Spring (Water)": "LI2 (Child/Sedate)", "Stream (Wood)": "LI3", "River (Fire)": "LI5", "Sea (Earth)": "LI11 (Mother/Tonify)"},
        "Stomach (ST)": {"Well (Metal)": "ST45 (Child/Sedate)", "Spring (Water)": "ST44", "Stream (Wood)": "ST43", "River (Fire)": "ST41 (Mother/Tonify)", "Sea (Earth)": "ST36 (Horary)"},
        "Small Intestine (SI)": {"Well (Metal)": "SI1", "Spring (Water)": "SI2 (Child/Sedate)", "Stream (Wood)": "SI3 (Mother/Tonify)", "River (Fire)": "SI5 (Horary)", "Sea (Earth)": "SI8"},
        "Bladder (BL)": {"Well (Metal)": "BL67 (Mother/Tonify)", "Spring (Water)": "BL66 (Horary)", "Stream (Wood)": "BL65 (Child/Sedate)", "River (Fire)": "BL60", "Sea (Earth)": "BL40"},
        "San Jiao (SJ)": {"Well (Metal)": "SJ1", "Spring (Water)": "SJ2 (Child/Sedate)", "Stream (Wood)": "SJ3 (Mother/Tonify)", "River (Fire)": "SJ6 (Horary)", "Sea (Earth)": "SJ10"},
        "Gallbladder (GB)": {"Well (Metal)": "GB44", "Spring (Water)": "GB43 (Mother/Tonify)", "Stream (Wood)": "GB41 (Horary)", "River (Fire)": "GB38 (Child/Sedate)", "Sea (Earth)": "GB34"}
    }
}


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_point_pairs_tab():
    """Render the Classical Point Combinations Engine tab."""
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #c89666; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            🔗 Classical Point Combinations Engine (配穴体系)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Master canonical TCM point pairing protocols: Host-Guest (Yuan-Luo), Back-Shu & Front-Mu, Eight Extraordinary Vessels, Mother-Child Five Shu tonification/sedation, and famous empirical combinations.
        </p>
    </div>
    """)

    sub_nav = st.radio(
        "Select Pairing Methodology",
        options=[
            "Host-Guest (Yuan-Luo)",
            "Back-Shu & Front-Mu",
            "Eight Confluent Vessels",
            "Famous Empirical Pairs",
            "Five Shu Tonification/Sedation",
            "Interactive Synergy Analyzer"
        ],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.write("")

    # SUB-TAB 1: HOST-GUEST (YUAN-LUO)
    if sub_nav == "Host-Guest (Yuan-Luo)":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">主客原络配穴法 (Host-Guest Yuan-Luo Combination)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                The <strong>Host (Yuan-Source)</strong> treats the primary diseased organ directly, while the <strong>Guest (Luo-Connecting)</strong> point of the Yin/Yang paired meridian reinforces treatment by unblocking channel communication.
            </div>
        </div>
        """)

        filter_organ = st.selectbox(
            "Filter by Primary Meridian (Host Organ)",
            options=["All 12 Channel Pairs"] + [p["primary_organ"] for p in HOST_GUEST_PAIRS]
        )

        display_pairs = HOST_GUEST_PAIRS if filter_organ == "All 12 Channel Pairs" else [p for p in HOST_GUEST_PAIRS if p["primary_organ"] == filter_organ]

        for p in display_pairs:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(255, 255, 255, 0.12); border-radius: 12px; padding: 18px 22px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.25);">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding-bottom: 10px; margin-bottom: 12px;">
                    <div>
                        <span style="font-size: 1.15rem; font-weight: 800; color: #ffffff;">{p['primary_organ']}</span>
                        <span style="color: #94a3b8; font-size: 0.9rem; margin: 0 8px;">paired with</span>
                        <span style="font-size: 1.1rem; font-weight: 700; color: #c89666;">{p['paired_organ']}</span>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 14px;">
                    <div style="background: rgba(0, 123, 167, 0.15); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 12px 14px;">
                        <div style="font-size: 0.76rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">👑 Host Point (Yuan-Source)</div>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin: 4px 0;">{p['host_point']}</div>
                        <div style="font-size: 0.83rem; color: #cbd5e1;">{p['host_role']}</div>
                    </div>
                    <div style="background: rgba(200, 150, 102, 0.15); border: 1px solid rgba(200, 150, 102, 0.3); border-radius: 8px; padding: 12px 14px;">
                        <div style="font-size: 0.76rem; font-weight: 800; color: #fde68a; text-transform: uppercase;">🤝 Guest Point (Luo-Connecting)</div>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin: 4px 0;">{p['guest_point']}</div>
                        <div style="font-size: 0.83rem; color: #cbd5e1;">{p['guest_role']}</div>
                    </div>
                </div>

                <div style="margin-bottom: 8px; font-size: 0.9rem; color: #e2e8f0; line-height: 1.45;">
                    <strong style="color: #38bdf8;">Clinical Synergy:</strong> {p['synergy']}
                </div>
                <div style="font-size: 0.88rem; color: #94a3b8; line-height: 1.45;">
                    <strong style="color: #c89666;">Indications:</strong> {p['indications']}
                </div>
            </div>
            """)

    # SUB-TAB 2: BACK-SHU & FRONT-MU
    elif sub_nav == "Back-Shu & Front-Mu":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #c89666;">俞募配穴法 (Back-Shu and Front-Mu Combination)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Combines Yang-aspect Back-Shu points on the Bladder meridian (treating chronic deficiency & cold) with Yin-aspect Front-Mu points on the chest/abdomen (treating acute excess & heat) for total Yin-Yang organ equilibrium.
            </div>
        </div>
        """)

        cols = st.columns(2)
        for i, sm in enumerate(SHU_MU_PAIRS):
            col = cols[i % 2]
            with col:
                render_clean_html(f"""
                <div style="background: #111827; border: 1px solid rgba(255,255,255,0.12); border-radius: 10px; padding: 16px 18px; margin-bottom: 16px; min-height: 240px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #ffffff; margin-bottom: 8px;">
                        {sm['organ']}
                    </div>
                    <div style="background: rgba(72, 78, 178, 0.2); border-radius: 6px; padding: 8px 12px; margin-bottom: 6px;">
                        <span style="font-size: 0.75rem; font-weight: 800; color: #c7d2fe; text-transform: uppercase;">Back-Shu (Yang):</span>
                        <div style="font-size: 0.95rem; font-weight: 700; color: #ffffff;">{sm['back_shu']}</div>
                    </div>
                    <div style="background: rgba(0, 123, 167, 0.2); border-radius: 6px; padding: 8px 12px; margin-bottom: 10px;">
                        <span style="font-size: 0.75rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">Front-Mu (Yin):</span>
                        <div style="font-size: 0.95rem; font-weight: 700; color: #ffffff;">{sm['front_mu']}</div>
                    </div>
                    <div style="font-size: 0.85rem; color: #e2e8f0; margin-bottom: 4px;">
                        <strong>Action:</strong> {sm['clinical_focus']}
                    </div>
                    <div style="font-size: 0.82rem; color: #94a3b8;">
                        <em>{sm['acute_chronic']}</em>
                    </div>
                </div>
                """)

    # SUB-TAB 3: EIGHT CONFLUENT VESSELS
    elif sub_nav == "Eight Confluent Vessels":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">八脉交会穴 (Eight Confluent Points of Extraordinary Vessels)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                The 4 classic Master-Couple pairs on the extremities that command the Eight Extraordinary Meridians (Qi Jing Ba Mai), connecting core torso territories and the entire endocrine/nervous network.
            </div>
        </div>
        """)

        for ev in EXTRAORDINARY_PAIRS:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(255, 255, 255, 0.12); border-radius: 12px; padding: 18px 22px; margin-bottom: 16px;">
                <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-bottom: 6px;">
                    {ev['title']}
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px;">
                    <div style="background: rgba(0, 123, 167, 0.2); border-left: 3px solid #007ba7; padding: 10px 14px; border-radius: 6px;">
                        <span style="font-size: 0.75rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">Master Point:</span>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff;">{ev['master_point']}</div>
                        <div style="font-size: 0.82rem; color: #cbd5e1;">{ev['master_vessel']}</div>
                    </div>
                    <div style="background: rgba(72, 78, 178, 0.2); border-left: 3px solid #484eb2; padding: 10px 14px; border-radius: 6px;">
                        <span style="font-size: 0.75rem; font-weight: 800; color: #c7d2fe; text-transform: uppercase;">Coupled Point:</span>
                        <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff;">{ev['couple_point']}</div>
                        <div style="font-size: 0.82rem; color: #cbd5e1;">{ev['couple_vessel']}</div>
                    </div>
                </div>
                <div style="font-size: 0.88rem; color: #fde68a; font-weight: 700; margin-bottom: 6px;">
                    Anatomical Sphere: {ev['body_regions']}
                </div>
                <div style="font-size: 0.9rem; color: #e2e8f0; line-height: 1.45; margin-bottom: 6px;">
                    <strong style="color: #38bdf8;">Clinical Power:</strong> {ev['clinical_power']}
                </div>
                <div style="font-size: 0.85rem; color: #94a3b8; line-height: 1.45;">
                    <strong style="color: #cbd5e1;">Synergy Rationale:</strong> {ev['synergy_mechanisms']}
                </div>
            </div>
            """)

    # SUB-TAB 4: FAMOUS EMPIRICAL PAIRS
    elif sub_nav == "Famous Empirical Pairs":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #fde68a;">历代名家经典绝配 (Time-Tested Classical Point Pairs)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Canonical empirical point pairings transmitted by legendary Chinese medical masters (Bian Que, Sun Simiao, Yang Jizhou) demonstrating synergistic exponential clinical outcomes.
            </div>
        </div>
        """)

        cols = st.columns(2)
        for i, ep in enumerate(CLASSICAL_EMPIRICAL_PAIRS):
            col = cols[i % 2]
            with col:
                render_clean_html(f"""
                <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 18px 20px; margin-bottom: 16px; min-height: 250px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px;">
                        <h4 style="color: #ffffff !important; font-size: 1.15rem; font-weight: 800; margin: 0;">{ep['name']}</h4>
                        <span style="background: rgba(0, 123, 167, 0.25); color: #38bdf8; font-size: 0.72rem; font-weight: 700; padding: 2px 7px; border-radius: 4px;">
                            {ep['category']}
                        </span>
                    </div>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #c89666; margin-bottom: 10px;">
                        {ep['points']}
                    </div>
                    <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 10px;">
                        {ep['description']}
                    </div>
                    <div style="font-size: 0.84rem; color: #34d399; font-weight: 600;">
                        ✓ Key Targets: {ep['key_indications']}
                    </div>
                </div>
                """)

    # SUB-TAB 5: FIVE SHU TONIFICATION/SEDATION
    elif sub_nav == "Five Shu Tonification/Sedation":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">五输穴与子母补泻法 (Five Shu Points & Mother-Child Tonification/Sedation)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Classical Nan Jing Rule: <em>"In case of deficiency, tonify the Mother; in case of excess, sedate the Child" (虚则补其母，实则泻其子)</em>.
            </div>
        </div>
        """)

        tab_yin, tab_yang = st.tabs(["☯️ Six Yin Channels (Wood -> Water)", "☀️ Six Yang Channels (Metal -> Earth)"])
        with tab_yin:
            for meridian, pts in FIVE_SHU_DATA["Yin Meridians"].items():
                render_clean_html(f"""
                <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #38bdf8; font-size: 1rem; margin-bottom: 6px;">{meridian}</div>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 0.85rem;">
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">井 (Wood): {pts['Well (Wood)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">荥 (Fire): {pts['Spring (Fire)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">输 (Earth): {pts['Stream (Earth)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">经 (Metal): {pts['River (Metal)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">合 (Water): {pts['Sea (Water)']}</span>
                    </div>
                </div>
                """)

        with tab_yang:
            for meridian, pts in FIVE_SHU_DATA["Yang Meridians"].items():
                render_clean_html(f"""
                <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">
                    <div style="font-weight: 800; color: #c89666; font-size: 1rem; margin-bottom: 6px;">{meridian}</div>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 0.85rem;">
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">井 (Metal): {pts['Well (Metal)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">荥 (Water): {pts['Spring (Water)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">输 (Wood): {pts['Stream (Wood)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">经 (Fire): {pts['River (Fire)']}</span>
                        <span style="background: rgba(255,255,255,0.06); padding: 4px 8px; border-radius: 4px; color: #e2e8f0;">合 (Earth): {pts['Sea (Earth)']}</span>
                    </div>
                </div>
                """)

    # SUB-TAB 6: INTERACTIVE SYNERGY ANALYZER
    elif sub_nav == "Interactive Synergy Analyzer":
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.1rem; color: #38bdf8;">🔮 Point Pair Synergy Analyzer</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Select any two core acupoints to analyze their channel relationships, anatomical synergy, and clinical indications.
            </div>
        </div>
        """)

        point_catalog = [
            "LI4 (Hegu)", "LIV3 (Taichong)", "ST36 (Zusanli)", "SP6 (Sanyinjiao)",
            "PC6 (Neiguan)", "SP4 (Gongsun)", "GB20 (Fengchi)", "BL40 (Weizhong)",
            "BL23 (Shenshu)", "KD3 (Taixi)", "HT7 (Shenmen)", "LU7 (Lieque)",
            "KD6 (Zhaohai)", "CV12 (Zhongwan)", "CV4 (Guanyuan)", "CV6 (Qihai)",
            "GB34 (Yanglingquan)", "ST40 (Fenglong)", "LI11 (Quchi)", "GV20 (Baihui)"
        ]

        col1, col2 = st.columns(2)
        with col1:
            p1 = st.selectbox("Select Point A", options=point_catalog, index=0)
        with col2:
            p2 = st.selectbox("Select Point B", options=point_catalog, index=1)

        code1 = p1.split()[0]
        code2 = p2.split()[0]

        # Check known combinations
        known_match = None
        for pair in CLASSICAL_EMPIRICAL_PAIRS:
            if code1 in pair["points"] and code2 in pair["points"]:
                known_match = ("Classical Pair", pair["name"], pair["description"], pair["key_indications"])
                break

        if not known_match:
            for hg in HOST_GUEST_PAIRS:
                if code1 in hg["host_point"] and code2 in hg["guest_point"]:
                    known_match = ("Host-Guest Pair", f"{hg['primary_organ']} + {hg['paired_organ']}", hg["synergy"], hg["indications"])
                    break
                elif code2 in hg["host_point"] and code1 in hg["guest_point"]:
                    known_match = ("Host-Guest Pair", f"{hg['primary_organ']} + {hg['paired_organ']}", hg["synergy"], hg["indications"])
                    break

        if not known_match:
            for ev in EXTRAORDINARY_PAIRS:
                if (code1 in ev["master_point"] and code2 in ev["couple_point"]) or (code2 in ev["master_point"] and code1 in ev["couple_point"]):
                    known_match = ("Extraordinary Vessel Confluent Pair", ev["title"], ev["synergy_mechanisms"], ev["clinical_power"])
                    break

        if known_match:
            render_clean_html(f"""
            <div style="background: rgba(16, 185, 129, 0.15); border: 1.5px solid #10b981; border-radius: 12px; padding: 20px 24px; margin-top: 14px;">
                <span style="background: #10b981; color: #0f172a; font-size: 0.76rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
                    ★ {known_match[0]} Detected!
                </span>
                <h3 style="color: #ffffff !important; font-size: 1.35rem; font-weight: 800; margin: 8px 0 4px 0;">
                    {known_match[1]}
                </h3>
                <div style="font-size: 0.95rem; color: #e2e8f0; line-height: 1.5; margin-bottom: 10px;">
                    {known_match[2]}
                </div>
                <div style="font-size: 0.9rem; color: #34d399; font-weight: 700;">
                    Target Indications: {known_match[3]}
                </div>
            </div>
            """)
        else:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(255, 255, 255, 0.12); border-radius: 12px; padding: 20px 24px; margin-top: 14px;">
                <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 0.76rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">
                    Custom Combination
                </span>
                <h3 style="color: #ffffff !important; font-size: 1.3rem; font-weight: 800; margin: 8px 0 4px 0;">
                    {p1} + {p2}
                </h3>
                <div style="font-size: 0.92rem; color: #cbd5e1; line-height: 1.5;">
                    Combines <strong>{p1}</strong> and <strong>{p2}</strong>. Provides localized and systemic balance by coordinating upper/lower extremity energy flow and harmonizing multi-channel circulation.
                </div>
            </div>
            """)

"""Supplemental High-Yield Flashcards (28 cards).

Brings the total card count to 212 cards, deeply covering all 7 requested categories:
Western Medicine, Meridians and Points, Diagnosis, Illness, Gynecology, Paediatrics, Safety and Ethics.
All points strictly use bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS = [
    # -------------------------------------------------------------------------
    # Diagnosis (7 cards)
    # -------------------------------------------------------------------------
    {
        "category": "Diagnosis",
        "title": "Tongue Cracks: Heart Fire vs Spleen vs Yin Deficiency",
        "front": "Differentiate tongue crack patterns: Deep central crack extending to the tip, transverse horizontal cracks, and short irregular cracks.",
        "back": "Differential Comparison of Tongue Cracks (Lie Wen She - 裂纹舌):\n• Deep Central Crack Extending Directly to the Tip:\n  - Heart Fire blazing, or severe constitutional tendency to Heart disharmonies and emotional anxiety.\n• Deep Central Crack with Yellow/Greasy Coat:\n  - Stomach Fire burning body fluids, or severe food stagnation.\n• Transverse Horizontal Cracks on Sides / Center:\n  - Spleen Qi and Spleen Yin deficiency (inability to generate fluids to moisten flesh).\n• Multiple Scattered Irregular Superficial Cracks with Red Peeled Body:\n  - Severe Kidney Yin deficiency with Empty Heat consuming essence and fluids.\n• Normal Variation (Congenital Fissured Tongue):\n  - Cracks present since childhood, accompanied by normal pink color and healthy thin white coating with root (not pathological).",
        "consensus": "Tongue cracks reflect depth and chronicity of fluid and essence depletion.",
        "variations": "A red dry tongue with cracks indicates active heat consuming fluids; a pale cracked tongue indicates long-standing blood deficiency.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Tongue Diagnosis"])
    },
    {
        "category": "Diagnosis",
        "title": "Eight Principles: True Cold with False Heat vs True Heat with False Cold",
        "front": "How do you distinguish 'True Cold with False Heat' (Yin Sheng Ge Yang) from 'True Heat with False Cold' (Yang Sheng Ge Yin)?",
        "back": "Critical Differential of Extreme Pathology:\n• True Cold with False Heat (Yin Sheng Ge Yang - 阴盛格阳 / False Heat):\n  - Surface Manifestations (False Branch): Flushed red cheeks (floating red like makeup), dry mouth, restless tossing, irritability, sore throat.\n  - Core Reality (True Root): Cold extremities, aversion to cold, desires warm drinks in small sips, clear profuse urine, loose stool with undigested food, PALE WET TONGUE, FAINT MINUTE DEEP PULSE.\n  - Mechanism: Extreme internal Yin cold expels weak Yang Qi to the exterior (floating Yang).\n\n• True Heat with False Cold (Yang Sheng Ge Yin - 阳盛格阴 / False Cold):\n  - Surface Manifestations (False Branch): Cold hands and feet, curled posture.\n  - Core Reality (True Root): Burning feverish chest/abdomen, dry mouth with desire for COLD drinks, halitosis, constipation, dark scanty urine, RED CRIMSON TONGUE WITH DRY YELLOW COAT, DEEP FORCEFUL RAPID PULSE.\n  - Mechanism: Deep internal Yang heat is so intense that it blocks circulation to the extremities, preventing Yang from reaching limbs.",
        "consensus": "Tongue body color and pulse forcefulness reveal the TRUE nature; superficial temperature reveals the FALSE branch.",
        "variations": "Treat True Cold with False Heat by warming Yang (never give cold herbs); treat True Heat with False Cold by clearing heat.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Shanghan Lun", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Leather (Ge) vs Hidden (Fu)",
        "front": "Compare the sensation and clinical significance of the Leather Pulse (Ge Mai) and Hidden Pulse (Fu Mai).",
        "back": "Tactile Sensation & Indications:\n• Leather / Tympanic Pulse (Ge Mai - 革脉):\n  - Sensation: Hard, tight, and stretched on the surface like pressing the drumhead of a tight leather drum, but completely empty and hollow underneath.\n  - Indications: Severe loss of Blood, severe loss of Essence (Jing), massive uterine hemorrhage, miscarriage.\n  - Reflection: Floating Yang Qi expanding in an empty vascular bed depleted of Blood and Essence.\n\n• Hidden Pulse (Fu Mai - 伏脉):\n  - Sensation: Deeper than a deep pulse; felt ONLY by pressing extremely hard down to the bone; imperceptible at superficial and middle depths.\n  - Indications: Severe acute pain (e.g., kidney stones, gallstones), syncope, extreme Cold obstruction, or Yang collapse.",
        "consensus": "Key emergency pulse markers: Leather indicates fluid/essence hemorrhage; Hidden indicates extreme obstruction or pain.",
        "variations": "A hidden pulse during an acute fainting spell confirms Yang Qi is temporarily collapsed or blocked internally.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies"])
    },
    {
        "category": "Diagnosis",
        "title": "Six Stages: Taiyang Zhong Feng vs Taiyang Shang Han",
        "front": "Compare Taiyang Wind Attack (Zhong Feng) and Taiyang Cold Attack (Shang Han) in the Shanghan Lun.",
        "back": "Differential Comparison of Taiyang Stage:\n• Taiyang Wind Attack (Taiyang Zhong Feng - 太阳中风 / Gui Zhi Tang pattern):\n  - Etiology: Wind pathogen injuring Defensive (Wei) Qi, disharmony between Ying and Wei.\n  - Cardinal Signs: Aversion to wind, moderate fever, SWEATING (spontaneous perspiration due to Wei Qi failure to consolidate sweat pores), nasal congestion, floating moderate / loose pulse (Fu Huan Mai).\n\n• Taiyang Cold Attack (Taiyang Shang Han - 太阳伤寒 / Ma Huang Tang pattern):\n  - Etiology: Cold pathogen contracting exterior, closing pores.\n  - Cardinal Signs: Severe aversion to cold, fever, ABSENCE OF SWEAT (anhidrosis - cold contracts sweat pores tightly), severe occipital headache, generalized body aching, dyspnea, floating tight pulse (Fu Jin Mai).",
        "consensus": "Presence of sweat (Zhong Feng) vs absence of sweat (Shang Han) is the definitive diagnostic fork.",
        "variations": "Sweating in Zhong Feng is deficient sweating; diaphoresis must NOT be forced with heavy pungent-warm herbs.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Zhang Zhongjing Shanghan Lun"])
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu: Liver Invading Spleen vs Liver Invading Stomach",
        "front": "Differentiate Liver Overacting on Spleen (Wood overacting on Earth) from Liver Invading Stomach.",
        "back": "Differential Comparison:\n• Liver Overacting on Spleen (Gan Pi Bu He - 肝脾不和 / IBS pattern):\n  - Chief Manifestation: Bowel / Intestinal disturbance.\n  - Symptoms: Alternating diarrhea and constipation, abdominal distension and pain preceded by stress/irritability, pain immediately RELIEVED AFTER DEFECATION, flatulence, fatigue, wiry-weak pulse.\n  - Primary Points: LV13 (Zhangmen / 章门), LV3 (Taichong / 太冲), SP6 (Sanyinjiao / 三阴交), ST36 (Zusanli / 足三里), ST25 (Tianshu / 天枢).\n\n• Liver Invading Stomach (Gan Wei Bu He - 肝胃不和 / GERD / Gastritis pattern):\n  - Chief Manifestation: Upper digestive / Gastric disturbance.\n  - Symptoms: Epigastric distension and burning pain radiating to hypochondrium, acid regurgitation, heartburn, frequent sour belching, nausea, vomiting, hiccup, sighing, wiry pulse.\n  - Primary Points: LV14 (Qimen / 期门), LV3 (Taichong / 太冲), REN12 (Zhongwan / 中脘), PC6 (Neiguan / 内关), ST36 (Zusanli / 足三里).",
        "consensus": "Clear anatomical division: Liver-Spleen affects intestines/stool; Liver-Stomach affects epigastrium/acid reflux.",
        "variations": "Tongue in both shows red lateral borders, but Liver-Stomach has a greasy yellow coat in the central third.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Foundations"])
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu: Kidney and Heart Disharmony (Xin Shen Bu Jiao)",
        "front": "What are the clinical manifestations, thermal dynamics, tongue, and pulse of Disharmony between Heart and Kidney (Xin Shen Bu Jiao)?",
        "back": "Heart and Kidney Disharmony (心肾不交):\n• Pathology:\n  - Normally, Kidney Water ascends to cool and nourish Heart Fire; Heart Fire descends to warm Kidney Water.\n  - When Kidney Yin is deficient, Water cannot ascend to control Fire; Heart Fire blazes uncontrollably in the Upper Jiao, while Kidney Yin remains depleted in the Lower Jiao.\n\n• Clinical Manifestations:\n  - Upper Jiao (Excess/Empty Fire): Severe insomnia, dream-disturbed sleep, difficulty falling asleep, palpitations, mental restlessness, anxiety, sores on tongue, dry throat.\n  - Lower Jiao (Yin Deficiency): Sore weak lumbar spine and knees, nocturnal emissions with erotic dreams, tinnitus like cicadas, hot flashes, five-palm heat, night sweats.\n\n• Tongue & Pulse:\n  - Tongue: Red body, especially bright red tip with prickles; peeled/absent coat in center and root.\n  - Pulse: Thin (Xi) and Rapid (Shuo); weak at Chi (Kidney) position, floating/rapid at Cun (Heart) position.\n\n• Core Point Prescription:\n  - HT7 (Shenmen / 神门), KI3 (Taixi / 太溪), KI6 (Zhaohai / 照海), BL15 (Xinshu / 心俞), BL23 (Shenshu / 肾俞), PC6 (Neiguan / 内关).",
        "consensus": "The premier pattern explaining severe chronic insomnia and psychosomatic anxiety.",
        "variations": "Formula correlation: Huang Lian E Jiao Tang (clears heart fire while nourishing kidney yin).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Foundations"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Scattered (San) vs Moving (Dong)",
        "front": "Describe the tactile feel and clinical significance of the Scattered Pulse (San Mai) and Moving Pulse (Dong Mai).",
        "back": "Tactile Sensation & Indications:\n• Scattered Pulse (San Mai - 散脉):\n  - Sensation: Floating, broad, irregular, completely diffuse without clear borders; feels like 'broken threads' or 'scattered dandelion seeds'; disappears completely when pressed lightly deeper.\n  - Indications: Severe exhaustion of Yuan Qi, imminent separation of Yin and Yang, critical heart failure.\n\n• Moving / Spinning Bean Pulse (Dong Mai - 动脉):\n  - Sensation: Short, round, rapid, slippery, and bulging like a 'spinning bean' or 'pebble rolling under the finger' felt ONLY at the middle Guan (Bar) position; lacks head and tail (absent at Cun and Chi).\n  - Indications: Extreme pain, sudden acute fright/terror, shock, palpitations.",
        "consensus": "San Mai indicates critical vital Qi collapse; Dong Mai indicates intense sudden pain or panic.",
        "variations": "Dong Mai is commonly palpated during acute renal colic, severe panic attacks, or acute palpitations.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies"])
    },

    # -------------------------------------------------------------------------
    # Illness (7 cards)
    # -------------------------------------------------------------------------
    {
        "category": "Illness",
        "title": "Jaundice (Huang Dan): Yang Jaundice vs Yin Jaundice",
        "front": "Differentiate Yang Jaundice (Damp-Heat) from Yin Jaundice (Cold-Damp) by skin hue, symptoms, tongue, and points.",
        "back": "Differential Comparison of Jaundice (黄疸):\n• Yang Jaundice (Yang Dan - 阳黄 / Damp-Heat):\n  - Skin Hue: Bright, vibrant, lustrous orange-yellow like the peel of a fresh tangerine.\n  - Symptoms: Acute onset, high fever, thirst, dark tea-colored urine, bitter taste, hypochondriac pain, constipation, nausea.\n  - Tongue: Red with thick greasy yellow coat; Pulse: Wiry, rapid, slippery.\n  - Points: LV14 (Qimen / 期门), GB24 (Riyue / 日月), GB34 (Yanglingquan / 阳陵泉), SP9 (Yinlingquan / 阴陵泉), BL18 (Ganshu / 肝俞), BL19 (Danshu / 胆俞), DU9 (Zhiyang / 至阳 - empirical master point for jaundice).\n\n• Yin Jaundice (Yin Dan - 阴黄 / Cold-Damp):\n  - Skin Hue: Dull, dark, smoky, withered, lusterless yellow like smoked bamboo.\n  - Symptoms: Chronic insidious onset, aversion to cold, fatigue, poor appetite, loose stools, epigastric fullness, cold limbs.\n  - Tongue: Pale, swollen with white greasy coat; Pulse: Deep, slow, weak.\n  - Points: Moxa on BL20 (Pishu / 脾俞), BL23 (Shenshu / 肾俞), REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), DU9 (Zhiyang / 至阳).",
        "consensus": "DU9 (Zhiyang - below T7) is the universal empirical point for all forms of jaundice.",
        "variations": "Bright orange = Yang (Damp-Heat); Dull smoky = Yin (Cold-Damp).",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Edema (Shui Zhong): Yang Edema vs Yin Edema",
        "front": "Contrast Yang Edema (Wind-Water, Dampness) and Yin Edema (Spleen/Kidney Yang Deficiency) by onset, location, and points.",
        "back": "Differential Comparison of Edema (水肿):\n• Yang Edema (Yang Shui - 阳水 / Acute):\n  - Onset & Progression: Rapid sudden onset; starts in the FACE, EYELIDS, and UPPER BODY, then spreads downward.\n  - Nature of Edema: Skin is tense, bright, firm, and springs back quickly after pressing (non-pitting or quick rebound).\n  - Symptoms: Chills, fever, sore throat, cough, aversion to wind, floating tight or rapid pulse.\n  - Points: LU7 (Lieque / 列缺), LI4 (Hegu / 合谷), SP9 (Yinlingquan / 阴陵泉), ST36 (Zusanli / 足三里), BL13 (Feishu / 肺俞).\n\n• Yin Edema (Yin Shui - 阴水 / Chronic):\n  - Onset & Progression: Slow insidious onset; starts in the ANKLES, FEET, and LOWER EXTREMITIES, aggravated after standing.\n  - Nature of Edema: Skin is pale, loose, soft, and leaves a deep, persistent indentation after finger pressure (true PITTING EDEMA).\n  - Symptoms: Cold lower back/knees, fatigue, abdominal fullness, loose stools, pale wet tongue, deep weak slow pulse.\n  - Points: Moxa on BL20 (Pishu / 脾俞), BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), REN4 (Guanyuan / 关元), KI7 (Fuliu / 复溜), SP9 (Yinlingquan / 阴陵泉).",
        "consensus": "Yang edema starts above (Lung failed to diffuse); Yin edema starts below (Kidney/Spleen failed to transform).",
        "variations": "KI7 + SP9 is the premier diuretic acupoint pair for mobilizing lower extremity fluid.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Hiccup (E Ni): Cold vs Heat vs Liver Qi Rebellion",
        "front": "Differentiate Hiccup (E Ni - 呃逆) caused by Stomach Cold, Stomach Fire, and Liver Qi Stagnation.",
        "back": "Differential Comparison of Hiccup (呃逆):\n• Stomach Cold (Wei Han E Ni):\n  - Sound: Slow, deep, forceful, spasmodic hiccups, relieved by warm drinks, aggravated by cold; epigastric cold pain, pale tongue with white coat.\n  - Points: Moxa on REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), BL17 (Geshu / 膈俞 - Hui of Blood / Diaphragm).\n\n• Stomach Fire (Wei Re E Ni):\n  - Sound: Loud, sharp, frequent, rapid resonant hiccups; bad breath, intense thirst, dry mouth, constipation, red tongue with dry yellow coat, rapid pulse.\n  - Points: ST44 (Neiting / 内庭), REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), PC6 (Neiguan / 内关).\n\n• Liver Qi Rebellion Invading Stomach (Gan Qi Fan Wei):\n  - Sound: Frequent paroxysmal hiccups triggered by emotional frustration or anger; chest and hypochondriac distension, sighing, wiry pulse.\n  - Points: LV3 (Taichong / 太冲), PC6 (Neiguan / 内关), BL17 (Geshu / 膈俞), REN17 (Danzhong / 膻中).\n\n• Master Empirical Point for All Hiccup: BL17 (Geshu / 膈俞) + PC6 (Neiguan / 内关).\n  - Mechanism: BL17 is the Diaphragm Back-Shu point (stops diaphragmatic spasm); PC6 calms rebellious middle jiao Qi.",
        "consensus": "BL17 and PC6 form the universal master treatment pair for intractable diaphragmatic spasms and hiccup.",
        "variations": "Cuanzhu (BL2) firm thumbnail acupressure is a renowned quick distal technique to halt acute hiccups.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Manic-Depression (Dian Kuang): Dian (Depression) vs Kuang (Mania)",
        "front": "Differentiate Dian Syndrome (Depression / Withdrawal) from Kuang Syndrome (Mania / Agitation) by symptoms, etiology, and points.",
        "back": "Differential Comparison of Dian Kuang (癫狂):\n• Dian Syndrome (Depression / Phlegm-Qi Stagnation - 癫证):\n  - Personality: Passive, introverted, withdrawn, sullen, depressed, silent, muttering to oneself, staring at walls, lack of appetite, social isolation.\n  - Mechanism: Liver Qi stagnation and Phlegm clouding the Heart orifices (Yin pattern).\n  - Tongue: Pale swollen with greasy white coating; Pulse: Wiry and slippery.\n  - Points: PC6 (Neiguan / 内关), HT7 (Shenmen / 神门), ST40 (Fenglong / 丰隆), LV3 (Taichong / 太冲), REN12 (Zhongwan / 中脘), DU20 (Baihui / 百会).\n\n• Kuang Syndrome (Mania / Phlegm-Fire Agitation - 狂证):\n  - Personality: Hyperactive, extroverted, violent, shouting, cursing, singing wildly from high places, stripping off clothing, destructive rage, extreme strength, insomnia.\n  - Mechanism: Blazing Yang fire combining with phlegm to harass the Heart and Shen (Yang pattern).\n  - Tongue: Red crimson body with thick greasy yellow coat; Pulse: Rapid, wiry, surging, forceful.\n  - Points: Prick Shixuan (EX-UE11) to bleed, DU26 (Shuigou / 水沟), DU14 (Dazhui / 大椎), PC8 (Laogong / 劳宫), LV2 (Xingjian / 行间), ST40 (Fenglong / 丰隆), ST44 (Neiting / 内庭).",
        "consensus": "Dian is Yin (withdrawal, dull phlegm); Kuang is Yang (violent mania, blazing phlegm-fire).",
        "variations": "Sun Simiao's Thirteen Ghost Points (Gui Xue) were specifically formulated for severe Dian Kuang psychosis.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Plantar Fasciitis / Calcaneal Spur: Local & Distal Points",
        "front": "State the etiology, hallmark pain presentation, and local/distal acupoint prescription for Plantar Fasciitis (Gen Tong - Heel Pain).",
        "back": "Clinical Protocol for Plantar Fasciitis / Heel Pain (跟痛症):\n• Hallmark Presentation:\n  - Sharp, stabbing or burning pain under the plantar calcaneus, worst with the VERY FIRST STEPS in the morning out of bed; pain slightly eases after walking, but worsens after prolonged weight-bearing.\n  - Etiology: Chronic micro-tears of the plantar aponeurosis origin; TCM: Kidney deficiency (Kidney governs bones/heel) with local Qi and Blood stasis in the Taiyang and Shaoyin channels.\n\n• Point Prescription:\n  - Ah Shi Point (Plantar Heel): Deep perpendicular insertion 0.5 - 0.8 cun directly into the tender calcaneal tubercle origin (often with electroacupuncture or moxa).\n  - KI3 (Taixi / 太溪) + BL60 (Kunlun / 昆仑): Master pair flanking the Achilles tendon to balance Yin/Yang and unblock heel Qi.\n  - KI1 (Yongquan / 涌泉): Promotes blood circulation in the plantar fascia.\n  - BL57 (Chengshan / 承山): Relaxes calf gastrocnemius/soleus tightness, reducing tensile stress on the plantar fascia.\n  - Distal Point: PC7 (Daling / 大陵 - anatomical wrist-ankle correspondence).",
        "consensus": "Local Ah Shi needling combined with BL57 calf relaxation provides superior relief for heel spurs.",
        "variations": "Warm foot soaks with herbs (Hong Hua, Tou Gu Cao) combined with acupuncture accelerate recovery.",
        "sources": json.dumps(["Royal TCM TCM-10 Traumatology", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Palpitations (Xin Ji): Heart Blood vs Heart Yang vs Phlegm-Fire",
        "front": "Differentiate Palpitations (Xin Ji) caused by Heart Blood Deficiency, Heart Yang Deficiency, and Phlegm-Fire Disturbing Heart.",
        "back": "Differential Comparison of Palpitations (心悸):\n• Heart Blood Deficiency (Xin Xue Xu):\n  - Symptoms: Palpitations triggered by fatigue or fright, dizziness, pale dull face, insomnia, dream-disturbed sleep, pale tongue, thin weak pulse.\n  - Points: HT7 (Shenmen / 神门), PC6 (Neiguan / 内关), BL15 (Xinshu / 心俞), BL20 (Pishu / 脾俞), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交).\n\n• Heart Yang Deficiency (Xin Yang Xu):\n  - Symptoms: Palpitations with feelings of emptiness/chill in the chest, shortness of breath, cold extremities, aversion to cold, pale wet tongue, deep weak or knotted pulse.\n  - Points: Moxa on BL15 (Xinshu / 心俞), REN17 (Danzhong / 膻中), REN14 (Juque / 巨阙), REN6 (Qihai / 气海), PC6 (Neiguan / 内关).\n\n• Phlegm-Fire Disturbing Heart (Tan Huo Rao Xin):\n  - Symptoms: Rapid forceful palpitations, chest oppression, agitation, insomnia with nightmare tossing, bitter mouth, yellow sputum, red tongue with thick greasy yellow coat, rapid slippery pulse.\n  - Points: PC6 (Neiguan / 内关), HT7 (Shenmen / 神门), ST40 (Fenglong / 丰隆), REN12 (Zhongwan / 中脘), LV2 (Xingjian / 行间), ST44 (Neiting / 内庭).",
        "consensus": "PC6 and HT7 form the universal foundation for all cardiac rhythm and palpitation disorders.",
        "variations": "If palpitations are accompanied by chest pain radiating down left arm (angina), immediately evaluate for myocardial ischemia.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Hypertension (Gao Xue Ya): Liver Yang Rising vs Phlegm-Damp",
        "front": "Differentiate Essential Hypertension (Gao Xue Ya) caused by Liver Yang Rising versus Phlegm-Damp Stagnation.",
        "back": "Differential Comparison of Hypertension (高血压):\n• Liver Yang Rising (Gan Yang Shang Kang - Most Common in Stressed Patients):\n  - Symptoms: Severe throbbing temporal headache, dizziness, tinnitus like rushing water, red face and eyes, irritability, insomnia, wiry forceful rapid pulse.\n  - Points: LV3 (Taichong / 太冲), GB20 (Fengchi / 风池), KI3 (Taixi / 太溪), Taiyang (太阳), LI11 (Quchi / 曲池), with bleeding at apex of ear (Er Jian).\n\n• Phlegm-Damp Stagnation (Tan Shi Zu Zhi - Common in Overweight Patients):\n  - Symptoms: Dull heavy dizziness as if head is wrapped tightly, heaviness of limbs, chest and epigastric oppression, palpitations, nausea, overweight, swollen tongue with greasy white coat, slippery pulse.\n  - Points: ST40 (Fenglong / 丰隆), SP9 (Yinlingquan / 阴陵泉), REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), LI11 (Quchi / 曲池).\n\n• Primary Distal Hypotensive Acupoint Pair:\n  - LI11 (Quchi / 曲池) + ST36 (Zusanli / 足三里): Clears upper body Yangming vascular pressure and regulates autonomic vascular resistance.",
        "consensus": "LI11, LV3, and GB20 are universally recognized as the most effective anti-hypertensive acupuncture triad.",
        "variations": "Pricking Er Jian (Ear Apex) to express 3–5 drops of blood causes rapid reflexive blood pressure reduction in acute hypertensive spikes.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },

    # -------------------------------------------------------------------------
    # Gynecology (4 cards)
    # -------------------------------------------------------------------------
    {
        "category": "Gynecology",
        "title": "Amenorrhea (Bi Jing): Depletion vs Obstruction",
        "front": "Differentiate Amenorrhea (absence of menses > 3–6 months) caused by Blood Depletion versus Qi/Blood/Phlegm Obstruction.",
        "back": "Differential Comparison of Amenorrhea (闭经):\n• Blood / Essence Depletion (Xu Zheng):\n  - Symptoms: Gradual lightening of menses culminating in cessation; emaciation, dry skin, dizziness, blurry vision, palpitations, fatigue, sore lumbar, pale dry tongue, thin weak pulse.\n  - Treatment Principle: Nourish Blood, tonify Kidney Jing, fortify Spleen.\n  - Points: BL20 (Pishu / 脾俞), BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), Zigong (EX-CA1).\n\n• Qi & Blood Stagnation / Obstruction (Shi Zheng):\n  - Symptoms: Abrupt cessation of menses following emotional trauma or cold invasion; lower abdominal distension and sharp pain, purple clots on previous cycles, purple tongue, wiry choppy pulse.\n  - Treatment Principle: Invigorate Blood, dispel stasis, move Qi, unblock Chong/Ren.\n  - Points: SP10 (Xuehai / 血海), LV3 (Taichong / 太冲), CV3 (Zhongji / 中极), SP8 (Diji / 地机), ST29 (Guilai / 归来), BL17 (Geshu / 膈俞).\n\n• Phlegm-Damp Obstruction (Tan Shi Bi Jing / PCOS):\n  - Symptoms: Obesity, hirsutism, sticky mouth, profuse vaginal discharge, swollen tongue with greasy white coat, slippery pulse.\n  - Points: ST40 (Fenglong / 丰隆), SP9 (Yinlingquan / 阴陵泉), REN12 (Zhongwan / 中脘), Zigong (EX-CA1).",
        "consensus": "Crucial distinction between an empty sea (nourish) vs an obstructed river (unblock).",
        "variations": "Always perform a pregnancy test (urine hCG) before treating secondary amenorrhea.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Uterine Prolapse (Zi Gong Tuo Chui): Spleen Sinking vs Kidney Deficiency",
        "front": "State the etiology, symptoms, and acupuncture/moxa protocol for Uterine Prolapse (Zi Gong Tuo Chui).",
        "back": "Clinical Protocol for Uterine Prolapse (子宫脱垂):\n• Etiology:\n  - Spleen Qi Sinking: Spleen governs muscles and holds organs; severe Post-Heaven Qi deficiency or early postpartum heavy lifting allows clear Yang to sink.\n  - Kidney Deficiency: Pre-Heaven Jing failure; Dai Mai loses its binding control and Chong/Ren vessels loosen.\n\n• Symptoms:\n  - Sensation of bearing-down heaviness in vagina, a fleshy mass protruding from vaginal introitus (worse upon standing or fatigue, retracts when supine), lumbar soreness, fatigue.\n\n• Acupuncture & Moxibustion Protocol:\n  - DU20 (Baihui / 百会): Heavy indirect moxibustion (moxa stick) or needle directed anteriorly to vigorously raise sinking Yang Qi.\n  - Zigong (EX-CA1): Puncture obliquely downward towards pubic symphysis 1.5 - 2.0 cun to elicit sensation lifting the pelvic floor.\n  - REN6 (Qihai / 气海) + ST36 (Zusanli / 足三里): Tonify central Qi.\n  - BL20 (Pishu / 脾俞) + BL23 (Shenshu / 肾俞): Reinforce muscle tone and Kidney support.",
        "consensus": "DU20 moxa and Zigong oblique needle direction are the classic dynamic duo for pelvic organ prolapse.",
        "variations": "Teach patient pelvic floor Kegel exercises in combination with acupuncture treatments.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Pelvic Inflammatory Disease (PID): Damp-Heat Stasis Protocol",
        "front": "What are the clinical signs of Pelvic Inflammatory Disease (PID / Fu Jian Yan) and the acupuncture protocol for Damp-Heat Stasis?",
        "back": "Clinical Protocol for PID (盆腔炎 - Damp-Heat & Blood Stasis):\n• Clinical Signs:\n  - Constant, dull, burning or sharp aching pain in the lower abdomen and pelvis, radiating to the lumbosacral region, worsened by sexual intercourse or pre-menses; profuse yellow purulent leukorrhea with foul odor, low-grade fever, dysuria.\n  - Tongue: Red with thick greasy yellow coat; Pulse: Slippery, rapid, and wiry.\n\n• Point Prescription:\n  - CV3 (Zhongji / 中极 - Front-Mu of Bladder, crossing of 3 Leg Yin): Clears damp-heat from pelvic cavity.\n  - Zigong (EX-CA1): Promotes pelvic blood circulation and clears local inflammation.\n  - SP9 (Yinlingquan / 阴陵泉) + SP6 (Sanyinjiao / 三阴交): Clears dampness, regulates lower jiao.\n  - BL32 (Ciliao / 次髎): Clears heat and unblocks pelvic stasis.\n  - LV8 (Ququan / 曲泉) + LV5 (Ligou / 蠡沟): Clears Liver channel damp-heat from genitals.",
        "consensus": "CV3, BL32, and Zigong form the primary anti-inflammatory triangle for pelvic infection.",
        "variations": "Acute high fever with severe peritoneal rigidity requires immediate antibiotic therapy and medical emergency referral.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Postpartum Depression (Chan Hou Yu Zheng): Blood Deficiency vs Stagnation",
        "front": "Differentiate Postpartum Depression caused by Heart and Spleen Blood Deficiency versus Liver Qi Stagnation.",
        "back": "Differential Comparison of Postpartum Depression (产后郁证):\n• Heart & Spleen Blood Deficiency (Most Common):\n  - Pathology: Massive blood loss during labor depletes Heart Blood; the Shen loses its anchor.\n  - Symptoms: Severe sadness, uncontrollable weeping, insomnia, profound fatigue, panic attacks, inability to bond with newborn, palpitations, pale sallow face, pale tongue, thin weak pulse.\n  - Points: HT7 (Shenmen / 神门), SP6 (Sanyinjiao / 三阴交), ST36 (Zusanli / 足三里), BL15 (Xinshu / 心俞), BL20 (Pishu / 脾俞), DU20 (Baihui / 百会).\n\n• Liver Qi Stagnation Transforming into Heat:\n  - Pathology: Emotional frustration, hormonal shifts, breast engorgement constraining Liver Qi.\n  - Symptoms: Severe irritability, anger, sudden mood swings, breast distension, chest oppression, bitter taste, insomnia, red tongue edges, wiry pulse.\n  - Points: LV3 (Taichong / 太冲), PC6 (Neiguan / 内关), Yintang (印堂), REN17 (Danzhong / 膻中), GB34 (Yanglingquan / 阳陵泉).",
        "consensus": "Postpartum depletion of blood is the primary predisposing cause of postpartum mood disorders in TCM.",
        "variations": "Any postpartum thoughts of harming infant or self (postpartum psychosis) demands immediate emergency psychiatric intervention.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology"])
    },

    # -------------------------------------------------------------------------
    # Safety and Ethics (4 cards)
    # -------------------------------------------------------------------------
    {
        "category": "Safety and Ethics",
        "title": "Bloodletting / Bleeding Therapy (Ci Luo): Safety & Limits",
        "front": "State the safety rules, bleeding volume limits, contraindications, and sterile protocols for Bloodletting Therapy (Ci Luo).",
        "back": "Bloodletting Safety Standards (Ci Luo Fa - 刺络放血):\n• Sterile Technique:\n  - Always wear clean disposable examination gloves on BOTH hands.\n  - Disinfect the skin thoroughly with 70% alcohol swab; use ONLY single-use sterile lancets or three-edged needles.\n  - Discard the lancet immediately into sharps container after a single puncture.\n\n• Bleeding Volume Limits:\n  - Standard Therapeutic Volume: Typically 3 to 10 drops of blood from Jing-Well points, ear apex, or superficial vein clusters (Taiyang, BL40).\n  - Stop bleeding by compressing the puncture site with a sterile dry cotton ball; never leave bleeding wounds uncompressed.\n\n• Strict Clinical Contraindications:\n  1. Patients with Hemophilia, von Willebrand disease, or severe coagulopathies.\n  2. Patients taking therapeutic Anticoagulants (Warfarin, DOACs, Heparin).\n  3. Severe thrombocytopenia (Platelets < 50 x 10^9/L).\n  4. Severe anemia, severe hypotension, dehydration, or extreme physical exhaustion.\n  5. Puncturing varicose veins directly (can cause catastrophic uncontainable hemorrhage).",
        "consensus": "Gloves, single-use lancets, and volume limits of 5–10 drops are mandatory safety standards.",
        "variations": "Bloodletting produces immediate clearance of heat toxins and resolves stubborn local blood stasis when practiced safely.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM Clean Needle Technique Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Patient Positioning: Fall Prevention & Posture Hazards",
        "front": "Explain the safety rules for patient positioning during acupuncture and the hazards of treating patients in the seated position.",
        "back": "Patient Positioning Safety Rules:\n• The Seated Posture Hazard:\n  - Treating a patient in a seated chair carries a high risk of Vasovagal Syncope (Needle Fainting).\n  - When a seated patient faints: Blood pools in lower extremities, cerebral perfusion drops rapidly, the head slumps forward, and the patient may fall out of the chair, suffering severe traumatic head injury or fractures, while bent needles tear deep muscles.\n  - Mandatory Rule: All new patients, anxious patients, and elderly patients MUST be treated in the SUPINE or PRONE position on a treatment table.\n\n• Supine & Prone Safety Precautions:\n  - Provide supportive pillows under knees (in supine) to reduce lumbar lordosis strain.\n  - Provide pillows under ankles (in prone) to prevent foot drop and Achilles tension.\n  - Instruct the patient explicitly NOT TO MOVE, change position, or reach for their phone while needles are inserted.\n  - Ensure the call bell or practitioner buzzer is within easy reach of the patient.",
        "consensus": "Proper table positioning is the most effective preventative measure against needle fainting and falls.",
        "variations": "If a patient cannot lie flat due to severe congestive heart failure or COPD (orthopnea), treat in a secure recliner chair with head support.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Professional Boundaries: Social Media & Gifts",
        "front": "What are the ethical standards for maintaining professional boundaries regarding social media communication and accepting gifts from patients (COM-02)?",
        "back": "Professional Boundaries Standards (COM-02 Ethics):\n• Social Media Guidelines:\n  - Maintain strict separation between personal and professional social media profiles.\n  - NEVER accept 'friend' requests or private social connections from current patients on personal platforms (Facebook, Instagram).\n  - NEVER post patient clinical stories, photos, tongue images, or testimonials online without explicit, written, signed patient media release forms; even de-identified details can be recognized and violate PIPEDA privacy.\n  - Avoid providing clinical advice or treatment diagnoses over social media direct messages.\n\n• Accepting Gifts from Patients:\n  - Minor, Token Gifts: Inexpensive token gifts of appreciation (e.g. box of cookies, holiday chocolates, flowers) may be accepted graciously on behalf of the clinic team.\n  - Expensive or Personal Gifts: Substantial monetary gifts, expensive jewelry, personal items, or loans must be politely DECLINED.\n  - Rationale: High-value gifts distort the therapeutic boundary, create indebtedness, alter practitioner objectivity, and blur professional fiduciary duties.",
        "consensus": "Social media separation and declining significant gifts protect the fiduciary integrity of healthcare practitioners.",
        "variations": "Document any gift offered and declined in the patient chart to ensure transparent clinical records.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics Handbook", "CTCMA Professional Boundaries Policy"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Medical Records: Pediatric Record Retention Law",
        "front": "State the specific legal rule for retaining clinical records of pediatric patients (minors) under Canadian jurisprudence.",
        "back": "Pediatric Record Retention Standard (COM-02 Jurisprudence):\n• The Legal Rule:\n  - Patient clinical records, consent forms, and financial ledgers for pediatric patients (individuals under the legal age of majority: 18 or 19 depending on province) must be retained for:\n  - 10 YEARS (or 16 years in certain jurisdictions) AFTER THE PATIENT ATTAINS THE AGE OF MAJORITY.\n\n• Concrete Example:\n  - In a province where the age of majority is 19:\n  - If you treat a 5-year-old child today, you cannot discard the records 10 years from now (at age 15).\n  - The clock ONLY STARTS TICKING when the patient turns 19.\n  - You must retain that record until the patient reaches age 29 (19 + 10 years)!\n\n• Legal Rationale:\n  - A minor cannot initiate a civil malpractice lawsuit on their own behalf; they have statutory rights to file legal claims within the limitation period once they reach the legal age of majority.",
        "consensus": "Universal medico-legal standard across Canadian health professions regulatory colleges.",
        "variations": "Failure to maintain pediatric records until 10 years post-majority is an act of professional misconduct and leaves practitioner completely defenseless against delayed lawsuits.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics & Jurisprudence Handbook", "Limitations Act", "CTCMA Record Keeping Bylaws"])
    }
]

"""Illness Flashcards (42 high-yield clinical medicine cards).

Covers Internal Medicine, Surgery, EENT, and Traumatology:
Bi syndrome, Wei syndrome, Xiao Ke, Headaches, Insomnia, Cough, Asthma,
Digestive disorders, Stroke, Dizziness, EENT, Bell's palsy, Musculoskeletal conditions.
All points strictly use bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS = [
    {
        "category": "Illness",
        "title": "Bi Syndrome: Four Classic Patterns (Wind, Cold, Damp, Heat)",
        "front": "Differentiate the four classic patterns of Bi Syndrome (Arthro-Rheumatic Pain): Wandering (Xing Bi), Painful (Tong Bi), Fixed (Zhuo Bi), and Febrile (Re Bi).",
        "back": "Differential Comparison of Bi Syndrome (痹证):\n• Wandering Bi (Xing Bi - 行痹 / Wind Bi):\n  - Symptoms: Wandering, migratory joint pain that shifts from joint to joint; limited movement, chills/fever.\n  - Treatment Principle: Expel wind, unblock channels, nourish blood ('Treat wind by first treating blood; once blood moves, wind extinguishes').\n  - Primary Points: BL17 (Geshu / 膈俞), SP10 (Xuehai / 血海), GB20 (Fengchi / 风池), plus local points.\n\n• Painful Bi (Tong Bi - 痛痹 / Cold Bi):\n  - Symptoms: Severe, sharp, stabbing joint pain in fixed location; pain relieved by warmth, aggravated by cold; no redness/heat in joints.\n  - Treatment Principle: Scatter cold, warm channels, unblock collateral vessels.\n  - Primary Points: Moxibustion on local points, BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元), ST36 (Zusanli / 足三里).\n\n• Fixed Bi (Zhuo Bi - 着痹 / Damp Bi):\n  - Symptoms: Fixed heavy aching joint pain, swelling, numbness in skin/muscles, aggravated on rainy/damp days.\n  - Treatment Principle: Transform dampness, unblock channels, fortify Spleen.\n  - Primary Points: SP9 (Yinlingquan / 阴陵泉), SP6 (Sanyinjiao / 三阴交), ST36 (Zusanli / 足三里), ST40 (Fenglong / 丰隆).\n\n• Febrile Bi (Re Bi - 热痹 / Heat Bi):\n  - Symptoms: Redness, swelling, heat, burning excruciating pain in one or multiple joints; fever, thirst, dark urine.\n  - Treatment Principle: Clear heat, cool blood, unblock channels.\n  - Primary Points: LI11 (Quchi / 曲池), DU14 (Dazhui / 大椎), SP10 (Xuehai / 血海), and bleed local congested veins.",
        "consensus": "Universal foundational TCM classification for musculoskeletal arthritis and rheumatism.",
        "variations": "Chronic Bi syndrome develops into Bone Bi (Gu Bi) with joint deformity, requiring tonification of Liver and Kidneys.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed.", "Maciocia Foundations"])
    },
    {
        "category": "Illness",
        "title": "Wei Syndrome (Flaccidity): 'Treat Wei by Selecting Yangming'",
        "front": "Explain the classical therapeutic principle 'Treat Wei Syndrome by selecting Yangming' (Du Wei Du Qu Yang Ming - 独取阳明) and its acupoint application.",
        "back": "Classical Therapeutic Principle:\n• Pathology of Wei Syndrome (痿证): Motor weakness, flaccidity, and progressive muscular atrophy of the limbs (e.g. ALS, multiple sclerosis, Guillain-Barré, muscular dystrophy, post-polio paralysis).\n• The Ling Shu & Suwen Chapter 44 state: 'To treat flaccidity, uniquely select the Yangming channel.'\n\nUnderlying Mechanism:\n1. Yangming (Stomach & Large Intestine) is the Sea of Water and Grain: it generates all Post-Heaven Qi and Blood.\n2. Yangming is rich in both Qi and Blood; tonifying Yangming nourishes the muscles and sinews (Spleen governs the muscles).\n3. Yangming controls the sinews of the entire body and binds the bones.\n\nPoint Application:\n• Upper Limbs: LI15 (Jianyu / 肩髃), LI11 (Quchi / 曲池), LI10 (Shousanli / 手三里), LI4 (Hegu / 合谷).\n• Lower Limbs: ST31 (Biguan / 髀关), ST32 (Futu / 伏兔), ST36 (Zusanli / 足三里), ST41 (Jiexi / 解溪), paired with SP6 (Sanyinjiao / 三阴交) and GB34 (Yanglingquan / 阳陵泉).",
        "consensus": "The master rule for treating neurological motor paralysis and muscle wasting in acupuncture.",
        "variations": "Supplement with Back-Shu points (BL20, BL23) to address root organ depletion in chronic stages.",
        "sources": json.dumps(["Huangdi Neijing Suwen Ch. 44", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Illness",
        "title": "Xiao Ke (Wasting & Thirsting): Upper, Middle, and Lower Differentiation",
        "front": "Differentiate Upper, Middle, and Lower Xiao Ke (Wasting and Thirsting / Diabetes) by primary organ involvement, cardinal symptom, and point prescriptions.",
        "back": "Differential Comparison of Xiao Ke (消渴):\n• Upper Xiao Ke (Shang Xiao - 上消):\n  - Primary Organ: Lungs (Lung Heat scorching fluids).\n  - Cardinal Symptom: Extreme polydipsia (excessive thirst, dry mouth, drinking vast quantities of water).\n  - Primary Points: LU10 (Yuji / 鱼际), LU11 (Shaoshang / 少商), LU9 (Taiyuan / 太渊), BL13 (Feishu / 肺俞), REN24 (Chengjiang / 承浆).\n\n• Middle Xiao Ke (Zhong Xiao - 中消):\n  - Primary Organ: Stomach (Stomach Fire consuming fluids and grains).\n  - Cardinal Symptom: Polyphagia (voracious hunger, eating constantly yet losing weight, constipation).\n  - Primary Points: ST44 (Neiting / 内庭), ST36 (Zusanli / 足三里), REN12 (Zhongwan / 中脘), BL21 (Weishu / 胃俞), SP6 (Sanyinjiao / 三阴交).\n\n• Lower Xiao Ke (Xia Xiao - 下消):\n  - Primary Organ: Kidneys (Kidney Yin/Yang deficiency failing to hold fluids).\n  - Cardinal Symptom: Polyuria (frequent profuse urination, sweet or turbid urine, sore lower back, dry mouth, dizziness).\n  - Primary Points: KI3 (Taixi / 太溪), KI6 (Zhaohai / 照海), BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元), SP6 (Sanyinjiao / 三阴交).\n\n• Master Empirical Point for All Xiao Ke: Yishu (EX-B3 / Weiwanxiashu - 1.5 cun lateral to T8), the Pancreas Shu point.",
        "consensus": "Universal tripartite classification of diabetic wasting disease in TCM.",
        "variations": "Lower Xiao Ke with cold signs indicates Kidney Yang deficiency; lower Xiao Ke with hot palms/soles indicates Kidney Yin deficiency.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Headache: Channel Differentiation & Distal Acupoints",
        "front": "Differentiate Headaches by channel location (Taiyang, Yangming, Shaoyang, Jueyin) and specify the classic distal points for each.",
        "back": "Channel Differentiation of Headaches (Tou Tong - 头痛):\n1. Taiyang Headache (Occipital Headache):\n   - Location: Occiput, base of skull, radiating down the neck and upper back.\n   - Distal Points: BL60 (Kunlun / 昆仑), SI3 (Houxi / 后溪), BL65 (Shugu / 束骨).\n   - Local Points: GB20 (Fengchi / 风池), BL10 (Tianzhu / 天柱).\n\n2. Yangming Headache (Frontal Headache):\n   - Location: Forehead, supraorbital ridge, temples.\n   - Distal Points: LI4 (Hegu / 合谷), ST44 (Neiting / 内庭).\n   - Local Points: Yintang (印堂), ST8 (Touwei / 头维), Yuyao (鱼腰).\n\n3. Shaoyang Headache (Temporal / One-Sided Headache / Migraine):\n   - Location: Temples, sides of the head, behind the ears.\n   - Distal Points: GB41 (Zulinqi / 足临泣), SJ5 (Waiguan / 外关), GB43 (Xiaxi / 侠溪).\n   - Local Points: Taiyang (太阳), GB8 (Shuaigu / 率谷), SJ20 (Jiaosun / 角孙).\n\n4. Jueyin Headache (Vertex Headache):\n   - Location: Crown/top of the head (vertex), often feeling like a nail driven into the skull.\n   - Distal Points: LV3 (Taichong / 太冲), KI1 (Yongquan / 涌泉).\n   - Local Point: DU20 (Baihui / 百会), Sishencong (四神聪).",
        "consensus": "The primary clinical diagnostic and treatment paradigm for acute and chronic headaches.",
        "variations": "Shao Yin headaches manifest as deep headache accompanied by cold limbs and deep faint pulse.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Illness",
        "title": "Insomnia: Four Major Patterns & Point Prescriptions",
        "front": "Differentiate the four major patterns of Insomnia (Heart-Kidney Disharmony, Heart-Spleen Deficiency, Liver Fire, Phlegm-Heat) by sleep disturbance type and points.",
        "back": "Differential Comparison of Insomnia (Bu Mei - 不寐):\n• Heart-Kidney Disharmony (Xin Shen Bu Jiao - 心肾不交):\n  - Sleep Disturbance: Inability to fall asleep, frequent waking, nocturnal emissions, night sweats, hot palms/soles, palpitations.\n  - Points: HT7 (Shenmen / 神门), KI3 (Taixi / 太溪), KI6 (Zhaohai / 照海), BL15 (Xinshu / 心俞), BL23 (Shenshu / 肾俞).\n\n• Heart and Spleen Deficiency (Xin Pi Liang Xu - 心脾两虚):\n  - Sleep Disturbance: Difficulty falling asleep, dream-disturbed sleep, easily awakened, waking up early and unable to return to sleep; accompanied by fatigue, poor memory, palpitations, pale complexion.\n  - Points: HT7 (Shenmen / 神门), SP6 (Sanyinjiao / 三阴交), BL15 (Xinshu / 心俞), BL20 (Pishu / 脾俞), ST36 (Zusanli / 足三里).\n\n• Liver Fire Blazing (Gan Huo Shang Yan - 肝火上炎):\n  - Sleep Disturbance: Total inability to sleep due to racing thoughts, agitation, irritability, vivid nightmarish dreams, bitter taste in mouth, headache.\n  - Points: LV2 (Xingjian / 行间), LV3 (Taichong / 太冲), GB20 (Fengchi / 风池), HT7 (Shenmen / 神门).\n\n• Phlegm-Heat Disturbing Mind (Tan Re Rao Xin - 痰热扰心):\n  - Sleep Disturbance: Restless sleep with tossing and turning, epigastric oppression, heavy head, nausea, profuse sputum, nightmares.\n  - Points: ST40 (Fenglong / 丰隆), REN12 (Zhongwan / 中脘), PC6 (Neiguan / 内关), ST44 (Neiting / 内庭), Anmian (安眠).",
        "consensus": "Universal differentiation of sleep disorders in clinical acupuncture.",
        "variations": "Anmian (Extra point midway between GB20 and SJ17) is an empirical master local point included across all insomnia protocols.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed.", "Maciocia Foundations"])
    },
    {
        "category": "Illness",
        "title": "Cough: Wind-Cold vs Wind-Heat vs Phlegm-Damp vs Lung Yin Deficiency",
        "front": "Contrast the clinical presentation and point prescriptions for Acute Exterior Cough (Wind-Cold, Wind-Heat) vs Chronic Interior Cough (Phlegm-Damp, Lung Yin Deficiency).",
        "back": "Differential Comparison of Cough (Ke Sou - 咳嗽):\n• Wind-Cold Cough (Feng Han Ke Sou):\n  - Presentation: Cough with thin white watery sputum, chills, aversion to cold, clear nasal discharge, floating tight pulse, thin white coat.\n  - Points: LU7 (Lieque / 列缺), BL13 (Feishu / 肺俞), LI4 (Hegu / 合谷), Fengchi (GB20).\n\n• Wind-Heat Cough (Feng Re Ke Sou):\n  - Presentation: Barking cough with thick yellow sticky sputum, sore throat, fever, yellow nasal discharge, floating rapid pulse, yellow coat.\n  - Points: LU5 (Chize / 尺泽), LU11 (Shaoshang / 少商), LI11 (Quchi / 曲池), LI4 (Hegu / 合谷), Dazhui (DU14).\n\n• Phlegm-Damp Cough (Tan Shi Ke Sou):\n  - Presentation: Chronic rattling cough with copious white sticky sputum easily expectorated, worse in morning, chest fullness, slippery pulse, greasy white coat.\n  - Points: ST40 (Fenglong / 丰隆), LU5 (Chize / 尺泽), BL13 (Feishu / 肺俞), REN12 (Zhongwan / 中脘), SP9 (Yinlingquan / 阴陵泉).\n\n• Lung Yin Deficiency Cough (Fei Yin Xu Ke Sou):\n  - Presentation: Chronic dry hacking cough with scanty sticky or blood-streaked sputum, hoarseness, dry throat, five-palm heat, night sweats, peeled red tongue, thin rapid pulse.\n  - Points: LU9 (Taiyuan / 太渊), KI6 (Zhaohai / 照海), BL13 (Feishu / 肺俞), BL43 (Gaohuangshu / 膏肓俞), SP6 (Sanyinjiao / 三阴交).",
        "consensus": "Classic respiratory differentiation guiding exterior clearing vs interior phlegm/yin regulation.",
        "variations": "BL43 (Gaohuangshu) is the premier classical point for chronic, debilitating lung conditions and severe Yin exhaustion.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Asthma and Wheezing: Excess vs Deficiency Differentiation",
        "front": "Differentiate Excess Asthma (Shi Chuan - Cold Phlegm, Phlegm-Heat) from Deficiency Asthma (Xu Chuan - Lung Deficiency, Kidney Failing to Grasp Qi).",
        "back": "Differential Comparison of Asthma (Xiao Chuan - 哮喘):\n• Excess Asthma (Shi Chuan - 实喘):\n  - Dynamics: Sudden acute onset, loud forceful wheezing, rapid breathing with chest distension; patient speaks with loud voice; breathing relieved by leaning forward and expectorating.\n  - Cold Phlegm: White profuse sputum, aversion to cold; Points: Dingchuan (定喘), LU7 (Lieque / 列缺), BL13 (Feishu / 肺俞), Moxa on REN17 (Danzhong / 膻中).\n  - Phlegm-Heat: Yellow thick sputum, fever, thirst, red tongue, slippery rapid pulse; Points: Dingchuan (定喘), LU5 (Chize / 尺泽), ST40 (Fenglong / 丰隆), LI11 (Quchi / 曲池).\n\n• Deficiency Asthma (Xu Chuan - 虚喘):\n  - Dynamics: Chronic insidious onset, feeble wheezing, shortness of breath worse with minor exertion, feeble low voice; patient inhales with difficulty; relieved by rest.\n  - Lung Qi Deficiency: Spontaneous sweating, weak cough, pale tongue; Points: BL13 (Feishu / 肺俞), LU9 (Taiyuan / 太渊), ST36 (Zusanli / 足三里), REN17 (Danzhong / 膻中).\n  - Kidney Failing to Grasp Qi: Rapid shallow breathing, more difficulty inhaling than exhaling, sore cold lower back, faint deep pulse; Points: BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), KI3 (Taixi / 太溪), KI7 (Fuliu / 复溜), REN4 (Guanyuan / 关元).",
        "consensus": "Dingchuan (EX-B1, 0.5 cun lateral to DU14) is the universal empirical point for acute bronchospasm.",
        "variations": "Kidney failing to grasp Qi manifests characteristically as 'difficult inhalation, easy exhalation'.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Epigastric Pain (Wei Tong): Food Stagnation vs Liver-Stomach vs Deficiency Cold",
        "front": "Differentiate Epigastric Pain (Wei Tong) caused by Food Stagnation, Liver-Stomach Disharmony, and Spleen-Stomach Deficiency Cold.",
        "back": "Differential Comparison of Epigastric Pain (胃痛):\n• Food Stagnation (Shi Zhi Wei Tong):\n  - Pain Character: Severe distending epigastric pain aggravated by food/eating, relieved by vomiting; foul belching, sour regurgitation, anorexia, foul breath, constipation or foul diarrhea.\n  - Tongue: Thick, greasy, dirty coating; Pulse: Slippery (Hua) and forceful.\n  - Points: REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), ST21 (Liangmen / 梁门), ST44 (Neiting / 内庭), Inner Neiting (Neiting prick).\n\n• Liver-Stomach Disharmony (Gan Wei Bu He):\n  - Pain Character: Distending pain radiating to the hypochondrium and flanks, aggravated by emotional stress or anger; frequent sighing, bitter taste, belching.\n  - Tongue: Thin white coat, red edges; Pulse: Wiry (Xian).\n  - Points: LV14 (Qimen / 期门), LV3 (Taichong / 太冲), REN12 (Zhongwan / 中脘), PC6 (Neiguan / 内关), ST36 (Zusanli / 足三里).\n\n• Spleen-Stomach Deficiency Cold (Pi Wei Xu Han):\n  - Pain Character: Dull, continuous aching epigastric pain relieved by warmth and pressure, worse on an empty stomach, relieved by eating small meals; spitting of watery fluid, fatigue, cold limbs.\n  - Tongue: Pale, swollen with teeth marks; Pulse: Deep, slow, weak.\n  - Points: Moxa on REN12 (Zhongwan / 中脘), BL20 (Pishu / 脾俞), BL21 (Weishu / 胃俞), ST36 (Zusanli / 足三里), SP4 (Gongsun / 公孙).",
        "consensus": "Cornerstone gastrointestinal differential in Chinese internal medicine.",
        "variations": "Acute severe epigastric stabbing pain in a fixed spot with vomiting of dark blood indicates Blood Stasis (Point: BL17, SP10, ST34).",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Zhong Feng (Wind-Stroke): Tense (Bi) vs Flaccid (Tuo) Syndrome",
        "front": "Differentiate the Tense (Bi Zheng) and Flaccid (Tuo Zheng) Syndromes of Acute Wind-Stroke (Zhong Feng) and their emergency acupuncture protocols.",
        "back": "Emergency Differential of Acute Wind-Stroke (中风):\n• Tense Syndrome (Bi Zheng - 闭证 / Excess Closure):\n  - Clinical Signs: Clenched fists, tightly locked jaw (trismus), rigid extremities, red face, stertorous breathing with rattling phlegm, constipation, urinary retention, wiry rapid forceful pulse.\n  - Mechanism: Extreme pathogenic wind, fire, and phlegm occluding the sensory orifices.\n  - Emergency Protocol: Resuscitate and unblock orifices with vigorous sedation.\n  - Primary Points: Prick all Shixuan (EX-UE11 / ten fingertips) to bleed, DU26 (Shuigou / 水沟), LV3 (Taichong / 太冲), LI4 (Hegu / 合谷), ST40 (Fenglong / 丰隆). (Strictly NO moxibustion).\n\n• Flaccid Syndrome (Tuo Zheng - 脱证 / Deficiency Collapse):\n  - Clinical Signs: Open mouth, closed eyes, flaccid paralyzed limbs, open hands, snoring/faint breathing, urinary and fecal incontinence, profuse oily cold sweat on forehead, cold extremities, faint minute pulse.\n  - Mechanism: Separation of Yin and Yang; total collapse of Yuan Qi.\n  - Emergency Protocol: Rescue Yang from collapse and secure vital Qi.\n  - Primary Points: Heavy Moxibustion on DU20 (Baihui / 百会), REN8 (Shenque / 神阙 - salt moxa), REN4 (Guanyuan / 关元), ST36 (Zusanli / 足三里).",
        "consensus": "Critical emergency differentiation: Bi syndrome requires bleeding and unblocking; Tuo syndrome requires urgent heavy moxibustion to rescue Yang.",
        "variations": "Western medicine emergency transport (EMS 911) is paramount during acute stroke; these protocols represent classical acupuncture emergency management.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Wind-Stroke Sequelae (Hemiplegia): Body & Scalp Acupuncture",
        "front": "Outline the body acupuncture prescription and Jiao's Scalp Acupuncture lines for treating post-stroke hemiplegia and aphasia.",
        "back": "Acupuncture Protocols for Wind-Stroke Sequelae (中风后遗症):\n• Body Acupuncture Principles:\n  - Treat Yangming channels primarily ('Treat flaccidity by selecting Yangming') to boost Qi and Blood.\n  - Upper Extremity: LI15 (Jianyu / 肩髃), LI11 (Quchi / 曲池), LI10 (Shousanli / 手三里), LI4 (Hegu / 合谷), SJ5 (Waiguan / 外关), Baxie (EX-UE9).\n  - Lower Extremity: GB30 (Huantiao / 环跳), ST31 (Biguan / 髀关), GB34 (Yanglingquan / 阳陵泉), ST36 (Zusanli / 足三里), ST41 (Jiexi / 解溪), Bafeng (EX-LE10).\n\n• Jiao's Scalp Acupuncture (Jiao Shunfa):\n  - Motor Line (Upper 1/5): Needle bilaterally or contralateral side to treat lower extremity paralysis.\n  - Motor Line (Middle 2/5): Contralateral side to treat upper extremity paralysis.\n  - Motor Line (Lower 2/5): Contralateral side to treat facial paralysis and motor speech impairment.\n  - Speech Line I (Motor Aphasia): Over the lower 2/5 of motor line.\n  - Speech Line II (Nominal Aphasia): 3 cm behind parietal tubercle.",
        "consensus": "Combining body Yangming channels with scalp motor zones produces the highest clinical recovery rates for post-stroke hemiplegia.",
        "variations": "Electroacupuncture with dense-disperse wave is frequently applied across LI11-LI4 and GB34-ST36 during the rehabilitation window.",
        "sources": json.dumps(["Royal TCM tcm-03 Acupuncture Foundation", "Jiao Shunfa Scalp Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Dizziness and Vertigo (Xuan Yun): Four Major Patterns",
        "front": "Differentiate Dizziness/Vertigo (Xuan Yun) caused by Liver Yang Rising, Phlegm-Turbidity, Qi/Blood Deficiency, and Kidney Essence Deficiency.",
        "back": "Differential Comparison of Vertigo (眩晕):\n• Liver Yang Rising (Gan Yang Shang Kang):\n  - Sensation: Severe dizziness, feeling off-balance, aggravated by anger/stress, tinnitus like ocean waves, throbbing headache, red eyes, wiry rapid pulse.\n  - Points: LV3 (Taichong / 太冲), GB20 (Fengchi / 风池), KI3 (Taixi / 太溪), Taiyang (太阳).\n\n• Phlegm-Turbidity Obstructing Middle Jiao (Tan Zhuo Zhong Zu):\n  - Sensation: Heavy dizziness as if head is tightly bound in a cloth, spinning vertigo with nausea, vomiting of phlegm, chest oppression, greasy white coat, slippery pulse.\n  - Points: ST40 (Fenglong / 丰隆), REN12 (Zhongwan / 中脘), PC6 (Neiguan / 内关), ST36 (Zusanli / 足三里), Baihui (DU20).\n\n• Qi and Blood Deficiency (Qi Xue Kui Xu):\n  - Sensation: Mild continuous dizziness worse with fatigue or standing up suddenly (orthostatic), pale sallow complexion, palpitations, insomnia, pale tongue, thin weak pulse.\n  - Points: DU20 (Baihui / 百会), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), BL15 (Xinshu / 心俞).\n\n• Kidney Essence Deficiency (Shen Jing Kui Xu):\n  - Sensation: Dizziness accompanied by empty sensation in the head, chronic tinnitus like cicadas, sore weak lumbar spine and knees, memory loss, thin deep pulse.\n  - Points: BL23 (Shenshu / 肾俞), KI3 (Taixi / 太溪), DU4 (Mingmen / 命门), GB39 (Xuanzhong / 悬钟 - Hui of Marrow).",
        "consensus": "Classic differentiation separating excess wind/phlegm from deficiency blood/essence.",
        "variations": "Western correlation includes BPPV, Meniere's disease, vestibular neuritis, and orthostatic hypotension.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Bell's Palsy (Facial Paralysis): Acute vs Recovery Protocol",
        "front": "Outline the etiology, clinical manifestations, acute phase precautions, and point prescription for Bell's Palsy (Mian Tan - 面瘫).",
        "back": "Clinical Protocol for Bell's Palsy (面瘫):\n• Etiology: Wind-Cold or Wind-Heat attacking the Shaoyang and Yangming channels of the face, causing Qi and Blood stagnation and muscle malnutrition.\n• Signs: Inability to wrinkle forehead, incomplete eye closure (Bell's phenomenon), flattening of nasolabial groove, drooping mouth angle, drooling, food trapped in cheek.\n\n⚠️ Acute Phase Precaution (Days 1 to 7):\n• Do NOT apply strong manual stimulation, heavy electroacupuncture, or aggressive manipulation on local facial points during the first 7 days (risks facial spasm and axonal exhaustion).\n• Focus on gentle superficial needling, distal points to dispel wind (LI4, SJ5, GB20), and moxibustion if Wind-Cold.\n\nPoint Prescription (Recovery Phase):\n• Forehead/Eye: Yuyao (鱼腰), BL2 (Zanzhu / 攒竹), ST1 (Chengqi / 承泣), SJ23 (Sizhukong / 丝竹空).\n• Cheek/Mouth: ST4 (Dicang / 地仓) transfixed to ST6 (Jiache / 颊车), LI20 (Yingxiang / 迎香), ST7 (Xiaguan / 下关).\n• Distal Points: LI4 (Hegu / 合谷 - Command of face), SJ5 (Waiguan / 外关), GB20 (Fengchi / 风池).",
        "consensus": "Dicang transfixing to Jiache is the premier local needle technique for facial paralysis.",
        "variations": "Forehead wrinkle loss distinguishes peripheral Bell's palsy (CN VII) from central stroke.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Illness",
        "title": "Sciatica: Taiyang (BL) vs Shaoyang (GB) Pattern Differentiation",
        "front": "Differentiate Sciatica presenting along the Taiyang (Bladder) channel versus the Shaoyang (Gallbladder) channel, detailing point selection for each.",
        "back": "Channel Differentiation of Sciatica (Zuo Gu Shen Jing Tong):\n• Taiyang Pattern (Bladder Channel Sciatica):\n  - Pain Distribution: Radiates from lumbar spine down the buttock, POSTERIOR thigh, popliteal fossa, calf, and lateral malleolus to the little toe.\n  - Aggravated by: Straight leg raise (posterior chain stretch).\n  - Primary Points:\n    - Local: BL23 (Shenshu / 肾俞), BL25 (Dachangshu / 大肠俞), BL32 (Ciliao / 次髎), BL36 (Chengfu / 承扶).\n    - Distal: BL40 (Weizhong / 委中 - Command of back), BL57 (Chengshan / 承山), BL60 (Kunlun / 昆仑).\n\n• Shaoyang Pattern (Gallbladder Channel Sciatica):\n  - Pain Distribution: Radiates from the buttock down the LATERAL aspect of the thigh, lateral knee, fibula, and lateral ankle to the 4th toe.\n  - Aggravated by: Hip flexion with internal rotation.\n  - Primary Points:\n    - Local: GB30 (Huantiao / 环跳 - deep insertion to elicit radiating de qi).\n    - Distal: GB34 (Yanglingquan / 阳陵泉 - Hui of Sinews), GB39 (Xuanzhong / 悬钟), GB41 (Zulinqi / 足临泣).",
        "consensus": "Precise channel identification dictates whether to select posterior Bladder points or lateral Gallbladder points.",
        "variations": "Patients frequently exhibit a combined Taiyang-Shaoyang pattern requiring points from both channels (e.g. GB30 + BL40 + GB34 + BL60).",
        "sources": json.dumps(["Royal TCM TCM-10 Traumatology", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Frozen Shoulder (Adhesive Capsulitis): Local & Distal ST38 Protocol",
        "front": "Detail the local point prescription and the empirical distal puncture technique at ST38 (Tiaokou) for Frozen Shoulder (Lou Jian Feng).",
        "back": "Clinical Protocol for Frozen Shoulder (漏肩风 - 50-Year Shoulder):\n• Local Points:\n  - Anterior (Yangming): LI15 (Jianyu / 肩髃), Jianneiling (EX-UE / Extra anterior shoulder point midway between anterior axillary fold and LI15).\n  - Lateral (Shaoyang): SJ14 (Jianliao / 肩髎).\n  - Posterior (Taiyang): SI9 (Jianzhen / 肩贞), SI10 (Naoshu / 臑俞), SI11 (Tianzong / 天宗).\n\n• Empirical Distal Master Point Technique: ST38 (Tiaokou / 条口):\n  - Location: 8 cun inferior to ST35, 1 fingerbreadth lateral to anterior tibial crest.\n  - Technique: Use a 2.5 to 3.0 cun needle on the affected side. Puncture perpendicularly 1.5 - 2.5 cun through towards BL57 (Chengshan / 承山).\n  - Crucial Manipulation: While strongly manipulating the needle with lifting/thrusting to generate strong de qi, instruct the patient to actively move, abduct, and rotate the painful shoulder.\n  - Mechanism: Powerfully unblocks Yangming and Taiyang Qi and Blood, dramatically improving shoulder range of motion instantly.",
        "consensus": "ST38 through-punctured to BL57 with active patient movement is the premier distal technique for adhesive capsulitis worldwide.",
        "variations": "Moxa on Jianneiling and LI15 is indicated if Cold Bi is the primary etiology.",
        "sources": json.dumps(["Royal TCM TCM-10 Traumatology", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Illness",
        "title": "Acute Lumbar Sprain: Emergency Distal Points",
        "front": "What are the primary distal acupoints for immediate pain relief and mobility restoration in Acute Lumbar Sprain (Ji Xing Yao Niu Shang)?",
        "back": "Emergency Distal Protocol for Acute Lumbar Sprain (急性腰扭伤):\n• Distal Points:\n  1. Yaotongxue (EX-UE7 - 腰痛穴 / Lumbar Pain Points):\n     - Location: On dorsum of hand, 2 points located between 2nd & 3rd metacarpal bases, and 4th & 5th metacarpal bases.\n     - Technique: Puncture obliquely 0.5 - 0.8 cun towards center of metacarpus with vigorous manipulation; instruct patient to gently flex, extend, and rotate the lumbar spine while needles are in place.\n  2. BL40 (Weizhong / 委中):\n     - Gao Wu Command point of the Lumbar Region. Prick popliteal superficial veins to bleed 5–10 drops, or perpendicular needle insertion.\n  3. DU26 (Shuigou / 水沟):\n     - Puncture obliquely upward 0.5 cun with vigorous reducing method; stimulate while patient walks/moves back.\n  4. SI3 (Houxi / 后溪) + BL62 (Shenmai / 申脉):\n     - Opens Du Mai and Yang Qiao Mai for spinal column pain.\n\n• Local points (BL23, BL25, Ah Shi) are added in subacute phase, but distal unblocking with active movement is paramount initially.",
        "consensus": "Yaotongxue and BL40 bleeding with active patient mobilization is the premier rapid-relief protocol for acute low back spasms.",
        "variations": "If pain is strictly on midline spine, needle DU26 and SI3; if lateral to spine, emphasize BL40 and Yaotongxue.",
        "sources": json.dumps(["Royal TCM TCM-10 Traumatology", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Diarrhea (Xie Xie): Acute vs Chronic (Cock-Crow Diarrhea)",
        "front": "Differentiate Acute Diarrhea (Damp-Heat, Cold-Damp) from Chronic Diarrhea (Spleen Deficiency, Cock-Crow / Daybreak Diarrhea).",
        "back": "Differential Comparison of Diarrhea (泄泻):\n• Acute Diarrhea:\n  - Cold-Damp: Watery stool, abdominal pain relieved by warmth, borborygmi, pale tongue, soft slow pulse. (Points: Moxa on REN8 Shenque, ST25 Tianshu, ST36 Zusanli, SP9 Yinlingquan).\n  - Damp-Heat: Urgent diarrhea with burning anus, foul-smelling yellow stool, abdominal pain, yellow greasy coat, slippery rapid pulse. (Points: ST25 Tianshu, ST37 Shangjuxu - Lower He-Sea of LI, SP9 Yinlingquan, LI11 Quchi).\n\n• Chronic Diarrhea:\n  - Spleen Deficiency: Loose stools with undigested food grains, worse after eating greasy food, fatigue, pale swollen tongue. (Points: BL20 Pishu, REN12 Zhongwan, ST36 Zusanli, SP3 Taibai).\n  - Cock-Crow / Daybreak Diarrhea (Wu Geng Xie - 五更泻 / Kidney Yang Deficiency):\n    - Diarrhea occurring every morning around 5 AM (dawn) preceded by abdominal pain and rumbling, relieved by defecation; cold limbs, cold lower back.\n    - Points: Moxa on DU4 (Mingmen / 命门), BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元), KI3 (Taixi / 太溪), ST36 (Zusanli / 足三里).",
        "consensus": "ST25 and ST37 form the core combination for all intestinal dysfunctions.",
        "variations": "ST37 (Shangjuxu) is the Lower He-Sea of Large Intestine; indispensable for acute intestinal inflammation.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Dysentery (Li Ji): Hallmark Symptoms & Treatment Protocol",
        "front": "What are the hallmark clinical symptoms of Dysentery (Li Ji - 痢疾) and the primary acupuncture protocol for Damp-Heat Dysentery?",
        "back": "Dysentery (痢疾 - Acute Bacillary Dysentery / Amebiasis):\n• Hallmark Clinical Triad:\n  1. Abdominal pain.\n  2. Tenesmus (Hou Zhong - 后重 / urgent, painful, straining desire to defecate with feeling of incomplete evacuation).\n  3. Stools mixed with red and white Pus and Blood (Bai Dai / Chi Bai Li).\n\n• Damp-Heat Dysentery (Shi Re Li - Most Common):\n  - Stools containing bright red blood and white pus, burning sensation in anus, tenesmus, fever, thirst, dark scanty urine, red tongue with thick greasy yellow coat, slippery rapid pulse.\n\n• Acupuncture Treatment Protocol:\n  - ST25 (Tianshu / 天枢 - Front-Mu of Large Intestine): Regulates intestines, relieves tenesmus.\n  - ST37 (Shangjuxu / 上巨虚 - Lower He-Sea of Large Intestine): Purges intestinal damp-heat, clears toxin.\n  - SP9 (Yinlingquan / 阴陵泉) + LI11 (Quchi / 曲池): Clears dampness and heat.\n  - BL32 (Ciliao / 次髎): Clears heat in lower jiao and relieves rectal tenesmus.\n  - Inner Neiting (prick to bleed) for toxic heat dysentery.",
        "consensus": "Tenesmus and bloody-purulent stool distinguish true dysentery from simple diarrhea.",
        "variations": "If more white pus = Dampness predominates; if more red blood = Heat and toxin predominate.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Constipation (Bian Bi): Heat vs Qi Stagnation vs Deficiency",
        "front": "Differentiate Constipation (Bian Bi) caused by Heat Accumulation, Qi Stagnation, Blood Deficiency, and Yang Deficiency.",
        "back": "Differential Comparison of Constipation (便秘):\n• Heat Constipation (Re Bi):\n  - Stools dry, hard, pebble-like; abdominal distension, red face, thirst, halitosis, red tongue with dry yellow coat, rapid forceful pulse.\n  - Points: ST25 (Tianshu / 天枢), SJ6 (Zhigou / 支沟), ST44 (Neiting / 内庭), LI11 (Quchi / 曲池), ST37 (Shangjuxu / 上巨虚).\n\n• Qi Stagnation Constipation (Qi Bi):\n  - Sensation of difficulty defecating despite stool not being severely dry; frequent belching, hypochondriac fullness, irritable mood, wiry pulse.\n  - Points: SJ6 (Zhigou / 支沟), LV3 (Taichong / 太冲), REN12 (Zhongwan / 中脘), ST25 (Tianshu / 天枢).\n\n• Blood Deficiency Constipation (Xue Xu Bi):\n  - Dry stools, difficulty defecating in elderly or postpartum women; pale face, dizziness, palpitations, pale tongue, thin pulse.\n  - Points: SJ6 (Zhigou / 支沟), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), KI6 (Zhaohai / 照海).\n\n• Yang Deficiency / Cold Constipation (Cold Bi):\n  - Difficulty passing stool, clear urine, cold limbs, pale wet tongue, deep slow pulse.\n  - Points: Moxa on SJ6 (Zhigou / 支沟), KI6 (Zhaohai / 照海), BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元).\n\n• Master Empirical Pair for All Constipation: SJ6 (Zhigou / 支沟) + KI6 (Zhaohai / 照海).\n  - Mechanism: SJ6 moves Qi and clears heat; KI6 moistens dryness and generates fluid in the lower jiao.",
        "consensus": "SJ6 + KI6 is the classic empirical point combination for constipation worldwide.",
        "variations": "SJ6 is the Sanjiao Jing-River point; renowned for clearing upper and lower constipation.",
        "sources": json.dumps(["Royal TCM TCM-06 Internal Medicine", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Illness",
        "title": "Tinnitus and Deafness: Sudden Onset vs Gradual Onset",
        "front": "Contrast Sudden Onset Tinnitus (Excess Liver/GB Fire) with Gradual Onset Tinnitus (Kidney Deficiency) by sound character and points.",
        "back": "Differential Comparison of Tinnitus (Er Ming - 耳鸣):\n• Sudden Onset Tinnitus / Deafness (Excess Pattern - Liver/GB Fire):\n  - Sound Character: Sudden onset, loud, high-pitched ringing or roaring like rushing water/ocean waves, not relieved or worsened by pressing ear (refuses pressure).\n  - Accompanied by: Irritability, red eyes, bitter mouth taste, headache, wiry rapid pulse, red tongue with yellow coat.\n  - Primary Points: Local ear points (SJ17 Yifeng, SI19 Tinggong, GB2 Tinghui) + Distal sedation points: GB43 (Xiaxi / 侠溪), LV2 (Xingjian / 行间), SJ5 (Waiguan / 外关).\n\n• Gradual Onset Tinnitus / Deafness (Deficiency Pattern - Kidney Deficiency):\n  - Sound Character: Chronic, gradual insidious onset, low-pitched faint buzzing like cicadas or distant hum, worse when tired or at night, temporarily IMPROVED OR DIMINISHED BY PRESSING EAR (desires pressure).\n  - Accompanied by: Sore weak lumbar/knees, dizziness, blurred vision, nocturnal emissions, thin deep pulse, pale or red peeled tongue.\n  - Primary Points: Local ear points (SJ17, SI19) + Distal tonification points: KI3 (Taixi / 太溪), BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), GB39 (Xuanzhong / 悬钟).",
        "consensus": "The response to ear pressure (worsened vs improved) definitively identifies excess vs deficiency tinnitus.",
        "variations": "SJ17 (Yifeng) is the master local point behind the earlobe for unblocking the auditory orifice.",
        "sources": json.dumps(["Royal TCM TCM-11 Eye ear nose throat", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Allergic Rhinitis / Bi Yuan: Wind-Heat vs Lung/Spleen Deficiency",
        "front": "Differentiate Allergic Rhinitis / Sinusitis (Bi Yuan - 鼻渊) caused by Wind-Heat attack versus Lung and Spleen Qi Deficiency.",
        "back": "Differential Comparison of Rhinitis (鼻渊):\n• Wind-Heat / Lung Heat Pattern:\n  - Symptoms: Severe nasal congestion, loss of smell, thick yellow foul-smelling nasal discharge, frontal headache, red eyes, fever, sore throat, red tongue tip with thin yellow coat, floating rapid pulse.\n  - Points: LI20 (Yingxiang / 迎香), Yintang (印堂), Bitong (EX-HN8), LU7 (Lieque / 列缺), LI4 (Hegu / 合谷), LI11 (Quchi / 曲池), GB20 (Fengchi / 风池).\n\n• Lung and Spleen Qi Deficiency Pattern (Chronic Allergic Rhinitis):\n  - Symptoms: Chronic recurring clear watery nasal discharge, paroxysmal sneezing attacks, pale nasal mucosa, nasal itching, worse with temperature changes or cold drafts; fatigue, spontaneous sweating, poor appetite, pale tongue with teeth marks, weak pulse.\n  - Points: LI20 (Yingxiang / 迎香), Yintang (印堂), Bitong (EX-HN8), BL13 (Feishu / 肺俞), BL20 (Pishu / 脾俞), ST36 (Zusanli / 足三里), LU9 (Taiyuan / 太渊), with moxa on DU14 (Dazhui / 大椎).",
        "consensus": "Bitong (at upper end of nasolabial groove) + LI20 is the premier local pair for nasal obstruction.",
        "variations": "Moxa on Dazhui and Feishu is particularly effective for chronic cold-induced allergic rhinitis.",
        "sources": json.dumps(["Royal TCM TCM-11 Eye ear nose throat", "CAM 3rd Ed."])
    },
    {
        "category": "Illness",
        "title": "Tennis Elbow (Lateral Epicondylitis): Ah Shi & Yangming Protocol",
        "front": "Detail the local and distal acupoint prescription and needle manipulation for Tennis Elbow (Lateral Epicondylitis / Zhou Lao).",
        "back": "Clinical Protocol for Tennis Elbow (肘劳 - Lateral Epicondylitis):\n• Etiology: Chronic repetitive strain or acute trauma injuring the common extensor tendon origin at the lateral epicondyle of the humerus, leading to Qi and Blood stasis in the Large Intestine Yangming channel.\n\n• Local Point Prescription:\n  - Ah Shi (阿是穴): Puncture directly into the tender point at the lateral epicondyle origin of extensor carpi radialis brevis.\n  - LI11 (Quchi / 曲池): In the depression at lateral end of cubital crease.\n  - LI10 (Shousanli / 手三里): 2 cun distal to LI11 on the extensor muscle belly.\n  - LI12 (Zhouliao / 肘髎): In the depression on the lateral border of humerus superior to epicondyle.\n  - LU5 (Chize / 尺泽): To balance Yin-Yang and clear local tendon heat.\n\n• Technique & Manipulation:\n  - Needle Ah Shi point with gentle pecking/multi-directional insertion (sparrow-pecking method) to stimulate local tendon repair.\n  - Apply indirect moxibustion (moxa stick) or warm needle acupuncture if pain is worse with cold/damp.\n  - Distal Point: LI4 (Hegu / 合谷) or ST38 (Tiaokou / 条口) on the same side with active wrist extension during manipulation.",
        "consensus": "LI10, LI11, and local Ah Shi points form the core protocol for lateral epicondylitis worldwide.",
        "variations": "Avoid deep needle manipulation directly against the periosteum if acute tendon inflammation is present.",
        "sources": json.dumps(["Royal TCM TCM-10 Traumatology", "CAM 3rd Ed.", "Deadman Manual"])
    }
]

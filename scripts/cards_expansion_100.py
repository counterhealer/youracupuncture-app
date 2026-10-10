"""100 High-Yield Board Exam Flashcards for TCM & Acupuncture Study Suite.

Covers critical curriculum gaps across all 7 categories:
- Meridians & Points: 28 cards
- Western Medicine: 20 cards
- Diagnosis: 16 cards
- Illness: 16 cards
- Gynecology: 8 cards
- Paediatrics: 6 cards
- Safety & Ethics: 6 cards
Total: 100 cards.
All point nomenclature strictly follows bilingual CODE (Pinyin / Hanzi).
"""

CARDS_100 = [
    # =========================================================================
    # 1. MERIDIANS & POINTS (28 CARDS)
    # =========================================================================
    {
        "category": "Meridians and Points",
        "title": "LU5 (Chize / 尺泽)",
        "front": "Identify the category, precise anatomical location, actions, and needling safety for LU5 (Chize / 尺泽).",
        "back": "• Category: He-Sea (Water point) of the Lung channel.\n• Location: On the cubital crease of the elbow, in the depression on the radial side of the tendon of biceps brachii.\n• Actions: Clears Lung heat, expels phlegm, descends rebellious Lung Qi, relaxes sinews.\n• Primary Indications: Cough, asthma, hemoptysis (coughing blood), fullness in chest, sore throat, elbow pain/spasm.\n• Needling: Perpendicular insertion 0.5–1.0 cun. Caution: Avoid cephalic vein puncture.",
        "consensus": "All major texts (CAM, Deadman) agree LU5 is the premier He-Sea water point for clearing excess Lung heat and draining phlegm from the upper burner.",
        "variations": "Deadman emphasizes sedating child point in Five Phase theory (Water point on Metal channel). CAM highlights prick-to-bleed for acute heatstroke and vomiting.",
        "sources": '["CAM p. 61", "Deadman p. 77"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "LU9 (Taiyuan / 太渊)",
        "front": "What are the categories, actions, and precautions for LU9 (Taiyuan / 太渊)?",
        "back": "• Category: Shu-Stream (Earth), Yuan-Source, and Hui-Meeting point for the Vessels (Mai).\n• Location: At the radial end of the transverse crease of the wrist, in the depression between the radial artery and abductor pollicis longus tendon.\n• Actions: Tonifies Lung Qi and Lung Yin, transforms phlegm, regulates and harmonizes all blood vessels.\n• Primary Indications: Chronic cough, wheezing, weak voice, pulseless disease (Takayasu's arteritis), wrist pain.\n• Needling: Perpendicular insertion 0.3–0.5 cun. Caution: Palpate and avoid the radial artery!",
        "consensus": "CAM and Deadman agree LU9 is the primary point to tonify Lung Qi and Yin (Mother point on Metal channel) and governs all pulse vessels.",
        "variations": "CAM notes gentle insertion without vigorous dispersion. Deadman notes essential role in promoting fluid production for Lung Yin deficiency.",
        "sources": '["CAM p. 64", "Deadman p. 83"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "LI10 (Shousanli / 手三里)",
        "front": "State the anatomical location, actions, and clinical indications for LI10 (Shousanli / 手三里).",
        "back": "• Location: On the radial side of the dorsal forearm, 2 cun distal to LI11 (Quchi), on the line connecting LI5 and LI11.\n• Actions: Regulates Qi and Blood, harmonizes the intestines and Stomach, expels wind-damp.\n• Primary Indications: Abdominal pain, diarrhea, toothache, motor impairment of upper limb, tennis elbow, shoulder stiffness.\n• Needling: Perpendicular insertion 0.8–1.2 cun.",
        "consensus": "Major clinical consensus regards LI10 as the 'Arm Zusanli', exerting distal regulatory power over intestinal peristalsis and local arm mobility.",
        "variations": "CAM emphasizes combination with ST36 for general exhaustion and digestive hypofunction.",
        "sources": '["CAM p. 70", "Deadman p. 109"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "LI20 (Yingxiang / 迎香)",
        "front": "Detail the location, actions, and needling technique for LI20 (Yingxiang / 迎香).",
        "back": "• Category: Crossing point of Large Intestine and Stomach channels.\n• Location: In the nasolabial groove, at the level of the midpoint of the lateral border of the ala nasi.\n• Actions: Opens nasal passages, dispels exterior wind, clears heat.\n• Primary Indications: Nasal congestion, rhinitis, sinusitis, loss of smell (anosmia), facial paralysis, epistaxis.\n• Needling: Oblique or transverse insertion 0.3–0.5 cun directed medially and superiorly along the nasolabial groove. Moxibustion is traditionally prohibited.",
        "consensus": "Premier local point in TCM for any nasal pathology. CAM and Deadman agree moxa is contraindicated due to facial sensitivity.",
        "variations": "Some classical texts note needle sensation radiating toward root of nose and inner canthus.",
        "sources": '["CAM p. 74", "Deadman p. 119"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "ST8 (Touwei / 头维)",
        "front": "What are the location, actions, and needling safety rules for ST8 (Touwei / 头维)?",
        "back": "• Category: Crossing point of Stomach, Gallbladder, and Yangwei channels.\n• Location: At the corner of the forehead, 0.5 cun directly above the anterior hairline, 4.5 cun lateral to the midline (DU24).\n• Actions: Dispels wind, relieves headache, clears the head and eyes.\n• Primary Indications: Frontal or temporal splitting headache, dizziness, eye pain, excessive lacrimation on exposure to wind.\n• Needling: Transverse insertion 0.5–1.0 cun along the scalp posteriorly or anteriorly. Moxibustion is contraindicated.",
        "consensus": "Consensus confirms ST8 as essential for Yangming/Shaoyang frontal headache with eye strain.",
        "variations": "Deadman notes puncture should strictly follow the subaponeurotic layer without vigorous pecking to avoid periosteal pain.",
        "sources": '["CAM p. 81", "Deadman p. 138"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "ST25 (Tianshu / 天枢)",
        "front": "Describe the category, location, actions, and needling depth precautions for ST25 (Tianshu / 天枢).",
        "back": "• Category: Front-Mu point of the Large Intestine.\n• Location: On the middle abdomen, 2 cun lateral to the center of the umbilicus (REN8).\n• Actions: Regulates intestines, harmonizes Spleen and Stomach, resolves damp-heat, moves Qi and blood stasis.\n• Primary Indications: Diarrhea, constipation, dysentery, abdominal pain, borborygmus, intestinal obstruction, menstrual irregularity.\n• Needling: Perpendicular insertion 0.8–1.5 cun. Caution: In thin patients, deep puncture may penetrate the peritoneal cavity!",
        "consensus": "Universal consensus confirms ST25 as the single most important Front-Mu point for both acute and chronic intestinal disorders.",
        "variations": "Maciocia highlights bidirectional regulation: sedates for constipation, tonifies/moxa for chronic loose stools.",
        "sources": '["CAM p. 86", "Deadman p. 153"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "ST28 (Shuidao / 水道)",
        "front": "What is the location, clinical meaning, and anatomical caution for ST28 (Shuidao / 水道)?",
        "back": "• Location: On the lower abdomen, 3 cun below the umbilicus (level with REN4), 2 cun lateral to the midline.\n• Translation/Meaning: 'Water Passage' – governs fluid pathways in lower abdomen.\n• Actions: Regulates the lower jiao, dispels damp-heat, benefits urination, moves blood stasis in uterus.\n• Primary Indications: Edema, urinary retention, dysuria (Lin syndrome), dysmenorrhea, infertility, uterine masses.\n• Needling: Perpendicular insertion 0.8–1.2 cun. Caution: Empty the urinary bladder prior to needling to avoid puncture!",
        "consensus": "Deadman and CAM agree ST28 is premier for lower abdominal fluid stagnation and gynecological damp-heat accumulation.",
        "variations": "CAM pairs ST28 with SP9 for ascites and lower extremity pitting edema.",
        "sources": '["CAM p. 87", "Deadman p. 157"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "ST40 (Fenglong / 丰隆)",
        "front": "Explain the category, location, and the classic principle of ST40 (Fenglong / 丰隆) in phlegm pathology.",
        "back": "• Category: Luo-Connecting point of the Stomach channel (linking to Spleen).\n• Location: On the anterolateral lower leg, 8 cun superior to the lateral malleolus, 1 fingerbreadth (middle finger) lateral to ST38.\n• Actions: Transforms and expels phlegm and dampness, clears phlegm from chest and mind, descends Stomach Qi.\n• Core Principle: The quintessential point for ALL forms of phlegm: substantial phlegm (cough, chest fullness) and insubstantial phlegm (dizziness, mania, lipomas, lethargy, cloudy thinking).\n• Needling: Perpendicular insertion 1.0–1.5 cun.",
        "consensus": "Universal consensus across all schools: ST40 is the number one distal point to resolve phlegm anywhere in the human body.",
        "variations": "CAM pairs ST40 with SP3 to treat the source and manifestation of damp-phlegm simultaneously.",
        "sources": '["CAM p. 91", "Deadman p. 169"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "ST44 (Neiting / 内庭)",
        "front": "State the category, location, and primary clinical actions for ST44 (Neiting / 内庭).",
        "back": "• Category: Ying-Spring (Water point) of the Stomach channel.\n• Location: On the dorsum of the foot, between the 2nd and 3rd toes, proximal to the margin of the web at the junction of red and white skin.\n• Actions: Clears Stomach Heat, harmonizes intestines, relieves pain.\n• Primary Indications: Toothache (especially lower jaw), facial pain/trigeminal neuralgia, sore throat, epistaxis, gastric acid regurgitation, febrile hunger.\n• Needling: Perpendicular or oblique insertion 0.5–0.8 cun directed proximally.",
        "consensus": "Classic Ying-Spring water point designed to extinguish flaring Stomach Fire in the head, face, and gastrointestinal tract.",
        "variations": "Deadman notes pairing with LI4 for severe acute facial inflammation and tooth abscess.",
        "sources": '["CAM p. 93", "Deadman p. 174"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "SP4 (Gongsun / 公孙)",
        "front": "Detail the category, confluent pairings, location, and actions of SP4 (Gongsun / 公孙).",
        "back": "• Category: Luo-Connecting point of Spleen channel; Confluent point of the Chong Mai (Chong Vessel).\n• Paired Confluent: Coupled with PC6 (Neiguan) to treat disorders of the chest, heart, and epigastrium.\n• Location: On the medial aspect of the foot, in the depression distal and inferior to the base of the 1st metatarsal bone.\n• Actions: Fortifies Spleen, harmonizes middle burner, regulates Chong Mai, resolves dampness.\n• Primary Indications: Epigastric pain, vomiting, acute diarrhea, dysmenorrhea, irregular menses, chest fullness.\n• Needling: Perpendicular insertion 0.5–1.0 cun.",
        "consensus": "Supreme clinical point for gastrointestinal harmony and gyn-endocrinological balance via the Sea of Blood (Chong Mai).",
        "variations": "CAM highlights treatment of acute food retention; Deadman highlights mental-emotional anxiety linked to gastric distress.",
        "sources": '["CAM p. 98", "Deadman p. 184"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "SP10 (Xuehai / 血海)",
        "front": "Identify the name meaning, location, actions, and clinical indications for SP10 (Xuehai / 血海).",
        "back": "• Translation/Name: 'Sea of Blood'.\n• Location: On the medial aspect of the thigh, 2 cun superior to the superior-medial border of the patella, on the bulge of the vastus medialis muscle.\n• Actions: Invigorates blood, dispels blood stasis, cools blood heat, tonifies blood.\n• Primary Indications: Urticaria, eczema, skin pruritus, psoriasis, dysmenorrhea, amenorrhea, dysfunctional uterine bleeding.\n• Needling: Perpendicular insertion 1.0–1.5 cun.",
        "consensus": "Universal consensus: Premier dermatological and gynecological point. Traditional axiom: 'To treat wind, first treat blood; when blood moves, wind naturally disappears.'",
        "variations": "CAM notes pairing with LI11 for acute allergic skin lesions.",
        "sources": '["CAM p. 101", "Deadman p. 193"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "HT5 (Tongli / 通里)",
        "front": "What are the category, location, and clinical indications for HT5 (Tongli / 通里)?",
        "back": "• Category: Luo-Connecting point of the Heart channel.\n• Location: On the radial side of the flexor carpi ulnaris tendon, 1 cun proximal to the transverse crease of the wrist (HT7).\n• Actions: Calms the Shen, regulates Heart rhythm, benefits the tongue and speech.\n• Primary Indications: Sudden loss of voice (aphasia/aphonia), stuttering, tongue stiffness after stroke, palpitations, arrhythmia, emotional agitation.\n• Needling: Perpendicular insertion 0.3–0.5 cun. Caution: Avoid ulnar artery on the medial side.",
        "consensus": "The premier acupoint for post-stroke speech impairment, motor aphasia, and sudden vocal cord paralysis due to Heart Luo path reaching the tongue root.",
        "variations": "Deadman notes special utility in menorrhagia caused by Heart fire communicating heat to the Small Intestine and Uterus.",
        "sources": '["CAM p. 107", "Deadman p. 214"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "HT6 (Yinxi / 阴郄)",
        "front": "Explain the category, location, actions, and emergency value of HT6 (Yinxi / 阴郄).",
        "back": "• Category: Xi-Cleft point of the Heart channel.\n• Location: On the radial side of the flexor carpi ulnaris tendon, 0.5 cun proximal to the wrist crease (HT7).\n• Actions: Regulates Heart blood, cools fire, nourishes Heart Yin, stops night sweats.\n• Primary Indications: Acute cardiac pain, angina pectoris, palpitations, night sweats (steaming bone), hematemesis, epistaxis.\n• Needling: Perpendicular insertion 0.3–0.5 cun.",
        "consensus": "Universal consensus: As a Xi-Cleft point, it treats acute pain (cardiac angina) and acute bleeding, while also acting as a key point for debilitating night sweats.",
        "variations": "CAM emphasizes combination with KI7 for severe night sweating from Heart/Kidney Yin exhaustion.",
        "sources": '["CAM p. 108", "Deadman p. 216"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "SI8 (Xiaohai / 小海)",
        "front": "Identify the category, location, actions, and needling sensation for SI8 (Xiaohai / 小海).",
        "back": "• Category: He-Sea (Earth point) of the Small Intestine channel.\n• Location: In the depression between the olecranon of the ulna and the medial epicondyle of the humerus (ulnar nerve groove).\n• Actions: Clears heat and swelling, calms Shen, activates channel and alleviates pain.\n• Primary Indications: Swelling of cheek, neck and shoulder stiffness, ulnar nerve neuropathy (cubital tunnel), epilepsy, numbness of pinky finger.\n• Needling: Perpendicular insertion 0.3–0.5 cun. An electric radiating sensation along ulnar nerve should not be excessively provoked.",
        "consensus": "Consensus confirms SI8 as Earth son-point for sedating Small Intestine fire, and key local point for cubital tunnel entrapment.",
        "variations": "Deadman notes historical indications for emotional mania and psycho-emotional agitation.",
        "sources": '["CAM p. 115", "Deadman p. 238"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "SI19 (Tinggong / 听宫)",
        "front": "State the anatomical location, channel crossing, actions, and opening-mouth protocol for SI19 (Tinggong / 听宫).",
        "back": "• Category: Crossing point of Small Intestine, San Jiao, and Gallbladder channels.\n• Location: On the face, anterior to the tragus and posterior to the condyloid process of the mandible, in the depression formed when the mouth is opened.\n• Protocol: Must needle with the patient's mouth slightly open to reveal the articular depression!\n• Actions: Benefits ears, clears heat, calms Shen.\n• Primary Indications: Tinnitus, deafness, otitis media, ear discharge, TMJ pain, toothache.\n• Needling: Perpendicular insertion 0.5–1.0 cun with mouth open.",
        "consensus": "Universal consensus: Premier auditory acupoint among the three ear points (SJ17, SI19, GB2).",
        "variations": "CAM pairs with SJ3 and GB43 for excess ear disorders; with KI3 for deficiency ear ringing.",
        "sources": '["CAM p. 120", "Deadman p. 250"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "BL1 (Jingming / 睛明)",
        "front": "Provide the precise needling technique and safety protocol for BL1 (Jingming / 睛明).",
        "back": "• Category: Crossing point of BL, SI, ST, GB, Yin Qiao, and Yang Qiao channels.\n• Location: 0.1 cun superior to the inner canthus of the eye.\n• Protocol: \n  1. Patient looks upward and outward.\n  2. Acupuncturist uses left index finger to gently push the eyeball laterally.\n  3. Puncture slowly along the medial orbital wall to depth of 0.5–1.0 cun.\n  4. STRICTLY NO rotation, lifting, or thrusting manipulation!\n  5. On withdrawal, immediately compress firmly with dry sterile cotton ball for 1–2 minutes to prevent hematoma.\n• Indications: Myopia, optic atrophy, glaucoma, conjunctivitis, night blindness.",
        "consensus": "Absolute board exam consensus: One of the highest-liability points in acupuncture. Technique must be exact to prevent retrobulbar hemorrhage.",
        "variations": "CAM warns against moxibustion under any circumstance. Deadman emphasizes slender 32-34 gauge needle.",
        "sources": '["CAM p. 124", "Deadman p. 256"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "BL11 (Dazhu / 大杼)",
        "front": "What are the categories, location, actions, and safety cautions for BL11 (Dazhu / 大杼)?",
        "back": "• Category: Hui-Meeting point of Bones; Sea of Blood point; Crossing of BL and SI.\n• Location: 1.5 cun lateral to the lower border of the spinous process of the 1st thoracic vertebra (T1).\n• Actions: Benefits bones and joints, expels exterior wind, descends Lung Qi.\n• Primary Indications: Bone pain, arthritis, rigid neck, early stage wind-cold invasion, fever, cough.\n• Needling: Oblique insertion toward the spine 0.5–0.8 cun. CAUTION: Medial/perpendicular or deep lateral insertion risks pneumothorax!",
        "consensus": "Universal consensus: Premier point for degenerative bone disorders, osteoporosis, and structural joint stiffness.",
        "variations": "Classical Ling Shu citation: One of the points of the Sea of Blood (with ST37, ST39).",
        "sources": '["CAM p. 128", "Deadman p. 265"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "BL17 (Geshu / 膈俞)",
        "front": "State the category, location, actions, and anatomical hazard for BL17 (Geshu / 膈俞).",
        "back": "• Category: Hui-Meeting point of Blood; Back-Shu point of the Diaphragm.\n• Location: 1.5 cun lateral to the lower border of the spinous process of T7 (level with inferior angle of scapula).\n• Actions: Invigorates blood, dispels blood stasis, cools blood heat, nourishes blood, harmonizes diaphragm.\n• Primary Indications: Chronic anemia, purpura, hemoptysis, epistaxis, angina, hiccups, belching, skin disorders.\n• Needling: Oblique insertion 0.5–0.8 cun toward the spine. CAUTION: Perpendicular deep insertion causes pneumothorax!",
        "consensus": "Universal consensus: Premier blood point in the entire acupuncture system. Key pair: BL17 + SP10 for all stubborn blood stasis.",
        "variations": "Maciocia notes BL17 tonifies blood when needle is supplemented/moxa, and invigorates blood when reduced.",
        "sources": '["CAM p. 130", "Deadman p. 277"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "BL52 (Zhishi / 志室)",
        "front": "What is the location, clinical meaning, and anatomical organ hazard for BL52 (Zhishi / 志室)?",
        "back": "• Location: On the lower back, 3 cun lateral to the lower border of the spinous process of L2 (level with BL23 Shenshu).\n• Name Meaning: 'Room of the Will' (Zhi = willpower of the Kidneys).\n• Actions: Tonifies Kidney essence, strengthens lumbar region, regulates urination, bolsters mental resolve/willpower.\n• Primary Indications: Low back pain, impotence, nocturnal emissions, edema, extreme fatigue, depression, lack of willpower.\n• Needling: Oblique insertion 0.5–1.0 cun. CAUTION: Deep perpendicular or lateral insertion can puncture the kidney parenchyma!",
        "consensus": "Consensus confirms outer Bladder line point corresponds to the spiritual-emotional aspect of the Kidney (Zhi).",
        "variations": "Deadman strictly warns that in thin individuals, the kidney lies directly beneath at a depth of less than 1.5 cun.",
        "sources": '["CAM p. 138", "Deadman p. 306"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "BL57 (Chengshan / 承山)",
        "front": "Detail the location, actions, and distal clinical indications for BL57 (Chengshan / 承山).",
        "back": "• Location: On the posterior lower leg, in the depression formed below the belly of the gastrocnemius muscle, midway between BL40 and the calcaneus (approx. 8 cun below BL40).\n• Actions: Relaxes sinews, activates channel, clears heat, treats hemorrhoids.\n• Primary Indications: Hemorrhoids, anal fissure, constipation, calf spasms/cramps, sciatica, heel pain.\n• Needling: Perpendicular insertion 1.0–2.0 cun.",
        "consensus": "Universal consensus: The primary distal point on the human body for hemorrhoids and anal disorders.",
        "variations": "Deadman notes pairing with Erbai (EX-UE2) and GV1 for bleeding or prolapsed hemorrhoids.",
        "sources": '["CAM p. 140", "Deadman p. 312"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "KI6 (Zhaohai / 照海)",
        "front": "What are the categories, confluent pairing, location, and actions for KI6 (Zhaohai / 照海)?",
        "back": "• Category: Confluent point of the Yin Qiao Mai (paired with LU7).\n• Location: 1 cun directly inferior to the prominence of the medial malleolus, in the groove between the lower border of malleolus and calcaneus.\n• Actions: Nourishes Kidney Yin, clears deficiency heat, calms Shen, benefits throat, regulates lower burner.\n• Primary Indications: Dry sore throat, chronic hoarseness, night sweats, insomnia (eyes stay open at night), irregular menses, constipation.\n• Needling: Perpendicular insertion 0.3–0.5 cun.",
        "consensus": "Universal consensus: Premier point to nourish Kidney Yin and soothe chronic yin-deficient throat and ocular dryness.",
        "variations": "CAM notes pairing with LU7 for Yin Qiao / Ren Mai combination treating chest, throat, and lung dryness.",
        "sources": '["CAM p. 147", "Deadman p. 343"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "KI7 (Fuliu / 复溜)",
        "front": "Explain the category, location, and the sweating regulation actions of KI7 (Fuliu / 复溜).",
        "back": "• Category: Jing-River (Metal point, Mother tonification point) of the Kidney channel.\n• Location: On the medial lower leg, 2 cun directly superior to KI3 (Taixi), on the anterior border of the Achilles tendon.\n• Actions: Tonifies Kidney Yang and Yin, regulates water pathways, regulates sweating.\n• Sweating Regulation: \n  - Spontaneous sweating (Qi/Yang deficiency): Tonify KI7, disperse LI4.\n  - Night sweating (Yin deficiency heat): Disperse LI4, tonify KI7, add HT6.\n• Needling: Perpendicular insertion 0.5–1.0 cun.",
        "consensus": "Universal consensus: Key point for treating pathological perspiration disorders and resolving lower limb edema.",
        "variations": "CAM emphasizes tonifying Kidney Yang for cold lower extremities and lumbar weakness.",
        "sources": '["CAM p. 148", "Deadman p. 346"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "PC3 (Quze / 曲泽)",
        "front": "State the category, location, actions, and emergency applications for PC3 (Quze / 曲泽).",
        "back": "• Category: He-Sea (Water point) of the Pericardium channel.\n• Location: On the cubital crease of the elbow, in the depression on the ulnar side of the biceps brachii tendon.\n• Actions: Clears summer-heat, cools blood, expels heat from Ying and Xue levels, stops vomiting.\n• Primary Indications: Heatstroke, acute gastroenteritis (vomiting and diarrhea in summer), febrile agitation, angina pectoris, trembling of arm.\n• Needling: Perpendicular insertion 0.8–1.2 cun, or prick to bleed with lancet. Caution: Avoid brachial artery and veins!",
        "consensus": "Universal consensus: Primary point for acute summer-heat collapse and acute toxic heat in blood level.",
        "variations": "CAM highlights pricking PC3 and BL40 to bleed for acute food poisoning with severe vomiting and diarrhea.",
        "sources": '["CAM p. 153", "Deadman p. 372"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "PC7 (Daling / 大陵)",
        "front": "Identify the categories, location, and clinical indications for PC7 (Daling / 大陵).",
        "back": "• Category: Shu-Stream, Yuan-Source, Earth (Son/Sedation) point of Pericardium; Ghost point (Sun Si-miao).\n• Location: At the midpoint of the wrist crease, between the tendons of palmaris longus and flexor carpi radialis.\n• Actions: Clears Heart Fire, calms Shen, harmonizes Stomach, treats carpal tunnel.\n• Primary Indications: Insomnia, manic-depressive behavior, foul breath (halitosis from Stomach Fire), chest oppression, carpal tunnel syndrome.\n• Needling: Perpendicular insertion 0.3–0.5 cun. Caution: Avoid median nerve!",
        "consensus": "Universal consensus: Premier point to extinguish Heart and Stomach Fire; sedation point for fire excess.",
        "variations": "Deadman notes prick-to-drain for severe psychotic mania.",
        "sources": '["CAM p. 156", "Deadman p. 378"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "SJ6 (Zhigou / 支沟)",
        "front": "Explain why SJ6 (Zhigou / 支沟) is considered the premier point for constipation and hypochondriac pain.",
        "back": "• Category: Jing-River (Fire point) of the San Jiao channel.\n• Location: On the dorsal forearm, 3 cun proximal to the wrist crease (SJ4), between radius and ulna.\n• Actions: Moves Qi in the San Jiao, clears heat, regulates bowels, relieves hypochondriac pain.\n• Core Applications:\n  1. Constipation: Classic empirical point for all types of constipation (paired with GB34 and ST25).\n  2. Hypochondriac Pain: Relieves Qi constraint in Liver/Gallbladder/San Jiao channels (intercostal neuralgia, shingles pain).\n• Needling: Perpendicular insertion 0.8–1.2 cun.",
        "consensus": "Universal consensus: Supreme point for moving constrained Qi in the Triple Burner and restoring bowel motility.",
        "variations": "CAM highlights immediate relief of herpes zoster intercostal neuralgia.",
        "sources": '["CAM p. 162", "Deadman p. 394"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "GB8 (Shuaigu / 率谷)",
        "front": "What is the location, crossing channel, and primary indication for GB8 (Shuaigu / 率谷)?",
        "back": "• Category: Crossing point of Gallbladder and Bladder channels.\n• Location: Superior to the apex of the auricle, 1.5 cun directly above the hairline.\n• Actions: Dispels wind, relieves pain, harmonizes Stomach and halts vomiting.\n• Primary Indications: Migraine, one-sided temporal headache, vertigo, nausea/vomiting accompanying headache, alcohol hangover.\n• Needling: Transverse insertion 0.5–1.0 cun posteriorly or anteriorly along scalp.",
        "consensus": "Key local point for Shaoyang temporal headache and post-intoxication cranial throbbing.",
        "variations": "CAM pairs GB8 with Taiyang and GB20 for acute cluster migraine.",
        "sources": '["CAM p. 170", "Deadman p. 420"]',
        "importance_level": 2
    },
    {
        "category": "Meridians and Points",
        "title": "GB39 (Xuanzhong / 悬钟)",
        "front": "State the category, location, actions, and stroke prevention role of GB39 (Xuanzhong / 悬钟).",
        "back": "• Category: Hui-Meeting point of Marrow.\n• Location: On the lateral lower leg, 3 cun superior to the tip of the lateral malleolus, in the depression between the posterior border of the fibula and the peroneus longus/brevis tendons.\n• Actions: Benefits essence and marrow, strengthens sinews and bones, dispels wind-damp, clears heat.\n• Primary Indications: Stiff neck (torticollis), wind-stroke prevention (moxa with ST36), hemiplegia, sciatica, dementia, leg pain.\n• Needling: Perpendicular insertion 1.0–1.5 cun.",
        "consensus": "Universal consensus: Essential point for marrow and bone nourishment, cervical spine stiffness, and preventative vascular health.",
        "variations": "Classical reference name is Juegu (绝骨).",
        "sources": '["CAM p. 182", "Deadman p. 454"]',
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "LV2 (Xingjian / 行间)",
        "front": "Detail the category, location, and Liver Fire clearing actions of LV2 (Xingjian / 行间).",
        "back": "• Category: Ying-Spring (Fire point, Son/Sedation point) of the Liver channel.\n• Location: On the dorsum of the foot, between the 1st and 2nd toes, proximal to the margin of the web at the junction of red and white skin.\n• Actions: Clears Liver Fire, sedates Liver Yang, cools blood, extinguishes wind.\n• Primary Indications: Severe headache, red burning eyes, irritability, sudden bouts of anger, bitter taste in mouth, menorrhagia, childhood convulsions.\n• Needling: Oblique insertion 0.5–0.8 cun directed proximally.",
        "consensus": "Universal consensus: The primary point to sedate flaring excess Liver Fire (Son point on Wood channel).",
        "variations": "Contrast with LV3: LV3 moves Liver Qi and tonifies Liver; LV2 aggressively purges Fire.",
        "sources": '["CAM p. 188", "Deadman p. 473"]',
        "importance_level": 1
    },

    # =========================================================================
    # 2. WESTERN MEDICINE (20 CARDS)
    # =========================================================================
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Hemoglobin A1c (HbA1c)",
        "front": "What are the clinical diagnostic thresholds for Hemoglobin A1c (HbA1c) and its clinical significance?",
        "back": "• Normal: < 5.7%\n• Prediabetes: 5.7% – 6.4%\n• Diabetes Mellitus: ≥ 6.5% (confirmed on repeat test)\n• Diabetic Target: Generally < 7.0% for non-pregnant adults.\n• Clinical Significance: Reflects average glycemic control over the preceding 2–3 months (lifespan of RBCs). In acupuncture, uncontrolled HbA1c (>8-9%) significantly increases the risk of delayed wound healing, peripheral neuropathy, and post-needling infection.",
        "consensus": "Gold-standard marker worldwide for diagnosing and monitoring long-term glycemic control.",
        "variations": "False lows occur in hemolytic anemia and recent blood transfusions; false highs occur in iron-deficiency anemia.",
        "sources": '["ADA Clinical Guidelines", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Lipid Panel & Cardiovascular Risk",
        "front": "What are the standard reference values and clinical implications of a fasting lipid panel?",
        "back": "• Total Cholesterol: Desirable < 200 mg/dL (< 5.2 mmol/L)\n• LDL Cholesterol (Bad): Optimal < 100 mg/dL (< 2.6 mmol/L); < 70 mg/dL in high-risk patients\n• HDL Cholesterol (Good): Protective > 40 mg/dL (> 1.0 mmol/L) for men, > 50 mg/dL (> 1.3 mmol/L) for women\n• Triglycerides: Normal < 150 mg/dL (< 1.7 mmol/L)\n• Clinical Relevance: High LDL and triglycerides drive atherosclerosis, coronary artery disease, stroke, and peripheral arterial disease. Triglycerides > 500 mg/dL trigger acute pancreatitis risk.",
        "consensus": "Atherosclerotic cardiovascular disease (ASCVD) risk calculators rely primarily on LDL, age, and blood pressure.",
        "variations": "Non-HDL cholesterol is increasingly utilized as a reliable secondary predictor in diabetic patients.",
        "sources": '["AHA/ACC Guidelines", "Harrison\'s IM"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Liver Function Tests (LFTs)",
        "front": "Compare ALT and AST, and explain the significance of the AST:ALT ratio.",
        "back": "• ALT (Alanine Aminotransferase): Highly liver-specific enzyme. Elevated in hepatocellular damage (hepatitis, fatty liver, toxins).\n• AST (Aspartate Aminotransferase): Found in liver, cardiac muscle, skeletal muscle, and kidneys.\n• AST:ALT Ratio:\n  - Ratio < 1 (ALT > AST): Characteristic of Non-Alcoholic Fatty Liver Disease (NAFLD) and viral hepatitis.\n  - Ratio > 2 (AST > ALT): Strongly suggestive of Alcoholic Liver Disease or cirrhosis.\n  - Massive elevation (>1,000 U/L): Indicates acute toxic necrosis (acetaminophen overdose), ischemic hepatitis, or acute viral hepatitis.",
        "consensus": "Standard hepatic panel components; ALT is the primary marker of acute liver injury.",
        "variations": "Elevated isolated AST with normal ALT suggests cardiac or skeletal muscle injury (rhabdomyolysis).",
        "sources": '["Harrison\'s IM", "Current Medical Diagnosis & Treatment"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Kidney Function (Creatinine & eGFR)",
        "front": "State normal reference ranges for Serum Creatinine and eGFR, and identify stages of Chronic Kidney Disease (CKD).",
        "back": "• Serum Creatinine: Adult Normal ~ 0.7 – 1.3 mg/dL (62 – 115 µmol/L).\n• eGFR (Estimated Glomerular Filtration Rate): Normal ≥ 90 mL/min/1.73m².\n• CKD Staging:\n  - Stage 1: eGFR ≥ 90 with kidney damage (proteinuria)\n  - Stage 2: eGFR 60–89 (mild decrease)\n  - Stage 3: eGFR 30–59 (moderate decrease)\n  - Stage 4: eGFR 15–29 (severe decrease)\n  - Stage 5: eGFR < 15 (Kidney Failure / End-Stage Renal Disease)\n• Acupuncture Safety: In advanced CKD, observe extreme caution regarding fluid retention, electrolyte imbalances, and bleeding risks.",
        "consensus": "eGFR calculation accounts for age, sex, and serum creatinine. Gold standard for evaluating renal clearance.",
        "variations": "Serum creatinine is influenced by muscle mass; amputees or bodybuilders may present misleading baselines.",
        "sources": '["KDIGO Guidelines", "Harrison\'s IM"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Thyroid Panel (TSH, Free T4)",
        "front": "Differentiate Primary Hypothyroidism from Primary Hyperthyroidism using lab values and clinical signs.",
        "back": "• Primary Hypothyroidism:\n  - Labs: Elevated TSH, Low Free T4 (FT4).\n  - Signs: Fatigue, cold intolerance, weight gain, constipation, dry skin, bradycardia, delayed deep tendon reflexes.\n• Primary Hyperthyroidism:\n  - Labs: Suppressed/Low TSH, Elevated Free T4 (FT4).\n  - Signs: Heat intolerance, weight loss despite increased appetite, tachycardia, palpitations, tremor, diarrhea, exophthalmos (Graves').\n• Subclinical Thyroid Disease: Abnormal TSH with normal Free T4.",
        "consensus": "TSH is the initial screening test of choice due to high sensitivity to minor changes in circulating thyroid hormones.",
        "variations": "Secondary/central hypothyroidism presents with low TSH and low FT4 (pituitary failure).",
        "sources": '["Harrison\'s IM", "Endocrine Society Guidelines"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Urinalysis Dipstick Interpretation",
        "front": "What are the clinical implications of Protein, Blood, Leukocyte Esterase, and Nitrites on a urine dipstick?",
        "back": "• Leukocyte Esterase & Nitrites: Positive indicates Bacterial Urinary Tract Infection (UTI). Gram-negative bacteria (E. coli) convert nitrates to nitrites.\n• Blood (Hematuria): Indicates urinary tract infection, nephrolithiasis (kidney stones), glomerulonephritis, or genitourinary malignancy.\n• Protein (Proteinuria): Persistent proteinuria indicates glomerular injury, diabetic nephropathy, preeclampsia in pregnancy, or nephrotic syndrome.\n• Glucose: Glycosuria indicates serum glucose exceeding renal threshold (~180 mg/dL), typical of uncontrolled diabetes.",
        "consensus": "Urinalysis is a fundamental, rapid screening tool for renal, urological, and metabolic disorders.",
        "variations": "Microscopic urinalysis is required to distinguish true red blood cells from free hemoglobin or myoglobin.",
        "sources": '["Current Medical Diagnosis & Treatment", "Harrison\'s IM"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Diagnostic Labs: Inflammatory Markers (ESR & CRP)",
        "front": "Compare ESR and CRP, and explain their utility in screening for systemic inflammatory emergencies.",
        "back": "• ESR (Erythrocyte Sedimentation Rate): Measures rate at which RBCs settle in anticoagulated blood over 1 hour. Slower to rise and slower to fall; influenced by age and red blood cell shape.\n• CRP (C-Reactive Protein): Acute-phase reactant synthesized by the liver. Rises and falls rapidly (within hours) in response to inflammation or infection.\n• Critical Emergency Utility: Massive elevations in ESR (>50–100 mm/hr) and CRP strongly support Giant Cell (Temporal) Arteritis, Polymyalgia Rheumatica, osteomyelitis, or severe systemic autoimmune flares.",
        "consensus": "Non-specific markers of systemic inflammation. Normal values rule against severe bacterial infection and active systemic vasculitis.",
        "variations": "High-sensitivity CRP (hs-CRP) is used specifically to stratify cardiovascular disease risk.",
        "sources": '["Harrison\'s IM", "UpToDate"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Giant Cell (Temporal) Arteritis",
        "front": "What are the hallmark signs, demographics, and immediate action required for Giant Cell Arteritis?",
        "back": "• Demographics: Adults > 50 years of age (typically > 70).\n• Hallmark Symptoms:\n  1. New-onset unilateral throbbing temporal headache.\n  2. Scalp tenderness (pain when combing hair).\n  3. Jaw claudication (fatigue/pain in jaw muscles while chewing).\n  4. Amaurosis fugax or sudden painless visual blurring/vision loss.\n• Immediate Action: Medical Emergency! Refer immediately to Emergency Department for systemic corticosteroid therapy. Untreated inflammation of the ophthalmic artery causes permanent, irreversible blindness!",
        "consensus": "Universal medical emergency consensus. Never attempt outpatient acupuncture while vision loss is threatened.",
        "variations": "Strongly associated with Polymyalgia Rheumatica (bilateral shoulder/pelvic girdle aching and morning stiffness).",
        "sources": '["Harrison\'s IM", "Emergency Medicine Guidelines"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Bacterial Meningitis",
        "front": "What is the classic clinical triad and physical exam maneuvers for acute Bacterial Meningitis?",
        "back": "• Classic Clinical Triad: High fever, altered mental status, and nuchal rigidity (stiff neck).\n• Pathognomonic Physical Signs:\n  1. Kernig's Sign: Patient supine, hip flexed 90°. Resistance or severe back/neck pain upon passive knee extension is positive.\n  2. Brudzinski's Sign: Passive forward flexion of patient's neck causes involuntary reflexive flexion of both hips and knees.\n• Immediate Action: Life-threatening emergency! Immediate 911 transfer for lumbar puncture and intravenous antibiotic therapy.",
        "consensus": "Critical emergency diagnosis. Petechial or purpuric rash indicates life-threatening meningococcemia.",
        "variations": "Elderly and infants may lack a high fever, presenting only with lethargy, hypothermia, or bulging fontanelle.",
        "sources": '["Harrison\'s IM", "CDC Guidelines"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Anaphylactic Shock",
        "front": "Describe the systemic presentation of Anaphylaxis and the immediate first-line medical intervention.",
        "back": "• Presentation: Acute, life-threatening multi-system IgE-mediated allergic reaction:\n  - Respiratory: Laryngeal edema, stridor, bronchospasm, severe wheezing, dyspnea.\n  - Cutaneous: Diffuse urticaria (hives), angioedema (swollen lips/tongue/eyelids), pruritus.\n  - Cardiovascular: Sudden hypotension, syncope, tachycardia, vascular collapse.\n• First-Line Treatment: Intramuscular (IM) Epinephrine 1:1,000 (0.3–0.5 mg in adults) injected into the anterolateral mid-thigh immediately! Call 911 without delay.",
        "consensus": "Epinephrine is the ONLY first-line medication; antihistamines and corticosteroids are secondary and must not delay epinephrine administration.",
        "variations": "Biphasic anaphylactic reactions can recur up to 8–12 hours later, requiring emergency room observation.",
        "sources": '["World Allergy Organization (WAO)", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Hypertensive Urgency vs Emergency",
        "front": "Differentiate Hypertensive Urgency from Hypertensive Emergency based on blood pressure criteria and end-organ damage.",
        "back": "• Blood Pressure Threshold: Systolic BP > 180 mmHg and/or Diastolic BP > 120 mmHg.\n• Hypertensive Urgency: Severely elevated BP WITHOUT evidence of acute end-organ damage. Treatment involves outpatient oral medication adjustment within 24–48 hours.\n• Hypertensive Emergency: Severely elevated BP WITH acute, life-threatening end-organ damage:\n  - Encephalopathy (confusion, seizures)\n  - Acute pulmonary edema (severe shortness of breath)\n  - Acute coronary syndrome / MI (chest pain)\n  - Aortic dissection (tearing back pain)\n  - Acute renal failure (hematuria, oliguria)\n• Action: Immediate 911 transfer for IV antihypertensive therapy.",
        "consensus": "The presence or absence of acute target-organ damage determines emergency vs urgency, not the absolute blood pressure number alone.",
        "variations": "Rapid lowering of blood pressure in urgency can cause cerebral ischemia; gradual control is mandated.",
        "sources": '["AHA/ACC Hypertension Guidelines", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Ectopic Pregnancy Triad",
        "front": "What is the classic clinical triad of Ectopic Pregnancy and why is it an emergency?",
        "back": "• Classic Clinical Triad: \n  1. Missed menstrual period (amenorrhea)\n  2. Acute severe unilateral lower pelvic/abdominal pain\n  3. Abnormal vaginal bleeding (spotting or hemorrhage)\n• Rupture Complications: Tubal rupture leads to massive intraperitoneal hemorrhage, referred shoulder pain (diaphragmatic irritation from hemoperitoneum), syncope, and hypovolemic shock.\n• Action: Immediate Emergency Department transfer for transvaginal ultrasound, serum quantitative beta-hCG, and surgical consultation.",
        "consensus": "Leading cause of first-trimester maternal mortality. Must be excluded in any woman of childbearing age presenting with pelvic pain.",
        "variations": "Pain may be diffuse or bilateral if substantial internal bleeding has accumulated in the peritoneal cavity.",
        "sources": '["ACOG Practice Bulletin", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Emergency Red Flag: Opioid Overdose Triad",
        "front": "Identify the Opioid Toxidrome Triad and the first-line emergency reversal protocol.",
        "back": "• Classic Triad: \n  1. Pinpoint pupils (miosis)\n  2. Respiratory depression (< 8–10 breaths/min or apnea)\n  3. Central nervous system depression (unconsciousness/coma)\n• Associated Signs: Cyanosis (blue lips/fingernails), snoring/gurgling respirations, bradycardia.\n• Emergency Protocol: Call 911 immediately. Administer Naloxone (Narcan) 4 mg intranasally or 0.4 mg IM. Initiate rescue breathing/CPR. Naloxone duration (30-90 min) is shorter than most opioids; patient must be monitored.",
        "consensus": "Worldwide standard of emergency response for opioid-induced respiratory arrest.",
        "variations": "Pupils may be normal or dilated if combined with stimulants, severe cerebral hypoxia, or certain synthetic opioids (meperidine).",
        "sources": '["SAMHSA Guidelines", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Physical Exam: Orthopedic Shoulder Impingement Tests",
        "front": "Demonstrate the execution and positive findings for Neer's Test and Hawkins-Kennedy Test.",
        "back": "• Neer's Impingement Test: Stabilize patient's scapula with one hand; with other hand, passively flex the fully pronated arm forward through maximum elevation. Pain indicates impingement of supraspinatus tendon against anterior-inferior acromion.\n• Hawkins-Kennedy Test: Flex patient's shoulder and elbow to 90°; support elbow and forcefully internally rotate the humerus. Pain indicates subacromial impingement / rotator cuff irritation.\n• Clinical Meaning: Both tests assess subacromial bursitis and supraspinatus tendinopathy.",
        "consensus": "Hawkins-Kennedy is considered more sensitive, while Neer's provides high specificity for subacromial pathology.",
        "variations": "Injecting lidocaine into subacromial space (Neer impingement test) completely relieves pain in true impingement.",
        "sources": '["Magee Orthopedic Physical Assessment", "AAOS"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Physical Exam: Rotator Cuff Tears (Drop Arm & Empty Can)",
        "front": "How are the Empty Can (Jobe's) Test and Drop Arm Test performed, and what do they diagnose?",
        "back": "• Jobe's Empty Can Test: Arms abducted to 90°, horizontally flexed 30° into scapular plane, fully internally rotated (thumbs pointing to floor). Examiner applies downward force while patient resists. Weakness or pain indicates supraspinatus tendon tear or tendinitis.\n• Drop Arm Test: Patient's arm passively abducted to 90°. Patient is instructed to slowly lower the arm to the side. Sudden dropping of the arm or inability to control descent from 90° to 60° indicates a full-thickness tear of the supraspinatus muscle.\n• Distinction: Drop Arm indicates full-thickness rupture; Empty Can detects tendinitis or partial tear.",
        "consensus": "Primary physical diagnostic maneuvers for rotator cuff integrity.",
        "variations": "Full-Can test (thumbs pointing up) is less provocative and frequently preferred in acute clinical pain.",
        "sources": '["Magee Orthopedic Physical Assessment", "AAOS"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Physical Exam: Knee Meniscal & Ligamentous Tests",
        "front": "Compare McMurray's Test, Lachman's Test, and Anterior Drawer Test.",
        "back": "• Lachman's Test: Knee flexed 20–30°. Examiner stabilizes femur with one hand and pulls tibia anteriorly with other hand. Increased anterior translation with soft/mushy end-feel indicates Anterior Cruciate Ligament (ACL) tear. Most sensitive test for ACL!\n• Anterior Drawer Test: Knee flexed 90°, foot stabilized. Forward pulling of tibia tests ACL integrity; less sensitive due to hamstring guarding.\n• McMurray's Test: Knee fully flexed. Examiner rotates tibia internally (tests lateral meniscus) or externally (tests medial meniscus) while extending the knee with varus/valgus stress. Palpable click or joint-line pain confirms meniscal tear.",
        "consensus": "Lachman test is superior to Anterior Drawer for acute ACL injuries due to minimal joint effusion interference at 30° flexion.",
        "variations": "Apley's compression and distraction test differentiates ligamentous vs meniscal injury in prone position.",
        "sources": '["Magee Orthopedic Physical Assessment", "AAOS"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Physical Exam: De Quervain's Tenosynovitis (Finkelstein's)",
        "front": "Describe Finkelstein's Test, the involved anatomical tendons, and clinical presentation.",
        "back": "• Procedure: Patient flexes thumb into the palm and closes the four fingers over the thumb into a fist. The examiner passively ulnar-deviates the patient's wrist.\n• Positive Finding: Sharp, excruciating pain over the radial styloid process.\n• Anatomical Structures Involved: Stenosing tenosynovitis of the 1st dorsal compartment of the wrist:\n  1. Abductor Pollicis Longus (APL) tendon\n  2. Extensor Pollicis Brevis (EPB) tendon\n• Demographics: Common in postpartum mothers ('new mother's wrist' from lifting infant) and repetitive smartphone/typing users.",
        "consensus": "Pathognomonic test for De Quervain's tenosynovitis. Must be distinguished from thumb carpometacarpal (CMC) arthritis.",
        "variations": "Eichhoff's test is the original name; modern modified Finkelstein involves gentle longitudinal traction with ulnar deviation.",
        "sources": '["Magee Orthopedic Physical Assessment", "AAOS"]',
        "importance_level": 2
    },
    {
        "category": "Western Medicine",
        "title": "Physical Exam: Upper Motor Neuron vs Lower Motor Neuron",
        "front": "Construct a comparison table differentiating Upper Motor Neuron (UMN) lesions from Lower Motor Neuron (LMN) lesions.",
        "back": "• Weakness: Present in both UMN and LMN lesions.\n• Deep Tendon Reflexes (DTR): \n  - UMN: Hyperreflexia (3+ or 4+), clonus\n  - LMN: Hyporeflexia or areflexia (0 or 1+)\n• Muscle Tone:\n  - UMN: Spasticity, hypertonia, 'clasp-knife' rigidity\n  - LMN: Flaccidity, hypotonia\n• Muscle Bulk / Atrophy:\n  - UMN: Disuse atrophy only (late, minimal)\n  - LMN: Severe, rapid neurogenic muscle wasting\n• Fasciculations:\n  - UMN: Absent\n  - LMN: Present (muscle twitches)\n• Pathological Reflexes:\n  - UMN: Positive Babinski sign (great toe extends, toes fan out), positive Hoffman sign\n  - LMN: Negative Babinski (normal plantar flexion)",
        "consensus": "Foundational neurological distinction tested on all medical and licensing board exams.",
        "variations": "Acute UMN shock (initial phase of stroke/spinal trauma) can transiently present with flaccidity before spasticity develops.",
        "sources": '["Harrison\'s IM", "Bickley Bates\' Guide to Physical Examination"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Anticoagulants vs Antiplatelets",
        "front": "Compare Anticoagulants and Antiplatelets, and explain clinical management in acupuncture practice.",
        "back": "• Antiplatelets: Aspirin, Clopidogrel (Plavix). Inhibit platelet aggregation; commonly prescribed for post-stent, stroke, and arterial clot prevention.\n• Anticoagulants: Warfarin (Coumadin, requires INR monitoring), Direct Oral Anticoagulants / DOACs (Apixaban/Eliquis, Rivaroxaban/Xarelto). Inhibit clotting factor cascade; prescribed for DVT/PE and atrial fibrillation.\n• Acupuncture Clinical Management:\n  1. Routine acupuncture is generally safe with fine gauge needles (36–40 gauge).\n  2. STRICTLY CONTRAINDICATED: Bloodletting/pricking therapy, deep intramuscular needling into non-compressible sites, aggressive gouging/manipulation.\n  3. Apply firm, prolonged direct pressure (1–2 minutes) upon needle withdrawal to avoid hematoma formation.",
        "consensus": "Universal CNT and acupuncture safety consensus. DOACs produce sudden, difficult-to-reverse bleeding.",
        "variations": "INR > 3.5 in Warfarin patients warrants extreme caution and referral for medical dose adjustment.",
        "sources": '["CNT Manual 7th Edition", "Goodman & Gilman\'s Pharmacology"]',
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Systemic Corticosteroids Adverse Effects",
        "front": "List the major long-term adverse effects of Systemic Corticosteroids (Prednisone) relevant to acupuncture.",
        "back": "• Musculoskeletal Risks: \n  - Accelerated Osteoporosis and pathological fractures (ribs, vertebrae).\n  - Avascular Necrosis (Osteonecrosis) of the femoral head (unexplained hip/groin pain).\n  - Muscle wasting and severe tendon vulnerability/rupture (especially Achilles and patellar tendons).\n• Dermatological & Infection: Thin fragile skin ('tissue paper skin'), easy bruising/hematomas, delayed wound healing, immunosuppression masking infection.\n• Endocrine: Adrenal suppression, Cushingoid features ('moon face', 'buffalo hump'), hyperglycemia/steroid-induced diabetes.\n• Acupuncture Caution: Use gentle shallow needling, avoid heavy electroacupuncture or forceful mobilization, maintain strict asepsis.",
        "consensus": "Crucial pharmacology knowledge for licensed practitioners managing chronic pain and autoimmune patients.",
        "variations": "Rapid cessation of chronic steroids causes acute life-threatening Addisonian adrenal crisis.",
        "sources": '["Goodman & Gilman\'s Pharmacology", "Harrison\'s IM"]',
        "importance_level": 1
    },

    # =========================================================================
    # 3. DIAGNOSIS (16 CARDS)
    # =========================================================================
    {
        "category": "Diagnosis",
        "title": "Tongue Body: Geographic Tongue vs Peeled Tongue",
        "front": "Differentiate Geographic Tongue from a Completely Peeled (Mirror) Tongue in etiology and clinical severity.",
        "back": "• Geographic Tongue (Map Tongue):\n  - Appearance: Tongue coating peeled in patches with defined borders that change location over days.\n  - Etiology: Stomach Yin deficiency with minor Qi stagnation; in children, often indicates allergic diathesis or food intolerance.\n• Completely Peeled / Mirror Tongue (Guang Bo She):\n  - Appearance: Complete absence of coating across the entire tongue body; surface appears glossy, shiny, and smooth like a mirror.\n  - Etiology: Severe, critical exhaustion of both Stomach Yin and Kidney Yin; body fluids are dangerously depleted.\n• Clinical Severity: Mirror tongue indicates profound constitutional yin deficiency requiring urgent fluid-nourishing therapy.",
        "consensus": "Universal diagnostic consensus across Maciocia and CAM.",
        "variations": "A peeled tongue with red body indicates severe Yin deficiency fire; a peeled pale tongue indicates exhaustion of both Qi and Blood.",
        "sources": '["Maciocia Diagnosis p. 112", "CAM p. 48"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Coating: Black Coat Differential",
        "front": "Explain the contradictory diagnostic meanings of a Black Dry Tongue Coat versus a Black Wet Tongue Coat.",
        "back": "• Black Dry / Hairy Tongue Coating:\n  - Etiology: Extreme Interior Heat burning body fluids to ashes.\n  - Accompanying Signs: High fever, delirium, dry feces, thirst for cold water, surging rapid pulse.\n• Black Wet / Slippery Tongue Coating:\n  - Etiology: Extreme Interior Cold with severe accumulation of Dampness and Yang collapse.\n  - Accompanying Signs: Cold limbs, loose watery stools, aversion to cold, deep slow weak pulse.\n• Core Diagnostic Principle: Always evaluate MOISTURE (dry vs wet) before determining whether a dark coat represents extreme heat or extreme cold!",
        "consensus": "Foundational tongue diagnostic paradox tested frequently on TCM board examinations.",
        "variations": "Bismuth medication (Pepto-Bismol) can artificially stain the tongue coating black.",
        "sources": '["Maciocia Tongue Diagnosis p. 145", "CAM p. 49"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Body: Deviated Tongue Clinical Meaning",
        "front": "What does a Deviated Tongue signify and what is its emergency significance?",
        "back": "• Manifestation: Tongue veers significantly to one side when protruded from the mouth.\n• Etiology: Internal Wind obstructing the collaterals, typically originating from Liver Yang rising or Phlegm-Fire.\n• Clinical Significance: \n  1. High predictive marker for impending Wind-Stroke (cerebrovascular accident / TIA).\n  2. Classic physical sequela of completed stroke (hemiplegia).\n• Emergency Action: If acute and accompanied by facial droop, arm weakness, or slurred speech, execute the FAST protocol and transfer to emergency care immediately!",
        "consensus": "Universal consensus across all diagnostic texts: A deviated tongue is a primary physical sign of internal wind in the cerebral vasculature.",
        "variations": "Must be distinguished from a tongue deviated due to dental structural missing teeth or congenital deviation.",
        "sources": '["Maciocia Tongue Diagnosis p. 78", "CAM p. 47"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Body: Tongue Prickles and Spots (Mang Ci)",
        "front": "Describe the diagnostic meaning and organ mapping of Red Prickles and Spots (Mang Ci) on the tongue.",
        "back": "• Appearance: Elevated red, dark, or thorny papillae protruding through or above the tongue coating.\n• Pathology: Indicates Heat in the Ying (Nutritive) or Xue (Blood) level, or extreme organ heat hyperfunction.\n• Topographical Organ Mapping:\n  - Tip: Flaring Heart Fire (insomnia, agitation, mouth ulcers)\n  - Sides: Liver or Gallbladder Fire (headache, bitter taste, anger)\n  - Center: Stomach Fire or Intestinal Heat (foul breath, constipation)\n  - Root: Lower Jiao Heat (urinary tract infection, pelvic inflammatory disease)",
        "consensus": "Classic diagnostic indicator of active heat toxin and capillary hypercongestion.",
        "variations": "Dark purple spots indicate blood stasis rather than active heat prickles.",
        "sources": '["Maciocia Tongue Diagnosis p. 95", "CAM p. 48"]',
        "importance_level": 2
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Hollow Pulse (Kou Mai)",
        "front": "What is the sensation, physical characteristic, and diagnostic meaning of a Hollow Pulse (Kou Mai)?",
        "back": "• Tactile Sensation: Felt floating, large, and soft on superficial touch, but hollow and empty in the center under moderate pressure, resembling a scallion or green onion stalk.\n• Pathology: Loss of Blood (hemorrhage) or severe loss of Yin fluids.\n• Clinical Indications: Massive postpartum hemorrhage, bleeding peptic ulcer, acute hemoptysis, severe fluid depletion from severe vomiting/diarrhea.\n• Mechanism: The vessel walls are expanded by floating Yang, while the internal volume of blood is severely depleted.",
        "consensus": "Classic 28 pulse quality indicating acute, catastrophic blood loss.",
        "variations": "Must be distinguished from Leather pulse, which is tight and hard on the exterior like a drumskin.",
        "sources": '["Maciocia Pulse Diagnosis p. 118", "CAM p. 52"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Leather / Drumskin Pulse (Ge Mai)",
        "front": "Describe the sensation and clinical meaning of a Leather Pulse (Ge Mai).",
        "back": "• Tactile Sensation: Felt hard, tight, and stretched superficially under the fingers like the taught leather surface of a drum, but completely empty and hollow upon deeper pressure.\n• Pathology: Severe depletion of Essence (*Jing*) and Blood, with unanchored Yang floating outward.\n• Clinical Indications: Miscarriage, massive continuous menorrhagia (flooding), chronic spermatorrhea, profound kidney essence exhaustion.",
        "consensus": "Consensus across Deadman, Maciocia, and CAM: Combines qualities of a Floating, Tight, and Empty pulse.",
        "variations": "Differentiated from Wiry pulse, which remains firm and solid into deep levels of palpation.",
        "sources": '["Maciocia Pulse Diagnosis p. 122", "CAM p. 53"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Hidden Pulse (Fu Mai)",
        "front": "State the depth, sensation, and diagnostic significance of a Hidden Pulse (Fu Mai).",
        "back": "• Tactile Sensation: Felt even deeper than a Deep (Chen) pulse; barely discernible until fingers press heavily against the periosteum of the radial bone.\n• Pathology: Severe Interior Cold, extreme acute pain, Syncope, or Yang collapse.\n• Clinical Indications: Cold accumulation in intestines, severe biliary colic, shock, hernia pain.\n• Clinical Note: If a hidden pulse has strength at bone level, it indicates excess interior cold/stasis; if completely weak and thready, it indicates impending Yang collapse.",
        "consensus": "A deep, hidden quality reflecting profound inward constraint of Yang Qi.",
        "variations": "Contrast with Weak (Ruo) pulse which is soft and deep without bone-level tightness.",
        "sources": '["Maciocia Pulse Diagnosis p. 88", "CAM p. 53"]',
        "importance_level": 2
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Moving / Stirred Pulse (Dong Mai)",
        "front": "Explain the unique characteristics and indications of a Moving Pulse (Dong Mai).",
        "back": "• Tactile Sensation: Short, round, slippery, rapid, and forceful; pulses like a vibrating, spinning bean without defined head or tail; often felt primarily in the Guan (middle) position.\n• Core Pathology: Conflict between Yin and Yang, intense acute pain, or sudden severe emotional fright and shock.\n• Indications: Acute heart pain, acute trauma/fracture pain, pediatric fright convulsions, severe panic attack.",
        "consensus": "Classic diagnostic description: 'Short, slippery, rapid, and bouncing like a bean under the finger.'",
        "variations": "Often recorded in pregnancy or during intense emotional shock in clinical gynecology.",
        "sources": '["Maciocia Pulse Diagnosis p. 132", "CAM p. 53"]',
        "importance_level": 2
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Scattered Pulse (San Mai)",
        "front": "What does a Scattered Pulse (San Mai) feel like and what does it portend clinically?",
        "back": "• Tactile Sensation: Diffuse, broken, chaotic, and irregular beats felt floating superficially; disappears completely with moderate or deep pressure; lacks distinct boundary.\n• Pathology: Critical exhaustion of Original Qi (Yuan Qi) and dispersal of Zang-Fu essence.\n• Prognostic Meaning: Highly ominous pulse indicating severe constitutional collapse, terminal illness, or impending heart failure.",
        "consensus": "Consensus regards Scattered pulse as a classic 'True Organ' (Zhen Zang) sign of vital exhaustion.",
        "variations": "Distinguished from Knotted or Intermittent pulse which retain distinct pulse volume between missed beats.",
        "sources": '["Maciocia Pulse Diagnosis p. 135", "CAM p. 53"]',
        "importance_level": 2
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu Pattern: Heart and Kidney Disharmony (*Xin Shen Bu Jiao*)",
        "front": "Detail the pathophysiology, cardinal symptoms, tongue, and pulse of Heart and Kidney Disharmony.",
        "back": "• Pathophysiology: Kidney Yin fails to ascend and cool the Heart; uncontrolled Heart Fire flares upward.\n• Cardinal Symptoms:\n  1. Insomnia with severe difficulty falling asleep, dream-disturbed sleep.\n  2. Palpitations, mental restlessness, anxiety, poor memory.\n  3. Lower back soreness, nocturnal emissions with erotic dreams, dry throat, night sweats.\n• Tongue: Red body, especially tipped red, with scanty or completely peeled coating.\n• Pulse: Thready and rapid (Xi Shuo), or deep weak in Chi position and floating rapid in Cun position.",
        "consensus": "One of the most frequently tested patterns on TCM licensing board examinations.",
        "variations": "Treatment principle: Nourish Kidney Yin, sedate Heart Fire, harmonize Heart and Kidney (e.g., Huang Lian E Jiao Tang).",
        "sources": '["Maciocia Foundations p. 642", "CAM p. 280"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu Pattern: Spleen and Kidney Yang Deficiency (*Pi Shen Yang Xu*)",
        "front": "What are the hallmark symptoms, tongue, and pulse of Spleen and Kidney Yang Deficiency?",
        "back": "• Pathophysiology: Failure of Mingmen Fire to warm Spleen Earth, leading to digestive collapse and cold fluid accumulation.\n• Cardinal Symptoms:\n  1. Dawn Diarrhea / Cock-crow Diarrhea (*Wu Geng Xie*): Urgency and watery diarrhea right before dawn (5 AM).\n  2. Severe cold limbs, cold aching lower back and knees, abdominal cold pain relieved by warmth/pressure.\n  3. Pitting edema of the lower extremities, clear profuse urination, exhaustion.\n• Tongue: Pale, swollen, moist body with scalloped teeth marks and thin white coat.\n• Pulse: Deep, slow, and weak (Chen Chi Ruo), especially faint in both Chi positions.",
        "consensus": "Classic systemic cold-deficiency pattern responsible for chronic geriatric diarrhea and intractable fatigue.",
        "variations": "Prescription formula: Si Shen Wan (Four Miracle Pill) + Li Zhong Wan.",
        "sources": '["Maciocia Foundations p. 638", "CAM p. 284"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu Pattern: Liver Fire Insulting the Lung (*Mu Huo Xing Jin*)",
        "front": "Explain the Five Phase dynamic, symptoms, tongue, and pulse of Liver Fire Insulting the Lung.",
        "back": "• Five Phase Dynamic: Wood Insulting Metal (counter-restriction / *Fan Wu*). Intense Liver Fire burns upward, drying and scorching Lung Metal.\n• Cardinal Symptoms:\n  1. Paroxysmal, violent, barking cough triggered or worsened by anger/emotional stress.\n  2. Hemoptysis (blood-streaked sputum), chest and hypochondriac distension and stabbing pain.\n  3. Bitter taste in mouth, red face, bloodshot eyes, extreme irritability.\n• Tongue: Red body with yellow coating, especially red along the lateral margins.\n• Pulse: Wiry and rapid (Xian Shuo).",
        "consensus": "Classic demonstration of five phase counter-restriction in clinical chest pathology.",
        "variations": "Treatment principle: Clear Liver Fire, descend Lung Qi, cool blood (e.g., Dai Ge San).",
        "sources": '["Maciocia Foundations p. 625", "CAM p. 278"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Zang-Fu Pattern: Phlegm Misting the Mind vs Phlegm-Fire Harassing",
        "front": "Contrast Phlegm Misting the Mind with Phlegm-Fire Harassing the Heart in manifestations and pulse.",
        "back": "• Phlegm Misting the Mind (Yin Phlegm):\n  - Symptoms: Stupor, confusion, lethargy, incoherent mumbling, rattling in throat, withdrawal, vacant stare, coma.\n  - Tongue: Pale or normal, thick white greasy coat.\n  - Pulse: Slippery and slow (Hua Chi) or soggy.\n• Phlegm-Fire Harassing the Heart (Yang Phlegm):\n  - Symptoms: Violent agitation, manic behavior, uncontrolled shouting, laughing and crying alternately, insomnia, hallucinations.\n  - Tongue: Red body, thick sticky yellow greasy coat.\n  - Pulse: Slippery and rapid (Hua Shuo), or wiry-rapid.",
        "consensus": "Critical psychiatric differential in Chinese Medicine: Yin withdrawal (Dian) vs Yang mania (Kuang).",
        "variations": "Phlegm Misting uses warm aromatic opening herbs (Su He Xiang Wan); Phlegm-Fire uses cold draining herbs (Meng Shi Gun Tan Wan).",
        "sources": '["Maciocia Foundations p. 648", "CAM p. 282"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Six Stages: Yangming Channel (*Jing*) vs Yangming Organ (*Fu*)",
        "front": "Compare the Four Bigs of Yangming Channel Syndrome with the Four Bowel Signs of Yangming Organ Syndrome.",
        "back": "• Yangming Channel Syndrome (*Yangming Jing Zheng*):\n  - Hallmark: The Four Bigs (*Si Da*):\n    1. Big Fever (high burning heat, no aversion to cold)\n    2. Big Thirst (intense craving for cold drinks)\n    3. Big Sweat (profuse continuous perspiration)\n    4. Big Pulse (surging, flooding, rapid - Hong Shuo)\n  - Classic Formula: Bai Hu Tang (White Tiger Decoction).\n• Yangming Organ Syndrome (*Yangming Fu Zheng*):\n  - Hallmark: Intestinal heat accumulation:\n    1. Tidal fever (spiking 3–5 PM)\n    2. Severe constipation with dry hard impacted stools\n    3. Abdominal fullness, distension, and severe pain worse with pressure\n    4. Dry yellow or burnt black prickly coating; Deep, forceful, rapid pulse (Chen Shi Shuo)\n  - Classic Formula: Da Cheng Qi Tang.",
        "consensus": "Cornerstone Shanghan Lun diagnostic distinction tested rigorously on board exams.",
        "variations": "Channel pattern has heat dispersed in the exterior; Organ pattern has heat bound with stool in the intestines.",
        "sources": '["Shanghan Lun", "Maciocia Foundations p. 710"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Six Stages: Shaoyang Syndrome Hallmark Presentation",
        "front": "What are the hallmark signs, pulse, and classic formula for Shaoyang Syndrome?",
        "back": "• Category: The Half-Exterior, Half-Interior stage of Shanghan Lun.\n• Cardinal Symptoms:\n  1. Alternating chills and fever (*Wang Lai Han Re*).\n  2. Bitter taste in mouth (*Kou Ku*).\n  3. Dry throat (*Yan Gan*).\n  4. Blurred vision / Dizziness (*Mu Xuan*).\n  5. Hypochondriac and chest fullness/pain (*Xiong Xie Ku Man*).\n  6. Lack of appetite, nausea, vomiting.\n• Pulse: Wiry pulse (Xian Mai).\n• Tongue: Thin white coat or unilateral coating.\n• Classic Formula: Xiao Chai Hu Tang (Minor Bupleurum Decoction).",
        "consensus": "Universal consensus across all diagnostic and herbal curricula.",
        "variations": "Sweating, purging, or vomiting are strictly contraindicated in Shaoyang; harmonizing is the sole correct strategy.",
        "sources": '["Shanghan Lun", "CAM p. 296"]',
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Four Levels: Ying Level vs Xue Level Differentiation",
        "front": "How do you distinguish Ying (Nutritive) level pathology from Xue (Blood) level pathology in Wenbing theory?",
        "back": "• Ying (Nutritive) Level:\n  - Symptoms: Fever worse at night, severe insomnia, mental delirium, faint/indistinct purple skin macules, dry mouth with little desire to drink.\n  - Tongue: Deep red/crimson body with stripped coat.\n  - Pulse: Thready and rapid (Xi Shuo).\n• Xue (Blood) Level:\n  - Symptoms: High fever, violent delirium, convulsions, profuse bright or dark bleeding from all orifices (hematemesis, epistaxis, hematuria, bloody stools), extensive vivid purpura/petechiae.\n  - Tongue: Deep crimson or purple, dry, trembling.\n  - Pulse: Wiry-rapid or hollow-rapid.\n• Key Distinction: Xue level is marked by overt, life-threatening hemorrhage, internal wind (convulsions), and blood consumption.",
        "consensus": "Foundational Wenbing warm-disease progression stages representing extreme depth of toxic heat.",
        "variations": "Xue level heat easily generates internal wind and consumptive tremors.",
        "sources": '["Wenbing Tiao Bian", "Maciocia Foundations p. 730"]',
        "importance_level": 1
    },

    # =========================================================================
    # 4. ILLNESS & CLINICAL SYNDROMES (16 CARDS)
    # =========================================================================
    {
        "category": "Illness",
        "title": "Headache by Meridian: Vertex Headache (*Jueyin*)",
        "front": "Identify the channel, etiology, and primary acupoints for a Vertex Headache.",
        "back": "• Channel: Jueyin (Liver channel - which ascends across vertex to DU20).\n• Etiology: Liver Yang rising, Liver Blood deficiency, or Jueyin Cold.\n• Symptoms: Throbbing, pulling, or freezing pain localized strictly at the crown of the head (vertex); often accompanied by dry heaving or acid regurgitation.\n• Primary Acupoints:\n  - Distal: LV3 (Taichong), LV2 (Xingjian)\n  - Local: DU20 (Baihui), Sishencong (EX-HN1)\n  - Adjunct: PC6 (Neiguan) to harmonize Jueyin and stop nausea.",
        "consensus": "Classic meridian-based headache differentiation in Chinese clinical acupuncture.",
        "variations": "CAM notes using moxa on DU20 if the vertex headache is caused by interior cold stagnation.",
        "sources": '["CAM p. 302", "Deadman p. 488"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Headache by Meridian: Frontal Headache (*Yangming*)",
        "front": "State the channel, etiology, and point prescription for a Frontal Headache.",
        "back": "• Channel: Yangming (Stomach and Large Intestine channels).\n• Etiology: Stomach Fire, Food Stagnation, or Exterior Wind-Heat.\n• Symptoms: Severe throbbing forehead pain, pain over eyebrows and frontal sinus, pain radiating to root of nose and eyes.\n• Primary Acupoints:\n  - Distal: ST44 (Neiting), LI4 (Hegu), ST36 (Zusanli)\n  - Local: Yintang (EX-HN3), ST8 (Touwei), GB14 (Yangbai), BL2 (Zanzhu).",
        "consensus": "Universal consensus across board curricula: Frontal pain is governed by Yangming channel.",
        "variations": "If accompanied by thick foul nasal discharge (sinusitis), add LI20 and Bitong.",
        "sources": '["CAM p. 302", "Maciocia Practice p. 18"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Headache by Meridian: Temporal Headache (*Shaoyang*)",
        "front": "Explain the channel, etiology, and points for a One-Sided / Temporal Headache.",
        "back": "• Channel: Shaoyang (Gallbladder and San Jiao channels).\n• Etiology: Liver and Gallbladder Yang rising, Liver Fire, or Shaoyang Exterior Wind.\n• Symptoms: Throbbing pain localized to one temple or hemisphere of the head, radiating around ear and jaw, accompanied by irritability and bitter taste.\n• Primary Acupoints:\n  - Distal: GB41 (Zulinqi), SJ5 (Waiguan), LV3 (Taichong)\n  - Local: Taiyang (EX-HN5), GB8 (Shuaigu), GB20 (Fengchi).",
        "consensus": "Classic migraine presentation in TCM; represents the vast majority of stress-related unilateral headaches.",
        "variations": "Deadman notes prick-to-bleed Taiyang with lancet for acute refractory migraine.",
        "sources": '["CAM p. 303", "Maciocia Practice p. 21"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Headache by Meridian: Occipital Headache (*Taiyang*)",
        "front": "Detail the channel, symptoms, and primary acupoints for an Occipital Headache.",
        "back": "• Channel: Taiyang (Bladder and Small Intestine channels).\n• Etiology: Exterior Wind-Cold invasion, or Kidney Deficiency.\n• Symptoms: Pain at the base of the skull, radiating down the nape of the neck and upper back, stiffness and restricted cervical rotation.\n• Primary Acupoints:\n  - Distal: BL60 (Kunlun), SI3 (Houxi), BL65 (Shugu)\n  - Local: BL10 (Tianzhu), DU14 (Dazhui), GB20 (Fengchi), DU16 (Fengfu).",
        "consensus": "Universal consensus: Occipital neck tension and headache is mapped directly to the Taiyang channel.",
        "variations": "If exterior wind-cold, add cupping over upper back and moxa on BL10.",
        "sources": '["CAM p. 303", "Maciocia Practice p. 24"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Neurological Syndrome: Trigeminal Neuralgia (*Mian Tong*)",
        "front": "What is the clinical presentation and acupuncture point protocol for Trigeminal Neuralgia?",
        "back": "• Clinical Presentation: Excruciating, lancinating, electric-shock paroxysmal facial pain triggered by touch, chewing, speaking, or cold wind along branches of CN V (Ophthalmic V1, Maxillary V2, Mandibular V3).\n• Etiology: Wind-Fire in Shaoyang/Yangming, or Stomach Fire.\n• Acupuncture Protocol:\n  - Branch 1 (Ophthalmic): BL2, GB14, Taiyang, Yintang\n  - Branch 2 (Maxillary): ST2, SI18, LI20\n  - Branch 3 (Mandibular): ST6, ST7, REN24, Jiachengjiang\n  - Distal Points: LI4, ST44, LV3, SJ5.\n• Technique: Gentle needling at local trigger zones; vigorous reduction distally.",
        "consensus": "Acupuncture provides high efficacy for trigeminal neuralgia; local needles must be inserted without violent pecking to avoid triggering spasms.",
        "variations": "CAM emphasizes avoiding needle retention directly inside acute hypersensitive trigger zones.",
        "sources": '["CAM p. 308", "Deadman p. 110"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Musculoskeletal Syndrome: TMJ Dysfunction",
        "front": "Identify the primary local and distal acupoint protocol for Temporomandibular Joint (TMJ) Dysfunction.",
        "back": "• Presentation: Pain and tenderness in jaw joint, clicking or popping during mastication, restricted jaw opening, bruxism/teeth grinding.\n• Channel Anatomy: Traversed by Stomach, Small Intestine, and Gallbladder channels.\n• Primary Acupoints:\n  - Local: ST7 (Xiaguan - anterior to condyloid process), SI19 (Tinggong - with mouth open), GB2 (Tinghui), ST6 (Jiache - in masseter belly)\n  - Ah Shi: Direct trigger point needling of masseter and temporalis muscles\n  - Distal: LI4 (Hegu), ST44 (Neiting), SJ5 (Waiguan).",
        "consensus": "Highly effective local acupuncture protocol targeting pterygoid, masseter, and temporalis spasm.",
        "variations": "Deadman notes pairing with Ashi points along the tender posterior cervical spine.",
        "sources": '["CAM p. 312", "Deadman p. 136"]',
        "importance_level": 2
    },
    {
        "category": "Illness",
        "title": "Musculoskeletal Syndrome: Lateral vs Medial Epicondylitis",
        "front": "Compare Lateral Epicondylitis (Tennis Elbow) and Medial Epicondylitis (Golfer's Elbow) in anatomy and point selection.",
        "back": "• Lateral Epicondylitis (Tennis Elbow):\n  - Pathology: Tendinopathy of extensor carpi radialis brevis origin at lateral epicondyle.\n  - Provocation: Pain with resisted wrist extension.\n  - Points: LI11 (Quchi), LI10 (Shousanli), LU5 (Chize), Ah Shi.\n• Medial Epicondylitis (Golfer's Elbow):\n  - Pathology: Tendinopathy of common flexor tendon origin at medial epicondyle.\n  - Provocation: Pain with resisted wrist flexion and pronation.\n  - Points: HT3 (Shaohai), SI8 (Xiaohai), PC3 (Quze), Ah Shi.",
        "consensus": "Standard orthopedic and clinical acupuncture protocol for chronic elbow overuse syndromes.",
        "variations": "Moxibustion (especially direct sparrow-pecking moxa) on Ah Shi points is highly recommended by CAM.",
        "sources": '["CAM p. 434", "Magee Orthopedic Assessment"]',
        "importance_level": 2
    },
    {
        "category": "Illness",
        "title": "Gastrointestinal: Acid Regurgitation & GERD (*Tun Suan*)",
        "front": "Differentiate Liver invading Stomach from Stomach Heat in GERD, and list key points.",
        "back": "• Liver Invading Stomach (Wood Overacting on Earth):\n  - Symptoms: Acid reflux triggered by anger/stress, frequent emotional belching, hypochondriac pain, irritability; wiry pulse.\n  - Formula/Points: LV14 (Qimen), LV3 (Taichong), REN12 (Zhongwan), PC6 (Neiguan).\n• Stomach Heat (Fire in Middle Burner):\n  - Symptoms: Sour acid regurgitation, burning epigastric pain, bad breath, intense thirst for cold water, constipation; red tongue with yellow coat, slippery-rapid pulse.\n  - Formula/Points: ST44 (Neiting), ST25 (Tianshu), REN12 (Zhongwan), ST36 (Zusanli).\n• Core Master Pair: PC6 (Neiguan) + ST36 (Zusanli) descends rebellious Stomach Qi in both patterns.",
        "consensus": "Universal consensus: PC6 and REN12 are mandatory in any pattern of gastroesophageal acid reflux.",
        "variations": "CAM notes adding SP4 as confluent pair with PC6 to regulate the Chong Mai.",
        "sources": '["CAM p. 320", "Maciocia Practice p. 340"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Gastrointestinal: Cholelithiasis / Gallstones (*Dan Shi Zheng*)",
        "front": "What is the clinical presentation and specific empirical acupoint for Gallbladder Stones (*Dan Shi Zheng*)?",
        "back": "• Clinical Presentation: Severe paroxysmal colicky pain in right upper quadrant, radiating to right shoulder and back, nausea, vomiting, fatty food intolerance, positive Murphy's sign.\n• Special Empirical Acupoint: Dannangxue (EX-LE6 / 胆囊穴):\n  - Location: 1–2 cun directly inferior to GB34 (Yanglingquan), tender on palpation.\n  - Action: Specific diagnostic and therapeutic point for gallbladder inflammation and stone expulsion.\n• Accompanying Points: GB34, GB24 (Riyue - Front-Mu), LV14 (Qimen), BL19 (Danshu - Back-Shu), SJ6 (Zhigou).\n• Caution: Impacted stone with fever/jaundice (Charcot's triad) requires emergency surgery!",
        "consensus": "Dannangxue is the universally recognized board exam point for gallbladder pathology.",
        "variations": "Electroacupuncture on Dannangxue and GB34 stimulates biliary motility in non-obstructed cholelithiasis.",
        "sources": '["CAM p. 332", "Deadman p. 460"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Urological: Lin Syndrome / Dysuria (Five Types)",
        "front": "Define the Five Types of Lin Syndrome (Dysuria) in Chinese Medicine.",
        "back": "• 1. Heat Lin (*Re Lin*): Burning, painful, urgent, dark yellow urination; damp-heat in Bladder.\n• 2. Stone Lin (*Shi Lin*): Severe colicky pain radiating to groin, urinary interruption, passage of sand/stones (calculi).\n• 3. Blood Lin (*Xue Lin*): Painful urination with visible blood or clots (hematuria).\n• 4. Qi Lin (*Qi Lin*): \n  - Excess: Fullness, distension in lower abdomen, hesitant flow (Liver Qi constraint).\n  - Deficiency: Dribbling after urination, bearing-down sensation, exhaustion (Spleen/Kidney deficiency).\n• 5. Cloudy Lin (*Gao Lin*): Milky, turbid, greasy urine resembling rice water; kidney essence depletion or dampness.\n• Core Base Points: REN3 (Zhongji - Front-Mu), BL28 (Pangguangshu - Back-Shu), SP9 (Yinlingquan), SP6 (Sanyinjiao).",
        "consensus": "Foundational urological differentiation tested in both acupuncture and herbal examinations.",
        "variations": "Ba Zheng San is the classic herbal prescription for Heat and Stone Lin.",
        "sources": '["CAM p. 350", "Maciocia Practice p. 550"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Cardiovascular: Palpitations (*Xin Ji*) Differential",
        "front": "Differentiate Heart Blood Deficiency from Heart Yang Deficiency in patients with Palpitations.",
        "back": "• Heart Blood Deficiency:\n  - Symptoms: Palpitations, dizziness, pale complexion, insomnia, poor memory, startled easily.\n  - Tongue: Pale body, thin white coat.\n  - Pulse: Thready and weak (Xi Ruo).\n  - Points: HT7 (Shenmen), BL15 (Xinshu), BL20 (Pishu), SP6 (Sanyinjiao), REN14 (Juque).\n• Heart Yang Deficiency:\n  - Symptoms: Palpitations with chest discomfort/tightness, cold limbs, aversion to cold, cyanotic pale lips, severe fatigue.\n  - Tongue: Pale, swollen, moist body.\n  - Pulse: Deep, weak, slow or knotted (Jie Mai).\n  - Points: BL15 (Xinshu), REN17 (Danzhong), DU14 (Dazhui), REN4 (Guanyuan), moxibustion is essential!",
        "consensus": "Universal consensus across internal medicine texts.",
        "variations": "If palpitations are accompanied by fluid retention and edema, it represents Water Insulting the Heart.",
        "sources": '["CAM p. 336", "Maciocia Practice p. 220"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Psychiatric: Depressive Disorder (*Yu Zheng*) & Plum-Pit Qi",
        "front": "Explain the pathology, cardinal symptom, and point protocol for Plum-Pit Qi (*Mei He Qi*).",
        "back": "• Pathology: Liver Qi Stagnation combining with Phlegm in the throat. Emotional constraint causes Qi to knot, producing phlegm that obstructs the pharynx.\n• Cardinal Symptom: Subjective sensation of a plum pit (lump) stuck in the throat that cannot be swallowed and cannot be hawked up; no physical swallowing obstruction; worsens with emotional stress.\n• Point Protocol:\n  - Move Liver Qi: LV3 (Taichong), PC6 (Neiguan)\n  - Dissolve Phlegm: ST40 (Fenglong), SP9 (Yinlingquan)\n  - Open Throat / Descend Qi: REN22 (Tiantu), REN17 (Danzhong), REN12 (Zhongwan)\n• Classic Herbal Formula: Ban Xia Hou Po Tang.",
        "consensus": "The quintessential TCM pattern for globus pharyngeus / emotional somatic conversion.",
        "variations": "Contrast with true esophageal carcinoma: Plum-pit Qi has no actual dysphagia (food passes easily).",
        "sources": '["CAM p. 344", "Maciocia Practice p. 610"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Internal Medicine: Yang Edema vs Yin Edema (*Shui Zhong*)",
        "front": "Compare Yang Edema with Yin Edema in etiology, onset, and clinical manifestations.",
        "back": "• Yang Edema (Excess / Exterior):\n  - Etiology: Exterior Wind-Water invading Lung; Lung fails to diffuse and descend water.\n  - Onset: Acute, rapid onset.\n  - Location: Starts in the face, eyelids, and upper body; skin is taut and shiny; fever/chills.\n  - Pulse/Tongue: Floating-slippery pulse, thin white coat.\n  - Treatment: Diffuse Lung, expel wind (LU7, LI4, BL13, SP9).\n• Yin Edema (Deficiency / Interior):\n  - Etiology: Spleen and Kidney Yang deficiency; failure to transform and transport fluids.\n  - Onset: Chronic, insidious onset.\n  - Location: Starts in ankles, feet, and lower abdomen; deep pitting edema; pale dull skin; cold limbs.\n  - Pulse/Tongue: Deep, slow, weak pulse; pale swollen tongue with teeth marks.\n  - Treatment: Warm Spleen/Kidney Yang (BL20, BL23, REN4, SP6, KI7 + Moxa).",
        "consensus": "Fundamental diagnostic division of edema tested on all licensing board exams.",
        "variations": "Yang edema can transform into Yin edema if chronic and untreated.",
        "sources": '["CAM p. 354", "Maciocia Practice p. 580"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Internal Medicine: Xiao Ke (Wasting-Thirsting) - Upper Jiao",
        "front": "Detail the clinical signs, organ pathology, and points for Upper Jiao Xiao Ke.",
        "back": "• Organ Pathology: Lung Heat consuming body fluids.\n• Hallmark Symptom: Excessive Thirst (*Duo Yin*) with continuous consumption of fluids, dry mouth and tongue, frequent clear urination.\n• Tongue: Red tip and edges, thin yellow dry coat.\n• Pulse: Rapid, surging, or flooding (Hong Shuo) in Cun position.\n• Primary Acupoints: \n  - Lung Heat: LU10 (Yuji), LU11 (Shaoshang), BL13 (Feishu)\n  - Fluid Production: KI3 (Taixi), CV24 (Chengjiang), SP6 (Sanyinjiao)\n  - Adjunct: ST36 (Zusanli).",
        "consensus": "Classic representation of early/mild diabetes mellitus presenting with polydipsia.",
        "variations": "Herbal reference: Xiao Ke Fang.",
        "sources": '["CAM p. 360", "Maciocia Practice p. 660"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Internal Medicine: Xiao Ke (Wasting-Thirsting) - Middle Jiao",
        "front": "What are the clinical signs, organ pathology, and points for Middle Jiao Xiao Ke?",
        "back": "• Organ Pathology: Stomach Fire scorching the middle burner.\n• Hallmark Symptom: Excessive Hunger (*Duo Shi*) with voracious appetite yet rapid weight loss (emaciation), dry stools, constipation.\n• Tongue: Red body, dry yellow thick coating.\n• Pulse: Slippery and forceful, rapid (Hua Shi Shuo).\n• Primary Acupoints:\n  - Drain Stomach Fire: ST44 (Neiting), ST45 (Lidui), ST25 (Tianshu)\n  - Protect Fluids & Spleen: SP6 (Sanyinjiao), CV12 (Zhongwan), BL20 (Pishu), BL21 (Weishu).",
        "consensus": "Represents diabetic polyphagia and hypermetabolic wasting.",
        "variations": "Herbal reference: Yu Nu Jian.",
        "sources": '["CAM p. 361", "Maciocia Practice p. 662"]',
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Internal Medicine: Xiao Ke (Wasting-Thirsting) - Lower Jiao",
        "front": "State the clinical signs, organ pathology, and points for Lower Jiao Xiao Ke.",
        "back": "• Organ Pathology: Kidney Yin and Kidney Yang exhaustion.\n• Hallmark Symptom: Excessive Urination (*Duo Niao*) with turbid, sweet, or oily urine, dry mouth, lumbar soreness, impotence, blurry vision.\n• Tongue: Deep red peeled tongue (Yin deficiency) or pale swollen tongue (Yang deficiency).\n• Pulse: Deep, thready, rapid (Xi Shuo) or deep, weak, faint (Chen Ruo).\n• Primary Acupoints:\n  - Tonify Kidney: KI3 (Taixi), BL23 (Shenshu), CV4 (Guanyuan), KI6 (Zhaohai)\n  - Conserve Fluids: SP6 (Sanyinjiao), BL28 (Pangguangshu).",
        "consensus": "Represents advanced chronic diabetes with polyuria, nephropathy, and diabetic retinopathy.",
        "variations": "Herbal reference: Liu Wei Di Huang Wan (Yin) or Jin Gui Shen Qi Wan (Yang).",
        "sources": '["CAM p. 362", "Maciocia Practice p. 665"]',
        "importance_level": 1
    },

    # =========================================================================
    # 5. GYNECOLOGY (8 CARDS)
    # =========================================================================
    {
        "category": "Gynecology",
        "title": "Menstrual Irregularity: Alternating Early and Late",
        "front": "What are the two major etiologies and treatment protocols for Alternating Early and Late Menses?",
        "back": "• Definition (*Yue Jing Xian Hou Wu Ding Qi*): Cycle fluctuates randomly more than 7 days early or late for 3+ consecutive months.\n• Etiology 1: Liver Qi Stagnation\n  - Signs: Distended breasts and abdomen, PMS, irritable, dark clotted flow; wiry pulse.\n  - Points: LV3, SP6, CV6 (Qihai), PC6, LV14.\n• Etiology 2: Kidney Deficiency\n  - Signs: Scanty pale blood, sore lower back, dizziness, nocturia; deep weak pulse.\n  - Points: KI3, BL23, CV4 (Guanyuan), SP6, Mingmen (DU4).",
        "consensus": "Universal consensus across TCM gynecological textbooks (Maciocia, CAM).",
        "variations": "If mixed Liver stagnation with Spleen deficiency, use Xiao Yao San protocol.",
        "sources": '["Maciocia OB/GYN p. 195", "CAM p. 368"]',
        "importance_level": 1
    },
    {
        "category": "Gynecology",
        "title": "Menstrual Volume: Scanty Menses (*Yue Jing Guo Shao*)",
        "front": "Differentiate Blood Deficiency, Blood Stasis, and Phlegm-Dampness in Scanty Menses.",
        "back": "• Blood Deficiency:\n  - Presentation: Thin, pale red blood, lasts only 1–2 days; pale dull complexion, dizziness, fatigue; pale tongue, thready pulse.\n  - Points: ST36, SP6, BL20, BL17, CV4.\n• Blood Stasis:\n  - Presentation: Dark purple blood with sharp clots; severe stabbing lower abdominal pain relieved after clots pass; purple tongue, wiry/choppy pulse.\n  - Points: SP10, LV3, SP6, Zigong, ST29.\n• Phlegm-Dampness:\n  - Presentation: Sticky, thick, pale blood; overweight patient, puffy face, heavy limbs, excessive white leukorrhea; swollen tongue, slippery pulse.\n  - Points: ST40, SP9, CV9, CV12, SP6.",
        "consensus": "Foundational differential for oligomenorrhea and hypomenorrhea.",
        "variations": "Phlegm-Damp pattern strongly correlates with Polycystic Ovarian Syndrome (PCOS).",
        "sources": '["Maciocia OB/GYN p. 205", "CAM p. 370"]',
        "importance_level": 1
    },
    {
        "category": "Gynecology",
        "title": "Menstrual Volume: Profuse Menses (*Yue Jing Guo Duo*)",
        "front": "Compare Qi Deficiency and Blood Heat in Profuse Menstrual Bleeding (Hypermenorrhea).",
        "back": "• Qi Deficiency (Spleen Not Controlling Blood):\n  - Flow: Profuse, thin, watery, pale red blood; continuous trickling.\n  - Accompanying: Shortness of breath, severe fatigue, empty bearing-down abdomen; pale tongue, weak pulse.\n  - Points: DU20 (lift Qi), SP1 (moxa - astringe blood), CV6, ST36, SP6.\n• Blood Heat (Excess Fire):\n  - Flow: Profuse, thick, bright red or dark purple blood; heavy gushing.\n  - Accompanying: Thirst, agitation, red face, concentrated urine, constipation; red tongue with yellow coat, rapid pulse.\n  - Points: SP10 (cool blood), LI11, KI2 (drain fire), SP6, LV2.",
        "consensus": "Universal consensus: Spleen deficiency vs Blood heat is the primary clinical fork for heavy periods.",
        "variations": "Moxa on SP1 (Yinbai) is specifically indicated for Qi deficiency bleeding, contraindicated in excess blood heat.",
        "sources": '["Maciocia OB/GYN p. 212", "CAM p. 372"]',
        "importance_level": 1
    },
    {
        "category": "Gynecology",
        "title": "Dysmenorrhea Timing: Pre vs During vs Post-Menstrual",
        "front": "What does the TIMING of menstrual cramping (Pre vs During vs Post) reveal about Excess vs Deficiency?",
        "back": "• Pain Before Menses (Pre-Menstrual):\n  - Nature: Excess pattern (Qi Stagnation or Cold Coagulation).\n  - Mechanism: Qi and blood accumulate in lower abdomen and cannot move freely.\n  - Treatment: Move Qi and invigorate blood (LV3, CV6, SP6, ST29).\n• Pain During Menses (Peak Flow):\n  - Nature: Severe Excess (Blood Stasis or Damp-Heat).\n  - Mechanism: Physical obstruction from blood clots and stasis.\n  - Treatment: Break stasis (SP10, Zigong, ST29, LV3).\n• Pain After Menses (Post-Menstrual):\n  - Nature: Deficiency pattern (Blood Deficiency or Kidney Yin/Yang deficiency).\n  - Mechanism: Empty channels lack nourishment after blood loss; dull nagging ache relieved by pressure.\n  - Treatment: Tonify Blood and Kidneys (CV4, ST36, SP6, KI3, BL20).",
        "consensus": "Universal board exam pearl: Timing of dysmenorrhea directly determines Excess vs Deficiency diagnosis.",
        "variations": "Pain relieved by warmth = Cold; pain relieved by pressure = Deficiency; pain aggravated by pressure = Excess.",
        "sources": '["Maciocia OB/GYN p. 240", "CAM p. 374"]',
        "importance_level": 1
    },
    {
        "category": "Gynecology",
        "title": "Gynecological Pathology: Polycystic Ovarian Syndrome (PCOS)",
        "front": "State the TCM etiology, cardinal signs, and core acupoint protocol for PCOS.",
        "back": "• TCM Etiology: Phlegm-Dampness accumulation in the Uterus combined with Kidney Yang deficiency.\n• Cardinal Signs: Amenorrhea or oligomenorrhea, female infertility, obesity, cystic ovaries, hirsutism/acne, insulin resistance.\n• Core Acupoint Protocol:\n  - Dissolve Phlegm & Dampness: ST40 (Fenglong), SP9 (Yinlingquan), CV9 (Shuifen)\n  - Warm Kidney Yang & Mingmen: BL23 (Shenshu), CV4 (Guanyuan), DU4 (Mingmen) + Moxa\n  - Open Uterus & Regulate Ovaries: Zigong (EX-CA1), SP6 (Sanyinjiao), ST29 (Guilai).",
        "consensus": "Modern consensus in integrative TCM gynecology for complex endocrine-metabolic conditions.",
        "variations": "Can present with Liver Qi stagnation and secondary Blood heat in younger hirsute patients.",
        "sources": '["Maciocia OB/GYN p. 480", "Integrative TCM Gynecology"]',
        "importance_level": 2
    },
    {
        "category": "Gynecology",
        "title": "Gynecological Pathology: Endometriosis (*Zi Gong Nei Mo Yi Wei Zheng*)",
        "front": "What is the primary pathological mechanism of Endometriosis in TCM and what is the treatment protocol?",
        "back": "• Primary Pathological Mechanism: Static Blood (Blood Stasis) in the lower abdomen and pelvic cavity, often initiated by Cold stagnation or chronic Liver Qi constraint.\n• Clinical Signs: Severe progressive dysmenorrhea (pain increases month by month), fixed lower abdominal masses, deep dyspareunia (pain with intercourse), dark menstrual blood with large clots, infertility.\n• Treatment Protocol:\n  - Invigorate Blood & Dissolve Masses: SP10 (Xuehai), LV3 (Taichong), Zigong (EX-CA1), ST29 (Guilai), BL17 (Geshu)\n  - Regulate Conception/Penetrating Vessels: SP4 (Gongsun) + PC6 (Neiguan)\n  - Dispel Cold (if present): CV4 + Moxa.",
        "consensus": "Universal consensus: Blood stasis is the constant, mandatory pathological entity in endometriosis.",
        "variations": "Herbal reference: Ge Xia Zhu Yu Tang or Shao Fu Zhu Yu Tang.",
        "sources": '["Maciocia OB/GYN p. 495", "CAM p. 376"]',
        "importance_level": 1
    },
    {
        "category": "Gynecology",
        "title": "Postpartum: Retention of Urine (*Chan Hou Xiao Bian Bu Tong*)",
        "front": "Identify the etiology, presentation, and acupuncture points for Postpartum Urinary Retention.",
        "back": "• Definition: Inability to pass urine, or painful dribbling after childbirth.\n• Etiologies:\n  1. Qi Deficiency: Bladder Qi fails to transform after exhaustive labor; weak distended bladder.\n  2. Blood Stasis: Physical birth trauma causes local swelling and hematoma compressing the urethra.\n• Primary Acupoints:\n  - Front-Mu of Bladder: REN3 (Zhongji)\n  - Benefit Water & Intestines: SP9 (Yinlingquan), SP6 (Sanyinjiao), BL28 (Pangguangshu)\n  - Lift Spleen Qi: ST36 (Zusanli), DU20 (Baihui)\n• Technique: Gentle needling; avoid deep vigorous puncture in tender postpartum lower abdomen.",
        "consensus": "Standard clinical postpartum complication recognized in hospital and outpatient acupuncture.",
        "variations": "Moxa over REN8 and REN4 helps immediately restore bladder sensory contraction in Qi exhaustion.",
        "sources": '["Maciocia OB/GYN p. 620", "CAM p. 390"]',
        "importance_level": 2
    },
    {
        "category": "Gynecology",
        "title": "Postpartum: Insufficient Lactation (*Que Ru*)",
        "front": "Differentiate Deficiency from Stagnation in Hypogalactia (Insufficient Lactation), and list key points.",
        "back": "• Deficiency of Qi and Blood:\n  - Signs: Scanty or absent milk, watery thin milk, breasts are soft and non-distended; pale face, fatigue; pale tongue, weak pulse.\n  - Points: SI1 (Shaoze - empirical lactation point!), REN17 (Danzhong), ST18 (Rugen), ST36 (Zusanli), BL20 (Pishu).\n• Liver Qi Stagnation:\n  - Signs: Scanty milk or milk fails to flow, breasts are painfully distended, swollen, and hard; emotional stress, irritability; wiry pulse.\n  - Points: SI1 (Shaoze), REN17 (Danzhong), ST18 (Rugen), LV3 (Taichong), LV14 (Qimen), GB41 (Zulinqi).",
        "consensus": "Universal consensus: SI1 (Shaoze) and REN17 (Danzhong) are the master empirical pair for any lactation deficit.",
        "variations": "SI1 can be stimulated with gentle needle insertion or pricked to bleed for acute emotional blockage.",
        "sources": '["CAM p. 392", "Deadman p. 228"]',
        "importance_level": 1
    },

    # =========================================================================
    # 6. PAEDIATRICS (6 CARDS)
    # =========================================================================
    {
        "category": "Paediatrics",
        "title": "Pediatric Vital Signs & Physiological Milestones",
        "front": "State normal pediatric Heart Rate and Respiratory Rate ranges by age group.",
        "back": "• Normal Heart Rates (BPM):\n  - Infant (0–12 months): 100 – 160 bpm\n  - Toddler (1–3 years): 90 – 140 bpm\n  - Preschool (3–5 years): 80 – 120 bpm\n  - School-age (6–12 years): 70 – 110 bpm\n• Normal Respiratory Rates (breaths/min):\n  - Newborn/Infant: 30 – 60 /min\n  - Toddler: 24 – 40 /min\n  - Child: 18 – 30 /min\n• Clinical Meaning: Children have naturally faster physiological metabolism ('Pure Yang'). Vital sign thresholds must never be evaluated against adult normal baselines!",
        "consensus": "Fundamental pediatric clinical knowledge required for safety screening on board examinations.",
        "variations": "Bradycardia in an infant (<100 bpm) is a critical emergency indicator of hypoxia and hypoventilation.",
        "sources": '["PALS Guidelines", "Nelson Pediatrics"]',
        "importance_level": 1
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Fontanelles: Normal Closure Milestones",
        "front": "What are the anatomical locations and normal closure timelines for the Anterior and Posterior Fontanelles?",
        "back": "• Anterior Fontanelle (Bregma):\n  - Shape: Diamond-shaped, situated at junction of sagittal, coronal, and frontal sutures.\n  - Normal Closure: Closes between 12 and 18 months of age.\n• Posterior Fontanelle (Lambda):\n  - Shape: Triangular, situated at junction of sagittal and lambdoid sutures.\n  - Normal Closure: Closes between 2 and 3 months of age (by 8 weeks).\n• Clinical Exam Rule: Never apply deep acupuncture needles into unclosed fontanelles (DU22, DU24, DU20 prohibited in infants)!",
        "consensus": "Universal pediatric milestones; strict anatomical contraindication zone for infant acupuncture.",
        "variations": "Premature closure (craniosynostosis) restricts brain development; delayed closure indicates congenital essence deficiency.",
        "sources": '["Nelson Pediatrics", "CAM p. 398"]',
        "importance_level": 1
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Fontanelles: Pathological Signs",
        "front": "What do a Sunken Fontanelle and a Bulging Fontanelle signify clinically?",
        "back": "• Sunken Fontanelle (*Xin Xian*):\n  - Etiology: Severe Dehydration and fluid depletion from acute diarrhea/vomiting, or profound Spleen-Kidney deficiency.\n  - Emergency Action: Requires immediate fluid resuscitation to prevent hypovolemic shock.\n• Bulging / Raised Fontanelle (*Xin Gao*):\n  - Etiology: Increased Intracranial Pressure (ICP) due to meningitis, encephalitis, hydrocephalus, or severe intracranial hemorrhage.\n  - Accompanying: High fever, shrill crying, projectile vomiting, lethargy.\n  - Action: Immediate 911 emergency transfer! Medical emergency.",
        "consensus": "Universal physical exam red flags in pediatric triage.",
        "variations": "A slightly pulsatile fontanelle when the baby is calm and sitting upright is normal.",
        "sources": '["Nelson Pediatrics", "Harrison\'s IM"]',
        "importance_level": 1
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Respiratory: Cold Asthma vs Heat Asthma",
        "front": "Differentiate Cold Asthma from Heat Asthma in pediatric patients, and list key points.",
        "back": "• Cold Asthma (*Han Xiao*):\n  - Symptoms: Wheezing with thin, watery, white frothy phlegm, cold hands and feet, pale face, absence of thirst, worsens with cold weather.\n  - Tongue: Pale with thin white coat; Pulse: Floating-tight or slow.\n  - Points: BL13 (Feishu), Dingchuan (EX-B1), REN17 (Danzhong), moxibustion is favored.\n• Heat Asthma (*Re Xiao*):\n  - Symptoms: Rapid loud wheezing with thick yellow sticky phlegm, high fever, red face, thirst for cold drinks, restlessness, constipation.\n  - Tongue: Red body with yellow greasy coat; Pulse: Rapid, slippery.\n  - Points: BL13, Dingchuan, LI11, LU5, GV14 (Dazhui), prick LU11.",
        "consensus": "Standard pediatric respiratory differentiation across all TCM textbooks.",
        "variations": "Children transform exterior cold into interior heat with extreme rapidity ('Rapid Transformation').",
        "sources": '["CAM p. 402", "Scott Pediatric Acupuncture"]',
        "importance_level": 2
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Digestive: Food Stagnation / Retention (*Shang Shi*)",
        "front": "Describe the presentation, tongue, pulse, and Sifeng protocol for Pediatric Food Retention.",
        "back": "• Presentation: Abdominal distension, pain worse with pressure, foul sour belching, vomiting undigested milk or food, sour diarrhea or constipation, restless nighttime sleep.\n• Tongue: Thick, greasy, dirty yellow or white coating.\n• Pulse: Slippery and rapid (Hua Shuo), or tight.\n• Sifeng (EX-UE10 / 四缝) Protocol:\n  - Location: Palmar surface of 2nd to 5th fingers, at the midpoint of the proximal interphalangeal creases.\n  - Technique: Prick with three-edged needle or lancet to squeeze out a small amount of clear/yellowish fluid or blood.\n  - Action: Specific empirical extra points to dissolve childhood food stagnation and Gan syndrome.",
        "consensus": "Universal consensus: Sifeng pricking is the quintessential traditional pediatric treatment for food retention.",
        "variations": "Accompanying points: Zhongwan (REN12), Zusanli (ST36), Tianshu (ST25).",
        "sources": '["CAM p. 406", "Deadman p. 574"]',
        "importance_level": 1
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Infectious: Mumps (*Zha Sai*)",
        "front": "State the TCM etiology, affected channels, and point protocol for Mumps (*Zha Sai*).",
        "back": "• TCM Etiology: Toxic Wind-Heat invading the Shaoyang (San Jiao/Gallbladder) and Yangming (Stomach) channels, obstructing the collaterals of the parotid gland.\n• Cardinal Symptoms: Unilateral or bilateral painful swelling of the parotid gland centered on earlobe, fever, pain chewing, dry mouth.\n• Complication Alert: Viral orchitis (testicular swelling and severe pain in boys) occurs when toxic heat descends into the Liver channel!\n• Acupuncture Protocol:\n  - Local Points: SJ17 (Yifeng), ST6 (Jiache), GB20 (Fengchi)\n  - Clear Heat Distally: LI11 (Quchi), SJ5 (Waiguan), LI4 (Hegu)\n  - Testicular Swelling (if present): LV3, LV1, SP6.",
        "consensus": "Classic infectious disease presentation in Chinese medicine pediatric curricula.",
        "variations": "Prick-to-bleed Shaoshang (LU11) or apex of the ear (Erjian) aggressively purges toxic parotid heat.",
        "sources": '["CAM p. 412", "Deadman p. 110"]',
        "importance_level": 2
    },

    # =========================================================================
    # 7. SAFETY & ETHICS (6 CARDS)
    # =========================================================================
    {
        "category": "Safety and Ethics",
        "title": "Clean Needle Technique: Hand Hygiene Protocol",
        "front": "When is Alcohol-Based Hand Rub permitted, and when is Soap and Water mandatory under CNT?",
        "back": "• Alcohol-Based Hand Rub (ABHR):\n  - Standards: Must contain 60%–95% ethanol or isopropanol.\n  - Application: Rub all surfaces of hands and fingers vigorously until completely dry (minimum 15–20 seconds).\n  - Permitted: Routine hand hygiene immediately before palpating points, between clean needle insertions, and between patients.\n• Soap and Water (Mandatory):\n  1. When hands are visibly soiled with dirt, organic matter, or blood/body fluids.\n  2. After using the restroom.\n  3. Before eating.\n  4. When caring for patients with known or suspected spore-forming pathogens (e.g., Clostridioides difficile or Norovirus), as alcohol does not destroy bacterial spores!",
        "consensus": "Universal CDC, WHO, and Clean Needle Technique (CNT) standard.",
        "variations": "Gloves do NOT substitute for hand hygiene; hands must be washed before donning and immediately after removing gloves.",
        "sources": '["CNT Manual 7th Edition p. 18", "CDC Guidelines"]',
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Clean Needle Technique: Antiseptic Skin Preparation",
        "front": "State the exact protocol and timing rules for skin disinfection prior to needle insertion.",
        "back": "• Antiseptic Agent: 70% Isopropyl Alcohol.\n• Swabbing Technique: \n  - Swab the point site firmly using a sterile cotton ball or alcohol prep pad.\n  - Wipe in concentric circles moving outward from center, OR use a firm unidirectional stroke.\n• TIMING / DRYING RULE (CRITICAL):\n  - The alcohol must be allowed to air-dry completely on the skin (minimum 30–60 seconds) before needle insertion!\n  - Rationale: Wet alcohol does not achieve full bactericidal effect, and inserting needles through wet alcohol causes chemical irritation, stinging pain, and introduces alcohol into subcutaneous tissue.\n  - STRICTLY PROHIBITED: Blowing on the skin or fanning the site to speed drying (contaminates the sterile site!).",
        "consensus": "Absolute standard across all worldwide acupuncture licensing safety examinations.",
        "variations": "If the skin is re-palpated with an unwashed finger after swabbing, the site must be swabbed again.",
        "sources": '["CNT Manual 7th Edition p. 24", "OSHA Bloodborne Standards"]',
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Sharps Disposal Regulations",
        "front": "What are the regulatory requirements for Sharps Containers and the 3/4 fill rule?",
        "back": "• Sharps Container Standards:\n  - Must be rigid, puncture-resistant, leak-proof on sides and bottom, sealable, and clearly labeled with the biohazard symbol in fluorescent orange/red.\n  - Must be placed within arm's reach of the treatment table and at eye level.\n• Disposal Protocol:\n  - Used needles must be placed into the container immediately upon withdrawal; never lay used needles on trays or counter surfaces.\n  - NEVER recap, bend, or shear needles by hand.\n• The 3/4 Full Rule (Critical):\n  - Sharps containers must be permanently locked and disposed of when filled to the marked fill line or 3/4 full!\n  - Overfilling causes needle protrusions and catastrophic needlestick puncture accidents.",
        "consensus": "OSHA, Canadian provincial health regulations, and CNT mandatory universal standards.",
        "variations": "Sharps must be collected by an authorized biohazardous medical waste disposal contractor.",
        "sources": '["OSHA 1910.1030", "CNT Manual 7th Edition p. 28"]',
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Needling Safety: Danger Points Around the Orbit (BL1 & ST1)",
        "front": "Summarize the anatomical risks and mandatory needling rules for orbital points BL1 (Jingming) and ST1 (Chengqi).",
        "back": "• Anatomical Hazards: Puncture of the eyeball (globe perforation), retrobulbar hemorrhage (which can rapidly compress the optic nerve causing blindness), and orbital hematoma.\n• Mandatory Needling Protocol:\n  1. Ensure patient is completely still; inform them not to talk or move.\n  2. For BL1: Push the eyeball laterally with finger; insert along medial orbital wall 0.5–1.0 cun.\n  3. For ST1: Push the eyeball superiorly; insert along inferior orbital floor 0.5–0.8 cun.\n  4. ABSOLUTE PROHIBITION: Never rotate, lift, or thrust the needle!\n  5. On needle removal, apply firm, continuous direct pressure with sterile dry cotton for minimum 1–2 minutes.\n  6. Moxibustion is strictly prohibited at both points.",
        "consensus": "High-liability board exam safety question. Highest incidence of severe malpractice claims in acupuncture.",
        "variations": "Patients taking anticoagulants should generally NOT receive orbital needling.",
        "sources": '["Deadman p. 256", "CNT Manual 7th Edition p. 45"]',
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Needling Safety: High-Risk Deep Visceral Punctures",
        "front": "Identify the visceral organ puncture hazards and safe depths for ST25, REN12, and BL22/BL23.",
        "back": "• 1. Peritoneal Cavity & Bowel Puncture (ST25 Tianshu & REN12 Zhongwan):\n  - Risk: Penetrating parietal peritoneum into small/large intestine, causing acute peritonitis.\n  - Safe Needling: Depth should not exceed 0.8–1.2 cun in thin/elderly patients; needle perpendicularly only to recommended depth.\n• 2. Kidney Puncture (BL22 Sanjiaoshu, BL23 Shenshu, BL52 Zhishi):\n  - Risk: Kidneys lie between T12 and L3. Direct deep puncture causes retroperitoneal hematoma, renal laceration, hematuria.\n  - Safe Needling: Needle obliquely toward the spine 0.5–0.8 cun; never needle deep perpendicularly into the renal angle in thin individuals.\n• 3. Urinary Bladder (REN3 Zhongji & REN4 Guanyuan):\n  - Risk: Penetrating a distended bladder. Patient MUST void urine before treatment!",
        "consensus": "Universal anatomical safety rules in Clean Needle Technique and Pan-Canadian safety guidelines.",
        "variations": "In obese patients, abdominal wall thickness is increased, but organ locations remain anatomically constant.",
        "sources": '["Deadman Point Precautions", "CNT Manual 7th Edition p. 42"]',
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Professional Jurisprudence: Mandatory Record Retention Period",
        "front": "State the legal medical record retention periods for Adult patients versus Pediatric patients.",
        "back": "• Adult Patient Records:\n  - Legal Requirement: Records must be securely retained for a minimum of 10 years from the date of the last professional service or clinical entry (varies from 7–10 years depending on Canadian province / state; 10 years is standard benchmark).\n• Pediatric / Minor Patient Records (CRITICAL):\n  - Legal Requirement: Records for a minor must be retained for 10 years AFTER the patient reaches the age of majority!\n  - Calculation: If age of majority is 18 (or 19 in BC), records must be retained until the patient is 18 + 10 = 28 years old (or 29 in BC)!\n  - Example: A 4-year-old child's record must be kept for 24 years before legal destruction is permitted.",
        "consensus": "Universal regulatory standard across Canadian provincial colleges (CTCMA, CTCMPAO) and North American health privacy acts.",
        "variations": "Secure destruction must involve certified cross-cut shredding or permanent electronic data wiping with a destruction certificate.",
        "sources": '["CTCMPAO Record Keeping Standards", "CTCMA Bylaws Part 6"]',
        "importance_level": 1
    }
]

print(f"Total expansion cards prepared: {len(CARDS_100)}")

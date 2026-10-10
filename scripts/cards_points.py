"""Meridians and Points Flashcards (50 high-yield point cards).

Covers point categories, Five Shu points, Yuan/Luo/Xi-Cleft, Back-Shu/Front-Mu,
Eight Confluent, Eight Hui, Command points, and specific channel points.
All points strictly use the bilingual format: CODE (Pinyin / Hanzi) with NO English translation.
"""

import json

CARDS = [
    {
        "category": "Meridians and Points",
        "title": "Five Shu Points: Clinical Dynamics & Five Element Correspondence",
        "front": "List the five Shu points in distal-to-proximal order, their classical indications (Nan Jing / Ling Shu), and their Yin vs Yang channel Five Element correspondences.",
        "back": "Five Shu Points (Distal to Proximal):\n1. Jing-Well: At fingers/toes tips. Wood on Yin channels; Metal on Yang channels. Indications: Clears heat, restores consciousness, treats fullness in chest and mental disorders.\n2. Ying-Spring: At digits web margins. Fire on Yin channels; Water on Yang channels. Indications: Clears heat from the channel and organ, changes of complexion.\n3. Shu-Stream: At wrists/ankles. Earth on Yin channels (also Yuan-Source on Yin); Wood on Yang channels. Indications: Heaviness of the body, joint pain (Bi syndrome), intermittent attacks.\n4. Jing-River: At forearms/calves. Metal on Yin channels; Fire on Yang channels. Indications: Cough, dyspnea, chills and fever, changes in the voice.\n5. He-Sea: At elbows/knees. Water on Yin channels; Earth on Yang channels. Indications: Rebellious Qi, diarrhea, stomach/intestinal disorders, skin diseases.",
        "consensus": "Universal foundational theory of distal point energetics in acupuncture practice.",
        "variations": "Ling Shu emphasizes seasonal use of Five Shu points (Winter = Jing-Well, Spring = Ying-Spring, Summer = Shu-Stream, Late Summer = Jing-River, Autumn = He-Sea).",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture", "Huangdi Neijing Ling Shu & Nan Jing"])
    },
    {
        "category": "Meridians and Points",
        "title": "Yuan-Source & Luo-Connecting Host-Guest Pairing",
        "front": "Explain the 'Host and Guest' (Zhu Ke) point combination theory using Yuan-Source and Luo-Connecting points.",
        "back": "Host and Guest (Zhu Ke - 主客) Theory:\n• Principle: Pairs the Yuan-Source point of the primarily affected channel (the 'Host') with the Luo-Connecting point of its internally-externally related paired channel (the 'Guest').\n• Mechanism: The Yuan-Source point directly tonifies or sedates the diseased organ, while the paired Luo point opens the connecting vessel to harmonize Qi and drain excess/replenish deficiency across the Yin-Yang pair.\n\nClassic Examples:\n• Lung disorder (Host) paired with Large Intestine (Guest): LU9 (Taiyuan / 太渊) [Host] + LI6 (Pianli / 偏历) [Guest].\n• Liver disorder (Host) paired with Gallbladder (Guest): LV3 (Taichong / 太冲) [Host] + GB37 (Guangming / 光明) [Guest].\n• Spleen disorder (Host) paired with Stomach (Guest): SP3 (Taibai / 太白) [Host] + ST40 (Fenglong / 丰隆) [Guest].",
        "consensus": "Foundational treatment strategy for stubborn channel and zang-fu imbalances.",
        "variations": "Deadman notes that Luo points can also be used alone as single distal points for psycho-emotional disharmonies connected to their respective channels.",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "Xi-Cleft Points: Clinical Significance & Yin vs Yang Specializations",
        "front": "Define Xi-Cleft (Accumulation) points and describe how their clinical actions differ between Yin channels and Yang channels.",
        "back": "Definition & Actions:\n• Xi-Cleft points are sites where the Qi and Blood of the channel plunge deeply and accumulate.\n• General Action: Premier points for treating acute, severe conditions and stubborn, intractable pain along the channel or in the related organ.\n\n⚠️ Yin vs Yang Channel Specializations:\n• Yin Channel Xi-Cleft Points: Specialize in stopping acute bleeding and severe blood stasis disorders (e.g. LU6 for acute hemoptysis, SP8 for severe acute dysmenorrhea, KI5 for amenorrhea with cramping).\n• Yang Channel Xi-Cleft Points: Specialize in treating acute, severe channel pain and acute inflammation (e.g. ST34 for severe acute epigastric pain or breast abscess, GB36 for acute rabies/toxin pain).",
        "consensus": "Essential emergency and acute-phase acupuncture treatment points.",
        "variations": "There are 16 Xi-Cleft points in total: 12 for the primary channels and 4 for the extraordinary vessels (Yin Wei: KI9, Yang Wei: GB35, Yin Qiao: KI8, Yang Qiao: BL59).",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "Back-Shu & Front-Mu Points: Yin-Yang Combination",
        "front": "Describe the clinical synergy of combining Back-Shu points with Front-Mu points (Mu-Shu Combination - 俞募配穴).",
        "back": "Mu-Shu Combination (俞募配穴):\n• Synergy: Pairs the Front-Mu point (located on the anterior Yin aspect) with the Back-Shu point (located on the posterior Yang aspect) of the same organ.\n• Dynamics:\n  - Front-Mu points correspond to Yang Qi gathering on the Yin aspect; highly sensitive to acute conditions and Yang/heat/excess patterns of the Fu organs.\n  - Back-Shu points correspond to Yin Blood gathering on the Yang aspect; premier points for treating chronic conditions, Yin/deficiency/cold patterns of the Zang organs.\n• Clinical Rule: Acute/Excess diseases often manifest tender Front-Mu points; Chronic/Deficiency diseases often manifest sluggish Back-Shu points.\n• Examples:\n  - Stomach disorders: REN12 (Zhongwan / 中脘) [Front-Mu] + BL20 (Pishu / 脾俞) or BL21 (Weishu / 胃俞) [Back-Shu].\n  - Lung disorders: LU1 (Zhongfu / 中府) [Front-Mu] + BL13 (Feishu / 肺俞) [Back-Shu].",
        "consensus": "Highly effective classic combination for internal organ pathology.",
        "variations": "Tenderness on palpation of Front-Mu points is a reliable diagnostic indicator of acute organ distress.",
        "sources": json.dumps(["CAM 3rd Ed.", "Maciocia Foundations", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "Eight Confluent Points of Extraordinary Vessels",
        "front": "List the Eight Confluent Points (Ba Mai Jiao Hui Xue), their paired master/couple relationships, and the anatomical areas they govern.",
        "back": "Eight Confluent Pairs:\n1. Chong Mai & Yin Wei Mai:\n   - Master: SP4 (Gongsun / 公孙); Couple: PC6 (Neiguan / 内关).\n   - Governs: Stomach, Heart, Chest, Epigastrium.\n\n2. Ren Mai & Yin Qiao Mai:\n   - Master: LU7 (Lieque / 列缺); Couple: KI6 (Zhaohai / 照海).\n   - Governs: Throat, Chest, Lungs, Diaphragm, Abdomen.\n\n3. Du Mai & Yang Qiao Mai:\n   - Master: SI3 (Houxi / 后溪); Couple: BL62 (Shenmai / 申脉).\n   - Governs: Inner canthus, Neck, Ear, Shoulder, Back, Spine.\n\n4. Dai Mai & Yang Wei Mai:\n   - Master: GB41 (Zulinqi / 足临泣); Couple: SJ5 (Waiguan / 外关).\n   - Governs: Outer canthus, Ear, Cheek, Neck, Shoulder, Lateral costal region, Hip.",
        "consensus": "Cornerstone of extraordinary vessel acupuncture; master point is needled first on one side, couple point on the opposite side.",
        "variations": "Gender needle order: Men needle master on left and couple on right; Women needle master on right and couple on left.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "Eight Hui-Meeting Points (Ba Hui Xue - 八会穴)",
        "front": "List the Eight Hui-Meeting Points and the specific anatomical tissues/substances each point commands.",
        "back": "Eight Hui-Meeting Points (八会穴):\n1. Zang organs: LV13 (Zhangmen / 章门) [Front-Mu of Spleen].\n2. Fu organs: REN12 (Zhongwan / 中脘) [Front-Mu of Stomach].\n3. Qi: REN17 (Danzhong / 膻中) [Front-Mu of Pericardium, Sea of Qi].\n4. Blood: BL17 (Geshu / 膈俞) [Diaphragm Shu].\n5. Sinews / Tendons: GB34 (Yanglingquan / 阳陵泉) [He-Sea of Gallbladder].\n6. Blood Vessels: LU9 (Taiyuan / 太渊) [Yuan-Source of Lung, Meeting of Pulses].\n7. Bone: BL11 (Dazhu / 大杼) [Meeting of Bone].\n8. Marrow: GB39 (Xuanzhong / 悬钟) [Meeting of Marrow].",
        "consensus": "Universal empirical points selected whenever pathology involves the corresponding tissue or physiological substance.",
        "variations": "BL17 with moxibustion tonifies Blood; BL17 with needle reduction moves Blood and eliminates stasis.",
        "sources": json.dumps(["CAM 3rd Ed.", "Nan Jing Chapter 45", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "Six Command Points (Gao Wu Command Points)",
        "front": "Identify the Six Command Points and the specific anatomical body regions each point commands.",
        "back": "Six Command Points:\n1. Abdomen: ST36 (Zusanli / 足三里) - 'For the abdomen, seek ST36.'\n2. Head and Back of Neck: LU7 (Lieque / 列缺) - 'For the head and neck, seek LU7.'\n3. Face and Mouth: LI4 (Hegu / 合谷) - 'For the face and mouth, seek LI4.'\n4. Back and Lumbar region: BL40 (Weizhong / 委中) - 'For the lumbar and back, seek BL40.'\n5. Chest and Flank: PC6 (Neiguan / 内关) - 'For the chest and flank, seek PC6.'\n6. Fainting and Resuscitation: DU26 (Shuigou / 水沟) - 'For emergency resuscitation, seek DU26.'",
        "consensus": "Core empirical points taught universally for distal symptomatic treatment.",
        "variations": "The original Four Command Points (Song Dynasty) were ST36, LI4, LU7, BL40; PC6 and DU26 were added in the Ming Dynasty by Gao Wu.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "The Four Gates (Si Guan - 四关)",
        "front": "What points comprise the Four Gates (Si Guan), and how do classical texts explain their clinical synergy?",
        "back": "Points: Bilateral LI4 (Hegu / 合谷) and LV3 (Taichong / 太冲).\n\nSynergy & Mechanisms:\n• LI4: Yuan-Source of Large Intestine (Yang / Upper body / Qi).\n• LV3: Yuan-Source of Liver (Yin / Lower body / Blood).\n• Combined Actions:\n  - Powerfully opens all 12 channels and expels internal and external pathogenic factors.\n  - Regulates and unblocks Qi and Blood throughout the entire body.\n  - Premier empirical combination for severe Liver Qi stagnation, generalized spasms, pain syndromes, agitation, and headaches.",
        "consensus": "Most frequently utilized 4-point combination in clinical acupuncture for moving stagnant Qi and pacifying the Shen.",
        "variations": "Caution in pregnancy: LI4 is strictly contraindicated due to strong downward Qi dispersion.",
        "sources": json.dumps(["Maciocia Foundations", "Deadman Manual", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "LU1 (Zhongfu / 中府)",
        "front": "Location, actions, and critical needling depth/angle safety rules for LU1 (Zhongfu / 中府).",
        "back": "Location: Lateral aspect of anterior chest, 6 cun lateral to midline, 1 cun inferior to LU2 in the infraclavicular fossa (level with 1st intercostal space).\nFront-Mu Point of Lung; Crossing point of Lung and Spleen channels.\n\nActions:\n• Clears lung heat, regulates lung Qi, descends rebellious Qi (cough, asthma, wheezing).\n• Alleviates chest fullness and pain.\n\n⚠️ Safety Rules:\n• Puncture OBLIQUELY 0.5 - 0.8 cun directed laterally towards the shoulder/arm.\n• Medial or deep perpendicular insertion carries a high risk of puncturing the lung apex, causing Pneumothorax.",
        "consensus": "Never needle perpendicularly or medially.",
        "variations": "CAM lists 0.5–0.8 cun oblique lateral; Deadman notes that in thin patients, the pleura is only 1.5 cm from the skin surface.",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "LU5 (Chize / 尺泽)",
        "front": "Location, point categories, indications, and needling technique for LU5 (Chize / 尺泽).",
        "back": "Location: On the cubital crease of the elbow, in the depression on the radial side of the biceps brachii tendon (with elbow slightly flexed).\nPoint Categories: He-Sea and Water point of the Lung channel.\n\nActions:\n• Clears lung heat and drains phlegm-heat from the upper jiao.\n• Descends rebellious Lung Qi (cough, hemoptysis, asthma).\n• Relaxes the sinews and clears heat from the urinary bladder (Water point association).\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun, or prick to bleed with three-edged needle for acute sore throat or febrile convulsions.",
        "consensus": "Premier point for clearing excess heat and phlegm-heat from the lungs.",
        "variations": "Avoid the cephalic vein on the radial aspect; prick with lancet to bleed in acute severe heat toxin.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "LU7 (Lieque / 列缺)",
        "front": "Location, specialized point categories, indications, and insertion technique for LU7 (Lieque / 列缺).",
        "back": "Location: 1.5 cun proximal to the radial styloid process, between the brachioradialis and abductor pollicis longus tendons.\nPoint Categories: Luo-Connecting point; Master point of Ren Mai; Command point of Head and Neck; Gao Wu Command point.\n\nActions:\n• Expels exterior wind, releases the exterior, opens the nose (nasal obstruction, rhinitis).\n• Commands disorders of the head and posterior neck (occipital headache, neck stiffness).\n• Regulates Ren Mai and opens water passages (edema, dysuria).\n\nNeedling:\n• Oblique insertion 0.5 - 1.0 cun proximally towards the elbow (to treat cough/exterior wind) or distally towards the hand.",
        "consensus": "Key point for exterior wind-cold/heat attacks and all head/neck conditions.",
        "variations": "Avoid the cephalic vein and superficial branch of radial nerve (which causes sharp electric sensations).",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "LU9 (Taiyuan / 太渊)",
        "front": "Location, point categories, indications, and anatomical cautions for LU9 (Taiyuan / 太渊).",
        "back": "Location: At the radial end of the transverse wrist crease, in the depression on the radial side of the radial artery.\nPoint Categories: Shu-Stream, Yuan-Source, and Earth (tonification) point of Lung; Hui-Meeting point of Blood Vessels.\n\nActions:\n• Premier point to tonify Lung Qi and Lung Yin.\n• Transforms phlegm and stops cough.\n• Unblocks the pulse and regulates blood circulation throughout all vessels.\n\n⚠️ Anatomical Caution:\n• Palpate the radial artery with finger; insert needle perpendicular 0.3 - 0.5 cun medially between the radial artery and abductor pollicis longus tendon.\n• Strictly avoid puncturing the radial artery (risk of hematoma).",
        "consensus": "Premier tonification point for chronic lung deficiency and pulse irregularities.",
        "variations": "Deadman emphasizes gentle insertion without violent manipulation to protect the radial artery.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "LU11 (Shaoshang / 少商)",
        "front": "Location, point categories, primary clinical actions, and emergency bleeding technique for LU11 (Shaoshang / 少商).",
        "back": "Location: Radial side of the thumb, 0.1 cun posterior to the corner of the nail.\nPoint Categories: Jing-Well and Wood point of the Lung channel.\n\nActions:\n• Clears severe heat from the throat and upper jiao.\n• Revives consciousness from coma or syncope.\n• Benefits throat swelling, severe acute tonsillitis, and mumps.\n\nTechnique:\n• Puncture 0.1 cun perpendicularly, or prick with three-edged needle to express 2–3 drops of blood for severe acute throat pain or high fever.",
        "consensus": "Number one emergency point for acute severe sore throat and high fever bleeding therapy.",
        "variations": "Pricking to bleed is markedly more effective than standard needle retention for acute wind-heat sore throat.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "LI4 (Hegu / 合谷)",
        "front": "Location, categories, primary actions, and strict pregnancy contraindications for LI4 (Hegu / 合谷).",
        "back": "Location: Dorsum of hand, between 1st and 2nd metacarpal bones, at midpoint of 2nd metacarpal bone on its radial margin.\nPoint Categories: Yuan-Source point of Large Intestine; Command point of Face and Mouth; Heavenly Star point.\n\nActions:\n• Dispels exterior wind, clears heat, alleviates pain.\n• Commands all disorders of face, eyes, nose, mouth, and teeth.\n• Induces labor and descends Qi.\n\n⚠️ Contraindication:\n• ABSOLUTELY CONTRAINDICATED in pregnancy due to powerful descending Qi action that can cause miscarriage. (Deliberately used in delayed labor).",
        "consensus": "Universal analgesic and exterior-releasing point, strictly forbidden during pregnancy.",
        "variations": "Perpendicular insertion 0.5 - 1.0 cun. De qi radiates toward the fingers or up the forearm.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "LI11 (Quchi / 曲池)",
        "front": "Location, categories, indications, and textbook needling depths for LI11 (Quchi / 曲池).",
        "back": "Location: With elbow flexed to 90°, in the depression at the lateral end of the transverse cubital crease, midway between LU5 and lateral epicondyle of humerus.\nPoint Categories: He-Sea, Earth, and Mother (tonification) point of Large Intestine; Heavenly Star point.\n\nActions:\n• Premier point for clearing heat and fire toxins from the entire body (high fever, sore throat).\n• Cools blood and clears skin itching, hives, eczema, and psoriasis.\n• Regulates Qi and Blood, alleviates upper limb hypertension and hemiplegia.\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.\n• CAM: 1.0 - 1.5 cun; Deadman: 1.0 - 1.5 cun directed towards HT3.",
        "consensus": "The single most important acupuncture point for clearing systemic heat and treating inflammatory skin diseases.",
        "variations": "Directing needle towards HT3 penetrates through to the Yin aspect for severe hemiplegia.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "LI20 (Yingxiang / 迎香)",
        "front": "Location, categories, indications, and insertion technique for LI20 (Yingxiang / 迎香).",
        "back": "Location: In the nasolabial groove, at the level of the midpoint of the lateral border of the ala nasi.\nPoint Categories: Crossing point of Large Intestine and Stomach channels.\n\nActions:\n• Opens nasal passages, dispels wind, clears heat.\n• Premier point for all nasal disorders: rhinitis, allergic sinusitis, nasal congestion, loss of smell (anosmia), epistaxis.\n• Alleviates facial swelling, facial paralysis, and biliary ascariasis.\n\nTechnique:\n• Oblique or transverse insertion 0.3 - 0.5 cun medially and superiorly towards the bridge of the nose / inner canthus.\n• Moxibustion is classically contraindicated at this point.",
        "consensus": "Premier local point for nasal obstruction and rhinitis.",
        "variations": "Classically contraindicated for moxa due to cosmetic scarring risk and sensitive facial tissue.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "ST8 (Touwei / 头维)",
        "front": "Location, indications, needling technique, and moxibustion status for ST8 (Touwei / 头维).",
        "back": "Location: At the corner of the forehead, 0.5 cun within the anterior hairline, 4.5 cun lateral to DU24.\nPoint Categories: Crossing point of Stomach, Gallbladder, and Yang Wei Mai.\n\nActions:\n• Clears head and brightens eyes, dispels wind, alleviates pain.\n• Premier point for Yangming and Shaoyang headaches (frontal, temporal), migraines, dizziness, eye twitching, tearing.\n\nTechnique:\n• Transverse / subcutaneous insertion 0.5 - 1.0 cun posteriorly or anteriorly along the scalp.\n• Moxibustion is STRICTLY CONTRAINDICATED at ST8 across all classical texts.",
        "consensus": "Essential headache point; needle subcutaneously; moxibustion forbidden.",
        "variations": "Classical contraindication for moxibustion is due to danger of flaring heat upward to the head and eyes.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "ST21 (Liangmen / 梁门)",
        "front": "Location, indications, and deep needling anatomical cautions for ST21 (Liangmen / 梁门).",
        "back": "Location: On the upper abdomen, 4 cun superior to umbilicus, 2 cun lateral to anterior midline (level with REN12).\n\nActions:\n• Harmonizes the middle jiao, descends rebellious Stomach Qi, relieves pain, transforms food stagnation.\n• Treats epigastric pain, vomiting, acid regurgitation, anorexia, abdominal distension.\n\n⚠️ Anatomical Cautions:\n• Perpendicular insertion 0.8 - 1.2 cun.\n• Deep needle insertion on the right side risks penetrating an enlarged liver; deep insertion on the left side risks penetrating the stomach if distended.\n• Palpate for hepatomegaly before inserting needles into the right upper abdomen.",
        "consensus": "Effective local point for stomach pain, but requires careful depth control to avoid visceral puncture.",
        "variations": "Instruct patient to empty bladder and ensure stomach is not overly full before deep needling.",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Meridians and Points",
        "title": "ST25 (Tianshu / 天枢)",
        "front": "Location, categories, clinical indications, and needling safety for ST25 (Tianshu / 天枢).",
        "back": "Location: On the abdomen, 2 cun lateral to the center of the umbilicus (level with REN8).\nPoint Categories: Front-Mu point of the Large Intestine.\n\nActions:\n• Regulates the intestines, clears damp-heat, harmonizes Stomach and Spleen, alleviates pain.\n• Premier point for all bowel disorders: acute/chronic diarrhea, dysentery, constipation, abdominal distension, intestinal abscess (appendicitis).\n• Regulates Qi and resolves blood stasis in the lower abdomen (gynecological dysmenorrhea).\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.\n• Deep needle insertion in thin patients risks penetrating the peritoneal cavity.",
        "consensus": "Bi-directional regulation point for both diarrhea and constipation.",
        "variations": "Moxa on ST25 is highly effective for chronic cold-deficiency diarrhea.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "ST36 (Zusanli / 足三里)",
        "front": "Location, categories, cardinal actions, and textbook depth discrepancies for ST36 (Zusanli / 足三里).",
        "back": "Location: 3 cun inferior to ST35 (Dubi / 犊鼻), one fingerbreadth lateral to the anterior tibial crest.\nPoint Categories: He-Sea, Earth, and Horary point of Stomach; Sea of Water and Grain; Gao Wu Command point of Abdomen; Heavenly Star point.\n\nActions:\n• Premier point for tonifying Qi, Blood, Yin, and Yang throughout the whole body.\n• Harmonizes Stomach, fortifies Spleen, resolves dampness, alleviates pain.\n• Regulates defensive (Wei) Qi, boosts immunity, treats general fatigue and digestive failure.\n\n⚠️ Textbook Depth Discrepancies:\n• CAM: Perpendicular 1.0 - 2.0 cun.\n• Deadman: Perpendicular or oblique 1.0 - 1.5 cun. Caution: excessively deep puncture in elderly/emaciated individuals risks hitting the interosseous membrane.",
        "consensus": "The single most famous tonification and digestive powerhouse point in acupuncture.",
        "variations": "CAM emphasizes deep tonification up to 2 cun; Deadman emphasizes 1.0–1.5 cun with distal oblique angle for knee/leg pain.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "ST40 (Fenglong / 丰隆)",
        "front": "Location, categories, primary clinical specialization, and actions of ST40 (Fenglong / 丰隆).",
        "back": "Location: Lateral aspect of lower leg, 8 cun superior to the lateral malleolus, two fingerbreadths lateral to anterior tibial crest (one fingerbreadth lateral to ST38).\nPoint Categories: Luo-Connecting point of the Stomach channel.\n\nActions:\n• The PREMIER point in acupuncture for resolving ALL forms of Phlegm (both substantial phlegm in the lungs and non-substantial phlegm in the mind/joints/vessels).\n• Clears phlegm from chest (cough, asthma, profuse sputum).\n• Clears phlegm misting the mind (dizziness, manic depression, anxiety, vertigo).\n• Alleviates constipation, abdominal fullness, and lower extremity edema.\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.",
        "consensus": "Universal first-line point for any phlegm or dampness manifestation.",
        "variations": "Combine with SP9 for dampness; combine with LU7 for phlegm cough; combine with PC6 for phlegm misting the heart.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "ST44 (Neiting / 内庭)",
        "front": "Location, point categories, indications, and clinical actions of ST44 (Neiting / 内庭).",
        "back": "Location: On dorsum of foot, in the web depression between 2nd and 3rd toes, proximal to margin of web.\nPoint Categories: Ying-Spring and Water point of the Stomach channel; Heavenly Star point.\n\nActions:\n• Clears heat and fire from the Stomach channel and Yangming organ.\n• Premier point for Yangming excess heat: toothache, trigeminal neuralgia, facial swelling, sore throat, epistaxis, acid regurgitation, hunger with vomiting.\n• Clears damp-heat from intestines (dysentery, diarrhea, abdominal pain).\n\nNeedling:\n• Perpendicular or oblique insertion 0.5 - 0.8 cun directed proximally.",
        "consensus": "Chief distal point for Stomach fire manifesting in the mouth, teeth, gums, and face.",
        "variations": "Deadman notes its efficacy in clearing food stagnation heat in children.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "SP4 (Gongsun / 公孙)",
        "front": "Location, categories, clinical synergy, and indications of SP4 (Gongsun / 公孙).",
        "back": "Location: Medial aspect of foot, in the depression distal and inferior to the base of the 1st metatarsal bone.\nPoint Categories: Luo-Connecting point of Spleen; Master point of Chong Mai (paired with PC6).\n\nActions:\n• Fortifies Spleen and harmonizes middle jiao.\n• Regulates Chong Mai (Sea of Blood), calming rebellious Qi in chest and abdomen.\n• Treats acute/chronic epigastric pain, vomiting, diarrhea, food stagnation, and dysmenorrhea.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun.",
        "consensus": "Premier point for combined middle jiao gastrointestinal and gynecological blood disorders.",
        "variations": "Paired with PC6 to treat nausea, morning sickness, and epigastric oppression.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "SP6 (Sanyinjiao / 三阴交)",
        "front": "Intersection channels, indications, and pregnancy contraindications for SP6 (Sanyinjiao / 三阴交).",
        "back": "Location: 3 cun superior to the tip of medial malleolus, posterior to the medial border of the tibia.\nIntersection: Crossing point of the Three Leg Yin channels (Spleen, Liver, Kidney).\n\nActions:\n• Fortifies Spleen and resolves dampness.\n• Harmonizes Liver and tonifies Kidney Yin and Blood.\n• Regulates menstruation, treats dysmenorrhea, amenorrhea, leukorrhea, uterine bleeding.\n• Calms the Shen and treats insomnia.\n\n⚠️ Contraindication:\n• ABSOLUTELY CONTRAINDICATED in pregnancy due to strong uterine-stimulating action.\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.",
        "consensus": "The master gynecological, urinary, and digestive Yin point, strictly forbidden during pregnancy.",
        "variations": "Deadman emphasizes needling close to the posterior tibial border to elicit radiating sensation down to the sole.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "SP9 (Yinlingquan / 阴陵泉)",
        "front": "Location, categories, primary clinical specialization, and indications of SP9 (Yinlingquan / 阴陵泉).",
        "back": "Location: On medial aspect of lower leg, in the depression of the angle formed by the medial condyle of the tibia and posterior border of tibia.\nPoint Categories: He-Sea and Water point of the Spleen channel.\n\nActions:\n• The PREMIER point on the body for resolving all forms of Dampness (Damp-Heat, Cold-Damp, exterior/interior damp).\n• Opens and regulates water passages (edema, dysuria, urinary retention, enuresis).\n• Resolves dampness in lower jiao (leukorrhea, diarrhea, jaundice, knee pain/swelling).\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.",
        "consensus": "Number one point for draining water, treating edema, and resolving dampness.",
        "variations": "Paired with ST40: SP9 drains fluid dampness; ST40 resolves turbid phlegm.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "SP10 (Xuehai / 血海)",
        "front": "Location, primary clinical actions, and differential needling/moxa for SP10 (Xuehai / 血海).",
        "back": "Location: Medial aspect of thigh, 2 cun superior to the superior-medial border of patella, on the bulge of vastus medialis muscle.\n\nActions:\n• 'Sea of Blood' - Invigorates blood and dispels blood stasis.\n• Cools blood and stops uterine bleeding.\n• Clears heat from blood and relieves skin diseases (urticaria, eczema, pruritus, erysipelas).\n\nDifferentiation:\n• Needling with reduction: Clears blood heat, resolves stasis (dysmenorrhea, skin rashes).\n• Needling with tonification or moxa: Nourishes blood and regulates deficient menses.",
        "consensus": "Premier point for all blood-level pathology (Blood Heat, Blood Stasis, Blood Deficiency).",
        "variations": "Deadman notes: locating the point by placing the practitioner's right palm over the patient's left patella with thumb pointing to vastus medialis.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "HT3 (Shaohai / 少海)",
        "front": "Location, categories, indications, and needling depth for HT3 (Shaohai / 少海).",
        "back": "Location: With elbow flexed, at the midpoint of the line connecting the medial end of the cubital crease and medial epicondyle of the humerus.\nPoint Categories: He-Sea and Water point of the Heart channel.\n\nActions:\n• Clears heart fire and phlegm-fire, calms the Shen (mania, depression, epilepsy, memory loss).\n• Relaxes the sinews, unblocks channel, alleviates elbow and medial arm pain.\n• Clears axillary lymph node swelling and scrofula.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun.",
        "consensus": "Key He-Sea point for heart phlegm-fire and medial arm pain.",
        "variations": "Can be punctured through toward LI11 for upper extremity flaccidity and stroke recovery.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "HT7 (Shenmen / 神门)",
        "front": "Location, categories, actions, and anatomical precautions for HT7 (Shenmen / 神门).",
        "back": "Location: At the wrist crease, on the radial side of the flexor carpi ulnaris tendon, in the depression at the proximal border of the pisiform bone.\nPoint Categories: Shu-Stream, Yuan-Source, and Earth (son/sedation) point of Heart; Heavenly Star point.\n\nActions:\n• Premier point on the body for calming the Shen (mind) and nourishing Heart Blood/Yin.\n• Treats insomnia, anxiety, dream-disturbed sleep, palpitations, panic attacks, dementia.\n• Clears heart fire and regulates heart rhythm.\n\n⚠️ Anatomical Caution:\n• Perpendicular insertion 0.3 - 0.5 cun.\n• Do not needle too deeply or laterally to avoid the ulnar artery and ulnar nerve.",
        "consensus": "The single most widely used point for insomnia, anxiety, and mental-emotional stabilization.",
        "variations": "Deadman notes: needle on the radial side of the flexor carpi ulnaris tendon, avoid transfixing into the ulnar neurovascular bundle.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "SI3 (Houxi / 后溪)",
        "front": "Location, categories, clinical indications, and spine actions for SI3 (Houxi / 后溪).",
        "back": "Location: On ulnar border of hand, in the depression proximal to head of 5th metacarpal bone, at junction of red and white skin.\nPoint Categories: Shu-Stream and Wood (tonification) point of Small Intestine; Master point of Du Mai (paired with BL62).\n\nActions:\n• Master point of the Governing Vessel (Du Mai): Governs the entire spine, occiput, and neck.\n• Clears wind-heat, benefits head and eyes, relaxes sinews (stiff neck, torticollis, spine pain, epilepsy).\n• Clears sensory organ heat: red painful eyes, tinnitus, deafness.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun towards the 2nd metacarpal bone.",
        "consensus": "Premier distal point for acute cervical spine stiffness, occipital headache, and thoracic/lumbar spinal pain.",
        "variations": "Paired with BL62 to open Du Mai for spinal column disorders and daytime epilepsy.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL1 (Jingming / 睛明)",
        "front": "Location, indications, specialized insertion protocol, and safety precautions for BL1 (Jingming / 睛明).",
        "back": "Location: 0.1 cun superior to the inner canthus of the eye.\nCrossing point of Bladder, Small Intestine, Stomach, Gallbladder, Sanjiao, Yin Qiao, and Yang Qiao channels.\n\nActions:\n• Clears heat, expels wind, brightens the eyes.\n• Premier ophthalmic point: myopia, optic atrophy, cataract, conjunctivitis, glaucoma, night blindness.\n\n⚠️ Specialized Safety Protocol:\n• Instruct patient to keep eyes closed and look upwards/laterally.\n• Gently push eyeball laterally with finger to open medial orbital space.\n• Puncture slowly along medial orbital wall 0.5 - 1.0 cun WITHOUT lifting, thrusting, or twirling.\n• Upon withdrawal, immediately compress firmly with sterile cotton for 1 to 2 minutes WITHOUT rubbing to prevent retrobulbar hematoma.",
        "consensus": "Ophthalmic master point requiring strict non-manipulation technique and immediate compression.",
        "variations": "CAM restricts depth to 0.3–0.7 cun; Deadman allows up to 1.0 cun in experienced hands.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL13 (Feishu / 肺俞)",
        "front": "Location, point categories, indications, and safe needling angle for BL13 (Feishu / 肺俞).",
        "back": "Location: 1.5 cun lateral to lower border of spinous process of 3rd thoracic vertebra (T3).\nPoint Categories: Back-Shu point of the Lung.\n\nActions:\n• Tonifies Lung Qi and Lung Yin, clears lung heat, descends rebellious Qi.\n• Treats acute and chronic cough, asthma, bronchitis, hemoptysis, night sweats, bone-steaming fever.\n\n⚠️ Critical Safety Angle:\n• Puncture OBLIQUELY 0.5 - 0.8 cun towards the spine (medially).\n• Deep perpendicular insertion carries a high risk of penetrating the intercostal space and parietal pleura, causing Pneumothorax.",
        "consensus": "Chief point for chronic lung deficiency and respiratory pathology; strictly oblique needling.",
        "variations": "Never puncture perpendicularly or laterally.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL18 (Ganshu / 肝俞)",
        "front": "Location, categories, clinical indications, and needling safety for BL18 (Ganshu / 肝俞).",
        "back": "Location: 1.5 cun lateral to lower border of spinous process of 9th thoracic vertebra (T9).\nPoint Categories: Back-Shu point of the Liver.\n\nActions:\n• Harmonizes Liver Qi, nourishes Liver Blood, subdues Liver Yang, clears Liver Fire.\n• Benefits the eyes (blurriness, redness, night blindness).\n• Treats jaundice, hypochondriac pain, anger, depression, dizziness, epilepsy.\n\n⚠️ Needling Safety:\n• Puncture obliquely towards the spine 0.5 - 0.8 cun.\n• Deep perpendicular insertion risks pneumothorax.",
        "consensus": "Essential Back-Shu point for all physical and emotional Liver imbalances.",
        "variations": "Combine with BL19 (Danshu) to treat jaundice and hypochondriac distension.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL20 (Pishu / 脾俞)",
        "front": "Location, categories, clinical indications, and needling safety for BL20 (Pishu / 脾俞).",
        "back": "Location: 1.5 cun lateral to lower border of spinous process of 11th thoracic vertebra (T11).\nPoint Categories: Back-Shu point of the Spleen.\n\nActions:\n• Tonifies Spleen Qi and Spleen Yang, fortifies Stomach, transforms dampness.\n• Nourishes Blood (Spleen produces blood) and holds blood in vessels (chronic bleeding).\n• Treats poor appetite, abdominal distension, chronic loose stools, edema, prolapse, jaundice.\n\n⚠️ Needling Safety:\n• Puncture obliquely towards the spine 0.5 - 0.8 cun.\n• Deep perpendicular insertion risks pneumothorax.",
        "consensus": "Chief Back-Shu point for digestive weakness, chronic dampness, and post-heaven Qi production.",
        "variations": "Frequently combined with BL23 (Shenshu) for chronic fatigue and post-illness debility.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL23 (Shenshu / 肾俞)",
        "front": "Location, categories, clinical actions, and anatomical cautions for BL23 (Shenshu / 肾俞).",
        "back": "Location: 1.5 cun lateral to lower border of spinous process of 2nd lumbar vertebra (L2).\nPoint Categories: Back-Shu point of the Kidney.\n\nActions:\n• Premier point to tonify Kidney Yin, Kidney Yang, and Kidney Essence (Jing).\n• Strengthens lumbar spine, knees, bones, and teeth; benefits ears and hearing.\n• Treats lumbar pain, tinnitus, impotence, seminal emission, infertility, enuresis, asthma from kidney failure to grasp Qi.\n\n⚠️ Anatomical Cautions:\n• Puncture perpendicularly or slightly obliquely towards spine 0.8 - 1.2 cun.\n• Deep perpendicular insertion (>1.5 cun in thin patients) risks penetrating the kidney parenchyma.",
        "consensus": "Number one point for tonifying pre-heaven essence and treating chronic lumbar weakness.",
        "variations": "Moxa on BL23 is highly effective for Kidney Yang deficiency and cold lower back/knees.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL40 (Weizhong / 委中)",
        "front": "Location, categories, clinical indications, and bleeding therapy for BL40 (Weizhong / 委中).",
        "back": "Location: Exactly in midpoint of transverse popliteal crease, between tendons of biceps femoris and semitendinosus.\nPoint Categories: He-Sea and Earth point of Bladder; Gao Wu Command point of Lumbar region and Back; Heavenly Star point.\n\nActions:\n• Premier point on the body for ALL acute and chronic low back pain, lumbar strain, sciatica, and knee pain.\n• Clears heat from the blood and summer-heat.\n• Treats skin erysipelas, carbuncles, eczema, and sudden collapse from sunstroke.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun, or prick superficial popliteal veins with three-edged needle to bleed 5–10 drops for acute lumbar spasm or blood heat skin conditions.",
        "consensus": "The single most important distal point for the lumbar spine and back.",
        "variations": "Do not insert deeply into the popliteal artery/vein and tibial nerve running through the fossa.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL57 (Chengshan / 承山)",
        "front": "Location, primary clinical indications, and empirical specialization of BL57 (Chengshan / 承山).",
        "back": "Location: Posterior midline of leg, in the depression below the bellies of the gastrocnemius muscle, midway between BL40 and BL60.\n\nActions:\n• Relaxes sinews, activates channel, alleviates calf muscle spasms (nocturnal leg cramps).\n• EMPIRICAL MASTER POINT for treating Hemorrhoids (pain, bleeding, prolapse).\n• Treats lower back pain, sciatica, constipation, and heel pain.\n\nNeedling:\n• Perpendicular insertion 1.0 - 2.0 cun. De qi produces a strong sensation radiating into the foot or up the calf.",
        "consensus": "Chief empirical point for hemorrhoids and gastrocnemius cramping.",
        "variations": "Deadman highlights its dual action on the upper end of the channel (headache) and lower orifices (anus).",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL60 (Kunlun / 昆仑)",
        "front": "Location, categories, indications, and pregnancy contraindications for BL60 (Kunlun / 昆仑).",
        "back": "Location: In the depression between the tip of the external (lateral) malleolus and the Achilles tendon.\nPoint Categories: Jing-River and Fire point of Bladder; Heavenly Star point.\n\nActions:\n• Clears heat, descends Yang, dispels wind, activates the channel.\n• Premier point for occipital headache, stiff neck, lumbar spine pain, sciatica, ankle pain.\n• Promotes labor and descends Qi.\n\n⚠️ Contraindication:\n• CONTRAINDICATED in pregnancy due to strong downward Qi action and ability to induce uterine contractions.\n\nNeedling:\n• Perpendicular insertion 0.5 - 0.8 cun (or puncture through towards KI3).",
        "consensus": "Powerful distal pain reliever for the entire posterior spine; strictly forbidden in pregnancy.",
        "variations": "Can be through-punctured to KI3 for chronic ankle arthritis and heel pain.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "BL67 (Zhiyin / 至阴)",
        "front": "Location, categories, and moxibustion protocol for correcting breech fetus presentation for BL67 (Zhiyin / 至阴).",
        "back": "Location: Lateral aspect of little toe, 0.1 cun posterior to the corner of the nail.\nPoint Categories: Jing-Well and Metal point of the Bladder channel.\n\nActions:\n• Corrects malposition of the fetus (breech presentation).\n• Promotes labor and expels retained placenta.\n• Clears head, brightens eyes (vertex headache, eye pain).\n\n⚠️ Breech Moxibustion Protocol:\n• Applied at week 32 to 34 of pregnancy.\n• Indirect moxibustion (moxa stick) applied bilaterally for 15–20 minutes daily for 7 to 10 days.\n• Mechanism: Stimulates fetal adrenal cortex and increases uterine motility to rotate fetus.\n• Standard needling is contraindicated during early/mid pregnancy.",
        "consensus": "The most famous empirical point in Chinese medicine for turning breech fetus.",
        "variations": "Pricking to bleed is used for acute heat-stroke or vertex headache.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Cochrane Systematic Review on Moxa for Breech"])
    },
    {
        "category": "Meridians and Points",
        "title": "KI1 (Yongquan / 涌泉)",
        "front": "Location, categories, clinical indications, and root grounding action of KI1 (Yongquan / 涌泉).",
        "back": "Location: On sole of foot, between 2nd and 3rd metatarsal bones, approximately 1/3 the distance from web margin to heel in the plantar depression formed when foot is flexed.\nPoint Categories: Jing-Well and Wood (son/sedation) point of Kidney.\n\nActions:\n• The lowest point on the human body; grounds and pulls rebellious excess Yang/Fire downward.\n• Revives consciousness from fainting, shock, coma, stroke, epilepsy.\n• Subdues Liver Wind, severe hypertension, vertex headache, mania, severe insomnia.\n• Clears empty heat (night sweats, dry tongue, throat pain).\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun (very sensitive / painful area).",
        "consensus": "Premier grounding and emergency resuscitation point for rebellious ascending Yang/Wind.",
        "variations": "Herbal paste (e.g. Wu Zhu Yu mixed with vinegar) applied to KI1 is a famous external remedy for hypertension and mouth ulcers.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "KI3 (Taixi / 太溪)",
        "front": "Location, categories, clinical actions, and tonification versatility of KI3 (Taixi / 太溪).",
        "back": "Location: In the depression midway between the tip of the medial malleolus and the Achilles tendon.\nPoint Categories: Shu-Stream, Yuan-Source, and Earth point of Kidney; Heavenly Star point.\n\nActions:\n• The PREMIER point on the body for tonifying the Kidney (both Kidney Yin and Kidney Yang).\n• Nourishes Kidney Yin: treats night sweats, hot flashes, dry throat, toothache, tinnitus, insomnia.\n• Fortifies Kidney Yang: treats lower back pain, cold knees, impotence, frequent urination, asthma.\n• Strengthens the lumbar spine and anchors floating deficient Yang.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun (or puncture through towards BL60).",
        "consensus": "Number one source point for tonifying congenital pre-heaven Kidney essence.",
        "variations": "Puncturing through towards BL60 treats stubborn ankle and heel disorders.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "KI6 (Zhaohai / 照海)",
        "front": "Location, categories, clinical indications, and pairing with LU7 for KI6 (Zhaohai / 照海).",
        "back": "Location: 1 cun directly inferior to the prominence of the medial malleolus, in the groove below the talus.\nPoint Categories: Master point of Yin Qiao Mai (paired with LU7); Crossing point of Kidney and Yin Qiao.\n\nActions:\n• Nourishes Kidney Yin, clears deficiency heat, moistens dryness.\n• Premier point for chronic dry throat, hoarseness, chronic tonsillitis, and globus hystericus.\n• Master point of Yin Qiao Mai: treats somnolence (excess Yin Qiao) and insomnia (deficient Yin Qiao).\n• Regulates lower jiao: amenorrhea, dysmenorrhea, constipation from Yin dryness.\n\nNeedling:\n• Perpendicular insertion 0.3 - 0.5 cun.",
        "consensus": "Key point for nourishing fluid, moistening throat, and balancing sleep cycles.",
        "variations": "LU7 + KI6 synergy: LU7 opens the chest and throat; KI6 moistens the throat and nourishes Yin.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "KI7 (Fuliu / 复溜)",
        "front": "Location, categories, sweating regulation, and edema actions of KI7 (Fuliu / 复溜).",
        "back": "Location: 2 cun superior to KI3, on the anterior border of the Achilles tendon.\nPoint Categories: Jing-River, Metal, and Mother (tonification) point of the Kidney.\n\nActions:\n• Tonifies Kidney Yang and regulates water metabolism (edema, abdominal distension, dysuria).\n• THE PREMIER POINT FOR REGULATING SWEATING:\n  - To stop spontaneous sweating (Qi deficiency): Tonify KI7, Reduce LI4.\n  - To promote sweating in exterior diseases: Reduce KI7, Tonify LI4.\n  - To treat night sweats (Yin deficiency): Tonify KI7, Combine with HT6.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun.",
        "consensus": "Chief point for regulating sweat pores and water passages.",
        "variations": "Mother point of Kidney channel (Metal generates Water); used to nourish kidney in deficiency states.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "PC6 (Neiguan / 内关)",
        "front": "Location, categories, cardiac/gastrointestinal actions, and needling depth for PC6 (Neiguan / 内关).",
        "back": "Location: 2 cun proximal to transverse wrist crease, between tendons of palmaris longus and flexor carpi radialis.\nPoint Categories: Luo-Connecting point of Pericardium; Master point of Yin Wei Mai; Gao Wu Command point of Chest.\n\nActions:\n• Premier point for nausea, vomiting, morning sickness, motion sickness, and hiccup.\n• Unbinds the chest, regulates heart Qi, relieves angina, chest tightness, palpitations, and arrhythmias.\n• Calms the Shen: treats anxiety, insomnia, panic disorders, and depression.\n\n⚠️ Anatomical Precautions:\n• Perpendicular insertion 0.5 - 1.0 cun.\n• Deep insertion risks penetrating the Median Nerve (manifests as electric shock shooting into middle fingers; if felt, withdraw immediately).",
        "consensus": "The most widely researched acupuncture point worldwide for anti-emetic and cardiovascular regulation.",
        "variations": "Can be through-punctured to SJ5 for hemiplegia and severe chest/flank constraint.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "NIH Consensus Statement on Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "SJ5 (Waiguan / 外关)",
        "front": "Location, categories, clinical indications, and pairing with GB41 for SJ5 (Waiguan / 外关).",
        "back": "Location: 2 cun proximal to dorsal wrist crease, between the radius and ulna.\nPoint Categories: Luo-Connecting point of Sanjiao; Master point of Yang Wei Mai (paired with GB41).\n\nActions:\n• Expels exterior wind-heat, releases the exterior (febrile diseases, common cold, flu).\n• Clears head and ears (tinnitus, earache, migraine, temporal headache, red eyes).\n• Unblocks the channel and alleviates hypochondriac pain, intercostal neuralgia, and arm paresis.\n\nNeedling:\n• Perpendicular insertion 0.5 - 1.0 cun (or oblique through to PC6).",
        "consensus": "Chief point for exterior wind-heat, ear disorders, and Shaoyang meridian syndromes.",
        "variations": "Paired with GB41 to open Yang Wei Mai and Dai Mai for lateral body pain and migraine.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "GB20 (Fengchi / 风池)",
        "front": "Location, needling angle, and anatomical danger precautions for GB20 (Fengchi / 风池).",
        "back": "Location: In the depression between upper portions of sternocleidomastoid and trapezius muscles, level with DU16.\nCrossing point of Gallbladder, Sanjiao, Yang Wei Mai, and Yang Qiao Mai.\n\nActions:\n• Subdues internal and external Wind, clears head and eyes, benefits ears and hearing.\n• Premier point for all headaches (occipital, temporal), hypertension, dizziness, neck stiffness, sinusitis, rhinitis, common cold.\n\n⚠️ Safe Needling Angle:\n• Direct needle OBLIQUELY 0.8 - 1.2 cun towards the tip of patient's nose or opposite inner canthus.\n• CRITICAL DANGER: Deep perpendicular insertion directed superiorly or medially towards foramen magnum risks penetrating the brainstem (medulla oblongata) or spinal cord.",
        "consensus": "Master point for all head/neck wind disorders; strictly enforce safe angled insertion.",
        "variations": "CAM permits needle aimed towards the Adam's apple; Deadman recommends aiming at opposite eyeball for safest path.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "GB21 (Jianjing / 肩井)",
        "front": "Location, actions, pneumothorax risk, and pregnancy contraindications for GB21 (Jianjing / 肩井).",
        "back": "Location: Midway between DU14 (Dazhui / 大椎) and the acromion at the highest point of the shoulder trapezius.\nCrossing point of Gallbladder, Sanjiao, Stomach, and Yang Wei Mai.\n\nActions:\n• Relaxes shoulder sinews, relieves trapezius spasm, stiff neck, frozen shoulder.\n• Descends rebellious Qi, treats phlegm nodules, benefits breasts (breast abscess, promotes lactation).\n\n⚠️ Safety Rules & Contraindications:\n• PNEUMOTHORAX RISK: Puncture POSTERIOR-OBLIQUELY 0.5 - 0.8 cun. Deep perpendicular insertion carries a high risk of puncturing the lung apex.\n• PREGNANCY CONTRAINDICATION: Strictly contraindicated in pregnancy due to strong downward Qi dispersion that can precipitate miscarriage.",
        "consensus": "Universal shoulder pain point; strictly avoid perpendicular depth and avoid during pregnancy.",
        "variations": "Never needle perpendicularly in emaciated individuals or patients with COPD.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Royal TCM COM-06 Safety Handbook"])
    },
    {
        "category": "Meridians and Points",
        "title": "GB30 (Huantiao / 环跳)",
        "front": "Location, indications, specialized needle depth, and sciatic nerve de qi for GB30 (Huantiao / 环跳).",
        "back": "Location: At the junction of lateral 1/3 and medial 2/3 of the line connecting the prominence of the greater trochanter to the sacral hiatus (patient in lateral recumbent position with affected leg flexed).\nCrossing point of Gallbladder and Bladder channels.\n\nActions:\n• Master point for Sciatica, piriformis syndrome, lumbar pain radiating down the leg, hip pain, and hemiplegia.\n\nTechnique:\n• Perpendicular insertion with a 3.0 to 4.0 cun needle (depth: 2.0 - 3.5 cun).\n• Correct de qi manifests as a strong radiating sensation shooting down the posterior/lateral leg to the foot, confirming stimulation of the Sciatic Nerve.",
        "consensus": "The single most important local point for sciatica and hip arthralgia.",
        "variations": "Patient positioning is critical: must be in lateral decubitus with flexed upper hip and extended lower leg.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "GB34 (Yanglingquan / 阳陵泉)",
        "front": "Location, categories, tendon/sinew actions, and needling for GB34 (Yanglingquan / 阳陵泉).",
        "back": "Location: In the depression anterior and inferior to the head of the fibula.\nPoint Categories: He-Sea and Earth point of Gallbladder; Hui-Meeting point of Sinews / Tendons; Heavenly Star point.\n\nActions:\n• Master point of Sinews (Hui-Meeting of Tendons): Governs all tendons, ligaments, and muscular stiffness throughout the entire body.\n• Soothes Liver Qi, clears Gallbladder damp-heat, treats hypochondriac pain, jaundice, cholecystitis, bitter taste in mouth.\n• Premier local point for knee swelling, hemiplegia, sciatica, and foot drop.\n\nNeedling:\n• Perpendicular insertion 1.0 - 1.5 cun.",
        "consensus": "Universal point for all tendon, ligament, and soft tissue injuries.",
        "variations": "Pair with LV3 to smooth Liver Qi; pair with GB30 for lower extremity motor recovery.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "LV3 (Taichong / 太冲)",
        "front": "Location, categories, Liver Qi soothing, and hypertension actions for LV3 (Taichong / 太冲).",
        "back": "Location: On dorsum of foot, in the depression distal to the junction of the 1st and 2nd metatarsal bones.\nPoint Categories: Shu-Stream, Yuan-Source, and Earth point of Liver; Heavenly Star point.\n\nActions:\n• The PREMIER point on the body for spreading and soothing stagnant Liver Qi.\n• Subdues Liver Yang rising and clears Liver Fire: treats hypertension, migraines, red painful eyes, dizziness, irritability.\n• Nourishes Liver Blood and Liver Yin.\n• Regulates menstruation, treats dysmenorrhea, PMS, depression, insomnia, and spasms.\n\nNeedling:\n• Perpendicular or oblique insertion 0.5 - 1.0 cun towards the heel.",
        "consensus": "The most vital Liver point in clinical acupuncture; foundational member of the Four Gates.",
        "variations": "Can be through-punctured to KI1 on the plantar surface for acute hypertension crisis.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "LV2 (Xingjian / 行间)",
        "front": "Location, point categories, and primary clinical actions for LV2 (Xingjian / 行间).",
        "back": "Location: On dorsum of foot, between 1st and 2nd toes, in the depression 0.5 cun proximal to web margin.\nPoint Categories: Ying-Spring and Fire (son/sedation) point of Liver.\n\nActions:\n• PREMIER point for sedating and purging blazing Liver Fire.\n• Clears head and eyes (severe red painful eyes, burning temporal headache, bitter mouth, anger).\n• Clears heat from blood to stop uterine bleeding (menorrhagia, metrorrhagia).\n• Extinguishes Liver wind and clears lower jiao damp-heat (dysuria, genital pain).\n\nNeedling:\n• Oblique insertion 0.5 - 0.8 cun directed proximally.",
        "consensus": "Number one sedation point for Liver fire blazing.",
        "variations": "Sedation son point on Liver channel (Fire drains Wood).",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "LV13 (Zhangmen / 章门)",
        "front": "Location, point categories, and clinical actions for LV13 (Zhangmen / 章门).",
        "back": "Location: On lateral side of abdomen, directly below free end of 11th floating rib.\nPoint Categories: Front-Mu point of Spleen; Hui-Meeting point of Zang Organs; Crossing point of Liver and Gallbladder.\n\nActions:\n• Harmonizes Liver and Spleen, fortifies Spleen, resolves food stagnation.\n• Alleviates abdominal distension, diarrhea, borborygmi, hypochondriac pain.\n• Regulates middle and lower jiao Qi flow.\n\n⚠️ Safety:\n• Puncture transversely or obliquely 0.5 - 1.0 cun.\n• Deep perpendicular insertion on the right side risks penetrating the liver; on the left risks penetrating an enlarged spleen.",
        "consensus": "Master point for Liver overacting on Spleen (IBS, stress diarrhea).",
        "variations": "Always palpate for organomegaly before needling lateral abdominal wall.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "LV14 (Qimen / 期门)",
        "front": "Location, categories, clinical actions, and needling safety for LV14 (Qimen / 期门).",
        "back": "Location: On mamillary line, in 6th intercostal space, 4 cun lateral to anterior midline.\nPoint Categories: Front-Mu point of Liver; Crossing point of Liver, Spleen, and Yin Wei Mai.\n\nActions:\n• Harmonizes Liver and Stomach, promotes smooth flow of Liver Qi.\n• Clears heat and blood stasis in chest/hypochondrium (intercostal neuralgia, pleurisy, hepatitis).\n• Treats breast distension, PMS, nausea, hiccup, acid regurgitation.\n\n⚠️ Critical Safety:\n• Puncture OBLIQUELY 0.5 - 0.8 cun along the intercostal space.\n• Deep perpendicular insertion carries a high risk of Pneumothorax, or penetrating liver (right) or spleen (left).",
        "consensus": "Premier Front-Mu point for hypochondriac fullness and Liver-Stomach disharmony.",
        "variations": "Never needle perpendicularly into the 6th intercostal space.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "REN4 (Guanyuan / 关元)",
        "front": "Location, categories, tonification actions, and safety cautions for REN4 (Guanyuan / 关元).",
        "back": "Location: On anterior midline of lower abdomen, 3 cun inferior to umbilicus (2 cun superior to pubic symphysis).\nPoint Categories: Front-Mu point of Small Intestine; Crossing point of Ren Mai and 3 Leg Yin (Spleen, Liver, Kidney); Gate of Yuan Qi.\n\nActions:\n• Premier point on the body for tonifying Yuan (Original) Qi, Kidney Yang, and Kidney Essence (Jing).\n• Warms the uterus, regulates menstruation, treats infertility, amenorrhea, dysmenorrhea.\n• Tonifies lower jiao: impotence, enuresis, chronic diarrhea, extreme exhaustion.\n\n⚠️ Safety Rules:\n• Puncture perpendicularly 0.8 - 1.5 cun.\n• Mandatory rule: Patient must empty urinary bladder before needling to avoid bladder puncture.\n• Strictly contraindicated in pregnancy.",
        "consensus": "Universal powerhouse for tonifying root vitality and warming Mingmen fire.",
        "variations": "Heavy moxibustion on REN4 is the premier method to rescue collapsed Yang in chronic fatigue and cold collapse.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "REN6 (Qihai / 气海)",
        "front": "Location, point categories, and clinical actions of REN6 (Qihai / 气海).",
        "back": "Location: On anterior midline, 1.5 cun inferior to umbilicus.\nPoint Categories: 'Sea of Qi' (Qihai).\n\nActions:\n• Tonifies Qi and Yang, fosters Yuan Qi, regulates Qi dynamics.\n• Treats general deficiency, fatigue, weakness, abdominal distension, diarrhea, organ prolapse.\n• Regulates menstruation and lower jiao urination (dysuria, enuresis).\n\nNeedling:\n• Perpendicular insertion 0.8 - 1.2 cun after emptying bladder.\n• Moxibustion is strongly indicated for Qi and Yang deficiency.",
        "consensus": "Chief point for general Qi tonification alongside ST36.",
        "variations": "REN6 tonifies Qi primarily; REN4 tonifies Essence and Yang primarily.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "REN12 (Zhongwan / 中脘)",
        "front": "Location, categories, clinical indications, and needling safety for REN12 (Zhongwan / 中脘).",
        "back": "Location: On anterior midline, 4 cun superior to umbilicus (midway between umbilicus and sternocostal angle).\nPoint Categories: Front-Mu point of Stomach; Hui-Meeting point of Fu Organs; Crossing point of Ren Mai, Small Intestine, Sanjiao, and Stomach.\n\nActions:\n• Master point for ALL Middle Jiao diseases (Stomach and Spleen).\n• Harmonizes Stomach, descends rebellious Qi, fortifies Spleen, resolves food stagnation and phlegm.\n• Treats epigastric pain, nausea, vomiting, acid reflux, abdominal fullness, diarrhea.\n\n⚠️ Safety:\n• Perpendicular insertion 0.8 - 1.2 cun.\n• Deep needle insertion risks penetrating the peritoneal cavity or left lobe of liver/distended stomach.",
        "consensus": "The single most important Front-Mu and local point for all digestive disorders.",
        "variations": "Combine with ST36 and PC6 as the universal triad for upper digestive disharmonies.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "REN17 (Danzhong / 膻中)",
        "front": "Location, categories, clinical actions, and needling angle for REN17 (Danzhong / 膻中).",
        "back": "Location: On anterior midline of sternum, level with 4th intercostal space (midpoint between the nipples in males).\nPoint Categories: Front-Mu point of Pericardium; Hui-Meeting point of Qi; Sea of Qi; Crossing point of Ren, Spleen, Kidney, Small Intestine, Sanjiao.\n\nActions:\n• The PREMIER point for regulating, unbinding, and tonifying Qi in the Upper Jiao (Zong Qi).\n• Unbinds chest, descends lung Qi, alleviates cough, asthma, chest pain, palpitations, dysphagia.\n• Regulates breast Qi and promotes lactation (insufficient lactation, mastitis).\n\n⚠️ Technique & Safety:\n• Puncture TRANSVERSELY / SUBCUTANEOUSLY 0.3 - 0.5 cun superiorly or inferiorly along the sternal bone.\n• NEVER puncture perpendicularly (risk of penetrating the sternal foramen in patients with congenital sternal defects, risking cardiac puncture).",
        "consensus": "Chief point for psycho-emotional chest oppression, panic, and lactation regulation.",
        "variations": "Congenital sternal foramen occurs in 5–10% of population; perpendicular needling can cause cardiac tamponade.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture", "Royal TCM COM-06 Safety Handbook"])
    },
    {
        "category": "Meridians and Points",
        "title": "DU4 (Mingmen / 命门)",
        "front": "Location, clinical indications, and moxibustion actions of DU4 (Mingmen / 命门).",
        "back": "Location: On posterior midline, in the depression below spinous process of 2nd lumbar vertebra (L2) (level with BL23).\nPoint Categories: 'Gate of Life' (Mingmen).\n\nActions:\n• Tonifies Original Yang, warms Mingmen Fire, strengthens Kidney Yang.\n• Strengthens lumbar spine and knees, relieves cold lower back pain.\n• Treats sexual dysfunction (impotence, premature ejaculation), infertility, clear profuse urination, dawn diarrhea.\n\nTechnique:\n• Perpendicular insertion 0.5 - 1.0 cun, or slight oblique-superior insertion.\n• Moxibustion (direct, moxa box, or ginger moxa) is premier therapy for Kidney Yang exhaustion.",
        "consensus": "Chief spinal point for warming life-gate fire and treating constitutional cold.",
        "variations": "Level with bilateral BL23 (Shenshu); frequently used together with moxa.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Meridians and Points",
        "title": "DU14 (Dazhui / 大椎)",
        "front": "Location, categories, fever clearing, and immune actions for DU14 (Dazhui / 大椎).",
        "back": "Location: On posterior midline, in depression below spinous process of 7th cervical vertebra (C7).\nPoint Categories: Meeting point of Du Mai with all Six Yang Channels; Sea of Qi.\n\nActions:\n• PREMIER point for clearing high fever and releasing all Yang excess heat (febrile diseases, sunstroke, malaria).\n• Tones and warms Yang Qi when combined with moxibustion (chronic deficiency, asthma, cold aversion).\n• Clears wind-heat, treats stiff neck, cervical spondylosis, upper respiratory infections.\n\nNeedling:\n• Perpendicular-oblique insertion slightly superiorly 0.5 - 1.0 cun.\n• Prick to bleed with three-edged needle and cup for rapid reduction of acute high fever.",
        "consensus": "Universal master point for thermal regulation: clears excess heat with needle/bleeding; tonifies Yang with moxa.",
        "variations": "C7 spinous process rotates when patient turns head, whereas T1 remains fixed.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "DU20 (Baihui / 百会)",
        "front": "Location, categories, dual action (raising vs subduing), and technique for DU20 (Baihui / 百会).",
        "back": "Location: On vertex of head, 5 cun posterior to anterior hairline, at midpoint of line connecting apex of both ears.\nPoint Categories: Meeting point of Du Mai with Bladder, Gallbladder, Sanjiao, and Liver channels; Sea of Marrow.\n\nActions & Dual Dynamics:\n• Raises Sinking Yang Qi: When needled or moxa'd with tonification, lifts prolapsed organs (rectum, uterus, stomach), treats chronic diarrhea, clear Yang failing to ascend.\n• Calms the Shen & Subdues Liver Wind: When needled with sedation or bled, clears head, subdues internal wind, calms agitation, treats headache, dizziness, hypertension, mania.\n\nTechnique:\n• Transverse / subcutaneous insertion 0.5 - 0.8 cun anteriorly (to raise Qi) or posteriorly.",
        "consensus": "Master point of the vertex; bidirectional regulator of Yang Qi and mental consciousness.",
        "variations": "Surrounded by the four Sishencong points for enhanced cognitive and sleep regulation.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual", "Maciocia Foundations"])
    },
    {
        "category": "Meridians and Points",
        "title": "DU26 (Shuigou / 水沟)",
        "front": "Location, categories, resuscitation actions, and emergency protocol for DU26 (Shuigou / 水沟).",
        "back": "Location: At junction of upper 1/3 and lower 2/3 of philtrum, below the nose.\nPoint Categories: Gao Wu Command point for Resuscitation; Crossing point of Du Mai, Large Intestine, and Stomach.\n\nActions:\n• THE PREMIER EMERGENCY RESUSCITATION POINT on the human body.\n• Restores consciousness from fainting, syncope, shock, coma, stroke, sunstroke, epilepsy.\n• Calms manic behavior and emotional distress.\n• Distal point for acute lumbar sprain (activates spinal Du Mai).\n\nTechnique:\n• Puncture obliquely upward towards nasal septum 0.3 - 0.5 cun with vigorous pecking/reducing manipulation until patient sheds tears or revives.\n• In emergency without needles: Press firmly with thumbnail into philtrum.",
        "consensus": "Universal first-line point for medical emergencies and consciousness restoration.",
        "variations": "Must elicit strong painful de qi to trigger sympathetic autonomic awakening.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "Extra Points: Yintang, Taiyang, and Sishencong",
        "front": "Specify locations, clinical indications, and needling methods for Extra Points Yintang (印堂), Taiyang (太阳), and Sishencong (四神聪).",
        "back": "Extra Points of the Head:\n1. Yintang (EX-HN3 - 印堂 / Hall of Impression):\n   - Location: Midway between the medial ends of the two eyebrows.\n   - Actions: Calms the Shen, induces sleep, treats frontal headache, sinusitis, rhinitis, infantile convulsions.\n   - Technique: Transverse/subcutaneous pinch and needle inferiorly 0.3 - 0.5 cun.\n\n2. Taiyang (EX-HN5 - 太阳 / Supreme Yang):\n   - Location: In the depression 1 fingerbreadth posterior to midpoint between outer canthus and lateral eyebrow.\n   - Actions: Clears Shaoyang heat, treats migraine, temporal headache, red painful eyes, toothache, facial paralysis.\n   - Technique: Perpendicular 0.5–0.8 cun, or prick to bleed for acute migraine/conjunctivitis.\n\n3. Sishencong (EX-HN1 - 四神聪 / Four Alert Spirits):\n   - Location: Group of 4 points on vertex, each 1.0 cun anterior, posterior, and bilateral to DU20 (Baihui / 百会).\n   - Actions: Calms Shen, sharpens memory, treats insomnia, dementia, vertigo, epilepsy.\n   - Technique: Transverse insertion 0.5 - 1.0 cun directed towards DU20.",
        "consensus": "Crucial trio of head extra points for neurological, ophthalmic, and psycho-emotional disorders.",
        "variations": "Pricking Taiyang to express 3–5 drops of blood gives dramatic immediate relief for acute throbbing migraines.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Meridians and Points",
        "title": "Extra Points: Huatuojiaji (华佗夹脊)",
        "front": "Location, spinal segmental relationship, and needling protocol for Huatuojiaji (华佗夹脊).",
        "back": "Huatuojiaji (EX-B2 - 华佗夹脊 / Hua Tuo's Paravertebral Points):\n• Location:\n  - 34 points in total, located bilaterally 0.5 cun lateral to the lower border of each spinous process from the 1st thoracic (T1) down to the 5th lumbar (L5) vertebra.\n\n• Segmental Innervation & Organ Correspondence:\n  - Points directly correspond to the spinal nerve roots and sympathetic chain:\n  - Upper Thoracic (T1–T4): Treats diseases of the Heart, Lungs, and Upper Limbs.\n  - Middle Thoracic (T5–T8): Treats diseases of the Liver, Gallbladder, Spleen, and Stomach.\n  - Lower Thoracic (T9–T12): Treats diseases of the Kidneys, Intestines, and Urinary Bladder.\n  - Lumbar (L1–L5): Treats lower back, pelvic organs, and Lower Limbs.\n\n• Needling Technique:\n  - Puncture perpendicularly 0.5 - 1.0 cun towards the spine (cervical/thoracic) or 1.0 - 1.5 cun (lumbar).\n  - Sensation: Radiates along intercostal nerves or down spinal column.",
        "consensus": "Bridging landmark between classical acupuncture and modern neuro-segmental medicine.",
        "variations": "Never needle deep perpendicularly laterally to avoid penetrating the thoracic pleura.",
        "sources": json.dumps(["Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    }
]

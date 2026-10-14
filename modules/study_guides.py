"""Printable Study Guides & Pocket Cheat Sheets (可打印学习手册与核心速查卡).

Provides 15 high-yield, comprehensive clinical reference matrices for NCCAOM and Pan-Canadian board exams:
1. Top 50 Essential Clinical Acupoints Pocket Matrix (Full 50 Points with search & filter)
2. Emergency Acupoints & Clinical Shock / Complication Protocols (15 protocols)
3. Five Shu Points & Mother-Child Tonification/Sedation Matrix (All 12 channels + Ben Horary points)
4. Yuan-Source & Luo-Connecting Master Host-Guest (Zhu-Ke) Pairing Table
5. Eight Confluent Points of Extraordinary Vessels (Coupled pairs, pathways & regional control)
6. Sixteen Xi-Cleft Points & Acute Pain / Hemorrhage Matrix (12 Regular + 4 Extraordinary)
7. Front-Mu & Back-Shu Master Combination Matrix (12 Zang-Fu organs & spinal levels)
8. Eight Influential (Hui-Meeting), Six Command & Lower He-Sea Master Guide
9. Extra Points (经外奇穴) Master Board Matrix (Anatomy, depths & indications)
10. Tongue Diagnosis Master Matrix (Body color, shape, coating, moisture & topography)
11. 28 Canonical Pulses Diagnostic Differential Matrix
12. Medical Red Flags & Urgent Hospital Referral Guide (Biomedical emergencies)
13. Pharmacology & Herb-Drug Interactions Master Matrix
14. Acupuncture Modalities: Electroacupuncture, Scalp Somatotopic Lines, Auricular & Moxa
15. Root vs Manifestation (Ben & Biao) & Treatment Principles Matrix
"""

from typing import Dict, List, Any
import streamlit as st

def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line so Streamlit markdown never creates <pre><code> blocks."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# =============================================================================
# 1. TOP 50 ESSENTIAL CLINICAL ACUPOINTS (COMPLETE DATASET)
# =============================================================================
TOP_50_ESSENTIAL_POINTS = [
    {
        "code": "LI4",
        "name": "Hegu",
        "chinese": "合谷",
        "channel": "Large Intestine (Hand Yangming)",
        "meridian_group": "Large Intestine",
        "category": "Yuan-Source Point; Gao Wu Command Point for Face & Mouth; Heavenly Star Point",
        "location": "On the dorsum of the hand, radial to the midpoint of the 2nd metacarpal bone, in the belly of the 1st dorsal interosseous muscle.",
        "needling": "Perpendicular insertion 0.5–1.0 cun. ⚠️ ABSOLUTE CONTRAINDICATION IN PREGNANCY (strongly downbears Qi and stimulates uterine contraction).",
        "functions": "Expels exterior Wind; supreme analgesic for all pain in the head, face, jaw, and sensory orifices; harmonizes Yin and Wei; clears heat.",
        "key_indications": "Headaches (frontal, tension), toothache, rhinitis, sinusitis, facial paralysis (Bell's palsy), sore throat, fever, amenorrhea, delayed labor.",
        "golden_pairings": "• Four Gates (Si Guan): LI4 + LV3 (strongly moves stagnant Qi and Blood throughout entire body)\n• Face/Mouth Command: LI4 + ST44 (severe toothache and facial heat)\n• Sweating Regulation: LI4 + KD7 (LI4 tonify + KD7 sedate to induce sweat; LI4 sedate + KD7 tonify to stop night sweats)\n• Exterior Wind-Heat: LI4 + LI11 + GV14",
        "board_pearl": "Most frequently tested point on board exams for pregnancy needling contraindications and Gao Wu Command Point associations."
    },
    {
        "code": "ST36",
        "name": "Zusanli",
        "chinese": "足三里",
        "channel": "Stomach (Foot Yangming)",
        "meridian_group": "Stomach",
        "category": "He-Sea Point (Earth); Gao Wu Command Point for Abdomen; Heavenly Star Point; Sea of Nourishment",
        "location": "3 cun inferior to ST35 (Dubi), one finger-breadth lateral to the anterior crest of the tibia, in the tibialis anterior muscle.",
        "needling": "Perpendicular insertion 1.0–1.5 cun. Moxa highly recommended for tonification and longevity.",
        "functions": "Supreme point for tonifying Post-Heaven Qi and Blood; fortifies Spleen and harmonizes Stomach; boosts Wei Qi and immune stamina; brightens eyes.",
        "key_indications": "Epigastric pain, nausea, vomiting, abdominal distension, diarrhea, chronic fatigue, general debility, anemia, knee pain.",
        "golden_pairings": "• Tonify Qi & Blood: ST36 + SP6 + RN12\n• Abdominal Fullness / Diarrhea: ST36 + ST25 + RN12\n• Boost Immune Wei Qi: ST36 + RN6 + BL20 (with moxibustion)",
        "board_pearl": "Known as the 'Three Mile Leg' point. Historically used by soldiers to march an extra 3 miles when exhausted."
    },
    {
        "code": "SP6",
        "name": "Sanyinjiao",
        "chinese": "三阴交",
        "channel": "Spleen (Foot Taiyin)",
        "meridian_group": "Spleen",
        "category": "Crossing Point of the Three Leg Yin Meridians (Spleen, Liver, Kidney); Heavenly Star Point",
        "location": "3 cun superior to the tip of the medial malleolus, directly posterior to the medial border of the tibia.",
        "needling": "Perpendicular insertion 1.0–1.5 cun. ⚠️ STRICTLY CONTRAINDICATED IN PREGNANCY (induces uterine contractions and cervical dilation).",
        "functions": "Fortifies Spleen and transforms dampness; nourishes Liver Blood and Kidney Yin; regulates menstruation and induces labor; harmonizes Lower Jiao.",
        "key_indications": "Dysmenorrhea, irregular menses, amenorrhea, uterine bleeding, infertility, delayed labor, insomnia, abdominal distension, loose stools, dysuria.",
        "golden_pairings": "• Supreme Gynecological Pair: SP6 + RN4 + LV3\n• Nourish Blood & Calm Spirit: SP6 + HT7 + BL15\n• Resolve Dampness & Edema: SP6 + SP9 + RN9",
        "board_pearl": "Number one point for all gynecological and obstetrical disorders; must never be needled in pregnant patients prior to full-term labor."
    },
    {
        "code": "LV3",
        "name": "Taichong",
        "chinese": "太冲",
        "channel": "Liver (Foot Jueyin)",
        "meridian_group": "Liver",
        "category": "Shu-Stream Point (Earth); Yuan-Source Point; Heavenly Star Point",
        "location": "On the dorsum of the foot, in the depression distal to the junction of the 1st and 2nd metatarsal bones.",
        "needling": "Perpendicular or oblique-proximal insertion 0.5–1.0 cun. Avoid puncturing the dorsalis pedis artery.",
        "functions": "Spreads stagnant Liver Qi; subdues Liver Yang rising and internal Wind; nourishes Liver Blood and Yin; clears head and eyes; regulates menstruation.",
        "key_indications": "Headache (vertex, temporal), dizziness, vertigo, irritability, emotional depression, anger, eye redness and pain, hypochondriac pain, dysmenorrhea, hypertension.",
        "golden_pairings": "• Four Gates (Si Guan): LV3 + LI4 (opens all 12 channels, releases systemic stasis)\n• Subdue Liver Yang: LV3 + GB20 + KD3\n• Regulate Liver Qi & Stomach: LV3 + PC6 + RN12",
        "board_pearl": "The supreme point in the body for resolving emotional constraint, frustration, and stagnation of Liver Qi."
    },
    {
        "code": "PC6",
        "name": "Neiguan",
        "chinese": "内关",
        "channel": "Pericardium (Hand Jueyin)",
        "meridian_group": "Pericardium",
        "category": "Luo-Connecting Point; Confluent Master Point of the Yin Wei Mai (coupled with SP4); Heavenly Star Point",
        "location": "2 cun proximal to the anterior wrist crease (PC7), between the tendons of palmaris longus and flexor carpi radialis.",
        "needling": "Perpendicular insertion 0.5–1.0 cun, or oblique proximal. Caution: direct deep needling may hit median nerve (electric shock sensation).",
        "functions": "Unbinds the chest and regulates Heart Qi; harmonizes Stomach and arrests nausea/vomiting; calms the Shen; opens Yin Wei Mai.",
        "key_indications": "Nausea, vomiting, morning sickness, motion sickness, epigastric fullness, angina, chest tightness, palpitations, anxiety, insomnia, depression.",
        "golden_pairings": "• Master of Chest & Stomach: PC6 + SP4 (opens Yin Wei Mai & Chong Mai)\n• Severe Nausea & Vomiting: PC6 + ST36 + RN12\n• Calm Shen & Palpitations: PC6 + HT7 + RN17",
        "board_pearl": "FDA-recognized and WHO-validated point for post-operative, chemotherapy-induced, and pregnancy nausea."
    },
    {
        "code": "LU7",
        "name": "Lieque",
        "chinese": "列缺",
        "channel": "Lung (Hand Taiyin)",
        "meridian_group": "Lung",
        "category": "Luo-Connecting Point; Confluent Master Point of Ren Mai (coupled with KD6); Gao Wu Command Point for Head & Nape; Heavenly Star Point",
        "location": "1.5 cun proximal to the radial styloid process, in the cleft between the tendons of brachioradialis and abductor pollicis longus.",
        "needling": "Oblique insertion 0.5–0.8 cun proximally or distally. Caution: avoid the cephalic vein and radial artery.",
        "functions": "Releases the exterior and expels Wind; diffuses Lung Qi and descends phlegm; opens Ren Mai; clears head and nape; regulates water passages.",
        "key_indications": "Exterior wind-cold/wind-heat, chills and fever, cough, asthma, wheezing, occipital headache, stiff neck, facial paralysis, sore throat, enuresis.",
        "golden_pairings": "• Head & Nape Command: LU7 + BL10 + GB20\n• Open Ren Mai (Throat & Lungs): LU7 + KD6\n• Exterior Wind-Cold: LU7 + LI4 + BL13",
        "board_pearl": "Test of location: interlock thumbs and index fingers of both hands; LU7 lies directly under the tip of the index finger in the styloid notch."
    },
    {
        "code": "GB20",
        "name": "Fengchi",
        "chinese": "风池",
        "channel": "Gallbladder (Foot Shaoyang)",
        "meridian_group": "Gallbladder",
        "category": "Crossing point of Gallbladder and San Jiao with Yang Wei Mai and Yang Qiao Mai",
        "location": "In the depression between the upper portion of sternocleidomastoid and trapezius muscles, level with DU16 (Fengfu).",
        "needling": "Oblique insertion 0.8–1.2 cun directed towards the tip of the nose or opposite eye. ⚠️ CAUTION: Deeper perpendicular insertion towards spinal canal risks puncturing medulla oblongata.",
        "functions": "Eliminates interior and exterior Wind; clears head and sensory orifices; benefits eyes, ears, and throat; subdues Liver Yang; relaxes neck sinews.",
        "key_indications": "Occipital headache, migraine, neck stiffness, cervical spondylosis, dizziness, vertigo, hypertension, common cold, sinusitis, tinnitus, red painful eyes.",
        "golden_pairings": "• Occipital Headache & Wind: GB20 + DU16 + LU7 + BL10\n• Liver Yang Rising Vertigo: GB20 + LV3 + KD3 + Taiyang\n• Red Painful Eyes: GB20 + Taiyang + LI4 + LV2",
        "board_pearl": "The premier point on the body for eliminating Wind from the head, neck, and brain."
    },
    {
        "code": "BL40",
        "name": "Weizhong",
        "chinese": "委中",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "He-Sea Point (Earth); Gao Wu Command Point for Lumbar Spine & Back; Heavenly Star Point",
        "location": "At the midpoint of the transverse popliteal crease, between the tendons of biceps femoris and semitendinosus.",
        "needling": "Perpendicular insertion 0.5–1.0 cun, or prick popliteal venules with three-edged needle to bleed. Caution: avoid popliteal artery and tibial nerve.",
        "functions": "Clears heat and cools blood; eliminates blood stasis; relaxes sinews and clears obstruction along the entire Taiyang meridian; treats lumbar spine.",
        "key_indications": "Acute and chronic lower back pain, sciatica, lumbar sprain, knee stiffness and pain, heatstroke, erysipelas, furuncles, urticaria, acute vomiting/diarrhea.",
        "golden_pairings": "• Lumbar & Back Command: BL40 + BL23 + Yaotongxue\n• Bleed for Blood Heat & Toxic Skin Rash: BL40 (bleed) + LI11 + SP10\n• Acute Lumbar Sprain: BL40 + DU26",
        "board_pearl": "Classical dictum: 'For lumbar pain and backache, seek Weizhong' (腰背委中求)."
    },
    {
        "code": "BL23",
        "name": "Shenshu",
        "chinese": "肾俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Kidney (肾之背俞穴)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 2nd lumbar vertebra (L2).",
        "needling": "Perpendicular or slightly oblique-medial insertion 0.8–1.2 cun. ⚠️ CAUTION: Deep lateral insertion risks puncturing the kidney parenchyma.",
        "functions": "Tonifies Kidney Yin, Kidney Yang, and Jing essence; strengthens lumbar spine, bones, and knees; benefits ears and eyes; regulates water passages.",
        "key_indications": "Chronic low back pain, weak knees, nocturnal emission, impotence, premature ejaculation, irregular menses, tinnitus, deafness, edema, asthma.",
        "golden_pairings": "• Tonify Kidney Yin & Yang: BL23 + KD3 + DU4 (Mingmen)\n• Chronic Lumbar Deficiency: BL23 + DU4 + BL40\n• Water Metabolism & Edema: BL23 + RN9 + SP9",
        "board_pearl": "The supreme Back-Shu point for constitutional stamina, reproductive vitality, and skeletal health."
    },
    {
        "code": "KD3",
        "name": "Taixi",
        "chinese": "太溪",
        "channel": "Kidney (Foot Shaoyin)",
        "meridian_group": "Kidney",
        "category": "Shu-Stream Point (Earth); Yuan-Source Point; Heavenly Star Point",
        "location": "In the depression between the tip of the medial malleolus and the Achilles tendon, level with the prominence of the medial malleolus.",
        "needling": "Perpendicular insertion 0.5–1.0 cun, directed towards BL60. Avoid puncturing the posterior tibial artery and vein.",
        "functions": "Nourishes Kidney Yin and anchors floating deficient Yang; tonifies Kidney Yang; clears empty heat; strengthens lumbar spine; benefits throat.",
        "key_indications": "Chronic sore dry throat, toothache from empty heat, tinnitus, deafness, insomnia, night sweats, low back soreness, impotence, frequent urination, asthma.",
        "golden_pairings": "• Nourish Kidney Yin & Anchor Yang: KD3 + LV3 + SP6\n• Chronic Deficient Sore Throat: KD3 + LU7 + KD6\n• Through-and-Through Ankle Needling: KD3 through to BL60 (Taixi through Kunlun)",
        "board_pearl": "The premier Yuan-Source point that simultaneously nourishes Kidney Yin and warms Kidney Yang."
    },
    {
        "code": "HT7",
        "name": "Shenmen",
        "chinese": "神门",
        "channel": "Heart (Hand Shaoyin)",
        "meridian_group": "Heart",
        "category": "Shu-Stream Point (Earth); Yuan-Source Point; Child / Sedation Point of Heart; Heavenly Star Point",
        "location": "At the wrist crease, on the radial side of the flexor carpi ulnaris tendon, in the depression at the proximal border of the pisiform bone.",
        "needling": "Perpendicular insertion 0.3–0.5 cun. Avoid puncturing the ulnar artery and nerve.",
        "functions": "Calms the Shen (spirit) and quiets the Heart; nourishes Heart Blood; clears Heart Heat; unbinds chest tightness.",
        "key_indications": "Insomnia, frequent dreaming, palpitations, anxiety, panic attacks, memory impairment, mania, disorientation, chest pain, epilepsy.",
        "golden_pairings": "• Supreme Shen Calming Pair: HT7 + SP6 + PC6\n• Heart Fire / Night Sweats: HT7 + KD3 + HT6\n• Palpitations with Blood Deficiency: HT7 + BL15 + BL20",
        "board_pearl": "Named 'Spirit Gate'. Number one point for psycho-emotional distress and intractable insomnia."
    },
    {
        "code": "DU20",
        "name": "Baihui",
        "chinese": "百会",
        "channel": "Governing Vessel (Du Mai)",
        "meridian_group": "Du Mai (GV)",
        "category": "Meeting point of Du Mai with Bladder, Gallbladder, San Jiao, and Liver meridians; Sea of Marrow",
        "location": "At the vertex of the head, 5 cun posterior to the anterior hairline, on the midline (midpoint of line connecting ear apexes).",
        "needling": "Subcutaneous / transverse insertion 0.5–0.8 cun anteriorly or posteriorly. Moxa highly effective for raising Yang.",
        "functions": "Raises sunken Yang Qi; stabilizes prolapse; clears the mental senses and calms Shen; eliminates internal wind; benefits brain.",
        "key_indications": "Uterine/rectal prolapse, gastroptosis, chronic diarrhea from sunken Spleen Yang, dizziness, vertex headache, depression, memory loss, stroke hemiplegia.",
        "golden_pairings": "• Raise Sunken Yang Qi: DU20 + RN6 + ST36 (with moxibustion)\n• Clear Brain Fog & Boost Focus: DU20 + Sishencong + Yintang\n• Subdue Wind & Liver Yang: DU20 + LV3 + GB20",
        "board_pearl": "Meeting of One Hundred Channels. Needled posteriorly to sedate Yang; needled anteriorly with moxa to raise sunken Yang."
    },
    {
        "code": "RN12",
        "name": "Zhongwan",
        "chinese": "中脘",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Front-Mu Point of Stomach (胃之募穴); Hui-Meeting Point of the Fu Organs (腑会中脘)",
        "location": "On the anterior midline of the upper abdomen, 4 cun superior to the umbilicus (midpoint between umbilicus and sternocostal angle).",
        "needling": "Perpendicular insertion 0.8–1.2 cun. ⚠️ CAUTION: Deep insertion risks puncturing peritoneal cavity, left lobe of liver, or transverse colon in thin patients.",
        "functions": "Harmonizes Stomach and fortifies Spleen; regulates Middle Jiao Qi; transforms dampness and phlegm; stops nausea and vomiting.",
        "key_indications": "Epigastric pain, acid reflux, GERD, nausea, vomiting, abdominal distension, food stagnation, poor appetite, diarrhea, dysentery, insomnia from full stomach.",
        "golden_pairings": "• Harmonize Stomach & Dissolve Food Stagnation: RN12 + ST36 + PC6\n• Front-Mu & Back-Shu Pair for Stomach: RN12 + BL21 (Weishu)\n• Phlegm in Middle Burner: RN12 + ST40 + SP9",
        "board_pearl": "Master point for all Six Yang Fu organs (Stomach, Gallbladder, Intestines, Bladder, San Jiao)."
    },
    {
        "code": "RN4",
        "name": "Guanyuan",
        "chinese": "关元",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Front-Mu Point of Small Intestine (小肠募穴); Meeting point of Ren Mai with Three Leg Yin (SP, LV, KD)",
        "location": "On the anterior midline of the lower abdomen, 3 cun inferior to the umbilicus.",
        "needling": "Perpendicular insertion 0.8–1.2 cun. ⚠️ CAUTION: Patient must empty urinary bladder prior to needling; deep insertion into full bladder causes peritonitis. Forbidden in pregnancy.",
        "functions": "Fortifies Original Yuan Qi; deeply nourishes Kidney Essence and warms Kidney Yang; regulates uterus and menstruation; rescues collapsed Yang.",
        "key_indications": "Extreme constitutional exhaustion, cold limbs, chronic diarrhea, nocturnal emission, impotence, infertility, dysmenorrhea, amenorrhea, urinary retention/incontinence.",
        "golden_pairings": "• Rescue Collapsed Yang & Warm Mingmen: RN4 + RN8 + DU4 (with salt moxibustion)\n• Gynecological Deficiency: RN4 + SP6 + KD3\n• Tonify Yuan Qi: RN4 + RN6 + ST36",
        "board_pearl": "Named 'Gate of Origin'. The premier reservoir for human vital prenatal Yuan Qi."
    },
    {
        "code": "RN6",
        "name": "Qihai",
        "chinese": "气海",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Sea of Qi (气海); Vital energetic tonification point",
        "location": "On the anterior midline of the lower abdomen, 1.5 cun inferior to the umbilicus.",
        "needling": "Perpendicular insertion 0.8–1.2 cun. ⚠️ CAUTION: Ensure empty bladder. Contraindicated in pregnancy.",
        "functions": "Fosters original Qi; tonifies Kidney and Spleen; harmonizes Blood; regulates lower abdominal Qi; stops chronic diarrhea.",
        "key_indications": "General debility, chronic fatigue, shortness of breath, abdominal distension, prolapse of uterus/rectum, enuresis, nocturnal emission, irregular menses, edema.",
        "golden_pairings": "• Sea of Qi + Leg Three Miles: RN6 + ST36 (supreme constitutional tonifier)\n• Warm Yang & Stop Exhaustion Diarrhea: RN6 + RN8 (moxa) + ST25\n• Rescue Sunken Qi: RN6 + DU20 + ST36",
        "board_pearl": "The supreme point for tonifying vital Qi in patients suffering from prolonged chronic wasting disease."
    },
    {
        "code": "RN17",
        "name": "Danzhong",
        "chinese": "膻中",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Front-Mu Point of Pericardium (心包募穴); Hui-Meeting Point of Qi (气会膻中); Sea of Qi",
        "location": "On the anterior midline of the sternum, level with the 4th intercostal space, midway between the nipples in men.",
        "needling": "Subcutaneous / transverse insertion 0.3–0.5 cun directed superiorly or inferiorly. ⚠️ CAUTION: Never needle perpendicularly (sternal foramen risk).",
        "functions": "Regulates and descends Lung Qi; unbinds chest and clears phlegm; unconstricts emotional Qi; promotes lactation.",
        "key_indications": "Chest fullness, angina pectoris, palpitations, shortness of breath, asthma, cough, dysphagia, insufficient lactation, breast abscess, grief and emotional sorrow.",
        "golden_pairings": "• Unbind Chest & Free Qi: RN17 + PC6 + LV3\n• Promote Lactation: RN17 + SI1 + ST18\n• Severe Bronchial Asthma: RN17 + Dingchuan + LU5",
        "board_pearl": "The emotional release center of the chest. Classic point for releasing suppressed sadness and weeping."
    },
    {
        "code": "GB34",
        "name": "Yanglingquan",
        "chinese": "阳陵泉",
        "channel": "Gallbladder (Foot Shaoyang)",
        "meridian_group": "Gallbladder",
        "category": "He-Sea Point (Earth); Hui-Meeting Point of Sinews & Tendons (筋会阳陵泉); Heavenly Star Point",
        "location": "On the lateral side of the lower leg, in the depression anterior and inferior to the head of the fibula.",
        "needling": "Perpendicular insertion 1.0–1.5 cun. Avoid direct pressure on the common peroneal nerve.",
        "functions": "Benefits tendons and sinews; spreads Liver and Gallbladder Qi; clears damp-heat in hepatobiliary system; harmonizes Shaoyang.",
        "key_indications": "Hemiplegia, sciatica, knee pain, hypochondriac pain, bitter taste, gallstones, cholecystitis, tendon cramping, muscular atrophy, habitual constipation.",
        "golden_pairings": "• Hui-Meeting of Sinews for Joint/Tendon Stiff: GB34 + BL11 + GB39\n• Hypochondriac Distension & Gallstones: GB34 + Danxue + LV14 + LV3\n• Lateral Sciatica: GB34 + GB30 + GB39",
        "board_pearl": "The single most important acupoint in the body for all tendon contractures, stiffness, and myofascial sprains."
    },
    {
        "code": "ST40",
        "name": "Fenglong",
        "chinese": "丰隆",
        "channel": "Stomach (Foot Yangming)",
        "meridian_group": "Stomach",
        "category": "Luo-Connecting Point of the Stomach Meridian (胃之络穴)",
        "location": "8 cun superior to the tip of the lateral malleolus, two finger-breadths lateral to the anterior crest of the tibia (lateral to ST38).",
        "needling": "Perpendicular insertion 1.0–1.5 cun.",
        "functions": "Transforms and dissolves tangible and intangible phlegm throughout the body; clears heat from Stomach; calms spirit; opens chest.",
        "key_indications": "Profuse sputum, chronic bronchitis, asthma, chest oppression, dizziness, vertigo, phlegm-induced mania, depression, obesity, lipomas, stroke phlegm misting heart.",
        "golden_pairings": "• Supreme Phlegm Dissolving Pair: ST40 + SP9\n• Phlegm-Heat Misting Shen: ST40 + PC5 + DU26\n• Dizziness from Phlegm Accumulation: ST40 + PC6 + DU20",
        "board_pearl": "Known universally as the 'Great Phlegm Evaporator'. The number one point on board exams for any phlegm diagnosis."
    },
    {
        "code": "LI11",
        "name": "Quchi",
        "chinese": "曲池",
        "channel": "Large Intestine (Hand Yangming)",
        "meridian_group": "Large Intestine",
        "category": "He-Sea Point (Earth); Mother / Tonification Point; Heavenly Star Point",
        "location": "With the elbow flexed at 90 degrees, in the depression at the lateral end of the transverse cubital crease, midway between LU5 and lateral epicondyle.",
        "needling": "Perpendicular insertion 1.0–1.5 cun.",
        "functions": "Clears heat and drains fire (exterior and interior); cools blood; dispels exterior wind and dampness; regulates Wei Qi; reduces blood pressure.",
        "key_indications": "High fever, sore throat, hypertension, urticaria, eczema, psoriasis, erysipelas, red painful eyes, upper limb paralysis, lateral epicondylitis (tennis elbow).",
        "golden_pairings": "• Clear High Fever & Toxic Heat: LI11 + DU14 + LI4\n• Skin Itching & Toxic Heat: LI11 + SP10 + BL40 (bleed)\n• Lateral Epicondylitis: LI11 + LI10 + Ashi points",
        "board_pearl": "The supreme point on the extremities for draining systemic high fever and skin inflammation."
    },
    {
        "code": "BL60",
        "name": "Kunlun",
        "chinese": "昆仑",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Jing-River Point (Fire); Heavenly Star Point; Aspirin of Acupuncture",
        "location": "In the depression between the prominence of the lateral malleolus and the Achilles tendon.",
        "needling": "Perpendicular insertion 0.5–1.0 cun, directed towards KD3. ⚠️ CONTRAINDICATED IN PREGNANCY (strongly downward-bearing).",
        "functions": "Clears heat and lowers excess Yang from the head; relaxes sinews and activates entire Bladder meridian; expedites labor.",
        "key_indications": "Occipital headache, neck rigidity, acute lumbar pain, sciatica, heel pain, ankle sprain, difficult/delayed labor, retained placenta, epistaxis.",
        "golden_pairings": "• Taiyang Occipital Headache & Neck Stiffness: BL60 + GB20 + BL10\n• Acute Lumbar Spine Spasm: BL60 + BL40 + Yaotongxue\n• Induce Labor (Full Term Only): BL60 + SP6 + LI4",
        "board_pearl": "Termed the 'Aspirin Point' for its rapid ability to extinguish occipital headaches and upper cervical tension."
    },
    {
        "code": "BL18",
        "name": "Ganshu",
        "chinese": "肝俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Liver (肝之背俞穴)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 9th thoracic vertebra (T9).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular insertion causes traumatic pneumothorax.",
        "functions": "Spreads Liver Qi; nourishes Liver Blood and Liver Yin; clears Liver Fire; brightens the eyes; eliminates internal wind.",
        "key_indications": "Hepatitis, jaundice, cholecystitis, hypochondriac pain, eye redness, night blindness, blurry vision, depression, anger, vertigo, epilepsy, intercostal neuralgia.",
        "golden_pairings": "• Liver Blood Deficiency Eye Disorders: BL18 + BL23 + LV8 + GB20\n• Liver Qi Stagnation & Flank Pain: BL18 + LV14 + LV3\n• Liver Fire Blazing: BL18 + LV2 + GB20",
        "board_pearl": "Primary diagnostic tender point for hepatobiliary inflammation and chronic eye pathology."
    },
    {
        "code": "BL20",
        "name": "Pishu",
        "chinese": "脾俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Spleen (脾之背俞穴)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 11th thoracic vertebra (T11).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular insertion risks pneumothorax.",
        "functions": "Tonifies Spleen Qi and Yang; resolves dampness; nourishes Blood; raises sunken Qi; holds Blood in vessels.",
        "key_indications": "Abdominal distension, anorexia, chronic fatigue, edema, loose stools, chronic diarrhea, jaundice, uterine bleeding from spleen deficiency, prolapse.",
        "golden_pairings": "• Tonify Spleen & Build Post-Natal Qi: BL20 + ST36 + RN12\n• Chronic Spleen Dampness & Edema: BL20 + SP9 + RN9\n• Spleen Failing to Control Blood: BL20 + SP1 (moxa) + SP6",
        "board_pearl": "The primary Back-Shu point for transforming chronic dampness and fatigue."
    },
    {
        "code": "BL13",
        "name": "Feishu",
        "chinese": "肺俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Lung (肺之背俞穴)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 3rd thoracic vertebra (T3).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular needle insertion causes traumatic pneumothorax.",
        "functions": "Diffuses and descends Lung Qi; tonifies Wei Qi; clears lung heat; stops coughing and wheezing; nourishes Lung Yin.",
        "key_indications": "Cough, asthma, bronchitis, pneumonia, hemoptysis, night sweats, tidal fever, spontaneous sweating, exterior wind syndromes, urticaria.",
        "golden_pairings": "• Acute Exterior Wind-Cold Attack: BL13 + LU7 + GV14\n• Chronic Lung Deficiency Asthma: BL13 + Dingchuan + RN17 + ST36\n• Lung Yin Deficiency Cough: BL13 + LU9 + KD3",
        "board_pearl": "Essential Back-Shu point for all respiratory ailments; cupping on BL13 is standard for early-stage colds."
    },
    {
        "code": "BL15",
        "name": "Xinshu",
        "chinese": "心俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Heart (心之背俞穴)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 5th thoracic vertebra (T5).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular insertion risks pneumothorax.",
        "functions": "Calms the Shen; nourishes Heart Blood and Yin; clears Heart Fire; unbinds chest tightness and moves blood stasis.",
        "key_indications": "Cardiac pain, angina, palpitations, tachycardia, arrhythmia, insomnia, poor memory, anxiety, night sweats, mania, epilepsy.",
        "golden_pairings": "• Calm Shen & Nourish Heart Blood: BL15 + HT7 + SP6\n• Front-Mu & Back-Shu Pair for Heart: BL15 + RN14 (Juque)\n• Heart Fire with Mouth Ulcers: BL15 + HT8 + KD6",
        "board_pearl": "Classical point for emotional wounds, heartbreak, and profound panic attacks."
    },
    {
        "code": "BL17",
        "name": "Geshu",
        "chinese": "膈俞",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Back-Shu Point of the Diaphragm; Hui-Meeting Point of Blood (血会膈俞)",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 7th thoracic vertebra (T7).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular insertion risks pneumothorax.",
        "functions": "Invigorates Blood and dispels Blood stasis; cools Blood heat; nourishes Blood; unbinds diaphragm and stops vomiting/hiccup.",
        "key_indications": "All blood stasis disorders, purpura, petechiae, anemia, intractable hiccups, esophageal spasm, epigastric pain, chronic skin itching, angina.",
        "golden_pairings": "• Move Blood & Dissolve Stasis: BL17 + SP10\n• Intractable Diaphragm Hiccups: BL17 + RN12 + PC6\n• Blood Deficiency Anemia: BL17 + BL20 + SP6 + ST36",
        "board_pearl": "Referred to as the 'Emperor of Blood Points'; indispensable for any condition exhibiting a purple tongue or stasis pain."
    },
    {
        "code": "BL11",
        "name": "Dazhu",
        "chinese": "大杼",
        "channel": "Bladder (Foot Taiyang)",
        "meridian_group": "Bladder",
        "category": "Hui-Meeting Point of Bones (骨会大杼); Sea of Blood Point; Meeting of Bladder and Small Intestine",
        "location": "1.5 cun lateral to the lower border of the spinous process of the 1st thoracic vertebra (T1).",
        "needling": "Oblique insertion 0.5–0.8 cun towards the spine. ⚠️ DANGER: Deep perpendicular needle risks pneumothorax.",
        "functions": "Benefits bones and joints; expels exterior wind pathogens; clears lung heat; relieves rigidity along spine and neck.",
        "key_indications": "Osteoarthritis, osteoporosis, cervical spondylosis, rigid spine, bone bi syndrome, fever, cough, exterior headache, common cold.",
        "golden_pairings": "• Hui-Meeting of Bones for Arthritic Bi: BL11 + GB34 + GB39\n• Cervical Stiffness & Neck Rigidity: BL11 + GB20 + SI3\n• Exterior Wind-Heat with High Fever: BL11 + GV14 + LI11",
        "board_pearl": "The premier point for degenerative joint disease and spinal bone spurs."
    },
    {
        "code": "DU14",
        "name": "Dazhui",
        "chinese": "大椎",
        "channel": "Governing Vessel (Du Mai)",
        "meridian_group": "Du Mai (GV)",
        "category": "Meeting point of Du Mai with all Six Yang Meridians (Sea of Yang)",
        "location": "On the posterior midline, in the depression below the spinous process of the 7th cervical vertebra (C7).",
        "needling": "Perpendicular-oblique insertion 0.5–1.0 cun slightly upwards. Pricking to bleed or cupping drains high heat.",
        "functions": "Clears heat and releases exterior fever; regulates Yang Qi; tonifies constitutional weakness; calms asthma and dispels wind.",
        "key_indications": "High fever, malaria, sunstroke, common cold, neck stiffness, bronchitis, asthma, eczema, epilepsy, leukopenia from chemotherapy.",
        "golden_pairings": "• Drain High Fever & Exterior Heat: DU14 + LI11 + LI4 + BL40 (bleed)\n• Tonify Yang & Boost Immunity: DU14 + DU4 + ST36 (with moxibustion)\n• Severe Allergic Asthma: DU14 + Dingchuan + BL13",
        "board_pearl": "The supreme crossroad of all Yang channels in the human body; number one point for eliminating high fevers."
    },
    {
        "code": "DU4",
        "name": "Mingmen",
        "chinese": "命门",
        "channel": "Governing Vessel (Du Mai)",
        "meridian_group": "Du Mai (GV)",
        "category": "Gate of Life (命门); Master Kidney Yang Tonification Point",
        "location": "On the posterior midline, in the depression below the spinous process of the 2nd lumbar vertebra (L2).",
        "needling": "Perpendicular insertion 0.5–1.0 cun. Moxibustion is strongly indicated and classical.",
        "functions": "Warms Mingmen Fire; tonifies Kidney Yang; nourishes Original Jing; strengthens lumbar spine and knees; stops dawn diarrhea.",
        "key_indications": "Lumbago from cold deficiency, cold limbs, impotence, spermatorrhea, premature ejaculation, female infertility, dawn diarrhea (Daybreak diarrhea), enuresis.",
        "golden_pairings": "• Warm Mingmen Fire: DU4 + BL23 + RN4 (with moxa)\n• Daybreak Diarrhea (Wu Geng Xie): DU4 + BL20 + ST36 + RN4\n• Impotence & Kidney Yang Collapse: DU4 + RN4 + KD3",
        "board_pearl": "The furnace of human vitality; moxa on DU4 dispels internal cold throughout the lower burner."
    },
    {
        "code": "DU24",
        "name": "Shenting",
        "chinese": "神庭",
        "channel": "Governing Vessel (Du Mai)",
        "meridian_group": "Du Mai (GV)",
        "category": "Meeting point of Du Mai with Bladder and Stomach meridians; Courtyard of the Spirit",
        "location": "0.5 cun directly above the midpoint of the anterior hairline, on the midline.",
        "needling": "Subcutaneous / transverse insertion 0.5–0.8 cun posteriorly.",
        "functions": "Calms the Shen and pacifies the spirit; eliminates wind; clears head and opens nasal passages; benefits eyes.",
        "key_indications": "Severe frontal headache, vertigo, chronic rhinitis, nasal congestion, sinusitis, mania, anxiety, panic, palpitations, insomnia, pediatric fright.",
        "golden_pairings": "• Calm Shen & Brain Hyperactivity: DU24 + Yintang + DU20\n• Chronic Sinusitis & Nasal Blockage: DU24 + Bitong + LI20 + LU7\n• Mania & Severe Anxiety: DU24 + HT7 + PC6",
        "board_pearl": "Translates as 'Spirit Courtyard'; an exceptional point for settling an overactive, racing mind."
    },
    {
        "code": "DU26",
        "name": "Shuigou",
        "chinese": "水沟 / 人中",
        "channel": "Governing Vessel (Du Mai)",
        "meridian_group": "Du Mai (GV)",
        "category": "Meeting point of Du Mai with Large Intestine and Stomach meridians; Ghost Point of Sun Si-miao",
        "location": "At the junction of the upper 1/3 and middle 1/3 of the philtrum midline.",
        "needling": "Oblique-superior insertion 0.3–0.5 cun with strong peck-and-twist stimulation. Strongly stimulating.",
        "functions": "Restores consciousness and rescues from collapse; clears heat and calms Shen; relieves acute lumbar spasm; benefits nose and face.",
        "key_indications": "Coma, syncope, shock, fainting during needling, acute mania, hysteria, heatstroke, acute lumbar sprain (needle while patient moves lumbar spine).",
        "golden_pairings": "• Emergency Resuscitation: DU26 + Twelve Jing-Well (bleed) + KD1\n• Acute Lumbar Sprain (Twist & Move): DU26 + BL40 + Yaotongxue\n• Needle Fainting (Vasovagal): DU26 + PC6 + ST36",
        "board_pearl": "The primary emergency acupoint in Chinese medicine; strong upward needle flicking wakes unconscious patients."
    },
    {
        "code": "RN8",
        "name": "Shenque",
        "chinese": "神阙",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Gate of the Spirit; Forbidden Needling Point (禁针)",
        "location": "In the center of the umbilicus.",
        "needling": "⚠️ ABSOLUTELY FORBIDDEN TO NEEDLE (禁针). Apply indirect moxibustion (salt moxa or ginger moxa).",
        "functions": "Warms Yang and rescues from collapse; strengthens Spleen and harmonizes intestines; consolidates Yuan Qi; stops profuse diarrhea.",
        "key_indications": "Yang collapse with cold sweating and icy limbs, shock, prolapse of rectum, chronic unyielding diarrhea, borborygmus, abdominal cold pain.",
        "golden_pairings": "• Salt Moxibustion for Yang Collapse: RN8 (salt moxa) + RN4 + DU4 + ST36\n• Chronic Cold Exhaustion Diarrhea: RN8 (ginger moxa) + ST25 + BL20\n• Umbilical Cold Colic: RN8 (moxa) + RN6 + ST36",
        "board_pearl": "Universally tested on licensing exams: NEVER insert a needle into RN8; always use moxa over salt."
    },
    {
        "code": "RN3",
        "name": "Zhongji",
        "chinese": "中极",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Front-Mu Point of the Bladder (膀胱之募穴); Meeting point of Ren Mai with Three Leg Yin",
        "location": "On the anterior midline of the lower abdomen, 4 cun inferior to the umbilicus (1 cun superior to pubic symphysis).",
        "needling": "Perpendicular insertion 0.5–1.0 cun. ⚠️ CAUTION: Empty bladder prior to insertion. Contraindicated in pregnancy.",
        "functions": "Clears damp-heat from Lower Jiao; regulates Bladder Qi transformation; dissolves urinary stones; regulates uterus and genital organs.",
        "key_indications": "Acute cystitis, dysuria, urinary retention, hematuria, enuresis, cloudy urine, prostatitis, pelvic inflammatory disease, dysmenorrhea, leukorrhea.",
        "golden_pairings": "• Acute Urinary Tract Infection / Dysuria: RN3 + SP9 + SP6 + BL28 (Pangguangshu)\n• Front-Mu & Back-Shu Pair for Bladder: RN3 + BL28\n• Pelvic Damp-Heat: RN3 + LV2 + SP6",
        "board_pearl": "Number one point for acute bacterial cystitis, painful urination, and lower burner damp-heat."
    },
    {
        "code": "RN14",
        "name": "Juque",
        "chinese": "巨阙",
        "channel": "Conception Vessel (Ren Mai)",
        "meridian_group": "Ren Mai (CV)",
        "category": "Front-Mu Point of the Heart (心之募穴)",
        "location": "On the anterior midline of the upper abdomen, 6 cun superior to the umbilicus (2 cun inferior to sternocostal angle).",
        "needling": "Perpendicular-oblique insertion 0.5–0.8 cun inferiorly. ⚠️ CAUTION: Deep perpendicular insertion risks puncturing left lobe of liver or heart if enlarged.",
        "functions": "Clears Heart Fire and calms Shen; harmonizes Stomach and descends rebellious Qi; unbinds chest tightness.",
        "key_indications": "Palpitations, angina pectoris, severe anxiety, panic attacks, mania, delirium, insomnia, acid reflux, nausea, vomiting, hiccups.",
        "golden_pairings": "• Front-Mu & Back-Shu Pair for Heart: RN14 + BL15\n• Severe Heart Fire / Manic Panic: RN14 + HT7 + PC6 + DU26\n• Chest Pain Radiating to Left Arm: RN14 + PC4 + RN17",
        "board_pearl": "Translates as 'Great Gateway'; crucial for acute psychosomatic distress and panic attacks."
    },
    {
        "code": "SP9",
        "name": "Yinlingquan",
        "chinese": "阴陵泉",
        "channel": "Spleen (Foot Taiyin)",
        "meridian_group": "Spleen",
        "category": "He-Sea Point (Water)",
        "location": "On the medial side of the lower leg, in the depression below the medial condyle of the tibia, at the level of the tuberosity of tibia.",
        "needling": "Perpendicular insertion 1.0–1.5 cun.",
        "functions": "Transforms and drains dampness from the entire body; opens water passages; benefits Lower Jiao; harmonizes Spleen and resolves edema.",
        "key_indications": "Edema, abdominal fullness, ascites, diarrhea, jaundice, dysuria, cloudy urine, leukorrhea, knee arthritis, eczema.",
        "golden_pairings": "• The Supreme Damp Draining Pair: SP9 + SP6\n• Damp-Heat in Bladder (Dysuria): SP9 + RN3 + BL28\n• Phlegm & Damp Elimination: SP9 + ST40",
        "board_pearl": "The water point of the Earth meridian; acts like a diuretic needle to drain accumulated damp fluids."
    },
    {
        "code": "SP10",
        "name": "Xuehai",
        "chinese": "血海",
        "channel": "Spleen (Foot Taiyin)",
        "meridian_group": "Spleen",
        "category": "Sea of Blood (血海)",
        "location": "With knee flexed, 2 cun superior to the superior-medial border of the patella, on the bulge of the vastus medialis muscle.",
        "needling": "Perpendicular or slightly oblique insertion 1.0–1.5 cun.",
        "functions": "Cools Blood heat; moves Blood stasis; nourishes Blood; harmonizes menstruation; dispels wind-rash from skin.",
        "key_indications": "Irregular menses, dysmenorrhea, amenorrhea, uterine bleeding, urticaria, acute eczema, psoriasis, purpura, inner knee pain.",
        "golden_pairings": "• Clear Blood Heat & Skin Rashes: SP10 + LI11 + BL40 (bleed)\n• Move Blood & Stop Menstrual Pain: SP10 + SP6 + LV3\n• Nourish Blood & Stop Itching: SP10 + BL17 + SP6",
        "board_pearl": "Classical dictum: 'Treat wind by first treating blood; once blood moves, wind naturally extinguishes' (治风先治血，血行风自灭)."
    },
    {
        "code": "SP4",
        "name": "Gongsun",
        "chinese": "公孙",
        "channel": "Spleen (Foot Taiyin)",
        "meridian_group": "Spleen",
        "category": "Luo-Connecting Point; Confluent Master Point of Chong Mai (coupled with PC6); Heavenly Star Point",
        "location": "In the depression distal and inferior to the base of the 1st metatarsal bone, at the border of red and white skin.",
        "needling": "Perpendicular insertion 0.5–1.0 cun.",
        "functions": "Fortifies Spleen and harmonizes Middle Jiao; regulates Chong Mai; unbinds chest and stomach; regulates intestines and menses.",
        "key_indications": "Gastric pain, epigastric fullness, vomiting, diarrhea, dysentery, abdominal pain, irregular menses, postpartum lochia retention, heart distress.",
        "golden_pairings": "• Confluent Pair for Heart, Chest & Stomach: SP4 + PC6\n• Acute Stomach Cramping: SP4 + ST36 + RN12\n• Chronic Spleen Weakness Diarrhea: SP4 + SP3 + BL20",
        "board_pearl": "Master of the Sea of Blood (Chong Mai); essential for all conditions linking digestion with gynecological bleeding."
    },
    {
        "code": "SP3",
        "name": "Taibai",
        "chinese": "太白",
        "channel": "Spleen (Foot Taiyin)",
        "meridian_group": "Spleen",
        "category": "Shu-Stream Point (Earth); Yuan-Source Point; Ben / Horary Point of Spleen (Earth on Earth)",
        "location": "Proximal and inferior to the 1st metatarsophalangeal joint, at the border of the red and white skin.",
        "needling": "Perpendicular insertion 0.5–0.8 cun.",
        "functions": "Tonifies Spleen Qi and Yang; transforms dampness; harmonizes Middle Jiao; relieves heaviness and body aches.",
        "key_indications": "Abdominal distension, borborygmus, diarrhea, constipation, vomiting, lethargy, heaviness in limbs, poor digestion, diabetes.",
        "golden_pairings": "• Spleen Yuan-Source & Stomach Luo (Host-Guest): SP3 + ST40\n• Spleen Qi Deficiency Fatigue: SP3 + ST36 + BL20\n• Heavy Damp Body Sensation: SP3 + SP9 + RN12",
        "board_pearl": "The Earth point on the Earth meridian; the purest point for tonifying foundational digestive Spleen Qi."
    },
    {
        "code": "ST25",
        "name": "Tianshu",
        "chinese": "天枢",
        "channel": "Stomach (Foot Yangming)",
        "meridian_group": "Stomach",
        "category": "Front-Mu Point of Large Intestine (大肠之募穴)",
        "location": "On the abdomen, 2 cun lateral to the center of the umbilicus.",
        "needling": "Perpendicular insertion 1.0–1.5 cun. Caution: ensure empty bladder; forbidden in pregnancy.",
        "functions": "Regulates intestines and Middle/Lower Jiao; transforms dampness and food accumulation; stops diarrhea and relieves constipation.",
        "key_indications": "Acute/chronic diarrhea, constipation, dysentery, abdominal pain, distension, appendicitis, intestinal paralysis, irregular menses.",
        "golden_pairings": "• Front-Mu & Back-Shu Pair for Large Intestine: ST25 + BL25\n• Diarrhea & Dysentery: ST25 + ST36 + ST37 (Lower He-Sea)\n• Chronic Habitual Constipation: ST25 + SJ6 + KD6",
        "board_pearl": "The pivot point of Heaven and Earth; bidirectional regulator that cures both diarrhea and constipation."
    },
    {
        "code": "ST44",
        "name": "Neiting",
        "chinese": "内庭",
        "channel": "Stomach (Foot Yangming)",
        "meridian_group": "Stomach",
        "category": "Ying-Spring Point (Water); Heavenly Star Point",
        "location": "Proximal to the web margin between the 2nd and 3rd toes, in the depression distal and lateral to the 2nd metatarsophalangeal joint.",
        "needling": "Perpendicular or oblique insertion 0.5–0.8 cun.",
        "functions": "Clears Stomach fire and drains heat from the Yangming channel; alleviates pain; harmonizes digestion.",
        "key_indications": "Toothache (especially upper teeth), trigeminal neuralgia, facial pain, sore throat, epistaxis, acid regurgitation, hunger with inability to eat, gastric burning.",
        "golden_pairings": "• Yangming Fire Toothache: ST44 + LI4 + ST6\n• Stomach Heat Burning Hunger: ST44 + RN12 + ST36\n• Facial Pain & Trigeminal Neuralgia: ST44 + ST7 + Taiyang",
        "board_pearl": "The ice cube of the Stomach meridian; drains blazing gastric fire from the mouth, teeth, and gums."
    },
    {
        "code": "ST8",
        "name": "Touwei",
        "chinese": "头维",
        "channel": "Stomach (Foot Yangming)",
        "meridian_group": "Stomach",
        "category": "Meeting point of Stomach, Gallbladder, and Yang Wei Mai",
        "location": "At the corner of the forehead, 0.5 cun directly above the hairline, 4.5 cun lateral to the anterior midline (DU24).",
        "needling": "Subcutaneous / transverse insertion 0.5–1.0 cun posteriorly. ⚠️ FORBIDDEN TO MOXA (禁灸).",
        "functions": "Clears head and brightens eyes; dispels wind; dissolves phlegm and stops splitting headaches; relieves vertigo.",
        "key_indications": "Splitting frontal/temporal headaches, migraine, eye pain with lacrimation, dizziness, vertigo, facial twitching.",
        "golden_pairings": "• Phlegm-Damp Heavy Frontal Headache: ST8 + Yintang + ST40\n• Temporal Migraine & Eye Throbbing: ST8 + Taiyang + GB20\n• Dizziness from Stomach Phlegm: ST8 + PC6 + DU20",
        "board_pearl": "Classic exam point: strictly forbidden to moxa (禁灸) due to risk of provoking blazing cranial fire."
    },
    {
        "code": "LU9",
        "name": "Taiyuan",
        "chinese": "太渊",
        "channel": "Lung (Hand Taiyin)",
        "meridian_group": "Lung",
        "category": "Shu-Stream Point (Earth); Yuan-Source Point; Mother / Tonification Point; Hui-Meeting Point of Vessels (脉会太渊)",
        "location": "At the radial end of the transverse wrist crease, in the depression on the radial side of the radial artery.",
        "needling": "Perpendicular insertion 0.3–0.5 cun. ⚠️ CAUTION: Avoid puncturing the pulsating radial artery.",
        "functions": "Tonifies Lung Qi and Lung Yin; transforms phlegm; harmonizes all blood vessels; regulates pulse; descends Lung Qi.",
        "key_indications": "Chronic cough, wheezing, asthma, hemoptysis, weak/pulseless disease (Takayasu arteritis), arteriosclerosis, wrist pain, voice loss.",
        "golden_pairings": "• Host-Guest Pair for Lung & Large Intestine: LU9 + LI6\n• Hui-Meeting of Vessels for Pulseless Disease: LU9 + BL17\n• Tonify Mother for Lung Deficiency: LU9 + ST36 + BL13",
        "board_pearl": "The gathering point of all blood vessels in the human body; crucial when feeling a faint or irregular radial pulse."
    },
    {
        "code": "LU5",
        "name": "Chize",
        "chinese": "尺泽",
        "channel": "Lung (Hand Taiyin)",
        "meridian_group": "Lung",
        "category": "He-Sea Point (Water); Child / Sedation Point of Lung",
        "location": "On the cubital crease, in the depression on the radial side of the tendon of biceps brachii.",
        "needling": "Perpendicular insertion 0.5–1.0 cun, or prick to bleed with three-edged needle for high heat.",
        "functions": "Clears Lung Heat and sedates Lung fire; expels phlegm; descends rebellious Qi; relaxes sinews and clears elbow pain.",
        "key_indications": "Cough with yellow thick sputum, asthma, acute bronchitis, hemoptysis, sore throat, fever, chest fullness, spasmodic elbow pain, infantile convulsion.",
        "golden_pairings": "• Sedate Child for Excess Lung Phlegm-Heat: LU5 + ST40 + Dingchuan\n• Coughing Blood / Hemoptysis: LU5 + LU6 (Xi-Cleft)\n• High Fever & Pneumonia: LU5 (bleed) + DU14 + LI11",
        "board_pearl": "Sedation point of the Lung; drains excess phlegm-fire and purges respiratory heat downward."
    },
    {
        "code": "LU1",
        "name": "Zhongfu",
        "chinese": "中府",
        "channel": "Lung (Hand Taiyin)",
        "meridian_group": "Lung",
        "category": "Front-Mu Point of the Lung (肺之募穴); Meeting point of Lung and Spleen meridians",
        "location": "On the lateral aspect of the chest, 6 cun lateral to the anterior midline, 1 cun inferior to LU2 (below clavicle).",
        "needling": "Oblique insertion 0.5–0.8 cun directed laterally towards the shoulder. ⚠️ DANGER: Medial perpendicular insertion causes pneumothorax.",
        "functions": "Diffuses and descends Lung Qi; clears lung heat and phlegm; stops coughing and wheezing; unbinds chest.",
        "key_indications": "Cough, asthma, chest pain, wheezing, fullness in chest, anterior shoulder and arm pain, dyspnea, bronchitis.",
        "golden_pairings": "• Front-Mu & Back-Shu Pair for Lung: LU1 + BL13\n• Severe Bronchial Spasm: LU1 + RN17 + Dingchuan\n• Anterior Shoulder Joint Pain: LU1 + Jianneiling + LI15",
        "board_pearl": "Meeting point of Spleen and Lung; explains why tonifying digestion relieves respiratory phlegm."
    },
    {
        "code": "HT3",
        "name": "Shaohai",
        "chinese": "少海",
        "channel": "Heart (Hand Shaoyin)",
        "meridian_group": "Heart",
        "category": "He-Sea Point (Water)",
        "location": "With elbow flexed, in the depression between the medial end of the transverse cubital crease and the medial epicondyle of the humerus.",
        "needling": "Perpendicular insertion 0.5–1.0 cun.",
        "functions": "Clears Heart Fire and calms Shen; relaxes tendons and transforms phlegm; benefits arm and elbow joints.",
        "key_indications": "Cardiac pain, angina, palpitations, axillary pain, scrofula, arm tremor, Parkinson tremor, medial epicondylitis (Golfer's elbow), mania.",
        "golden_pairings": "• Hand & Arm Tremor: HT3 + LI11 + GB34\n• Clear Heart Fire & Insomnia: HT3 + HT7 + KD3\n• Golfer's Elbow (Medial Epicondylitis): HT3 + Ashi + SI8",
        "board_pearl": "The He-Sea water point of the Heart; cools emotional fire and stops involuntary motor hand tremors."
    },
    {
        "code": "HT5",
        "name": "Tongli",
        "chinese": "通里",
        "channel": "Heart (Hand Shaoyin)",
        "meridian_group": "Heart",
        "category": "Luo-Connecting Point of the Heart Meridian; Heavenly Star Point",
        "location": "1 cun proximal to the transverse wrist crease (HT7), on the radial side of the flexor carpi ulnaris tendon.",
        "needling": "Perpendicular insertion 0.3–0.5 cun.",
        "functions": "Calms the Shen and regulates Heart rhythm; benefits tongue and speech; opens heart collateral; clears heat.",
        "key_indications": "Sudden loss of voice, aphasia after stroke, stuttering, sore throat, palpitations, arrhythmia, insomnia, depression, heavy uterine bleeding.",
        "golden_pairings": "• Post-Stroke Aphasia & Speech Loss: HT5 + DU15 (Yamen) + Renmai/Tongue points\n• Arrhythmia & Cardiac Palpitations: HT5 + PC6 + BL15\n• Emotional Depression & Heart Heat: HT5 + HT7 + LV3",
        "board_pearl": "Heart collateral connects directly to the tongue; the number one point for post-stroke motor aphasia."
    },
    {
        "code": "KD1",
        "name": "Yongquan",
        "chinese": "涌泉",
        "channel": "Kidney (Foot Shaoyin)",
        "meridian_group": "Kidney",
        "category": "Jing-Well Point (Wood); Child / Sedation Point of Kidney; Heavenly Star Point",
        "location": "On the sole of the foot, in the depression when the foot is in plantar flexion, approximately at the junction of anterior 1/3 and posterior 2/3.",
        "needling": "Perpendicular insertion 0.5–1.0 cun. Strong needle sensation. Moxa applied to ground floating Yang.",
        "functions": "Revives consciousness and rescues collapse; subdues Liver Wind and Liver Yang; clears heat and calms Shen; anchors empty fire downward.",
        "key_indications": "Coma, stroke, syncope, heatstroke, infantile convulsion, vertex headache, extreme hypertension, insomnia from Yin deficiency, hot soles.",
        "golden_pairings": "• Ground Extreme Hypertension & Yang Rising: KD1 + LV3 + GB20\n• Resuscitation & Coma Rescue: KD1 + DU26 + Twelve Jing-Well\n• Severe Insomnia from Kidney-Heart Disharmony: KD1 (moxa) + HT7",
        "board_pearl": "The only acupoint located on the sole of the human foot; acts as the ultimate electrical ground for excessive cerebral fire."
    },
    {
        "code": "KD6",
        "name": "Zhaohai",
        "chinese": "照海",
        "channel": "Kidney (Foot Shaoyin)",
        "meridian_group": "Kidney",
        "category": "Confluent Master Point of Yin Qiao Mai (coupled with LU7); Master of Throat & Eyes",
        "location": "In the depression 1 cun directly inferior to the prominence of the medial malleolus.",
        "needling": "Perpendicular insertion 0.3–0.5 cun.",
        "functions": "Nourishes Kidney Yin and clears empty heat; moistens throat and lungs; opens Yin Qiao Mai; calms Shen; regulates Lower Jiao.",
        "key_indications": "Chronic dry sore throat, night sweats, tidal fever, dry mouth, insomnia, somnolence, epilepsy, constipation, irregular menses, urinary frequency.",
        "golden_pairings": "• Confluent Pair for Throat & Chest: KD6 + LU7\n• Nourish Fluid & Stop Dry Constipation: KD6 + SJ6 (Zhaohai + Zhigou)\n• Yin Deficiency Insomnia: KD6 (tonify) + BL62 (sedate)",
        "board_pearl": "The premier fluid-nourishing point; pairing KD6 with SJ6 creates the famous 'Ocean Steaming' laxative effect."
    },
    {
        "code": "KD7",
        "name": "Fuliu",
        "chinese": "复溜",
        "channel": "Kidney (Foot Shaoyin)",
        "meridian_group": "Kidney",
        "category": "Jing-River Point (Metal); Mother / Tonification Point of Kidney",
        "location": "2 cun directly superior to KD3 (Taixi), on the anterior border of the Achilles tendon.",
        "needling": "Perpendicular insertion 0.5–1.0 cun.",
        "functions": "Tonifies Kidney Yang and Kidney Yin; regulates sweating (opens and closes pores); drains dampness and resolves edema; strengthens lower back.",
        "key_indications": "Spontaneous sweating, night sweats, lack of sweating in fever, edema, abdominal distension, diarrhea, lumbar pain, cold legs, atrophy of lower limbs.",
        "golden_pairings": "• Regulate Sweating Protocol: KD7 + LI4 (KD7 tonify + LI4 sedate stops sweat; KD7 sedate + LI4 tonify promotes sweat)\n• Tonify Kidney Yang & Resolve Edema: KD7 + BL23 + SP9\n• Cold Lumbar Aching: KD7 + KD3 + DU4",
        "board_pearl": "The master regulator of human perspiration and fluid balance."
    },
    {
        "code": "GB39",
        "name": "Xuanzhong",
        "chinese": "悬钟 / 绝骨",
        "channel": "Gallbladder (Foot Shaoyang)",
        "meridian_group": "Gallbladder",
        "category": "Hui-Meeting Point of Marrow (髓会绝骨); Stroke Prevention Point",
        "location": "3 cun superior to the tip of the lateral malleolus, in the depression between the posterior border of fibula and tendons of peroneus longus/brevis.",
        "needling": "Perpendicular insertion 1.0–1.5 cun.",
        "functions": "Benefits Marrow and nourishes Brain; strengthens bones and sinews; clears Gallbladder fire; dispels wind-dampness; prevents stroke.",
        "key_indications": "Cervical stiffness and spondylosis, stroke hemiplegia, flaccidity of lower limbs, bone bi, dementia, memory loss, sciatica, hypochondriac pain.",
        "golden_pairings": "• Hui-Meeting of Marrow for Stroke Rehabilitation: GB39 + GB34 + BL11\n• Severe Acute Torticollis & Neck Rigidity: GB39 + GB20 + SI3 + LU7\n• Prevent Stroke in Elderly with Hypertensive Vertigo: GB39 (moxa) + ST36",
        "board_pearl": "The gathering point of Marrow; quintessential for cervical myelopathy and cognitive preservation."
    },
    {
        "code": "TE5",
        "name": "Waiguan",
        "chinese": "外关",
        "channel": "San Jiao (Hand Shaoyang)",
        "meridian_group": "San Jiao",
        "category": "Luo-Connecting Point; Confluent Master Point of Yang Wei Mai (coupled with GB41); Heavenly Star Point",
        "location": "2 cun proximal to the dorsal wrist crease, between the radius and ulna, on the radial side of extensor digitorum communis tendon.",
        "needling": "Perpendicular insertion 0.5–1.0 cun. Can needle through to PC6 (Waiguan through Neiguan).",
        "functions": "Expels exterior Wind-Heat; releases Shaoyang syndromes; clears head and benefits ears; unblocks Yang Wei Mai; activates collateral.",
        "key_indications": "Fever and chills, common cold, temporal migraine, tinnitus, deafness, otitis media, cheek swelling, sore throat, torticollis, wrist pain, finger tremor.",
        "golden_pairings": "• Confluent Pair for Temporal Migraine & Ears: TE5 + GB41\n• Release Exterior Wind-Heat: TE5 + LI4 + LI11 + GB20\n• Tinnitus & Sudden Deafness: TE5 + TE17 + GB2",
        "board_pearl": "Master of the Yang Linking Vessel (Yang Wei Mai); supreme point for temporal headaches and ear pathologies."
    }
]

# Backwards compatibility alias
TOP_50_POINTS_SAMPLE = [
    (f"{p['code']} ({p['name']} / {p['chinese']})", f"{p['category']}. {p['functions']} Indications: {p['key_indications']} Needling: {p['needling']}")
    for p in TOP_50_ESSENTIAL_POINTS
]


# =============================================================================
# 2. EMERGENCY PROTOCOLS & COMPLICATION ALGORITHMS (15 PROTOCOLS)
# =============================================================================
EMERGENCY_PROTOCOLS = [
    {
        "emergency": "Needle Fainting / Vasovagal Syncope (晕针急救)",
        "clinical_presentation": "Sudden dizziness, vertigo, pallor, cold clammy sweating, nausea, palpitations, weak thready pulse, impending loss of consciousness during or after needling.",
        "primary_points": "DU26 (Shuigou / Renzhong) + PC6 (Neiguan) + ST36 (Zusanli)",
        "immediate_action": "1. Immediately withdraw ALL needles.\n2. Lay patient completely flat (supine) with legs elevated 30 degrees (Trendelenburg position).\n3. Offer warm sweetened water or warm electrolyte drink.\n4. Press firmly with fingernail or needle DU26 with strong upward stimulation.\n5. If severe Yang collapse with cold limbs, apply indirect moxa to RN8 (Shenque) and RN4 (Guanyuan)."
    },
    {
        "emergency": "Loss of Consciousness / Coma / Severe Shock (昏迷急救与回阳救逆)",
        "clinical_presentation": "Unresponsiveness to vocal/physical stimuli, flaccid or closed jaw, respiratory depression, thready-faint pulse, potential circulatory collapse.",
        "primary_points": "DU26 (Shuigou) + Twelve Jing-Well Points (十二井穴刺血) + KD1 (Yongquan)",
        "immediate_action": "1. Immediately assess airway, breathing, and circulation (CAB); call 911 EMS.\n2. Prick the Twelve Jing-Well points (bilateral thumbs and fingers) with three-edged needle to express 2-3 drops of dark blood.\n3. Vigorously pinch or needle DU26 with upward pecking technique.\n4. Needle KD1 with deep strong dispersal to ground shock.\n5. If Closed Coma (clenched teeth, red face): bleed Jing-Well + ST40. If Flaccid Collapse (open mouth, incontinence, cold limbs): massive moxa to RN8 and RN4."
    },
    {
        "emergency": "Angina Pectoris / Acute Coronary Syndrome (心绞痛急救)",
        "clinical_presentation": "Substernal crushing chest pressure radiating to left shoulder, inner arm, or jaw, cold sweat, cyanosis, shortness of breath, impending sense of doom.",
        "primary_points": "PC6 (Neiguan) + PC4 (Ximen, Xi-Cleft) + HT9 (Shaochong) + RN17 (Danzhong)",
        "immediate_action": "1. CALL 911 IMMEDIATELY. Place patient in comfortable semi-Fowler position (never flat).\n2. Strongly needle PC6 and PC4 (Xi-Cleft) with vigorous reducing method to unblock pericardial stasis.\n3. Prick HT9 with sterile lancet to bleed.\n4. Administer patient's prescribed sublingual Nitroglycerin or Chewable Aspirin (325mg) if permitted and conscious.\n5. Keep Automated External Defibrillator (AED) on standby."
    },
    {
        "emergency": "Acute Heatstroke / Sunstroke (中暑急救)",
        "clinical_presentation": "Body core temperature > 40°C, flushed face, hot dry skin or profuse sweating cessation, delirium, rapid bounding pulse, collapse.",
        "primary_points": "DU26 (Shuigou) + BL40 (Weizhong bleed) + Twelve Jing-Well Points + LI11 (Quchi)",
        "immediate_action": "1. Move patient immediately to cool shaded area, remove heavy clothing, apply ice packs to axillae, groin, and neck.\n2. Prick popliteal veins of BL40 with three-edged needle to express dark venous blood (releases blood-level heat).\n3. Prick the Twelve Jing-Well points on fingers to bleed.\n4. Needle LI11 and DU14 to purge systemic fire.\n5. Fan patient and call emergency services if delirium or unresponsiveness persists."
    },
    {
        "emergency": "Acute Severe Epistaxis / Profuse Nosebleed (鼻衄急救)",
        "clinical_presentation": "Continuous, profuse bleeding from one or both nostrils, blood pooling in pharynx, lightheadedness, anxiety.",
        "primary_points": "SP1 (Yinbai, direct moxa) + LI4 (Hegu) + DU23 (Shangxing) + ST44 (Neiting)",
        "immediate_action": "1. Instruct patient to lean forward slightly (never tilt head backward to prevent blood aspiration).\n2. Pinch nasal cartilages firmly for 10-15 continuous minutes; apply ice compress to bridge of nose and nape of neck.\n3. Apply direct moxa cone or moxa roll directly to SP1 (Yinbai) until skin reddens (premier point for stopping uterine and mucosal bleeding).\n4. Strongly needle LI4 with reducing technique; needle ST44 if bleeding is from blazing Stomach heat."
    },
    {
        "emergency": "Traumatic Pneumothorax Recognition & Protocol (医源性外伤性气胸急救)",
        "clinical_presentation": "Sudden sharp stabbing chest pain during or immediately following thoracic needling (e.g. BL13, LU1, GB21), acute shortness of breath, cough, tachypnea, cyanosis, tracheal deviation, absent unilateral breath sounds.",
        "primary_points": "IMMEDIATE HOSPITALIZATION (Do NOT attempt to treat tension pneumothorax with acupuncture).",
        "immediate_action": "1. STOP NEEDLING IMMEDIATELY. Leave patient in high-Fowler seated position.\n2. CALL 911 IMMEDIATELY. Inform dispatch of suspected iatrogenic pneumothorax from thoracic acupuncture.\n3. Keep patient calm, minimize physical movement, administer emergency oxygen if equipped.\n4. Monitor respiratory rate, pulse oximetry, and blood pressure continuously until EMS arrives."
    },
    {
        "emergency": "Stuck Needle Management (滞针处理法则)",
        "clinical_presentation": "Needle cannot be rotated, lifted, or thrust; patient feels extreme pulling pain when needle is manipulated.",
        "primary_points": "Ashi relaxation tapping, adjacent acupoint stimulation.",
        "immediate_action": "1. Calm the patient and instruct them to take deep, slow diaphragmatic breaths to relax muscle spasm.\n2. If caused by unidirectional rotation, gently rotate the needle in the REVERSE direction to untangle fibrous tissue.\n3. Gently tap or massage the skin adjacent to the stuck needle.\n4. Insert another needle 0.5 cun adjacent to the stuck needle to divert local Qi and relieve spasm.\n5. Leave needle in place for 10-15 minutes until muscle tone softens spontaneously."
    },
    {
        "emergency": "Bent Needle Management (弯针处理法则)",
        "clinical_presentation": "Needle shaft bends markedly due to patient postural movement, sudden muscle spasm, or accidental external collision.",
        "primary_points": "Mechanical postural realignment.",
        "immediate_action": "1. NEVER forcibly pull, rotate, or jerk a bent needle (risk of immediate needle fracture/breakage).\n2. Restore the patient's body to the exact original position they were in when the needle was inserted.\n3. Once muscle tension relaxes, slowly withdraw the needle following the curvature of the bend.\n4. Inspect needle shaft after withdrawal to confirm complete integrity."
    },
    {
        "emergency": "Broken Needle Management (折针处理法则)",
        "clinical_presentation": "Needle shaft fractures, leaving fragment inside or under subcutaneous tissue.",
        "primary_points": "Emergency surgical extraction protocol.",
        "immediate_action": "1. Instruct the patient to REMAIN COMPLETELY STILL. Any muscle twitching or movement can drive the fragment deeper.\n2. If broken end is visible above skin: clamp firmly with sterile mosquito hemostatic forceps and withdraw cleanly.\n3. If broken end is flush with skin: press down on tissue around the needle with fingers until broken end protrudes, then extract with forceps.\n4. If broken fragment is completely buried under skin: DO NOT POKE AROUND. Mark skin location, immobilize limb, and transport immediately to hospital emergency department for fluoroscopic surgical extraction."
    },
    {
        "emergency": "Post-Needling Hematoma & Severe Bruising (血肿处理法则)",
        "clinical_presentation": "Rapid subcutaneous swelling, purple skin discoloration, localized aching pain following needle withdrawal.",
        "primary_points": "Mechanical compression and thermal transition protocol.",
        "immediate_action": "1. Apply firm, direct pressure with sterile dry cotton ball for at least 3-5 continuous minutes (do not rub).\n2. Within the first 24 hours: apply COLD compress or ice pack to restrict bleeding and reduce local swelling.\n3. After 24 hours: switch to WARM compress and gentle local heat or moxa to accelerate blood stasis reabsorption.\n4. Caution patient not to perform vigorous exercise with the affected limb for 24 hours."
    },
    {
        "emergency": "Severe Moxibustion Burns & Cupping Blisters (烫伤与水泡无菌处理)",
        "clinical_presentation": "Erythema, blistering (bullae), severe superficial burning pain following moxibustion or prolonged cupping.",
        "primary_points": "Aseptic wound management.",
        "immediate_action": "1. For small blisters (< 1 cm): clean with sterile saline, apply aloe vera or burn ointment, protect with sterile gauze; do NOT break blister.\n2. For large blisters (> 1 cm): disinfect surrounding skin with Betadine, puncture base with sterile syringe needle to aspirate fluid while leaving blister roof intact, dress with sterile antibiotic ointment and dry dressing.\n3. For 2nd/3rd degree burns with open dermis: refer immediately for outpatient surgical wound care to prevent cellulitis."
    },
    {
        "emergency": "Pediatric High-Fever Convulsions (小儿高热惊厥急救)",
        "clinical_presentation": "Sudden loss of consciousness in infant/child with spike in body temperature (> 39°C), tonic-clonic jerking, eye rolling, clenched teeth.",
        "primary_points": "DU26 (Renzhong) + Twelve Jing-Well (bleed) + DU14 (Dazhui) + KD1 (Yongquan)",
        "immediate_action": "1. Turn child to side-lying recovery position to maintain open airway and prevent aspiration of saliva/vomit.\n2. DO NOT insert fingers or tongue depressors into child's mouth.\n3. Firmly pinch DU26 with thumbnail; prick Twelve Jing-Well points with sterile lancet to express drops of blood.\n4. Sponge child with lukewarm water (never alcohol or ice water).\n5. Call 911 if seizure lasts longer than 5 minutes or if child has difficulty breathing."
    },
    {
        "emergency": "Acute Severe Asthma Attack / Bronchospasm (急性哮喘发作)",
        "clinical_presentation": "Audible expiratory wheezing, severe dyspnea, inability to speak full sentences, intercostal retractions, cyanosis.",
        "primary_points": "Dingchuan (EX-B1) + LU5 (Chize) + RN17 (Danzhong) + PC6 (Neiguan)",
        "immediate_action": "1. Seat patient upright leaning forward resting on elbows; help patient administer their prescribed rescue inhaler (Albuterol / Ventolin).\n2. Needle Dingchuan (0.5 cun lateral to DU14) with oblique medial insertion 0.5–0.8 cun to stop bronchial spasm.\n3. Strongly needle LU5 (He-Sea) and PC6 (unbinds chest) with reducing technique.\n4. Needle RN17 transversely downward.\n5. If patient exhibits peak flow < 50%, silent chest, or cyanosis: call 911 immediately."
    },
    {
        "emergency": "Acute Urinary Retention (急性尿潴留急救)",
        "clinical_presentation": "Extreme lower abdominal distension and agonizing pain, inability to void despite desperate urge, palpable tense bladder.",
        "primary_points": "RN3 (Zhongji) + SP9 (Yinlingquan) + SP6 (Sanyinjiao) + BL28 (Pangguangshu)",
        "immediate_action": "1. Position patient comfortably in private warm room; run warm tap water within earshot.\n2. Needle RN3 with oblique-inferior insertion 0.5–1.0 cun (NEVER deep perpendicular to avoid puncturing the tensely distended bladder).\n3. Strongly stimulate SP9 and SP6 with reducing technique to open lower burner water gates.\n4. Needle BL28 and apply warm moxa to lower abdomen.\n5. If patient cannot void within 30-45 minutes: transfer immediately to urgent care or ER for Foley catheterization."
    },
    {
        "emergency": "Hypertensive Crisis / Severe Liver Yang Rising (高血压危象与肝阳暴亢)",
        "clinical_presentation": "Blood pressure spike (> 180/120 mmHg), splitting vertex headache, throbbing temples, flushed face, bloodshot eyes, tinnitus, nausea, visual changes.",
        "primary_points": "Taiyang (bleed) + Ear Apex (Erjian bleed) + KD1 (Yongquan) + LV3 (Taichong)",
        "immediate_action": "1. Have patient sit comfortably in quiet, dim room; measure blood pressure.\n2. Prick Ear Apex (Erjian, folded ear tip) with lancet to bleed 5-10 drops of dark blood (rapidly reduces cerebral hypertension).\n3. Prick Taiyang or bleed temporal venules with sterile needle.\n4. Deeply needle KD1 and LV3 to anchor ascending Liver Yang downward.\n5. Check for neurological deficits (FAST test); if chest pain, shortness of breath, or numbness present, call 911 immediately."
    }
]


# =============================================================================
# 3. COMPLETE FIVE SHU POINTS & MOTHER-CHILD MATRIX
# =============================================================================
FIVE_SHU_MATRIX_DATA = [
    {
        "meridian": "Lung (Hand Taiyin / 肺经)",
        "element": "Yin (Metal)",
        "jing_well": "LU11 (Wood / 木)",
        "ying_spring": "LU10 (Fire / 火)",
        "shu_stream": "LU9 (Earth / 土)",
        "jing_river": "LU8 (Metal / 金)",
        "he_sea": "LU5 (Water / 水)",
        "horary_ben": "LU8 (Metal on Metal)",
        "mother_tonify": "LU9 (Earth creates Metal)",
        "child_sedate": "LU5 (Metal creates Water)",
        "clinical_pearl": "LU9 tonifies chronic Lung Qi/Yin deficiency; LU5 purges excess Lung phlegm-heat and acute wheezing."
    },
    {
        "meridian": "Large Intestine (Hand Yangming / 大肠经)",
        "element": "Yang (Metal)",
        "jing_well": "LI1 (Metal / 金)",
        "ying_spring": "LI2 (Water / 水)",
        "shu_stream": "LI3 (Wood / 木)",
        "jing_river": "LI5 (Fire / 火)",
        "he_sea": "LI11 (Earth / 土)",
        "horary_ben": "LI1 (Metal on Metal)",
        "mother_tonify": "LI11 (Earth creates Metal)",
        "child_sedate": "LI2 (Metal creates Water)",
        "clinical_pearl": "LI11 strongly drains systemic heat and cools blood; LI2 sedates acute Yangming toothache and throat swelling."
    },
    {
        "meridian": "Stomach (Foot Yangming / 胃经)",
        "element": "Yang (Earth)",
        "jing_well": "ST45 (Metal / 金)",
        "ying_spring": "ST44 (Water / 水)",
        "shu_stream": "ST43 (Wood / 木)",
        "jing_river": "ST41 (Fire / 火)",
        "he_sea": "ST36 (Earth / 土)",
        "horary_ben": "ST36 (Earth on Earth)",
        "mother_tonify": "ST41 (Fire creates Earth)",
        "child_sedate": "ST45 (Earth creates Metal)",
        "clinical_pearl": "ST36 is supreme Post-Natal tonifier; ST45 sedates acute nightmares, insomnia, and food stagnation."
    },
    {
        "meridian": "Spleen (Foot Taiyin / 脾经)",
        "element": "Yin (Earth)",
        "jing_well": "SP1 (Wood / 木)",
        "ying_spring": "SP2 (Fire / 火)",
        "shu_stream": "SP3 (Earth / 土)",
        "jing_river": "SP5 (Metal / 金)",
        "he_sea": "SP9 (Water / 水)",
        "horary_ben": "SP3 (Earth on Earth)",
        "mother_tonify": "SP2 (Fire creates Earth)",
        "child_sedate": "SP5 (Earth creates Metal)",
        "clinical_pearl": "SP3 tonifies Spleen Qi; SP1 moxa stops hemorrhage; SP9 drains accumulated lower burner dampness."
    },
    {
        "meridian": "Heart (Hand Shaoyin / 心经)",
        "element": "Yin (Fire)",
        "jing_well": "HT9 (Wood / 木)",
        "ying_spring": "HT8 (Fire / 火)",
        "shu_stream": "HT7 (Earth / 土)",
        "jing_river": "HT4 (Metal / 金)",
        "he_sea": "HT3 (Water / 水)",
        "horary_ben": "HT8 (Fire on Fire)",
        "mother_tonify": "HT9 (Wood creates Fire)",
        "child_sedate": "HT7 (Fire creates Earth)",
        "clinical_pearl": "HT7 sedates Heart Fire and grounds wandering Shen; HT9 revives consciousness from coma."
    },
    {
        "meridian": "Small Intestine (Hand Taiyang / 小肠经)",
        "element": "Yang (Fire)",
        "jing_well": "SI1 (Metal / 金)",
        "ying_spring": "SI2 (Water / 水)",
        "shu_stream": "SI3 (Wood / 木)",
        "jing_river": "SI5 (Fire / 火)",
        "he_sea": "SI8 (Earth / 土)",
        "horary_ben": "SI5 (Fire on Fire)",
        "mother_tonify": "SI3 (Wood creates Fire)",
        "child_sedate": "SI2 (Fire creates Earth)",
        "clinical_pearl": "SI3 opens Du Mai for occipital headache and spinal spasm; SI1 promotes lactation."
    },
    {
        "meridian": "Bladder (Foot Taiyang / 膀胱经)",
        "element": "Yang (Water)",
        "jing_well": "BL67 (Metal / 金)",
        "ying_spring": "BL66 (Water / 水)",
        "shu_stream": "BL65 (Wood / 木)",
        "jing_river": "BL60 (Fire / 火)",
        "he_sea": "BL40 (Earth / 土)",
        "horary_ben": "BL66 (Water on Water)",
        "mother_tonify": "BL67 (Metal creates Water)",
        "child_sedate": "BL65 (Water creates Wood)",
        "clinical_pearl": "BL67 turns breech babies (moxa); BL40 clears blood heat and commands lumbar spine."
    },
    {
        "meridian": "Kidney (Foot Shaoyin / 肾经)",
        "element": "Yin (Water)",
        "jing_well": "KD1 (Wood / 木)",
        "ying_spring": "KD2 (Fire / 火)",
        "shu_stream": "KD3 (Earth / 土)",
        "jing_river": "KD7 (Metal / 金)",
        "he_sea": "KD10 (Water / 水)",
        "horary_ben": "KD10 (Water on Water)",
        "mother_tonify": "KD7 (Metal creates Water)",
        "child_sedate": "KD1 (Water creates Wood)",
        "clinical_pearl": "KD7 tonifies Kidney Yang and regulates sweating; KD1 sedates ascending Liver Yang and subdues fever."
    },
    {
        "meridian": "Pericardium (Hand Jueyin / 心包经)",
        "element": "Yin (Fire)",
        "jing_well": "PC9 (Wood / 木)",
        "ying_spring": "PC8 (Fire / 火)",
        "shu_stream": "PC7 (Earth / 土)",
        "jing_river": "PC5 (Metal / 金)",
        "he_sea": "PC3 (Water / 水)",
        "horary_ben": "PC8 (Fire on Fire)",
        "mother_tonify": "PC9 (Wood creates Fire)",
        "child_sedate": "PC7 (Fire creates Earth)",
        "clinical_pearl": "PC7 sedates chest fullness and clearing heat; PC8 clears mouth ulcers and palm heat."
    },
    {
        "meridian": "San Jiao (Hand Shaoyang / 三焦经)",
        "element": "Yang (Fire)",
        "jing_well": "SJ1 / TE1 (Metal / 金)",
        "ying_spring": "SJ2 / TE2 (Water / 水)",
        "shu_stream": "SJ3 / TE3 (Wood / 木)",
        "jing_river": "SJ6 / TE6 (Fire / 火)",
        "he_sea": "SJ10 / TE10 (Earth / 土)",
        "horary_ben": "SJ6 (Fire on Fire)",
        "mother_tonify": "SJ3 (Wood creates Fire)",
        "child_sedate": "SJ10 (Fire creates Earth)",
        "clinical_pearl": "SJ3 clears ear tinnitus and temporal headaches; SJ6 clears hypochondriac pain and constipation."
    },
    {
        "meridian": "Gallbladder (Foot Shaoyang / 胆经)",
        "element": "Yang (Wood)",
        "jing_well": "GB44 (Metal / 金)",
        "ying_spring": "GB43 (Water / 水)",
        "shu_stream": "GB41 (Wood / 木)",
        "jing_river": "GB38 (Fire / 火)",
        "he_sea": "GB34 (Earth / 土)",
        "horary_ben": "GB41 (Wood on Wood)",
        "mother_tonify": "GB43 (Water creates Wood)",
        "child_sedate": "GB38 (Wood creates Fire)",
        "clinical_pearl": "GB41 opens Dai Mai and clears breast pain; GB38 is empirical sedation point for one-sided migraine."
    },
    {
        "meridian": "Liver (Foot Jueyin / 肝经)",
        "element": "Yin (Wood)",
        "jing_well": "LV1 (Wood / 木)",
        "ying_spring": "LV2 (Fire / 火)",
        "shu_stream": "LV3 (Earth / 土)",
        "jing_river": "LV4 (Metal / 金)",
        "he_sea": "LV8 (Water / 水)",
        "horary_ben": "LV1 (Wood on Wood)",
        "mother_tonify": "LV8 (Water creates Wood)",
        "child_sedate": "LV2 (Wood creates Fire)",
        "clinical_pearl": "LV8 tonifies Liver Blood and Yin; LV2 strongly sedates blazing Liver fire, eye pain, and acute anger."
    }
]


# =============================================================================
# 4. YUAN-SOURCE & LUO-CONNECTING MASTER HOST-GUEST (ZHU-KE) PAIRING TABLE
# =============================================================================
YUAN_LUO_PAIRS_DATA = [
    {
        "affected_meridian": "Lung Channel Affected (Primary / Host)",
        "host_yuan": "LU9 (Taiyuan / 太渊)",
        "interior_exterior": "Large Intestine Channel (Secondary / Guest)",
        "guest_luo": "LI6 (Pianli / 偏历)",
        "clinical_indications": "Cough, asthma, shortness of breath, fullness in chest, dry throat, fever, chills, toothache, epistaxis, edema of facial limbs."
    },
    {
        "affected_meridian": "Large Intestine Affected (Primary / Host)",
        "host_yuan": "LI4 (Hegu / 合谷)",
        "interior_exterior": "Lung Channel (Secondary / Guest)",
        "guest_luo": "LU7 (Lieque / 列缺)",
        "clinical_indications": "Toothache, facial pain, sore throat, red painful eyes, epistaxis, nasal congestion, stiff neck, exterior wind-heat, abdominal colic."
    },
    {
        "affected_meridian": "Spleen Channel Affected (Primary / Host)",
        "host_yuan": "SP3 (Taibai / 太白)",
        "interior_exterior": "Stomach Channel (Secondary / Guest)",
        "guest_luo": "ST40 (Fenglong / 丰隆)",
        "clinical_indications": "Abdominal distension, poor appetite, loose stools, muscle fatigue, body heaviness, profuse phlegm, nausea, dizziness, vomiting."
    },
    {
        "affected_meridian": "Stomach Channel Affected (Primary / Host)",
        "host_yuan": "ST42 (Chongyang / 冲阳)",
        "interior_exterior": "Spleen Channel (Secondary / Guest)",
        "guest_luo": "SP4 (Gongsun / 公孙)",
        "clinical_indications": "Epigastric pain, acid reflux, hunger with inability to eat, abdominal cramping, facial paralysis, manic laughing, swelling of lower limbs."
    },
    {
        "affected_meridian": "Heart Channel Affected (Primary / Host)",
        "host_yuan": "HT7 (Shenmen / 神门)",
        "interior_exterior": "Small Intestine Channel (Secondary / Guest)",
        "guest_luo": "SI7 (Zhizheng / 支正)",
        "clinical_indications": "Palpitations, insomnia, anxiety, chest tightness, cardiac pain, aphasia, mental confusion, warts on skin, neck stiffness."
    },
    {
        "affected_meridian": "Small Intestine Affected (Primary / Host)",
        "host_yuan": "SI4 (Wangu / 腕骨)",
        "interior_exterior": "Heart Channel (Secondary / Guest)",
        "guest_luo": "HT5 (Tongli / 通里)",
        "clinical_indications": "Scapular pain, neck rigidity, hypogastric distension, dark burning urination, tongue sores, speech difficulty, heart vexation."
    },
    {
        "affected_meridian": "Kidney Channel Affected (Primary / Host)",
        "host_yuan": "KD3 (Taixi / 太溪)",
        "interior_exterior": "Bladder Channel (Secondary / Guest)",
        "guest_luo": "BL58 (Feiyang / 飞扬)",
        "clinical_indications": "Chronic low back pain, weak knees, cold lower limbs, tinnitus, dizziness, dry throat, dysuria, frequent urination, nasal congestion."
    },
    {
        "affected_meridian": "Bladder Channel Affected (Primary / Host)",
        "host_yuan": "BL64 (Jinggu / 京骨)",
        "interior_exterior": "Kidney Channel (Secondary / Guest)",
        "guest_luo": "KD4 (Dazhong / 大钟)",
        "clinical_indications": "Severe occipital headache, stiff neck, spinal pain, lumbar spasm, urinary retention, enuresis, heel pain, fear, anxiety."
    },
    {
        "affected_meridian": "Pericardium Affected (Primary / Host)",
        "host_yuan": "PC7 (Daling / 大陵)",
        "interior_exterior": "San Jiao Channel (Secondary / Guest)",
        "guest_luo": "SJ5 / TE5 (Waiguan / 外关)",
        "clinical_indications": "Chest pain, palpitations, emotional turmoil, mania, vomiting, insomnia, temporal migraine, ear pain, tinnitus, febrile disease."
    },
    {
        "affected_meridian": "San Jiao Channel Affected (Primary / Host)",
        "host_yuan": "SJ4 / TE4 (Yangchi / 阳池)",
        "interior_exterior": "Pericardium Channel (Secondary / Guest)",
        "guest_luo": "PC6 (Neiguan / 内关)",
        "clinical_indications": "Alternating chills and fever, deafness, tinnitus, ear pain, sore throat, hypochondriac pain, nausea, vomiting, chest oppression."
    },
    {
        "affected_meridian": "Liver Channel Affected (Primary / Host)",
        "host_yuan": "LV3 (Taichong / 太冲)",
        "interior_exterior": "Gallbladder Channel (Secondary / Guest)",
        "guest_luo": "GB37 (Guangming / 光明)",
        "clinical_indications": "Hypochondriac distension, dizziness, vertex headache, irritability, depression, red painful eyes, blurry vision, night blindness, menstrual cramps."
    },
    {
        "affected_meridian": "Gallbladder Affected (Primary / Host)",
        "host_yuan": "GB40 (Qiuxu / 丘墟)",
        "interior_exterior": "Liver Channel (Secondary / Guest)",
        "guest_luo": "LV5 (Ligou / 蠡沟)",
        "clinical_indications": "Bitter taste in mouth, sighing, lateral ribcage pain, gallstones, temporal headache, genital itching, priapism, testicular swelling."
    }
]


# =============================================================================
# 5. EIGHT CONFLUENT POINTS OF EXTRAORDINARY VESSELS (BA MAI JIAO HUI XUE)
# =============================================================================
EIGHT_CONFLUENT_PAIRS_DATA = [
    {
        "couple_name": "Pair 1: Chong Mai & Yin Wei Mai (冲脉 - 阴维脉配穴)",
        "master_point": "SP4 (Gongsun / 公孙) — Chong Mai (Sea of Blood)",
        "coupled_point": "PC6 (Neiguan / 内关) — Yin Wei Mai (Interior Linking)",
        "body_regions": "Heart, Chest, Epigastrium, Stomach, Gastrointestinal tract, Uterus",
        "clinical_indications": "Gastric pain, acid reflux, nausea, vomiting, morning sickness, abdominal distension, angina pectoris, palpitations, anxiety, dysmenorrhea, postpartum lochial retention, food stagnation.",
        "classical_verse": "公孙冲脉胃心胸，内关阴维下膈同。"
    },
    {
        "couple_name": "Pair 2: Ren Mai & Yin Qiao Mai (任脉 - 阴峤脉配穴)",
        "master_point": "LU7 (Lieque / 列缺) — Ren Mai (Sea of Yin)",
        "coupled_point": "KD6 (Zhaohai / 照海) — Yin Qiao Mai (Yin Heel)",
        "body_regions": "Lungs, Throat, Diaphragm, Chest, Female Genitourinary System, Kidneys",
        "clinical_indications": "Chronic dry cough, asthma, throat constriction, plum pit Qi (globus hystericus), chronic sore hoarse throat, loss of voice, night sweats, tidal fever, urinary retention, dysuria, irregular menses, constipation.",
        "classical_verse": "列缺任脉行肺系，阴峤照海在咽喉。"
    },
    {
        "couple_name": "Pair 3: Du Mai & Yang Qiao Mai (督脉 - 阳峤脉配穴)",
        "master_point": "SI3 (Houxi / 后溪) — Du Mai (Sea of Yang)",
        "coupled_point": "BL62 (Shenmai / 申脉) — Yang Qiao Mai (Yang Heel)",
        "body_regions": "Neck, Shoulder, Spine, Lumbar region, Inner Canthus of Eye, Brain",
        "clinical_indications": "Occipital headache, cervical spondylosis, stiff neck, acute lumbar sprain, ankylosing spondylitis, spinal pain, daytime mania, epilepsy, insomnia with agitation, tremors, inner eye corner pain.",
        "classical_verse": "后溪督脉寻颈项，阳峤申脉内眦连。"
    },
    {
        "couple_name": "Pair 4: Dai Mai & Yang Wei Mai (带脉 - 阳维脉配穴)",
        "master_point": "GB41 (Zulinqi / 足临泣) — Dai Mai (Girdle Vessel)",
        "coupled_point": "SJ5 / TE5 (Waiguan / 外关) — Yang Wei Mai (Exterior Linking)",
        "body_regions": "Outer Canthus of Eye, Retroauricular, Cheek, Shoulder, Lateral Torso, Hip",
        "clinical_indications": "Temporal migraine, tinnitus, deafness, otitis media, cheek swelling, scrofula, intercostal neuralgia, hypochondriac distension, leukorrhea, pelvic girdle pain, hip joint arthritis, sciatica along Shaoyang.",
        "classical_verse": "临泣带脉目锐眦，外关阳维手背连。"
    }
]


# =============================================================================
# 6. SIXTEEN XI-CLEFT POINTS & ACUTE PAIN / BLEEDING MATRIX
# =============================================================================
XI_CLEFT_POINTS_DATA = [
    {"channel": "Lung (LU)", "point": "LU6 (Kongzui / 孔最)", "depth": "0.5–1.0 cun perp.", "primary_action": "Acute hemoptysis, severe coughing of blood, spasmodic asthma, acute sore throat."},
    {"channel": "Large Intestine (LI)", "point": "LI7 (Wenliu / 温溜)", "depth": "0.5–1.0 cun perp.", "primary_action": "Acute borborygmus, acute abdominal pain, carbuncles, severe sore throat."},
    {"channel": "Stomach (ST)", "point": "ST34 (Liangqiu / 梁丘)", "depth": "0.5–1.0 cun perp.", "primary_action": "Acute epigastric cramping, severe acid pain, acute mastitis with breast swelling."},
    {"channel": "Spleen (SP)", "point": "SP8 (Diji / 地机)", "depth": "1.0–1.5 cun perp.", "primary_action": "Severe acute dysmenorrhea, pelvic cramping, uterine bleeding, acute diarrhea."},
    {"channel": "Heart (HT)", "point": "HT6 (Yinxi / 阴郄)", "depth": "0.3–0.5 cun perp.", "primary_action": "Severe angina pectoris, acute palpitations, hematemesis, profuse night sweats."},
    {"channel": "Small Intestine (SI)", "point": "SI6 (Yanglao / 养老)", "depth": "0.5–0.8 cun oblique", "primary_action": "Acute severe lumbar sprain, stiff neck, scapular pain, blurry vision in elderly."},
    {"channel": "Bladder (BL)", "point": "BL63 (Jinmen / 金门)", "depth": "0.5–0.8 cun perp.", "primary_action": "Acute severe lower back pain, sciatica, ankle inversion sprain, epilepsy convulsions."},
    {"channel": "Kidney (KD)", "point": "KD5 (Shuiquan / 水泉)", "depth": "0.3–0.5 cun perp.", "primary_action": "Acute dysmenorrhea, amenorrhea, hematuria, painful dysuria, uterine prolapse."},
    {"channel": "Pericardium (PC)", "point": "PC4 (Ximen / 郄门)", "depth": "0.5–1.0 cun perp.", "primary_action": "Acute myocardial ischemia, crushing chest pain, angina, acute panic attacks."},
    {"channel": "San Jiao (TE/SJ)", "point": "TE7 / SJ7 (Huizong / 会宗)", "depth": "0.5–1.0 cun perp.", "primary_action": "Severe temporal ear pain, sudden deafness, arm tremors, epilepsy seizures."},
    {"channel": "Gallbladder (GB)", "point": "GB36 (Waiqiu / 外丘)", "depth": "0.5–1.0 cun perp.", "primary_action": "Acute hypochondriac pain, intercostal spasm, rabies bite pain, neck scrofula."},
    {"channel": "Liver (LV)", "point": "LV6 (Zhongdu / 中都)", "depth": "0.5–0.8 cun sub-q", "primary_action": "Acute persistent uterine bleeding (metrorrhagia), acute hepatitis pain, hernia."},
    {"channel": "Yin Wei Mai", "point": "KD9 (Zhubin / 筑宾)", "depth": "1.0–1.2 cun perp.", "primary_action": "Acute psychiatric mania, severe anxiety, delirium, clearing fetal toxins."},
    {"channel": "Yang Wei Mai", "point": "GB35 (Yangjiao / 阳交)", "depth": "1.0–1.5 cun perp.", "primary_action": "Acute lateral thoracic pain, sciatica, swelling of knee and foot."},
    {"channel": "Yin Qiao Mai", "point": "KD8 (Jiaoxin / 交信)", "depth": "0.5–1.0 cun perp.", "primary_action": "Severe persistent uterine bleeding, irregular menses, severe testicular pain."},
    {"channel": "Yang Qiao Mai", "point": "BL59 (Fuyang / 跗阳)", "depth": "0.8–1.2 cun perp.", "primary_action": "Acute severe sciatica, lumbar pain with inability to stand, lower limb paralysis."}
]


# =============================================================================
# 7. FRONT-MU & BACK-SHU MASTER COMBINATION MATRIX (YU-MU PEI XUE)
# =============================================================================
FRONT_MU_BACK_SHU_DATA = [
    {"organ": "Lung (Fei / 肺)", "back_shu": "BL13 (Feishu / 肺俞)", "level": "T3 (spinous process)", "front_mu": "LU1 (Zhongfu / 中府)", "mu_loc": "6 cun lateral to midline, 1st ICS", "rule": "Lung Yin def tonify BL13; Phlegm-heat drain LU1"},
    {"organ": "Pericardium (Xinbao / 心包)", "back_shu": "BL14 (Jueyinshu / 厥阴俞)", "level": "T4 (spinous process)", "front_mu": "RN17 (Danzhong / 膻中)", "mu_loc": "Midline of sternum, 4th ICS", "rule": "Chest oppression drain RN17; Palpitations tonify BL14"},
    {"organ": "Heart (Xin / 心)", "back_shu": "BL15 (Xinshu / 心俞)", "level": "T5 (spinous process)", "front_mu": "RN14 (Juque / 巨阙)", "mu_loc": "Midline of abdomen, 6 cun above navel", "rule": "Heart blood def tonify BL15; Heart fire drain RN14"},
    {"organ": "Liver (Gan / 肝)", "back_shu": "BL18 (Ganshu / 肝俞)", "level": "T9 (spinous process)", "front_mu": "LV14 (Qimen / 期门)", "mu_loc": "Mamillary line, 6th ICS", "rule": "Liver blood def tonify BL18; Qi stagnation drain LV14"},
    {"organ": "Gallbladder (Dan / 胆)", "back_shu": "BL19 (Danshu / 胆俞)", "level": "T10 (spinous process)", "front_mu": "GB24 (Riyue / 日月)", "mu_loc": "Mamillary line, 7th ICS", "rule": "Gallstones & damp-heat drain GB24; Timidity tonify BL19"},
    {"organ": "Spleen (Pi / 脾)", "back_shu": "BL20 (Pishu / 脾俞)", "level": "T11 (spinous process)", "front_mu": "LV13 (Zhangmen / 章门)", "mu_loc": "Tip of 11th free floating rib", "rule": "Spleen Qi def tonify BL20; Cold food stagnation drain LV13"},
    {"organ": "Stomach (Wei / 胃)", "back_shu": "BL21 (Weishu / 胃俞)", "level": "T12 (spinous process)", "front_mu": "RN12 (Zhongwan / 中脘)", "mu_loc": "Midline of abdomen, 4 cun above navel", "rule": "Stomach fire drain RN12; Stomach deficiency tonify BL21"},
    {"organ": "San Jiao (Sanjiao / 三焦)", "back_shu": "BL22 (Sanjiaoshu / 三焦俞)", "level": "L1 (spinous process)", "front_mu": "RN5 (Shimen / 石门)", "mu_loc": "Midline of abdomen, 2 cun below navel", "rule": "Fluid stagnation drain RN5; Water metabolism tonify BL22"},
    {"organ": "Kidney (Shen / 肾)", "back_shu": "BL23 (Shenshu / 肾俞)", "level": "L2 (spinous process)", "front_mu": "GB25 (Jingmen / 京门)", "mu_loc": "Lower border of free 12th rib", "rule": "Kidney deficiency tonify BL23; Renal colic palpate GB25"},
    {"organ": "Large Intestine (Dachang / 大肠)", "back_shu": "BL25 (Dachangshu / 大肠俞)", "level": "L4 (spinous process)", "front_mu": "ST25 (Tianshu / 天枢)", "mu_loc": "2 cun lateral to center of navel", "rule": "Acute diarrhea/constipation drain ST25; Chronic tonify BL25"},
    {"organ": "Small Intestine (Xiaochang / 小肠)", "back_shu": "BL27 (Xiaochangshu / 小肠俞)", "level": "S1 (1st sacral foramen)", "front_mu": "RN4 (Guanyuan / 关元)", "mu_loc": "Midline of abdomen, 3 cun below navel", "rule": "Deficiency cold warm RN4; Heat in intestines tonify BL27"},
    {"organ": "Urinary Bladder (Pangguang / 膀胱)", "back_shu": "BL28 (Pangguangshu / 膀胱俞)", "level": "S2 (2nd sacral foramen)", "front_mu": "RN3 (Zhongji / 中极)", "mu_loc": "Midline of abdomen, 4 cun below navel", "rule": "Acute cystitis drain RN3; Frequent urination tonify BL28"}
]


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_study_guides_tab():
    """Render the Printable Study Guides & Pocket Cheat Sheets tab."""
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #10b981; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            📚 Printable Study Guides & Pocket Cheat Sheets (临床速查宝典)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            15 exhaustive, board-ready reference matrices covering all 50 Essential Points, Emergency Shock Protocols, Five Shu Points, Yuan-Luo Host-Guest pairs, Confluent & Xi-Cleft tables, Tongue & Pulse diagnostics, Medical Red Flags, and Herb-Drug interactions.
        </p>
    </div>
    """)

    sheet_choice = st.selectbox(
        "Select Quick-Reference Study Guide",
        options=[
            "⭐ Top 50 Essential Clinical Acupoints (Top 50 临床核心要穴完整口袋卡)",
            "🚨 Emergency Acupoints & Shock Protocols (急症急救与针灸意外处理全纲)",
            "🌊 Five Shu Points & Mother-Child Tonification/Sedation Table (十二经五输穴与五行配属全表)",
            "🔗 Yuan-Source & Luo-Connecting Master Pairing Table (主客原络配穴全表)",
            "⚡ Eight Confluent Points of Extraordinary Vessels (八脉交会穴与八法配穴矩阵)",
            "🚨 Sixteen Xi-Cleft Points & Acute Pain/Bleeding Matrix (十六郄穴急症速查表)",
            "🏛️ Front-Mu & Back-Shu Master Combination Matrix (俞募穴脏腑辨证总纲)",
            "⭐ Eight Influential (Hui-Meeting) & Six Command Points (八会穴与六总穴速查表)",
            "📍 Extra Points (经外奇穴) Master Board Matrix (高频经外奇穴考点矩阵)",
            "👅 Tongue Diagnosis Master Matrix (舌诊全景辨证精要卡)",
            "⚖️ 28 Pulses Diagnostic Differential Matrix (二十八脉分类归纳总纲)",
            "🩺 Medical Red Flags & Urgent Hospital Referral Guide (西医急症危险征象与紧急转诊全景指南)",
            "💊 Pharmacology & Herb-Drug Interactions Master Matrix (常用西药药理机制与中草药配伍禁忌矩阵)",
            "⚡ Acupuncture Modalities: Electroacupuncture, Scalp, Ear & Moxa (针灸辅助疗法精要卡：电针、头针、耳穴与灸法)",
            "🎯 Root vs Manifestation (Ben & Biao) Treatment Principles Matrix (标本缓急与治则配属全解矩阵)"
        ]
    )

    st.write("")

    # =========================================================================
    # GUIDE 1: TOP 50 ESSENTIAL POINTS (RICH INTERACTIVE CARD MATRIX)
    # =========================================================================
    if sheet_choice.startswith("⭐ Top 50 Essential"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #fde68a;">⭐ 临床核心50要穴完整口袋卡 (Complete 50 Essential Points Pocket Guide)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                These 50 points account for >85% of all daily clinical acupuncture prescriptions and over 70% of NCCAOM and CARB-TCMPA board exam point-location questions.
            </div>
        </div>
        """)

        col_search, col_filter = st.columns([2, 1])
        with col_search:
            search_query = st.text_input("🔍 Search Points (Code, Name, Indication, or Action):", value="").strip().lower()
        with col_filter:
            channel_filter = st.selectbox(
                "Filter by Meridian:",
                options=[
                    "All Meridians",
                    "Lung", "Large Intestine", "Stomach", "Spleen",
                    "Heart", "Small Intestine", "Bladder", "Kidney",
                    "Pericardium", "San Jiao", "Gallbladder", "Liver",
                    "Du Mai (GV)", "Ren Mai (CV)"
                ]
            )

        # Filter points
        filtered_points = []
        for p in TOP_50_ESSENTIAL_POINTS:
            match_channel = (channel_filter == "All Meridians") or (p["meridian_group"].lower() in channel_filter.lower())
            if not match_channel:
                continue
            
            if search_query:
                combined_text = f"{p['code']} {p['name']} {p['chinese']} {p['channel']} {p['category']} {p['functions']} {p['key_indications']} {p['golden_pairings']}".lower()
                if search_query not in combined_text:
                    continue
            
            filtered_points.append(p)

        st.caption(f"Showing **{len(filtered_points)}** of 50 Essential Acupoints")

        cols_50 = st.columns(2)
        for i, pt in enumerate(filtered_points):
            col = cols_50[i % 2]
            pairings_html = pt['golden_pairings'].replace(chr(92) + 'n', '<br/>').replace(chr(10), '<br/>')
            with col:
                render_clean_html(f"""
                <div style="background: #111827; border: 1.5px solid rgba(255,255,255,0.12); border-radius: 10px; padding: 16px; margin-bottom: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                        <div>
                            <span style="font-size: 1.2rem; font-weight: 800; color: #38bdf8;">{pt['code']}</span>
                            <span style="font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-left: 6px;">{pt['name']}</span>
                            <span style="font-size: 0.95rem; color: #94a3b8; margin-left: 4px;">({pt['chinese']})</span>
                        </div>
                        <span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px;">
                            {pt['meridian_group']}
                        </span>
                    </div>

                    <div style="font-size: 0.78rem; font-weight: 700; color: #fbbf24; margin-bottom: 6px;">
                        🏷️ {pt['category']}
                    </div>

                    <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 6px;">
                        <strong>📍 Location:</strong> {pt['location']}
                    </div>

                    <div style="background: rgba(239, 68, 68, 0.1); border-left: 3px solid #ef4444; padding: 6px 10px; border-radius: 4px; font-size: 0.78rem; color: #fca5a5; line-height: 1.4; margin-bottom: 8px;">
                        <strong>⚠️ Needling:</strong> {pt['needling']}
                    </div>

                    <div style="font-size: 0.82rem; color: #e2e8f0; line-height: 1.45; margin-bottom: 6px;">
                        <strong>⚡ Functions:</strong> {pt['functions']}
                    </div>

                    <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 8px;">
                        <strong>🎯 Indications:</strong> {pt['key_indications']}
                    </div>

                    <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 6px 10px; border-radius: 4px; font-size: 0.78rem; color: #a7f3d0; line-height: 1.4; margin-bottom: 6px;">
                        <strong>✨ Golden Pairings:</strong><br/>
                        {pairings_html}
                    </div>

                    <div style="font-size: 0.76rem; color: #94a3b8; font-style: italic;">
                        💡 <strong>Board Pearl:</strong> {pt['board_pearl']}
                    </div>
                </div>
                """)

    # =========================================================================
    # GUIDE 2: EMERGENCY PROTOCOLS & SHOCK ALGORITHMS
    # =========================================================================
    elif sheet_choice.startswith("🚨 Emergency Acupoints"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #ef4444;">🚨 针灸临床急症急救与意外处理全景指南 (Emergency & Complication Protocols)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Comprehensive Clean Needle Technique (CNT) and clinical emergency algorithms for syncope, pneumothorax, stuck/broken needles, anaphylaxis, and acute cardiovascular collapse.
            </div>
        </div>
        """)

        for em in EMERGENCY_PROTOCOLS:
            action_html = em['immediate_action'].replace(chr(92) + 'n', '<br/>').replace(chr(10), '<br/>')
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(239, 68, 68, 0.35); border-radius: 12px; padding: 18px 22px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="color: #ffffff; font-size: 1.18rem; font-weight: 800;">{em['emergency']}</span>
                    <span style="background: rgba(239, 68, 68, 0.25); color: #f87171; font-size: 0.75rem; font-weight: 800; padding: 3px 10px; border-radius: 4px;">
                        CRITICAL PROTOCOL
                    </span>
                </div>
                <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.5; margin-bottom: 8px;">
                    <strong>Clinical Presentation:</strong> {em['clinical_presentation']}
                </div>
                <div style="background: rgba(0, 123, 167, 0.2); border-left: 3px solid #38bdf8; border-radius: 6px; padding: 10px 14px; margin-bottom: 10px;">
                    <span style="font-size: 0.78rem; font-weight: 800; color: #38bdf8; text-transform: uppercase;">Primary Emergency Points:</span>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin-top: 2px;">{em['primary_points']}</div>
                </div>
                <div style="font-size: 0.86rem; color: #34d399; font-weight: 600; line-height: 1.5;">
                    <strong>✓ Step-by-Step Action:</strong><br/>
                    {action_html}
                </div>
            </div>
            """)

    # =========================================================================
    # GUIDE 3: FIVE SHU MATRIX
    # =========================================================================
    elif sheet_choice.startswith("🌊 Five Shu Points"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #38bdf8;">🌊 十二经五输穴与五行生克配属全表 (Complete Five Shu Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                <strong>Yin Meridians:</strong> Well (Wood) → Spring (Fire) → Stream (Earth) → River (Metal) → Sea (Water).<br/>
                <strong>Yang Meridians:</strong> Well (Metal) → Spring (Water) → Stream (Wood) → River (Fire) → Sea (Earth).<br/>
                <strong>Nan Jing Ch. 69 Rule:</strong> "In deficiency, tonify the Mother (虚则补其母); In excess, sedate the Child (实则泻其子)."
            </div>
        </div>
        """)

        table_md = """
| Meridian | 井 (Well) | 荥 (Spring) | 输 (Stream) | 经 (River) | 合 (Sea) | 本穴 (Horary) | 补母 (Tonify) | 泻子 (Sedate) |
|---|---|---|---|---|---|---|---|---|
| **Lung (LU)** | LU11 (木) | LU10 (火) | **LU9 (土)** | LU8 (金) | **LU5 (水)** | **LU8 (金)** | **LU9** (Earth) | **LU5** (Water) |
| **L. Intestine (LI)** | LI1 (金) | **LI2 (水)** | LI3 (木) | LI5 (火) | **LI11 (土)** | **LI1 (金)** | **LI11** (Earth) | **LI2** (Water) |
| **Stomach (ST)** | **ST45 (金)** | ST44 (水) | ST43 (木) | **ST41 (火)** | ST36 (土) | **ST36 (土)** | **ST41** (Fire) | **ST45** (Metal) |
| **Spleen (SP)** | SP1 (木) | **SP2 (火)** | SP3 (土) | **SP5 (金)** | SP9 (水) | **SP3 (土)** | **SP2** (Fire) | **SP5** (Metal) |
| **Heart (HT)** | **HT9 (木)** | HT8 (火) | **HT7 (土)** | HT4 (金) | HT3 (水) | **HT8 (火)** | **HT9** (Wood) | **HT7** (Earth) |
| **S. Intestine (SI)** | SI1 (金) | **SI2 (水)** | **SI3 (木)** | SI5 (火) | SI8 (土) | **SI5 (火)** | **SI3** (Wood) | **SI2** (Water) |
| **Bladder (BL)** | **BL67 (金)** | BL66 (水) | **BL65 (木)** | BL60 (火) | BL40 (土) | **BL66 (水)** | **BL67** (Metal) | **BL65** (Wood) |
| **Kidney (KD)** | **KD1 (木)** | KD2 (火) | KD3 (土) | **KD7 (金)** | KD10 (水) | **KD10 (水)**| **KD7** (Metal) | **KD1** (Wood) |
| **Pericardium (PC)** | **PC9 (木)** | PC8 (火) | **PC7 (土)** | PC5 (金) | PC3 (水) | **PC8 (火)** | **PC9** (Wood) | **PC7** (Earth) |
| **San Jiao (SJ)** | SJ1 (金) | **SJ2 (水)** | **SJ3 (木)** | SJ6 (火) | SJ10 (土) | **SJ6 (火)** | **SJ3** (Wood) | **SJ10** (Earth)|
| **Gallbladder (GB)**| GB44 (金) | **GB43 (水)**| GB41 (木) | **GB38 (火)**| GB34 (土) | **GB41 (木)** | **GB43** (Water) | **GB38** (Fire) |
| **Liver (LIV)** | LIV1 (木) | **LIV2 (火)**| LIV3 (土) | LIV4 (金) | **LIV8 (水)** | **LIV1 (木)** | **LIV8** (Water) | **LIV2** (Fire) |
"""
        st.markdown(table_md)

        st.markdown("""
---
### 📖 Classical Dynamic Indications (*Nan Jing* Chapter 68)
- **Jing-Well Points (井主心下满)**: Treats fullness below the Heart (epigastric distress, mental anguish, loss of consciousness, acute stroke).
- **Ying-Spring Points (荥主身热)**: Treats heat in the body (febrile syndromes, thirst, local and channel inflammation).
- **Shu-Stream Points (输主体重节痛)**: Treats body heaviness and painful aching joints (Bi syndromes, chronic arthralgia).
- **Jing-River Points (经主喘咳寒热)**: Treats coughing, dyspnea, chills and fever, asthma, changes in voice.
- **He-Sea Points (合主逆气而泄)**: Treats rebellious Qi and diarrhea (stomach vomiting, enteritis, visceral disorders of the Yang Fu organs).
""")

    # =========================================================================
    # GUIDE 4: YUAN-SOURCE & LUO-CONNECTING MASTER HOST-GUEST PAIRS
    # =========================================================================
    elif sheet_choice.startswith("🔗 Yuan-Source & Luo-Connecting"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #a78bfa;">🔗 主客原络配穴全纲 (Host-Guest Yuan-Luo Combination Master Guide)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Classical pairing of the <strong>Host (Primary affected channel Yuan-Source point)</strong> with the <strong>Guest (Paired interior-exterior channel Luo-Connecting point)</strong> to treat dual channel disorders.
            </div>
        </div>
        """)

        for pair in YUAN_LUO_PAIRS_DATA:
            render_clean_html(f"""
            <div style="background: #111827; border: 1px solid rgba(167, 139, 250, 0.3); border-radius: 10px; padding: 14px 18px; margin-bottom: 12px;">
                <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff; margin-bottom: 6px;">
                    {pair['affected_meridian']}
                </div>
                <div style="display: flex; gap: 12px; margin-bottom: 8px;">
                    <div style="background: rgba(167, 139, 250, 0.15); border-radius: 6px; padding: 6px 12px; flex: 1;">
                        <span style="font-size: 0.75rem; font-weight: 700; color: #c4b5fd; text-transform: uppercase;">Host (Primary Yuan):</span>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff;">{pair['host_yuan']}</div>
                    </div>
                    <div style="background: rgba(56, 189, 248, 0.15); border-radius: 6px; padding: 6px 12px; flex: 1;">
                        <span style="font-size: 0.75rem; font-weight: 700; color: #7dd3fc; text-transform: uppercase;">Guest (Paired Luo):</span>
                        <div style="font-size: 1rem; font-weight: 800; color: #ffffff;">{pair['guest_luo']}</div>
                    </div>
                </div>
                <div style="font-size: 0.84rem; color: #cbd5e1; line-height: 1.45;">
                    <strong>Clinical Indications:</strong> {pair['clinical_indications']}
                </div>
            </div>
            """)

        st.markdown("""
---
### 🌟 The Great Luo Points (大络)
- **Great Luo of Spleen — SP21 (Dabao / 大包)**: Located 6 cun inferior to the axilla on the mid-axillary line in the 7th intercostal space.
  - *Action*: Regulates all collateral blood throughout the body. Treats systemic muscle aching and flaccidity of all joints.
- **Great Luo of Stomach — Xuli (虚里)**: Located below the left breast where the apical impulse of the heart is palpated.
  - *Action*: Reflects the state of Zong Qi (Pectoral Qi). An irregular or bounding beat indicates exhaustion of Yuan Qi.
""")

    # =========================================================================
    # GUIDE 5: EIGHT CONFLUENT POINTS OF EXTRAORDINARY VESSELS
    # =========================================================================
    elif sheet_choice.startswith("⚡ Eight Confluent Points"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #fbbf24;">⚡ 奇经八脉八穴与八法配穴矩阵 (Eight Confluent Points of Extraordinary Vessels)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Classical cross-coupling of the 8 Master Confluent points to control specific anatomical zones, internal organ systems, and emotional pathologies.
            </div>
        </div>
        """)

        for c_pair in EIGHT_CONFLUENT_PAIRS_DATA:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(251, 191, 36, 0.35); border-radius: 12px; padding: 18px 22px; margin-bottom: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
                <div style="font-size: 1.15rem; font-weight: 800; color: #fbbf24; margin-bottom: 6px;">
                    {c_pair['couple_name']}
                </div>
                <div style="display: flex; gap: 10px; margin-bottom: 10px;">
                    <div style="background: rgba(251, 191, 36, 0.15); border-radius: 6px; padding: 8px 12px; flex: 1;">
                        <span style="font-size: 0.74rem; font-weight: 700; color: #fde68a;">MASTER POINT:</span>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff;">{c_pair['master_point']}</div>
                    </div>
                    <div style="background: rgba(56, 189, 248, 0.15); border-radius: 6px; padding: 8px 12px; flex: 1;">
                        <span style="font-size: 0.74rem; font-weight: 700; color: #bae6fd;">COUPLED POINT:</span>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff;">{c_pair['coupled_point']}</div>
                    </div>
                </div>
                <div style="font-size: 0.85rem; color: #38bdf8; font-weight: 700; margin-bottom: 4px;">
                    📍 Regional Territory: {c_pair['body_regions']}
                </div>
                <div style="font-size: 0.84rem; color: #cbd5e1; line-height: 1.45; margin-bottom: 6px;">
                    <strong>Core Clinical Indications:</strong> {c_pair['clinical_indications']}
                </div>
                <div style="font-size: 0.78rem; color: #94a3b8; font-style: italic;">
                    📜 Classical Verse: {c_pair['classical_verse']}
                </div>
            </div>
            """)

    # =========================================================================
    # GUIDE 6: SIXTEEN XI-CLEFT POINTS & ACUTE MATRIX
    # =========================================================================
    elif sheet_choice.startswith("🚨 Sixteen Xi-Cleft"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #f87171;">🚨 十六郄穴急症速查表 (The 16 Xi-Cleft Points Master Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Where Qi and Blood deeply accumulate. <strong>Yin Xi-Cleft points</strong> treat severe acute bleeding and blood disorders; <strong>Yang Xi-Cleft points</strong> treat severe acute pain.
            </div>
        </div>
        """)

        xi_md = """
| Channel / Vessel | Xi-Cleft Point (郄穴) | Safe Needling Depth | Primary Acute Clinical Action |
|---|---|---|---|
| **Lung (LU)** | **LU6 (Kongzui / 孔最)** | 0.5–1.0 cun perp. | Acute hemoptysis (coughing blood), spasmodic asthma, acute severe sore throat |
| **Large Intestine (LI)** | **LI7 (Wenliu / 温溜)** | 0.5–1.0 cun perp. | Acute borborygmus, acute abdominal pain, carbuncles, severe throat pain |
| **Stomach (ST)** | **ST34 (Liangqiu / 梁丘)** | 0.5–1.0 cun perp. | Acute gastric cramping, burning epigastric pain, acute mastitis |
| **Spleen (SP)** | **SP8 (Diji / 地机)** | 1.0–1.5 cun perp. | Severe acute dysmenorrhea, uterine cramping, acute diarrhea |
| **Heart (HT)** | **HT6 (Yinxi / 阴郄)** | 0.3–0.5 cun perp. | Acute angina pectoris, palpitations, hematemesis, profuse night sweats |
| **Small Intestine (SI)**| **SI6 (Yanglao / 养老)** | 0.5–0.8 cun oblique | Severe acute lumbar sprain, stiff neck, scapular pain, blurry vision |
| **Bladder (BL)** | **BL63 (Jinmen / 金门)** | 0.5–0.8 cun perp. | Acute severe lumbar spasm, sciatica, ankle inversion sprain, epilepsy |
| **Kidney (KD)** | **KD5 (Shuiquan / 水泉)** | 0.3–0.5 cun perp. | Acute dysmenorrhea, amenorrhea, hematuria, dysuria, uterine prolapse |
| **Pericardium (PC)** | **PC4 (Ximen / 郄门)** | 0.5–1.0 cun perp. | Acute myocardial ischemia, crushing chest pain, angina, panic attack |
| **San Jiao (TE/SJ)** | **TE7 / SJ7 (Huizong / 会宗)**| 0.5–1.0 cun perp. | Acute temporal ear pain, sudden deafness, arm tremors, epilepsy |
| **Gallbladder (GB)** | **GB36 (Waiqiu / 外丘)** | 0.5–1.0 cun perp. | Acute hypochondriac pain, intercostal neuralgia, rabies bite pain |
| **Liver (LV)** | **LV6 (Zhongdu / 中都)** | 0.5–0.8 cun sub-q | Acute persistent uterine bleeding (metrorrhagia), hepatitis pain, hernia |
| **Yin Wei Mai** | **KD9 (Zhubin / 筑宾)** | 1.0–1.2 cun perp. | Acute psychiatric mania, severe anxiety, delirium, clearing fetal toxins |
| **Yang Wei Mai** | **GB35 (Yangjiao / 阳交)** | 1.0–1.5 cun perp. | Acute lateral thoracic pain, sciatica, swelling of knee and foot |
| **Yin Qiao Mai** | **KD8 (Jiaoxin / 交信)** | 0.5–1.0 cun perp. | Severe persistent uterine bleeding, irregular menses, testicular pain |
| **Yang Qiao Mai** | **BL59 (Fuyang / 跗阳)** | 0.8–1.2 cun perp. | Acute severe sciatica, lumbar pain with inability to stand, foot drop |
"""
        st.markdown(xi_md)

    # =========================================================================
    # GUIDE 7: FRONT-MU & BACK-SHU MATRIX
    # =========================================================================
    elif sheet_choice.startswith("🏛️ Front-Mu & Back-Shu"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #34d399;">🏛️ 俞募穴脏腑辨证与配对总纲 (Front-Mu & Back-Shu Master Guide)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Classical Mu-Shu Pairing (俞募配穴法). <strong>Back-Shu points</strong> lie on the Bladder meridian on the back (Yang aspect) and tonify chronic deficiency; <strong>Front-Mu points</strong> lie on the chest/abdomen (Yin aspect) and drain acute excess heat.
            </div>
        </div>
        """)

        mu_shu_md = """
| Internal Organ | Back-Shu Point (背俞穴) | Spinal Vertebral Level | Front-Mu Point (腹募穴) | Front-Mu Anatomical Location | Mu-Shu Clinical Selection Rule |
|---|---|---|---|---|---|
| **Lung (LU)** | **BL13 (Feishu)** | T3 (spinous process) | **LU1 (Zhongfu)** | 6 cun lateral to midline, 1st ICS | Lung Yin def tonify BL13; Phlegm-heat drain LU1 |
| **Pericardium (PC)**| **BL14 (Jueyinshu)**| T4 (spinous process) | **RN17 (Danzhong)** | Midline of sternum, 4th ICS | Chest oppression drain RN17; Palpitations tonify BL14 |
| **Heart (HT)** | **BL15 (Xinshu)** | T5 (spinous process) | **RN14 (Juque)** | Midline of abdomen, 6 cun above navel | Heart blood def tonify BL15; Heart fire drain RN14 |
| **Liver (LV)** | **BL18 (Ganshu)** | T9 (spinous process) | **LV14 (Qimen)** | Mamillary line, 6th ICS | Liver blood def tonify BL18; Qi stagnation drain LV14 |
| **Gallbladder (GB)**| **BL19 (Danshu)** | T10 (spinous process) | **GB24 (Riyue)** | Mamillary line, 7th ICS | Gallstones & damp-heat drain GB24; Timidity tonify BL19 |
| **Spleen (SP)** | **BL20 (Pishu)** | T11 (spinous process) | **LV13 (Zhangmen)**| Tip of 11th free floating rib | Spleen Qi def tonify BL20; Cold food stagnation drain LV13 |
| **Stomach (ST)** | **BL21 (Weishu)** | T12 (spinous process) | **RN12 (Zhongwan)**| Midline of abdomen, 4 cun above navel | Stomach fire drain RN12; Stomach deficiency tonify BL21 |
| **San Jiao (SJ)** | **BL22 (Sanjiaoshu)**| L1 (spinous process) | **RN5 (Shimen)** | Midline of abdomen, 2 cun below navel | Fluid stagnation drain RN5; Water metabolism tonify BL22 |
| **Kidney (KD)** | **BL23 (Shenshu)** | L2 (spinous process) | **GB25 (Jingmen)** | Lower border of free 12th rib | Kidney deficiency tonify BL23; Renal colic palpate GB25 |
| **Large Intestine**| **BL25 (Dachangshu)**| L4 (spinous process) | **ST25 (Tianshu)** | 2 cun lateral to center of navel | Acute diarrhea/constipation drain ST25; Chronic tonify BL25 |
| **Small Intestine**| **BL27 (Xiaochangshu)**| S1 (1st sacral foramen) | **RN4 (Guanyuan)** | Midline of abdomen, 3 cun below navel | Deficiency cold warm RN4; Heat in intestines tonify BL27 |
| **Urinary Bladder**| **BL28 (Pangguangshu)**| S2 (2nd sacral foramen) | **RN3 (Zhongji)** | Midline of abdomen, 4 cun below navel | Acute cystitis drain RN3; Frequent urination tonify BL28 |
"""
        st.markdown(mu_shu_md)

    # =========================================================================
    # GUIDE 8: HUI-MEETING, COMMAND & LOWER HE-SEA POINTS
    # =========================================================================
    elif sheet_choice.startswith("⭐ Eight Influential"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #38bdf8;">⭐ 八会穴、六总穴与下合穴速查宝典 (Influential, Command & Lower He-Sea)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                The three foundational category matrices for somatic tissues, regional body topologies, and the Six Yang Fu bowels.
            </div>
        </div>
        """)

        st.markdown("""
### 1. Eight Influential / Hui-Meeting Points (八会穴)
| Tissue / Energy System | Hui-Meeting Point | Meridian | Primary Clinical Action |
|---|---|---|---|
| **Zang Organs (脏会)** | **LV13 (Zhangmen / 章门)** | Liver | Fortifies Spleen, harmonizes Liver-Spleen, relieves abdominal distension |
| **Fu Organs (腑会)** | **RN12 (Zhongwan / 中脘)** | Ren Mai | Master of all 6 Yang Fu bowels; relieves acid reflux, food stasis, and bloating |
| **Qi (气会)** | **RN17 (Danzhong / 膻中)** | Ren Mai | Regulates thoracic Qi, unbinds chest, stops asthma, wheezing, and emotional grief |
| **Blood (血会)** | **BL17 (Geshu / 膈俞)** | Bladder | Moves blood stasis, stops acute bleeding, nourishes blood in anemia |
| **Sinews & Tendons (筋会)** | **GB34 (Yanglingquan / 阳陵泉)** | Gallbladder | Relaxes tight sinews, relieves muscle spasms, contractures, and joint stiffness |
| **Blood Vessels (脉会)** | **LU9 (Taiyuan / 太渊)** | Lung | Harmonizes circulation, tonifies weak pulse, treats pulseless disease |
| **Bones (骨会)** | **BL11 (Dazhu / 大杼)** | Bladder | Treats osteoporosis, osteoarthritis, spinal rigidity, and bone Bi syndromes |
| **Marrow (髓会)** | **GB39 (Xuanzhong / 悬钟)** | Gallbladder | Nourishes brain marrow, stroke prevention, dementia, cervical myelopathy |

---

### 2. Six Command Points of Gao Wu & Ma Dan Yang (六总穴)
| Body Region | Command Point | Channel | Classical Rule & Clinical Indication |
|---|---|---|---|
| **Head & Nape (头项)** | **LU7 (Lieque / 列缺)** | Lung | "Head and nape seek Lieque" (头项寻列缺): Occipital headache, neck rigidity, colds |
| **Face & Mouth (面口)** | **LI4 (Hegu / 合谷)** | Large Intestine | "Face and mouth belong to Hegu" (面口合谷收): Toothache, Bell's palsy, sinusitis |
| **Abdomen (肚腹)** | **ST36 (Zusanli / 足三里)** | Stomach | "Belly and abdomen stay with Zusanli" (肚腹三里留): Epigastric pain, diarrhea |
| **Back & Lumbar (腰背)**| **BL40 (Weizhong / 委中)** | Bladder | "Lumbar spine and back seek Weizhong" (腰背委中求): Low back pain, sciatica |
| **Chest & Epigastrium (胸脘)**| **PC6 (Neiguan / 内关)** | Pericardium | Chest fullness, palpitations, nausea, vomiting, angina, motion sickness |
| **Lateral Ribs & Flanks (胁肋)**| **GB34 (Yanglingquan / 阳陵泉)**| Gallbladder | Hypochondriac pain, intercostal neuralgia, lateral torso pain, gallstones |

---

### 3. Lower He-Sea Points of the Six Fu Organs (六腑下合穴)
*Crucial rule: The Lower He-Sea points of the arm Yang channels (LI, SI, SJ) are located on the LOWER EXTREMITIES (Stomach and Bladder meridians).*

| Yang Fu Organ | Lower He-Sea Point | Meridian Location | Clinical Hallmark |
|---|---|---|---|
| **Stomach (ST)** | **ST36 (Zusanli / 足三里)** | Stomach Meridian | Epigastric pain, gastric ulcers, vomiting, food stagnation |
| **Large Intestine (LI)**| **ST37 (Shangjuxu / 上巨虚)**| Stomach Meridian | Acute enteritis, appendicitis, abdominal pain, diarrhea, constipation |
| **Small Intestine (SI)**| **ST39 (Xiajuxu / 下巨虚)**| Stomach Meridian | Lower abdominal cramping, borborygmus, flatulence, small bowel colic |
| **Gallbladder (GB)** | **GB34 (Yanglingquan / 阳陵泉)**| Gallbladder Meridian | Cholecystitis, gallstones, bitter taste, vomiting of bile |
| **Urinary Bladder (BL)**| **BL40 (Weizhong / 委中)** | Bladder Meridian | Acute dysuria, urinary retention, enuresis, cloudy urine |
| **San Jiao (TE/SJ)** | **BL39 (Weiyang / 委阳)** | Bladder Meridian | Fluid retention, edema, lower abdominal distension, oliguria |
""")

    # =========================================================================
    # GUIDE 9: EXTRA POINTS (JING WAI QI XUE) MASTER MATRIX
    # =========================================================================
    elif sheet_choice.startswith("📍 Extra Points"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #f472b6;">📍 高频经外奇穴考点矩阵 (Extra Points Master Board Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                The 30 essential Extra Points tested on Pan-Canadian and NCCAOM exams, organized by anatomical body region with safety depths and clinical indications.
            </div>
        </div>
        """)

        extra_md = """
| Region | Extra Point | Precise Anatomical Location | Needling Method & Depth | High-Yield Clinical Indications |
|---|---|---|---|---|
| **Head/Face** | **Yintang (印堂)** | At the midpoint between the two medial ends of eyebrows | Sub-Q 0.3–0.5 cun downward | Frontal headache, rhinitis, insomnia, infant fright |
| **Head/Face** | **Taiyang (太阳)** | 1 cun posterior to midpoint between outer canthus & eyebrow | Perp 0.3–0.5 cun / bleed | One-sided migraine, red painful eyes, toothache |
| **Head/Face** | **Sishencong (四神聪)**| Group of 4 points, each 1 cun anterior, post, lat to DU20 | Sub-Q 0.5–1.0 cun to DU20 | Insomnia, poor memory, dizziness, dementia, hydrocephalus |
| **Head/Face** | **Yuyao (鱼腰)** | At the midpoint of the eyebrow directly above pupil | Sub-Q 0.3–0.5 cun med/lat | Supraorbital pain, twitching of eyelids, facial paralysis |
| **Head/Face** | **Qiuhou (球后)** | Junction of lateral 1/4 and medial 3/4 of lower orbital rim | Slow perp 0.5–1.0 cun | Optic neuritis, glaucoma, myopia. **NEVER MANIPULATE** |
| **Head/Face** | **Bitong (鼻通)** | At the highest point of the nasolabial groove | Sub-Q 0.3–0.5 cun upward | Allergic rhinitis, sinusitis, anosmia, nasal polyp |
| **Head/Face** | **Anmian (安眠)** | Midpoint between GB20 and SJ17 (behind ear) | Perp 0.5–1.0 cun | Premier point for insomnia, palpitations, vertigo, hysteria |
| **Head/Face** | **Jinjin & Yuye (金津玉液)**| Left (Jinjin) and right (Yuye) veins under tongue | Prick to bleed with lancet | Sudden loss of voice, aphasia, vomiting, diabetes thirst |
| **Chest/Abdomen**| **Zigong (子宫)** | 3 cun lateral to RN3 (4 cun below navel) | Perp 0.8–1.2 cun | Uterine prolapse, female infertility, dysmenorrhea |
| **Chest/Abdomen**| **Tituo (提托)** | 4 cun lateral to RN4 (3 cun below navel) | Perp 0.8–1.2 cun | Severe uterine prolapse, hernia, lower abdominal distension |
| **Chest/Abdomen**| **Sanjiaojiu (三角灸)**| Triangle with navel as top apex; bottom sides = mouth width | Indirect moxibustion only | Chronic diarrhea, hernia, abdominal cold colic |
| **Back/Spine** | **Dingchuan (定喘)** | 0.5 cun lateral to lower border of C7 (DU14) | Perp-oblique 0.5–0.8 cun | Asthma, wheezing, bronchitis, cough, urticaria |
| **Back/Spine** | **Huatuojiaji (华佗夹脊)**| 0.5 cun lateral to spinous processes T1 through L5 | Perp-medial 0.5–1.0 cun | T1–T4 (Lung/Heart), T5–T8 (Digestive), L1–L5 (Urogenital) |
| **Back/Spine** | **Bailao (百劳)** | 2 cun superior to DU14, 1 cun lateral to midline | Perp 0.5–0.8 cun | Scrofula, neck rigidity, cough, night sweats |
| **Back/Spine** | **Yaoyan (腰眼)** | In depression 3.5 cun lateral to lower border of L4 | Perp 1.0–1.5 cun | Chronic lower back pain, orchitis, gynecological pain |
| **Back/Spine** | **Shiqizhuixue (十七椎)**| On midline below spinous process of 5th lumbar (L5) | Perp 0.5–1.0 cun | Acute severe lumbago, intractable dysmenorrhea, enuresis |
| **Upper Limb** | **Shixuan (十宣)** | At the tips of all ten fingers, 0.1 cun from free nail edge | Prick to bleed with lancet | Coma, sunstroke, high fever, infantile convulsions, shock |
| **Upper Limb** | **Sifeng (四缝)** | On palmar surface of fingers 2–5, midpoint of PIP crease | Prick to express yellow fluid | Childhood malnutrition (Gan syndrome), whooping cough |
| **Upper Limb** | **Baxie (八邪)** | On dorsum of hand at junction of red/white skin of webs | Oblique 0.5–0.8 cun | Arthritis of fingers, numbness, hand swelling, headache |
| **Upper Limb** | **Yaotongxue (腰痛穴)**| Dorsum of hand between 2nd/3rd and 4th/5th metacarpal bases | Oblique 0.5–0.8 cun to wrist| Acute lumbar sprain (needle while patient moves back) |
| **Upper Limb** | **Luozhen (落枕)** | On dorsum of hand between 2nd and 3rd metacarpal heads | Perp 0.5–0.8 cun | Acute stiff neck (torticollis), shoulder and arm pain |
| **Upper Limb** | **Erbai (二白)** | 4 cun proximal to wrist crease, on both sides of FCR tendon | Perp 0.5–1.0 cun | Hemorrhoids, prolapse of rectum, forearm neuralgia |
| **Upper Limb** | **Jianneiling (肩内陵)**| Midpoint between anterior axillary fold and LI15 | Perp 1.0–1.5 cun | Frozen shoulder (adhesive capsulitis), anterior shoulder pain |
| **Lower Limb** | **Heding (鹤顶)** | In depression above midpoint of superior patellar border | Perp 0.5–1.0 cun | Knee arthritis, weakness of knee joint, patellofemoral pain |
| **Lower Limb** | **Xiyan / Neixiyan (膝眼)**| In depressions lateral and medial to patellar ligament | Oblique 0.5–1.0 cun | Knee pain, swelling, gonarthritis, lower leg atrophy |
| **Lower Limb** | **Lanwei (阑尾穴)** | 2 cun inferior to ST36 on right lower leg | Perp 1.0–1.5 cun | Acute and chronic appendicitis (tender to palpation) |
| **Lower Limb** | **Danxue (胆囊穴)** | 1–2 cun directly inferior to GB34 (tender spot) | Perp 1.0–1.5 cun | Cholecystitis, gallstones, biliary ascariasis, flank pain |
| **Lower Limb** | **Bafeng (八风)** | On dorsum of foot at junction of red/white skin of webs | Oblique 0.5–0.8 cun | Toe arthritis, numbness, peripheral neuropathy, foot edema |
| **Lower Limb** | **Baichongwo (百虫窝)**| 1 cun superior to SP10 on vastus medialis | Perp 1.0–1.5 cun | Severe skin itching, urticaria, eczema, intestinal parasites |
"""
        st.markdown(extra_md)

    # =========================================================================
    # GUIDE 10: TONGUE DIAGNOSIS MASTER MATRIX
    # =========================================================================
    elif sheet_choice.startswith("👅 Tongue Diagnosis"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #ec4899;">👅 舌诊全景辨证精要卡 (Tongue Diagnosis Master Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Categorized by Tongue Body Color, Body Shape, Coating Color, Coating Moisture, and Organ Topography for rapid diagnostic recall.
            </div>
        </div>
        """)

        tongue_md = """
### 1. Tongue Body Color (舌质颜色)
| Body Color | Diagnostic Meaning | Primary Pathological Syndromes | Clinical Hallmark |
|---|---|---|---|
| **Pale / White (淡白舌)** | Yang Deficiency or Blood Deficiency | Spleen/Kidney Yang deficiency (if wet/swollen) or Liver Blood deficiency (if dry/thin) | Lack of warmth or nourishment reaching tongue vessels |
| **Light Red (淡红舌)** | Normal Zheng Qi | Healthy balanced constitution | Vibrant pink color with thin white coating and supple shape |
| **Red (红舌)** | Heat Syndrome | Interior full heat (if yellow coating) or Yin deficiency (if peeled/no coating) | Accelerated blood circulation from pathogenic fire |
| **Deep Red / Crimson (绛舌)** | Extreme Severe Heat | Warm pathogen entering Ying/Xue levels or severe Kidney Yin exhaustion | Dark crimson coloration; signifies risk of delirium/bleeding |
| **Purple / Dusky (紫暗/青紫舌)**| Blood Stasis or Extreme Cold | Qi stagnation blood stasis (red-purple) or Cold coagulating blood (blue-purple) | Petechiae, distended sublingual veins, intractable localized pain |

---

### 2. Tongue Body Shape & Demarcations (舌体形态)
| Body Shape | Visual Hallmark | Diagnostic Indication |
|---|---|---|
| **Swollen / Enlarged (胖大舌)** | Fills mouth, scallops on teeth | Spleen Qi deficiency with damp accumulation; Kidney Yang deficiency |
| **Thin / Small (瘦薄舌)** | Narrow, flat, diminished mass | Blood deficiency (if pale) or Yin deficiency with fluid exhaustion (if red/dry) |
| **Teeth Marks / Scalloped (齿痕舌)**| Indentations along lateral edges | Spleen Qi deficiency failing to transform internal damp fluids |
| **Cracked (裂纹舌)** | Fissures or deep transverse lines | Chronic Yin exhaustion, Stomach Yin deficiency (center cracks), or normal variant |
| **Prickles / Red Points (芒刺/红点)**| Raised erythematous strawberry papillae | Blazing interior heat; Tip (Heart fire), Sides (Liver fire), Center (Stomach fire) |
| **Stiff / Rigid (强硬舌)** | Inflexible, impairs speech | Wind-stroke warning sign, heat invading Pericardium, or severe phlegm misting |
| **Deviated (歪斜舌)** | Leans to one side upon protrusion | Internal Wind obstructing collaterals (classic stroke / TIA precursor) |
| **Flaccid / Limp (痿软舌)** | Completely limp, cannot protrude | Severe collapse of Qi, Blood, or Yin fluids |

---

### 3. Tongue Coating Color & Moisture (舌苔色泽与津液)
| Coating Feature | Clinical Presentation | Pathological Significance |
|---|---|---|
| **Thin White (薄白苔)** | Normal thin veil over surface | Normal healthy tongue, or early-stage exterior Wind-Cold attack |
| **Thick White (厚白苔)** | Dense white blanket obscuring body | Interior cold accumulation, damp-cold in middle burner, food stagnation |
| **Yellow (黄苔)** | Light yellow to deep brownish-yellow | Interior heat syndrome; deeper yellow signifies deeper, more toxic heat |
| **Grey / Black (灰黑苔)** | Dark grey or soot-like black coating | Extreme cold (if wet and slippery) or Extreme scorching heat (if dry and cracked) |
| **Greasy / Turbid (腻苔)** | Sticky, oily, cannot be scraped off | Heavy dampness, turbid phlegm retention, damp-heat, food accumulation |
| **Peeled / Mirror (剥苔/镜面舌)**| Patchy loss of coating / smooth red | Stomach and Kidney Yin exhaustion; complete loss of stomach root |

---

### 4. Tongue Organ Somatotopic Map (脏腑舌面分区)
- **Tongue Tip (舌尖)**: Heart & Lung (Upper Jiao) — Red tip indicates Heart fire or Lung exterior heat.
- **Tongue Center (舌中)**: Spleen & Stomach (Middle Jiao) — Central crack/peeling indicates Stomach Yin deficiency.
- **Tongue Lateral Borders (舌边)**: Liver & Gallbladder — Red or swollen sides indicate Liver Qi stagnation or Liver fire.
- **Tongue Root (舌根)**: Kidney, Urinary Bladder & Intestines (Lower Jiao) — Thick yellow coating at root indicates lower burner damp-heat.
- **Sublingual Veins (舌下静脉)**: Distended, dark purple, tortuous sublingual veins indicate systemic Blood Stasis.
"""
        st.markdown(tongue_md)

    # =========================================================================
    # GUIDE 11: 28 PULSES CLASSIFICATION
    # =========================================================================
    elif sheet_choice.startswith("⚖️ 28 Pulses"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #c89666;">⚖️ 二十八脉分类归纳总纲 (The 28 Canonical Pulses Taxonomic Matrix)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Categorized by Depth, Rate, Strength, and Morphological Shape for rapid exam recall and clinical differentiation.
            </div>
        </div>
        """)

        pulse_matrix_md = """
| Category | Pulse Types (脉象) | Clinical Hallmark | Primary Pathologies |
|---|---|---|---|
| **Depth (部位)** | **Floating (浮)**, Drumskin/Leather (革), Scallion-stalk (芤), Scattered (散) | Surface light touch | Exterior syndromes, floating Yang, blood hemorrhage |
| **Depth (部位)** | **Deep (沉)**, Hidden (伏), Confined (牢) | Deep bone/tendon level | Interior syndromes, deep visceral cold, fixed pain |
| **Rate (速率)** | **Slow (迟)**, Moderate/Relaxed (缓) | < 60 bpm (< 4 beats/breath) | Cold syndrome, Spleen dampness, Yang deficiency |
| **Rate (速率)** | **Rapid (数)**, Hurried (疾) | > 90 bpm (> 5 beats/breath) | Heat syndrome, acute fever, Yin deficiency fire |
| **Strength (力度)** | **Empty/Deficient (虚)**, Weak (弱), Minute (微), Soft/Soggy (濡) | Soft, compressible, faint | Qi, Blood, Yin, or Yang deficiency |
| **Strength (力度)** | **Full/Excess (实)**, Surging (洪), Long (长) | Powerful, expansive | Full excess Heat, phlegm/food stagnation |
| **Shape (形态)** | **Slippery (滑)**, Long (长) | Smooth, fluid like rolling pearls | Phlegm, dampness, food retention, pregnancy |
| **Shape (形态)** | **Choppy (涩)**, Short (短) | Rough, knife scraping bamboo | Blood stasis, Essence exhaustion |
| **Tension (张力)** | **Wiry (弦)**, Tight (紧) | Straight like guitar string / twisted rope | Liver stagnation, hypertension, severe cold pain |
| **Rhythm (节律)** | **Knotted (结)**, Intermittent (代), Abrupt (促) | Pauses in beat succession | Arrhythmias, organ Qi exhaustion, extreme heat |
"""
        st.markdown(pulse_matrix_md)

    # =========================================================================
    # GUIDE 12: MEDICAL RED FLAGS
    # =========================================================================
    elif sheet_choice.startswith("🩺 Medical Red Flags"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #f87171;">🩺 西医急症危险征象与紧急转诊全景指南 (Medical Red Flags & Referrals)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Critical clinical warning signs synthesized from David Anzaldua, MD (TCM Review Seminars). Conditions requiring immediate 911 EMS dispatch, emergency department evaluation, or urgent specialist workup.
            </div>
        </div>
        """)

        red_flags_md = """
| Body System | Clinical Presentation | Primary Rule Out | Urgency Level | Acupuncturist Mandatory Action |
|---|---|---|---|---|
| **Neurological** | Thunderclap 'worst headache of life', meningismus, vomiting | **Subarachnoid Hemorrhage (SAH)** | **Immediate 911** | Supine rest, call 911 immediately. Never needle analgesic points. |
| **Neurological** | Gradual confusion, unsteady gait weeks after minor head bump in elderly | **Chronic Subdural Hematoma (SDH)** | **Emergency ED (< 24h)** | Urgent head CT/MRI. Do not attribute to simple Jing deficiency. |
| **Neurological** | Sudden drop attack upon neck extension or rotation; 5 D's | **Vertebrobasilar Insufficiency (VBI)** | **Urgent Neuro (< 48h)** | **NO cervical manipulation**. Refer for carotid/vertebral Doppler. |
| **Neurological** | Unilateral temporal throbbing, jaw claudication, scalp tenderness, age > 50 | **Temporal Arteritis (Giant Cell)** | **Same-Day ED (< 12h)** | Immediate high-dose steroids to prevent irreversible blindness. |
| **Neurological** | Sudden facial droop, arm weakness, slurred speech (FAST criteria) | **Acute Ischemic Stroke / TIA** | **Immediate 911** | Note last known normal time. Expedite tissue plasminogen activator (tPA). |
| **Spine / Ortho** | Saddle anesthesia, urinary retention / bowel incontinence, leg weakness | **Cauda Equina Syndrome** | **Emergency ED (< 24h)** | Emergency decompression MRI/surgery within 24-48h to prevent paralysis. |
| **Spine / Ortho** | Constant dull back pain, worse at night, unrelieved by bed rest, weight loss | **Spinal Malignancy / Metastasis** | **Urgent Specialist** | Spinal MRI, CBC, ESR, protein electrophoresis. No spinal thrusts. |
| **Cardiovascular** | Crushing substernal chest pressure, cold sweats, dyspnea radiating to jaw/arm | **Acute Myocardial Infarction (MI)** | **Immediate 911** | Call 911. High Fowler position, monitor vitals, prepare AED. |
| **Cardiovascular** | Sudden awakening 1-2h into sleep gasping for air, orthopnea, bilateral edema | **Paroxysmal Nocturnal Dyspnea (PND)** | **Urgent Cardiology** | Decompensated left-sided CHF. Refer for diuretics and echocardiogram. |
| **Vascular / Leg** | Unilateral calf swelling > 3cm, redness, calf tenderness after flight | **Deep Vein Thrombosis (DVT)** | **Emergency ED (< 12h)** | **NEVER massage or needle calf**. Venous duplex ultrasound to prevent PE. |
| **Cardiopulmonary**| Sudden sharp pleuritic chest pain, severe dyspnea, tachycardia, hemoptysis | **Pulmonary Embolism (PE)** | **Immediate 911** | High mortality risk from dislodged DVT. Immediate oxygen & 911 transfer. |
| **Pediatric** | Child sitting in tripod position, drooling, inspiratory stridor, high fever | **Acute Epiglottitis** | **Immediate 911** | **NEVER insert tongue depressor**. Call 911 immediately for airway control. |
| **Abdominal** | Severe RLQ pain abruptly disappears, followed hours later by board-like rigidity | **Appendicitis Perforation (Peritonitis)** | **Immediate 911** | Sudden pain loss = rupture ('Honeymoon phase'). Emergency appendectomy. |
| **Abdominal** | Severe epigastric pain radiating directly to back, relieved by curling forward | **Acute Pancreatitis** | **Immediate 911 / ED** | Serum lipase & amylase. Risk of hemorrhagic necrotizing pancreatitis. |
| **Obstetric** | Amenorrhea, sharp unilateral pelvic pain, abnormal vaginal spotting | **Ruptured Ectopic Pregnancy** | **Immediate 911** | Life-threatening intra-abdominal hemorrhage. Immediate emergency transfer. |
"""
        st.markdown(red_flags_md)

    # =========================================================================
    # GUIDE 13: PHARMACOLOGY & HERB-DRUG INTERACTIONS
    # =========================================================================
    elif sheet_choice.startswith("💊 Pharmacology"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #a78bfa;">💊 常用西药药理机制与中草药配伍禁忌矩阵 (Pharmacology & Herb Interactions)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Essential pharmaceutical mechanisms, drug-induced TCM patterns, and high-risk herb interactions from TCM Review Seminars.
            </div>
        </div>
        """)

        pharma_md = """
| Drug Class & Examples | Western Mechanism | TCM Pattern Presentation | High-Risk Herb Interactions | Clinical Safety Pearl |
|---|---|---|---|---|
| **Anticoagulants**<br/>Warfarin (Coumadin), Heparin | Inhibits Vitamin K-dependent clotting factors (II, VII, IX, X) | Spontaneous bleeding, petechiae, purple tongue | **Dang Gui, Dan Shen, Tao Ren, Hong Hua, San Qi, Shui Zhi** | Drastically spikes INR > 4.0; risk of fatal hemorrhagic stroke. |
| **Antiplatelets**<br/>Aspirin, Clopidogrel (Plavix) | Irreversibly blocks platelet cyclooxygenase / ADP receptors | Upper GI irritation, bleeding diathesis, easy bruising | **Ginkgo Biloba (Bai Guo), Da Suan (Garlic), Dan Shen** | Stop all blood-invigorating herbs 1-2 weeks before surgery. |
| **Corticosteroids**<br/>Prednisone, Dexamethasone | Suppresses PLA2, cytokine cascade, and immune system | Kidney Yin & Jing exhaustion, Empty Heat, fluid dampness | Warm drying tonics exacerbate fluid retention; watch immune status | Never stop abruptly; risk of fatal adrenal crisis. |
| **Loop Diuretics**<br/>Furosemide (Lasix), Bumetanide | Inhibits Na+/K+/2Cl- symporter in thick ascending limb | Severe fluid/Yin consumption, thirst, weakness | **Gan Cao (Licorice)** compounds potassium wasting | Synergistic hypokalemia triggers fatal ventricular arrhythmias. |
| **Cardiac Glycosides**<br/>Digoxin (Lanoxin) | Inhibits Na+/K+-ATPase, boosting cardiac contractility | Yellow-green visual halos, bradycardia, nausea | **Gan Cao** (via hypokalemia) and **calcium-rich herbs** (Mu Li, Long Gu) | Hypokalemia dramatically increases toxic digitalis sensitivity. |
| **Beta-Blockers**<br/>Metoprolol, Atenolol, Propranolol | Blocks beta-1 adrenergic receptors; drops HR & BP | Slow pulse (Chi Mai), cold extremities, lethargy | Cold sedatives; caution with damp-forming tonics | **Masks hypoglycemia warning signs** (tremors, tachycardia) in diabetics. |
| **Antidiabetics**<br/>Metformin, Glipizide, Insulin | Decreases hepatic glucose production; boosts uptake | Spleen Qi deficiency with nausea/diarrhea | Hypoglycemic herbs: **Huang Lian, Shan Yao, Cang Zhu** | Synergistic hypoglycemia; ensure patient eats before needling. |
| **SSRIs / SNRIs**<br/>Fluoxetine, Sertraline, Duloxetine | Blocks reuptake of serotonin / norepinephrine in CNS | Liver Qi stagnation with internal heat, dry mouth | **St. John's Wort, Ma Huang** | Combined use triggers life-threatening **Serotonin Syndrome**. |
| **NSAIDs**<br/>Ibuprofen, Naproxen, Meloxicam | Inhibits COX-1 and COX-2 prostaglandin synthesis | Stomach Yin deficiency, epigastric burning, ulcer | Co-admin with blood-invigorating herbs | Leading cause of non-ulcer GI bleeding; check for black tarry stools. |
| **ACE Inhibitors**<br/>Lisinopril, Enalapril, Ramipril | Blocks conversion of Angiotensin I to Angiotensin II | Dry non-productive cough, Yin deficiency tickle | Potassium-rich herbs; cough mimics Lung Yin deficiency | Drug-induced cough does not respond to Lung herbs; switch to ARB. |
"""
        st.markdown(pharma_md)

    # =========================================================================
    # GUIDE 14: ACUPUNCTURE MODALITIES
    # =========================================================================
    elif sheet_choice.startswith("⚡ Acupuncture Modalities"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #38bdf8;">⚡ 针灸辅助疗法精要卡：电针参数、焦氏头针与耳穴 (Acupuncture Modalities)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Electroacupuncture parameters, Jiao Shunfa scalp somatotopic lines, and Auricular master points for Pan-Canadian and board licensing exams.
            </div>
        </div>
        """)

        modalities_md = """
### 1. Electro-Acupuncture (EA) Waveform & Frequency Guide
| Waveform / Frequency | Neurochemical Mechanism | Clinical Indications | Critical Safety Limits |
|---|---|---|---|
| **Low Frequency (2–5 Hz Continuous)** | Releases **Beta-Endorphin** & Enkephalins in CSF | Chronic dull pain, motor weakness, paralysis, Bells palsy | Rhythmic visible twitch; limit treatment to 20-30 mins |
| **High Frequency (50–100 Hz Continuous)** | Releases **Dynorphin** in spinal cord | Acute severe pain, muscle spasm, joint inflammation, anesthesia | Rapid tetanic buzz; avoids muscle fatigue |
| **Dense-Disperse (2 Hz / 100 Hz Cycling)** | Releases **all 3 opioid peptides**; prevents nerve habituation | Sciatica, chronic intractable back pain, severe arthralgia | **Gold standard for clinical pain analgesia** |
| **Intermittent / Discontinuous Mode** | Pulse-pause cycle simulates voluntary motor firing | Flaccid muscle paralysis, stroke rehabilitation, foot drop | Prevents neuromuscular fatigue |

> ⚠️ **Absolute EA Contraindications**: NEVER use on patients with cardiac pacemakers/ICDs. NEVER cross the heart (e.g. left arm to right arm, or anterior chest to posterior thorax). NEVER cross the brainstem/carotid sinus.

---

### 2. Jiao Shunfa Scalp Acupuncture Lines (Pan-Canadian Blueprint)
| Scalp Line | Anatomical Location | Somatotopic Division | Clinical Uses |
|---|---|---|---|
| **MS6 Dingnie Qianxiexian (Motor Line)** | Qianshencong (1 cun anterior to GV20) to GB6 (Xuanli) | • **Upper 1/5**: Lower limb & trunk<br/>• **Middle 2/5**: Upper limb & hand<br/>• **Lower 2/5**: Face, speech, salivation | Contralateral motor hemiplegia, stroke rehabilitation, central facial palsy. Twirl 200 rpm. |
| **MS7 Dingnie Houxiexian (Sensory Line)** | 1.5 cun posterior and parallel to MS6 (GV20 to GB7) | • **Upper 1/5**: Lower limb sensation<br/>• **Middle 2/5**: Upper limb sensation<br/>• **Lower 2/5**: Facial sensory numbness | Contralateral sensory paresthesia, numbness, burning pain. |
| **MS8 Chorea & Tremor Line** | Parallel and 1.5 cun anterior to MS6 (Motor Line) | Full line | Parkinsons tremors, chorea, intention tremors. |
| **MS10 & MS11 Speech Areas II & III** | Vertically down from parietal tubercle (II) / 4cm posterior (III) | Posterior speech areas | Receptive / sensory aphasia, nominal aphasia. |

---

### 3. Auricular Acupuncture Master Points & NADA Protocol
| Auricular Point | Anatomical Zone on Ear | Primary Physiological Function | Clinical Applications |
|---|---|---|---|
| **Shenmen (神门)** | Apex of Triangular Fossa | Calms spirit, alleviates pain, reduces cortical excitation | Anxiety, insomnia, pain relief, hypertension, stress |
| **Sympathetic (交感)** | Junction of inferior antihelix crus & internal helix | Regulates autonomic balance, dilates blood vessels, visceral antispasmodic | GI colic, gallstones, angina, arterial spasm |
| **Point Zero (零点)** | Geometric center of ear at root of ascending helix | Homeostatic master reset, anchors autonomic nervous system | General physiological balancing, shock recovery |
| **NADA 5-Point Protocol** | Sympathetic, Shenmen, Kidney, Liver, Lung | Holistic detox, autonomic regulation, emotional trauma recovery | Substance abuse withdrawal, PTSD, smoking cessation |
"""
        st.markdown(modalities_md)

    # =========================================================================
    # GUIDE 15: ROOT VS MANIFESTATION (BEN & BIAO)
    # =========================================================================
    elif sheet_choice.startswith("🎯 Root vs Manifestation"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #34d399;">🎯 标本缓急与治则配属全解矩阵 (Ben & Biao Treatment Principles)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Classical strategies for managing root causes vs acute secondary manifestations, upright vs pathogenic priority, and regular vs non-contrary treatment methods.
            </div>
        </div>
        """)

        principles_md = """
### 1. Root (Ben / 本) vs Manifestation (Biao / 标) Priority Rules
| Strategy | Clinical Scenario | Classical Rule | Representative Clinical Examples |
|---|---|---|---|
| **Treat Biao Urgently (急则治其标)** | Secondary manifestation is acute, agonizing, or life-threatening | When branch threatens life, treat branch first | • **Massive bleeding / hemorrhage**: Stop bleeding first (Biao), then tonify Qi/Blood (Ben).<br/>• **Severe acute dyspnea**: Relieve wheezing first, then tonify Kidney/Lung.<br/>• **Agonizing acute pain / urinary retention**: Unblock retention first. |
| **Treat Ben in Chronic Conditions (缓则治其本)** | Manifestations are mild, chronic, or non-life-threatening | Once acute crisis passes, treat fundamental root | • **Chronic lumbar soreness**: Tonify Kidney Yang directly without chasing dull back ache.<br/>• **Chronic allergic rhinitis in remission**: Tonify Lung and Spleen Qi. |
| **Treat Ben and Biao Simultaneously (标本同治)** | Both root deficiency and branch excess are equally prominent | Dual focus prevents either side from decompensating | • **Spleen Qi Deficiency with Damp Edema**: Tonify Spleen (Ben) while leaching dampness (Biao).<br/>• **Exterior Wind-Cold with Interior Qi Deficiency**: Release exterior while tonifying upright Qi. |

---

### 2. Upright Qi (Fu Zheng) vs Pathogenic Evil (Qu Xie) Allocation
| Principle | Patient Constitution vs Pathogenic Evil | Clinical Rule | Example Strategy |
|---|---|---|---|
| **Tonify Upright Only (单纯扶正)** | Pure deficiency pattern with no active pathogen | Tonify without fear of feeding evil | Postpartum exhaustion, chronic convalescent weakness |
| **Expel Pathogen Only (单纯祛邪)** | Strong constitutional Zheng Qi with acute severe pathogen | Purge forcefully without holding back | Early-stage Yangming organ excess constipation (Da Cheng Qi Tang) |
| **Expel Pathogen First, Tonify Later (先攻后补)** | Severe pathogenic excess in a patient whose Zheng Qi cannot tolerate tonics | Tonifying would trap and feed the pathogen ('关门留寇') | Severe food stagnation with high fever; purge accumulation before nourishing |
| **Tonify Upright First, Expel Later (先补后攻)** | Extreme constitutional collapse where purging would cause immediate demise | Patient would die from purgative exhaustion | Extreme constitutional depletion with intestinal parasites; tonify Qi before deworming |
| **Expel and Tonify Concurrently (攻补兼施)** | Deficiency and excess inextricably interwoven | Tonify upright while expelling evil simultaneously | Blood deficiency with severe blood stasis; Spleen deficiency with damp-heat |

---

### 3. Regular Treatment (Zheng Zhi) vs Non-Contrary Treatment (Fan Zhi)
| Method | Clinical Principle | Classical Formula | Clinical Indication |
|---|---|---|---|
| **Treating Cold with Heat (寒者热之)** | Regular Treatment (正治) | Warm herbs/moxa for Cold | Interior Cold / Yang deficiency with Si Ni Tang |
| **Treating Heat with Cold (热者寒之)** | Regular Treatment (正治) | Cold/Cool herbs for Heat | Full Heat with Bai Hu Tang |
| **Treating Heat with Heat (热因热用)** | Non-Contrary / Indirect (反治) | Use Hot herbs for True Cold with **False Heat** | **Dai Yang Syndrome** (True cold in lower burner pushing floating false Yang to face) |
| **Treating Cold with Cold (寒因寒用)** | Non-Contrary / Indirect (反治) | Use Cold herbs for True Heat with **False Cold** | **Jueyin Reversal Cold** (Extreme interior heat with deep cold extremities) |
| **Tonify for Fullness (塞因塞用)** | Non-Contrary / Indirect (反治) | Tonify for pseudo-distension | Severe Spleen deficiency abdominal bloating |
| **Drain for Diarrhea (通因通用)** | Non-Contrary / Indirect (反治) | Purge for pseudo-diarrhea | Damp-Heat dysentery with stasis; lochial retention diarrhea |
"""
        st.markdown(principles_md)

# -*- coding: utf-8 -*-
"""Clinical Expansion Script: Generates 12 Board Exam Cases and 12 Diagnostic Patterns."""

import pprint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# 12 NEW COMPREHENSIVE CLINICAL CASES
# =============================================================================
NEW_CASES = [
    {
        "id": "CASE-024",
        "title": "Patient Intake: 24yo Male (Cystic Fibrosis with Secondary Bronchiectasis)",
        "category": "Internal Medicine & Respiratory",
        "patient": {
            "age": 24,
            "gender": "Male",
            "occupation": "Graduate Student in Biology",
            "chief_complaint": "Chronic paroxysmal cough with blood-streaked sputum, wheezing, dyspnea on mild exertion, and drenching night sweats for 6 weeks.",
            "history": "Diagnosed with cystic fibrosis in early childhood. Developed secondary bronchiectasis confirmed by high-resolution chest CT showing localized bronchial dilation in bilateral lower lobes. Negative PPD tuberculin test. Maintained on rotating antibiotic courses, inhaled bronchodilators, and mucolytics. Reports progressive physical wasting, dry mouth, persistent sore throat, and heart palpitations.",
            "four_examinations": {
                "inspection": "Emaciated, tall slender habitus; prominent malar flush (bright red cheeks); dry cracked lips; dull red tongue body with anterior and central peeling (geographic coat) and fine transverse cracks in the Lung zone.",
                "auscultation_olfaction": "Rapid, shallow, wheezing respiration; breathy hoarse voice; persistent hacking cough producing scanty, tenacious, blood-streaked (rust-colored) sputum.",
                "inquiry": "Constant unquenchable thirst with preference for small cool sips; drenching nocturnal sweats soaking bedclothes; palpitations during evening hours; five-palm heat (burning sensation in soles, palms, chest); severe fatigue.",
                "palpation": "Skin feels dry and warm to touch especially in late afternoon; radial pulse is Fine/Thready (Xi) and Rapid (Shuo) with weakness in both Cun positions."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Primary Pattern Identification (Zang-Fu & Eight Principles)",
                "prompt": "Based on the presentation of chronic cough with blood-streaked sputum, emaciation, night sweats, red peeled tongue, and a thready-rapid pulse, what is the primary TCM diagnosis?",
                "options": [
                    "A. Wind-Heat Invading the Lung with Phlegm-Heat",
                    "B. Lung and Kidney Yin Deficiency with Empty Fire Flaring (Fei Shen Yin Xu)",
                    "C. Spleen and Lung Qi Deficiency with Damp Phlegm",
                    "D. Liver Fire Invading the Lung Scorching Blood Vessels"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Wind-Heat invasion presents with acute onset fever, chills, sore swollen throat, yellow purulent sputum, and a floating-rapid pulse. This patient has a longstanding constitutional pathology with hallmark signs of Yin deficiency.",
                    "B": "✅ **Correct (Lung & Kidney Yin Deficiency):** Chronic disease consuming Yin fluids impairs the moistening and descending of Lung Qi. Empty Fire flares upward, damaging bronchial capillaries (blood-streaked sputum) and producing five-palm heat, malar flush, night sweats, peeled red tongue, and a thready-rapid pulse (CAM & Maciocia).",
                    "C": "❌ **Incorrect:** Spleen and Lung Qi deficiency presents with copious white watery or foamy sputum, pale flabby tongue with teeth marks, loose stools, and an empty/weak pulse without night sweats or hemoptysis.",
                    "D": "❌ **Incorrect:** Liver Fire invading the Lung produces sudden bursts of violent spasmodic coughing triggered by emotional rage, severe hypochondriac pain, bitter taste in mouth, wiry-rapid pulse, and thick yellow coat."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Cardinal Point Prescription & Confluent Strategy",
                "prompt": "Which acupuncture point prescription best addresses both the acute hemoptysis/cough and the constitutional root Yin deficiency in this case?",
                "options": [
                    "A. LU1 (Zhongfu), LU7 (Lieque), KI6 (Zhaohai), HT6 (Yinxi), LU9 (Taiyuan), KI3 (Taixi), BL43 (Gaohuangshu)",
                    "B. BL13 (Feishu), SP4 (Gongsun), PC6 (Neiguan), CV12 (Zhongwan), ST40 (Fenglong), LU5 (Chize)",
                    "C. LI4 (Hegu), LI11 (Quchi), GV14 (Dazhui), LU10 (Yuji), ST44 (Neiting)",
                    "D. BL23 (Shenshu), GV4 (Mingmen), CV4 (Guanyuan), KI3 (Taixi), BL20 (Pishu)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** This formula combines the master Eight Confluent pair LU7 + KI6 (opening the Ren Mai and Yin Qiao Mai to moisten the throat, lung, and chest); HT6 (Xi-Cleft of Heart, premier empirical point for night sweats); LU9 + KI3 (Yuan-Source points tonifying Lung/Kidney Yin); LU1 (Front-Mu regulating Lung Qi); and BL43 (Gaohuangshu, renowned historical point for profound consumptive Yin/Blood deficiency).",
                    "B": "❌ **Incorrect:** SP4 + PC6 opens the Chong Mai and Yin Wei Mai for middle jiao dampness and stomach nausea; ST40 dissolves phlegm. This prescription does not sufficiently nourish Kidney Yin or halt empty fire hemoptysis.",
                    "C": "❌ **Incorrect:** Pure heat-clearing dispersal formula (LI11, GV14, ST44) for acute exterior Yangming heat; it would further dry up precious Yin fluids.",
                    "D": "❌ **Incorrect:** Warming Kidney Yang tonification formula (Mingmen GV4 with Shenshu BL23); contraindicated in Yin deficiency with empty heat."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Clinical Precautions & Anatomical Safety",
                "prompt": "What is the critical anatomical safety precaution when needling thoracic points (LU1, BL13, BL43) in an emaciated patient with chronic lung disease?",
                "options": [
                    "A. Puncture perpendicularly 1.5 to 2.0 cun to reach the pleura and stimulate lung parenchymal circulation.",
                    "B. Puncture strictly obliquely or transverse-obliquely 0.5 to 0.8 cun away from the lung field; never puncture perpendicularly to prevent traumatic pneumothorax.",
                    "C. Apply heavy direct scarring moxibustion over the upper ribs for 45 minutes.",
                    "D. Needling should be replaced by deep vigorous tuina cupping over the subclavicular triangle."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect (High Risk):** Deep perpendicular needling on the chest or upper back directly punctures the parietal and visceral pleura, causing tension pneumothorax—a life-threatening emergency (Deadman warning).",
                    "B": "✅ **Correct (Pneumothorax Prevention):** Emaciated patients have diminished subcutaneous adipose tissue and thinned chest walls. Needling LU1, BL13, and BL43 must strictly follow oblique or transverse insertion directed along the intercostal ribs, never perpendicular.",
                    "C": "❌ **Incorrect:** Direct scarring moxibustion is contraindicated in active Yin deficiency with hemoptysis.",
                    "D": "❌ **Incorrect:** Deep aggressive cupping over the subclavicular fossa can cause vascular bruising and pleural shearing."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Lung and Kidney Yin Deficiency with Empty Fire Flaring (Fei Shen Yin Xu, Xu Huo Shang Yan)",
                "Consumptive Pulmonary Fluid Exhaustion with Bronchial Vessel Injury"
            ],
            "treatment_principles": [
                "Nourish Lung and Kidney Yin (滋养肺肾之阴)",
                "Clear Empty Heat and Astringe Capillary Bleeding (清降虚火，凉血止血)",
                "Moisten the Respiratory Tract and Calm Wheezing (润肺降逆，定喘止咳)"
            ],
            "cardinal_points": ["LU1", "LU7", "KI6", "HT6", "LU9", "KI3", "BL43", "BL13"],
            "synergies": [
                "Eight Confluent Vessel Master-Couple pair (LU7 Lieque + KI6 Zhaohai) opens the Ren Mai and Yin Qiao Mai to flood the bronchial mucosa with Yin fluids.",
                "Xi-Cleft night sweat astringent pair (HT6 Yinxi + KI6 Zhaohai) arrests nocturnal fluid loss.",
                "Consumptive tonic pair (LU9 Taiyuan + BL43 Gaohuangshu) repairs deep structural pulmonary tissue."
            ],
            "cautions": "ANATOMICAL DANGER: Emaciated patients with chronic bronchiectasis have high apical pleura. Never needle LU1, BL13, or BL43 perpendicularly. Confirm patient does not have massive active hemoptysis (>100 mL/24h) which requires immediate emergency transport."
        }
    },
    {
        "id": "CASE-025",
        "title": "Patient Intake: 89yo Female (Severe Geriatric Constipation & Intestinal Dryness)",
        "category": "Geriatric & Digestive",
        "patient": {
            "age": 89,
            "gender": "Female",
            "occupation": "Retired Seamstress",
            "chief_complaint": "Intractable constipation with bowel movements only once every 8 to 10 days, accompanied by dry scybalous stools, dry mouth, and withered skin.",
            "history": "Suffering from chronic constipation for over 12 years, progressively worsening. Stool is dry, small, and hard like sheep dung, requiring manual evacuation or enemas. Has tried high-fiber diets and stimulant laxatives (senna, bisacodyl) with diminishing efficacy and abdominal cramping. Patient is emaciated, constantly sips warm water to quench unquenchable mouth dryness, and has lusterless pale skin and brittle ridged fingernails.",
            "four_examinations": {
                "inspection": "Frail, cachectic habitus; dry wrinkled lusterless facial complexion; dry brittle split nails; pale-red tongue body with completely peeled geographic coat (mirror tongue) and prominent central longitudinal cracks.",
                "auscultation_olfaction": "Weak, thin, low-pitched voice; slow deliberate speech; shortness of breath upon walking across room.",
                "inquiry": "No bowel movement for 7 days; severe exhaustion after attempting defecation; constant mouth dryness with frequent sips of water; dizziness on standing (orthostatic); dull abdominal discomfort without acute sharp pain.",
                "palpation": "Soft flaccid abdominal wall without rebound tenderness; palpable hard fecal impaction in the left iliac fossa (sigmoid colon) non-tender to pressure; radial pulse is Fine/Thready (Xi) and Choppy/Hesitant (Se)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Diagnosis according to Eight Principles & Six Stages",
                "prompt": "Based on the severe constipation with sheep dung stools, emaciation, lusterless dry skin, peeled mirror tongue, and a thready-choppy pulse in an 89yo patient, what is the diagnosis?",
                "options": [
                    "A. Yangming Bowel Excess Heat Pattern (Da Chang Shi Re)",
                    "B. Yangming Level: Blood and Yin Deficiency with Intestinal Fluid Depletion (Chang Zao Bian Bi)",
                    "C. Taiyin Spleen Deficiency Cold with Excessive Damp Accumulation",
                    "D. Shaoyang Gallbladder Damp-Heat Obstruction"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Yangming Bowel Excess Heat (Cheng Qi Tang pattern) presents with high tidal fever, profuse sweating, abdominal fullness that is severe and worse on pressure (Ju An), delirious speech, and a deep forceful rapid pulse. Applying drastic purgatives to this 89yo emaciated patient would cause fatal fluid and Yang collapse.",
                    "B": "✅ **Correct (Blood/Yin Deficiency with Intestinal Dryness):** In elderly patients, constitutional Blood and Yin decline depletes the bodily fluids (Jin Ye) that lubricate the lower intestines. The bowel becomes dry like a riverbed without water ('no water to float the boat'). Characterized by sheep dung stools, lusterless skin, dry peeled tongue, and a thready-choppy pulse.",
                    "C": "❌ **Incorrect:** Taiyin Cold-Damp presents with watery diarrhea, abdominal pain relieved by warmth and pressure, pale flabby tongue with thick slippery white coat, and a slow pulse—the exact opposite of dry constipation.",
                    "D": "❌ **Incorrect:** Shaoyang pattern presents with alternating chills and fever, bitter taste, hypochondriac fullness, and a wiry pulse."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Strategic Acupuncture Treatment Prescription",
                "prompt": "Which point combination best embodies the clinical strategy of 'Increasing water to float the boat' (Zeng Ye Run Chang) for this patient?",
                "options": [
                    "A. ST25 (Tianshu), ST37 (Shangjuxu), SJ6 (Zhigou), KI6 (Zhaohai), SP6 (Sanyinjiao), CV12 (Zhongwan)",
                    "B. LI11 (Quchi), ST44 (Neiting), LI4 (Hegu), ST25 (Tianshu), LR3 (Taichong) with vigorous reducing method",
                    "C. GV4 (Mingmen), BL23 (Shenshu), CV4 (Guanyuan), ST36 (Zusanli) with heavy warming moxa cones",
                    "D. BL25 (Dachangshu), BL28 (Pangguangshu), CV3 (Zhongji), SP9 (Yinlingquan) with bloodletting"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** This formula combines the premier empirical constipation pair SJ6 + KI6 (Zhigou clears the San Jiao pathway while Zhaohai nourishes Kidney Yin and lower burner fluids); ST25 + ST37 (Front-Mu and Lower He-Sea of Large Intestine to gently regulate peristalsis without harsh draining); SP6 (nourishes Blood and Yin); and CV12 (harmonizes middle burner Qi).",
                    "B": "❌ **Incorrect:** Strong reducing method on LI11, ST44, and LI4 is designed to purge Yangming Fire and would further exhaust this frail patient's Yin fluids.",
                    "C": "❌ **Incorrect:** Heavy direct moxibustion on Mingmen and Guanyuan warms Yang and dries Dampness, which would aggravate severe intestinal dryness.",
                    "D": "❌ **Incorrect:** Bloodletting is strongly contraindicated in severe Blood/Yin deficiency in an 89-year-old."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Clinical Empirical Point Pairing Mechanism",
                "prompt": "What is the classic textbook rationale for combining SJ6 (Zhigou) with KI6 (Zhaohai) in treating dry constipation?",
                "options": [
                    "A. SJ6 expels external wind pathogens while KI6 drains dampness through diuresis.",
                    "B. SJ6 regulates San Jiao Qi movement in the bowels while KI6 nourishes Yin fluids to moisten the intestines.",
                    "C. SJ6 arrests vomiting while KI6 anchors ascending Liver Yang.",
                    "D. SJ6 stops diarrhea while KI6 consolidates Kidney Jing."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Neither point is used here for exterior wind or diuretic damp draining.",
                    "B": "✅ **Correct (SJ6 + KI6 Synergy):** SJ6 (Fire point of San Jiao) regulates the Qi mechanism of the intestines and unblocks stagnation; KI6 (Yin Qiao Master) generates Kidney water and lower burner fluids. Together, they create the ideal synergy of promoting movement while nourishing moisture ('Zeng Ye Run Chang').",
                    "C": "❌ **Incorrect:** Irrelevant to intestinal constipation.",
                    "D": "❌ **Incorrect:** Both points promote smooth evacuation in this context, not astringency."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Blood and Yin Deficiency with Intestinal Fluid Depletion (Xue Xu Yin Kui, Chang Zao Bian Bi)",
                "Yangming Level Dryness with Depleted Fluid Reservoir"
            ],
            "treatment_principles": [
                "Nourish Blood and Enrich Yin to Lubricate the Intestines (养血滋阴，润肠通便)",
                "Regulate Lower Jiao Qi Movement Gently (理气通导，增液行舟)"
            ],
            "cardinal_points": ["ST25", "ST37", "SJ6", "KI6", "SP6", "CV12", "ST36"],
            "synergies": [
                "Empirical Fluid-Moving pair (SJ6 Zhigou + KI6 Zhaohai) generates Yin fluids and moves stagnant fecal matter.",
                "Large Intestine Mu-He combination (ST25 Tianshu + ST37 Shangjuxu) restores colon motility.",
                "Blood-nourishing duo (SP6 Sanyinjiao + ST36 Zusanli) replenishes postnatal Qi and Blood."
            ],
            "cautions": "STIMULANT LAXATIVE WARNING: Strictly avoid drastic bitter-cold purgatives (Da Huang, Mang Xiao, Senna). Ensure gentle needle manipulation (even/reinforcing) to prevent needle shock in frail geriatric patients. Check for fecal impaction with bowel obstruction signs."
        }
    },
    {
        "id": "CASE-026",
        "title": "Patient Intake: 47yo Male (Acute Biliary Colic / Cholecystitis)",
        "category": "Internal Medicine & Digestive",
        "patient": {
            "age": 47,
            "gender": "Male",
            "occupation": "Construction Contractor",
            "chief_complaint": "Severe paroxysmal cramping pain in the right hypochondrium radiating to the right shoulder and back, accompanied by nausea, vomiting of bitter bile, and bright yellow sclera.",
            "history": "Episodes of dull right upper quadrant fullness for 6 months after eating fried foods. Last night, after a celebratory dinner of barbecued pork and beer, experienced sudden excruciating right subcostal pain radiating upward through the right scapula. Vomited gastric contents and greenish-yellow bitter fluid three times. Temperature is 38.3°C. Dark amber urine and light clay-colored stools.",
            "four_examinations": {
                "inspection": "Patient curled forward holding right upper abdomen in distress; sclera and facial skin display bright orange-yellow jaundice; Red tongue body with thick, sticky, foul-smelling yellow coating.",
                "auscultation_olfaction": "Groaning loudly with each spasm; heavy coarse breathing; foul breath odor.",
                "inquiry": "Intense cramping right subcostal pain; severe bitter taste in mouth; burning sensation throughout epigastrium; fever with chills; complete repulsion toward food.",
                "palpation": "Acute tenderness and localized muscle guarding at the right costal margin with positive Murphy's sign (sudden arrest of inspiration upon deep subcostal palpation); acute exquisite tenderness at Dannangxue (Extra point below right GB34); radial pulse is Wiry (Xian) and Slippery-Rapid (Hua-Shuo)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Primary Zang-Fu Pattern Identification",
                "prompt": "What is the primary TCM pattern for this presentation of acute right hypochondriac colicky pain radiating to the scapula, bright jaundice, bitter taste, yellow greasy tongue coat, and a wiry-slippery-rapid pulse?",
                "options": [
                    "A. Liver Qi Stagnation with Spleen Deficiency",
                    "B. Damp-Heat in Liver and Gallbladder with Biliary Obstruction (Gan Dan Shi Re)",
                    "C. Cold Coagulation in the Liver Channel",
                    "D. Spleen and Stomach Damp-Heat with Food Stagnation only"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Liver-Spleen disharmony presents with dull distension without fever, jaundice, or positive Murphy's sign, with a wiry-weak pulse and thin white coat.",
                    "B": "✅ **Correct (Damp-Heat in Liver & Gallbladder):** Heavy alcohol and fatty foods create internal Damp-Heat that steams the Liver and Gallbladder. The bile ducts become congested and obstructed, producing excruciating right subcostal colic radiating to the right shoulder, Murphy's sign, jaundice, dark urine, yellow greasy tongue coat, and a wiry-slippery-rapid pulse.",
                    "C": "❌ **Incorrect:** Cold in the Liver channel produces pain in the scrotum or lower abdomen relieved by heat, with pale tongue and deep slow wiry pulse.",
                    "D": "❌ **Incorrect:** Pure middle jiao food stagnation centers on the epigastrium with foul belching and abdominal distension, lacking jaundice and biliary radiation."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Empirical & Channel Point Selection",
                "prompt": "Which acupuncture prescription includes the premier empirical point for acute gallbladder colic and clearing Damp-Heat?",
                "options": [
                    "A. Dannangxue (EX-LE6), GB34 (Yanglingquan), GB24 (Riyue), LR14 (Qimen), SP9 (Yinlingquan), LI11 (Quchi), BL19 (Danshu)",
                    "B. CV12 (Zhongwan), ST36 (Zusanli), SP4 (Gongsun), PC6 (Neiguan), BL20 (Pishu)",
                    "C. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 (Mingmen), BL52 (Zhishi)",
                    "D. LU7 (Lieque), LI4 (Hegu), BL13 (Feishu), GV14 (Dazhui)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** Dannangxue (located 1-2 cun below right GB34) is the legendary empirical point for acute cholecystitis and gallstones; GB34 (He-Sea of Gallbladder) unblocks biliary flow; GB24 + LR14 (Front-Mu points of GB and Liver) clear local inflammation; SP9 drains dampness; LI11 clears toxic heat; and BL19 regulates Gallbladder Back-Shu.",
                    "B": "❌ **Incorrect:** Spleen/Stomach harmonizing formula for simple indigestion and vomiting, omitting Gallbladder channel points.",
                    "C": "❌ **Incorrect:** Kidney Yang tonification formula; contraindicated in acute inflammatory Damp-Heat.",
                    "D": "❌ **Incorrect:** Exterior wind-heat Lung formula."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Western Medical Red Flag Recognition",
                "prompt": "Which constellation of clinical signs (Charcot's Triad) indicates acute ascending cholangitis requiring immediate emergency hospital transfer?",
                "options": [
                    "A. Occipital headache, clear rhinorrhea, and stiff neck.",
                    "B. Right upper quadrant pain, high spiking fever with shaking chills, and jaundice.",
                    "C. Left lower quadrant pain, chronic constipation, and afebrile state.",
                    "D. Epigastric hunger, dry mouth, and normal body temperature."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Classic signs of common cold / Wind-Cold.",
                    "B": "✅ **Correct (Charcot's Triad):** Right upper quadrant abdominal pain + high fever with rigors + jaundice constitutes Charcot's Triad for acute ascending cholangitis (bacterial infection of obstructed bile duct). If accompanied by hypotension and confusion (Reynolds' Pentad), it represents septic shock requiring urgent surgical/endoscopic decompression.",
                    "C": "❌ **Incorrect:** Suggests diverticulitis.",
                    "D": "❌ **Incorrect:** Stomach Yin deficiency."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Damp-Heat in Liver and Gallbladder with Biliary Colic (Gan Dan Shi Re, Dan Shi Tong)",
                "Obstruction of the Bile Duct by Damp-Heat and Phlegm-Stones"
            ],
            "treatment_principles": [
                "Clear Heat, Drain Dampness, and Purge Gallbladder Fire (清利肝胆湿热)",
                "Unblock the Gallbladder Collaterals and Arrest Acute Spasms (利胆通腑，化石止痛)"
            ],
            "cardinal_points": ["Dannangxue", "GB34", "GB24", "LR14", "SP9", "LI11", "BL19", "ST36"],
            "synergies": [
                "Empirical Biliary pair (Right Dannangxue + GB34 Yanglingquan) produces immediate spasmolysis of the sphincter of Oddi.",
                "Front-Mu clearing pair (GB24 Riyue + LR14 Qimen) eliminates local inflammation and hypochondriac pain.",
                "Damp-draining duo (SP9 Yinlingquan + LI11 Quchi) drives heat and moisture out through urine and bowels."
            ],
            "cautions": "SURGICAL RED FLAG: Murphy's sign and Charcot's triad must be closely monitored. If high fever (>38.5°C), peritoneal signs (rebound tenderness, rigid board-like abdomen), or septic confusion develop, immediately transfer patient to the nearest Emergency Department for ultrasound and intravenous antibiotic therapy."
        }
    },
    {
        "id": "CASE-027",
        "title": "Patient Intake: 33yo Female (Bloody Dysuria / Acute UTI - Xue Lin)",
        "category": "Urogenital & Internal Medicine",
        "patient": {
            "age": 33,
            "gender": "Female",
            "occupation": "Corporate Event Planner",
            "chief_complaint": "Sudden onset excruciating burning dysuria with urinary frequency every 15 minutes, suprapubic cramping, and visible dark red blood in urine for 24 hours.",
            "history": "High-stress job requiring prolonged standing and holding urine during multi-day conferences. Onset began acutely after a 14-hour workday. Voiding produces intense urethral scalding and only small dribbles of cloudy pinkish-red urine. No prior history of nephrolithiasis. In-clinic dipstick urinalysis shows: Large Blood (+++), Positive Leukocyte Esterase (+++), Positive Nitrites (++), Protein (+). Patient is afebrile (37.2°C).",
            "four_examinations": {
                "inspection": "Restless, distressed expression; flushed cheeks; Red tongue body with thick yellow slimy coating concentrated heavily on the posterior root (Kidney/Bladder zone).",
                "auscultation_olfaction": "Rapid breathing; groaning upon bladder spasms; urine sample has a sharp, foul, pungent odor.",
                "inquiry": "Excruciating urethral burning with sharp stabbing suprapubic pain before and after urination; sensation of incomplete voiding; dry mouth with bitter taste; irritability; constipation for 2 days.",
                "palpation": "Marked tenderness on deep palpation over CV3 (Zhongji) and suprapubic region; NO costovertebral angle (CVA) tenderness upon bilateral kidney punch percussion; radial pulse is Slippery (Hua) and Rapid (Shuo)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Diagnosis & Pattern Differentiation (Lin Syndrome)",
                "prompt": "What is the primary TCM pattern for acute burning dysuria with hematuria, suprapubic pain, thick yellow coating on the tongue root, and a slippery-rapid pulse?",
                "options": [
                    "A. Qi Lin (Qi Dysuria) due to Liver Qi Stagnation",
                    "B. Xue Lin (Blood Dysuria) due to Lower Jiao Damp-Heat Injuring Blood Vessels",
                    "C. Gao Lin (Chylous Dysuria) due to Kidney Deficiency",
                    "D. Shi Lin (Stone Dysuria) due to Urinary Calculus Obstruction without Infection"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Qi Lin presents with hypochondriac fullness and hesitant urination aggravated by anger/stress, without gross hematuria or purulent nitrites.",
                    "B": "✅ **Correct (Xue Lin / Blood Dysuria):** Pathogenic Damp-Heat descends and accumulates in the Bladder. The intense heat injures local capillary vessels, forcing blood to spill into the urine (Xue Lin). Characterized by scalding dysuria, hematuria, thick yellow tongue root coat, and a slippery-rapid pulse.",
                    "C": "❌ **Incorrect:** Gao Lin presents with milky, turbid, rice-water or fatty urine from Kidney failure to secure essence.",
                    "D": "❌ **Incorrect:** Shi Lin produces sudden agonizing loin-to-groin colic from physical stone movement with interrupted urinary stream, often without the systemic foul damp-heat coating."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Cardinal Point Prescription for Lower Jiao Damp-Heat",
                "prompt": "Which acupuncture prescription directly targets the Bladder Mu-Shu points, drains Damp-Heat, and stops hematuria?",
                "options": [
                    "A. BL28 (Pangguangshu), CV3 (Zhongji), SP9 (Yinlingquan), BL63 (Jinmen), SP10 (Xuehai), SP6 (Sanyinjiao)",
                    "B. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 (Mingmen), BL52 (Zhishi)",
                    "C. LU7 (Lieque), KI6 (Zhaohai), BL13 (Feishu), HT6 (Yinxi), LU9 (Taiyuan)",
                    "D. ST36 (Zusanli), CV12 (Zhongwan), SP3 (Taibai), BL20 (Pishu)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** BL28 + CV3 (Back-Shu and Front-Mu of Bladder) directly clear heat and unblock the lower waterways; SP9 (He-Sea) drains dampness; BL63 (Xi-Cleft of Bladder) rapidly relieves acute excruciating urethral pain and spasm; SP10 (Sea of Blood) cools blood and halts hematuria; and SP6 harmonizes the three lower Yin channels.",
                    "B": "❌ **Incorrect:** Kidney Yang tonification with Mingmen moxibustion is contraindicated in acute infectious Damp-Heat.",
                    "C": "❌ **Incorrect:** Lung/Kidney Yin tonic formula for respiratory disorders.",
                    "D": "❌ **Incorrect:** Middle jiao digestive tonification formula."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Clinical Assessment & Red Flag Protocol",
                "prompt": "Which physical examination finding is essential to confirm that an acute lower urinary tract infection has NOT ascended into acute pyelonephritis?",
                "options": [
                    "A. Absence of bilateral Costovertebral Angle (CVA) tenderness on gentle percussion.",
                    "B. Presence of abdominal guarding in the right iliac fossa.",
                    "C. Presence of swollen cervical lymph nodes.",
                    "D. Absence of knee reflex."
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** Percussing the 12th rib costovertebral angle (Murphy's kidney punch) tests for renal parenchymal inflammation. In uncomplicated lower UTI (cystitis), CVA tenderness is negative. If positive and accompanied by high fever, shaking rigors, nausea, and flank pain, it indicates acute pyelonephritis—an urgent medical condition requiring immediate antibiotic therapy.",
                    "B": "❌ **Incorrect:** McBurney's sign indicates appendicitis.",
                    "C": "❌ **Incorrect:** Upper respiratory / pharyngeal sign.",
                    "D": "❌ **Incorrect:** Neurological reflex testing."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Lower Jiao Damp-Heat Invading Urinary Bladder with Blood Vessel Injury (Pang Guang Shi Re, Xue Lin)",
                "Acute Hematuric Dysuria (Urinary Tract Infection)"
            ],
            "treatment_principles": [
                "Clear Heat, Drain Dampness, and Unblock the Lower Waterways (清热利湿，通淋止痛)",
                "Cool Blood and Arrest Hematuria (凉血止血)"
            ],
            "cardinal_points": ["BL28", "CV3", "SP9", "BL63", "SP10", "SP6"],
            "synergies": [
                "Bladder Mu-Shu pair (CV3 Zhongji + BL28 Pangguangshu) directly regulates bladder Qi transformation and expels pathogenic heat.",
                "Xi-Cleft analgesic strategy (BL63 Jinmen) arrests acute bladder spasms and scalding urethral pain.",
                "Blood-cooling astringent pair (SP10 Xuehai + SP6 Sanyinjiao) clears vascular heat and stops urinary bleeding."
            ],
            "cautions": "MEDICAL RED FLAG: Always perform CVA percussion. If patient develops high fever (>38.5°C), flank pain, shaking chills, or vomiting, immediate antibiotic referral for ascending pyelonephritis is mandatory. Ensure patient drinks copious warm water/cranberry tea and does not delay micturition."
        }
    },
    {
        "id": "CASE-028",
        "title": "Patient Intake: 63yo Male (Late-Stage Xiao Ke / Diabetic Retinopathy & Cataract)",
        "category": "Endocrine & Sensory",
        "patient": {
            "age": 63,
            "gender": "Male",
            "occupation": "Retired Postal Clerk",
            "chief_complaint": "Progressive visual blurring with dark floating spots, accompanied by severe thirst, urination 5 to 6 times per night, and lumbar weakness in a patient with 15-year type 2 diabetes.",
            "history": "Diagnosed with type 2 diabetes mellitus 15 years ago; currently on metformin and evening basal insulin. HbA1c is 8.6%. Recent ophthalmological evaluation reveals bilateral non-proliferative diabetic retinopathy and early posterior subcapsular cataracts. Patient complains of unquenchable thirst, frequent voluminous urination of turbid urine resembling fat, dry mouth, persistent tinnitus, and chronic lower back and knee soreness.",
            "four_examinations": {
                "inspection": "Emaciated body frame; dark, lusterless, sallow complexion with dark circles under the eyes; dull vacant eye gaze; Red tongue body with dry peeled center cracks (mirror tongue) and little or no coating.",
                "auscultation_olfaction": "Low feeble voice; slow quiet respiration.",
                "inquiry": "Constant thirst with massive water intake; urine is greasy/turbid; visual acuity deteriorating; floaters described as dark cobwebs; severe lumbar ache and weak rubbery knees; dry stools.",
                "palpation": "Weak lumbar musculature; stocking-distribution decreased sensation on bilateral feet (diabetic sensory neuropathy); radial pulse is Deep (Chen), Fine/Thready (Xi), and Weak in both Chi positions."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Diagnosis according to Three Jiao Xiao Ke Classification",
                "prompt": "What is the primary TCM pattern for this patient presenting with copious turbid urination, severe polydipsia, blurred vision, lumbar weakness, red peeled tongue, and deep thready weak pulse?",
                "options": [
                    "A. Upper Jiao Xiao Ke (Lung Heat Scorching Fluids)",
                    "B. Middle Jiao Xiao Ke (Stomach Heat Blazing)",
                    "C. Lower Jiao Xiao Ke with Liver and Kidney Yin Deficiency (Xia Xiao / Shen Yin Xu)",
                    "D. Pure Spleen Yang Deficiency with Cold Fluid Accumulation"
                ],
                "correct_index": 2,
                "explanations": {
                    "A": "❌ **Incorrect:** Upper Jiao Xiao Ke is characterized primarily by excessive thirst (drinking dozens of glasses of water) due to Lung heat, without copious fatty urine or diabetic retinopathy.",
                    "B": "❌ **Incorrect:** Middle Jiao Xiao Ke features voracious hunger (Xiao Gu Shan Ji) with rapid weight loss and severe constipation from Stomach Fire, rather than primary nocturia and visual decay.",
                    "C": "✅ **Correct (Lower Jiao Xiao Ke / Kidney & Liver Yin Deficiency):** Chronic Xiao Ke consumes the True Yin of the Kidneys and Liver. Kidney Yin deficiency fails to secure urine, creating turbid fatty urine (Xiao Ke). Liver Yin and Blood deficiency fails to nourish the eyes, causing diabetic retinopathy and cataracts (Nei Zhang). Characterized by lumbar soreness, red peeled tongue, and deep thready weak Chi pulse.",
                    "D": "❌ **Incorrect:** Spleen Yang deficiency produces watery diarrhea, edema, and cold limbs, not unquenchable thirst or dry peeled mirror tongue."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Comprehensive Point Prescription & Channel Strategy",
                "prompt": "Which point formulation addresses both the Lower Jiao Kidney Yin root and the visual degradation according to combined textbook standards?",
                "options": [
                    "A. KI3 (Taixi), BL23 (Shenshu), CV4 (Guanyuan), SP6 (Sanyinjiao), BL18 (Ganshu), GB37 (Guangming), BL1 (Jingming), ST36 (Zusanli)",
                    "B. LI11 (Quchi), ST44 (Neiting), GV14 (Dazhui), LI4 (Hegu), ST25 (Tianshu)",
                    "C. LU7 (Lieque), LI4 (Hegu), BL13 (Feishu), LU5 (Chize), LU10 (Yuji)",
                    "D. BL28 (Pangguangshu), CV3 (Zhongji), SP9 (Yinlingquan), BL63 (Jinmen)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** KI3 + BL23 + CV4 tonify Kidney Yin and consolidate the lower gates; SP6 harmonizes the three lower Yin; BL18 (Liver Back-Shu) and GB37 (Luo-Connecting of Gallbladder, renowned as the 'Bright Light' point) nourish Liver Blood and directly benefit the eyes; BL1 (Jingming) improves local retinal and ocular microcirculation; and ST36 supports postnatal Qi.",
                    "B": "❌ **Incorrect:** Vigorous heat-clearing formula for acute excess fire.",
                    "C": "❌ **Incorrect:** Formula for acute Lung wind-heat.",
                    "D": "❌ **Incorrect:** Formula for acute urinary tract damp-heat (Lin syndrome)."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Precision Needling Technique for BL1 (Jingming)",
                "prompt": "What is the mandatory clinical needling technique for BL1 (Jingming) to ensure patient safety and avoid orbital hematoma?",
                "options": [
                    "A. Ask the patient to keep their eyes open; insert rapidly 1.5 cun perpendicularly with vigorous twirling.",
                    "B. Ask patient to close eyes gently; push eyeball laterally with clean thumb/index finger; insert needle slowly 0.5-1.0 cun along the medial orbital wall without lifting, thrusting, or rotating.",
                    "C. Apply strong electroacupuncture across bilateral BL1 at 100 Hz for 30 minutes.",
                    "D. Puncture horizontally across the bridge of the nose."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect (High Risk):** Never needle with eyes open or use vigorous manipulation near the eyeball; this punctures the ophthalmic artery and causes retrobulbar hematoma (Deadman safety alert).",
                    "B": "✅ **Correct (CAM & Deadman Safety):** Patient closes eyes; acupuncturist gently pushes the eyeball laterally to create a safe needle path; puncture slowly and smoothly 0.5-1.0 cun along the orbital margin. Absolutely NO lifting, thrusting, or twirling. Upon needle withdrawal, apply firm sterile pressure with cotton ball for 1-2 minutes.",
                    "C": "❌ **Incorrect:** Electroacupuncture is strictly contraindicated at BL1 Jingming.",
                    "D": "❌ **Incorrect:** Does not stimulate the Jingming point."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Lower Jiao Wasting & Thirsting (Xia Xiao / 下消)",
                "Liver and Kidney Yin Deficiency with Essence Depletion and Ocular Malnutrition (Gan Shen Yin Xu, Nei Zhang)"
            ],
            "treatment_principles": [
                "Nourish Kidney and Liver Yin (滋补肝肾之阴)",
                "Secure Essence, Quench Thirst, and Brighten the Eyes (固精生津，清肝明目)"
            ],
            "cardinal_points": ["KI3", "BL23", "CV4", "SP6", "BL18", "GB37", "BL1", "ST36"],
            "synergies": [
                "Ocular Luo-Shu combination (BL18 Ganshu + GB37 Guangming) directly floods the optic nerve and retina with enriched Liver Blood.",
                "Lower Jiao Yin-Anchor (KI3 Taixi + CV4 Guanyuan) stops turbid urinary leakage and regenerates True Water.",
                "Three Leg Yin Bridge (SP6 Sanyinjiao) pulls excessive fire downward and nourishes body fluids."
            ],
            "cautions": "OCULAR SAFETY PROTOCOL: Needle BL1 Jingming with extreme caution. No manipulation; compress site for 2 minutes after removal. Diabetic patients have compromised peripheral microcirculation and delayed wound healing; inspect feet at every visit and avoid aggressive moxibustion on diabetic extremities to prevent burns and diabetic foot ulcers."
        }
    },
    {
        "id": "CASE-029",
        "title": "Patient Intake: 41yo Female (Uterine Bleeding / Spleen Not Controlling Blood - Beng Lou)",
        "category": "Gynecology & Obstetrics",
        "patient": {
            "age": 41,
            "gender": "Female",
            "occupation": "Middle School Counselor",
            "chief_complaint": "Persistent, continuous, pale watery uterine bleeding for 18 days accompanied by profound exhaustion, severe dizziness upon standing, and shortness of breath.",
            "history": "History of long hours of mental overwork, worry, and irregular meals. Menses historically heavy but would stop within 6 days. This cycle began as a heavy flood that failed to halt, continuing as a constant daily trickling (Lou) of thin pale blood without clots. Gynecological ultrasound is negative for fibroids, polyps, or endometrial hyperplasia. Complete blood count shows Hemoglobin 88 g/L (microcytic hypochromic anemia). Patient is pale, cold, and exhausted.",
            "four_examinations": {
                "inspection": "Ashen, lusterless, sallow facial complexion; pale conjunctiva, lips, and nailbeds; weak slumping posture; Pale and swollen tongue body with scalloped teeth marks and thin moist white coating.",
                "auscultation_olfaction": "Soft, feeble, breathy voice; frequent sighing; disinclined to speak due to shortness of breath.",
                "inquiry": "Constant trickling of pale watery blood without foul odor or dark clots; severe orthostatic lightheadedness; palpitations upon minor exertion; cold intolerance; poor appetite; loose watery stools; spontaneous sweating.",
                "palpation": "Soft, flaccid, non-tender lower abdomen; cool extremities to touch; radial pulse is Deficient (Xu), Soft/Soggy (Ru), and Thready (Xi)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Pattern Differentiation for Uterine Bleeding (Beng Lou)",
                "prompt": "What is the primary TCM pattern for prolonged pale thin uterine bleeding, sallow complexion, fatigue, poor appetite, pale tongue with teeth marks, and a weak thready pulse?",
                "options": [
                    "A. Blood Heat Invading Chong and Ren Channels",
                    "B. Spleen Failing to Control Blood (Pi Bu Tong Xue)",
                    "C. Blood Stasis Obstructing the Uterus (Han Ning Xue Yu)",
                    "D. Liver Fire Blazing Causing Reckless Blood Flow"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Blood Heat produces sudden profuse bright red or dark purple thick bleeding with clots, thirst, mental restlessness, red tongue with yellow coat, and rapid pulse.",
                    "B": "✅ **Correct (Spleen Not Controlling Blood):** Spleen Qi commands and holds the blood within the vessels (Tong Xue). Chronic worry and overwork exhaust Spleen Qi, which loses its astringent holding power, allowing blood to leak continuously from the Chong and Ren channels (Beng Lou). Characterized by pale thin blood, fatigue, teeth marks on a pale tongue, and a weak thready pulse.",
                    "C": "❌ **Incorrect:** Blood Stasis presents with sharp stabbing lower abdominal pain aggravated by pressure, dark purplish blood with large clots, and purple tongue with choppy pulse.",
                    "D": "❌ **Incorrect:** Liver Fire presents with wiry-rapid pulse, bitter taste, temporal headaches, and thick red blood."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Cardinal Point & Moxibustion Technique",
                "prompt": "Which acupuncture point and treatment modality is the renowned textbook emergency master method to stop chronic uterine bleeding from Spleen deficiency?",
                "options": [
                    "A. Bleeding the ear apex (Erjian) with a lancet.",
                    "B. Direct moxibustion (moxa cone or stick) on SP1 (Yinbai / 隐白).",
                    "C. Heavy reducing manipulation on LR3 (Taichong) and LI4 (Hegu).",
                    "D. Puncturing CV3 (Zhongji) deeply with electrical stimulation."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Erjian bleeding clears extreme excess heat, contraindicated in Qi-deficiency hemorrhage.",
                    "B": "✅ **Correct (Moxa on SP1 Yinbai):** SP1 (Jing-Well wood point of Spleen Taiyin) is the premier classical master point for uterine hemorrhage. Direct or stick moxibustion on SP1 strongly stimulates Spleen Qi, astringes vessels, elevates sunken Yang, and arrests uterine flooding and trickling (Beng Lou).",
                    "C": "❌ **Incorrect:** Strong reducing on Four Gates is a dispersing technique that would aggravate bleeding.",
                    "D": "❌ **Incorrect:** Deep needling at CV3 can injure an enlarged bladder or uterus, not indicated for chronic hemorrhage."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Comprehensive Supportive Point Formula",
                "prompt": "Which supporting point combination best tonifies Spleen Qi, lifts sunken Yang, and manages blood volume?",
                "options": [
                    "A. SP10 (Xuehai), SP6 (Sanyinjiao), BL20 (Pishu), CV6 (Qihai), GV20 (Baihui), ST36 (Zusanli)",
                    "B. LI11 (Quchi), ST44 (Neiting), GV14 (Dazhui), SP9 (Yinlingquan)",
                    "C. BL28 (Pangguangshu), CV3 (Zhongji), BL63 (Jinmen)",
                    "D. KI3 (Taixi), BL23 (Shenshu), CV4 (Guanyuan) without moxa"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** SP10 regulates the Sea of Blood; SP6 harmonizes the three leg Yin; BL20 directly tonifies Spleen Qi; CV6 (Sea of Qi) and ST36 boost postnatal Qi production; and GV20 (Baihui with moxa) raises sunken Yang Qi to halt downward leakage of blood.",
                    "B": "❌ **Incorrect:** Pure heat-clearing formula.",
                    "C": "❌ **Incorrect:** Formula for urinary tract infection.",
                    "D": "❌ **Incorrect:** Tonifies Kidney Yin, but lacks the specific Spleen blood-holding points."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Spleen Failing to Control Blood (Pi Bu Tong Xue / 脾不统血)",
                "Chong and Ren Channel Instability with Flooding and Trickling (Beng Lou / 崩漏)"
            ],
            "treatment_principles": [
                "Tonify Spleen Qi, Raise Sunken Yang, and Astringe Hemorrhage (健脾益气，摄血固冲)",
                "Nourish Qi and Blood to Restore Hemodynamic Stability (益气生血)"
            ],
            "cardinal_points": ["SP1", "SP10", "SP6", "BL20", "CV6", "GV20", "ST36"],
            "synergies": [
                "Classical Hemostatic Master (SP1 Yinbai with moxa) astringes bleeding and anchors Spleen Qi.",
                "Yang-Lifting duo (GV20 Baihui + CV6 Qihai) raises sunken Qi to halt downward pelvic flooding.",
                "Blood-Holding pair (BL20 Pishu + SP10 Xuehai) restores vessel integrity and splenic control over blood."
            ],
            "cautions": "HEMODYNAMIC RED FLAG: Severe acute uterine hemorrhage can cause hypovolemic shock. If patient presents with blood pressure <90/60 mmHg, heart rate >110 bpm, syncopal collapse, or hemoglobin <70 g/L, initiate emergency transport for intravenous fluid resuscitation and blood transfusion."
        }
    },
    {
        "id": "CASE-030",
        "title": "Patient Intake: 50yo Male (Involuntary Facial Hemispasm / Post-Bell's Palsy)",
        "category": "Neurological & Sensory",
        "patient": {
            "age": 50,
            "gender": "Male",
            "occupation": "Commercial Driver",
            "chief_complaint": "Involuntary, rhythmic, twitching spasms of the left eyelid and corner of the mouth, occurring multiple times an hour for 3 months following incomplete recovery from Bell's palsy.",
            "history": "Suffered acute idiopathic facial nerve paralysis (Bell's palsy) 4 months ago after driving long distances with the driver's side window open in cold rainy weather. The acute flaccidity resolved partially with oral corticosteroids and acupuncture, but over the last 12 weeks, abnormal involuntary spasms developed on the left side of the face. Spasms are triggered by talking, chewing, emotional tension, and exposure to air conditioning.",
            "four_examinations": {
                "inspection": "Left palpebral fissure narrows intermittently during spasm; corner of left mouth twitches and pulls laterally and upward; mild contracture of left nasolabial fold; Pale slightly swollen tongue body with thin white greasy coating.",
                "auscultation_olfaction": "Occasional speech hesitation and mild articulation slurring during active spasms; heavy sighing.",
                "inquiry": "Tightness, stiffness, and crawling sensation (formication) across left cheek and jaw; spasms worsen dramatically under fatigue or stress; difficulty reading due to left eyelid twitching; neck and shoulder tension.",
                "palpation": "Hypertonic, taut, irritable bands in the left zygomaticus major, orbicularis oculi, and masseter muscles; exquisite tenderness over left GB20 and Taiyang; radial pulse is Wiry (Xian) and Slippery (Hua)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Pathophysiology & TCM Pattern Identification",
                "prompt": "What is the primary TCM pattern for post-paralytic facial spasms characterized by involuntary twitching, localized stiffness, pale swollen tongue with greasy coat, and a wiry-slippery pulse?",
                "options": [
                    "A. Extreme Heat Generating Liver Wind",
                    "B. Wind-Phlegm and Blood Stasis Obstructing Facial Channels (Zhong Luo / Mian Ji)",
                    "C. Kidney Yang Deficiency with Cold Accumulation",
                    "D. Acute Exterior Wind-Cold Invading Taiyang"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Extreme Heat generating Wind produces high fevers, generalized convulsions, stiff neck, and deep red tongue.",
                    "B": "✅ **Correct (Wind-Phlegm Obstructing Facial Channels):** Incomplete recovery from Bell's palsy leaves residual pathogenic Wind and Phlegm lodged in the Yangming and Shaoyang channels of the face. Qi and Blood stasis in the collaterals causes malnutrition and hyperirritability of the facial sinews, producing involuntary spasms (Mian Ji). Characterized by local twitching, greasy coat, and a wiry-slippery pulse.",
                    "C": "❌ **Incorrect:** Kidney Yang deficiency presents with cold limbs, lumbago, pale profuse urine, and deep slow pulse.",
                    "D": "❌ **Incorrect:** Acute Wind-Cold invasion was the initial trigger 4 months ago, but the current chronic spasm represents channel sinew malnourishment and internal Wind-Phlegm."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Point Prescription & Local Needling Technique",
                "prompt": "Which acupuncture prescription and technique is most effective to relax spastic facial sinews without triggering further muscular contracture?",
                "options": [
                    "A. Deep perpendicular needling into the facial nerve trunk with continuous 50 Hz electroacupuncture.",
                    "B. Subcutaneous/transverse shallow insertion across local points: ST4 (Dicang) joined to ST6 (Jiache), Taiyang joined to GB1, GB20 (Fengchi), LI4 (Hegu), and LR3 (Taichong).",
                    "C. Direct moxibustion burns directly on the orbicularis oculi muscle belly.",
                    "D. Vigorous deep needle manipulation with strong electrical current on ST7 and SI18."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect (High Risk):** Aggressive electroacupuncture on spastic facial muscles triggers severe permanent contracture and synkinesis (nerve miswiring).",
                    "B": "✅ **Correct (Transverse Joined Needling & Four Gates):** Transverse (subcutaneous) through-and-through needling (Tou Xue) such as ST4 towards ST6 and Taiyang towards GB1 smooths channel Qi and relaxes sinews without irritating the facial nerve trunk. Distal points LR3 + LI4 (Four Gates) extinguish internal wind and unblock collaterals.",
                    "C": "❌ **Incorrect:** Direct scarring moxa on the eyelid causes severe skin burns and corneal injury.",
                    "D": "❌ **Incorrect:** Strong electrical current aggravates facial spasticity."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Clinical Contraindication in Facial Hemispasm",
                "prompt": "What therapeutic modality is specifically CONTRAINDICATED in the treatment of chronic facial hemispasm / post-paralytic synkinesis?",
                "options": [
                    "A. Gentle manual feather-touch acupressure along the jawline.",
                    "B. Strong, high-frequency electrical stimulation (Electroacupuncture) over the spastic facial muscles.",
                    "C. Application of warm compress to the preauricular area.",
                    "D. Distal needling on LI4 and LR3."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Gentle acupressure is safe and therapeutic.",
                    "B": "✅ **Correct (Electroacupuncture Contraindicated):** CARB-TCMPA and clinical consensus warn that strong electric stimulation over spastic facial muscles overexcites the facial nerve, promoting abnormal axonal branching (synkinesis) and worsening muscle spasticity. Treatment must rely on gentle, shallow, manual sedating technique.",
                    "C": "❌ **Incorrect:** Warm compress relaxes muscle tension and is beneficial.",
                    "D": "❌ **Incorrect:** Distal Four Gates needling is highly indicated."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Wind-Phlegm and Blood Stasis Obstructing Facial Channels (Zhong Luo, Mian Ji / 面肌痉挛)",
                "Sinew Malnutrition following Facial Paralysis (Bell's Palsy Sequelae)"
            ],
            "treatment_principles": [
                "Extinguish Internal Wind, Dissolve Phlegm, and Relax Facial Sinews (息风化痰，缓痉舒筋)",
                "Unblock Yangming and Shaoyang Channels, Regulate Qi and Blood (通经活络，调和气血)"
            ],
            "cardinal_points": ["ST4", "ST6", "Taiyang", "GB20", "LI4", "LR3", "SJ5"],
            "synergies": [
                "Joined Facial Sinew pair (ST4 Dicang directed subcutaneously towards ST6 Jiache) gently releases hypertonic zygomatic and buccinator muscles.",
                "Four Gates master combination (LI4 Hegu + LR3 Taichong) calms neuromuscular irritability and extinguishes channel wind.",
                "Occipital Wind-Clearing point (GB20 Fengchi) relieves cervical-facial nerve tension."
            ],
            "cautions": "ELECTROACUPUNCTURE CONTRAINDICATION: Absolutely avoid strong electrical stimulation on the face in hemispasm to prevent irreversible synkinesis. Use shallow subcutaneous needling. Advise patient to protect the face from cold drafts and manage psychological stress."
        }
    },
    {
        "id": "CASE-031",
        "title": "Patient Intake: 71yo Male (Chest Bi / Impending Coronary Infarction - Surgical Red Flag)",
        "category": "Cardiovascular Emergency & Red Flag",
        "patient": {
            "age": 71,
            "gender": "Male",
            "occupation": "Retired Heavy Crane Operator",
            "chief_complaint": "Sudden onset crushing retrosternal chest heaviness radiating down the inner left arm to the little finger, accompanied by nausea, cold profuse sweating, and shortness of breath for 40 minutes.",
            "history": "History of hypertension and hyperlipidemia for 20 years. Smoker (1 pack/day for 45 years). Previous episodes of exertional angina relieved within 5 minutes by sublingual nitroglycerin; however, today the pain began while watching television, is significantly more intense ('feels like an elephant standing on my chest'), and failed to resolve after taking two nitroglycerin tablets 15 minutes apart. Patient appears anxious with a sense of impending doom.",
            "four_examinations": {
                "inspection": "Ashen, grayish, deathly pale complexion; forehead and upper lip drenched in cold beads of sweat; cyanosis of lips and nailbeds; Dark Purple tongue body with prominent stasis macules on the margins and engorged sublingual veins.",
                "auscultation_olfaction": "Rapid labored panting respiration; weak groaning voice; inability to speak in full sentences.",
                "inquiry": "Excruciating substernal vise-like pressure; sharp radiating pain into left shoulder, medial arm, and jaw; extreme nausea and lightheadedness; feeling of impending doom.",
                "palpation": "Cold, clammy extremities; radial pulse is Knotted/Intermittent (Jie Dai), Thready (Xi), and Irregular with rate 104 bpm; blood pressure is 92/58 mmHg."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Medical Red Flag Diagnosis & Immediate Action",
                "prompt": "What is the mandatory immediate clinical action when a patient presents with crushing substernal chest pain >20 minutes unresponsive to nitroglycerin, cold diaphoresis, and cyanosis?",
                "options": [
                    "A. Administer a full 45-minute acupuncture treatment using heavy moxibustion on CV8.",
                    "B. Immediately call 911 (Emergency Medical Services); maintain patient supine, assist with emergency aspirin if indicated, and monitor airway/breathing/circulation.",
                    "C. Tell the patient to drive himself to his family physician's clinic tomorrow morning.",
                    "D. Perform vigorous tuina massage over the upper thoracic spine."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect (Fatal Delay):** Attempting an in-clinic acupuncture session during an acute evolving myocardial infarction delays critical coronary reperfusion therapy (catheterization/thrombolysis) and constitutes gross medical malpractice.",
                    "B": "✅ **Correct (Immediate 911 Activation):** Crushing retrosternal chest pain radiating to the left arm lasting >20 minutes, unresponsive to nitroglycerin, accompanied by diaphoresis and hypotension, is the hallmark of Acute Coronary Syndrome / Acute Myocardial Infarction (Chest Bi with Heart Yang Collapse). Acupuncturist must immediately dial 911, keep the patient resting comfortably, keep the airway patent, and prepare for CPR if cardiac arrest occurs.",
                    "C": "❌ **Incorrect (Fatal Delay):** Patient could experience ventricular fibrillation and cardiac arrest within minutes.",
                    "D": "❌ **Incorrect:** Thoracic spinal manipulation during acute coronary occlusion is dangerous and contraindicated."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Emergency First-Aid Acupressure while Awaiting EMS",
                "prompt": "While emergency medical transport is actively en route, which point may be stimulated with firm fingertip/fingernail pressure to stabilize cardiac rhythm and relieve chest oppression?",
                "options": [
                    "A. PC6 (Neiguan) and HT7 (Shenmen)",
                    "B. ST36 (Zusanli) and SP9 (Yinlingquan)",
                    "C. GB20 (Fengchi) and LI20 (Yingxiang)",
                    "D. BL25 (Dachangshu) and BL28 (Pangguangshu)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (PC6 + HT7 Acupressure):** Firm fingernail pressure on PC6 (Neiguan) stimulates vagal afferents to improve coronary perfusion and ease substernal oppression, while HT7 (Shenmen) soothes acute panic and Shen agitation while waiting for paramedics.",
                    "B": "❌ **Incorrect:** Digestive points with no direct acute coronary action.",
                    "C": "❌ **Incorrect:** Head/nasal points.",
                    "D": "❌ **Incorrect:** Lower bowel/bladder points."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. TCM Pattern & Post-Stabilization Cardinal Formula",
                "prompt": "What is the primary TCM pattern and textbook cardinal point formula for Chest Bi due to severe Heart Blood Stasis and Yang Qi collapse once hospitalized and medically stabilized?",
                "options": [
                    "A. Pattern: Heart Blood Stasis with Heart Yang Collapse; Formula: PC6 (Neiguan), PC4 (Ximen), HT7 (Shenmen), BL15 (Xinshu), BL17 (Geshu), CV17 (Danzhong)",
                    "B. Pattern: Lung Yin Deficiency; Formula: LU7, KI6, BL13, BL43",
                    "C. Pattern: Spleen Qi Deficiency; Formula: SP3, ST36, CV12, BL20",
                    "D. Pattern: Liver Fire Blazing; Formula: LR2, GB43, LI11, ST44"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** PC6 + PC4 (Xi-Cleft) directly resolve acute coronary blood stasis; HT7 calms the Heart Shen; BL15 + CV17 (Back-Shu and Front-Mu / Hui of Qi) restore thoracic Yang Qi; and BL17 (Hui of Blood) clears systemic stasis.",
                    "B": "❌ **Incorrect:** Respiratory formula.",
                    "C": "❌ **Incorrect:** Spleen digestive formula.",
                    "D": "❌ **Incorrect:** Liver fire formula."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Severe Heart Blood Stasis with Heart Yang Collapse (Xin Xue Yu Zu, Xin Yang Shuai Jie)",
                "True Heart Pain / Acute Coronary Syndrome (Zhen Xin Tong / 胸痹心痛)"
            ],
            "treatment_principles": [
                "EMERGENCY PROTOCOL: Immediate 911 Activation & Hospital Transfer",
                "Invigorate Heart Blood, Dissolve Stasis, and Warm Thoracic Yang (活血化瘀，通阳开痹)",
                "Stabilize Coronary Collaterals and Regulate Cardiac Shen (理气通络，安定心神)"
            ],
            "cardinal_points": ["PC6", "PC4", "HT7", "BL15", "BL17", "CV17", "SP10"],
            "synergies": [
                "Coronary Xi-Cleft Master pair (PC6 Neiguan + PC4 Ximen) provides potent opening of cardiac vessels and pain relief.",
                "Thoracic Qi-Blood meeting pair (CV17 Danzhong + BL17 Geshu) moves chest Qi to propel stagnant blood.",
                "Heart Mu-Shu resonance (CV14 Juque + BL15 Xinshu) restores cardiac rhythm."
            ],
            "cautions": "CARDIAC RED FLAG: Never attempt in-office acupuncture as primary therapy for acute evolving MI. Always record exact onset time, keep patient calm and resting supine, withhold food/fluids, confirm aspirin status, and monitor vital signs until EMS takes over."
        }
    },
    {
        "id": "CASE-032",
        "title": "Patient Intake: 29yo Male (Phlegm-Fire Agitating Shen / Manic Disorder - Kuang Zheng)",
        "category": "Psychiatric & Mental Health",
        "patient": {
            "age": 29,
            "gender": "Male",
            "occupation": "Nightclub Promoter",
            "chief_complaint": "Acute onset manic agitation, relentless rapid incoherent speech, sleeplessness for 5 consecutive nights, aggressive posturing, and uncontrolled shouting.",
            "history": "Escalated acutely after a 7-day binge of hard alcohol, stimulants, spicy food, and intense interpersonal disputes. Family reports patient has been singing from the rooftop, disrobing, pacing relentlessly, and claiming supernatural powers. Has not slept in over 100 hours. Refuses to sit still or eat normal meals. Brought to clinical attention by concerned family members.",
            "four_examinations": {
                "inspection": "Glaring bloodshot eyes; crimson flushed face; chaotic pacing with hyperactive gestures; violent muscular posturing; Red tongue body with thick, greasy, foul-smelling yellow coating.",
                "auscultation_olfaction": "Loud, coarse, incessant speech; rapid incoherent rambling; aggressive shouting; heavy panting respiration.",
                "inquiry": "Patient declares he is immune to sleep and possesses limitless energy; reports boiling heat in chest; thirst with desire for cold drinks; constipated for 4 days with foul-smelling dry stool; dark burning urine.",
                "palpation": "Warm hyperdynamic skin; forceful, Slippery (Hua), and Rapid (Shuo) radial pulse with fullness in both Guan and Cun positions."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Pattern Differentiation in Classical Psychiatric Disorders (Dian Kuang)",
                "prompt": "What is the classic TCM diagnosis for this presentation of acute manic agitation, incoherent shouting, zero sleep, red eyes, yellow slimy tongue coat, and a slippery-rapid pulse?",
                "options": [
                    "A. Dian Syndrome (Depressive / Phlegm-Damp Stagnation)",
                    "B. Kuang Syndrome (Manic Disorder due to Phlegm-Fire Agitating the Shen / Tan Huo Rao Xin)",
                    "C. Heart and Kidney Non-Interaction with Yin Deficiency",
                    "D. Spleen and Heart Blood Deficiency"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect (Dian Syndrome):** Dian is characterized by depressive withdrawal, mutism, stupor, incoherent whispering, and introversion caused by Phlegm-Damp misting the mind. Kuang is the manic Yang opposite (agitated, shouting, violent).",
                    "B": "✅ **Correct (Kuang Syndrome / Phlegm-Fire Agitating Shen):** Alcohol, emotional rage, and rich food generate intense toxic Fire that condenses bodily fluids into sticky Phlegm. Phlegm-Fire rushes upward to harass the Heart and cloud the Shen, producing manic agitation (Kuang Zheng), uninhibited speech, supercharged Yang energy, yellow greasy coat, and a slippery-rapid pulse.",
                    "C": "❌ **Incorrect:** Heart-Kidney disharmony produces insomnia, night sweats, lower back soreness, and a fine rapid pulse without manic violence.",
                    "D": "❌ **Incorrect:** Blood deficiency causes fatigue, sadness, poor memory, and pale tongue."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Point Prescription & Phlegm-Clearing Strategy",
                "prompt": "Which acupuncture prescription directly purges toxic Phlegm-Fire from the Heart and anchors the agitated Shen?",
                "options": [
                    "A. PC5 (Jianshi), ST40 (Fenglong), GV26 (Renzhong), GV14 (Dazhui), HT7 (Shenmen), SP1 (Yinbai), LI11 (Quchi)",
                    "B. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 (Mingmen), SP6 (Sanyinjiao) with moxa",
                    "C. LU7 (Lieque), KI6 (Zhaohai), BL13 (Feishu), HT6 (Yinxi), LU9 (Taiyuan)",
                    "D. CV12 (Zhongwan), ST36 (Zusanli), SP3 (Taibai), BL20 (Pishu)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** PC5 (Jing-River of Pericardium) is the renowned point to transform Phlegm in the Heart and open the orifices; ST40 (Luo of Stomach) dissolves systemic phlegm; GV26 and GV14 clear toxic Yang fire and pacify mania; HT7 sedates Heart Fire; SP1 (Sun Simiao Ghost point) anchors spastic Shen; and LI11 clears toxic heat.",
                    "B": "❌ **Incorrect:** Warming Kidney Yang with moxibustion is strictly contraindicated in blazing Phlegm-Fire.",
                    "C": "❌ **Incorrect:** Respiratory Yin tonic formula.",
                    "D": "❌ **Incorrect:** Digestive tonic formula."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Historical Role of Sun Simiao's Ghost Points (Gui Xue)",
                "prompt": "Which point in this prescription is one of the celebrated Thirteen Ghost Points (Gui Xue) described by Sun Simiao for acute mania and severe psychological disturbance?",
                "options": [
                    "A. SP1 (Yinbai - Ghost Eye / Gui Yan) and GV26 (Renzhong - Ghost Palace / Gui Gong)",
                    "B. ST36 (Zusanli) and SP9 (Yinlingquan)",
                    "C. BL23 (Shenshu) and KI3 (Taixi)",
                    "D. LU7 (Lieque) and KI6 (Zhaohai)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (Thirteen Ghost Points):** In the Tang Dynasty, Sun Simiao codified 13 Ghost Points (Gui Xue) specifically for sudden severe manic psychosis, delirium, and spiritual possession. GV26 (Gui Gong) and SP1 (Gui Yan) are two of the premier points utilized to shock the mind back to clarity and dispel turbid phlegm-fire.",
                    "B": "❌ **Incorrect:** Common lower leg points.",
                    "C": "❌ **Incorrect:** Kidney tonification points.",
                    "D": "❌ **Incorrect:** Confluent channel points."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Phlegm-Fire Agitating the Shen (Tan Huo Rao Xin / 痰火扰心)",
                "Manic Disorder / Bipolar Mania (Kuang Zheng / 狂证)"
            ],
            "treatment_principles": [
                "Purge Heart Fire, Dissolve Turbid Phlegm, and Open the Orifices (清心泻火，化痰开窍)",
                "Anchor the Spirit and Subdue Hyperactive Yang (镇心安神，平肝熄火)"
            ],
            "cardinal_points": ["PC5", "ST40", "GV26", "GV14", "HT7", "SP1", "LI11"],
            "synergies": [
                "Phlegm-Transforming Master pair (PC5 Jianshi + ST40 Fenglong) sweeps sticky phlegm out of the pericardial chest and restores cognitive lucidity.",
                "Ghost Point Anchor pair (GV26 Renzhong + SP1 Yinbai) calms psychiatric frenzy.",
                "Yang Fire Purging duo (GV14 Dazhui + LI11 Quchi) drains toxic systemic heat."
            ],
            "cautions": "PSYCHIATRIC EMERGENCY & SAFETY: Acute manic agitation requires a secure, calm environment with clinical assistants present to prevent harm to self or others. If patient displays active psychosis, severe dehydration, or violent delirium, emergency psychiatric evaluation and medical hospitalization are required."
        }
    },
    {
        "id": "CASE-033",
        "title": "Patient Intake: 4yo Male (Infantile Food Stagnation & Spleen Impairment - Gan Ji)",
        "category": "Pediatrics",
        "patient": {
            "age": 4,
            "gender": "Male",
            "occupation": "Preschooler",
            "chief_complaint": "Distended swollen abdomen like a drum, emaciated spindly limbs, capricious appetite with pica (eating dirt/chalk), restless night teeth grinding, and alternating bowel habits for 2 months.",
            "history": "History of improper weaning and excessive consumption of sugary snacks, pastries, cold milk, and fried chicken nuggets. Over the past 8 weeks, the child became irritable, developed a protruding tympanic belly, lost subcutaneous muscle mass in the limbs, and began grinding his teeth aggressively in sleep. Stool alternates between foul-smelling diarrhea with undigested milk curds and dry pellet constipation.",
            "four_examinations": {
                "inspection": "Spindly thin arms and legs with swollen protruding belly (potbelly); dry lusterless sallow face; dry brittle hair grouped in tufts; Pale tongue body with thick, greasy, patchy yellow curd-like coating.",
                "auscultation_olfaction": "Loud petulant crying; sour foul odor from the mouth (rotten breath); audible borborygmi.",
                "inquiry": "Night restlessness with teeth grinding; picky appetite with cravings for strange non-food substances (paper, chalk); excessive sweating on forehead during sleep; irritability.",
                "palpation": "Abdomen feels warm, tight, and distended with tympanic resonance; superficial venule at the index finger Qi Bar (气关) is thick, engorged, and dark purplish; pulse is Slippery (Hua) and Rapid (Shuo)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Pediatric Pattern Identification (Gan Ji)",
                "prompt": "What is the primary TCM diagnosis for a 4yo child presenting with a potbelly, emaciated limbs, foul breath, night teeth grinding, thick curd-like tongue coat, and a purple vein at the Qi bar?",
                "options": [
                    "A. Acute Exterior Wind-Cold Common Cold",
                    "B. Infantile Malnutrition due to Food Stagnation and Spleen Deficiency (Xiao Er Gan Ji / 疳积)",
                    "C. Kidney Yin Deficiency with Empty Fire",
                    "D. Acute Bacillary Dysentery"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Acute Wind-Cold presents with fever, chills, and clear runny nose.",
                    "B": "✅ **Correct (Xiao Er Gan Ji / Infantile Nutritional Stagnation):** Improper feeding and overindulgence in rich/cold foods impair the delicate Spleen and Stomach of young children. Food stagnates in the middle burner, fermenting into toxic heat and parasites, while Qi and Blood production collapses, producing emaciation with a protruding potbelly (Gan Ji).",
                    "C": "❌ **Incorrect:** Extremely rare in a 4yo child; does not produce food accumulation potbelly.",
                    "D": "❌ **Incorrect:** Dysentery features acute high fever, tenesmus, and constant bloody pus in stool."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Legendary Pediatric Extra Point Technique (Sifeng)",
                "prompt": "Which specialized pediatric extra acupuncture point is pricked to express a drop of clear yellowish fluid to resolve chronic food accumulation and malnutrition?",
                "options": [
                    "A. Sifeng (EX-UE10 / 四缝)",
                    "B. Shixuan (EX-UE11 / 十宣)",
                    "C. Taiyang (EX-HN5 / 太阳)",
                    "D. Yintang (EX-HN3 / 印堂)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (Sifeng Pricking):** Sifeng is located on the palmar surface of the 2nd to 5th fingers at the midpoint of the proximal interphalangeal creases. Pricking with a sterile lancet to express a drop of yellow translucent lymph/fluid directly harmonizes Spleen Qi, clears toxic food accumulation, stimulates digestion, and treats infantile Gan Ji.",
                    "B": "❌ **Incorrect:** Shixuan points are on the tips of the 10 fingers used for high-fever coma and resuscitation.",
                    "C": "❌ **Incorrect:** Taiyang is on the temple for migraines.",
                    "D": "❌ **Incorrect:** Yintang is between the eyebrows."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Pediatric Needle Retention Principle",
                "prompt": "What is the standard textbook needle retention principle when treating a 4-year-old child?",
                "options": [
                    "A. Retain needles for 45 minutes with heavy electrical stimulation.",
                    "B. Swift insertion and immediate withdrawal without needle retention (Fei Zhen / Non-retention technique).",
                    "C. Apply heavy direct scarring moxibustion on all points.",
                    "D. Insert needles deeply into the muscle belly and ask the child to walk around."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Children under 7 should not have needles retained for long periods, as it exhausts their delicate Qi and causes extreme panic.",
                    "B": "✅ **Correct (Swift Non-Retention Technique):** In pediatric acupuncture, Qi moves swiftly and responds immediately. The golden rule is rapid insertion, gentle stimulation for 1-2 seconds until Qi arrives (De Qi), and immediate needle withdrawal without retention (Fei Zhen).",
                    "C": "❌ **Incorrect:** Direct scarring moxa is strictly prohibited in pediatrics.",
                    "D": "❌ **Incorrect:** Dangerous."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Infantile Malnutrition and Food Stagnation Impairing Spleen (Xiao Er Gan Ji / 疳积)",
                "Middle Jiao Fermentative Obstruction with Qi-Blood Collapse"
            ],
            "treatment_principles": [
                "Dissolve Food Accumulation, Harmonize Spleen and Stomach (消积导滞，和胃健脾)",
                "Prick Sifeng to Drain Lymphatic Stagnation and Stimulate Growth (点刺四缝)"
            ],
            "cardinal_points": ["Sifeng", "ST36", "CV12", "BL20", "SP3"],
            "synergies": [
                "Pediatric Miracle point (Sifeng EX-UE10 pricking) immediately relieves abdominal distension and normalizes digestive secretions.",
                "Middle Burner Harmony pair (CV12 Zhongwan + ST36 Zusanli) restores gastric motility.",
                "Earth Root combination (BL20 Pishu + SP3 Taibai) rebuilds Spleen Qi absorption."
            ],
            "cautions": "PEDIATRIC SAFETY: Never retain needles in young children. Always use rapid insertion-withdrawal technique. Educate parents on strict dietary reform: eliminate dairy, cold sweets, and fruit juices; introduce warm, soft, easily digested congee."
        }
    },
    {
        "id": "CASE-034",
        "title": "Patient Intake: 38yo Female (Fibromyalgia & Chronic Fatigue - Spleen-Kidney Yang Deficiency)",
        "category": "Internal Medicine & Rheumatology",
        "patient": {
            "age": 38,
            "gender": "Female",
            "occupation": "Data Analyst",
            "chief_complaint": "Widespread bilateral musculoskeletal aching with 14 designated tender points, debilitating chronic fatigue, brain fog, and morning stiffness lasting over an hour for 18 months.",
            "history": "Diagnosed with fibromyalgia by rheumatologist after extensive workup excluding lupus and rheumatoid arthritis. Pain is described as a heavy, dull, diffuse ache throughout the neck, shoulders, hips, and knees, dramatically aggravated by cold damp weather and rainy seasons. Waking up in the morning feels like 'having been beaten all night'. Patient suffers from non-restorative sleep, brain fog, cold hands and feet, and loose unformed stools.",
            "four_examinations": {
                "inspection": "Sluggish tired demeanor; puffy swelling under eyes; pale sallow complexion; Pale, swollen, flabby tongue body with deep teeth marks along the lateral margins and a thick, moist, slippery white coating.",
                "auscultation_olfaction": "Quiet, breathy, low voice; frequent yawning and sighing.",
                "inquiry": "Body feels heavily weighed down like carrying wet blankets; joints stiff for 90 minutes every morning; hands and feet chronically cold; poor focus and memory; loose watery stools with undigested food; fatigue unrelieved by 10 hours of sleep.",
                "palpation": "Moderate palpation pressure over bilateral upper trapezius, second costochondral junctions, lateral epicondyles, and greater trochanters produces acute jump sign and tender grimacing; extremities feel cold to touch; radial pulse is Deep (Chen), Soft/Soggy (Ru), and Slow (Chi)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Comprehensive Bi Syndrome Pattern Identification",
                "prompt": "What is the primary TCM pattern for widespread musculoskeletal aching aggravated by rainy weather, heavy limbs, profound fatigue, cold intolerance, swollen pale scalloped tongue, and a deep soggy pulse?",
                "options": [
                    "A. Wind-Heat Bi Syndrome with Toxic Heat",
                    "B. Spleen and Kidney Yang Deficiency with Fixed Cold-Damp Bi Syndrome (Han Shi Bi)",
                    "C. Pure Liver Fire Blazing with Blood Stasis",
                    "D. Acute Exterior Wind-Cold Attack"
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Heat Bi presents with hot, swollen, red joints, fever, and a rapid pulse.",
                    "B": "✅ **Correct (Spleen-Kidney Yang Deficiency with Cold-Damp Bi):** Spleen Yang deficiency fails to transform fluids, generating chronic internal Dampness. Kidney Yang deficiency fails to warm the channels, allowing Cold and Damp to lodge deeply in the muscles, fascia, and joints (Fixed Bi / Zhuo Bi). Characterized by heavy aching aggravated by rain, cold limbs, swollen scalloped tongue, and deep soggy pulse.",
                    "C": "❌ **Incorrect:** Liver fire presents with wiry pulse, red eyes, and anger.",
                    "D": "❌ **Incorrect:** Acute attack does not account for 18 months of systemic fatigue and deep soggy pulse."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Point Prescription & Warming Modality",
                "prompt": "Which treatment strategy best dispels stubborn Cold-Damp from the sinews while tonifying the root Yang Qi?",
                "options": [
                    "A. Moxibustion on CV4 (Guanyuan) and GV14 (Dazhui), combined with SP9 (Yinlingquan), ST36 (Zusanli), BL20 (Pishu), BL23 (Shenshu), and GB34 (Yanglingquan)",
                    "B. Bloodletting on Shixuan and ear apex with ice packs on the joints",
                    "C. Strong sedating manipulation on LI11, ST44, and GV14 without moxibustion",
                    "D. Needling LU7 and KI6 alone with cool retention"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (Warming Moxa & Damp Resolution):** Moxibustion on CV4 and GV14 infuses Yang Qi into the Governor and Conception vessels to dispel deep cold; SP9 (He-Sea) is the premier point to resolve Dampness; ST36 + BL20 tonify Spleen Qi; BL23 tonifies Kidney Yang; and GB34 (Hui of Sinews) relaxes tight, tender, fibromyalgic muscular bands.",
                    "B": "❌ **Incorrect:** Bloodletting and ice packs severely damage Yang Qi and worsen Cold-Damp Bi.",
                    "C": "❌ **Incorrect:** Dispersing heat-clearing formula.",
                    "D": "❌ **Incorrect:** Insufficient to address deep structural Cold-Damp Bi."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. The Diagnostic Role of Tender Trigger Points (Ashi Points)",
                "prompt": "In treating fibromyalgia pain, how are local tender trigger points (Ashi Xue) integrated into the treatment plan according to Sun Simiao's teachings?",
                "options": [
                    "A. Ashi points should be strictly avoided in all chronic conditions.",
                    "B. Palpate the precise reactive tender knots and apply gentle local needle insertion or warm needle technique to unblock stagnant Qi and Blood locally.",
                    "C. Ashi points must only be treated on the non-painful side of the body.",
                    "D. Needles must be hammered forcefully into bone periosteum."
                ],
                "correct_index": 1,
                "explanations": {
                    "A": "❌ **Incorrect:** Ashi points are fundamental in pain management.",
                    "B": "✅ **Correct (Ashi Points Integration):** Sun Simiao stated 'Where there is pain, there is an acupuncture point' (Yi Tong Wei Shu). Combining root tonification with gentle, localized needling of active myofascial trigger points (Ashi points) disperses local focal ischemia, breaks muscular knots, and restores regional microcirculation.",
                    "C": "❌ **Incorrect:** Contralateral needling is an option for acute sprains, but bilateral Ashi palpation is standard in fibromyalgia.",
                    "D": "❌ **Incorrect:** Dangerous and traumatic."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Spleen and Kidney Yang Deficiency with Fixed Cold-Damp Bi (Pi Shen Yang Xu, Han Shi Bi / 寒湿痹)",
                "Latent Pathogen Accumulation in the Muscular Fascia (Fibromyalgia)"
            ],
            "treatment_principles": [
                "Warm and Supplement Spleen and Kidney Yang (温补脾肾之阳)",
                "Dispel Cold-Damp, Unblock Channels, and Relax Sinews (祛风除湿，散寒通痹，舒筋缓痛)"
            ],
            "cardinal_points": ["SP9", "ST36", "BL20", "BL23", "CV4", "GV14", "GB34"],
            "synergies": [
                "Yang-Igniting Moxa pair (CV4 Guanyuan + GV14 Dazhui) drives internal warming energy into the core.",
                "Damp-Expelling Earth pair (SP9 Yinlingquan + ST36 Zusanli) vaporizes interstitial fluid stagnation.",
                "Hui-Meeting Sinew master (GB34 Yanglingquan) softens chronic fibromyalgic myofascial trigger points."
            ],
            "cautions": "TREATMENT TOLERANCE WARNING: Fibromyalgia patients have central nervous system sensitization and hyperalgesia. Avoid overly aggressive manual manipulation or excessive needle retention during initial visits to prevent post-treatment flare-ups. Warm needle or indirect moxibustion is exceptionally well-tolerated."
        }
    },
    {
        "id": "CASE-035",
        "title": "Patient Intake: 46yo Male (Cervical Radiculopathy & Thoracic Outlet Syndrome - C6 Dermatome)",
        "category": "Musculoskeletal & Neurological",
        "patient": {
            "age": 46,
            "gender": "Male",
            "occupation": "Architectural Draftsman",
            "chief_complaint": "Sharp burning electric pain shooting from the lower cervical spine through the left shoulder down the lateral forearm into the thumb and index finger for 6 weeks.",
            "history": "Spends 8–10 hours daily bent over computer CAD screens with forward head posture. Pain began as a dull ache in the left neck and scapula, progressing to acute lancinating pain down the arm. Waking at night from tingling and numbness in the thumb and index finger (C6 dermatome). Positive Spurling's test (axial compression with neck extension and left lateral flexion reproduces radicular shooting pain down arm). Positive Adson's test (radial pulse diminishes upon neck extension and rotation toward affected side).",
            "four_examinations": {
                "inspection": "Guarded posture with head tilted slightly rightward to relieve left nerve root compression; atrophy of left thenar eminence; Dark Reddish-Purple tongue body with stasis petechiae along lateral borders.",
                "auscultation_olfaction": "Grimacing and holding left arm across chest; normal breath sounds.",
                "inquiry": "Sharp stabbing pain worse with neck extension and turning; numbness in thumb; drop in grip strength when holding tools; pain disrupts sleep when sleeping on left side.",
                "palpation": "Exquisite focal tenderness and radiation upon palpating left Hua Tuo Jia Ji points at C5-C7; hypertonic taut bands in anterior scalene and pectoralis minor; decreased left biceps reflex (2/4 vs 4/4 right); radial pulse is Wiry (Xian) and Choppy/Hesitant (Se)."
            }
        },
        "multiple_choice_questions": [
            {
                "question_id": "Q1",
                "title": "1. Channel & Bi Syndrome Differentiation",
                "prompt": "What is the primary TCM pattern for sharp shooting neck-to-hand pain along the Taiyang and Shaoyang/Yangming channels with numb C6 dermatome, purple tongue, and a wiry-choppy pulse?",
                "options": [
                    "A. Taiyang and Shaoyang Channel Obstruction with Blood Stasis and Nerve Root Compression (Bi Zheng / Jing Luo Yu Zu)",
                    "B. Spleen Qi Deficiency with Sinking of Central Qi",
                    "C. Exterior Wind-Cold Attack without Stasis",
                    "D. Kidney Yin Deficiency with Empty Fire only"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (Channel Obstruction with Blood Stasis):** Chronic forward head posture causes mechanical disc herniation and cervical canal stenosis. In TCM, postural strain leads to Qi and Blood stagnation in the Taiyang, Shaoyang, and Yangming channels. Stagnant blood compresses the nerve roots and collaterals, producing sharp radicular pain, C6 numbness, purple tongue with stasis dots, and a wiry-choppy pulse.",
                    "B": "❌ **Incorrect:** Spleen sinking produces organ prolapse and watery diarrhea, not radiculopathy.",
                    "C": "❌ **Incorrect:** Acute exterior wind does not produce C6 sensory deficit or purple tongue stasis dots.",
                    "D": "❌ **Incorrect:** Kidney Yin deficiency produces hollow lumbago and night sweats."
                }
            },
            {
                "question_id": "Q2",
                "title": "2. Precision Paravertebral Needle Prescription",
                "prompt": "Which specialized point prescription directly decompresses the cervical nerve roots and unblocks the affected arm meridians?",
                "options": [
                    "A. Hua Tuo Jia Ji (C5-C7 on left), SI14 (Jianwaishu), GB21 (Jianjing), LI11 (Quchi), LI4 (Hegu), SJ5 (Waiguan), LU7 (Lieque)",
                    "B. ST25 (Tianshu), ST37 (Shangjuxu), SP9 (Yinlingquan), CV12 (Zhongwan)",
                    "C. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 (Mingmen)",
                    "D. BL28 (Pangguangshu), CV3 (Zhongji), BL63 (Jinmen)"
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct:** Left Hua Tuo Jia Ji points at C5-C7 directly target the exiting dorsal rami and relieve disc/radicular edema; SI14 and GB21 relieve intense scapular tension; LI11 + LI4 + LU7 open the Yangming/Taiyin channels passing into the thumb and index finger; and SJ5 (Waiguan) opens the Yang Wei Mai.",
                    "B": "❌ **Incorrect:** Abdominal bowel formula.",
                    "C": "❌ **Incorrect:** Lumbar Kidney formula.",
                    "D": "❌ **Incorrect:** Bladder Lin formula."
                }
            },
            {
                "question_id": "Q3",
                "title": "3. Critical Anatomical Precaution for GB21 (Jianjing)",
                "prompt": "What life-threatening anatomical danger must be strictly prevented when needling GB21 (Jianjing) at the highest point of the shoulder trapezius?",
                "options": [
                    "A. Penetrating the apex of the lung causing traumatic pneumothorax.",
                    "B. Puncturing the femoral artery.",
                    "C. Damaging the peroneal nerve.",
                    "D. Piercing the orbital eyeball."
                ],
                "correct_index": 0,
                "explanations": {
                    "A": "✅ **Correct (Pneumothorax Warning for GB21):** GB21 is situated directly over the apex of the lung and dome of the pleura. Deep perpendicular downward insertion carries an extremely high risk of puncturing the apical pleura, resulting in traumatic pneumothorax. The needle MUST be directed horizontally or obliquely anterior/posterior along the trapezius muscle belly, NEVER perpendicularly inferiorly (Deadman & CARB-TCMPA safety mandatory warning).",
                    "B": "❌ **Incorrect:** Femoral artery is in the groin.",
                    "C": "❌ **Incorrect:** Peroneal nerve is at the knee/fibula.",
                    "D": "❌ **Incorrect:** Eyeball is in the head."
                }
            }
        ],
        "standard_diagnosis": {
            "patterns": [
                "Cervical Channel Obstruction with Blood Stasis and Nerve Root Compression (Jing Luo Yu Zu, Bi Zheng / 颈椎病)",
                "Taiyang, Shaoyang, and Yangming Collateral Stagnation (C6 Radiculopathy)"
            ],
            "treatment_principles": [
                "Unblock Cervical Collaterals, Invigorate Blood, and Stop Pain (通经活络，活血化瘀，通络止痛)",
                "Relax Hypertonic Scalene Musculature and Decompress Nerve Roots (舒筋缓痛)"
            ],
            "cardinal_points": ["Hua Tuo Jia Ji C5-C7", "SI14", "GB21", "LI11", "LI4", "SJ5", "LU7"],
            "synergies": [
                "Paravertebral Nerve Root Decompressor (Hua Tuo Jia Ji C5-C7) eliminates localized inflammatory edema around the exiting C6 root.",
                "Trapezius Tension Releaser (SI14 Jianwaishu + GB21 Jianjing) relieves shoulder girdle impingement.",
                "Hand Yangming Distal duo (LI11 Quchi + LI4 Hegu) drives channel Qi through the forearm into the thumb and index finger."
            ],
            "cautions": "PNEUMOTHORAX DANGER AT GB21: Never puncture GB21 perpendicularly or deeply. Always pinch the trapezius muscle and insert obliquely or transversely. Verify absence of progressive motor deficit; if patient develops rapidly advancing thenar weakness or loss of arm motor control, urgent neurosurgical MRI consultation is required."
        }
    }
]

print(f"Generated {len(NEW_CASES)} new cases successfully.")

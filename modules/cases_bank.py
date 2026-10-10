"""Pan-Canadian Examination Clinical Case Bank for Acupuncturists.

Curated cases conforming to the CARB-TCMPA (Canadian Alliance of Regulatory Bodies of
Traditional Chinese Medicine Practitioners and Acupuncturists) Examination Blueprint.
Contains 35 comprehensive patient cases:
- Musculoskeletal & Pain Syndromes (Bi Syndromes, Stiff Neck, Lumbago, Sciatica, Frozen Shoulder, Knee Bi, Tennis Elbow, Fibromyalgia, Cervical Radiculopathy)
- Neurological & Sensory (Bell's Palsy, Stroke Sequelae, Trigeminal Neuralgia, Insomnia, Vertigo, Facial Hemispasm)
- Internal Medicine (Asthma, Chronic Cough, GERD/Epigastric Pain, Daybreak Diarrhea, Diabetes Xiao Ke, Bronchiectasis, Cholecystitis, Geriatric Constipation)
- Urogenital & Nephrology (Acute Xue Lin / UTI with Hematuria, Kidney Yang/Yin Decline)
- Gynecology & Obstetrics (Dysmenorrhea, PMS Migraines, Morning Sickness, Menopause, Uterine Bleeding / Beng Lou)
- Psychiatric & Mental Health (Manic Disorder / Phlegm-Fire Agitating Shen)
- Pediatrics (Infantile Malnutrition / Gan Ji with Sifeng Pricking)
- Dermatology & External (Herpes Zoster, Urticaria)
- Clean Needle Technique, High-Risk Anatomy & Clinical Emergency Protocols (Needle Shock, Pneumothorax, Acute Coronary Syndrome Red Flag)
"""

from typing import List, Dict, Any

CLINICAL_CASES: List[Dict[str, Any]] = [   {   'category': 'Neurological & Gynecological',
        'id': 'CASE-001',
        'multiple_choice_questions': [   {   'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Liver Qi Stagnation transforming '
                                                                      'into Fire):** Temporal headaches travel along '
                                                                      'the Gallbladder channel (paired with Liver in '
                                                                      'the Wood element). Worsening with emotional '
                                                                      'stress, hypochondriac fullness, frequent '
                                                                      'sighing, red tongue margins, and a wiry/rapid '
                                                                      'pulse in the left Guan position are textbook '
                                                                      'hallmarks of constrained Liver Qi generating '
                                                                      'Fire (CAM & Maciocia).',
                                                                 'B': '❌ **Incorrect (Spleen and Stomach Qi '
                                                                      'Deficiency):** While the patient suffers from '
                                                                      'secondary postprandial distension and loose '
                                                                      'stools due to Wood overacting on Earth, pure '
                                                                      'Spleen deficiency produces dull frontal '
                                                                      'headaches relieved by eating, pale flabby '
                                                                      'tongue with teeth marks, and a weak (Ruo) '
                                                                      'pulse—not throbbing temporal pain with red '
                                                                      'sides and a wiry pulse.',
                                                                 'C': '❌ **Incorrect (Exterior Wind-Cold Invading '
                                                                      'Taiyang):** Exterior Wind-Cold produces '
                                                                      'occipital headaches with neck stiffness, acute '
                                                                      'chills, aversion to cold, and a floating-tight '
                                                                      '(Fu-Jin) pulse. This patient has a 3-year '
                                                                      'chronic history with clear internal heat signs.',
                                                                 'D': '❌ **Incorrect (Kidney Yin Deficiency with Empty '
                                                                      'Heat):** Presents with dull, hollow vertex or '
                                                                      'generalized head pain, night sweats, 5-palm '
                                                                      'heat, peeled red tongue with no coat, and a '
                                                                      'thready-rapid (Xi-Shuo) pulse, rather than '
                                                                      'forceful sighing and a wiry Guan pulse.'},
                                             'options': [   'A. Liver Qi Stagnation transforming into Fire',
                                                            'B. Spleen and Stomach Qi Deficiency',
                                                            'C. Exterior Wind-Cold Invading the Taiyang Channel',
                                                            'D. Kidney Yin Deficiency with Empty Heat'],
                                             'prompt': "Based on the patient's symptoms (throbbing temporal headaches, "
                                                       'irritability, red tongue sides, wiry pulse), which TCM pattern '
                                                       'is the primary diagnosis?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Identification (Diagnosis)'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** This is the premier formula to '
                                                                      'warm and tonify Kidney Yang and Mingmen Gate of '
                                                                      'Life (BL23, DU4, CV4, KI3). Applying warming '
                                                                      'tonification points on a patient with Liver '
                                                                      'Fire would severely aggravate heat and temporal '
                                                                      'headaches.',
                                                                 'B': '❌ **Incorrect:** This is a Lung Taiyin formula '
                                                                      'designed for exterior wind invasion, cough, and '
                                                                      'asthma (LU7, BL13, LU5). It does not address '
                                                                      'Liver Qi stagnation or Shaoyang migraines.',
                                                                 'C': '✅ **Correct:** This prescription synthesizes '
                                                                      'the classic textbook strategy:\n'
                                                                      '• LV3 (Yuan-Source) + LI4 (Yuan-Source) form '
                                                                      "the famous 'Four Gates' (Si Guan) to open the "
                                                                      '12 channels and smooth stagnant Qi.\n'
                                                                      '• GB20 and Taiyang clear local Shaoyang heat '
                                                                      'and extinguish wind to stop migraine pain.\n'
                                                                      '• SP6 nourishes Yin and Blood to anchor Liver '
                                                                      'Yang and harmonizes Spleen digestion.',
                                                                 'D': '❌ **Incorrect:** This is an Earth tonification '
                                                                      'formula for pure Spleen/Stomach deficiency. '
                                                                      'While supporting the middle jiao is helpful, '
                                                                      'completely omitting Liver points and local '
                                                                      "headache points fails to resolve the patient's "
                                                                      'chief complaint.'},
                                             'options': [   'A. BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), CV4 (Guanyuan '
                                                            '/ 关元), KI3 (Taixi / 太溪)',
                                                            'B. LU7 (Lieque / 列缺), LI4 (Hegu / 合谷), BL13 (Feishu / '
                                                            '肺俞), LU5 (Chize / 尺泽)',
                                                            'C. LV3 (Taichong / 太冲), LI4 (Hegu / 合谷), GB20 (Fengchi / '
                                                            '风池), Taiyang (太阳), SP6 (Sanyinjiao / 三阴交)',
                                                            'D. SP3 (Taibai / 太白), ST36 (Zusanli / 足三里), CV12 '
                                                            '(Zhongwan / 中脘), BL20 (Pishu / 脾俞)'],
                                             'prompt': 'Which acupuncture point prescription best addresses this '
                                                       "patient's root and branch according to combined textbook "
                                                       'principles?',
                                             'question_id': 'Q2',
                                             'title': '2. Point Prescription & Channel Strategy'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Moxibustion adds Yang heat and '
                                                                      'is contraindicated in acute Liver Fire blazing '
                                                                      'with red tongue margins and temporal throbbing.',
                                                                 'B': '✅ **Correct:** Reducing method disperses '
                                                                      'stagnant Qi and clears Liver Fire. Crucially, '
                                                                      'LI4 and SP6 are strongly contraindicated in '
                                                                      'pregnancy (Deadman & CAM), so pregnancy must be '
                                                                      'confirmed negative before vigorous downward '
                                                                      'stimulation. For GB20, pointing towards the '
                                                                      'opposite eye socket (or tip of the nose) '
                                                                      'ensures safe insertion avoiding the spinal '
                                                                      'canal and medulla oblongata.',
                                                                 'C': '❌ **Incorrect:** Dangerous technique! '
                                                                      'Puncturing GB20 deeply towards the foramen '
                                                                      'magnum risks penetrating the cranial cavity and '
                                                                      'medulla oblongata (Deadman anatomical warning).',
                                                                 'D': '❌ **Incorrect:** Tonification and warm needle '
                                                                      'technique (Wen Zhen) are indicated for '
                                                                      'Cold-Deficiency syndromes, not excess Fire/Heat '
                                                                      'patterns.'},
                                             'options': [   'A. Heavy indirect moxibustion on all points for 30 '
                                                            'minutes to disperse dampness.',
                                                            'B. Reducing (Sedating) method on LV3 and LI4; verify '
                                                            'pregnancy status before reducing LI4 and SP6; needle GB20 '
                                                            'obliquely towards the opposite eye socket.',
                                                            'C. Perpendicular deep insertion at GB20 pointing directly '
                                                            'towards the foramen magnum.',
                                                            'D. Strong tonification method with heating needles (Wen '
                                                            'Zhen) on all points.'],
                                             'prompt': 'What needle manipulation and clinical precautions are '
                                                       'indicated across textbooks for this patient?',
                                             'question_id': 'Q3',
                                             'title': '3. Needling Technique & Precautions'}],
        'patient': {   'age': 36,
                       'chief_complaint': 'Severe throbbing temporal headaches occurring 2-3 times per week, '
                                          'significantly worsening before menses.',
                       'four_examinations': {   'auscultation_olfaction': 'Speech is rapid and forceful; frequent deep '
                                                                          'sighs throughout consultation.',
                                                'inquiry': 'Sleep is restless with vivid dreaming. Appetite is '
                                                           'irregular, experiences epigastric distension after eating '
                                                           'during stressful days. Menses are irregular with dark '
                                                           'clots and breast distension.',
                                                'inspection': 'Tense facial expression. Tongue body is slightly red, '
                                                              'notably more red along the lateral edges/margins, with '
                                                              'a thin yellowish-white coating.',
                                                'palpation': 'Pulse is Wiry (Xian) and slightly Rapid (Shuo), '
                                                             'especially marked in the left Guan (Liver) position.'},
                       'gender': 'Female',
                       'history': 'Episodes started 3 years ago under intense work stress. Pain is sharp and '
                                  'distending, predominantly on the sides of the head and temples. Often accompanied '
                                  'by irritability, bitter taste in mouth in the morning, sighing, hypochondriac '
                                  'fullness, and alternating constipation and loose stools.',
                       'occupation': 'Corporate Attorney'},
        'standard_diagnosis': {   'cardinal_points': ['LV3', 'LI4', 'GB20', 'TAIYANG', 'GB34', 'SP6', 'ST36'],
                                  'cautions': 'Check if pregnancy is possible before applying strong reducing method '
                                              'on LI4 or SP6. Caution needling GB20 towards foramen magnum; needle '
                                              'obliquely toward opposite eye socket.',
                                  'patterns': [   'Liver Qi Stagnation transforming into Fire',
                                                  'Liver-Spleen Disharmony',
                                                  'Liver Qi Invading Spleen'],
                                  'synergies': [   'Four Gates (LV3 + LI4)',
                                                   'Shaoyang headache pair (GB20 + Taiyang)',
                                                   'Earth tonification (ST36 + SP6)'],
                                  'treatment_principles': [   'Soothe Liver Qi',
                                                              'Clear Liver Fire',
                                                              'Harmonize Liver and Spleen',
                                                              'Extinguish Wind and Alleviate Headache']},
        'title': 'Patient Intake: 36yo Female (Corporate Attorney)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-002',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Stabbing pain aggravated by '
                                                                      'pressure, purple tongue, and wiry pulse define '
                                                                      'Lumbar Blood Stasis (Qi Zhi Xue Yu), typically '
                                                                      'seen in acute traumatic disc herniation or '
                                                                      'sprain.',
                                                                 'B': '✅ **Correct:** Chronic dull aching improved by '
                                                                      'warmth/rest, cold sensation, frequent nocturia, '
                                                                      'pale wet tongue with teeth marks, and deep-weak '
                                                                      'pulse in the Chi positions are textbook '
                                                                      'hallmarks of Kidney Yang Deficiency failing to '
                                                                      'warm the lower burner (CAM, Deadman & '
                                                                      'Maciocia).',
                                                                 'C': '❌ **Incorrect:** Burning sensation, yellow '
                                                                      'urine, and yellow greasy coat indicate '
                                                                      'Damp-Heat in the lower jiao (Shi Re).',
                                                                 'D': '❌ **Incorrect:** Acute traumatic onset with '
                                                                      'guarding is characteristic of acute lumbar '
                                                                      'muscle sprain or Qi stagnation.'},
                                             'options': [   'A. Severe fixed stabbing pain worse with pressure, purple '
                                                            'tongue with petechiae, wiry pulse.',
                                                            'B. Dull aching pain alleviated by warmth and pressure, '
                                                            'copious clear nocturia, pale swollen tongue with wet '
                                                            'coat, and a deep-weak pulse.',
                                                            'C. Burning lumbar pain with yellow urine, yellow greasy '
                                                            'tongue coat, and a slippery-rapid pulse.',
                                                            'D. Acute onset after heavy lifting with localized muscle '
                                                            'guarding and inability to bend forward.'],
                                             'prompt': "Which key clinical signs confirm that this patient's low back "
                                                       'pain originates from Kidney Yang Deficiency rather than acute '
                                                       'Lumbar Blood Stasis?',
                                             'question_id': 'Q1',
                                             'title': '1. Differential Diagnosis & Pattern Confirmation'},
                                         {   'correct_index': 3,
                                             'explanations': {   'A': '❌ **Incorrect:** LI11, DU14, and ST44 disperse '
                                                                      'excess fire and external wind-heat. Applying '
                                                                      'fire-clearing points would further damage the '
                                                                      "patient's depleted Yang.",
                                                                 'B': '❌ **Incorrect:** Bleeding BL40 is used for '
                                                                      'acute excess blood stasis or summer-heat '
                                                                      'stroke, not chronic deficiency-cold.',
                                                                 'C': '❌ **Incorrect:** SJ5 + GB41 opens the Dai Mai '
                                                                      'for Shaoyang headache or damp-heat leukorrhea, '
                                                                      'not Kidney Yang low back pain.',
                                                                 'D': '✅ **Correct:** BL23 (Back-Shu of Kidney) and '
                                                                      'DU4 (Mingmen) directly replenish primal Yang '
                                                                      'and warm the lumbar spine. CV4 (Guanyuan) with '
                                                                      'moxibustion tonifies original Qi (Yuan Qi) and '
                                                                      'warms the lower dantian. KI3 tonifies Kidney '
                                                                      'source energy.'},
                                             'options': [   'A. Dispersing technique on LI11, DU14, ST44 with cupping '
                                                            'to drain toxic fire.',
                                                            'B. Fast prick-and-bleed technique on BL40 with plum '
                                                            'blossom needle to release heat.',
                                                            'C. Electro-acupuncture on SJ5 and GB41 with strong '
                                                            'continuous high-frequency stimulation.',
                                                            'D. Tonification needle technique with indirect '
                                                            'moxibustion (or warm needle Wen Zhen) on BL23 (Shenshu), '
                                                            'DU4 (Mingmen), CV4 (Guanyuan), and KI3 (Taixi).'],
                                             'prompt': 'Which treatment plan and modality combination provides the '
                                                       'definitive textbook standard for this patient?',
                                             'question_id': 'Q2',
                                             'title': '2. Point Selection & Therapeutic Modality'},
                                         {   'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** Safety protocol emphasized in '
                                                                      'CARB-TCMPA clean needle standards: elderly '
                                                                      'patients often have reduced thermal sensation; '
                                                                      'practitioner must place their own finger '
                                                                      'adjacent to the moxa zone to gauge heat and '
                                                                      'prevent accidental burn injury.',
                                                                 'B': '❌ **Incorrect:** Purposely causing scarring '
                                                                      'blisters (scarring moxa) over the spine is '
                                                                      'archaic and violates modern Canadian '
                                                                      'professional clinical safety and infection '
                                                                      'control standards.',
                                                                 'C': '❌ **Incorrect:** Moxibustion is strongly '
                                                                      'indicated for elderly Yang deficiency; it is '
                                                                      'not contraindicated, provided safety '
                                                                      'precautions are maintained.',
                                                                 'D': '❌ **Incorrect:** Ice contradicts the warming '
                                                                      'principle and causes pathological cold pathogen '
                                                                      'penetration.'},
                                             'options': [   'A. Monitor skin temperature closely because decreased '
                                                            'sensory perception in elderly or neuropathy patients '
                                                            'elevates the risk of severe thermal burns.',
                                                            'B. Induce scarring pustular moxa blisters directly over '
                                                            'the spinal cord to trigger immune defense.',
                                                            'C. Moxibustion is strictly prohibited on the lower back '
                                                            'in all patients over 60 years old.',
                                                            'D. Apply ice packs immediately after moxa to shock the '
                                                            'channel Qi into circulation.'],
                                             'prompt': 'When applying moxibustion to DU4 (Mingmen) and BL23 (Shenshu) '
                                                       'in an elderly patient with constitutional Yang deficiency, '
                                                       'what clinical guideline must be followed?',
                                             'question_id': 'Q3',
                                             'title': '3. Moxibustion Technique & Clinical Safety'}],
        'patient': {   'age': 62,
                       'chief_complaint': 'Deep aching and soreness in the lumbar region and knees for over 4 years, '
                                          'severely aggravated by cold weather and prolonged standing.',
                       'four_examinations': {   'auscultation_olfaction': 'Voice is soft, low, and lacks vitality; '
                                                                          'slow breathing pattern.',
                                                'inquiry': 'Lumbar ache is alleviated by resting in bed and warm '
                                                           'heating pads. Stools tend to be loose, occasionally '
                                                           'occurring early in the morning.',
                                                'inspection': 'Pale, slightly sallow complexion with dark circles '
                                                              'under the eyes. Tongue body is pale, swollen/enlarged '
                                                              'with scalloped teeth marks along the margins, covered '
                                                              'with a thin wet white coating.',
                                                'palpation': 'Lumbar musculature is cool to the touch without acute '
                                                             'muscle spasm or sharp focal trigger points. Pulse is '
                                                             'Deep (Chen), Weak (Ruo), and Slow (Chi), most markedly '
                                                             'deficient in both Chi (Kidney) positions.'},
                       'gender': 'Male',
                       'history': 'Gradual onset following decades of working outdoors in sub-zero Canadian '
                                  'temperatures. Reports cold sensation in the lower back like sitting on ice. Marked '
                                  'fatigue by late afternoon, frequent clear copious urination, and waking 3-4 times '
                                  'per night to urinate. Diminished libido and feeling chilled even when wearing '
                                  'multiple layers.',
                       'occupation': 'Retired Forest Ranger'},
        'standard_diagnosis': {   'cardinal_points': ['BL23', 'DU4', 'CV4', 'KI3', 'BL20', 'ST36', 'YAOYAN'],
                                  'cautions': 'Avoid strong reducing needle techniques. Moxibustion (direct ginger '
                                              'moxa or warm needle technique Wen Zhen) is strongly indicated. Ensure '
                                              'elderly patient skin is monitored to prevent moxa burns.',
                                  'patterns': [   'Kidney Yang Deficiency',
                                                  'Mingmen Fire Decline',
                                                  'Kidney and Spleen Yang Deficiency'],
                                  'synergies': [   'Back-Shu and Mingmen warming pair (BL23 + DU4)',
                                                   'Yuan-Source Kidney root (KI3)',
                                                   'Front-Mu and Sea of Qi synergy (CV4 with Moxa)',
                                                   'Post-heaven reinforcement (BL20 + ST36)'],
                                  'treatment_principles': [   'Warm and Tonify Kidney Yang',
                                                              'Supplement Mingmen Gate of Life',
                                                              'Strengthen Lumbar Spine and Knees',
                                                              'Warm the Channels and Dispel Cold']},
        'title': 'Patient Intake: 62yo Male (Retired Forest Ranger)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-003',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Foot Shaoyin and Taiyin '
                                                                      'traverse the medial aspect of the leg and '
                                                                      'abdomen, not the anterior-lateral shoulder.',
                                                                 'B': '❌ **Incorrect:** Hand Jueyin and Shaoyin travel '
                                                                      'along the anterior medial arm; tenderness at '
                                                                      'LI15 and TE14 indicates the lateral Yang '
                                                                      'aspect.',
                                                                 'C': '✅ **Correct:** LI15 is the premier point of '
                                                                      'Hand Yangming (Large Intestine) located in the '
                                                                      'anterior depression of the acromion. TE14 '
                                                                      'belongs to Hand Shaoyang (San Jiao) in the '
                                                                      'posterior depression. Together they govern the '
                                                                      'lateral and anterior shoulder mobility.',
                                                                 'D': '❌ **Incorrect:** Foot Taiyang runs down the '
                                                                      'back; Foot Jueyin traverses the medial lower '
                                                                      'limb.'},
                                             'options': [   'A. Foot Shaoyin (Kidney) and Foot Taiyin (Spleen)',
                                                            'B. Hand Jueyin (Pericardium) and Hand Shaoyin (Heart)',
                                                            'C. Hand Yangming (Large Intestine) and Hand Shaoyang (San '
                                                            'Jiao)',
                                                            'D. Foot Taiyang (Bladder) and Foot Jueyin (Liver)'],
                                             'prompt': 'Tenderness at LI15 (Jianyu) and TE14 (Jianliao) with severe '
                                                       'abduction restriction identifies obstruction along which '
                                                       'primary acupuncture channels?',
                                             'question_id': 'Q1',
                                             'title': '1. Channel Differentiation & Pattern Recognition'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** SP1 is for uterine bleeding '
                                                                      'and spleen deficiency dreaming.',
                                                                 'B': '✅ **Correct (ST38 Tiaokou):** ST38 is the '
                                                                      'classic distal master empirical point for '
                                                                      'shoulder pain and frozen shoulder. Puncturing '
                                                                      'through towards BL57 (Chengshan) combined with '
                                                                      'active shoulder movement (Dong Qi technique) '
                                                                      'dramatically unblocks channel Qi and restores '
                                                                      'elevation range of motion (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** KI1 treats loss of '
                                                                      'consciousness, hypertension, vertex headache, '
                                                                      'not frozen shoulder.',
                                                                 'D': '❌ **Incorrect:** BL67 is for turning breech '
                                                                      'babies.'},
                                             'options': [   'A. SP1 (Yinbai) with direct moxa cone to stop bleeding.',
                                                            'B. ST38 (Tiaokou) punctured perpendicularly 1.0 - 1.5 cun '
                                                            'towards BL57 while the patient actively moves the '
                                                            'affected shoulder.',
                                                            'C. KI1 (Yongquan) with deep perpendicular puncture to '
                                                            'ground ascending Yang.',
                                                            'D. BL67 (Zhiyin) with moxa to correct fetal malposition.'],
                                             'prompt': 'Which distal empirical acupuncture point on the lower limb is '
                                                       'famously indicated for shoulder stiffness and pain, and how '
                                                       'should it be needled?',
                                             'question_id': 'Q2',
                                             'title': '2. Distal Empirical Point Strategy'},
                                         {   'correct_index': 3,
                                             'explanations': {   'A': '❌ **Incorrect:** Femoral vessels are in the '
                                                                      'groin/femoral triangle (SP12/ST30 area).',
                                                                 'B': '❌ **Incorrect:** Common peroneal nerve is at '
                                                                      'the knee (GB34 area).',
                                                                 'C': '❌ **Incorrect:** Carotid and jugular are in the '
                                                                      'anterior neck (ST9 area).',
                                                                 'D': '✅ **Correct:** SI9 is located 1 cun superior to '
                                                                      'the posterior axillary fold. Deep anterior or '
                                                                      'medial insertion risks puncturing the axillary '
                                                                      'nerve, circumflex humeral vessels, and branches '
                                                                      'of the brachial plexus. Needle perpendicularly '
                                                                      '0.5-1.0 cun strictly within safe muscular '
                                                                      'margins (Deadman anatomical precautions).'},
                                             'options': [   'A. The femoral artery and femoral vein.',
                                                            'B. The common peroneal nerve in the fibular head.',
                                                            'C. The carotid artery and jugular vein.',
                                                            'D. The axillary nerve, posterior circumflex humeral '
                                                            'artery, and deep brachial plexus.'],
                                             'prompt': 'When treating the posterior aspect of the shoulder at SI9 '
                                                       '(Jianzhen), what anatomical structure must the acupuncturist '
                                                       'safeguard against damaging?',
                                             'question_id': 'Q3',
                                             'title': '3. Needling Safety & Anatomical Caution'}],
        'patient': {   'age': 54,
                       'chief_complaint': 'Severe stiffness and sharp pain in the right shoulder joint for 2 months, '
                                          'worsening over the last week. Inability to abduct arm beyond 60 degrees or '
                                          'reach behind her back to fasten her bra.',
                       'four_examinations': {   'auscultation_olfaction': 'Wincing and groaning when attempting '
                                                                          'passive shoulder abduction past 65°.',
                                                'inquiry': 'Reports heavy sensation in the right arm, numbness in the '
                                                           'fingers upon waking, and general aversion to cold weather.',
                                                'inspection': 'Restricted right shoulder mobility. Active abduction '
                                                              'limited to 60°, external rotation limited to 20°. '
                                                              'Muscular atrophy starting in supraspinatus. Tongue body '
                                                              'is pale with a thick white sticky coating.',
                                                'palpation': 'Marked tenderness upon palpation of LI15 (Jianyu), TE14 '
                                                             '(Jianliao), and Jianneiling (Extra). Subacromial space '
                                                             'is cold to touch. Pulse is Tight (Jin) and Wiry (Xian).'},
                       'gender': 'Female',
                       'history': 'Carried a heavy mailbag on her right shoulder daily in rain and wind. Initial mild '
                                  "ache gradually stiffened into a 'frozen' state. Pain is intensely aggravated when "
                                  'exposed to drafts or cold air conditioning, and somewhat eased by a hot shower. '
                                  'Night pain wakes her when turning onto the right side.',
                       'occupation': 'Post Office Mail Carrier'},
        'standard_diagnosis': {   'cardinal_points': [   'LI15',
                                                         'TE14',
                                                         'SI9',
                                                         'JIANNEILING',
                                                         'LI11',
                                                         'LI4',
                                                         'ST38',
                                                         'GB34'],
                                  'cautions': 'Moxibustion and warm needle technique (Wen Zhen) are highly effective '
                                              'here. Avoid deep perpendicular puncture at Jianzhen (SI9) to protect '
                                              'axillary neurovascular bundle.',
                                  'patterns': [   'Wind-Cold-Damp Bi Syndrome (Painful Bi)',
                                                  'Obstruction of Large Intestine and San Jiao Channels',
                                                  'Qi and Blood Stagnation in Shoulder'],
                                  'synergies': [   'Local Three Needles of Shoulder (LI15, TE14, Jianneiling)',
                                                   'Distal empirical master point ST38 (Tiaokou) with active '
                                                   'mobilization during needle manipulation',
                                                   'Hui-Meeting of Sinews (GB34)'],
                                  'treatment_principles': [   'Dispel Wind, Scatter Cold, Resolve Dampness',
                                                              'Unblock Channels and Collaterals',
                                                              'Alleviate Shoulder Pain',
                                                              'Harmonize Qi and Blood']},
        'title': 'Patient Intake: 54yo Female (Postal Carrier)'},
    {   'category': 'Neurological & Sensory',
        'id': 'CASE-004',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Central facial paralysis '
                                                                      '(stroke) spares the upper face (forehead '
                                                                      'wrinkling and eye closure are preserved) '
                                                                      'because upper facial muscles have bilateral '
                                                                      'cortical innervation. This patient cannot close '
                                                                      'his eye or wrinkle his forehead, which confirms '
                                                                      "lower motor neuron peripheral Bell's Palsy.",
                                                                 'B': '✅ **Correct:** Sudden onset following cold '
                                                                      "exposure, inability to close the eye (Bell's "
                                                                      'phenomenon), facial droop, thin white coat, and '
                                                                      'floating-tight pulse are textbook indicators of '
                                                                      'acute exterior Wind-Cold invading the Yangming '
                                                                      'and Shaoyang channels of the face (CAM & '
                                                                      'Deadman).',
                                                                 'C': '❌ **Incorrect:** Liver Yang Rising presents '
                                                                      'with severe vertigo, red tongue, wiry-rapid '
                                                                      'pulse, not isolated flaccid peripheral facial '
                                                                      'nerve palsy after driving in cold wind.',
                                                                 'D': '❌ **Incorrect:** Damp-heat presents with greasy '
                                                                      'yellow tongue coat, slippery pulse, and '
                                                                      'constitutional heat signs.'},
                                             'options': [   'A. Wind-Stroke (Zhong Feng) involving Central Facial '
                                                            'Paralysis from cerebral infarction',
                                                            'B. Exterior Wind-Cold Invading the Facial Yangming and '
                                                            "Shaoyang Channels (Peripheral Facial Paralysis / Bell's "
                                                            'Palsy)',
                                                            'C. Liver Yang Rising transforming into Internal Wind',
                                                            'D. Spleen and Stomach Damp-Heat obstructing facial '
                                                            'muscles'],
                                             'prompt': 'Based on the acute onset after cold draft exposure, inability '
                                                       'to close the eye, pale tongue with thin white coat, and '
                                                       'floating-tight pulse, what is the primary diagnosis?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation & Stage Assessment'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** This warms Kidney Yang, '
                                                                      'irrelevant to facial nerve revival.',
                                                                 'B': '❌ **Incorrect:** This is a Lung phlegm/cough '
                                                                      'formula.',
                                                                 'C': '✅ **Correct:** ST4 transfixed subcutaneously '
                                                                      'towards ST6 joins the corners of the mouth and '
                                                                      'jaw to restore orbicularis oris and buccinator '
                                                                      'function. GB14 to Yuyao raises the drooping '
                                                                      'brow. TE17 (Yifeng) unblocks the facial nerve '
                                                                      'trunk as it exits the stylomastoid foramen. LI4 '
                                                                      "is the classic Gao Wu command point: 'The Face "
                                                                      "and Mouth look to Hegu' (Mian kou hegu shou).",
                                                                 'D': '❌ **Incorrect:** Bleeding blood heat points is '
                                                                      'inappropriate for acute Wind-Cold nerve '
                                                                      'paresis.'},
                                             'options': [   'A. BL23 (Shenshu), DU4 (Mingmen), KI3 (Taixi) with heavy '
                                                            'moxibustion',
                                                            'B. LU5 (Chize), LU7 (Lieque), BL13 (Feishu) with '
                                                            'perpendicular deep puncture',
                                                            'C. ST4 (Dicang) transfixed towards ST6 (Jiache), GB14 '
                                                            '(Yangbai) transfixed towards Yuyao, TE17 (Yifeng), and '
                                                            'distal LI4 (Hegu)',
                                                            'D. SP10 (Xuehai), BL40 (Weizhong), LR2 (Xingjian) with '
                                                            'bleeding method'],
                                             'prompt': 'Which acupuncture point prescription and classic needling '
                                                       'technique is the gold standard for acute facial paralysis?',
                                             'question_id': 'Q2',
                                             'title': '2. Point Prescription & Transfixion Needling (Tou Zhen)'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Over-stimulating paralyzed '
                                                                      'muscles with heavy electro-acupuncture in the '
                                                                      'acute stage causes facial muscle contracture, '
                                                                      'spasms, and permanent aberrant re-innervation '
                                                                      '(synkinesis / crocodile tears).',
                                                                 'B': '❌ **Incorrect:** Distal points (LI4, SJ5) '
                                                                      'should be stimulated vigorously to expel '
                                                                      'exterior wind without fatiguing facial muscles.',
                                                                 'C': '✅ **Correct:** In the acute stage (days 1-7), '
                                                                      'gentle superficial needling prevents nerve '
                                                                      'exhaustion. Because the patient cannot blink, '
                                                                      'the cornea is vulnerable to desiccation, '
                                                                      'ulceration, and exposure keratitis. '
                                                                      'Recommending eye drops and an eye shield is an '
                                                                      'essential CARB-TCMPA safety standard.',
                                                                 'D': '❌ **Incorrect:** Deep aggressive puncture into '
                                                                      'the parotid gland can damage the facial nerve '
                                                                      'branches and parotid structures.'},
                                             'options': [   'A. Apply strong aggressive high-voltage '
                                                            'electro-acupuncture for 60 minutes to force the muscles '
                                                            'into contraction.',
                                                            'B. Strictly avoid needling distal points on the limbs.',
                                                            'C. Apply gentle superficial needling locally to prevent '
                                                            'secondary facial spasm or synkinesis, and instruct '
                                                            'patient on eye protection (lubricating eye drops/patch) '
                                                            'to prevent exposure keratitis.',
                                                            'D. Perform deep perpendicular punctures into the parotid '
                                                            'gland to stimulate the deep facial nerve trunk.'],
                                             'prompt': 'What critical clinical precaution must the acupuncturist '
                                                       "follow during the acute first week of Bell's Palsy?",
                                             'question_id': 'Q3',
                                             'title': '3. Needling Intensity & Corneal Safety Precaution'}],
        'patient': {   'age': 42,
                       'chief_complaint': 'Sudden onset right-sided facial weakness upon waking, inability to close '
                                          'right eye, water leaking from right mouth corner when drinking.',
                       'four_examinations': {   'auscultation_olfaction': 'Speech is slightly slurred due to impaired '
                                                                          'lip seal; no dysphasia.',
                                                'inquiry': 'Reports numbness and heavy sensation in right cheek; '
                                                           'aversion to cold wind; mild soreness around right mastoid '
                                                           'process.',
                                                'inspection': 'Asymmetrical face: flattened right nasolabial fold, '
                                                              'sagging right mouth angle, incomplete right eye closure '
                                                              "(Bell's sign: eyeball turns upward and outward when "
                                                              'attempting closure). Tongue body is pale with a thin '
                                                              'white coating.',
                                                'palpation': 'Loss of muscle tone in right zygomaticus, orbicularis '
                                                             'oculi, and frontalis muscles. Pulse is Floating and '
                                                             'Tight (Fu-Jin).'},
                       'gender': 'Male',
                       'history': 'Drove his work truck for 2 hours in sub-zero Canadian winter temperatures with the '
                                  "driver's window cracked open yesterday. Woke up this morning unable to wrinkle his "
                                  'forehead on the right side or smile. Food gets trapped between his right cheek and '
                                  'gums. Mild retroauricular soreness behind right ear.',
                       'occupation': 'Carpenter'},
        'standard_diagnosis': {   'cardinal_points': ['ST4', 'ST6', 'GB14', 'TAIYANG', 'LI4', 'TE17', 'SJ5'],
                                  'cautions': 'During acute stage (days 1-7), apply gentle superficial needling; avoid '
                                              'vigorous high-frequency electroacupuncture which can provoke permanent '
                                              'facial synkinesis or spasm. Advise patient to wear eye patch and use '
                                              'lubricating drops to prevent corneal exposure keratitis.',
                                  'patterns': [   'Exterior Wind-Cold Invading Yangming and Shaoyang Channels of Face',
                                                  'Wind-Cold Facial Paralysis (Mian Tan)'],
                                  'synergies': [   'Transfixion needling (Tou Zhen) pair (ST4 toward ST6)',
                                                   'Distal Yangming command master (LI4)',
                                                   'Local channel opener behind ear (TE17 Yifeng)'],
                                  'treatment_principles': [   'Dispel Wind and Scatter Cold',
                                                              'Unblock Facial Yangming and Shaoyang Channels',
                                                              'Regulate Qi and Blood',
                                                              'Nourish Tendons and Restore Movement']},
        'title': 'Patient Intake: 42yo Male (Carpenter)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-005',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Foot Jueyin and Shaoyin travel '
                                                                      'up the medial thigh/leg, not the posterolateral '
                                                                      'aspect.',
                                                                 'B': '❌ **Incorrect:** Foot Taiyin and Yangming '
                                                                      'travel anteriorly along the shin and anterior '
                                                                      'thigh.',
                                                                 'C': '✅ **Correct:** Foot Taiyang (Bladder) travels '
                                                                      'down the posterior thigh to the popliteal '
                                                                      'fossa, calf, and 5th toe (S1 nerve root). Foot '
                                                                      'Shaoyang (Gallbladder) travels down the lateral '
                                                                      'thigh, fibula, and lateral malleolus (L5 nerve '
                                                                      'root). Sciatica typically compresses L5 and S1 '
                                                                      'nerve roots.',
                                                                 'D': '❌ **Incorrect:** These are upper extremity '
                                                                      'channels.'},
                                             'options': [   'A. Foot Jueyin (Liver) and Foot Shaoyin (Kidney) - L2/L3 '
                                                            'dermatomes',
                                                            'B. Foot Taiyin (Spleen) and Foot Yangming (Stomach) - '
                                                            'L3/L4 dermatomes',
                                                            'C. Foot Taiyang (Bladder) and Foot Shaoyang (Gallbladder) '
                                                            '- L5/S1 dermatomes',
                                                            'D. Hand Taiyang (Small Intestine) and Hand Yangming '
                                                            '(Large Intestine) - C6/C7 dermatomes'],
                                             'prompt': 'Pain radiating down the posterior-lateral thigh to the lateral '
                                                       'malleolus and 5th toe maps directly to which acupuncture '
                                                       'channels and neurological dermatome?',
                                             'question_id': 'Q1',
                                             'title': '1. Channel Differentiation & Neurological Alignment'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** ST36 is the command point for '
                                                                      'the abdomen, not the back.',
                                                                 'B': '✅ **Correct (BL40 Weizhong):** The classic Song '
                                                                      "of the Four Command Points declares: 'The "
                                                                      "Lumbar and Back seek Weizhong' (Yao bei "
                                                                      'weizhong qiu). For acute fixed traumatic pain '
                                                                      'with dusky tongue and purple macules (Blood '
                                                                      'Stasis), pricking superficial engorged venules '
                                                                      'at BL40 to drain dark stagnant blood produces '
                                                                      'immediate decompression of channel pressure '
                                                                      '(Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** GB34 is for sinews; bleeding '
                                                                      'BL40 is the primary command strategy.',
                                                                 'D': '❌ **Incorrect:** KI1 is for grounding rising '
                                                                      'fire/fainting.'},
                                             'options': [   'A. ST36 (Zusanli) tonified with moxa',
                                                            'B. BL40 (Weizhong) bled with a lancet or three-edged '
                                                            'needle to express dark purple blood',
                                                            'C. GB34 (Yanglingquan) punctured with hot needle '
                                                            'technique',
                                                            'D. KI1 (Yongquan) stimulated with direct moxibustion'],
                                             'prompt': 'Which point is the Lower He-Sea of the Bladder and the premier '
                                                       'command point for the lumbar region, and what special method '
                                                       'is used for acute blood stasis?',
                                             'question_id': 'Q2',
                                             'title': '2. Lower He-Sea Command Point Strategy'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Radicular pain past the knee '
                                                                      'is typical of sciatica and can be managed '
                                                                      'conservatively.',
                                                                 'B': "❌ **Incorrect:** Pain on coughing (Dejerine's "
                                                                      'sign) indicates dural irritation from disc '
                                                                      'pressure; it is common in disc herniations.',
                                                                 'C': '✅ **Correct (Cauda Equina Syndrome Red Flag):** '
                                                                      'Compression of the cauda equina roots causes '
                                                                      'progressive bilateral neurological deficits, '
                                                                      'saddle numbness (perineal/perianal loss of '
                                                                      'sensation), and urinary retention or fecal '
                                                                      'incontinence. This is a neurosurgical emergency '
                                                                      'requiring MRI and surgical decompression within '
                                                                      '24-48 hours to prevent permanent paraplegia and '
                                                                      'permanent loss of sphincter control (CARB-TCMPA '
                                                                      'safety guidelines).',
                                                                 'D': '❌ **Incorrect:** Mild coldness is common in Qi '
                                                                      'and Blood deficiency or stagnation.'},
                                             'options': [   'A. Pain radiating past the knee.',
                                                            'B. Pain worsening upon coughing.',
                                                            'C. Sudden onset of bilateral lower extremity weakness '
                                                            'accompanied by saddle anesthesia and loss of bowel or '
                                                            'bladder control (Cauda Equina Syndrome).',
                                                            'D. Feeling cool sensation in the toes.'],
                                             'prompt': 'What emergent clinical presentation in a patient with severe '
                                                       'sciatica warrants immediate emergency medical referral (Red '
                                                       'Flag)?',
                                             'question_id': 'Q3',
                                             'title': '3. Red Flag Referral & Needle Depth at GB30'}],
        'patient': {   'age': 48,
                       'chief_complaint': 'Excruciating sharp shooting and burning pain radiating from right gluteal '
                                          'region down the posterolateral thigh to the calf and 5th toe.',
                       'four_examinations': {   'auscultation_olfaction': 'Labored breathing during transitions from '
                                                                          'sitting to standing due to acute pain.',
                                                'inquiry': 'Cannot find a comfortable sleeping position. Pain feels '
                                                           'like a tight band or electric wire pulling from the hip to '
                                                           'the foot.',
                                                'inspection': 'Antalgic list (leaning trunk away from the affected '
                                                              'right side to relieve nerve root compression). Tongue '
                                                              'body is dusky purple with distinct purplish stasis '
                                                              'macules on the margins, thin white coat.',
                                                'palpation': 'Marked tenderness upon palpating right Huantiao (GB30) '
                                                             'and Zhibian (BL54). Sensation to light touch diminished '
                                                             'along lateral foot (S1 dermatome). Pulse is Wiry (Xian) '
                                                             'and Choppy/Hesitant (Se).'},
                       'gender': 'Female',
                       'history': "Felt a sharp 'pop' in her lower back 5 days ago while lifting a 40 lb crate. Pain "
                                  'radiates continuously down the right leg, exacerbated by coughing, sneezing, and '
                                  'prolonged sitting. Right calf feels heavy and numb. Straight Leg Raise (SLR / '
                                  "Lasegue's test) is positive on the right at 35 degrees.",
                       'occupation': 'Warehouse Inventory Manager'},
        'standard_diagnosis': {   'cardinal_points': ['GB30', 'BL40', 'BL54', 'GB34', 'BL60', 'ASHIPOI'],
                                  'cautions': 'Needling GB30 requires deep insertion (2.0-3.0 cun) to reach piriformis '
                                              'depth and elicit radiating Deqi to the foot, but avoid violent repeated '
                                              'piston manipulation to prevent sciatic nerve trunk intraneural '
                                              'hematoma. Screen for cauda equina syndrome red flags (saddle '
                                              'anesthesia, bowel/bladder incontinence).',
                                  'patterns': [   'Taiyang and Shaoyang Channel Obstruction with Blood Stasis',
                                                  'Lumbar Disc Herniation / Sciatica (Bi Zheng)'],
                                  'synergies': [   'Major gluteal sciatic motor pair (GB30 + BL54)',
                                                   'Lower He-Sea Lumbar command point (BL40 Weizhong)',
                                                   'Hui-Meeting point of Sinews (GB34)',
                                                   'Distal Taiyang conductor (BL60)'],
                                  'treatment_principles': [   'Activate Blood and Dissolve Stasis',
                                                              'Unblock Taiyang and Shaoyang Channels',
                                                              'Alleviate Sciatic Pain and Relax Tendons',
                                                              'Harmonize Collaterals']},
        'title': 'Patient Intake: 48yo Female (Warehouse Manager)'},
    {   'category': 'Gynecology & Obstetrics',
        'id': 'CASE-006',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Deficiency presents with dull, '
                                                                      'lingering ache occurring towards the end of '
                                                                      'menses, relieved by gentle pressure, with pale '
                                                                      'watery blood and pale tongue.',
                                                                 'B': '✅ **Correct:** Cold causes contraction and '
                                                                      "stagnation ('Cold coagulates and congeals "
                                                                      "blood'). Sharp stabbing pain relieved by "
                                                                      'warmth, aggravated by cold/pressure, dark '
                                                                      'clotted blood, purplish tongue with petechiae, '
                                                                      'and deep-tight pulse are classic textbook '
                                                                      'findings for Cold Coagulation with Blood Stasis '
                                                                      '(CAM, Maciocia).',
                                                                 'C': '❌ **Incorrect:** Damp-heat presents with '
                                                                      'foul-smelling dark menses, burning sensation, '
                                                                      'yellow greasy coat, and slippery-rapid pulse.',
                                                                 'D': '❌ **Incorrect:** Yin deficiency presents with '
                                                                      'scanty light red blood, night sweats, 5-palm '
                                                                      'heat, and peeled red tongue.'},
                                             'options': [   'A. Qi and Blood Deficiency failing to nourish the uterus',
                                                            'B. Cold Coagulation and Blood Stasis in the Uterus (Han '
                                                            'Ning Xue Yu)',
                                                            'C. Damp-Heat Pouring Downward into the Lower Jiao',
                                                            'D. Liver and Kidney Yin Deficiency with Empty Fire'],
                                             'prompt': 'Severe cramping relieved by warmth, aggravated by pressure and '
                                                       'cold, with dark clotted menses and a deep-tight pulse confirms '
                                                       'which pattern?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation (Zang-Fu & Pathogen)'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** SP1 is the Jing-Well point for '
                                                                      'stopping uterine bleeding.',
                                                                 'B': '❌ **Incorrect:** SP4 is the Luo-Connecting and '
                                                                      'Confluent point for Chong Mai.',
                                                                 'C': '✅ **Correct (SP8 Diji):** Xi-Cleft points are '
                                                                      'where channel Qi and Blood plunge deeply; they '
                                                                      'are specifically indicated for acute, severe '
                                                                      'pain and obstinate conditions in their '
                                                                      'respective organ. SP8 (located 3 cun inferior '
                                                                      'to SP9) is the premier Xi-Cleft point to '
                                                                      'rapidly stop acute dysmenorrhea pain and '
                                                                      'regulate uterine blood flow (Deadman & CAM).',
                                                                 'D': '❌ **Incorrect:** SP10 is Sea of Blood, used for '
                                                                      'chronic skin itching or nourishing blood.'},
                                             'options': [   'A. SP1 (Yinbai)',
                                                            'B. SP4 (Gongsun)',
                                                            'C. SP8 (Diji)',
                                                            'D. SP10 (Xuehai)'],
                                             'prompt': 'Which acupuncture point is the Xi-Cleft point of the Spleen '
                                                       'channel and is renowned as the primary emergency point for '
                                                       'acute dysmenorrhea?',
                                             'question_id': 'Q2',
                                             'title': '2. Xi-Cleft Point Strategy for Acute Pain'},
                                         {   'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Bladder Safety):** CV3 is located '
                                                                      '4 cun below the umbilicus directly overlying '
                                                                      'the urinary bladder. If the bladder is full, '
                                                                      'deep perpendicular insertion can puncture the '
                                                                      'bladder wall, causing extravasation of urine '
                                                                      'into the peritoneal cavity and chemical '
                                                                      'peritonitis. Having the patient void before '
                                                                      'treatment is a mandatory Canadian Clean Needle '
                                                                      'safety rule.',
                                                                 'B': '❌ **Incorrect:** Cold drinks worsen cold '
                                                                      'stagnation.',
                                                                 'C': '❌ **Incorrect:** Puncturing 3 cun deep in the '
                                                                      'lower abdomen risks bladder/intestinal '
                                                                      'puncture.',
                                                                 'D': '❌ **Incorrect:** Ice contradicts the warming '
                                                                      'principle.'},
                                             'options': [   'A. Instruct the patient to empty their urinary bladder '
                                                            'immediately prior to treatment to avoid puncturing a '
                                                            'distended bladder.',
                                                            'B. Have the patient drink 1 liter of cold water to test '
                                                            'thermal response.',
                                                            'C. Insert the needle 3 cun perpendicularly into the '
                                                            'pelvic cavity.',
                                                            'D. Apply ice packs to the sacrum before moxa.'],
                                             'prompt': 'When needling CV3 (Zhongji) and applying moxibustion for '
                                                       'severe uterine cold stagnation, what clinical procedure must '
                                                       'always precede needle insertion?',
                                             'question_id': 'Q3',
                                             'title': '3. Therapeutic Modality & Bladder Safety'}],
        'patient': {   'age': 24,
                       'chief_complaint': 'Severe cramping and stabbing lower abdominal pain occurring 1-2 days before '
                                          'and during menses, forcing her to miss classes monthly.',
                       'four_examinations': {   'auscultation_olfaction': 'Quiet, weak voice during cramping attacks.',
                                                'inquiry': 'Menses arrive every 28-32 days, flow lasts 5 days. Lower '
                                                           'abdomen feels icy cold to her own hand. Denies nausea, '
                                                           'diarrhea, or urinary burning.',
                                                'inspection': 'Curled into fetal position holding lower abdomen. '
                                                              'Complexion is pale and drawn. Tongue body is purplish '
                                                              'dusky with distinct dark purple petechiae on the sides '
                                                              'and base, thin white coating.',
                                                'palpation': 'Lower abdominal palpation reveals cold skin and marked '
                                                             'tenderness over the uterus; patient guards against deep '
                                                             'pressure. Pulse is Deep (Chen), Wiry (Xian), and Tight '
                                                             '(Jin).'},
                       'gender': 'Female',
                       'history': 'Pain started at menarche (age 13) and progressively intensified. Pain is sharply '
                                  'localized to the hypogastrium, relieved by heating pads and hot tea, and sharply '
                                  'aggravated by cold drinks and pressure. Menstrual flow is dark purplish with large '
                                  'clots; passing clots temporarily eases the cramping. Cold hands and feet during '
                                  'menstruation.',
                       'occupation': 'University Graduate Student'},
        'standard_diagnosis': {   'cardinal_points': ['CV3', 'SP8', 'SP6', 'ST29', 'BL32', 'ZIGONG'],
                                  'cautions': 'Moxibustion (indirect stick or warm needle) on lower abdomen (CV3, '
                                              'ST29, Zigong) is strongly indicated to melt cold coagulation. In women '
                                              'of childbearing age presenting with severe pelvic pain, verify '
                                              'pregnancy status and screen for ectopic pregnancy red flags before '
                                              'applying vigorous blood-invigorating needles.',
                                  'patterns': [   'Cold Coagulation and Blood Stasis in Uterus (Han Ning Xue Yu)',
                                                  'Primary Dysmenorrhea (Tong Jing)'],
                                  'synergies': [   'Xi-Cleft acute menstrual pain master (SP8 Diji)',
                                                   'Front-Mu and Uterine palace local pair (CV3 + Zigong with Moxa)',
                                                   'Three Yin junction and Chong/Ren regulator (SP6)',
                                                   'Lumbosacral plexus regulator (BL32 Ciliao)'],
                                  'treatment_principles': [   'Warm the Uterus and Dispel Cold',
                                                              'Promote Blood Circulation and Dissolve Stasis',
                                                              'Regulate Chong and Ren Channels',
                                                              'Stop Menstrual Pain']},
        'title': 'Patient Intake: 24yo Female (University Student)'},
    {   'category': 'Neurological & Sensory',
        'id': 'CASE-007',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Heart Fire presents with '
                                                                      'mouth/tongue ulcers, bitter taste, red tongue '
                                                                      'tip, and rapid surging pulse.',
                                                                 'B': '❌ **Incorrect:** Liver Fire presents with '
                                                                      'violent headaches, irritability, red eyes, and '
                                                                      'wiry-rapid pulse.',
                                                                 'C': '✅ **Correct:** The Spleen governs '
                                                                      'transformation/transportation and produces '
                                                                      'Blood; the Heart governs Blood and houses the '
                                                                      'Shen (Spirit). When Spleen Qi is deficient, '
                                                                      'blood production fails. Without sufficient '
                                                                      'Heart Blood to anchor the Shen at night, the '
                                                                      'mind wanders, causing difficulty falling asleep '
                                                                      'and vivid dreaming (CAM, Maciocia).',
                                                                 'D': '❌ **Incorrect:** Food stagnation causes '
                                                                      'insomnia from epigastric fullness, acid '
                                                                      'regurgitation, and foul breath.'},
                                             'options': [   'A. Heart Fire Blazing disturbing the Shen',
                                                            'B. Liver Fire Transformed into Wind',
                                                            'C. Heart and Spleen Deficiency (Xin Pi Liang Xu) failing '
                                                            'to nourish and anchor the Spirit',
                                                            "D. Food Stagnation in Stomach disrupting sleep ('Stomach "
                                                            "disharmony leads to restless sleep')"],
                                             'prompt': 'Difficulty falling asleep with palpitations, poor memory, pale '
                                                       'lips, loose stools, pale tongue, and thready-weak pulse '
                                                       'confirms which TCM etiology?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation & Shen Pathophysiology'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** PC6 is Luo-Connecting of '
                                                                      'Pericardium, opening the chest.',
                                                                 'B': "✅ **Correct (HT7 Shenmen):** HT7 ('Spirit "
                                                                      "Gate') is located on the wrist crease at the "
                                                                      'radial border of the flexor carpi ulnaris '
                                                                      'tendon. As the Yuan-Source and Shu-Stream Earth '
                                                                      'point of the Heart, it directly nourishes Heart '
                                                                      'Blood, clears deficiency heat, and anchors the '
                                                                      'Shen (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** HT3 is the He-Sea point on the '
                                                                      'elbow.',
                                                                 'D': '❌ **Incorrect:** BL15 is the Back-Shu point on '
                                                                      'the thorax.'},
                                             'options': [   'A. PC6 (Neiguan)',
                                                            'B. HT7 (Shenmen)',
                                                            'C. HT3 (Shaohai)',
                                                            'D. BL15 (Xinshu)'],
                                             'prompt': 'Which point is the Yuan-Source and Shu-Stream point of the '
                                                       'Heart channel and the premier point for calming the Spirit?',
                                             'question_id': 'Q2',
                                             'title': '2. Point Prescription & Yuan-Source Spirit Anchor'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Perpendicular insertion over '
                                                                      '1.0 cun in the thoracic zone easily punctures '
                                                                      'the parietal and visceral pleura, causing '
                                                                      'traumatic pneumothorax (a leading malpractice '
                                                                      'liability in acupuncture).',
                                                                 'B': '✅ **Correct:** CARB-TCMPA Safety standard: All '
                                                                      'medial bladder line points on the thorax (BL11 '
                                                                      'to BL21) must be needled obliquely medially '
                                                                      'toward the spine (or transversely/obliquely '
                                                                      'along the rib) at a shallow depth of 0.5 to 0.8 '
                                                                      'cun to ensure the needle tip remains over '
                                                                      'bony/muscular planes and stays away from the '
                                                                      'pleural cavity.',
                                                                 'C': '❌ **Incorrect:** Extremely dangerous, '
                                                                      'guaranteed pneumothorax.',
                                                                 'D': '❌ **Incorrect:** Lateral puncture penetrates '
                                                                      'intercostal spaces and lung tissue.'},
                                             'options': [   'A. Perpendicular insertion 1.5 - 2.0 cun directly into '
                                                            'the intercostal space.',
                                                            'B. Oblique insertion 0.5 - 0.8 cun directed medially '
                                                            'towards the vertebral column (or along the rib surface).',
                                                            'C. Perpendicular insertion 2.5 cun until bone is struck.',
                                                            'D. Puncture perpendicularly towards the lateral axillary '
                                                            'line.'],
                                             'prompt': 'What is the mandatory needling direction and depth for BL15 '
                                                       '(Xinshu) located 1.5 cun lateral to the lower border of T5 '
                                                       'spinous process?',
                                             'question_id': 'Q3',
                                             'title': '3. Needling Angle & Pneumothorax Safety at BL15'}],
        'patient': {   'age': 39,
                       'chief_complaint': 'Difficulty falling asleep for over 1 year, taking 2-3 hours to sleep, '
                                          'accompanied by constant fatigue, heart palpitations, and forgetfulness.',
                       'four_examinations': {   'auscultation_olfaction': 'Quiet speech, frequent sighing from '
                                                                          'exhaustion.',
                                                'inquiry': 'Denies night sweats or fever. Appetite is poor; feels '
                                                           'bloating after small lunches. Menses are light pink, '
                                                           'scanty, and arrive late.',
                                                'inspection': 'Sallow, lusterless complexion. Pale lips and pale '
                                                              'palpebral conjunctivae. Tongue body is pale, thin, with '
                                                              'scalloped teeth marks along the margins and a thin '
                                                              'white coating.',
                                                'palpation': 'Pulse is Thready (Xi) and Weak (Ruo), particularly '
                                                             'delicate in the left Cun (Heart) and right Guan (Spleen) '
                                                             'positions.'},
                       'gender': 'Female',
                       'history': 'Under severe work stress grading exams and managing difficult classrooms. Sleep is '
                                  'fitful and disturbed by vivid non-frightening dreams. Wakes up unrefreshed. Reports '
                                  'mild dizziness upon standing, diminished appetite, loose stools after greasy meals, '
                                  'and noticeable thinning of hair.',
                       'occupation': 'High School Teacher'},
        'standard_diagnosis': {   'cardinal_points': ['HT7', 'SP6', 'BL15', 'BL20', 'PC6', 'ANMIAN', 'ST36'],
                                  'cautions': 'Tonification method is indicated. When needling Back-Shu points BL15 '
                                              '(Xinshu) and BL20 (Pishu), needle obliquely toward the spine 0.5-0.8 '
                                              'cun. Never insert perpendicularly into thoracic intercostal spaces due '
                                              'to high risk of pneumothorax.',
                                  'patterns': [   'Heart and Spleen Deficiency (Xin Pi Liang Xu)',
                                                  'Blood Deficiency Failing to Anchor Shen (Insomnia / Bu Mei)'],
                                  'synergies': [   'Yuan-Source Shen anchor (HT7 Shenmen)',
                                                   'Three Yin intersection blood builder (SP6)',
                                                   'Back-Shu heart-spleen tonic pair (BL15 + BL20)',
                                                   'Extra empirical sleep master (Anmian)',
                                                   'Post-heaven root (ST36)'],
                                  'treatment_principles': [   'Tonify Spleen Qi and Generate Blood',
                                                              'Nourish the Heart and Anchor the Shen (Mind)',
                                                              'Calm the Spirit and Restore Sleep']},
        'title': 'Patient Intake: 39yo Female (High School Teacher)'},
    {   'category': 'Internal Medicine',
        'id': 'CASE-008',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Heart does not produce phlegm.',
                                                                 'B': '✅ **Correct:** Classic fundamental TCM maxim: '
                                                                      "'Pi wei sheng tan zhi yuan, fei wei zhu tan zhi "
                                                                      "qi' (The Spleen is the source of phlegm "
                                                                      'formation; the Lung is the storage vessel for '
                                                                      'phlegm). Impaired Spleen transformation of '
                                                                      'fluids causes dampness to pool, which congeals '
                                                                      'into phlegm that flows upward to lodge in the '
                                                                      'bronchial tree (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Kidney governs water, but '
                                                                      'Spleen produces phlegm.',
                                                                 'D': '❌ **Incorrect:** Not a canonical TCM aphorism.'},
                                             'options': [   "A. 'The Heart produces Phlegm and the Liver stores it.'",
                                                            "B. 'The Spleen is the source of Phlegm production; the "
                                                            "Lung is the container that stores Phlegm.'",
                                                            "C. 'The Kidney generates Phlegm and the Bladder "
                                                            "transforms it.'",
                                                            "D. 'The Gallbladder cooks Phlegm into Fire.'"],
                                             'prompt': 'According to classic TCM physiology, what is the precise organ '
                                                       'relationship explaining why Spleen dysfunction causes chronic '
                                                       'productive cough?',
                                             'question_id': 'Q1',
                                             'title': '1. Zang-Fu Relationship & Phlegm Etiology'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** ST36 tonifies Qi and Blood.',
                                                                 'B': '❌ **Incorrect:** SP9 is the He-Sea point for '
                                                                      'draining Dampness (edema, diarrhea), not '
                                                                      'specifically congealed phlegm.',
                                                                 'C': '✅ **Correct (ST40 Fenglong):** ST40 is the '
                                                                      'Luo-Connecting point of the Stomach channel '
                                                                      'connecting to the Spleen. It has the unique '
                                                                      "empirical action of activating the Spleen's "
                                                                      'fluid transformation mechanism and dissolving '
                                                                      'both substantial phlegm (sputum) and '
                                                                      'non-substantial phlegm (nodules, lipomas, '
                                                                      'clouding of mind) anywhere in the body (Deadman '
                                                                      '& CAM).',
                                                                 'D': '❌ **Incorrect:** LU9 is Yuan-Source for '
                                                                      'tonifying Lung Yin/Qi.'},
                                             'options': [   'A. ST36 (Zusanli)',
                                                            'B. SP9 (Yinlingquan)',
                                                            'C. ST40 (Fenglong)',
                                                            'D. LU9 (Taiyuan)'],
                                             'prompt': 'Which acupuncture point is universally recognized across '
                                                       'textbooks as the premier empirical point to dissolve and '
                                                       'transform all forms of Phlegm in the body?',
                                             'question_id': 'Q2',
                                             'title': '2. Master Empirical Point for All Phlegm'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Deqi does not produce dyspnea '
                                                                      'or pleuritic chest pain.',
                                                                 'B': '✅ **Correct (Pneumothorax Emergency):** '
                                                                      'Pneumothorax symptoms can develop immediately '
                                                                      'or hours later. Pleuritic pain, shortness of '
                                                                      'breath, diminished breath sounds on '
                                                                      'auscultation, and tachypnea after upper '
                                                                      'back/chest needling indicate air leakage into '
                                                                      'the pleural space. The practitioner must keep '
                                                                      'the patient calm, seated upright, administer '
                                                                      'oxygen if certified, and call 911 immediately '
                                                                      '(CARB-TCMPA safety guidelines).',
                                                                 'C': '❌ **Incorrect:** Local twitch response is '
                                                                      'momentary, not dyspneic.',
                                                                 'D': '❌ **Incorrect:** Not a biomechanical trauma.'},
                                             'options': [   'A. Normal Deqi propagation through the Taiyang channel.',
                                                            'B. Traumatic Pneumothorax requiring immediate chest '
                                                            'examination and emergency hospital transfer.',
                                                            'C. Myofascial trigger point release twitch response.',
                                                            'D. Sudden Heart Fire flare-up.'],
                                             'prompt': 'If a patient experiences sudden sharp chest pain, shortness of '
                                                       'breath, rapid shallow breathing, and dry cough 20 minutes '
                                                       'following needling of thoracic back points, what complication '
                                                       'must be suspected?',
                                             'question_id': 'Q3',
                                             'title': '3. Pneumothorax Red Flag Identification'}],
        'patient': {   'age': 58,
                       'chief_complaint': 'Chronic loose cough for 6 months, producing profuse white sticky sputum '
                                          'that is easy to expectorate, worse in the mornings.',
                       'four_examinations': {   'auscultation_olfaction': 'Rattling, wet bronchial cough; deep, '
                                                                          'gurgling sound in the chest during '
                                                                          'expiration.',
                                                'inquiry': 'Reports heavy sensation in the head and limbs like wearing '
                                                           'wet clothes; loose stools with undigested food; absence of '
                                                           'thirst.',
                                                'inspection': 'Overweight constitution. Dull facial complexion. Tongue '
                                                              'body is pale and swollen with scalloped tooth marks, '
                                                              'covered in a thick, sticky, greasy white coating.',
                                                'palpation': 'Epigastrium is soft but distended upon palpation. Pulse '
                                                             'is Slippery (Hua) and Moderate/Soggy (Ru).'},
                       'gender': 'Male',
                       'history': 'Long history of consuming cold beers, dairy, and deep-fried diner food. Reports '
                                  'heavy fullness and oppression in the chest and epigastrium, loss of appetite, and '
                                  'chronic fatigue. Denies fever, night sweats, blood in sputum, or sore throat. '
                                  'Walking upstairs makes him short of breath.',
                       'occupation': 'Heavy Machinery Mechanic'},
        'standard_diagnosis': {   'cardinal_points': ['LU7', 'LU5', 'ST40', 'CV12', 'BL13', 'BL20'],
                                  'cautions': 'Avoid tonifying methods that trap dampness. Disperse or harmonize. At '
                                              'BL13 (Feishu), maintain oblique medial insertion toward spine 0.5-0.8 '
                                              'cun to prevent pneumothorax. If patient develops hemoptysis (blood in '
                                              'sputum) or unexplained rapid weight loss, initiate medical referral for '
                                              'chest X-ray / CT.',
                                  'patterns': [   'Phlegm-Damp Obstructing the Lung (Tan Shi Zu Fei)',
                                                  'Spleen Deficiency Generating Phlegm Stored in Lung'],
                                  'synergies': [   'Master empirical phlegm transformer (ST40 Fenglong)',
                                                   'Front-Mu of Stomach middle jiao transformer (CV12)',
                                                   'Luo-Connecting Lung commander (LU7)',
                                                   'Water He-Sea phlegm clearer (LU5 Chize)',
                                                   'Back-Shu Lung-Spleen pair (BL13 + BL20)'],
                                  'treatment_principles': [   'Strengthen the Spleen and Dry Dampness',
                                                              'Transform Phlegm and Diffuse Lung Qi',
                                                              'Descend Rebellious Qi and Stop Cough']},
        'title': 'Patient Intake: 58yo Male (Heavy Machinery Mechanic)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-009',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Heat Bi presents with red, '
                                                                      'burning hot, swollen joints and a rapid pulse.',
                                                                 'B': '✅ **Correct:** Chronic knee swelling with '
                                                                      "atrophy resembling a crane's leg is "
                                                                      "traditionally named 'Crane's Knee Wind' (He Xi "
                                                                      'Feng), caused by Cold-Damp pathogens stagnating '
                                                                      'in the sinews combined with Liver/Kidney '
                                                                      'deficiency (CAM & Deadman).',
                                                                 'C': '❌ **Incorrect:** Gout presents with acute '
                                                                      'exquisite erythema, burning pain typically at '
                                                                      'the 1st MTP joint.',
                                                                 'D': '❌ **Incorrect:** Liver Wind causes tremors, '
                                                                      'convulsions, or stroke, not localized knee '
                                                                      'joint degeneration.'},
                                             'options': [   'A. Heat Bi (Re Bi) with blazing Fire',
                                                            "B. Cold-Damp Bi Syndrome / Crane's Knee Wind (He Xi Feng)",
                                                            'C. Gouty Arthritis due to Toxic Damp-Heat in Blood',
                                                            'D. Liver Wind Agitating Internally'],
                                             'prompt': 'Bilateral knee swelling with quadriceps atrophy, pain '
                                                       'aggravated by cold and dampness, with a pale swollen tongue '
                                                       'and deep-slow pulse describes which classic TCM syndrome?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation & Clinical Terminology'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Superficial 0.1 cun insertion '
                                                                      'does not reach joint capsules or infrapatellar '
                                                                      'fat pads.',
                                                                 'B': '✅ **Correct:** With the knee flexed at 90°, the '
                                                                      'medial and lateral soft depressions adjacent to '
                                                                      'the patellar ligament open up. Needling '
                                                                      'directed toward the center of the joint cavity '
                                                                      'engages the synovial lining, stimulates joint '
                                                                      'fluid reabsorption, and relieves patellofemoral '
                                                                      'friction (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Bleeding is not indicated on '
                                                                      'infrapatellar fat pads.',
                                                                 'D': '❌ **Incorrect:** Puncturing through bone is '
                                                                      'dangerous and absurd.'},
                                             'options': [   'A. Perpendicular 0.1 cun into the skin only.',
                                                            'B. Punctured obliquely 1.0 - 1.5 cun directed slightly '
                                                            'upwards and medially toward the center of the joint '
                                                            'cavity behind the patellar ligament with the knee flexed '
                                                            'at 90 degrees.',
                                                            'C. Strongly bled with a plum blossom needle until 50 ml '
                                                            'of blood is drained.',
                                                            'D. Needled through the patellar bone using an orthopedic '
                                                            'hammer.'],
                                             'prompt': "How should the classic local point pair 'Eyes of the Knee' "
                                                       '(Dubi ST35 and Neixiyan) be needled for knee osteoarthritis?',
                                             'question_id': 'Q2',
                                             'title': '2. Joint Point Pair & Needle Direction'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Bruising is minor compared to '
                                                                      'joint infection.',
                                                                 'B': '✅ **Correct (Infection Control Safety):** '
                                                                      'Intra-articular structures have limited '
                                                                      'phagocytic defense. A needle contaminated by '
                                                                      'unwashed hands or non-sterile technique '
                                                                      'introduces bacteria directly into the joint '
                                                                      'space, triggering acute purulent septic '
                                                                      'arthritis requiring emergency surgical joint '
                                                                      'debridement and prolonged IV antibiotics '
                                                                      '(CARB-TCMPA safety guidelines).',
                                                                 'C': '❌ **Incorrect:** Needle breakage is extremely '
                                                                      'rare with modern stainless steel single-use '
                                                                      'needles.',
                                                                 'D': '❌ **Incorrect:** Knee needling does not cause '
                                                                      'anaphylaxis.'},
                                             'options': [   'A. Because knee points are prone to excessive bruising.',
                                                            'B. Because the synovial joint cavity is avascular and '
                                                            'closed; introducing skin flora (e.g. Staphylococcus '
                                                            'aureus) into the joint space can cause irreversible '
                                                            'septic arthritis and permanent joint destruction.',
                                                            'C. Because knee needles can break if the patient '
                                                            'twitches.',
                                                            'D. Because knee points cause systemic anaphylaxis.'],
                                             'prompt': 'Why is rigorous aseptic Clean Needle Technique (CNT) '
                                                       'critically emphasized when treating intra-articular knee '
                                                       'points in Canada?',
                                             'question_id': 'Q3',
                                             'title': '3. Clean Needle Technique & Septic Joint Safety'}],
        'patient': {   'age': 67,
                       'chief_complaint': 'Bilateral knee aching, deep stiffness, and swelling for over 2 years, '
                                          'making it agonizing to descend stairs or squat.',
                       'four_examinations': {   'auscultation_olfaction': 'Audible crepitation/crackling in both '
                                                                          'patellofemoral joints on passive flexion.',
                                                'inquiry': 'Feels heavy weakness in lower limbs; lower back ache; '
                                                           'aversion to cold winds.',
                                                'inspection': 'Bilateral suprapatellar and infrapatellar swelling '
                                                              "('Crane's Knee' appearance) with quadriceps femoris "
                                                              'muscular atrophy. Tongue body is pale, swollen, with '
                                                              'scalloped margins and a thick wet white coating.',
                                                'palpation': 'Knee joints feel cold to touch; joint effusion palpable. '
                                                             'Marked tenderness at Dubi (ST35), Neixiyan, and Heding. '
                                                             'Pulse is Deep (Chen), Slow (Chi), and Slippery (Hua).'},
                       'gender': 'Female',
                       'history': 'Stood on cold concrete bakery floors for 35 years. Knees are stiff for 45 minutes '
                                  'every morning upon waking. Pain is acutely aggravated by rainy, damp, and cold '
                                  'Canadian weather, and eased somewhat by hot compresses. Noticeable crepitus '
                                  '(grating sound and feel) during knee flexion.',
                       'occupation': 'Retired Baker'},
        'standard_diagnosis': {   'cardinal_points': ['ST35', 'NEIXIYAN', 'HEDING', 'GB34', 'SP9', 'ST36'],
                                  'cautions': 'Strict aseptic Clean Needle Technique (CNT) is mandatory: puncturing '
                                              'the knee capsule in an elderly or immunocompromised patient risks '
                                              'catastrophic septic arthritis. Needling directly into an acutely '
                                              'infected, hot, erythematous septic joint is contraindicated.',
                                  'patterns': [   "Cold-Damp Knee Bi Syndrome (He Xi Feng / Crane's Knee)",
                                                  'Spleen and Kidney Deficiency with Local Meridian Stagnation'],
                                  'synergies': [   'Eyes of the Knee joint cavity pair (ST35 Dubi + Neixiyan)',
                                                   'Superior patellar regulator (Heding)',
                                                   'Hui-Meeting of Sinews (GB34)',
                                                   'He-Sea dampness drainer (SP9 Yinlingquan)',
                                                   'Earth tonic (ST36)'],
                                  'treatment_principles': [   'Dispel Cold and Eliminate Dampness',
                                                              'Unblock Knee Channels and Collaterals',
                                                              'Strengthen Tendons and Bones',
                                                              'Tonify Spleen and Kidney']},
        'title': 'Patient Intake: 67yo Female (Retired Baker)'},
    {   'category': 'Internal Medicine',
        'id': 'CASE-010',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Spleen failing to nourish Lung '
                                                                      'causes chronic phlegm or shortness of breath.',
                                                                 'B': '✅ **Correct:** Emotional constraint causes '
                                                                      'Liver (Wood) Qi to stagnate. When constrained '
                                                                      'Wood turns into Fire, it overacts '
                                                                      'transverse-wise on Stomach (Earth), preventing '
                                                                      'Stomach Qi from descending normally and forcing '
                                                                      'acid/food upward (rebellious Qi) with burning '
                                                                      'pain (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Reversed control between Metal '
                                                                      'and Fire is not involved here.',
                                                                 'D': '❌ **Incorrect:** Water over-controlling Fire '
                                                                      'manifests in Heart-Kidney imbalances.'},
                                             'options': [   'A. Earth failing to produce Metal',
                                                            'B. Wood (Liver) Overacting on Earth (Stomach / Spleen) '
                                                            'transforming into Fire',
                                                            'C. Metal insulting Fire',
                                                            'D. Water over-controlling Fire'],
                                             'prompt': 'Burning epigastric distension triggered by emotional stress, '
                                                       'loud belching, wiry-rapid pulse, and red tongue margins '
                                                       'reflects which classic Five-Element pathological dynamic?',
                                             'question_id': 'Q1',
                                             'title': '1. Five-Element Relationship & Pathology'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** LU7 opens the Ren Mai (head '
                                                                      'and neck).',
                                                                 'B': '❌ **Incorrect:** SI3 opens the Du Mai (spine '
                                                                      'and back).',
                                                                 'C': '✅ **Correct (PC6 Neiguan):** The Ba Mai Jiao '
                                                                      'Hui Xue (Eight Confluent Points) assign PC6 to '
                                                                      'the Yin Wei Mai. It commands the chest, heart, '
                                                                      "and epigastrium ('Xin xiong wei nei guan'). It "
                                                                      'descends rebellious Stomach Qi, stops nausea, '
                                                                      'relieves hiccups, and calms emotional '
                                                                      'constraint (Deadman & CAM).',
                                                                 'D': '❌ **Incorrect:** GB41 opens the Dai Mai (outer '
                                                                      'cantus, hip, migraine).'},
                                             'options': [   'A. LU7 (Lieque)',
                                                            'B. SI3 (Houxi)',
                                                            'C. PC6 (Neiguan)',
                                                            'D. GB41 (Zulinqi)'],
                                             'prompt': 'Which acupuncture point opens the Yin Wei Mai (Yin Linking '
                                                       'Vessel) and is the premier master point for all epigastric, '
                                                       'cardiac, and chest disorders?',
                                             'question_id': 'Q2',
                                             'title': '2. Eight Confluent Master Point for Epigastrium & Chest'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Perpendicular insertion over 1 '
                                                                      'cun easily pierces through the intercostal '
                                                                      'membrane into the pleural cavity and liver '
                                                                      'tissue.',
                                                                 'B': '✅ **Correct:** CARB-TCMPA safety guidelines '
                                                                      'mandate that LR14 must be needled obliquely or '
                                                                      'transversely (0.5 to 0.8 cun) along the '
                                                                      'intercostal groove. Deep perpendicular '
                                                                      'insertion risks traumatic pneumothorax on '
                                                                      'either side, and on the right side risks '
                                                                      'hepatic parenchymal laceration with internal '
                                                                      'bleeding (Deadman precautions).',
                                                                 'C': '❌ **Incorrect:** Extremely dangerous, could '
                                                                      'puncture pericardium.',
                                                                 'D': '❌ **Incorrect:** Moxa stick is not a needle '
                                                                      'insertion.'},
                                             'options': [   'A. Perpendicular insertion 1.5 - 2.0 cun directly into '
                                                            'the intercostal muscle.',
                                                            'B. Oblique or transverse insertion 0.5 - 0.8 cun along '
                                                            'the course of the intercostal space; perpendicular deep '
                                                            'puncture is strictly contraindicated due to risk of '
                                                            'pneumothorax and liver puncture.',
                                                            'C. Deep upward insertion towards the apex of the heart.',
                                                            'D. Perpendicular insertion with high-frequency moxa '
                                                            'stick.'],
                                             'prompt': 'When needling LR14 (Qimen, the Front-Mu point of the Liver '
                                                       'located in the 6th intercostal space along the mamillary '
                                                       'line), what is the mandatory needling direction and safety '
                                                       'rule?',
                                             'question_id': 'Q3',
                                             'title': '3. Anatomical Caution at LR14 (Qimen)'}],
        'patient': {   'age': 44,
                       'chief_complaint': 'Burning and distending pain in the epigastrium radiating into both '
                                          'hypochondria, with frequent acid regurgitation and sour belching.',
                       'four_examinations': {   'auscultation_olfaction': 'Loud, explosive belching and frequent '
                                                                          'involuntary deep sighing.',
                                                'inquiry': 'Burning sensation behind the sternum (pyrosis / '
                                                           'heartburn), relieved temporarily by cold milk. Restless '
                                                           'sleep with vivid dreams. Constipation with dry knotty '
                                                           'stools.',
                                                'inspection': 'Flushed cheeks during consultation, furrowed brow. '
                                                              'Tongue body is red, particularly more fiery red along '
                                                              'the lateral edges, covered with a thin yellow coating.',
                                                'palpation': 'Epigastrium and right hypochondrium are tender to '
                                                             'palpation with mild muscle guarding. Pulse is Wiry '
                                                             '(Xian) and Rapid (Shuo).'},
                       'gender': 'Male',
                       'history': 'Pain intensifies dramatically during stressful deadlines and financial audits. '
                                  'Experiences emotional irritability, tight sensation in the throat (plum-pit '
                                  'sensation), dry bitter taste in the mouth, and bloating immediately after eating.',
                       'occupation': 'Financial Risk Analyst'},
        'standard_diagnosis': {   'cardinal_points': ['CV12', 'ST36', 'PC6', 'LR14', 'LR3', 'ST44'],
                                  'cautions': 'Needling LR14 (Qimen) in the 6th intercostal space must be strictly '
                                              'oblique 0.5-0.8 cun along the rib course. Perpendicular insertion risks '
                                              'puncturing the pleura, lungs, or underlying liver/spleen.',
                                  'patterns': [   'Liver Qi Invading Stomach with Heat Transformation (Gan Wei Bu He)',
                                                  'Epigastric Pain / Acid Reflux (Wei Tong / Tun Suan)'],
                                  'synergies': [   'Front-Mu of Stomach master (CV12 Zhongwan)',
                                                   'Eight Confluent chest/epigastric regulator (PC6 Neiguan)',
                                                   'Front-Mu of Liver intercostal anchor (LR14 Qimen)',
                                                   'Yuan-Source Wood sedater (LR3)',
                                                   'Water-Spring Stomach heat clearer (ST44 Neiting)'],
                                  'treatment_principles': [   'Soothe Liver Qi and Clear Liver Heat',
                                                              'Harmonize the Stomach and Descend Rebellious Qi',
                                                              'Alleviate Epigastric Pain and Stop Acid']},
        'title': 'Patient Intake: 44yo Male (Financial Risk Analyst)'},
    {   'category': 'Internal Medicine',
        'id': 'CASE-011',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Heat Wheezing produces thick, '
                                                                      'sticky, foul-smelling yellow or green sputum, '
                                                                      'burning sensation in chest, red tongue with '
                                                                      'yellow coat, and slippery-rapid pulse.',
                                                                 'B': '❌ **Incorrect:** Yin deficiency wheezing '
                                                                      'presents with dry non-productive cough, night '
                                                                      'sweats, 5-palm heat, and peeled red tongue.',
                                                                 'C': '✅ **Correct:** Cold Wheezing (Han Xiao) occurs '
                                                                      'when exterior Wind-Cold constrains pre-existing '
                                                                      'deep-seated cold fluids in the bronchial tree. '
                                                                      'Cold causes phlegm to remain thin, white, and '
                                                                      'frothy, accompanied by severe bronchospasm, '
                                                                      'aversion to cold, and white slippery tongue '
                                                                      'coat (CAM, Maciocia).',
                                                                 'D': '❌ **Incorrect:** Spleen failing to hold blood '
                                                                      'causes hemorrhages.'},
                                             'options': [   'A. Heat Wheezing (Re Xiao) with thick yellow phlegm and '
                                                            'thirst',
                                                            'B. Lung and Kidney Yin Deficiency with Empty Fire',
                                                            'C. Cold Wheezing (Han Xiao) with retention of Cold Phlegm',
                                                            'D. Spleen Qi Deficiency failing to hold Blood'],
                                             'prompt': 'Wheezing with profuse thin frothy white sputum, aversion to '
                                                       'cold, pale tongue with white slippery coat, and floating-tight '
                                                       'pulse defines which diagnostic category?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation (Cold Wheezing vs Heat Wheezing)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Bailao (2 cun above C7, 1 cun '
                                                                      'lateral) is for scrofula, neck pain, night '
                                                                      'sweats.',
                                                                 'B': "✅ **Correct (Dingchuan - 'Stop Wheezing'):** "
                                                                      'Dingchuan is famously situated 0.5 cun lateral '
                                                                      'to C7 (Dazhui). It has an immediate reflex '
                                                                      'bronchodilating action that diffuses Lung Qi, '
                                                                      'descends rebellious airway Qi, and arrests '
                                                                      'acute wheezing in both bronchial asthma and '
                                                                      'bronchitis (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Huatuo Jiaji is a general '
                                                                      'spinal group.',
                                                                 'D': '❌ **Incorrect:** Yaotongxue is for acute lumbar '
                                                                      'sprain.'},
                                             'options': [   'A. Bailao',
                                                            'B. Dingchuan',
                                                            'C. Huatuo Jiaji',
                                                            'D. Yaotongxue'],
                                             'prompt': 'Which Extra point located 0.5 cun lateral to the lower border '
                                                       'of the spinous process of C7 is the premier point for '
                                                       'arresting wheezing and dyspnea?',
                                             'question_id': 'Q2',
                                             'title': '2. Premier Empirical Extra Point for Wheezing'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Perpendicular deep puncture at '
                                                                      'CV22 penetrates directly into the trachea, '
                                                                      'causing violent cough, hemoptysis, or puncture '
                                                                      'of the brachiocephalic artery/aortic arch.',
                                                                 'B': '✅ **Correct (CV22 Safety Protocol):** '
                                                                      'CARB-TCMPA examination rules strictly test '
                                                                      'CV22: first insert 0.2-0.3 cun perpendicularly '
                                                                      'through the skin, then alter the needle angle '
                                                                      'to point directly downwards, hugging the '
                                                                      'posterior surface of the manubrium of the '
                                                                      'sternum 0.5 to 1.0 cun. This avoids penetrating '
                                                                      'the trachea or the great vessels located '
                                                                      'immediately behind it (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Angling upwards risks '
                                                                      'penetrating the thyroid gland or larynx.',
                                                                 'D': '❌ **Incorrect:** CV22 is not a bleeding point.'},
                                             'options': [   'A. Puncture 2.0 cun perpendicularly straight back towards '
                                                            'the trachea.',
                                                            'B. Puncture 0.2 - 0.3 cun perpendicularly, then direct '
                                                            'the needle tip downwards behind the posterior aspect of '
                                                            'the manubrium of the sternum to a depth of 0.5 - 1.0 cun.',
                                                            'C. Puncture horizontally upwards towards the thyroid '
                                                            'cartilage 1.5 cun.',
                                                            'D. Bleed the point with a lancet.'],
                                             'prompt': 'What is the correct two-step insertion technique for CV22 '
                                                       '(Tiantu) located in the center of the suprasternal fossa?',
                                             'question_id': 'Q3',
                                             'title': '3. Needle Technique & Anatomical Safety at CV22 (Tiantu)'}],
        'patient': {   'age': 29,
                       'chief_complaint': 'Acute wheezing, shortness of breath, chest constriction, and inability to '
                                          'lie flat following exposure to autumn cold air.',
                       'four_examinations': {   'auscultation_olfaction': 'Loud, high-pitched expiratory wheezing '
                                                                          'audible across the room; rapid panting '
                                                                          'breath.',
                                                'inquiry': 'Feels tight constriction in upper chest; chills without '
                                                           'sweating; headache in the occiput.',
                                                'inspection': 'Orthopneic posture (sitting upright, leaning forward '
                                                              'with arms propped on knees). Pale complexion, slight '
                                                              'cyanotic tinge around lips. Tongue body is pale with a '
                                                              'thick white wet/slippery coating.',
                                                'palpation': 'Pulse is Floating, Tight, and Rapid (Fu Jin Shuo).'},
                       'gender': 'Male',
                       'history': 'History of childhood asthma. Paroxysm triggered after raking wet cold leaves '
                                  'outdoors for 6 hours. Expectoration of profuse, thin, clear, frothy white sputum. '
                                  'Aversion to cold, lack of thirst, preferred drinking hot water.',
                       'occupation': 'Landscape Gardener'},
        'standard_diagnosis': {   'cardinal_points': ['DINGCHUAN', 'LU7', 'BL13', 'CV22', 'CV17', 'PC6'],
                                  'cautions': 'Needling CV22 (Tiantu) requires precise technique: puncture 0.2 cun '
                                              'perpendicularly, then angle needle inferiorly behind the manubrium of '
                                              'sternum 0.5-1.0 cun. Red Flag Emergency Rule: If oxygen saturation '
                                              '(SpO2) drops below 92%, or patient develops silent chest (loss of '
                                              'breath sounds from critical airway occlusion), cyanosis, or confusion, '
                                              'immediately administer bronchodilator and call 911.',
                                  'patterns': [   'Cold Wheezing Paroxysm (Han Xiao / Asthma Attack)',
                                                  'Exterior Wind-Cold Constraining Interior Cold Phlegm'],
                                  'synergies': [   'Premier empirical anti-wheezing Extra point (Dingchuan)',
                                                   'Front-Mu of Pericardium / Hui-Meeting of Qi (CV17 Danzhong)',
                                                   'Suprasternal notch throat opener (CV22 Tiantu)',
                                                   'Lung Luo-connecting diffuser (LU7)'],
                                  'treatment_principles': [   'Dispel Wind and Scatter Cold',
                                                              'Diffuse Lung Qi and Transform Phlegm',
                                                              'Descend Rebellious Qi and Relieve Wheezing (Ding '
                                                              'Chuan)']},
        'title': 'Patient Intake: 29yo Male (Landscape Gardener)'},
    {   'category': 'Neurological & Sensory',
        'id': 'CASE-012',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Heart fire and spleen cold '
                                                                      'does not explain rotary vertigo with sore '
                                                                      'lumbar and wiry-rapid pulse.',
                                                                 'B': "✅ **Correct:** 'Water fails to nourish Wood' "
                                                                      '(Kidney Yin fails to anchor Liver Yin). The '
                                                                      'depleted Yin is the Root (Ben), causing Yang to '
                                                                      'lose its restraint and surge uncontrollably up '
                                                                      'to the head (Branch / Biao), causing severe '
                                                                      'spinning vertigo, throbbing headache, tinnitus, '
                                                                      'and elevated blood pressure (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Phlegm-damp vertigo presents '
                                                                      "with heavy clouded head ('wrapped in a towel') "
                                                                      'and greasy tongue, not flushed face and roaring '
                                                                      'tinnitus.',
                                                                 'D': '❌ **Incorrect:** Irrelevant to vertigo.'},
                                             'options': [   'A. Root: Heart Fire; Branch: Spleen Cold',
                                                            'B. Root: Kidney and Liver Yin Deficiency; Branch: '
                                                            'Hyperactive Liver Yang Rising / Internal Wind',
                                                            'C. Root: Spleen Qi Deficiency; Branch: Phlegm-Damp '
                                                            'Stagnation',
                                                            'D. Root: Lung Dryness; Branch: Large Intestine Heat'],
                                             'prompt': "What is the precise 'Root' (Ben) and 'Branch' (Biao) dynamic "
                                                       "operating in this patient's severe vertigo?",
                                             'question_id': 'Q1',
                                             'title': '1. Root and Branch Pathophysiology'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Moxa on BL23/DU4 warms Yang '
                                                                      'and would violently exacerbate ascending Yang '
                                                                      'Fire and vertigo.',
                                                                 'B': '✅ **Correct:** LR3 (Yuan-Source of Liver) '
                                                                      'strongly drains constrained Wood fire and draws '
                                                                      'rebellious Yang downwards; GB20 clears wind '
                                                                      'from the head. Concurrently, tonifying KD3 '
                                                                      '(Yuan-Source of Kidney) and SP6 nourishes Yin '
                                                                      'and restores Water to anchor the Yang '
                                                                      'permanently (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Bleeding Jing-Well points of '
                                                                      'Lung/LI is for acute sore throat and loss of '
                                                                      'consciousness.',
                                                                 'D': '❌ **Incorrect:** Local scalp needling alone '
                                                                      'does not address the systemic Zang-Fu root.'},
                                             'options': [   'A. Tonifying BL23 and DU4 with heavy moxibustion',
                                                            'B. Reducing (Sedating) LR3 (Taichong) and GB20 (Fengchi), '
                                                            'while Tonifying KD3 (Taixi) and SP6 (Sanyinjiao)',
                                                            'C. Bleeding LU11 and LI1 with lancet',
                                                            'D. Retaining needles only on local scalp points without '
                                                            'limb points'],
                                             'prompt': 'Which combination of points directly executes the principle of '
                                                       "'Sedating Wood to quell the Branch while Tonifying Water to "
                                                       "support the Root'?",
                                             'question_id': 'Q2',
                                             'title': '2. Point Strategy (Subduing Branch while Nourishing Root)'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Delaying emergency medical '
                                                                      'care for stroke causes irreversible brain '
                                                                      'infarction; time is brain.',
                                                                 'B': '❌ **Incorrect:** Dangerous malpractice delay.',
                                                                 'C': '✅ **Correct (CARB-TCMPA Emergency Protocol):** '
                                                                      'New onset of unilateral weakness, arm drift, '
                                                                      'facial droop, or dysphasia indicates acute '
                                                                      'cerebrovascular accident (ischemic stroke or '
                                                                      'intracranial hemorrhage). The therapeutic '
                                                                      'window for thrombolysis (tPA / endovascular '
                                                                      'thrombectomy) is within 4.5 hours of onset. '
                                                                      'Calling 911 immediately is legally and '
                                                                      'ethically required of all Canadian registered '
                                                                      'acupuncturists.',
                                                                 'D': '❌ **Incorrect:** Cupping is irrelevant and '
                                                                      'delays critical care.'},
                                             'options': [   'A. Apply strong needle manipulation on DU26 and retain '
                                                            'needles for 2 hours.',
                                                            'B. Instruct the patient to drink hot green tea and rest '
                                                            'for an hour.',
                                                            'C. Recognize acute stroke / TIA (FAST protocol: Face, '
                                                            'Arms, Speech, Time), terminate the acupuncture session, '
                                                            'and immediately dial 911 for emergency medical transport.',
                                                            "D. Perform cupping on the patient's upper back."],
                                             'prompt': 'If during the consultation, the patient suddenly exhibits '
                                                       'slurred speech and right-sided arm drift (inability to '
                                                       'maintain arms extended for 10 seconds), what is the mandatory '
                                                       'immediate action under Canadian regulatory standards?',
                                             'question_id': 'Q3',
                                             'title': '3. Canadian Red Flag & Stroke Triage Protocol'}],
        'patient': {   'age': 56,
                       'chief_complaint': 'Severe spinning dizziness and vertigo for 3 days, with ringing in the ears '
                                          'like roaring waves, throbbing temporal headaches, and irritability.',
                       'four_examinations': {   'auscultation_olfaction': 'Loud, resonant, irritable voice; sighs '
                                                                          'frequently.',
                                                'inquiry': 'Reports bitter taste in the mouth in the morning, dry '
                                                           'throat, constipation, and aching soreness in the lower '
                                                           'back and knees.',
                                                'inspection': 'Flushed face, injected bloodshot conjunctivae. Restless '
                                                              'motor posture. Tongue body is deep red, notably stiff '
                                                              'with red edges and a thin dry yellow coating.',
                                                'palpation': 'Pulse is Wiry (Xian), Rapid (Shuo), and Forceful (You '
                                                             'Li), especially prominent in the left Guan (Liver) '
                                                             'position, while the Chi (Kidney) position is thin.'},
                       'gender': 'Male',
                       'history': 'Episodes of dizziness have recurred over 2 years during stressful business '
                                  'negotiations. Patient feels as if the room is swaying beneath him. Aggravated by '
                                  'emotional frustration or sudden head turns. Blood pressure measured in clinic is '
                                  '172/104 mmHg. Reports insomnia and vivid dreams.',
                       'occupation': 'Small Business Owner'},
        'standard_diagnosis': {   'cardinal_points': ['LR3', 'GB20', 'TAIYANG', 'KD3', 'SP6', 'DU20'],
                                  'cautions': 'Sedate LR3 and GB20; tonify KD3 and SP6. CARB-TCMPA Red Flag Protocol: '
                                              'When a patient with severe vertigo has blood pressure >= 180/110 mmHg, '
                                              'or develops new focal neurological signs (facial asymmetry, limb '
                                              'weakness, pronator drift, dysarthria, or ataxia), the acupuncturist '
                                              'must immediately recognize impending stroke / hypertensive crisis and '
                                              'initiate emergency 911 referral.',
                                  'patterns': [   'Liver Yang Rising Transforming into Internal Wind (Gan Yang Shang '
                                                  'Kang)',
                                                  'Vertigo (Xuan Yun) with Underlying Kidney Yin Deficiency'],
                                  'synergies': [   'Wood drainer and Yuan-Source master (LR3 Taichong)',
                                                   'Major wind pool occipital regulator (GB20 Fengchi)',
                                                   'Water root tonic (KD3 Taixi)',
                                                   'Three Yin convergence (SP6)',
                                                   'Clear orifice pacifier (DU20 Baihui)'],
                                  'treatment_principles': [   'Subdue Liver Yang and Extinguish Internal Wind',
                                                              'Nourish Kidney and Liver Yin (Water nourishing Wood)',
                                                              'Clear Liver Fire and Settle the Head']},
        'title': 'Patient Intake: 56yo Male (Small Business Owner)'},
    {   'category': 'Gynecology & Obstetrics',
        'id': 'CASE-013',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** LU7 + KI6 opens the Ren Mai '
                                                                      'and Yin Qiao Mai (throat, chest, lung).',
                                                                 'B': '❌ **Incorrect:** SI3 + BL62 opens the Du Mai '
                                                                      'and Yang Qiao Mai (spine, back).',
                                                                 'C': '✅ **Correct (PC6 + SP4):** PC6 opens the Yin '
                                                                      'Wei Mai (commands interior chest and '
                                                                      'epigastrium) and SP4 opens the Chong Mai (Sea '
                                                                      'of Blood, which connects directly to the uterus '
                                                                      'and middle jiao). In pregnancy, Blood pools in '
                                                                      'the Chong Mai to nourish the fetus, causing '
                                                                      'Chong Mai Qi to rebel upwards into the Stomach. '
                                                                      'Combining PC6 and SP4 harmonizes Chong Mai and '
                                                                      'descends rebellious Stomach Qi (CAM, Deadman, '
                                                                      'Maciocia).',
                                                                 'D': '❌ **Incorrect:** SJ5 + GB41 opens the Dai Mai '
                                                                      '(outer cantus, hip).'},
                                             'options': [   'A. LU7 (Lieque) and KI6 (Zhaohai)',
                                                            'B. SI3 (Houxi) and BL62 (Shenmai)',
                                                            'C. PC6 (Neiguan) and SP4 (Gongsun)',
                                                            'D. SJ5 (Waiguan) and GB41 (Zulinqi)'],
                                             'prompt': 'Which classic pair of Eight Confluent Points (Ba Mai Jiao Hui '
                                                       'Xue) is the premier evidence-based choice for '
                                                       'pregnancy-related nausea and vomiting?',
                                             'question_id': 'Q1',
                                             'title': '1. Confluent Point Pair for Nausea & Chong Mai Rebellion'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** PC6, ST36, and gentle CV12 are '
                                                                      'standard safe points for treating morning '
                                                                      'sickness.',
                                                                 'B': '✅ **Correct (CARB-TCMPA Mandatory Safety '
                                                                      'Standard):** LI4 (strongly descends Qi), SP6 '
                                                                      '(Three Yin intersection, contracts uterus), '
                                                                      'BL60 (moves blood down), GB21 (descends Qi from '
                                                                      'shoulders to womb), BL67 (turns fetus), and '
                                                                      'lower abdominal/sacral points are strictly '
                                                                      'contraindicated in pregnancy. Needling them '
                                                                      'risks provoking uterine cramping, vaginal '
                                                                      'bleeding, or miscarriage (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** HT7 and DU20 are safe for '
                                                                      'calming anxiety.',
                                                                 'D': '❌ **Incorrect:** LU9 and KI3 are safe tonifying '
                                                                      'points.'},
                                             'options': [   'A. PC6 (Neiguan), ST36 (Zusanli), CV12 (Zhongwan)',
                                                            'B. LI4 (Hegu), SP6 (Sanyinjiao), BL60 (Kunlun), and GB21 '
                                                            '(Jianjing)',
                                                            'C. HT7 (Shenmen), Anmian, DU20 (Baihui)',
                                                            'D. LU9 (Taiyuan), KI3 (Taixi), SP9 (Yinlingquan)'],
                                             'prompt': 'Which group of acupuncture points is STRICTLY PROHIBITED '
                                                       '(Contraindicated) during pregnancy due to their potent action '
                                                       'of stimulating uterine contractions and inducing labor?',
                                             'question_id': 'Q2',
                                             'title': '2. Absolute Pregnancy Contraindications'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Food aversions are normal '
                                                                      'physiologic symptoms of pregnancy.',
                                                                 'B': '❌ **Incorrect:** Fatigue is common in early '
                                                                      'pregnancy.',
                                                                 'C': '✅ **Correct (Biomedical Safety Assessment):** '
                                                                      'Severe hyperemesis gravidarum causes '
                                                                      'intractable dehydration, hypokalemia, '
                                                                      'hyponatremia, and starvation ketosis, which can '
                                                                      "trigger cardiac arrhythmias or Wernicke's "
                                                                      'encephalopathy in the mother and growth '
                                                                      'restriction in the fetus. Immediate IV '
                                                                      'rehydration, electrolyte replacement, and '
                                                                      'medical monitoring are required (CARB-TCMPA '
                                                                      'candidate guide).',
                                                                 'D': '❌ **Incorrect:** Minor functional symptom.'},
                                             'options': [   'A. Mild food aversion to garlic and coffee.',
                                                            'B. Feeling sleepy after lunch.',
                                                            'C. Inability to retain fluids for over 24 hours, presence '
                                                            'of ketones in urine (ketonuria), postural '
                                                            'hypotension/tachycardia, and loss of skin turgor (severe '
                                                            'dehydration and electrolyte imbalance).',
                                                            'D. Belching after drinking peppermint tea.'],
                                             'prompt': 'What biomedical clinical sign indicates that a pregnant '
                                                       'patient with hyperemesis gravidarum requires immediate '
                                                       'transfer to an urgent care / emergency medical center?',
                                             'question_id': 'Q3',
                                             'title': '3. Biomedical Dehydration & Referral Criteria'}],
        'patient': {   'age': 28,
                       'chief_complaint': 'Severe persistent nausea, dry heaving, and vomiting 5-6 times daily in her '
                                          '8th week of pregnancy, unable to keep food or liquids down.',
                       'four_examinations': {   'auscultation_olfaction': 'Weak, low voice; frequent gagging sounds '
                                                                          'during history taking.',
                                                'inquiry': 'Urine output is decreased and dark yellow. Denies fever, '
                                                           'abdominal pain, or vaginal spotting. Sips of '
                                                           'room-temperature ginger water help slightly.',
                                                'inspection': 'Pale, dehydrated appearance with dry chapped lips. '
                                                              'Lying motionless on exam table. Tongue body is pale '
                                                              'with a thin, dry white coating.',
                                                'palpation': 'Skin turgor is mildly reduced. Epigastric palpation is '
                                                             'gentle and non-tender. Pulse is Slippery (Hua) and Rapid '
                                                             '(Shuo) in the Cun positions, but Weak (Ruo) in the '
                                                             'Guan/Chi positions.'},
                       'gender': 'Female',
                       'history': 'First pregnancy (primigravida). Nausea began 2 weeks ago and progressively '
                                  'worsened. Highly sensitive to food smells (especially coffee, meat, and garlic). '
                                  'Vomits clear sour liquid and bile. Reports profound fatigue, dizziness upon '
                                  'standing, and mild dry mouth.',
                       'occupation': 'Elementary School Teacher'},
        'standard_diagnosis': {   'cardinal_points': ['PC6', 'CV12', 'ST36', 'SP4'],
                                  'cautions': 'ABSOLUTE PREGNANCY CONTRAINDICATIONS: Under Canadian Clean Needle and '
                                              'safety regulations, points that strongly descend Qi, invigorate blood, '
                                              'or stimulate uterine contractions are STRICTLY FORBIDDEN during '
                                              'pregnancy: LI4 (Hegu), SP6 (Sanyinjiao), BL60 (Kunlun), GB21 '
                                              '(Jianjing), BL67 (Zhiyin), and lower abdominal/sacral points (CV3-CV7, '
                                              'BL27-BL34). Needling CV12 must be gentle and shallow (0.5 cun) without '
                                              'downward thrusting.',
                                  'patterns': [   'Morning Sickness / Hyperemesis Gravidarum (Ren Shen E Zu)',
                                                  'Stomach Qi Rebelling Upward due to Chong Mai Disharmony and Spleen '
                                                  'Deficiency'],
                                  'synergies': [   'Master nausea pair (PC6 Neiguan + SP4 Gongsun - Eight Confluent '
                                                   'Chong/Yinwei)',
                                                   'Front-Mu Stomach harmonizer (CV12 Zhongwan - gentle needle only)',
                                                   'Post-heaven replenisher (ST36 Zusanli)'],
                                  'treatment_principles': [   'Harmonize the Middle Jiao and Descend Rebellious '
                                                              'Stomach Qi',
                                                              'Strengthen Spleen and Settle Chong Mai',
                                                              'Stop Nausea and Vomiting']},
        'title': 'Patient Intake: 28yo Female (Elementary Teacher)'},
    {   'category': 'Internal Medicine',
        'id': 'CASE-014',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Damp-heat dysentery features '
                                                                      'tenesmus, burning anus, red/white bloody '
                                                                      'stools, and yellow greasy coat.',
                                                                 'B': '❌ **Incorrect:** Food stagnation diarrhea '
                                                                      'smells foul like rotten eggs and occurs after '
                                                                      'gluttony.',
                                                                 'C': '✅ **Correct (Wu Geng Xie):** At dawn (5:00 AM, '
                                                                      'the transition between Yin and Yang), primal '
                                                                      'Yang is at its nadir. When Mingmen Fire is '
                                                                      'deficient, it cannot warm Spleen Earth to '
                                                                      'transform food and fluids. The cold fluids '
                                                                      'plunge downward, creating acute morning watery '
                                                                      'diarrhea with undigested food (CAM & Maciocia).',
                                                                 'D': '❌ **Incorrect:** Liver-Spleen diarrhea occurs '
                                                                      'during bouts of anger or emotional stress.'},
                                             'options': [   'A. Damp-Heat Dysentery (Li Ji)',
                                                            'B. Food Stagnation Diarrhea',
                                                            'C. Daybreak / Cock-Crow Diarrhea (Wu Geng Xie) due to '
                                                            'Mingmen Fire failing to warm Spleen Earth',
                                                            'D. Liver Qi Stagnation invading the Spleen'],
                                             'prompt': 'Watery diarrhea occurring strictly at the fifth watch of the '
                                                       'night (5:00 AM dawn) with abdominal pain relieved by '
                                                       'defecation and cold extremities is classically known in TCM '
                                                       'as:',
                                             'question_id': 'Q1',
                                             'title': '1. Chronobiological Pattern Identification'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Heart Front-Mu and Back-Shu.',
                                                                 'B': '✅ **Correct:** ST25 (Tianshu) is the Front-Mu '
                                                                      'point of the Large Intestine, located 2 cun '
                                                                      'lateral to the umbilicus; it harmonizes and '
                                                                      'regulates bowel function. Pairing it with BL20 '
                                                                      '(Back-Shu of Spleen) and BL23 (Back-Shu of '
                                                                      'Kidney) executes the Mu-Shu combination to warm '
                                                                      'the root organs and treat the affected bowel '
                                                                      '(Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Lung Front-Mu and Back-Shu.',
                                                                 'D': '❌ **Incorrect:** Bladder Front-Mu and '
                                                                      'Back-Shu.'},
                                             'options': [   'A. CV14 (Juque) and BL15 (Xinshu)',
                                                            'B. ST25 (Tianshu) combined with BL20 (Pishu) and BL23 '
                                                            '(Shenshu)',
                                                            'C. LU1 (Zhongfu) and BL13 (Feishu)',
                                                            'D. CV3 (Zhongji) and BL28 (Pangguangshu)'],
                                             'prompt': 'Which combination of Front-Mu and Back-Shu points specifically '
                                                       'targets the large intestine while nourishing Spleen and Kidney '
                                                       'Yang?',
                                             'question_id': 'Q2',
                                             'title': '2. Front-Mu and Back-Shu Synergy for Intestinal Regulation'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Needling or burning CV8 '
                                                                      'directly is strictly prohibited (Deadman '
                                                                      'contraindications).',
                                                                 'B': '✅ **Correct (Indirect Salt Moxa on CV8):** CV8 '
                                                                      '(the umbilicus) is contraindicated to needle '
                                                                      'insertion! The classic standard is indirect '
                                                                      'salt moxibustion (Ge Yan Jiu): filling the '
                                                                      'navel level with salt and placing a slice of '
                                                                      'ginger with a burning moxa cone on top. This '
                                                                      'powerfully warms the lower abdomen, restores '
                                                                      'Mingmen Fire, and stops intractable chronic '
                                                                      'diarrhea (CAM & Deadman).',
                                                                 'C': '❌ **Incorrect:** Ice damages Yang.',
                                                                 'D': '❌ **Incorrect:** Not a valid modality.'},
                                             'options': [   'A. Direct scarring moxibustion that burns the skin.',
                                                            'B. Indirect Salt Moxibustion (filling the umbilicus with '
                                                            'clean salt and burning moxa cones on top of it or atop a '
                                                            'ginger slice).',
                                                            'C. Ice application over moxa ashes.',
                                                            'D. Wet needle technique with vinegar.'],
                                             'prompt': 'What classic moxibustion technique applied to CV8 (Shenque) is '
                                                       'famously indicated to rescue collapsed Yang, warm the '
                                                       'intestines, and stop chronic daybreak diarrhea?',
                                             'question_id': 'Q3',
                                             'title': '3. Moxibustion Modality on the Umbilicus'}],
        'patient': {   'age': 65,
                       'chief_complaint': 'Watery loose diarrhea occurring every single morning around 5:00 AM (at '
                                          'dawn), preceded by lower abdominal cramping and gurgling, completely '
                                          'relieved by defecation.',
                       'four_examinations': {   'auscultation_olfaction': 'Loud abdominal borborygmi (rumbling) '
                                                                          'audible prior to bowel movements; low quiet '
                                                                          'voice.',
                                                'inquiry': 'Lower back feels freezing cold like sitting on ice; '
                                                           'aversion to Canadian winter weather; stool contains '
                                                           'undigested food particles with no blood or mucus.',
                                                'inspection': 'Pale, withered complexion. Tongue body is pale, '
                                                              'swollen/enlarged with distinct scalloped teeth '
                                                              'impressions, covered in a thin wet slippery white coat.',
                                                'palpation': 'Lower abdomen is cool and relieved by firm warm '
                                                             'pressure. Pulse is Deep (Chen), Weak (Ruo), and Slow '
                                                             '(Chi), most markedly deficient in the Chi (Kidney) and '
                                                             'Guan (Spleen) positions.'},
                       'gender': 'Male',
                       'history': "Has suffered from this 'cock-crow diarrhea' (Wu Geng Xie) for 5 years. Wakes with a "
                                  'sudden urgency to evacuate. Accompanied by chronic dull aching in the lumbar spine, '
                                  'cold knees, cold feet in bed, poor appetite, and fatigue after meals. Urination is '
                                  'clear and frequent at night (nocturia 3 times).',
                       'occupation': 'Retired Accountant'},
        'standard_diagnosis': {   'cardinal_points': ['BL23', 'BL20', 'DU4', 'CV4', 'ST36', 'ST25'],
                                  'cautions': 'Tonification technique with heavy moxibustion (indirect salt '
                                              'moxibustion on CV8 Shenque or warm needles Wen Zhen on DU4 and BL23) is '
                                              'the primary textbook modality. Dispersing methods and cold-clearing '
                                              'herbs/points are strictly contraindicated.',
                                  'patterns': [   'Spleen and Kidney Yang Deficiency',
                                                  'Daybreak Diarrhea (Wu Geng Xie / Cock-Crow Diarrhea)'],
                                  'synergies': [   'Back-Shu Yang tonic pair (BL23 + BL20)',
                                                   'Mingmen Gate of Life igniter (DU4 with Moxa)',
                                                   'Front-Mu of Large Intestine regulator (ST25 Tianshu)',
                                                   'Original Qi reservoir (CV4 Guanyuan)',
                                                   'Post-Heaven support (ST36)'],
                                  'treatment_principles': [   'Warm and Tonify Kidney Yang',
                                                              'Strengthen Spleen Yang and Warm Mingmen',
                                                              'Astringe the Intestines and Check Diarrhea']},
        'title': 'Patient Intake: 65yo Male (Retired Accountant)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-015',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Hand Taiyin runs on the '
                                                                      'anterior radial border (LU5).',
                                                                 'B': '❌ **Incorrect:** Hand Shaoyin runs along the '
                                                                      'medial elbow (HT3).',
                                                                 'C': '✅ **Correct:** The Hand Yangming (Large '
                                                                      'Intestine) channel traverses the lateral aspect '
                                                                      'of the forearm and passes directly over the '
                                                                      'extensor muscle mass (LI10 Shousanli) and the '
                                                                      'lateral epicondylar depression (LI11 Quchi and '
                                                                      'LI12 Zhouliao). Tennis elbow is classically '
                                                                      'differentiated as Hand Yangming Tendon Bi (CAM '
                                                                      '& Deadman).',
                                                                 'D': '❌ **Incorrect:** Foot channel on the lower '
                                                                      'limb.'},
                                             'options': [   'A. Hand Taiyin (Lung Channel)',
                                                            'B. Hand Shaoyin (Heart Channel)',
                                                            'C. Hand Yangming (Large Intestine Channel)',
                                                            'D. Foot Jueyin (Liver Channel)'],
                                             'prompt': 'Pain located precisely at the lateral epicondyle of the '
                                                       'humerus along the extensor carpi radialis brevis muscle '
                                                       'corresponds directly to which primary acupuncture channel?',
                                             'question_id': 'Q1',
                                             'title': '1. Channel Differentiation & Orthopedic Correlation'},
                                         {   'correct_index': 0,
                                             'explanations': {   'A': "✅ **Correct (LI10 Shousanli):** LI10 ('Arm "
                                                                      "Three Miles') lies directly in the belly of the "
                                                                      'extensor carpi radialis longus and brevis '
                                                                      'muscles. Needling LI10 releases the tension on '
                                                                      'the common extensor tendon origin at the '
                                                                      'lateral epicondyle, dramatically relieving '
                                                                      'tennis elbow pain and restoring grip strength '
                                                                      '(Deadman & CAM).',
                                                                 'B': '❌ **Incorrect:** LI4 is distal on the hand.',
                                                                 'C': '❌ **Incorrect:** TE5 is on the posterior '
                                                                      'forearm between radius and ulna.',
                                                                 'D': '❌ **Incorrect:** LU7 is proximal to the radial '
                                                                      'styloid.'},
                                             'options': [   'A. LI10 (Shousanli)',
                                                            'B. LI4 (Hegu)',
                                                            'C. TE5 (Waiguan)',
                                                            'D. LU7 (Lieque)'],
                                             'prompt': 'Which point located 2 cun distal to LI11 on the line '
                                                       'connecting LI11 to LI5 is the premier point for relieving '
                                                       'forearm tension and extensor tendon strain?',
                                             'question_id': 'Q2',
                                             'title': '2. Point Selection & Empirical Muscular Point'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Deep 3-cun puncture risks '
                                                                      'nerve damage.',
                                                                 'B': '✅ **Correct (Radial Nerve Precautions):** The '
                                                                      'radial nerve branches into the superficial '
                                                                      'sensory and deep motor (posterior interosseous) '
                                                                      'branches adjacent to the radial head and '
                                                                      'supinator muscle. Overly deep or aggressive '
                                                                      'pistoning manipulation can cause neuritis, hand '
                                                                      'weakness (wrist drop / finger drop), or '
                                                                      'paresthesias. Safe needling depth is 0.5 to 1.0 '
                                                                      'cun (Deadman anatomical precautions).',
                                                                 'C': '❌ **Incorrect:** Moxa burns violate infection '
                                                                      'control standards.',
                                                                 'D': '❌ **Incorrect:** Dangerous.'},
                                             'options': [   'A. Insert needles perpendicularly 3 cun deep to touch '
                                                            'bone.',
                                                            'B. Avoid violent repeated pistoning into the radial '
                                                            'tunnel to prevent injuring the deep branch of the radial '
                                                            'nerve (posterior interosseous nerve).',
                                                            'C. Apply heavy moxibustion until second-degree burn '
                                                            'blisters form.',
                                                            'D. Electrify needles at 120 volts.'],
                                             'prompt': 'When needling around the lateral epicondyle and radial head, '
                                                       'what clinical precaution prevents iatrogenic nerve injury?',
                                             'question_id': 'Q3',
                                             'title': '3. Needling Technique & Radial Nerve Safety'}],
        'patient': {   'age': 45,
                       'chief_complaint': 'Sharp localized pain on the lateral aspect of his right elbow for 6 weeks, '
                                          'severely aggravated by turning screwdrivers or lifting heavy tools.',
                       'four_examinations': {   'auscultation_olfaction': 'Normal tone; reports frustration at not '
                                                                          'being able to work full shifts.',
                                                'inquiry': 'Pain is dull at rest, sharp and stabbing upon gripping or '
                                                           'turning doorknobs. Denies numbness in hand fingers.',
                                                'inspection': 'No gross redness or swelling, but patient holds right '
                                                              'arm in slight flexion to protect elbow. Tongue body is '
                                                              'slightly dusky on the margins with a thin white coat.',
                                                'palpation': 'Acute focal tenderness at the lateral epicondyle, LI11 '
                                                             '(Quchi), LI10 (Shousanli), and LI12 (Zhouliao). Pulse is '
                                                             'Wiry (Xian) and slightly Tight (Jin).'},
                       'gender': 'Male',
                       'history': 'Repetitive forearm pronation and wrist extension at work. Point tenderness over the '
                                  'common extensor tendon origin at the lateral epicondyle of the humerus. Pain '
                                  'radiates down the dorsolateral forearm. Cannot lift a coffee mug without sharp '
                                  "twinges. Cozen's test (resisted wrist extension with elbow extended) is strongly "
                                  'positive.',
                       'occupation': 'Master Electrician'},
        'standard_diagnosis': {   'cardinal_points': ['LI11', 'LI10', 'LI12', 'ASHIPOI', 'LI4', 'TE5'],
                                  'cautions': 'Avoid deep needle transfixion into the radial nerve trunk in the radial '
                                              'groove. When applying local electro-acupuncture, use comfortable '
                                              'low-frequency continuous or mixed frequency stimulation; avoid violent '
                                              'muscle tetany that could further tear degenerated common extensor '
                                              'tendon fibers.',
                                  'patterns': [   'Hand Yangming Channel Qi and Blood Stagnation',
                                                  'Tendon Bi Syndrome of the Elbow (Zhou Lao / Tennis Elbow)'],
                                  'synergies': [   'Local Yangming He-Sea and extensor mass pair (LI11 + LI10)',
                                                   'Olecranon fossa channel point (LI12)',
                                                   'Distal Yangming command master (LI4)',
                                                   'Focal tender Ashi trigger needling'],
                                  'treatment_principles': [   'Invigorate Blood and Dissolve Stasis',
                                                              'Unblock Hand Yangming Channel',
                                                              'Relax Tendons and Eliminate Pain',
                                                              'Nourish Local Sinews']},
        'title': 'Patient Intake: 45yo Male (Master Electrician)'},
    {   'category': 'Pain & Musculoskeletal',
        'id': 'CASE-016',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Yaotongxue is for acute lumbar '
                                                                      'sprain.',
                                                                 'B': '✅ **Correct (Luozhen with Dong Qi Technique):** '
                                                                      "Luozhen ('Stiff Neck') is located on the dorsum "
                                                                      'of the hand proximal to the 2nd and 3rd '
                                                                      'metacarpophalangeal joints. Strongly '
                                                                      'manipulating this distal point while having the '
                                                                      'patient actively rotate their neck recruits '
                                                                      'channel Qi, breaks reflexive protective muscle '
                                                                      'spasms, and dramatically restores cervical '
                                                                      'range of motion within minutes (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Baxie is for numbness and '
                                                                      'arthritis of the fingers.',
                                                                 'D': '❌ **Incorrect:** Sifeng is for childhood '
                                                                      'malnutrition/indigestion.'},
                                             'options': [   'A. Yaotongxue, needled while the patient bends their '
                                                            'lower back.',
                                                            'B. Luozhen, strongly manipulated while instructing the '
                                                            'patient to actively and gently rotate their stiff neck '
                                                            '(Dong Qi technique).',
                                                            'C. Baxie, bled with a three-edged needle.',
                                                            'D. Sifeng, pricked to express yellowish fluid.'],
                                             'prompt': 'Which Extra point on the dorsum of the hand between the 2nd '
                                                       'and 3rd metacarpal heads is the master empirical point for '
                                                       'stiff neck, and how is it manipulated?',
                                             'question_id': 'Q1',
                                             'title': '1. Distal Empirical Point & Dynamic Needling (Dong Qi)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** SI1 is Jing-Well for breast '
                                                                      'milk/fainting.',
                                                                 'B': '✅ **Correct (SI3 Houxi):** SI3 is the '
                                                                      'Shu-Stream Wood point of the Small Intestine '
                                                                      'channel and the Confluent point connecting to '
                                                                      'the Du Mai (Governor Vessel). It unblocks the '
                                                                      'entire posterior midline of the body, treats '
                                                                      'neck stiffness, occipital headache, and '
                                                                      'scapular spasms (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** SI6 is Xi-Cleft for elderly '
                                                                      'eye disorders.',
                                                                 'D': '❌ **Incorrect:** SI8 is He-Sea on the medial '
                                                                      'elbow.'},
                                             'options': [   'A. SI1 (Shaoze)',
                                                            'B. SI3 (Houxi)',
                                                            'C. SI6 (Yanglao)',
                                                            'D. SI8 (Xiaohai)'],
                                             'prompt': 'Which point on the Hand Taiyang (Small Intestine) channel is '
                                                       'the Shu-Stream and Confluent point of the Du Mai, governing '
                                                       'the spine and occiput?',
                                             'question_id': 'Q2',
                                             'title': '2. Confluent Point of Du Mai for Spine & Neck'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Brachial artery is in the '
                                                                      'upper arm, not upper trapezius.',
                                                                 'B': '✅ **Correct (CARB-TCMPA Pneumothorax Safety '
                                                                      'Standard):** The apical pleura and cupola of '
                                                                      'the lung rise superiorly through the thoracic '
                                                                      'inlet into the base of the neck, directly deep '
                                                                      'to the muscular belly of GB21. Perpendicular '
                                                                      'insertion over 0.8-1.0 cun in slender or '
                                                                      'asthenic patients penetrates straight into the '
                                                                      'lung parenchyma. Acupuncturists must pinch the '
                                                                      'muscle and needle horizontally/posteriorly '
                                                                      'across the muscle belly (Deadman anatomical '
                                                                      'warnings).',
                                                                 'C': '❌ **Incorrect:** Facial nerve is on the face.',
                                                                 'D': '❌ **Incorrect:** Thyroid is in the anterior '
                                                                      'neck.'},
                                             'options': [   'A. It risks puncturing the brachial artery.',
                                                            'B. The apex of the lung and cervical pleura lie '
                                                            'immediately beneath the trapezius muscle; deep '
                                                            'perpendicular puncture directly punctures the lung, '
                                                            'causing traumatic pneumothorax.',
                                                            'C. It permanently paralyses the facial nerve.',
                                                            'D. It damages the thyroid gland.'],
                                             'prompt': 'Why is perpendicular deep insertion at GB21 (Jianjing) '
                                                       'considered one of the highest clinical liabilities in '
                                                       'acupuncture?',
                                             'question_id': 'Q3',
                                             'title': '3. Pneumothorax Risk & Mandatory Safety Rule at GB21'}],
        'patient': {   'age': 31,
                       'chief_complaint': 'Acute inability to rotate neck to the left upon waking this morning, with '
                                          'severe spasming pain radiating from the left occiput to the shoulder.',
                       'four_examinations': {   'auscultation_olfaction': 'Wincing when asked to gently turn head.',
                                                'inquiry': 'Reports feeling cold draft in the neck overnight; denies '
                                                           'numbness or tingling in the upper limbs; denies fever.',
                                                'inspection': 'Head is held in an antalgic position: tilted slightly '
                                                              'to the left with chin rotated to the right to minimize '
                                                              'muscle stretch. Tongue body is normal pink with a thin '
                                                              'white coat.',
                                                'palpation': 'Severe hypertonicity and acute tender trigger points '
                                                             'palpable along the left upper trapezius (GB21), levator '
                                                             'scapulae, and occipital margin (GB20). Pulse is Wiry '
                                                             '(Xian) and Tight (Jin).'},
                       'gender': 'Female',
                       'history': 'Slept with an open window directly facing her bed on a cold autumn night with her '
                                  'head propped awkwardly on two high pillows. Woke up unable to check her car blind '
                                  'spot. Turning head to the left causes severe sharp spasms in the left levator '
                                  'scapulae and trapezius muscles.',
                       'occupation': 'Graphic Designer'},
        'standard_diagnosis': {   'cardinal_points': ['LUOZHEN', 'SI3', 'GB20', 'GB21', 'ASHIPOI'],
                                  'cautions': 'CRITICAL ANATOMICAL WARNING AT GB21 (JIANJING): The apex of the lung '
                                              'and cupola of the pleura rise 1 to 2 cm above the medial third of the '
                                              'clavicle immediately beneath GB21. Perpendicular deep insertion is the '
                                              'SINGLE MOST FREQUENT CAUSE OF PNEUMOTHORAX in clinical practice. '
                                              'Puncture must be strictly posterior-oblique 0.5-0.8 cun hugging '
                                              'muscular tissue. Perpendicular deep puncture is strictly prohibited.',
                                  'patterns': [   'Acute Stiff Neck (Luo Zhen / Torticollis)',
                                                  'Wind-Cold and Qi Stagnation in Taiyang and Shaoyang Channels'],
                                  'synergies': [   'Premier empirical stiff neck hand point (Luozhen with Dong Qi '
                                                   'active movement)',
                                                   'Confluent point of Du Mai (SI3 Houxi)',
                                                   'Major cervical wind gate (GB20 Fengchi)',
                                                   'Local shoulder muscle relaxer (GB21 Jianjing)'],
                                  'treatment_principles': [   'Dispel Wind and Disperse Cold',
                                                              'Activate Qi and Relax Tendons',
                                                              'Unblock Neck Channels and Restore Cervical Mobility']},
        'title': 'Patient Intake: 31yo Female (Graphic Designer)'},
    {   'category': 'Dermatology & External',
        'id': 'CASE-017',
        'multiple_choice_questions': [   {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Eczema presents with dry, '
                                                                      'lichenified, scaly patches without dermatomal '
                                                                      'vesicular bands.',
                                                                 'B': '❌ **Incorrect:** Psoriasis presents with '
                                                                      'silver-scaled plaques.',
                                                                 'C': '✅ **Correct:** Herpes zoster is classically '
                                                                      "named 'Coiling Waist Fire Toxin' (Chan Yao Huo "
                                                                      "Dan) or 'Snake String Sore' (She Chuan Cang). "
                                                                      'When Liver and Gallbladder Damp-Heat transforms '
                                                                      'into toxic Fire, it flares outward into the '
                                                                      'Shaoyang channels and skin, creating agonizing '
                                                                      'burning pain and fluid-filled blisters (CAM & '
                                                                      'Maciocia).',
                                                                 'D': '❌ **Incorrect:** Urticaria presents with '
                                                                      'transient wheals.'},
                                             'options': [   'A. Eczema due to Blood Deficiency Wind-Dryness',
                                                            'B. Psoriasis due to Blood Cold',
                                                            'C. Herpes Zoster (Chan Yao Huo Dan / Snake String Sore) '
                                                            'due to Damp-Heat Fire Blazing in the Liver and '
                                                            'Gallbladder Channels',
                                                            'D. Urticaria due to Exterior Wind-Cold'],
                                             'prompt': 'Unilateral band of burning vesicular eruptions along the '
                                                       'hypochondrium with red tongue, yellow greasy coat, and '
                                                       'wiry-rapid pulse corresponds to which classic disease and '
                                                       'pattern?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation & Classic TCM Disease Name'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Puncturing into vesicles '
                                                                      'breaches the epidermal barrier, causing '
                                                                      'secondary staphylococcal infection and viral '
                                                                      'spread.',
                                                                 'B': "✅ **Correct (Weici Technique):** 'Surrounding "
                                                                      "the Dragon' (Weici) is the gold standard "
                                                                      'clinical technique described in Deadman and '
                                                                      'CAM: fine needles are placed in healthy skin '
                                                                      'around the perimeter of the herpes rash, angled '
                                                                      'obliquely inward toward the lesion center, '
                                                                      "especially pinning the advancing 'head' and "
                                                                      "'tail' of the eruption. This cuts off local "
                                                                      'heat toxin and relieves neuropathic tension.',
                                                                 'C': '❌ **Incorrect:** Direct moxibustion on '
                                                                      'vesicular burns risks severe blistering and '
                                                                      'infection.',
                                                                 'D': '❌ **Incorrect:** Irrelevant.'},
                                             'options': [   'A. Puncturing perpendicularly directly into the center of '
                                                            'each fluid blister.',
                                                            'B. Inserting 4 to 8 fine needles obliquely (at 15-30 '
                                                            'degrees) into healthy skin 0.5 - 1.0 cm outside the '
                                                            'perimeter of the eruption, directing the needle tips '
                                                            'towards the center and base of the lesion, with special '
                                                            "needles at the 'head' and 'tail' of the rash.",
                                                            'C. Applying intense moxibustion until the vesicles pop.',
                                                            'D. Bleeding the soles of both feet.'],
                                             'prompt': 'What is the proper method for executing the classic '
                                                       "'Surrounding the Dragon' (Weici / 围刺) needling technique for "
                                                       'localized herpes zoster lesions?',
                                             'question_id': 'Q2',
                                             'title': "2. Classic 'Surrounding the Dragon' (Weici) Technique"},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Delaying evaluation for herpes '
                                                                      'zoster ophthalmicus can result in permanent '
                                                                      'loss of sight.',
                                                                 'B': '✅ **Correct (Ophthalmic Red Flag):** Vesicles '
                                                                      'on the tip of the nose indicate involvement of '
                                                                      'the nasociliary branch of the ophthalmic nerve '
                                                                      "(V1 - Hutchinson's sign). This has a >75% "
                                                                      'correlation with serious intraocular '
                                                                      'involvement (keratitis, anterior uveitis, '
                                                                      'glaucoma, and corneal ulceration/blindness). '
                                                                      'Immediate emergency medical/ophthalmological '
                                                                      'referral for systemic antiviral therapy is '
                                                                      'mandatory under Canadian regulatory '
                                                                      'competencies.',
                                                                 'C': '❌ **Incorrect:** Inappropriate and dangerous.',
                                                                 'D': '❌ **Incorrect:** Plum blossom needling on an '
                                                                      'eyelid risks eye perforation.'},
                                             'options': [   'A. Reassure the patient and schedule a follow-up in 2 '
                                                            'weeks.',
                                                            'B. Urgent same-day ophthalmological referral to evaluate '
                                                            'for Herpes Zoster Ophthalmicus and prevent corneal '
                                                            'perforation / permanent blindness.',
                                                            'C. Tell the patient to wash the eye with cold tap water.',
                                                            'D. Apply plum blossom needle directly to the upper '
                                                            'eyelid.'],
                                             'prompt': 'If a patient with herpes zoster presents with vesicles '
                                                       'extending to the forehead, upper eyelid, and the tip or side '
                                                       "of the nose (Hutchinson's sign), what emergency medical "
                                                       'referral is required?',
                                             'question_id': 'Q3',
                                             'title': "3. Ophthalmic Emergency Red Flag (Hutchinson's Sign)"}],
        'patient': {   'age': 61,
                       'chief_complaint': 'Excruciating burning, stabbing neuropathic pain along the right flank and '
                                          'chest for 4 days, followed by an outbreak of clustered blistering red '
                                          'vesicles.',
                       'four_examinations': {   'auscultation_olfaction': 'Rapid breathing; groaning when clothing '
                                                                          'brushes against the affected skin.',
                                                'inquiry': 'Reports severe allodynia (touching skin with a cotton '
                                                           'shirt feels like boiling oil); bitter taste in mouth; '
                                                           'constipation.',
                                                'inspection': 'Agitated, tearful expression. Unilateral band-like '
                                                              'erythematous rash with clustered vesicular eruptions '
                                                              "(Herpes Zoster / 'Snake String Sore' She Chuan Cang). "
                                                              'Tongue body is red with a thick yellow greasy coating.',
                                                'palpation': 'Extreme hypersensitivity to touch over right T5-T6 '
                                                             'dermatome. Pulse is Wiry (Xian), Slippery (Hua), and '
                                                             'Rapid (Shuo).'},
                       'gender': 'Female',
                       'history': 'Pain preceded the skin rash by 3 days, initially mistaken for pleurisy. Eruption is '
                                  'strictly unilateral, wrapping around the right T5-T6 dermatome from the spine to '
                                  'the sternum. Clusters of tense, clear-fluid filled vesicles on an erythematous '
                                  'base. Low-grade fever, restlessness, dark concentrated urine.',
                       'occupation': 'Retired Nurse'},
        'standard_diagnosis': {   'cardinal_points': ['JIAJI', 'LI11', 'LR2', 'GB34', 'ASHIPOI', 'SP10'],
                                  'cautions': 'Clean Needle Technique & Infection Control: Herpes zoster vesicles '
                                              'contain active varicella-zoster virus (VZV). NEVER insert needles '
                                              'directly through intact vesicles to avoid secondary bacterial infection '
                                              'or viral inoculation. Wear disposable gloves. Dispose of all needles '
                                              'immediately in biohazard sharps containers. If rash involves the '
                                              "ophthalmic branch of trigeminal nerve (V1 - tip of nose / Hutchinson's "
                                              'sign), immediate ophthalmological ER referral is required to prevent '
                                              'corneal blindness.',
                                  'patterns': [   'Damp-Heat and Toxic Fire Blazing in Liver and Gallbladder Channels '
                                                  '(Gan Dan Shi Re)',
                                                  'Herpes Zoster / Shingles (Chan Yao Huo Dan / She Chuan Cang)'],
                                  'synergies': [   'Segmental spinal nerve regulation (Huatuo Jiaji at T5-T6 levels)',
                                                   'Surrounding the Dragon peripheral ring technique (Weici around the '
                                                   'head and tail of rash)',
                                                   'Fire clearing master (LI11 Quchi)',
                                                   'Liver fire drainer (LR2 Xingjian)',
                                                   'He-Sea Shaoyang opener (GB34)'],
                                  'treatment_principles': [   'Clear Heat and Drain Fire',
                                                              'Dispel Dampness and Purge Toxic Heat',
                                                              'Invigorate Blood and Stop Severe Neuropathic Pain']},
        'title': 'Patient Intake: 61yo Female (Retired Nurse)'},
    {   'category': 'Internal Medicine',
        'id': 'CASE-018',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Inverted definitions.',
                                                                 'B': '✅ **Correct:** Classic San Xiao framework: '
                                                                      'Upper Xiao (Shang Xiao - Lung) is characterized '
                                                                      'by excessive polydipsia (thirst); Middle Xiao '
                                                                      '(Zhong Xiao - Stomach) is characterized by '
                                                                      'polyphagia with emaciation (hunger); Lower Xiao '
                                                                      '(Xia Xiao - Kidney) is characterized by '
                                                                      'polyuria with turbid urine and lumbar '
                                                                      'exhaustion (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Middle Xiao is Stomach/Spleen.',
                                                                 'D': '❌ **Incorrect:** Lower Xiao is Kidney/Bladder.'},
                                             'options': [   'A. Upper Xiao: Excessive urination; Lower Xiao: Excessive '
                                                            'thirst.',
                                                            'B. Upper Xiao: Extreme thirst (Lung Heat); Middle Xiao: '
                                                            'Voracious hunger with emaciation (Stomach Heat); Lower '
                                                            'Xiao: Copious turbid urine with lumbar soreness (Kidney '
                                                            'Yin/Yang Deficiency).',
                                                            'C. Middle Xiao is caused by Heart Fire.',
                                                            'D. Lower Xiao presents only with cough.'],
                                             'prompt': 'In the classic TCM differentiation of Xiao Ke (Wasting and '
                                                       'Thirsting), which clinical sign specifically distinguishes '
                                                       "'Middle Jiao Xiao Ke' (Zhong Xiao) from Upper and Lower Xiao?",
                                             'question_id': 'Q1',
                                             'title': '1. Three Wasting Stages (San Xiao) Differentiation'},
                                         {   'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Pishu is at T11.',
                                                                 'B': '❌ **Incorrect:** Weishu is at T12.',
                                                                 'C': '✅ **Correct (Yishu / Weiguanxiashu):** Yishu '
                                                                      "('Pancreas Shu') is situated at T8, between "
                                                                      'Feishu (T7) and Ganshu (T9). Modern and '
                                                                      'classical TCM practice recognizes Yishu as the '
                                                                      'dedicated empirical acupuncture point to '
                                                                      'stimulate pancreatic islet function, regulate '
                                                                      'blood sugar, and alleviate Xiao Ke symptoms '
                                                                      '(Deadman & CAM).',
                                                                 'D': '❌ **Incorrect:** Shenshu is at L2.'},
                                             'options': [   'A. Pishu (BL20)',
                                                            'B. Weishu (BL21)',
                                                            'C. Yishu (also known as Weiguanxiashu)',
                                                            'D. Shenshu (BL23)'],
                                             'prompt': 'Which Extra point located 1.5 cun lateral to the lower border '
                                                       'of the spinous process of the 8th thoracic vertebra (T8) is '
                                                       'the premier empirical point for diabetes and pancreatic '
                                                       'regulation?',
                                             'question_id': 'Q2',
                                             'title': '2. Empirical Pancreatic Extra Point (Yishu)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Diabetes is not a primary '
                                                                      'coagulation factor deficiency like hemophilia.',
                                                                 'B': '✅ **Correct (Diabetic Safety Protocol):** Loss '
                                                                      'of protective sensation means the patient '
                                                                      'cannot feel excessive heat from moxa or tissue '
                                                                      'trauma from large-gauge needles. Impaired white '
                                                                      'blood cell chemotaxis and microvascular disease '
                                                                      'hinder wound repair. A burn or micro-infection '
                                                                      'can rapidly escalate to deep tissue necrosis, '
                                                                      'requiring surgical amputation (CARB-TCMPA '
                                                                      'safety guidelines).',
                                                                 'C': '❌ **Incorrect:** Acupuncture does not cause '
                                                                      'catastrophic sudden hypoglycemia.',
                                                                 'D': '❌ **Incorrect:** Absurd.'},
                                             'options': [   'A. Because diabetic patients bleed excessively like '
                                                            'hemophiliacs.',
                                                            'B. Because diabetic microangiopathy and peripheral '
                                                            'sensory neuropathy result in blunted pain/heat perception '
                                                            'and poor tissue perfusion, where even minor burns or '
                                                            'needle punctures can progress into non-healing chronic '
                                                            'diabetic foot ulcers, secondary osteomyelitis, and '
                                                            'gangrene.',
                                                            'C. Because foot points cause instantaneous hypoglycemia.',
                                                            'D. Because foot needles break under high blood sugar '
                                                            'levels.'],
                                             'prompt': 'Why must an acupuncturist exercise extreme caution and avoid '
                                                       'heavy moxibustion or aggressive distal needling on the feet of '
                                                       'a diabetic patient?',
                                             'question_id': 'Q3',
                                             'title': '3. Diabetic Foot Ulcer & Infection Risk'}],
        'patient': {   'age': 52,
                       'chief_complaint': 'Excessive relentless hunger (eating 5 large meals daily), yet losing 15 lbs '
                                          'over 3 months, accompanied by extreme thirst and drinking 4-5 liters of ice '
                                          'water daily.',
                       'four_examinations': {   'auscultation_olfaction': 'Loud voice, distinct foul halitosis (bad '
                                                                          'breath) noticeable during interview.',
                                                'inquiry': "Reports voracious appetite ('eating like a wolf'), "
                                                           'polyuria (frequent copious urination), and fatigue despite '
                                                           'eating heavily.',
                                                'inspection': 'Thinning limbs with abdominal adiposity. Flushed '
                                                              'complexion. Tongue body is red, dry, with a thick dry '
                                                              'rough yellow coating and cracked surface in the central '
                                                              'Stomach area.',
                                                'palpation': 'Pulse is Slippery (Hua), Rapid (Shuo), and Forceful (You '
                                                             'Li), particularly robust in the right Guan '
                                                             '(Stomach/Spleen) position.'},
                       'gender': 'Male',
                       'history': 'Long history of consuming hamburgers, french fries, sweet sodas, and staying '
                                  'sedentary. Reports dry mouth, cracked lips, foul breath, and passing hard dry '
                                  'stools once every 3-4 days. Fasting blood glucose measured in medical clinic is '
                                  '11.4 mmol/L (HbA1c: 9.2%).',
                       'occupation': 'Long-Haul Truck Driver'},
        'standard_diagnosis': {   'cardinal_points': ['ST44', 'ST36', 'CV12', 'SP6', 'BL21', 'YISHU'],
                                  'cautions': 'DIABETIC COMPLICATION SAFETY: Diabetic patients frequently suffer from '
                                              'peripheral neuropathy (loss of protective pain and thermal sensation) '
                                              'and peripheral arterial disease (poor microcirculation). Under '
                                              "CARB-TCMPA safety standards: inspect the patient's feet for "
                                              'pre-existing ulcers before treatment; avoid aggressive needle retention '
                                              'on feet/toes if severe neuropathy is present; avoid burning moxibustion '
                                              'directly on diabetic feet due to impaired healing and gangrene risk.',
                                  'patterns': [   'Middle Jiao Xiao Ke / Wasting and Thirsting (Zhong Xiao)',
                                                  'Stomach Heat Blazing with Yin Fluid Consumption (Wei Re Chi Sheng)'],
                                  'synergies': [   'Water/Spring point to clear Stomach fire (ST44 Neiting)',
                                                   'Empirical pancreatic Back-Shu point (Yishu / Weiguanxiashu)',
                                                   'Front-Mu Stomach balancer (CV12)',
                                                   'Three Yin fluid generator (SP6)',
                                                   'Back-Shu of Stomach (BL21)'],
                                  'treatment_principles': [   'Clear Stomach Heat and Drain Fire',
                                                              'Nourish Stomach and Spleen Yin',
                                                              'Promote Body Fluids and Relieve Thirst']},
        'title': 'Patient Intake: 52yo Male (Long-Haul Driver)'},
    {   'category': 'Neurological & Sensory',
        'id': 'CASE-019',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** V1 supplies the forehead, '
                                                                      'upper eyelid, and eye.',
                                                                 'B': '✅ **Correct:** The maxillary division (V2) of '
                                                                      'the trigeminal nerve exits the infraorbital '
                                                                      'foramen (at ST2 Sibai) and innervates the lower '
                                                                      'eyelid, cheek, upper lip, and maxillary teeth. '
                                                                      'This follows the precise anatomical trajectory '
                                                                      'of the Foot Yangming (Stomach) channel across '
                                                                      'the face (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** V3 supplies the lower jaw and '
                                                                      'chin.',
                                                                 'D': '❌ **Incorrect:** Facial nerve is motor (mimetic '
                                                                      'muscles), while trigeminal nerve is sensory '
                                                                      '(pain transmission).'},
                                             'options': [   'A. Ophthalmic division (V1) - Foot Taiyang Channel',
                                                            'B. Maxillary division (V2) - Foot Yangming (Stomach) '
                                                            'Channel',
                                                            'C. Mandibular division (V3) - Foot Jueyin Channel',
                                                            'D. Facial Nerve motor branch - Hand Taiyin Channel'],
                                             'prompt': 'Severe electric shock-like paroxysmal pain affecting the right '
                                                       'upper lip, nasolabial fold, and cheek corresponds to which '
                                                       'cranial nerve branch and TCM channel?',
                                             'question_id': 'Q1',
                                             'title': '1. Cranial Nerve & Channel Anatomy'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Mechanical agitation of '
                                                                      'trigger zones precipitates agonizing, '
                                                                      'protracted lancinating spasms.',
                                                                 'B': '✅ **Correct (Clinical Needling Strategy):** In '
                                                                      'trigeminal neuralgia, the primary therapeutic '
                                                                      'heavy lifting must be done distally via the '
                                                                      'Four Gates (LI4 + LR3) and the Ying-Spring fire '
                                                                      'point (ST44) to drain systemic wind-fire. Local '
                                                                      'needles at ST2 or ST7 should be inserted with '
                                                                      'minimal trauma and retained quietly without '
                                                                      'vigorous manipulation (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Direct moxa on the lip causes '
                                                                      'burns and fires.',
                                                                 'D': '❌ **Incorrect:** Earlobe bleeding does not '
                                                                      'address V2 neuralgia.'},
                                             'options': [   'A. Apply strong violent pistoning and electro-acupuncture '
                                                            'directly on the trigger point to destroy the nerve.',
                                                            'B. Heavily sedate distal points (LI4, LR3, ST44) to draw '
                                                            'fire downward, while keeping local facial needle '
                                                            'insertion gentle, shallow, and without heavy manual '
                                                            'manipulation to avoid triggering paroxysms.',
                                                            'C. Burn direct moxa cones on the upper lip.',
                                                            "D. Bleed the patient's earlobe until 100 drops of blood "
                                                            'are released.'],
                                             'prompt': 'How should an acupuncturist manipulate local facial points '
                                                       'located near trigger zones during an acute trigeminal '
                                                       'neuralgia attack?',
                                             'question_id': 'Q2',
                                             'title': '2. Local Trigger Point Manipulation Strategy'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Femoral vein is in the groin.',
                                                                 'B': '✅ **Correct (ST7 Depth Precaution):** ST7 lies '
                                                                      'directly over the masseter muscle and the '
                                                                      'mandibular notch. Deep to the mandibular notch '
                                                                      'in the infratemporal fossa lies the maxillary '
                                                                      'artery and the dense pterygoid venous plexus. '
                                                                      'Inserting deeper than 1.0-1.2 cun can puncture '
                                                                      'these vascular structures, causing deep '
                                                                      'infratemporal hematoma and severe jaw trismus '
                                                                      '(Deadman precautions).',
                                                                 'C': '❌ **Incorrect:** Optic nerve is within the '
                                                                      'orbit.',
                                                                 'D': '❌ **Incorrect:** Spinal cord is inside the '
                                                                      'vertebral canal.'},
                                             'options': [   'A. The femoral vein.',
                                                            'B. The maxillary artery and deep pterygoid venous plexus.',
                                                            'C. The optic nerve.',
                                                            'D. The spinal cord.'],
                                             'prompt': 'When needling ST7 (Xiaguan, in the depression between the '
                                                       'zygomatic arch and the mandibular notch), what structure must '
                                                       'be avoided by not inserting beyond 1.0 - 1.2 cun deep?',
                                             'question_id': 'Q3',
                                             'title': '3. Anatomical Depth & Vessel Caution at ST7 (Xiaguan)'}],
        'patient': {   'age': 55,
                       'chief_complaint': 'Paroxysms of excruciating, lancinating electric-shock like facial pain on '
                                          'the right cheek and upper lip, lasting 10-30 seconds per attack.',
                       'four_examinations': {   'auscultation_olfaction': 'Speaks very slowly through closed lips to '
                                                                          'avoid moving facial muscles.',
                                                'inquiry': 'Reports feeling like lightning strikes or hot needles '
                                                           'stabbed into her upper jaw and cheek. Irritable, poor '
                                                           'sleep, dry mouth, constipation.',
                                                'inspection': 'Terrified, guarded facial expression. Avoids speaking '
                                                              'or moving right side of mouth. Tongue body is red with '
                                                              'a thin yellow coating, slightly dryer in the center.',
                                                'palpation': "Trigger point ('trigger zone') hyperesthesia over right "
                                                             'Sibai (ST2) and Xiaguan (ST7). Pulse is Wiry (Xian) and '
                                                             'Rapid (Shuo).'},
                       'gender': 'Female',
                       'history': 'Pain began 4 months ago. Attacks are triggered instantly by brushing teeth, chewing '
                                  'food, washing face with cold water, or even a light breeze touching her right '
                                  'nasolabial fold (trigger zone in V2 maxillary nerve branch). Patient covers her '
                                  'face with a scarf and has avoided brushing her teeth for 4 days out of terror of '
                                  'triggering an attack.',
                       'occupation': 'Bank Teller'},
        'standard_diagnosis': {   'cardinal_points': ['ST2', 'ST7', 'LI4', 'LR3', 'GB20', 'ST44'],
                                  'cautions': 'CRITICAL NEEDLING TECHNIQUE AT TRIGGER POINTS: Directly manipulating '
                                              'needles aggressively at local trigger points (e.g. ST2) can trigger '
                                              'severe paroxysmal attacks. During the acute paroxysmal phase, apply '
                                              'heavy reducing manipulation to DISTAL points (LI4, LR3, ST44) first, '
                                              'and keep local facial needles (ST2, ST7) extremely light, shallow, and '
                                              'non-manipulated (or use gentle retention without lifting/thrusting). At '
                                              'ST7 (Xiaguan), insert perpendicularly 0.5-1.0 cun; deep insertion over '
                                              '1.5 cun risks penetrating the maxillary artery.',
                                  'patterns': [   'Stomach Fire and Wind-Heat Attacking Facial Yangming Channels',
                                                  'Trigeminal Neuralgia / Facial Pain (Mian Tong)'],
                                  'synergies': [   'Distal Four Gates pair (LI4 + LR3 - heavily sedated)',
                                                   'Local Yangming infraorbital master (ST2 Sibai)',
                                                   'Mandibular notch channel joint (ST7 Xiaguan)',
                                                   'Water-Spring Stomach fire cooler (ST44)',
                                                   'Major wind queller (GB20)'],
                                  'treatment_principles': [   'Purge Stomach Fire and Clear Facial Heat',
                                                              'Extinguish Wind and Relieve Spasms',
                                                              'Unblock Yangming and Shaoyang Collaterals',
                                                              'Stop Paroxysmal Facial Pain']},
        'title': 'Patient Intake: 55yo Female (Bank Teller)'},
    {   'category': 'Neurological & Sensory',
        'id': 'CASE-020',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Liver fire presents with red '
                                                                      'face, irritability, loud voice, and wiry-rapid '
                                                                      'pulse.',
                                                                 'B': "✅ **Correct:** 'Qi is the commander of Blood; "
                                                                      'when Qi is deficient, it cannot push Blood '
                                                                      "through the micro-collaterals.' Qi deficiency "
                                                                      'leads to spontaneous sweating and fatigue, '
                                                                      'while stagnant Blood produces dusky purple '
                                                                      'tongue, choppy pulse, and flaccid/spastic limb '
                                                                      'paralysis (CAM, Maciocia). This is the hallmark '
                                                                      "pattern described in Wang Qingren's Yi Lin Gai "
                                                                      'Cuo.',
                                                                 'C': '❌ **Incorrect:** Wind-Cold is an acute exterior '
                                                                      'pattern.',
                                                                 'D': '❌ **Incorrect:** Spleen collapse presents with '
                                                                      'shock and prolapse.'},
                                             'options': [   'A. Liver Fire Blazing with Phlegm-Heat',
                                                            'B. Qi Deficiency and Blood Stasis (Qi Xu Xue Yu) failing '
                                                            'to unblock the channels',
                                                            'C. Wind-Cold Invading the Taiyang Channel',
                                                            'D. Spleen Yang Collapse'],
                                             'prompt': 'Hemiplegia accompanied by spontaneous sweating, pale dusky '
                                                       'purple tongue, mental fatigue, and a thready-choppy pulse '
                                                       'represents which classic pattern of stroke recovery?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation in Stroke Recovery'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Ipsilateral needling is '
                                                                      'incorrect for pyramidal tract decussation; '
                                                                      'middle 2/5 represents the upper limb.',
                                                                 'B': '✅ **Correct (Scalp Motor Area):** Corticospinal '
                                                                      'fibers decussate in the medulla; therefore, '
                                                                      'left cerebral lesions produce right-sided motor '
                                                                      "deficit. In Jiao's system, the Motor Area runs "
                                                                      'from Qianshencong to Xuanli. The upper 1/5 '
                                                                      'controls the contralateral lower limb and '
                                                                      'trunk; the middle 2/5 controls the '
                                                                      'contralateral upper limb; the lower 2/5 '
                                                                      'controls the face and speech (CAM & Deadman).',
                                                                 'C': '❌ **Incorrect:** Sensory area is for numbness, '
                                                                      'not motor power.',
                                                                 'D': '❌ **Incorrect:** Chorea-tremor area is for '
                                                                      "Parkinson's or chorea."},
                                             'options': [   'A. Right Motor Area - middle 2/5',
                                                            'B. Left (Contralateral) Motor Area - upper 1/5 of the '
                                                            'line',
                                                            'C. Bilateral Sensory Area - lower 2/5',
                                                            'D. Contralateral Chorea-Tremor Area only'],
                                             'prompt': "In Jiao Shunfa's scalp acupuncture system for right-sided "
                                                       'hemiplegia, which side and segment of the Motor Area must be '
                                                       'treated for the right lower limb?',
                                             'question_id': 'Q2',
                                             'title': "2. Scalp Acupuncture (Jiao's System) Motor Area Mapping"},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Perpendicular insertion into '
                                                                      'adult cranial bone is impossible and painful.',
                                                                 'B': '✅ **Correct (CARB-TCMPA Scalp Needling '
                                                                      'Standards):** The needle must enter at a '
                                                                      '30-degree angle to slip into the loose areolar '
                                                                      'connective tissue beneath the epicranial '
                                                                      'aponeurosis. Because the scalp is richly '
                                                                      'supplied by anastomosing branches of the '
                                                                      'external and internal carotid arteries, '
                                                                      'bleeding upon removal is common; firm pressure '
                                                                      'with sterile cotton for 30-60 seconds prevents '
                                                                      'large, unsightly subcutaneous hematomas '
                                                                      '(Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Dangerous and impossible in '
                                                                      'adults.',
                                                                 'D': '❌ **Incorrect:** Violates basic safety.'},
                                             'options': [   'A. Perpendicular 1.0 cun into the cranial bone sutures.',
                                                            'B. Insert at approximately 30 degrees to the scalp into '
                                                            'the loose subaponeurotic layer beneath the galea '
                                                            'aponeurotica, advance 1.0 - 1.5 cun; upon withdrawal, '
                                                            'compress the site firmly with a sterile cotton ball to '
                                                            'prevent subcutaneous scalp hematoma.',
                                                            'C. Insert needles through the fontanelles into brain '
                                                            'parenchyma.',
                                                            'D. Retain needles without touching for 3 days.'],
                                             'prompt': 'What is the proper insertion angle, layer, and post-removal '
                                                       'protocol for scalp acupuncture?',
                                             'question_id': 'Q3',
                                             'title': '3. Scalp Needling Depth & Hematoma Prevention'}],
        'patient': {   'age': 68,
                       'chief_complaint': 'Right-sided upper and lower limb weakness, spasticity in right arm, and '
                                          'difficulty walking 5 months following an ischemic stroke.',
                       'four_examinations': {   'auscultation_olfaction': 'Speech is hesitant and low-volume, but '
                                                                          'clear.',
                                                'inquiry': 'Reports numbness in right fingers and toes; feels weak and '
                                                           'depleted; bowel movements are sluggish without dry stool.',
                                                'inspection': 'Slow, circumducting gait with cane. Right arm carried '
                                                              'in flexed position. Tongue body is pale, dusky purple '
                                                              'with teeth marks and a thin white coating.',
                                                'palpation': 'Increased muscle tone (Ashworth scale 2) in right biceps '
                                                             'and wrist flexors. Pulse is Thready (Xi), Weak (Ruo), '
                                                             'and Choppy/Hesitant (Se).'},
                       'gender': 'Male',
                       'history': 'Suffered a left middle cerebral artery (MCA) ischemic stroke 5 months ago. '
                                  'Discharged from rehabilitation hospital with residual right hemiparesis: right arm '
                                  'is flexed across chest with clenched fist (flexor spasticity); right leg is stiff '
                                  'and circumducts during ambulation. Mild expressive aphasia (words are hesitant but '
                                  'comprehension is intact). Pale sallow complexion, chronic fatigue, spontaneous '
                                  'sweating upon exertion.',
                       'occupation': 'Retired High School Principal'},
        'standard_diagnosis': {   'cardinal_points': [   'SCALPMOTOR',
                                                         'LI15',
                                                         'LI11',
                                                         'LI4',
                                                         'GB30',
                                                         'GB34',
                                                         'ST36',
                                                         'SP6'],
                                  'cautions': 'Scalp acupuncture technique: Insert needles at a 30-degree angle to the '
                                              'scalp into the loose subaponeurotic connective tissue layer (galea '
                                              'aponeurotica), advance 1.0-1.5 cun, and twirl rapidly at 200 rotations '
                                              'per minute for 1-2 minutes. Press insertion sites firmly with sterile '
                                              'dry cotton ball upon needle removal because scalp tissue is highly '
                                              'vascular and bleeds easily.',
                                  'patterns': [   'Post-Stroke Sequelae (Zhong Feng Hou Yi Zheng / Hemiplegia)',
                                                  'Qi Deficiency and Blood Stasis Obstructing the Channels and '
                                                  'Collaterals (Qi Xu Xue Yu)'],
                                  'synergies': [   'Jiao Shunfa Scalp Motor Area (contralateral left Motor Area: upper '
                                                   '1/5 for leg, middle 2/5 for arm)',
                                                   'Upper limb Yangming trio (LI15 + LI11 + LI4)',
                                                   'Lower limb motor facilitators (GB30 + GB34 + ST36)',
                                                   'Qi tonic root (ST36 Zusanli)'],
                                  'treatment_principles': [   'Tonify Primal Qi and Generate Blood',
                                                              'Activate Blood and Dissolve Collateral Stasis',
                                                              'Unblock Channels and Nourish Tendons',
                                                              'Awaken the Brain and Restore Function']},
        'title': 'Patient Intake: 68yo Male (Retired Principal)'},
    {   'category': 'Gynecology & Obstetrics',
        'id': 'CASE-021',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Full Heat presents with high '
                                                                      'fever, profuse sweating, extreme thirst, '
                                                                      'surging pulse (Da Mai), and thick yellow '
                                                                      'coating.',
                                                                 'B': '✅ **Correct:** At menopause (age 7x7=49 in the '
                                                                      'Su Wen), Tiangui dries up and Kidney Yin '
                                                                      'declines. Without sufficient Yin fluid to '
                                                                      'anchor and balance Yang, the ministerial fire '
                                                                      'loses restraint and flares upward as Empty Heat '
                                                                      '(hot flashes, night sweats, red peeled tongue, '
                                                                      'and thready-rapid pulse) (CAM, Maciocia).',
                                                                 'C': '❌ **Incorrect:** Phlegm-heat presents with '
                                                                      'manic behavior and thick greasy yellow coat.',
                                                                 'D': '❌ **Incorrect:** Yang deficiency presents with '
                                                                      'cold intolerance and pale wet tongue.'},
                                             'options': [   'A. Full Heat in the Yangming Organ stage with '
                                                            'constipation and surging pulse',
                                                            'B. Kidney Yin Deficiency with Empty Heat Flaring Upward '
                                                            '(Xu Huo)',
                                                            'C. Phlegm-Heat Harassing the Heart',
                                                            'D. Spleen and Kidney Yang Deficiency with Floating Yang'],
                                             'prompt': 'Surging hot flashes, drenching night sweats, 5-palm heat, red '
                                                       'peeled tongue with no coat, and a thready-rapid pulse confirm '
                                                       'which diagnostic entity?',
                                             'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation (Empty Heat vs Full Heat)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** HT3 is He-Sea point on elbow.',
                                                                 'B': '✅ **Correct (HT6 Yinxi):** HT6 (located 0.5 cun '
                                                                      'proximal to the wrist crease on the radial side '
                                                                      'of flexor carpi ulnaris tendon) is the Xi-Cleft '
                                                                      'point of the Hand Shaoyin Heart channel. It has '
                                                                      'a specific, powerful empirical action to clear '
                                                                      'Heart Empty Fire, astringe pores, and '
                                                                      'immediately arrest drenching night sweats '
                                                                      '(Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** HT7 is Yuan-Source for '
                                                                      'insomnia and palpitations.',
                                                                 'D': '❌ **Incorrect:** SI3 treats occipital headache '
                                                                      'and spinal disorders.'},
                                             'options': [   'A. HT3 (Shaohai)',
                                                            'B. HT6 (Yinxi)',
                                                            'C. HT7 (Shenmen)',
                                                            'D. SI3 (Houxi)'],
                                             'prompt': 'Which acupuncture point is the Xi-Cleft point of the Heart '
                                                       'channel and is universally recognized across textbooks as the '
                                                       'premier point to stop night sweats?',
                                             'question_id': 'Q2',
                                             'title': '2. Premier Point for Night Sweats (Dao Han)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Moxa is used across all age '
                                                                      'groups.',
                                                                 'B': '✅ **Correct (Contraindication of Moxa):** '
                                                                      "Classic clinical rule: 'Do not apply fire to "
                                                                      "fire.' In Yin deficiency with empty heat "
                                                                      '(cracked red tongue without coat, rapid pulse), '
                                                                      'the body lacks cool fluids. Applying burning '
                                                                      'Artemisia (moxa) acts like pouring oil on a '
                                                                      'flame, evaporating residual fluids and '
                                                                      'worsening night sweats and hot flashes (Deadman '
                                                                      '& CAM).',
                                                                 'C': '❌ **Incorrect:** Moxa does not cause cardiac '
                                                                      'arrest.',
                                                                 'D': '❌ **Incorrect:** Moxa is used on many '
                                                                      'anatomical regions.'},
                                             'options': [   'A. Because moxibustion is only used for children.',
                                                            'B. Because moxibustion introduces pure Yang thermal '
                                                            'energy into an already parched, Yin-depleted state, which '
                                                            'violently fans the Empty Fire and severely exacerbates '
                                                            'hot flashes, insomnia, and dry fluids.',
                                                            'C. Because moxa triggers immediate cardiac arrest.',
                                                            'D. Because moxa only works on the lower back.'],
                                             'prompt': 'Why is moxibustion therapy strictly contraindicated for this '
                                                       "patient's hot flashes and night sweats?",
                                             'question_id': 'Q3',
                                             'title': '3. Therapeutic Modality Contraindication'}],
        'patient': {   'age': 51,
                       'chief_complaint': 'Frequent sudden hot flashes (8-10 episodes daily) with drenching sweats, '
                                          'especially at night, accompanied by insomnia and mood swings for 8 months.',
                       'four_examinations': {   'auscultation_olfaction': 'Speech is rapid and breathy; sighs when '
                                                                          'discussing fatigue.',
                                                'inquiry': "Reports 'five-palm heat' (burning sensation in palms, "
                                                           'soles, and chest); dry throat at night; memory lapses; '
                                                           'irritability.',
                                                'inspection': 'Malar flushing (redness on cheekbones). Anxious, '
                                                              'exhausted appearance. Tongue body is distinctly red, '
                                                              'dry, with fine superficial cracks, and completely '
                                                              'peeled (scanty coating / geographical tongue with no '
                                                              'coat).',
                                                'palpation': 'Skin feels warm and dry to touch. Pulse is Thready (Xi) '
                                                             'and Rapid (Shuo), particularly deficient, weak, and thin '
                                                             'in both Chi (Kidney) positions.'},
                       'gender': 'Female',
                       'history': 'Menstrual cycles became irregular 14 months ago and ceased completely 5 months ago. '
                                  'Hot flashes begin with an intense heat surging from the chest into the neck and '
                                  'face, followed by drenching perspiration and subsequent shivering chills. Wakes '
                                  'drenched in sweat 2-3 times nightly. Reports vaginal dryness, dry hair, lower back '
                                  'soreness, and a high-pitched tinnitus resembling cicadas in the evening.',
                       'occupation': 'High School Librarian'},
        'standard_diagnosis': {   'cardinal_points': ['KD3', 'KD6', 'HT6', 'SP6', 'CV4', 'LR3'],
                                  'cautions': 'CONTRAINDICATION OF MOXIBUSTION: Moxibustion strongly adds Yang fire '
                                              'and is CONTRAINDICATED in severe Yin Deficiency with blazing Empty '
                                              'Fire. Tonify Kidney Yin using gentle needle retention without heat. '
                                              'Advise patient on hydration and lifestyle adjustments.',
                                  'patterns': [   'Kidney Yin Deficiency with Empty Fire Flaring (Shen Yin Xu, Xu Huo '
                                                  'Shang Yan)',
                                                  'Menopausal Syndrome (Jue Jing Qian Hou Zhu Zheng)'],
                                  'synergies': [   'Yuan-Source Kidney water anchor (KD3 Taixi)',
                                                   'Confluent point of Yin Qiao Mai (KD6 Zhaohai)',
                                                   'Xi-Cleft of Heart master for night sweats (HT6 Yinxi)',
                                                   'Three Yin intersection (SP6 Sanyinjiao)',
                                                   'Front-Mu of Small Intestine / Original Qi reservoir (CV4 Guanyuan '
                                                   '- needle only, no moxa)'],
                                  'treatment_principles': [   'Nourish Kidney Yin and Enrich Primal Water',
                                                              'Clear Empty Heat and Settle Rebellious Fire',
                                                              'Calm the Spirit and Stop Night Sweats']},
        'title': 'Patient Intake: 51yo Female (School Librarian)'},
    {   'category': 'Dermatology & External',
        'id': 'CASE-022',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Spleen/Lung aphorism.',
                                                                 'B': '✅ **Correct:** Classic fundamental dermatology '
                                                                      "principle from the Yi Zong Jin Jian: 'Zhi feng "
                                                                      "xian zhi xue, xue xing feng zi mie' (In "
                                                                      'treating wind, first treat the blood; when '
                                                                      'blood moves freely, wind naturally '
                                                                      'extinguishes). Purging heat from the Blood '
                                                                      'level with points like SP10 (Xuehai) and LI11 '
                                                                      'cools the cutaneous microvasculature and '
                                                                      'eliminates pruritus (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Metal controls Wood, but not '
                                                                      'the primary skin aphorism.',
                                                                 'D': '❌ **Incorrect:** Not a canonical maxim.'},
                                             'options': [   "A. 'To treat Phlegm, one must first warm the Kidney.'",
                                                            "B. 'To treat Wind, first treat the Blood; once Blood "
                                                            "flows smoothly, Wind will naturally be extinguished' (Zhi "
                                                            'feng xian zhi xue, xue xing feng zi mie).',
                                                            "C. 'To treat the Liver, first tonify the Lung.'",
                                                            "D. 'To treat Cold, first bleed the Jing-Well points.'"],
                                             'prompt': 'Which famous ancient Chinese medical maxim governs the '
                                                       'treatment of severe skin pruritus and acute wind-heat '
                                                       'eruptions?',
                                             'question_id': 'Q1',
                                             'title': '1. Ancient Aphorism & Blood-Wind Relationship'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** SP9 drains dampness.',
                                                                 'B': "✅ **Correct (SP10 Xuehai):** SP10 ('Sea of "
                                                                      "Blood') is situated on the bulge of the vastus "
                                                                      'medialis muscle. It is the premier point on the '
                                                                      'body to regulate, invigorate, cool, and nourish '
                                                                      'Blood. When sedated, it expels Wind and clears '
                                                                      'Blood Heat in urticaria, eczema, and pruritus '
                                                                      '(Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** ST36 tonifies Qi and Blood.',
                                                                 'D': '❌ **Incorrect:** LR8 is He-Sea for nourishing '
                                                                      'Liver Yin/Blood.'},
                                             'options': [   'A. SP9 (Yinlingquan)',
                                                            'B. SP10 (Xuehai)',
                                                            'C. ST36 (Zusanli)',
                                                            'D. LR8 (Ququan)'],
                                             'prompt': 'Which acupuncture point located 2 cun proximal to the '
                                                       "superior-medial border of the patella is known as the 'Sea of "
                                                       "Blood' and is premier for all skin conditions?",
                                             'question_id': 'Q2',
                                             'title': '2. Sea of Blood (Xuehai) Point Function'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Throat tightness with stridor '
                                                                      'is a medical emergency, not simple Qi '
                                                                      'stagnation.',
                                                                 'B': '✅ **Correct (Anaphylaxis Red Flag):** Urticaria '
                                                                      'accompanied by angioedema of the larynx, '
                                                                      'bronchospasm, and cardiovascular collapse is '
                                                                      'life-threatening anaphylaxis. Immediate '
                                                                      'administration of intramuscular epinephrine in '
                                                                      'the anterolateral thigh and calling 911 is the '
                                                                      'standard emergency medical protocol required by '
                                                                      'Canadian healthcare regulations.',
                                                                 'C': '❌ **Incorrect:** Dangerous delay.',
                                                                 'D': '❌ **Incorrect:** Trivializes a lethal '
                                                                      'emergency.'},
                                             'options': [   'A. Mild Qi stagnation.',
                                                            'B. Acute Anaphylactic Shock / Angioedema requiring '
                                                            'immediate intramuscular Epinephrine (EpiPen) '
                                                            'administration and emergency 911 dispatch.',
                                                            'C. Wind-Cold invading the Taiyin channel.',
                                                            'D. Normal emotional reaction to itching.'],
                                             'prompt': 'If a patient with acute urticaria suddenly complains of throat '
                                                       'tightness, difficulty swallowing, inspiratory stridor, and '
                                                       'dizziness, what life-threatening emergency must be identified?',
                                             'question_id': 'Q3',
                                             'title': '3. Anaphylaxis Emergency Recognition'}],
        'patient': {   'age': 22,
                       'chief_complaint': 'Sudden widespread eruption of intensely itchy, raised red wheals across '
                                          'trunk and limbs for 24 hours after an outdoor soccer game in warm humid '
                                          'weather.',
                       'four_examinations': {   'auscultation_olfaction': 'Agitated voice.',
                                                'inquiry': 'Reports intense burning sensation upon scratching; thirst '
                                                           'for cool drinks; slight constipation.',
                                                'inspection': 'Restless, scratching arms continuously. Prominent '
                                                              'erythematous edematous urticarial plaques and wheals '
                                                              'across body with active dermographism. Tongue body is '
                                                              'red at the tip and lateral margins with a thin yellow '
                                                              'coating.',
                                                'palpation': 'Skin lesions are warm to touch; excoriations from '
                                                             'scratching. Pulse is Floating (Fu) and Rapid (Shuo).'},
                       'gender': 'Male',
                       'history': 'Began sweating heavily during the match, then drank iced energy drinks and sat in '
                                  'the cold wind. Within 2 hours, raised wheals appeared on his abdomen, rapidly '
                                  'spreading to his back, thighs, and arms. Wheals are bright red, edematous, with '
                                  'irregular shapes that appear and disappear rapidly (moving like wind). Burning '
                                  'pruritus is so intense he cannot sleep.',
                       'occupation': 'University Soccer Athlete'},
        'standard_diagnosis': {   'cardinal_points': ['LI11', 'SP10', 'BL40', 'LI4', 'SP6', 'DU14'],
                                  'cautions': 'Pricking and bleeding technique (using sterile lancet at DU14 or BL40 '
                                              'to express 2-3 drops of dark blood) is highly effective for rapidly '
                                              'clearing Blood Heat, but must be conducted strictly under Canadian '
                                              'Bloodborne Pathogen Standards (disposable gloves, immediate disposal '
                                              'into yellow sharps container, sterile cotton swab pressure). Rule out '
                                              'anaphylaxis (stridor, lip/tongue swelling, bronchospasm, or hypotension '
                                              'requiring immediate epinephrine injection and 911 call).',
                                  'patterns': [   'Acute Urticaria / Hives (Yin Zhen / Feng Zhen Kuai)',
                                                  'Wind-Heat Invading the Skin and Blood Level (Feng Re Ke Biao)'],
                                  'synergies': [   'Premier heat and itching clearer (LI11 Quchi)',
                                                   'Sea of Blood master regulator (SP10 Xuehai)',
                                                   'Upper Du Mai heat vent (DU14 Dazhui - prick and cup)',
                                                   'Lower He-Sea blood cooler (BL40 Weizhong)',
                                                   'Distal wind diffuser (LI4)'],
                                  'treatment_principles': [   'Dispel Wind and Clear Heat',
                                                              'Cool Blood and Drain Fire',
                                                              'Stop Itching and Resolve Wheals']},
        'title': 'Patient Intake: 22yo Male (University Athlete)'},
    {   'category': 'Safety & Emergency Protocols',
        'id': 'CASE-023',
        'multiple_choice_questions': [   {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Warm tea helps prevent '
                                                                      'syncope.',
                                                                 'B': '✅ **Correct (Yun Zhen Etiology):** Vasovagal '
                                                                      'syncope is triggered by a sudden surge in '
                                                                      'parasympathetic tone with peripheral '
                                                                      'vasodilation and bradycardia. Fasting '
                                                                      '(hypoglycemia), psychological fear/needle '
                                                                      'phobia, physical fatigue, seated posture (blood '
                                                                      'pools in lower limbs), and violent manual '
                                                                      'needle stimulation are the classic predisposing '
                                                                      'causes (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** Ear seeds have virtually zero '
                                                                      'risk of syncope.',
                                                                 'D': '❌ **Incorrect:** Rested patients are less prone '
                                                                      'to shock.'},
                                             'options': [   'A. Drinking hot ginger tea 10 minutes before treatment.',
                                                            'B. First-time treatment, extreme anxiety/nervousness, '
                                                            'hunger/empty stomach, fatigue/exhaustion, and overly '
                                                            'aggressive needle manipulation in a seated position.',
                                                            'C. Receiving gentle ear seeds on the auricular shell.',
                                                            'D. Sleeping 8 hours the night before.'],
                                             'prompt': 'According to classic textbooks and modern Canadian safety '
                                                       'standards, which combination of patient factors dramatically '
                                                       'increases the risk of Needle Shock (Yun Zhen)?',
                                             'question_id': 'Q1',
                                             'title': '1. Predisposing Factors for Needle Shock (Yun Zhen)'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Continuing stimulation worsens '
                                                                      'vasovagal collapse.',
                                                                 'B': '✅ **Correct (Mandatory Step 1):** The universal '
                                                                      'Canadian Clean Needle and clinical emergency '
                                                                      'guideline is: STOP needling and IMMEDIATELY '
                                                                      'REMOVE ALL NEEDLES. Retaining needles continues '
                                                                      'the noxious sensory stimulus and risks bending '
                                                                      'or breaking needles if the patient convulses or '
                                                                      'slumps over (CARB-TCMPA candidate safety '
                                                                      'guide).',
                                                                 'C': '❌ **Incorrect:** Abandoning a patient in '
                                                                      'syncope violates professional duty of care.',
                                                                 'D': '❌ **Incorrect:** Forcing an orthostatic patient '
                                                                      'to stand causes immediate cerebral ischemia and '
                                                                      'dangerous collapse.'},
                                             'options': [   'A. Apply electrical stimulation to the existing needles.',
                                                            'B. Immediately stop needle manipulation and withdraw all '
                                                            'needles from the patient.',
                                                            'C. Run out of the clinic room to find a medical textbook.',
                                                            'D. Force the patient to stand up and walk around the '
                                                            'room.'],
                                             'prompt': 'What is the very FIRST mandatory clinical action an '
                                                       'acupuncturist must take the instant a patient displays '
                                                       'symptoms of Needle Shock?',
                                             'question_id': 'Q2',
                                             'title': '2. Step-by-Step Emergency Revival Protocol'},
                                         {   'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** ST4 is for facial paralysis.',
                                                                 'B': '✅ **Correct (DU26 Renzhong / Shuigou):** DU26 '
                                                                      'is the classic premier resuscitation point '
                                                                      'connecting the Du Mai with the Yangming '
                                                                      'channels. Firm fingernail pressing directed '
                                                                      'obliquely upward stimulates the trigeminal and '
                                                                      'facial nerve branches, triggering sympathetic '
                                                                      'vasomotor tone, elevating blood pressure, '
                                                                      'stimulating respiration, and restoring '
                                                                      'consciousness (Deadman & CAM).',
                                                                 'C': '❌ **Incorrect:** LI20 is for nasal congestion.',
                                                                 'D': '❌ **Incorrect:** CV24 is on the chin.'},
                                             'options': [   'A. ST4 (Dicang)',
                                                            'B. DU26 (Renzhong / Shuigou)',
                                                            'C. LI20 (Yingxiang)',
                                                            'D. CV24 (Chengjiang)'],
                                             'prompt': 'Which acupuncture point located at the junction of the upper '
                                                       'third and lower two-thirds of the philtrum is the premier '
                                                       'point used with firm fingernail pressure to revive '
                                                       'consciousness?',
                                             'question_id': 'Q3',
                                             'title': '3. Acupressure Point for Immediate Resuscitation'}],
        'patient': {   'age': 27,
                       'chief_complaint': 'First-time acupuncture patient suddenly turns pale, breaks into cold clammy '
                                          'perspiration, reports dizziness and nausea, and loses consciousness during '
                                          'strong needle manipulation.',
                       'four_examinations': {   'auscultation_olfaction': 'Shallow, faint respiration; inaudible '
                                                                          'speech.',
                                                'inquiry': 'Unresponsive to verbal questions for 30 seconds.',
                                                'inspection': 'Ashen, deathly pale facial complexion; profuse cold '
                                                              'beads of sweat dripping from forehead and nose; limp '
                                                              'extremities; eyes rolled upward.',
                                                'palpation': 'Extremities are cold and clammy to touch. Radial pulse '
                                                             'is Faint, Deep, and Slow (Wei Chen Chi), with heart rate '
                                                             'dropping precipitously to 48 beats per minute '
                                                             '(bradycardia).'},
                       'gender': 'Male',
                       'history': 'Never received acupuncture before. Highly anxious about needles. Rushed to clinic '
                                  'without eating breakfast. During the initial insertion and vigorous reducing '
                                  "manipulation of LI4 (Hegu) and LV3 (Taichong), the patient gasped, said 'I feel "
                                  "like I'm going to throw up and pass out', rolled his eyes back, and became "
                                  'unresponsive.',
                       'occupation': 'Software Engineer'},
        'standard_diagnosis': {   'cardinal_points': ['DU26', 'PC6', 'ST36', 'DU20'],
                                  'cautions': 'CARB-TCMPA MANDATORY NEEDLE SHOCK EMERGENCY PROTOCOL: 1. Immediately '
                                              'STOP needling and WITHDRAW ALL NEEDLES. 2. Place patient in supine '
                                              'position with head flat/low and legs elevated (Trendelenburg position) '
                                              'to restore cerebral blood perfusion. 3. Loosen restrictive '
                                              'collar/clothing and ensure open airway. 4. Apply firm fingernail '
                                              'pressure to DU26 (Renzhong) and PC6. 5. Offer warm water or '
                                              'sugar/glucose drink once consciousness is fully regained. 6. NEVER '
                                              'allow the patient to stand up immediately. 7. If the patient does not '
                                              'regain consciousness within 1-2 minutes, or if pulse/breathing stops, '
                                              'immediately initiate CPR and call 911.',
                                  'patterns': [   'Needle Shock / Vasovagal Syncope (Yun Zhen / 晕针)',
                                                  'Acute Sudden Depletion of Qi and Temporary Departure of Shen'],
                                  'synergies': [   'Premier resuscitation master point (DU26 Renzhong / Shuigou - '
                                                   'fingernail acupressure)',
                                                   'Cardiac and vagal stabilizer (PC6 Neiguan)',
                                                   'Qi reservoir (ST36 Zusanli)',
                                                   'Sea of Marrow lifter (DU20 Baihui)'],
                                  'treatment_principles': [   'Emergency Revival of Consciousness (Xing Shen)',
                                                              'Restore Yang Qi and Elevate Blood Pressure',
                                                              'Calm the Spirit and Stabilize Heart Rhythm']},
        'title': 'Patient Intake: 27yo Male (Software Engineer)'},
    {   'id': 'CASE-024',
        'title': 'Patient Intake: 24yo Male (Cystic Fibrosis with Secondary Bronchiectasis)',
        'category': 'Internal Medicine & Respiratory',
        'patient': {   'age': 24,
                       'gender': 'Male',
                       'occupation': 'Graduate Student in Biology',
                       'chief_complaint': 'Chronic paroxysmal cough with blood-streaked sputum, wheezing, dyspnea on '
                                          'mild exertion, and drenching night sweats for 6 weeks.',
                       'history': 'Diagnosed with cystic fibrosis in early childhood. Developed secondary '
                                  'bronchiectasis confirmed by high-resolution chest CT showing localized bronchial '
                                  'dilation in bilateral lower lobes. Negative PPD tuberculin test. Maintained on '
                                  'rotating antibiotic courses, inhaled bronchodilators, and mucolytics. Reports '
                                  'progressive physical wasting, dry mouth, persistent sore throat, and heart '
                                  'palpitations.',
                       'four_examinations': {   'inspection': 'Emaciated, tall slender habitus; prominent malar flush '
                                                              '(bright red cheeks); dry cracked lips; dull red tongue '
                                                              'body with anterior and central peeling (geographic '
                                                              'coat) and fine transverse cracks in the Lung zone.',
                                                'auscultation_olfaction': 'Rapid, shallow, wheezing respiration; '
                                                                          'breathy hoarse voice; persistent hacking '
                                                                          'cough producing scanty, tenacious, '
                                                                          'blood-streaked (rust-colored) sputum.',
                                                'inquiry': 'Constant unquenchable thirst with preference for small '
                                                           'cool sips; drenching nocturnal sweats soaking bedclothes; '
                                                           'palpitations during evening hours; five-palm heat (burning '
                                                           'sensation in soles, palms, chest); severe fatigue.',
                                                'palpation': 'Skin feels dry and warm to touch especially in late '
                                                             'afternoon; radial pulse is Fine/Thready (Xi) and Rapid '
                                                             '(Shuo) with weakness in both Cun positions.'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Primary Pattern Identification (Zang-Fu & Eight Principles)',
                                             'prompt': 'Based on the presentation of chronic cough with blood-streaked '
                                                       'sputum, emaciation, night sweats, red peeled tongue, and a '
                                                       'thready-rapid pulse, what is the primary TCM diagnosis?',
                                             'options': [   'A. Wind-Heat Invading the Lung with Phlegm-Heat',
                                                            'B. Lung and Kidney Yin Deficiency with Empty Fire Flaring '
                                                            '(Fei Shen Yin Xu)',
                                                            'C. Spleen and Lung Qi Deficiency with Damp Phlegm',
                                                            'D. Liver Fire Invading the Lung Scorching Blood Vessels'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Wind-Heat invasion presents '
                                                                      'with acute onset fever, chills, sore swollen '
                                                                      'throat, yellow purulent sputum, and a '
                                                                      'floating-rapid pulse. This patient has a '
                                                                      'longstanding constitutional pathology with '
                                                                      'hallmark signs of Yin deficiency.',
                                                                 'B': '✅ **Correct (Lung & Kidney Yin Deficiency):** '
                                                                      'Chronic disease consuming Yin fluids impairs '
                                                                      'the moistening and descending of Lung Qi. Empty '
                                                                      'Fire flares upward, damaging bronchial '
                                                                      'capillaries (blood-streaked sputum) and '
                                                                      'producing five-palm heat, malar flush, night '
                                                                      'sweats, peeled red tongue, and a thready-rapid '
                                                                      'pulse (CAM & Maciocia).',
                                                                 'C': '❌ **Incorrect:** Spleen and Lung Qi deficiency '
                                                                      'presents with copious white watery or foamy '
                                                                      'sputum, pale flabby tongue with teeth marks, '
                                                                      'loose stools, and an empty/weak pulse without '
                                                                      'night sweats or hemoptysis.',
                                                                 'D': '❌ **Incorrect:** Liver Fire invading the Lung '
                                                                      'produces sudden bursts of violent spasmodic '
                                                                      'coughing triggered by emotional rage, severe '
                                                                      'hypochondriac pain, bitter taste in mouth, '
                                                                      'wiry-rapid pulse, and thick yellow coat.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Cardinal Point Prescription & Confluent Strategy',
                                             'prompt': 'Which acupuncture point prescription best addresses both the '
                                                       'acute hemoptysis/cough and the constitutional root Yin '
                                                       'deficiency in this case?',
                                             'options': [   'A. LU1 (Zhongfu), LU7 (Lieque), KI6 (Zhaohai), HT6 '
                                                            '(Yinxi), LU9 (Taiyuan), KI3 (Taixi), BL43 (Gaohuangshu)',
                                                            'B. BL13 (Feishu), SP4 (Gongsun), PC6 (Neiguan), CV12 '
                                                            '(Zhongwan), ST40 (Fenglong), LU5 (Chize)',
                                                            'C. LI4 (Hegu), LI11 (Quchi), GV14 (Dazhui), LU10 (Yuji), '
                                                            'ST44 (Neiting)',
                                                            'D. BL23 (Shenshu), GV4 (Mingmen), CV4 (Guanyuan), KI3 '
                                                            '(Taixi), BL20 (Pishu)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** This formula combines the master '
                                                                      'Eight Confluent pair LU7 + KI6 (opening the Ren '
                                                                      'Mai and Yin Qiao Mai to moisten the throat, '
                                                                      'lung, and chest); HT6 (Xi-Cleft of Heart, '
                                                                      'premier empirical point for night sweats); LU9 '
                                                                      '+ KI3 (Yuan-Source points tonifying Lung/Kidney '
                                                                      'Yin); LU1 (Front-Mu regulating Lung Qi); and '
                                                                      'BL43 (Gaohuangshu, renowned historical point '
                                                                      'for profound consumptive Yin/Blood deficiency).',
                                                                 'B': '❌ **Incorrect:** SP4 + PC6 opens the Chong Mai '
                                                                      'and Yin Wei Mai for middle jiao dampness and '
                                                                      'stomach nausea; ST40 dissolves phlegm. This '
                                                                      'prescription does not sufficiently nourish '
                                                                      'Kidney Yin or halt empty fire hemoptysis.',
                                                                 'C': '❌ **Incorrect:** Pure heat-clearing dispersal '
                                                                      'formula (LI11, GV14, ST44) for acute exterior '
                                                                      'Yangming heat; it would further dry up precious '
                                                                      'Yin fluids.',
                                                                 'D': '❌ **Incorrect:** Warming Kidney Yang '
                                                                      'tonification formula (Mingmen GV4 with Shenshu '
                                                                      'BL23); contraindicated in Yin deficiency with '
                                                                      'empty heat.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Clinical Precautions & Anatomical Safety',
                                             'prompt': 'What is the critical anatomical safety precaution when '
                                                       'needling thoracic points (LU1, BL13, BL43) in an emaciated '
                                                       'patient with chronic lung disease?',
                                             'options': [   'A. Puncture perpendicularly 1.5 to 2.0 cun to reach the '
                                                            'pleura and stimulate lung parenchymal circulation.',
                                                            'B. Puncture strictly obliquely or transverse-obliquely '
                                                            '0.5 to 0.8 cun away from the lung field; never puncture '
                                                            'perpendicularly to prevent traumatic pneumothorax.',
                                                            'C. Apply heavy direct scarring moxibustion over the upper '
                                                            'ribs for 45 minutes.',
                                                            'D. Needling should be replaced by deep vigorous tuina '
                                                            'cupping over the subclavicular triangle.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect (High Risk):** Deep perpendicular '
                                                                      'needling on the chest or upper back directly '
                                                                      'punctures the parietal and visceral pleura, '
                                                                      'causing tension pneumothorax—a life-threatening '
                                                                      'emergency (Deadman warning).',
                                                                 'B': '✅ **Correct (Pneumothorax Prevention):** '
                                                                      'Emaciated patients have diminished subcutaneous '
                                                                      'adipose tissue and thinned chest walls. '
                                                                      'Needling LU1, BL13, and BL43 must strictly '
                                                                      'follow oblique or transverse insertion directed '
                                                                      'along the intercostal ribs, never '
                                                                      'perpendicular.',
                                                                 'C': '❌ **Incorrect:** Direct scarring moxibustion is '
                                                                      'contraindicated in active Yin deficiency with '
                                                                      'hemoptysis.',
                                                                 'D': '❌ **Incorrect:** Deep aggressive cupping over '
                                                                      'the subclavicular fossa can cause vascular '
                                                                      'bruising and pleural shearing.'}}],
        'standard_diagnosis': {   'patterns': [   'Lung and Kidney Yin Deficiency with Empty Fire Flaring (Fei Shen '
                                                  'Yin Xu, Xu Huo Shang Yan)',
                                                  'Consumptive Pulmonary Fluid Exhaustion with Bronchial Vessel '
                                                  'Injury'],
                                  'treatment_principles': [   'Nourish Lung and Kidney Yin (滋养肺肾之阴)',
                                                              'Clear Empty Heat and Astringe Capillary Bleeding '
                                                              '(清降虚火，凉血止血)',
                                                              'Moisten the Respiratory Tract and Calm Wheezing '
                                                              '(润肺降逆，定喘止咳)'],
                                  'cardinal_points': ['LU1', 'LU7', 'KI6', 'HT6', 'LU9', 'KI3', 'BL43', 'BL13'],
                                  'synergies': [   'Eight Confluent Vessel Master-Couple pair (LU7 Lieque + KI6 '
                                                   'Zhaohai) opens the Ren Mai and Yin Qiao Mai to flood the bronchial '
                                                   'mucosa with Yin fluids.',
                                                   'Xi-Cleft night sweat astringent pair (HT6 Yinxi + KI6 Zhaohai) '
                                                   'arrests nocturnal fluid loss.',
                                                   'Consumptive tonic pair (LU9 Taiyuan + BL43 Gaohuangshu) repairs '
                                                   'deep structural pulmonary tissue.'],
                                  'cautions': 'ANATOMICAL DANGER: Emaciated patients with chronic bronchiectasis have '
                                              'high apical pleura. Never needle LU1, BL13, or BL43 perpendicularly. '
                                              'Confirm patient does not have massive active hemoptysis (>100 mL/24h) '
                                              'which requires immediate emergency transport.'}},
    {   'id': 'CASE-025',
        'title': 'Patient Intake: 89yo Female (Severe Geriatric Constipation & Intestinal Dryness)',
        'category': 'Geriatric & Digestive',
        'patient': {   'age': 89,
                       'gender': 'Female',
                       'occupation': 'Retired Seamstress',
                       'chief_complaint': 'Intractable constipation with bowel movements only once every 8 to 10 days, '
                                          'accompanied by dry scybalous stools, dry mouth, and withered skin.',
                       'history': 'Suffering from chronic constipation for over 12 years, progressively worsening. '
                                  'Stool is dry, small, and hard like sheep dung, requiring manual evacuation or '
                                  'enemas. Has tried high-fiber diets and stimulant laxatives (senna, bisacodyl) with '
                                  'diminishing efficacy and abdominal cramping. Patient is emaciated, constantly sips '
                                  'warm water to quench unquenchable mouth dryness, and has lusterless pale skin and '
                                  'brittle ridged fingernails.',
                       'four_examinations': {   'inspection': 'Frail, cachectic habitus; dry wrinkled lusterless '
                                                              'facial complexion; dry brittle split nails; pale-red '
                                                              'tongue body with completely peeled geographic coat '
                                                              '(mirror tongue) and prominent central longitudinal '
                                                              'cracks.',
                                                'auscultation_olfaction': 'Weak, thin, low-pitched voice; slow '
                                                                          'deliberate speech; shortness of breath upon '
                                                                          'walking across room.',
                                                'inquiry': 'No bowel movement for 7 days; severe exhaustion after '
                                                           'attempting defecation; constant mouth dryness with '
                                                           'frequent sips of water; dizziness on standing '
                                                           '(orthostatic); dull abdominal discomfort without acute '
                                                           'sharp pain.',
                                                'palpation': 'Soft flaccid abdominal wall without rebound tenderness; '
                                                             'palpable hard fecal impaction in the left iliac fossa '
                                                             '(sigmoid colon) non-tender to pressure; radial pulse is '
                                                             'Fine/Thready (Xi) and Choppy/Hesitant (Se).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Diagnosis according to Eight Principles & Six Stages',
                                             'prompt': 'Based on the severe constipation with sheep dung stools, '
                                                       'emaciation, lusterless dry skin, peeled mirror tongue, and a '
                                                       'thready-choppy pulse in an 89yo patient, what is the '
                                                       'diagnosis?',
                                             'options': [   'A. Yangming Bowel Excess Heat Pattern (Da Chang Shi Re)',
                                                            'B. Yangming Level: Blood and Yin Deficiency with '
                                                            'Intestinal Fluid Depletion (Chang Zao Bian Bi)',
                                                            'C. Taiyin Spleen Deficiency Cold with Excessive Damp '
                                                            'Accumulation',
                                                            'D. Shaoyang Gallbladder Damp-Heat Obstruction'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Yangming Bowel Excess Heat '
                                                                      '(Cheng Qi Tang pattern) presents with high '
                                                                      'tidal fever, profuse sweating, abdominal '
                                                                      'fullness that is severe and worse on pressure '
                                                                      '(Ju An), delirious speech, and a deep forceful '
                                                                      'rapid pulse. Applying drastic purgatives to '
                                                                      'this 89yo emaciated patient would cause fatal '
                                                                      'fluid and Yang collapse.',
                                                                 'B': '✅ **Correct (Blood/Yin Deficiency with '
                                                                      'Intestinal Dryness):** In elderly patients, '
                                                                      'constitutional Blood and Yin decline depletes '
                                                                      'the bodily fluids (Jin Ye) that lubricate the '
                                                                      'lower intestines. The bowel becomes dry like a '
                                                                      "riverbed without water ('no water to float the "
                                                                      "boat'). Characterized by sheep dung stools, "
                                                                      'lusterless skin, dry peeled tongue, and a '
                                                                      'thready-choppy pulse.',
                                                                 'C': '❌ **Incorrect:** Taiyin Cold-Damp presents with '
                                                                      'watery diarrhea, abdominal pain relieved by '
                                                                      'warmth and pressure, pale flabby tongue with '
                                                                      'thick slippery white coat, and a slow pulse—the '
                                                                      'exact opposite of dry constipation.',
                                                                 'D': '❌ **Incorrect:** Shaoyang pattern presents with '
                                                                      'alternating chills and fever, bitter taste, '
                                                                      'hypochondriac fullness, and a wiry pulse.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Strategic Acupuncture Treatment Prescription',
                                             'prompt': 'Which point combination best embodies the clinical strategy of '
                                                       "'Increasing water to float the boat' (Zeng Ye Run Chang) for "
                                                       'this patient?',
                                             'options': [   'A. ST25 (Tianshu), ST37 (Shangjuxu), SJ6 (Zhigou), KI6 '
                                                            '(Zhaohai), SP6 (Sanyinjiao), CV12 (Zhongwan)',
                                                            'B. LI11 (Quchi), ST44 (Neiting), LI4 (Hegu), ST25 '
                                                            '(Tianshu), LR3 (Taichong) with vigorous reducing method',
                                                            'C. GV4 (Mingmen), BL23 (Shenshu), CV4 (Guanyuan), ST36 '
                                                            '(Zusanli) with heavy warming moxa cones',
                                                            'D. BL25 (Dachangshu), BL28 (Pangguangshu), CV3 (Zhongji), '
                                                            'SP9 (Yinlingquan) with bloodletting'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** This formula combines the '
                                                                      'premier empirical constipation pair SJ6 + KI6 '
                                                                      '(Zhigou clears the San Jiao pathway while '
                                                                      'Zhaohai nourishes Kidney Yin and lower burner '
                                                                      'fluids); ST25 + ST37 (Front-Mu and Lower He-Sea '
                                                                      'of Large Intestine to gently regulate '
                                                                      'peristalsis without harsh draining); SP6 '
                                                                      '(nourishes Blood and Yin); and CV12 (harmonizes '
                                                                      'middle burner Qi).',
                                                                 'B': '❌ **Incorrect:** Strong reducing method on '
                                                                      'LI11, ST44, and LI4 is designed to purge '
                                                                      'Yangming Fire and would further exhaust this '
                                                                      "frail patient's Yin fluids.",
                                                                 'C': '❌ **Incorrect:** Heavy direct moxibustion on '
                                                                      'Mingmen and Guanyuan warms Yang and dries '
                                                                      'Dampness, which would aggravate severe '
                                                                      'intestinal dryness.',
                                                                 'D': '❌ **Incorrect:** Bloodletting is strongly '
                                                                      'contraindicated in severe Blood/Yin deficiency '
                                                                      'in an 89-year-old.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Clinical Empirical Point Pairing Mechanism',
                                             'prompt': 'What is the classic textbook rationale for combining SJ6 '
                                                       '(Zhigou) with KI6 (Zhaohai) in treating dry constipation?',
                                             'options': [   'A. SJ6 expels external wind pathogens while KI6 drains '
                                                            'dampness through diuresis.',
                                                            'B. SJ6 regulates San Jiao Qi movement in the bowels while '
                                                            'KI6 nourishes Yin fluids to moisten the intestines.',
                                                            'C. SJ6 arrests vomiting while KI6 anchors ascending Liver '
                                                            'Yang.',
                                                            'D. SJ6 stops diarrhea while KI6 consolidates Kidney '
                                                            'Jing.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Neither point is used here for '
                                                                      'exterior wind or diuretic damp draining.',
                                                                 'B': '✅ **Correct (SJ6 + KI6 Synergy):** SJ6 (Fire '
                                                                      'point of San Jiao) regulates the Qi mechanism '
                                                                      'of the intestines and unblocks stagnation; KI6 '
                                                                      '(Yin Qiao Master) generates Kidney water and '
                                                                      'lower burner fluids. Together, they create the '
                                                                      'ideal synergy of promoting movement while '
                                                                      "nourishing moisture ('Zeng Ye Run Chang').",
                                                                 'C': '❌ **Incorrect:** Irrelevant to intestinal '
                                                                      'constipation.',
                                                                 'D': '❌ **Incorrect:** Both points promote smooth '
                                                                      'evacuation in this context, not astringency.'}}],
        'standard_diagnosis': {   'patterns': [   'Blood and Yin Deficiency with Intestinal Fluid Depletion (Xue Xu '
                                                  'Yin Kui, Chang Zao Bian Bi)',
                                                  'Yangming Level Dryness with Depleted Fluid Reservoir'],
                                  'treatment_principles': [   'Nourish Blood and Enrich Yin to Lubricate the '
                                                              'Intestines (养血滋阴，润肠通便)',
                                                              'Regulate Lower Jiao Qi Movement Gently (理气通导，增液行舟)'],
                                  'cardinal_points': ['ST25', 'ST37', 'SJ6', 'KI6', 'SP6', 'CV12', 'ST36'],
                                  'synergies': [   'Empirical Fluid-Moving pair (SJ6 Zhigou + KI6 Zhaohai) generates '
                                                   'Yin fluids and moves stagnant fecal matter.',
                                                   'Large Intestine Mu-He combination (ST25 Tianshu + ST37 Shangjuxu) '
                                                   'restores colon motility.',
                                                   'Blood-nourishing duo (SP6 Sanyinjiao + ST36 Zusanli) replenishes '
                                                   'postnatal Qi and Blood.'],
                                  'cautions': 'STIMULANT LAXATIVE WARNING: Strictly avoid drastic bitter-cold '
                                              'purgatives (Da Huang, Mang Xiao, Senna). Ensure gentle needle '
                                              'manipulation (even/reinforcing) to prevent needle shock in frail '
                                              'geriatric patients. Check for fecal impaction with bowel obstruction '
                                              'signs.'}},
    {   'id': 'CASE-026',
        'title': 'Patient Intake: 47yo Male (Acute Biliary Colic / Cholecystitis)',
        'category': 'Internal Medicine & Digestive',
        'patient': {   'age': 47,
                       'gender': 'Male',
                       'occupation': 'Construction Contractor',
                       'chief_complaint': 'Severe paroxysmal cramping pain in the right hypochondrium radiating to the '
                                          'right shoulder and back, accompanied by nausea, vomiting of bitter bile, '
                                          'and bright yellow sclera.',
                       'history': 'Episodes of dull right upper quadrant fullness for 6 months after eating fried '
                                  'foods. Last night, after a celebratory dinner of barbecued pork and beer, '
                                  'experienced sudden excruciating right subcostal pain radiating upward through the '
                                  'right scapula. Vomited gastric contents and greenish-yellow bitter fluid three '
                                  'times. Temperature is 38.3°C. Dark amber urine and light clay-colored stools.',
                       'four_examinations': {   'inspection': 'Patient curled forward holding right upper abdomen in '
                                                              'distress; sclera and facial skin display bright '
                                                              'orange-yellow jaundice; Red tongue body with thick, '
                                                              'sticky, foul-smelling yellow coating.',
                                                'auscultation_olfaction': 'Groaning loudly with each spasm; heavy '
                                                                          'coarse breathing; foul breath odor.',
                                                'inquiry': 'Intense cramping right subcostal pain; severe bitter taste '
                                                           'in mouth; burning sensation throughout epigastrium; fever '
                                                           'with chills; complete repulsion toward food.',
                                                'palpation': 'Acute tenderness and localized muscle guarding at the '
                                                             "right costal margin with positive Murphy's sign (sudden "
                                                             'arrest of inspiration upon deep subcostal palpation); '
                                                             'acute exquisite tenderness at Dannangxue (Extra point '
                                                             'below right GB34); radial pulse is Wiry (Xian) and '
                                                             'Slippery-Rapid (Hua-Shuo).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Primary Zang-Fu Pattern Identification',
                                             'prompt': 'What is the primary TCM pattern for this presentation of acute '
                                                       'right hypochondriac colicky pain radiating to the scapula, '
                                                       'bright jaundice, bitter taste, yellow greasy tongue coat, and '
                                                       'a wiry-slippery-rapid pulse?',
                                             'options': [   'A. Liver Qi Stagnation with Spleen Deficiency',
                                                            'B. Damp-Heat in Liver and Gallbladder with Biliary '
                                                            'Obstruction (Gan Dan Shi Re)',
                                                            'C. Cold Coagulation in the Liver Channel',
                                                            'D. Spleen and Stomach Damp-Heat with Food Stagnation '
                                                            'only'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Liver-Spleen disharmony '
                                                                      'presents with dull distension without fever, '
                                                                      "jaundice, or positive Murphy's sign, with a "
                                                                      'wiry-weak pulse and thin white coat.',
                                                                 'B': '✅ **Correct (Damp-Heat in Liver & '
                                                                      'Gallbladder):** Heavy alcohol and fatty foods '
                                                                      'create internal Damp-Heat that steams the Liver '
                                                                      'and Gallbladder. The bile ducts become '
                                                                      'congested and obstructed, producing '
                                                                      'excruciating right subcostal colic radiating to '
                                                                      "the right shoulder, Murphy's sign, jaundice, "
                                                                      'dark urine, yellow greasy tongue coat, and a '
                                                                      'wiry-slippery-rapid pulse.',
                                                                 'C': '❌ **Incorrect:** Cold in the Liver channel '
                                                                      'produces pain in the scrotum or lower abdomen '
                                                                      'relieved by heat, with pale tongue and deep '
                                                                      'slow wiry pulse.',
                                                                 'D': '❌ **Incorrect:** Pure middle jiao food '
                                                                      'stagnation centers on the epigastrium with foul '
                                                                      'belching and abdominal distension, lacking '
                                                                      'jaundice and biliary radiation.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Empirical & Channel Point Selection',
                                             'prompt': 'Which acupuncture prescription includes the premier empirical '
                                                       'point for acute gallbladder colic and clearing Damp-Heat?',
                                             'options': [   'A. Dannangxue (EX-LE6), GB34 (Yanglingquan), GB24 '
                                                            '(Riyue), LR14 (Qimen), SP9 (Yinlingquan), LI11 (Quchi), '
                                                            'BL19 (Danshu)',
                                                            'B. CV12 (Zhongwan), ST36 (Zusanli), SP4 (Gongsun), PC6 '
                                                            '(Neiguan), BL20 (Pishu)',
                                                            'C. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 '
                                                            '(Mingmen), BL52 (Zhishi)',
                                                            'D. LU7 (Lieque), LI4 (Hegu), BL13 (Feishu), GV14 '
                                                            '(Dazhui)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** Dannangxue (located 1-2 cun '
                                                                      'below right GB34) is the legendary empirical '
                                                                      'point for acute cholecystitis and gallstones; '
                                                                      'GB34 (He-Sea of Gallbladder) unblocks biliary '
                                                                      'flow; GB24 + LR14 (Front-Mu points of GB and '
                                                                      'Liver) clear local inflammation; SP9 drains '
                                                                      'dampness; LI11 clears toxic heat; and BL19 '
                                                                      'regulates Gallbladder Back-Shu.',
                                                                 'B': '❌ **Incorrect:** Spleen/Stomach harmonizing '
                                                                      'formula for simple indigestion and vomiting, '
                                                                      'omitting Gallbladder channel points.',
                                                                 'C': '❌ **Incorrect:** Kidney Yang tonification '
                                                                      'formula; contraindicated in acute inflammatory '
                                                                      'Damp-Heat.',
                                                                 'D': '❌ **Incorrect:** Exterior wind-heat Lung '
                                                                      'formula.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Western Medical Red Flag Recognition',
                                             'prompt': "Which constellation of clinical signs (Charcot's Triad) "
                                                       'indicates acute ascending cholangitis requiring immediate '
                                                       'emergency hospital transfer?',
                                             'options': [   'A. Occipital headache, clear rhinorrhea, and stiff neck.',
                                                            'B. Right upper quadrant pain, high spiking fever with '
                                                            'shaking chills, and jaundice.',
                                                            'C. Left lower quadrant pain, chronic constipation, and '
                                                            'afebrile state.',
                                                            'D. Epigastric hunger, dry mouth, and normal body '
                                                            'temperature.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Classic signs of common cold / '
                                                                      'Wind-Cold.',
                                                                 'B': "✅ **Correct (Charcot's Triad):** Right upper "
                                                                      'quadrant abdominal pain + high fever with '
                                                                      "rigors + jaundice constitutes Charcot's Triad "
                                                                      'for acute ascending cholangitis (bacterial '
                                                                      'infection of obstructed bile duct). If '
                                                                      'accompanied by hypotension and confusion '
                                                                      "(Reynolds' Pentad), it represents septic shock "
                                                                      'requiring urgent surgical/endoscopic '
                                                                      'decompression.',
                                                                 'C': '❌ **Incorrect:** Suggests diverticulitis.',
                                                                 'D': '❌ **Incorrect:** Stomach Yin deficiency.'}}],
        'standard_diagnosis': {   'patterns': [   'Damp-Heat in Liver and Gallbladder with Biliary Colic (Gan Dan Shi '
                                                  'Re, Dan Shi Tong)',
                                                  'Obstruction of the Bile Duct by Damp-Heat and Phlegm-Stones'],
                                  'treatment_principles': [   'Clear Heat, Drain Dampness, and Purge Gallbladder Fire '
                                                              '(清利肝胆湿热)',
                                                              'Unblock the Gallbladder Collaterals and Arrest Acute '
                                                              'Spasms (利胆通腑，化石止痛)'],
                                  'cardinal_points': [   'Dannangxue',
                                                         'GB34',
                                                         'GB24',
                                                         'LR14',
                                                         'SP9',
                                                         'LI11',
                                                         'BL19',
                                                         'ST36'],
                                  'synergies': [   'Empirical Biliary pair (Right Dannangxue + GB34 Yanglingquan) '
                                                   'produces immediate spasmolysis of the sphincter of Oddi.',
                                                   'Front-Mu clearing pair (GB24 Riyue + LR14 Qimen) eliminates local '
                                                   'inflammation and hypochondriac pain.',
                                                   'Damp-draining duo (SP9 Yinlingquan + LI11 Quchi) drives heat and '
                                                   'moisture out through urine and bowels.'],
                                  'cautions': "SURGICAL RED FLAG: Murphy's sign and Charcot's triad must be closely "
                                              'monitored. If high fever (>38.5°C), peritoneal signs (rebound '
                                              'tenderness, rigid board-like abdomen), or septic confusion develop, '
                                              'immediately transfer patient to the nearest Emergency Department for '
                                              'ultrasound and intravenous antibiotic therapy.'}},
    {   'id': 'CASE-027',
        'title': 'Patient Intake: 33yo Female (Bloody Dysuria / Acute UTI - Xue Lin)',
        'category': 'Urogenital & Internal Medicine',
        'patient': {   'age': 33,
                       'gender': 'Female',
                       'occupation': 'Corporate Event Planner',
                       'chief_complaint': 'Sudden onset excruciating burning dysuria with urinary frequency every 15 '
                                          'minutes, suprapubic cramping, and visible dark red blood in urine for 24 '
                                          'hours.',
                       'history': 'High-stress job requiring prolonged standing and holding urine during multi-day '
                                  'conferences. Onset began acutely after a 14-hour workday. Voiding produces intense '
                                  'urethral scalding and only small dribbles of cloudy pinkish-red urine. No prior '
                                  'history of nephrolithiasis. In-clinic dipstick urinalysis shows: Large Blood (+++), '
                                  'Positive Leukocyte Esterase (+++), Positive Nitrites (++), Protein (+). Patient is '
                                  'afebrile (37.2°C).',
                       'four_examinations': {   'inspection': 'Restless, distressed expression; flushed cheeks; Red '
                                                              'tongue body with thick yellow slimy coating '
                                                              'concentrated heavily on the posterior root '
                                                              '(Kidney/Bladder zone).',
                                                'auscultation_olfaction': 'Rapid breathing; groaning upon bladder '
                                                                          'spasms; urine sample has a sharp, foul, '
                                                                          'pungent odor.',
                                                'inquiry': 'Excruciating urethral burning with sharp stabbing '
                                                           'suprapubic pain before and after urination; sensation of '
                                                           'incomplete voiding; dry mouth with bitter taste; '
                                                           'irritability; constipation for 2 days.',
                                                'palpation': 'Marked tenderness on deep palpation over CV3 (Zhongji) '
                                                             'and suprapubic region; NO costovertebral angle (CVA) '
                                                             'tenderness upon bilateral kidney punch percussion; '
                                                             'radial pulse is Slippery (Hua) and Rapid (Shuo).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Diagnosis & Pattern Differentiation (Lin Syndrome)',
                                             'prompt': 'What is the primary TCM pattern for acute burning dysuria with '
                                                       'hematuria, suprapubic pain, thick yellow coating on the tongue '
                                                       'root, and a slippery-rapid pulse?',
                                             'options': [   'A. Qi Lin (Qi Dysuria) due to Liver Qi Stagnation',
                                                            'B. Xue Lin (Blood Dysuria) due to Lower Jiao Damp-Heat '
                                                            'Injuring Blood Vessels',
                                                            'C. Gao Lin (Chylous Dysuria) due to Kidney Deficiency',
                                                            'D. Shi Lin (Stone Dysuria) due to Urinary Calculus '
                                                            'Obstruction without Infection'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Qi Lin presents with '
                                                                      'hypochondriac fullness and hesitant urination '
                                                                      'aggravated by anger/stress, without gross '
                                                                      'hematuria or purulent nitrites.',
                                                                 'B': '✅ **Correct (Xue Lin / Blood Dysuria):** '
                                                                      'Pathogenic Damp-Heat descends and accumulates '
                                                                      'in the Bladder. The intense heat injures local '
                                                                      'capillary vessels, forcing blood to spill into '
                                                                      'the urine (Xue Lin). Characterized by scalding '
                                                                      'dysuria, hematuria, thick yellow tongue root '
                                                                      'coat, and a slippery-rapid pulse.',
                                                                 'C': '❌ **Incorrect:** Gao Lin presents with milky, '
                                                                      'turbid, rice-water or fatty urine from Kidney '
                                                                      'failure to secure essence.',
                                                                 'D': '❌ **Incorrect:** Shi Lin produces sudden '
                                                                      'agonizing loin-to-groin colic from physical '
                                                                      'stone movement with interrupted urinary stream, '
                                                                      'often without the systemic foul damp-heat '
                                                                      'coating.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Cardinal Point Prescription for Lower Jiao Damp-Heat',
                                             'prompt': 'Which acupuncture prescription directly targets the Bladder '
                                                       'Mu-Shu points, drains Damp-Heat, and stops hematuria?',
                                             'options': [   'A. BL28 (Pangguangshu), CV3 (Zhongji), SP9 (Yinlingquan), '
                                                            'BL63 (Jinmen), SP10 (Xuehai), SP6 (Sanyinjiao)',
                                                            'B. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 '
                                                            '(Mingmen), BL52 (Zhishi)',
                                                            'C. LU7 (Lieque), KI6 (Zhaohai), BL13 (Feishu), HT6 '
                                                            '(Yinxi), LU9 (Taiyuan)',
                                                            'D. ST36 (Zusanli), CV12 (Zhongwan), SP3 (Taibai), BL20 '
                                                            '(Pishu)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** BL28 + CV3 (Back-Shu and '
                                                                      'Front-Mu of Bladder) directly clear heat and '
                                                                      'unblock the lower waterways; SP9 (He-Sea) '
                                                                      'drains dampness; BL63 (Xi-Cleft of Bladder) '
                                                                      'rapidly relieves acute excruciating urethral '
                                                                      'pain and spasm; SP10 (Sea of Blood) cools blood '
                                                                      'and halts hematuria; and SP6 harmonizes the '
                                                                      'three lower Yin channels.',
                                                                 'B': '❌ **Incorrect:** Kidney Yang tonification with '
                                                                      'Mingmen moxibustion is contraindicated in acute '
                                                                      'infectious Damp-Heat.',
                                                                 'C': '❌ **Incorrect:** Lung/Kidney Yin tonic formula '
                                                                      'for respiratory disorders.',
                                                                 'D': '❌ **Incorrect:** Middle jiao digestive '
                                                                      'tonification formula.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Clinical Assessment & Red Flag Protocol',
                                             'prompt': 'Which physical examination finding is essential to confirm '
                                                       'that an acute lower urinary tract infection has NOT ascended '
                                                       'into acute pyelonephritis?',
                                             'options': [   'A. Absence of bilateral Costovertebral Angle (CVA) '
                                                            'tenderness on gentle percussion.',
                                                            'B. Presence of abdominal guarding in the right iliac '
                                                            'fossa.',
                                                            'C. Presence of swollen cervical lymph nodes.',
                                                            'D. Absence of knee reflex.'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** Percussing the 12th rib '
                                                                      "costovertebral angle (Murphy's kidney punch) "
                                                                      'tests for renal parenchymal inflammation. In '
                                                                      'uncomplicated lower UTI (cystitis), CVA '
                                                                      'tenderness is negative. If positive and '
                                                                      'accompanied by high fever, shaking rigors, '
                                                                      'nausea, and flank pain, it indicates acute '
                                                                      'pyelonephritis—an urgent medical condition '
                                                                      'requiring immediate antibiotic therapy.',
                                                                 'B': "❌ **Incorrect:** McBurney's sign indicates "
                                                                      'appendicitis.',
                                                                 'C': '❌ **Incorrect:** Upper respiratory / pharyngeal '
                                                                      'sign.',
                                                                 'D': '❌ **Incorrect:** Neurological reflex '
                                                                      'testing.'}}],
        'standard_diagnosis': {   'patterns': [   'Lower Jiao Damp-Heat Invading Urinary Bladder with Blood Vessel '
                                                  'Injury (Pang Guang Shi Re, Xue Lin)',
                                                  'Acute Hematuric Dysuria (Urinary Tract Infection)'],
                                  'treatment_principles': [   'Clear Heat, Drain Dampness, and Unblock the Lower '
                                                              'Waterways (清热利湿，通淋止痛)',
                                                              'Cool Blood and Arrest Hematuria (凉血止血)'],
                                  'cardinal_points': ['BL28', 'CV3', 'SP9', 'BL63', 'SP10', 'SP6'],
                                  'synergies': [   'Bladder Mu-Shu pair (CV3 Zhongji + BL28 Pangguangshu) directly '
                                                   'regulates bladder Qi transformation and expels pathogenic heat.',
                                                   'Xi-Cleft analgesic strategy (BL63 Jinmen) arrests acute bladder '
                                                   'spasms and scalding urethral pain.',
                                                   'Blood-cooling astringent pair (SP10 Xuehai + SP6 Sanyinjiao) '
                                                   'clears vascular heat and stops urinary bleeding.'],
                                  'cautions': 'MEDICAL RED FLAG: Always perform CVA percussion. If patient develops '
                                              'high fever (>38.5°C), flank pain, shaking chills, or vomiting, '
                                              'immediate antibiotic referral for ascending pyelonephritis is '
                                              'mandatory. Ensure patient drinks copious warm water/cranberry tea and '
                                              'does not delay micturition.'}},
    {   'id': 'CASE-028',
        'title': 'Patient Intake: 63yo Male (Late-Stage Xiao Ke / Diabetic Retinopathy & Cataract)',
        'category': 'Endocrine & Sensory',
        'patient': {   'age': 63,
                       'gender': 'Male',
                       'occupation': 'Retired Postal Clerk',
                       'chief_complaint': 'Progressive visual blurring with dark floating spots, accompanied by severe '
                                          'thirst, urination 5 to 6 times per night, and lumbar weakness in a patient '
                                          'with 15-year type 2 diabetes.',
                       'history': 'Diagnosed with type 2 diabetes mellitus 15 years ago; currently on metformin and '
                                  'evening basal insulin. HbA1c is 8.6%. Recent ophthalmological evaluation reveals '
                                  'bilateral non-proliferative diabetic retinopathy and early posterior subcapsular '
                                  'cataracts. Patient complains of unquenchable thirst, frequent voluminous urination '
                                  'of turbid urine resembling fat, dry mouth, persistent tinnitus, and chronic lower '
                                  'back and knee soreness.',
                       'four_examinations': {   'inspection': 'Emaciated body frame; dark, lusterless, sallow '
                                                              'complexion with dark circles under the eyes; dull '
                                                              'vacant eye gaze; Red tongue body with dry peeled center '
                                                              'cracks (mirror tongue) and little or no coating.',
                                                'auscultation_olfaction': 'Low feeble voice; slow quiet respiration.',
                                                'inquiry': 'Constant thirst with massive water intake; urine is '
                                                           'greasy/turbid; visual acuity deteriorating; floaters '
                                                           'described as dark cobwebs; severe lumbar ache and weak '
                                                           'rubbery knees; dry stools.',
                                                'palpation': 'Weak lumbar musculature; stocking-distribution decreased '
                                                             'sensation on bilateral feet (diabetic sensory '
                                                             'neuropathy); radial pulse is Deep (Chen), Fine/Thready '
                                                             '(Xi), and Weak in both Chi positions.'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Diagnosis according to Three Jiao Xiao Ke Classification',
                                             'prompt': 'What is the primary TCM pattern for this patient presenting '
                                                       'with copious turbid urination, severe polydipsia, blurred '
                                                       'vision, lumbar weakness, red peeled tongue, and deep thready '
                                                       'weak pulse?',
                                             'options': [   'A. Upper Jiao Xiao Ke (Lung Heat Scorching Fluids)',
                                                            'B. Middle Jiao Xiao Ke (Stomach Heat Blazing)',
                                                            'C. Lower Jiao Xiao Ke with Liver and Kidney Yin '
                                                            'Deficiency (Xia Xiao / Shen Yin Xu)',
                                                            'D. Pure Spleen Yang Deficiency with Cold Fluid '
                                                            'Accumulation'],
                                             'correct_index': 2,
                                             'explanations': {   'A': '❌ **Incorrect:** Upper Jiao Xiao Ke is '
                                                                      'characterized primarily by excessive thirst '
                                                                      '(drinking dozens of glasses of water) due to '
                                                                      'Lung heat, without copious fatty urine or '
                                                                      'diabetic retinopathy.',
                                                                 'B': '❌ **Incorrect:** Middle Jiao Xiao Ke features '
                                                                      'voracious hunger (Xiao Gu Shan Ji) with rapid '
                                                                      'weight loss and severe constipation from '
                                                                      'Stomach Fire, rather than primary nocturia and '
                                                                      'visual decay.',
                                                                 'C': '✅ **Correct (Lower Jiao Xiao Ke / Kidney & '
                                                                      'Liver Yin Deficiency):** Chronic Xiao Ke '
                                                                      'consumes the True Yin of the Kidneys and Liver. '
                                                                      'Kidney Yin deficiency fails to secure urine, '
                                                                      'creating turbid fatty urine (Xiao Ke). Liver '
                                                                      'Yin and Blood deficiency fails to nourish the '
                                                                      'eyes, causing diabetic retinopathy and '
                                                                      'cataracts (Nei Zhang). Characterized by lumbar '
                                                                      'soreness, red peeled tongue, and deep thready '
                                                                      'weak Chi pulse.',
                                                                 'D': '❌ **Incorrect:** Spleen Yang deficiency '
                                                                      'produces watery diarrhea, edema, and cold '
                                                                      'limbs, not unquenchable thirst or dry peeled '
                                                                      'mirror tongue.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Comprehensive Point Prescription & Channel Strategy',
                                             'prompt': 'Which point formulation addresses both the Lower Jiao Kidney '
                                                       'Yin root and the visual degradation according to combined '
                                                       'textbook standards?',
                                             'options': [   'A. KI3 (Taixi), BL23 (Shenshu), CV4 (Guanyuan), SP6 '
                                                            '(Sanyinjiao), BL18 (Ganshu), GB37 (Guangming), BL1 '
                                                            '(Jingming), ST36 (Zusanli)',
                                                            'B. LI11 (Quchi), ST44 (Neiting), GV14 (Dazhui), LI4 '
                                                            '(Hegu), ST25 (Tianshu)',
                                                            'C. LU7 (Lieque), LI4 (Hegu), BL13 (Feishu), LU5 (Chize), '
                                                            'LU10 (Yuji)',
                                                            'D. BL28 (Pangguangshu), CV3 (Zhongji), SP9 (Yinlingquan), '
                                                            'BL63 (Jinmen)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** KI3 + BL23 + CV4 tonify Kidney '
                                                                      'Yin and consolidate the lower gates; SP6 '
                                                                      'harmonizes the three lower Yin; BL18 (Liver '
                                                                      'Back-Shu) and GB37 (Luo-Connecting of '
                                                                      "Gallbladder, renowned as the 'Bright Light' "
                                                                      'point) nourish Liver Blood and directly benefit '
                                                                      'the eyes; BL1 (Jingming) improves local retinal '
                                                                      'and ocular microcirculation; and ST36 supports '
                                                                      'postnatal Qi.',
                                                                 'B': '❌ **Incorrect:** Vigorous heat-clearing formula '
                                                                      'for acute excess fire.',
                                                                 'C': '❌ **Incorrect:** Formula for acute Lung '
                                                                      'wind-heat.',
                                                                 'D': '❌ **Incorrect:** Formula for acute urinary '
                                                                      'tract damp-heat (Lin syndrome).'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Precision Needling Technique for BL1 (Jingming)',
                                             'prompt': 'What is the mandatory clinical needling technique for BL1 '
                                                       '(Jingming) to ensure patient safety and avoid orbital '
                                                       'hematoma?',
                                             'options': [   'A. Ask the patient to keep their eyes open; insert '
                                                            'rapidly 1.5 cun perpendicularly with vigorous twirling.',
                                                            'B. Ask patient to close eyes gently; push eyeball '
                                                            'laterally with clean thumb/index finger; insert needle '
                                                            'slowly 0.5-1.0 cun along the medial orbital wall without '
                                                            'lifting, thrusting, or rotating.',
                                                            'C. Apply strong electroacupuncture across bilateral BL1 '
                                                            'at 100 Hz for 30 minutes.',
                                                            'D. Puncture horizontally across the bridge of the nose.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect (High Risk):** Never needle with '
                                                                      'eyes open or use vigorous manipulation near the '
                                                                      'eyeball; this punctures the ophthalmic artery '
                                                                      'and causes retrobulbar hematoma (Deadman safety '
                                                                      'alert).',
                                                                 'B': '✅ **Correct (CAM & Deadman Safety):** Patient '
                                                                      'closes eyes; acupuncturist gently pushes the '
                                                                      'eyeball laterally to create a safe needle path; '
                                                                      'puncture slowly and smoothly 0.5-1.0 cun along '
                                                                      'the orbital margin. Absolutely NO lifting, '
                                                                      'thrusting, or twirling. Upon needle withdrawal, '
                                                                      'apply firm sterile pressure with cotton ball '
                                                                      'for 1-2 minutes.',
                                                                 'C': '❌ **Incorrect:** Electroacupuncture is strictly '
                                                                      'contraindicated at BL1 Jingming.',
                                                                 'D': '❌ **Incorrect:** Does not stimulate the '
                                                                      'Jingming point.'}}],
        'standard_diagnosis': {   'patterns': [   'Lower Jiao Wasting & Thirsting (Xia Xiao / 下消)',
                                                  'Liver and Kidney Yin Deficiency with Essence Depletion and Ocular '
                                                  'Malnutrition (Gan Shen Yin Xu, Nei Zhang)'],
                                  'treatment_principles': [   'Nourish Kidney and Liver Yin (滋补肝肾之阴)',
                                                              'Secure Essence, Quench Thirst, and Brighten the Eyes '
                                                              '(固精生津，清肝明目)'],
                                  'cardinal_points': ['KI3', 'BL23', 'CV4', 'SP6', 'BL18', 'GB37', 'BL1', 'ST36'],
                                  'synergies': [   'Ocular Luo-Shu combination (BL18 Ganshu + GB37 Guangming) directly '
                                                   'floods the optic nerve and retina with enriched Liver Blood.',
                                                   'Lower Jiao Yin-Anchor (KI3 Taixi + CV4 Guanyuan) stops turbid '
                                                   'urinary leakage and regenerates True Water.',
                                                   'Three Leg Yin Bridge (SP6 Sanyinjiao) pulls excessive fire '
                                                   'downward and nourishes body fluids.'],
                                  'cautions': 'OCULAR SAFETY PROTOCOL: Needle BL1 Jingming with extreme caution. No '
                                              'manipulation; compress site for 2 minutes after removal. Diabetic '
                                              'patients have compromised peripheral microcirculation and delayed wound '
                                              'healing; inspect feet at every visit and avoid aggressive moxibustion '
                                              'on diabetic extremities to prevent burns and diabetic foot ulcers.'}},
    {   'id': 'CASE-029',
        'title': 'Patient Intake: 41yo Female (Uterine Bleeding / Spleen Not Controlling Blood - Beng Lou)',
        'category': 'Gynecology & Obstetrics',
        'patient': {   'age': 41,
                       'gender': 'Female',
                       'occupation': 'Middle School Counselor',
                       'chief_complaint': 'Persistent, continuous, pale watery uterine bleeding for 18 days '
                                          'accompanied by profound exhaustion, severe dizziness upon standing, and '
                                          'shortness of breath.',
                       'history': 'History of long hours of mental overwork, worry, and irregular meals. Menses '
                                  'historically heavy but would stop within 6 days. This cycle began as a heavy flood '
                                  'that failed to halt, continuing as a constant daily trickling (Lou) of thin pale '
                                  'blood without clots. Gynecological ultrasound is negative for fibroids, polyps, or '
                                  'endometrial hyperplasia. Complete blood count shows Hemoglobin 88 g/L (microcytic '
                                  'hypochromic anemia). Patient is pale, cold, and exhausted.',
                       'four_examinations': {   'inspection': 'Ashen, lusterless, sallow facial complexion; pale '
                                                              'conjunctiva, lips, and nailbeds; weak slumping posture; '
                                                              'Pale and swollen tongue body with scalloped teeth marks '
                                                              'and thin moist white coating.',
                                                'auscultation_olfaction': 'Soft, feeble, breathy voice; frequent '
                                                                          'sighing; disinclined to speak due to '
                                                                          'shortness of breath.',
                                                'inquiry': 'Constant trickling of pale watery blood without foul odor '
                                                           'or dark clots; severe orthostatic lightheadedness; '
                                                           'palpitations upon minor exertion; cold intolerance; poor '
                                                           'appetite; loose watery stools; spontaneous sweating.',
                                                'palpation': 'Soft, flaccid, non-tender lower abdomen; cool '
                                                             'extremities to touch; radial pulse is Deficient (Xu), '
                                                             'Soft/Soggy (Ru), and Thready (Xi).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation for Uterine Bleeding (Beng Lou)',
                                             'prompt': 'What is the primary TCM pattern for prolonged pale thin '
                                                       'uterine bleeding, sallow complexion, fatigue, poor appetite, '
                                                       'pale tongue with teeth marks, and a weak thready pulse?',
                                             'options': [   'A. Blood Heat Invading Chong and Ren Channels',
                                                            'B. Spleen Failing to Control Blood (Pi Bu Tong Xue)',
                                                            'C. Blood Stasis Obstructing the Uterus (Han Ning Xue Yu)',
                                                            'D. Liver Fire Blazing Causing Reckless Blood Flow'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Blood Heat produces sudden '
                                                                      'profuse bright red or dark purple thick '
                                                                      'bleeding with clots, thirst, mental '
                                                                      'restlessness, red tongue with yellow coat, and '
                                                                      'rapid pulse.',
                                                                 'B': '✅ **Correct (Spleen Not Controlling Blood):** '
                                                                      'Spleen Qi commands and holds the blood within '
                                                                      'the vessels (Tong Xue). Chronic worry and '
                                                                      'overwork exhaust Spleen Qi, which loses its '
                                                                      'astringent holding power, allowing blood to '
                                                                      'leak continuously from the Chong and Ren '
                                                                      'channels (Beng Lou). Characterized by pale thin '
                                                                      'blood, fatigue, teeth marks on a pale tongue, '
                                                                      'and a weak thready pulse.',
                                                                 'C': '❌ **Incorrect:** Blood Stasis presents with '
                                                                      'sharp stabbing lower abdominal pain aggravated '
                                                                      'by pressure, dark purplish blood with large '
                                                                      'clots, and purple tongue with choppy pulse.',
                                                                 'D': '❌ **Incorrect:** Liver Fire presents with '
                                                                      'wiry-rapid pulse, bitter taste, temporal '
                                                                      'headaches, and thick red blood.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Cardinal Point & Moxibustion Technique',
                                             'prompt': 'Which acupuncture point and treatment modality is the renowned '
                                                       'textbook emergency master method to stop chronic uterine '
                                                       'bleeding from Spleen deficiency?',
                                             'options': [   'A. Bleeding the ear apex (Erjian) with a lancet.',
                                                            'B. Direct moxibustion (moxa cone or stick) on SP1 (Yinbai '
                                                            '/ 隐白).',
                                                            'C. Heavy reducing manipulation on LR3 (Taichong) and LI4 '
                                                            '(Hegu).',
                                                            'D. Puncturing CV3 (Zhongji) deeply with electrical '
                                                            'stimulation.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Erjian bleeding clears extreme '
                                                                      'excess heat, contraindicated in Qi-deficiency '
                                                                      'hemorrhage.',
                                                                 'B': '✅ **Correct (Moxa on SP1 Yinbai):** SP1 '
                                                                      '(Jing-Well wood point of Spleen Taiyin) is the '
                                                                      'premier classical master point for uterine '
                                                                      'hemorrhage. Direct or stick moxibustion on SP1 '
                                                                      'strongly stimulates Spleen Qi, astringes '
                                                                      'vessels, elevates sunken Yang, and arrests '
                                                                      'uterine flooding and trickling (Beng Lou).',
                                                                 'C': '❌ **Incorrect:** Strong reducing on Four Gates '
                                                                      'is a dispersing technique that would aggravate '
                                                                      'bleeding.',
                                                                 'D': '❌ **Incorrect:** Deep needling at CV3 can '
                                                                      'injure an enlarged bladder or uterus, not '
                                                                      'indicated for chronic hemorrhage.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Comprehensive Supportive Point Formula',
                                             'prompt': 'Which supporting point combination best tonifies Spleen Qi, '
                                                       'lifts sunken Yang, and manages blood volume?',
                                             'options': [   'A. SP10 (Xuehai), SP6 (Sanyinjiao), BL20 (Pishu), CV6 '
                                                            '(Qihai), GV20 (Baihui), ST36 (Zusanli)',
                                                            'B. LI11 (Quchi), ST44 (Neiting), GV14 (Dazhui), SP9 '
                                                            '(Yinlingquan)',
                                                            'C. BL28 (Pangguangshu), CV3 (Zhongji), BL63 (Jinmen)',
                                                            'D. KI3 (Taixi), BL23 (Shenshu), CV4 (Guanyuan) without '
                                                            'moxa'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** SP10 regulates the Sea of Blood; '
                                                                      'SP6 harmonizes the three leg Yin; BL20 directly '
                                                                      'tonifies Spleen Qi; CV6 (Sea of Qi) and ST36 '
                                                                      'boost postnatal Qi production; and GV20 (Baihui '
                                                                      'with moxa) raises sunken Yang Qi to halt '
                                                                      'downward leakage of blood.',
                                                                 'B': '❌ **Incorrect:** Pure heat-clearing formula.',
                                                                 'C': '❌ **Incorrect:** Formula for urinary tract '
                                                                      'infection.',
                                                                 'D': '❌ **Incorrect:** Tonifies Kidney Yin, but lacks '
                                                                      'the specific Spleen blood-holding points.'}}],
        'standard_diagnosis': {   'patterns': [   'Spleen Failing to Control Blood (Pi Bu Tong Xue / 脾不统血)',
                                                  'Chong and Ren Channel Instability with Flooding and Trickling (Beng '
                                                  'Lou / 崩漏)'],
                                  'treatment_principles': [   'Tonify Spleen Qi, Raise Sunken Yang, and Astringe '
                                                              'Hemorrhage (健脾益气，摄血固冲)',
                                                              'Nourish Qi and Blood to Restore Hemodynamic Stability '
                                                              '(益气生血)'],
                                  'cardinal_points': ['SP1', 'SP10', 'SP6', 'BL20', 'CV6', 'GV20', 'ST36'],
                                  'synergies': [   'Classical Hemostatic Master (SP1 Yinbai with moxa) astringes '
                                                   'bleeding and anchors Spleen Qi.',
                                                   'Yang-Lifting duo (GV20 Baihui + CV6 Qihai) raises sunken Qi to '
                                                   'halt downward pelvic flooding.',
                                                   'Blood-Holding pair (BL20 Pishu + SP10 Xuehai) restores vessel '
                                                   'integrity and splenic control over blood.'],
                                  'cautions': 'HEMODYNAMIC RED FLAG: Severe acute uterine hemorrhage can cause '
                                              'hypovolemic shock. If patient presents with blood pressure <90/60 mmHg, '
                                              'heart rate >110 bpm, syncopal collapse, or hemoglobin <70 g/L, initiate '
                                              'emergency transport for intravenous fluid resuscitation and blood '
                                              'transfusion.'}},
    {   'id': 'CASE-030',
        'title': "Patient Intake: 50yo Male (Involuntary Facial Hemispasm / Post-Bell's Palsy)",
        'category': 'Neurological & Sensory',
        'patient': {   'age': 50,
                       'gender': 'Male',
                       'occupation': 'Commercial Driver',
                       'chief_complaint': 'Involuntary, rhythmic, twitching spasms of the left eyelid and corner of '
                                          'the mouth, occurring multiple times an hour for 3 months following '
                                          "incomplete recovery from Bell's palsy.",
                       'history': "Suffered acute idiopathic facial nerve paralysis (Bell's palsy) 4 months ago after "
                                  "driving long distances with the driver's side window open in cold rainy weather. "
                                  'The acute flaccidity resolved partially with oral corticosteroids and acupuncture, '
                                  'but over the last 12 weeks, abnormal involuntary spasms developed on the left side '
                                  'of the face. Spasms are triggered by talking, chewing, emotional tension, and '
                                  'exposure to air conditioning.',
                       'four_examinations': {   'inspection': 'Left palpebral fissure narrows intermittently during '
                                                              'spasm; corner of left mouth twitches and pulls '
                                                              'laterally and upward; mild contracture of left '
                                                              'nasolabial fold; Pale slightly swollen tongue body with '
                                                              'thin white greasy coating.',
                                                'auscultation_olfaction': 'Occasional speech hesitation and mild '
                                                                          'articulation slurring during active spasms; '
                                                                          'heavy sighing.',
                                                'inquiry': 'Tightness, stiffness, and crawling sensation (formication) '
                                                           'across left cheek and jaw; spasms worsen dramatically '
                                                           'under fatigue or stress; difficulty reading due to left '
                                                           'eyelid twitching; neck and shoulder tension.',
                                                'palpation': 'Hypertonic, taut, irritable bands in the left '
                                                             'zygomaticus major, orbicularis oculi, and masseter '
                                                             'muscles; exquisite tenderness over left GB20 and '
                                                             'Taiyang; radial pulse is Wiry (Xian) and Slippery '
                                                             '(Hua).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Pathophysiology & TCM Pattern Identification',
                                             'prompt': 'What is the primary TCM pattern for post-paralytic facial '
                                                       'spasms characterized by involuntary twitching, localized '
                                                       'stiffness, pale swollen tongue with greasy coat, and a '
                                                       'wiry-slippery pulse?',
                                             'options': [   'A. Extreme Heat Generating Liver Wind',
                                                            'B. Wind-Phlegm and Blood Stasis Obstructing Facial '
                                                            'Channels (Zhong Luo / Mian Ji)',
                                                            'C. Kidney Yang Deficiency with Cold Accumulation',
                                                            'D. Acute Exterior Wind-Cold Invading Taiyang'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Extreme Heat generating Wind '
                                                                      'produces high fevers, generalized convulsions, '
                                                                      'stiff neck, and deep red tongue.',
                                                                 'B': '✅ **Correct (Wind-Phlegm Obstructing Facial '
                                                                      "Channels):** Incomplete recovery from Bell's "
                                                                      'palsy leaves residual pathogenic Wind and '
                                                                      'Phlegm lodged in the Yangming and Shaoyang '
                                                                      'channels of the face. Qi and Blood stasis in '
                                                                      'the collaterals causes malnutrition and '
                                                                      'hyperirritability of the facial sinews, '
                                                                      'producing involuntary spasms (Mian Ji). '
                                                                      'Characterized by local twitching, greasy coat, '
                                                                      'and a wiry-slippery pulse.',
                                                                 'C': '❌ **Incorrect:** Kidney Yang deficiency '
                                                                      'presents with cold limbs, lumbago, pale profuse '
                                                                      'urine, and deep slow pulse.',
                                                                 'D': '❌ **Incorrect:** Acute Wind-Cold invasion was '
                                                                      'the initial trigger 4 months ago, but the '
                                                                      'current chronic spasm represents channel sinew '
                                                                      'malnourishment and internal Wind-Phlegm.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Point Prescription & Local Needling Technique',
                                             'prompt': 'Which acupuncture prescription and technique is most effective '
                                                       'to relax spastic facial sinews without triggering further '
                                                       'muscular contracture?',
                                             'options': [   'A. Deep perpendicular needling into the facial nerve '
                                                            'trunk with continuous 50 Hz electroacupuncture.',
                                                            'B. Subcutaneous/transverse shallow insertion across local '
                                                            'points: ST4 (Dicang) joined to ST6 (Jiache), Taiyang '
                                                            'joined to GB1, GB20 (Fengchi), LI4 (Hegu), and LR3 '
                                                            '(Taichong).',
                                                            'C. Direct moxibustion burns directly on the orbicularis '
                                                            'oculi muscle belly.',
                                                            'D. Vigorous deep needle manipulation with strong '
                                                            'electrical current on ST7 and SI18.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect (High Risk):** Aggressive '
                                                                      'electroacupuncture on spastic facial muscles '
                                                                      'triggers severe permanent contracture and '
                                                                      'synkinesis (nerve miswiring).',
                                                                 'B': '✅ **Correct (Transverse Joined Needling & Four '
                                                                      'Gates):** Transverse (subcutaneous) '
                                                                      'through-and-through needling (Tou Xue) such as '
                                                                      'ST4 towards ST6 and Taiyang towards GB1 smooths '
                                                                      'channel Qi and relaxes sinews without '
                                                                      'irritating the facial nerve trunk. Distal '
                                                                      'points LR3 + LI4 (Four Gates) extinguish '
                                                                      'internal wind and unblock collaterals.',
                                                                 'C': '❌ **Incorrect:** Direct scarring moxa on the '
                                                                      'eyelid causes severe skin burns and corneal '
                                                                      'injury.',
                                                                 'D': '❌ **Incorrect:** Strong electrical current '
                                                                      'aggravates facial spasticity.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Clinical Contraindication in Facial Hemispasm',
                                             'prompt': 'What therapeutic modality is specifically CONTRAINDICATED in '
                                                       'the treatment of chronic facial hemispasm / post-paralytic '
                                                       'synkinesis?',
                                             'options': [   'A. Gentle manual feather-touch acupressure along the '
                                                            'jawline.',
                                                            'B. Strong, high-frequency electrical stimulation '
                                                            '(Electroacupuncture) over the spastic facial muscles.',
                                                            'C. Application of warm compress to the preauricular area.',
                                                            'D. Distal needling on LI4 and LR3.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Gentle acupressure is safe and '
                                                                      'therapeutic.',
                                                                 'B': '✅ **Correct (Electroacupuncture '
                                                                      'Contraindicated):** CARB-TCMPA and clinical '
                                                                      'consensus warn that strong electric stimulation '
                                                                      'over spastic facial muscles overexcites the '
                                                                      'facial nerve, promoting abnormal axonal '
                                                                      'branching (synkinesis) and worsening muscle '
                                                                      'spasticity. Treatment must rely on gentle, '
                                                                      'shallow, manual sedating technique.',
                                                                 'C': '❌ **Incorrect:** Warm compress relaxes muscle '
                                                                      'tension and is beneficial.',
                                                                 'D': '❌ **Incorrect:** Distal Four Gates needling is '
                                                                      'highly indicated.'}}],
        'standard_diagnosis': {   'patterns': [   'Wind-Phlegm and Blood Stasis Obstructing Facial Channels (Zhong '
                                                  'Luo, Mian Ji / 面肌痉挛)',
                                                  "Sinew Malnutrition following Facial Paralysis (Bell's Palsy "
                                                  'Sequelae)'],
                                  'treatment_principles': [   'Extinguish Internal Wind, Dissolve Phlegm, and Relax '
                                                              'Facial Sinews (息风化痰，缓痉舒筋)',
                                                              'Unblock Yangming and Shaoyang Channels, Regulate Qi and '
                                                              'Blood (通经活络，调和气血)'],
                                  'cardinal_points': ['ST4', 'ST6', 'Taiyang', 'GB20', 'LI4', 'LR3', 'SJ5'],
                                  'synergies': [   'Joined Facial Sinew pair (ST4 Dicang directed subcutaneously '
                                                   'towards ST6 Jiache) gently releases hypertonic zygomatic and '
                                                   'buccinator muscles.',
                                                   'Four Gates master combination (LI4 Hegu + LR3 Taichong) calms '
                                                   'neuromuscular irritability and extinguishes channel wind.',
                                                   'Occipital Wind-Clearing point (GB20 Fengchi) relieves '
                                                   'cervical-facial nerve tension.'],
                                  'cautions': 'ELECTROACUPUNCTURE CONTRAINDICATION: Absolutely avoid strong electrical '
                                              'stimulation on the face in hemispasm to prevent irreversible '
                                              'synkinesis. Use shallow subcutaneous needling. Advise patient to '
                                              'protect the face from cold drafts and manage psychological stress.'}},
    {   'id': 'CASE-031',
        'title': 'Patient Intake: 71yo Male (Chest Bi / Impending Coronary Infarction - Surgical Red Flag)',
        'category': 'Cardiovascular Emergency & Red Flag',
        'patient': {   'age': 71,
                       'gender': 'Male',
                       'occupation': 'Retired Heavy Crane Operator',
                       'chief_complaint': 'Sudden onset crushing retrosternal chest heaviness radiating down the inner '
                                          'left arm to the little finger, accompanied by nausea, cold profuse '
                                          'sweating, and shortness of breath for 40 minutes.',
                       'history': 'History of hypertension and hyperlipidemia for 20 years. Smoker (1 pack/day for 45 '
                                  'years). Previous episodes of exertional angina relieved within 5 minutes by '
                                  'sublingual nitroglycerin; however, today the pain began while watching television, '
                                  "is significantly more intense ('feels like an elephant standing on my chest'), and "
                                  'failed to resolve after taking two nitroglycerin tablets 15 minutes apart. Patient '
                                  'appears anxious with a sense of impending doom.',
                       'four_examinations': {   'inspection': 'Ashen, grayish, deathly pale complexion; forehead and '
                                                              'upper lip drenched in cold beads of sweat; cyanosis of '
                                                              'lips and nailbeds; Dark Purple tongue body with '
                                                              'prominent stasis macules on the margins and engorged '
                                                              'sublingual veins.',
                                                'auscultation_olfaction': 'Rapid labored panting respiration; weak '
                                                                          'groaning voice; inability to speak in full '
                                                                          'sentences.',
                                                'inquiry': 'Excruciating substernal vise-like pressure; sharp '
                                                           'radiating pain into left shoulder, medial arm, and jaw; '
                                                           'extreme nausea and lightheadedness; feeling of impending '
                                                           'doom.',
                                                'palpation': 'Cold, clammy extremities; radial pulse is '
                                                             'Knotted/Intermittent (Jie Dai), Thready (Xi), and '
                                                             'Irregular with rate 104 bpm; blood pressure is 92/58 '
                                                             'mmHg.'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Medical Red Flag Diagnosis & Immediate Action',
                                             'prompt': 'What is the mandatory immediate clinical action when a patient '
                                                       'presents with crushing substernal chest pain >20 minutes '
                                                       'unresponsive to nitroglycerin, cold diaphoresis, and cyanosis?',
                                             'options': [   'A. Administer a full 45-minute acupuncture treatment '
                                                            'using heavy moxibustion on CV8.',
                                                            'B. Immediately call 911 (Emergency Medical Services); '
                                                            'maintain patient supine, assist with emergency aspirin if '
                                                            'indicated, and monitor airway/breathing/circulation.',
                                                            'C. Tell the patient to drive himself to his family '
                                                            "physician's clinic tomorrow morning.",
                                                            'D. Perform vigorous tuina massage over the upper thoracic '
                                                            'spine.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect (Fatal Delay):** Attempting an '
                                                                      'in-clinic acupuncture session during an acute '
                                                                      'evolving myocardial infarction delays critical '
                                                                      'coronary reperfusion therapy '
                                                                      '(catheterization/thrombolysis) and constitutes '
                                                                      'gross medical malpractice.',
                                                                 'B': '✅ **Correct (Immediate 911 Activation):** '
                                                                      'Crushing retrosternal chest pain radiating to '
                                                                      'the left arm lasting >20 minutes, unresponsive '
                                                                      'to nitroglycerin, accompanied by diaphoresis '
                                                                      'and hypotension, is the hallmark of Acute '
                                                                      'Coronary Syndrome / Acute Myocardial Infarction '
                                                                      '(Chest Bi with Heart Yang Collapse). '
                                                                      'Acupuncturist must immediately dial 911, keep '
                                                                      'the patient resting comfortably, keep the '
                                                                      'airway patent, and prepare for CPR if cardiac '
                                                                      'arrest occurs.',
                                                                 'C': '❌ **Incorrect (Fatal Delay):** Patient could '
                                                                      'experience ventricular fibrillation and cardiac '
                                                                      'arrest within minutes.',
                                                                 'D': '❌ **Incorrect:** Thoracic spinal manipulation '
                                                                      'during acute coronary occlusion is dangerous '
                                                                      'and contraindicated.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Emergency First-Aid Acupressure while Awaiting EMS',
                                             'prompt': 'While emergency medical transport is actively en route, which '
                                                       'point may be stimulated with firm fingertip/fingernail '
                                                       'pressure to stabilize cardiac rhythm and relieve chest '
                                                       'oppression?',
                                             'options': [   'A. PC6 (Neiguan) and HT7 (Shenmen)',
                                                            'B. ST36 (Zusanli) and SP9 (Yinlingquan)',
                                                            'C. GB20 (Fengchi) and LI20 (Yingxiang)',
                                                            'D. BL25 (Dachangshu) and BL28 (Pangguangshu)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (PC6 + HT7 Acupressure):** Firm '
                                                                      'fingernail pressure on PC6 (Neiguan) stimulates '
                                                                      'vagal afferents to improve coronary perfusion '
                                                                      'and ease substernal oppression, while HT7 '
                                                                      '(Shenmen) soothes acute panic and Shen '
                                                                      'agitation while waiting for paramedics.',
                                                                 'B': '❌ **Incorrect:** Digestive points with no '
                                                                      'direct acute coronary action.',
                                                                 'C': '❌ **Incorrect:** Head/nasal points.',
                                                                 'D': '❌ **Incorrect:** Lower bowel/bladder points.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. TCM Pattern & Post-Stabilization Cardinal Formula',
                                             'prompt': 'What is the primary TCM pattern and textbook cardinal point '
                                                       'formula for Chest Bi due to severe Heart Blood Stasis and Yang '
                                                       'Qi collapse once hospitalized and medically stabilized?',
                                             'options': [   'A. Pattern: Heart Blood Stasis with Heart Yang Collapse; '
                                                            'Formula: PC6 (Neiguan), PC4 (Ximen), HT7 (Shenmen), BL15 '
                                                            '(Xinshu), BL17 (Geshu), CV17 (Danzhong)',
                                                            'B. Pattern: Lung Yin Deficiency; Formula: LU7, KI6, BL13, '
                                                            'BL43',
                                                            'C. Pattern: Spleen Qi Deficiency; Formula: SP3, ST36, '
                                                            'CV12, BL20',
                                                            'D. Pattern: Liver Fire Blazing; Formula: LR2, GB43, LI11, '
                                                            'ST44'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** PC6 + PC4 (Xi-Cleft) directly '
                                                                      'resolve acute coronary blood stasis; HT7 calms '
                                                                      'the Heart Shen; BL15 + CV17 (Back-Shu and '
                                                                      'Front-Mu / Hui of Qi) restore thoracic Yang Qi; '
                                                                      'and BL17 (Hui of Blood) clears systemic stasis.',
                                                                 'B': '❌ **Incorrect:** Respiratory formula.',
                                                                 'C': '❌ **Incorrect:** Spleen digestive formula.',
                                                                 'D': '❌ **Incorrect:** Liver fire formula.'}}],
        'standard_diagnosis': {   'patterns': [   'Severe Heart Blood Stasis with Heart Yang Collapse (Xin Xue Yu Zu, '
                                                  'Xin Yang Shuai Jie)',
                                                  'True Heart Pain / Acute Coronary Syndrome (Zhen Xin Tong / 胸痹心痛)'],
                                  'treatment_principles': [   'EMERGENCY PROTOCOL: Immediate 911 Activation & Hospital '
                                                              'Transfer',
                                                              'Invigorate Heart Blood, Dissolve Stasis, and Warm '
                                                              'Thoracic Yang (活血化瘀，通阳开痹)',
                                                              'Stabilize Coronary Collaterals and Regulate Cardiac '
                                                              'Shen (理气通络，安定心神)'],
                                  'cardinal_points': ['PC6', 'PC4', 'HT7', 'BL15', 'BL17', 'CV17', 'SP10'],
                                  'synergies': [   'Coronary Xi-Cleft Master pair (PC6 Neiguan + PC4 Ximen) provides '
                                                   'potent opening of cardiac vessels and pain relief.',
                                                   'Thoracic Qi-Blood meeting pair (CV17 Danzhong + BL17 Geshu) moves '
                                                   'chest Qi to propel stagnant blood.',
                                                   'Heart Mu-Shu resonance (CV14 Juque + BL15 Xinshu) restores cardiac '
                                                   'rhythm.'],
                                  'cautions': 'CARDIAC RED FLAG: Never attempt in-office acupuncture as primary '
                                              'therapy for acute evolving MI. Always record exact onset time, keep '
                                              'patient calm and resting supine, withhold food/fluids, confirm aspirin '
                                              'status, and monitor vital signs until EMS takes over.'}},
    {   'id': 'CASE-032',
        'title': 'Patient Intake: 29yo Male (Phlegm-Fire Agitating Shen / Manic Disorder - Kuang Zheng)',
        'category': 'Psychiatric & Mental Health',
        'patient': {   'age': 29,
                       'gender': 'Male',
                       'occupation': 'Nightclub Promoter',
                       'chief_complaint': 'Acute onset manic agitation, relentless rapid incoherent speech, '
                                          'sleeplessness for 5 consecutive nights, aggressive posturing, and '
                                          'uncontrolled shouting.',
                       'history': 'Escalated acutely after a 7-day binge of hard alcohol, stimulants, spicy food, and '
                                  'intense interpersonal disputes. Family reports patient has been singing from the '
                                  'rooftop, disrobing, pacing relentlessly, and claiming supernatural powers. Has not '
                                  'slept in over 100 hours. Refuses to sit still or eat normal meals. Brought to '
                                  'clinical attention by concerned family members.',
                       'four_examinations': {   'inspection': 'Glaring bloodshot eyes; crimson flushed face; chaotic '
                                                              'pacing with hyperactive gestures; violent muscular '
                                                              'posturing; Red tongue body with thick, greasy, '
                                                              'foul-smelling yellow coating.',
                                                'auscultation_olfaction': 'Loud, coarse, incessant speech; rapid '
                                                                          'incoherent rambling; aggressive shouting; '
                                                                          'heavy panting respiration.',
                                                'inquiry': 'Patient declares he is immune to sleep and possesses '
                                                           'limitless energy; reports boiling heat in chest; thirst '
                                                           'with desire for cold drinks; constipated for 4 days with '
                                                           'foul-smelling dry stool; dark burning urine.',
                                                'palpation': 'Warm hyperdynamic skin; forceful, Slippery (Hua), and '
                                                             'Rapid (Shuo) radial pulse with fullness in both Guan and '
                                                             'Cun positions.'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Pattern Differentiation in Classical Psychiatric Disorders '
                                                      '(Dian Kuang)',
                                             'prompt': 'What is the classic TCM diagnosis for this presentation of '
                                                       'acute manic agitation, incoherent shouting, zero sleep, red '
                                                       'eyes, yellow slimy tongue coat, and a slippery-rapid pulse?',
                                             'options': [   'A. Dian Syndrome (Depressive / Phlegm-Damp Stagnation)',
                                                            'B. Kuang Syndrome (Manic Disorder due to Phlegm-Fire '
                                                            'Agitating the Shen / Tan Huo Rao Xin)',
                                                            'C. Heart and Kidney Non-Interaction with Yin Deficiency',
                                                            'D. Spleen and Heart Blood Deficiency'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect (Dian Syndrome):** Dian is '
                                                                      'characterized by depressive withdrawal, mutism, '
                                                                      'stupor, incoherent whispering, and introversion '
                                                                      'caused by Phlegm-Damp misting the mind. Kuang '
                                                                      'is the manic Yang opposite (agitated, shouting, '
                                                                      'violent).',
                                                                 'B': '✅ **Correct (Kuang Syndrome / Phlegm-Fire '
                                                                      'Agitating Shen):** Alcohol, emotional rage, and '
                                                                      'rich food generate intense toxic Fire that '
                                                                      'condenses bodily fluids into sticky Phlegm. '
                                                                      'Phlegm-Fire rushes upward to harass the Heart '
                                                                      'and cloud the Shen, producing manic agitation '
                                                                      '(Kuang Zheng), uninhibited speech, supercharged '
                                                                      'Yang energy, yellow greasy coat, and a '
                                                                      'slippery-rapid pulse.',
                                                                 'C': '❌ **Incorrect:** Heart-Kidney disharmony '
                                                                      'produces insomnia, night sweats, lower back '
                                                                      'soreness, and a fine rapid pulse without manic '
                                                                      'violence.',
                                                                 'D': '❌ **Incorrect:** Blood deficiency causes '
                                                                      'fatigue, sadness, poor memory, and pale '
                                                                      'tongue.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Point Prescription & Phlegm-Clearing Strategy',
                                             'prompt': 'Which acupuncture prescription directly purges toxic '
                                                       'Phlegm-Fire from the Heart and anchors the agitated Shen?',
                                             'options': [   'A. PC5 (Jianshi), ST40 (Fenglong), GV26 (Renzhong), GV14 '
                                                            '(Dazhui), HT7 (Shenmen), SP1 (Yinbai), LI11 (Quchi)',
                                                            'B. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 '
                                                            '(Mingmen), SP6 (Sanyinjiao) with moxa',
                                                            'C. LU7 (Lieque), KI6 (Zhaohai), BL13 (Feishu), HT6 '
                                                            '(Yinxi), LU9 (Taiyuan)',
                                                            'D. CV12 (Zhongwan), ST36 (Zusanli), SP3 (Taibai), BL20 '
                                                            '(Pishu)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** PC5 (Jing-River of Pericardium) '
                                                                      'is the renowned point to transform Phlegm in '
                                                                      'the Heart and open the orifices; ST40 (Luo of '
                                                                      'Stomach) dissolves systemic phlegm; GV26 and '
                                                                      'GV14 clear toxic Yang fire and pacify mania; '
                                                                      'HT7 sedates Heart Fire; SP1 (Sun Simiao Ghost '
                                                                      'point) anchors spastic Shen; and LI11 clears '
                                                                      'toxic heat.',
                                                                 'B': '❌ **Incorrect:** Warming Kidney Yang with '
                                                                      'moxibustion is strictly contraindicated in '
                                                                      'blazing Phlegm-Fire.',
                                                                 'C': '❌ **Incorrect:** Respiratory Yin tonic formula.',
                                                                 'D': '❌ **Incorrect:** Digestive tonic formula.'}},
                                         {   'question_id': 'Q3',
                                             'title': "3. Historical Role of Sun Simiao's Ghost Points (Gui Xue)",
                                             'prompt': 'Which point in this prescription is one of the celebrated '
                                                       'Thirteen Ghost Points (Gui Xue) described by Sun Simiao for '
                                                       'acute mania and severe psychological disturbance?',
                                             'options': [   'A. SP1 (Yinbai - Ghost Eye / Gui Yan) and GV26 (Renzhong '
                                                            '- Ghost Palace / Gui Gong)',
                                                            'B. ST36 (Zusanli) and SP9 (Yinlingquan)',
                                                            'C. BL23 (Shenshu) and KI3 (Taixi)',
                                                            'D. LU7 (Lieque) and KI6 (Zhaohai)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Thirteen Ghost Points):** In the '
                                                                      'Tang Dynasty, Sun Simiao codified 13 Ghost '
                                                                      'Points (Gui Xue) specifically for sudden severe '
                                                                      'manic psychosis, delirium, and spiritual '
                                                                      'possession. GV26 (Gui Gong) and SP1 (Gui Yan) '
                                                                      'are two of the premier points utilized to shock '
                                                                      'the mind back to clarity and dispel turbid '
                                                                      'phlegm-fire.',
                                                                 'B': '❌ **Incorrect:** Common lower leg points.',
                                                                 'C': '❌ **Incorrect:** Kidney tonification points.',
                                                                 'D': '❌ **Incorrect:** Confluent channel points.'}}],
        'standard_diagnosis': {   'patterns': [   'Phlegm-Fire Agitating the Shen (Tan Huo Rao Xin / 痰火扰心)',
                                                  'Manic Disorder / Bipolar Mania (Kuang Zheng / 狂证)'],
                                  'treatment_principles': [   'Purge Heart Fire, Dissolve Turbid Phlegm, and Open the '
                                                              'Orifices (清心泻火，化痰开窍)',
                                                              'Anchor the Spirit and Subdue Hyperactive Yang '
                                                              '(镇心安神，平肝熄火)'],
                                  'cardinal_points': ['PC5', 'ST40', 'GV26', 'GV14', 'HT7', 'SP1', 'LI11'],
                                  'synergies': [   'Phlegm-Transforming Master pair (PC5 Jianshi + ST40 Fenglong) '
                                                   'sweeps sticky phlegm out of the pericardial chest and restores '
                                                   'cognitive lucidity.',
                                                   'Ghost Point Anchor pair (GV26 Renzhong + SP1 Yinbai) calms '
                                                   'psychiatric frenzy.',
                                                   'Yang Fire Purging duo (GV14 Dazhui + LI11 Quchi) drains toxic '
                                                   'systemic heat.'],
                                  'cautions': 'PSYCHIATRIC EMERGENCY & SAFETY: Acute manic agitation requires a '
                                              'secure, calm environment with clinical assistants present to prevent '
                                              'harm to self or others. If patient displays active psychosis, severe '
                                              'dehydration, or violent delirium, emergency psychiatric evaluation and '
                                              'medical hospitalization are required.'}},
    {   'id': 'CASE-033',
        'title': 'Patient Intake: 4yo Male (Infantile Food Stagnation & Spleen Impairment - Gan Ji)',
        'category': 'Pediatrics',
        'patient': {   'age': 4,
                       'gender': 'Male',
                       'occupation': 'Preschooler',
                       'chief_complaint': 'Distended swollen abdomen like a drum, emaciated spindly limbs, capricious '
                                          'appetite with pica (eating dirt/chalk), restless night teeth grinding, and '
                                          'alternating bowel habits for 2 months.',
                       'history': 'History of improper weaning and excessive consumption of sugary snacks, pastries, '
                                  'cold milk, and fried chicken nuggets. Over the past 8 weeks, the child became '
                                  'irritable, developed a protruding tympanic belly, lost subcutaneous muscle mass in '
                                  'the limbs, and began grinding his teeth aggressively in sleep. Stool alternates '
                                  'between foul-smelling diarrhea with undigested milk curds and dry pellet '
                                  'constipation.',
                       'four_examinations': {   'inspection': 'Spindly thin arms and legs with swollen protruding '
                                                              'belly (potbelly); dry lusterless sallow face; dry '
                                                              'brittle hair grouped in tufts; Pale tongue body with '
                                                              'thick, greasy, patchy yellow curd-like coating.',
                                                'auscultation_olfaction': 'Loud petulant crying; sour foul odor from '
                                                                          'the mouth (rotten breath); audible '
                                                                          'borborygmi.',
                                                'inquiry': 'Night restlessness with teeth grinding; picky appetite '
                                                           'with cravings for strange non-food substances (paper, '
                                                           'chalk); excessive sweating on forehead during sleep; '
                                                           'irritability.',
                                                'palpation': 'Abdomen feels warm, tight, and distended with tympanic '
                                                             'resonance; superficial venule at the index finger Qi Bar '
                                                             '(气关) is thick, engorged, and dark purplish; pulse is '
                                                             'Slippery (Hua) and Rapid (Shuo).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Pediatric Pattern Identification (Gan Ji)',
                                             'prompt': 'What is the primary TCM diagnosis for a 4yo child presenting '
                                                       'with a potbelly, emaciated limbs, foul breath, night teeth '
                                                       'grinding, thick curd-like tongue coat, and a purple vein at '
                                                       'the Qi bar?',
                                             'options': [   'A. Acute Exterior Wind-Cold Common Cold',
                                                            'B. Infantile Malnutrition due to Food Stagnation and '
                                                            'Spleen Deficiency (Xiao Er Gan Ji / 疳积)',
                                                            'C. Kidney Yin Deficiency with Empty Fire',
                                                            'D. Acute Bacillary Dysentery'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Acute Wind-Cold presents with '
                                                                      'fever, chills, and clear runny nose.',
                                                                 'B': '✅ **Correct (Xiao Er Gan Ji / Infantile '
                                                                      'Nutritional Stagnation):** Improper feeding and '
                                                                      'overindulgence in rich/cold foods impair the '
                                                                      'delicate Spleen and Stomach of young children. '
                                                                      'Food stagnates in the middle burner, fermenting '
                                                                      'into toxic heat and parasites, while Qi and '
                                                                      'Blood production collapses, producing '
                                                                      'emaciation with a protruding potbelly (Gan Ji).',
                                                                 'C': '❌ **Incorrect:** Extremely rare in a 4yo child; '
                                                                      'does not produce food accumulation potbelly.',
                                                                 'D': '❌ **Incorrect:** Dysentery features acute high '
                                                                      'fever, tenesmus, and constant bloody pus in '
                                                                      'stool.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Legendary Pediatric Extra Point Technique (Sifeng)',
                                             'prompt': 'Which specialized pediatric extra acupuncture point is pricked '
                                                       'to express a drop of clear yellowish fluid to resolve chronic '
                                                       'food accumulation and malnutrition?',
                                             'options': [   'A. Sifeng (EX-UE10 / 四缝)',
                                                            'B. Shixuan (EX-UE11 / 十宣)',
                                                            'C. Taiyang (EX-HN5 / 太阳)',
                                                            'D. Yintang (EX-HN3 / 印堂)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Sifeng Pricking):** Sifeng is '
                                                                      'located on the palmar surface of the 2nd to 5th '
                                                                      'fingers at the midpoint of the proximal '
                                                                      'interphalangeal creases. Pricking with a '
                                                                      'sterile lancet to express a drop of yellow '
                                                                      'translucent lymph/fluid directly harmonizes '
                                                                      'Spleen Qi, clears toxic food accumulation, '
                                                                      'stimulates digestion, and treats infantile Gan '
                                                                      'Ji.',
                                                                 'B': '❌ **Incorrect:** Shixuan points are on the tips '
                                                                      'of the 10 fingers used for high-fever coma and '
                                                                      'resuscitation.',
                                                                 'C': '❌ **Incorrect:** Taiyang is on the temple for '
                                                                      'migraines.',
                                                                 'D': '❌ **Incorrect:** Yintang is between the '
                                                                      'eyebrows.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Pediatric Needle Retention Principle',
                                             'prompt': 'What is the standard textbook needle retention principle when '
                                                       'treating a 4-year-old child?',
                                             'options': [   'A. Retain needles for 45 minutes with heavy electrical '
                                                            'stimulation.',
                                                            'B. Swift insertion and immediate withdrawal without '
                                                            'needle retention (Fei Zhen / Non-retention technique).',
                                                            'C. Apply heavy direct scarring moxibustion on all points.',
                                                            'D. Insert needles deeply into the muscle belly and ask '
                                                            'the child to walk around.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Children under 7 should not '
                                                                      'have needles retained for long periods, as it '
                                                                      'exhausts their delicate Qi and causes extreme '
                                                                      'panic.',
                                                                 'B': '✅ **Correct (Swift Non-Retention Technique):** '
                                                                      'In pediatric acupuncture, Qi moves swiftly and '
                                                                      'responds immediately. The golden rule is rapid '
                                                                      'insertion, gentle stimulation for 1-2 seconds '
                                                                      'until Qi arrives (De Qi), and immediate needle '
                                                                      'withdrawal without retention (Fei Zhen).',
                                                                 'C': '❌ **Incorrect:** Direct scarring moxa is '
                                                                      'strictly prohibited in pediatrics.',
                                                                 'D': '❌ **Incorrect:** Dangerous.'}}],
        'standard_diagnosis': {   'patterns': [   'Infantile Malnutrition and Food Stagnation Impairing Spleen (Xiao '
                                                  'Er Gan Ji / 疳积)',
                                                  'Middle Jiao Fermentative Obstruction with Qi-Blood Collapse'],
                                  'treatment_principles': [   'Dissolve Food Accumulation, Harmonize Spleen and '
                                                              'Stomach (消积导滞，和胃健脾)',
                                                              'Prick Sifeng to Drain Lymphatic Stagnation and '
                                                              'Stimulate Growth (点刺四缝)'],
                                  'cardinal_points': ['Sifeng', 'ST36', 'CV12', 'BL20', 'SP3'],
                                  'synergies': [   'Pediatric Miracle point (Sifeng EX-UE10 pricking) immediately '
                                                   'relieves abdominal distension and normalizes digestive secretions.',
                                                   'Middle Burner Harmony pair (CV12 Zhongwan + ST36 Zusanli) restores '
                                                   'gastric motility.',
                                                   'Earth Root combination (BL20 Pishu + SP3 Taibai) rebuilds Spleen '
                                                   'Qi absorption.'],
                                  'cautions': 'PEDIATRIC SAFETY: Never retain needles in young children. Always use '
                                              'rapid insertion-withdrawal technique. Educate parents on strict dietary '
                                              'reform: eliminate dairy, cold sweets, and fruit juices; introduce warm, '
                                              'soft, easily digested congee.'}},
    {   'id': 'CASE-034',
        'title': 'Patient Intake: 38yo Female (Fibromyalgia & Chronic Fatigue - Spleen-Kidney Yang Deficiency)',
        'category': 'Internal Medicine & Rheumatology',
        'patient': {   'age': 38,
                       'gender': 'Female',
                       'occupation': 'Data Analyst',
                       'chief_complaint': 'Widespread bilateral musculoskeletal aching with 14 designated tender '
                                          'points, debilitating chronic fatigue, brain fog, and morning stiffness '
                                          'lasting over an hour for 18 months.',
                       'history': 'Diagnosed with fibromyalgia by rheumatologist after extensive workup excluding '
                                  'lupus and rheumatoid arthritis. Pain is described as a heavy, dull, diffuse ache '
                                  'throughout the neck, shoulders, hips, and knees, dramatically aggravated by cold '
                                  "damp weather and rainy seasons. Waking up in the morning feels like 'having been "
                                  "beaten all night'. Patient suffers from non-restorative sleep, brain fog, cold "
                                  'hands and feet, and loose unformed stools.',
                       'four_examinations': {   'inspection': 'Sluggish tired demeanor; puffy swelling under eyes; '
                                                              'pale sallow complexion; Pale, swollen, flabby tongue '
                                                              'body with deep teeth marks along the lateral margins '
                                                              'and a thick, moist, slippery white coating.',
                                                'auscultation_olfaction': 'Quiet, breathy, low voice; frequent yawning '
                                                                          'and sighing.',
                                                'inquiry': 'Body feels heavily weighed down like carrying wet '
                                                           'blankets; joints stiff for 90 minutes every morning; hands '
                                                           'and feet chronically cold; poor focus and memory; loose '
                                                           'watery stools with undigested food; fatigue unrelieved by '
                                                           '10 hours of sleep.',
                                                'palpation': 'Moderate palpation pressure over bilateral upper '
                                                             'trapezius, second costochondral junctions, lateral '
                                                             'epicondyles, and greater trochanters produces acute jump '
                                                             'sign and tender grimacing; extremities feel cold to '
                                                             'touch; radial pulse is Deep (Chen), Soft/Soggy (Ru), and '
                                                             'Slow (Chi).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Comprehensive Bi Syndrome Pattern Identification',
                                             'prompt': 'What is the primary TCM pattern for widespread musculoskeletal '
                                                       'aching aggravated by rainy weather, heavy limbs, profound '
                                                       'fatigue, cold intolerance, swollen pale scalloped tongue, and '
                                                       'a deep soggy pulse?',
                                             'options': [   'A. Wind-Heat Bi Syndrome with Toxic Heat',
                                                            'B. Spleen and Kidney Yang Deficiency with Fixed Cold-Damp '
                                                            'Bi Syndrome (Han Shi Bi)',
                                                            'C. Pure Liver Fire Blazing with Blood Stasis',
                                                            'D. Acute Exterior Wind-Cold Attack'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Heat Bi presents with hot, '
                                                                      'swollen, red joints, fever, and a rapid pulse.',
                                                                 'B': '✅ **Correct (Spleen-Kidney Yang Deficiency with '
                                                                      'Cold-Damp Bi):** Spleen Yang deficiency fails '
                                                                      'to transform fluids, generating chronic '
                                                                      'internal Dampness. Kidney Yang deficiency fails '
                                                                      'to warm the channels, allowing Cold and Damp to '
                                                                      'lodge deeply in the muscles, fascia, and joints '
                                                                      '(Fixed Bi / Zhuo Bi). Characterized by heavy '
                                                                      'aching aggravated by rain, cold limbs, swollen '
                                                                      'scalloped tongue, and deep soggy pulse.',
                                                                 'C': '❌ **Incorrect:** Liver fire presents with wiry '
                                                                      'pulse, red eyes, and anger.',
                                                                 'D': '❌ **Incorrect:** Acute attack does not account '
                                                                      'for 18 months of systemic fatigue and deep '
                                                                      'soggy pulse.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Point Prescription & Warming Modality',
                                             'prompt': 'Which treatment strategy best dispels stubborn Cold-Damp from '
                                                       'the sinews while tonifying the root Yang Qi?',
                                             'options': [   'A. Moxibustion on CV4 (Guanyuan) and GV14 (Dazhui), '
                                                            'combined with SP9 (Yinlingquan), ST36 (Zusanli), BL20 '
                                                            '(Pishu), BL23 (Shenshu), and GB34 (Yanglingquan)',
                                                            'B. Bloodletting on Shixuan and ear apex with ice packs on '
                                                            'the joints',
                                                            'C. Strong sedating manipulation on LI11, ST44, and GV14 '
                                                            'without moxibustion',
                                                            'D. Needling LU7 and KI6 alone with cool retention'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Warming Moxa & Damp Resolution):** '
                                                                      'Moxibustion on CV4 and GV14 infuses Yang Qi '
                                                                      'into the Governor and Conception vessels to '
                                                                      'dispel deep cold; SP9 (He-Sea) is the premier '
                                                                      'point to resolve Dampness; ST36 + BL20 tonify '
                                                                      'Spleen Qi; BL23 tonifies Kidney Yang; and GB34 '
                                                                      '(Hui of Sinews) relaxes tight, tender, '
                                                                      'fibromyalgic muscular bands.',
                                                                 'B': '❌ **Incorrect:** Bloodletting and ice packs '
                                                                      'severely damage Yang Qi and worsen Cold-Damp '
                                                                      'Bi.',
                                                                 'C': '❌ **Incorrect:** Dispersing heat-clearing '
                                                                      'formula.',
                                                                 'D': '❌ **Incorrect:** Insufficient to address deep '
                                                                      'structural Cold-Damp Bi.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. The Diagnostic Role of Tender Trigger Points (Ashi Points)',
                                             'prompt': 'In treating fibromyalgia pain, how are local tender trigger '
                                                       'points (Ashi Xue) integrated into the treatment plan according '
                                                       "to Sun Simiao's teachings?",
                                             'options': [   'A. Ashi points should be strictly avoided in all chronic '
                                                            'conditions.',
                                                            'B. Palpate the precise reactive tender knots and apply '
                                                            'gentle local needle insertion or warm needle technique to '
                                                            'unblock stagnant Qi and Blood locally.',
                                                            'C. Ashi points must only be treated on the non-painful '
                                                            'side of the body.',
                                                            'D. Needles must be hammered forcefully into bone '
                                                            'periosteum.'],
                                             'correct_index': 1,
                                             'explanations': {   'A': '❌ **Incorrect:** Ashi points are fundamental in '
                                                                      'pain management.',
                                                                 'B': '✅ **Correct (Ashi Points Integration):** Sun '
                                                                      "Simiao stated 'Where there is pain, there is an "
                                                                      "acupuncture point' (Yi Tong Wei Shu). Combining "
                                                                      'root tonification with gentle, localized '
                                                                      'needling of active myofascial trigger points '
                                                                      '(Ashi points) disperses local focal ischemia, '
                                                                      'breaks muscular knots, and restores regional '
                                                                      'microcirculation.',
                                                                 'C': '❌ **Incorrect:** Contralateral needling is an '
                                                                      'option for acute sprains, but bilateral Ashi '
                                                                      'palpation is standard in fibromyalgia.',
                                                                 'D': '❌ **Incorrect:** Dangerous and traumatic.'}}],
        'standard_diagnosis': {   'patterns': [   'Spleen and Kidney Yang Deficiency with Fixed Cold-Damp Bi (Pi Shen '
                                                  'Yang Xu, Han Shi Bi / 寒湿痹)',
                                                  'Latent Pathogen Accumulation in the Muscular Fascia (Fibromyalgia)'],
                                  'treatment_principles': [   'Warm and Supplement Spleen and Kidney Yang (温补脾肾之阳)',
                                                              'Dispel Cold-Damp, Unblock Channels, and Relax Sinews '
                                                              '(祛风除湿，散寒通痹，舒筋缓痛)'],
                                  'cardinal_points': ['SP9', 'ST36', 'BL20', 'BL23', 'CV4', 'GV14', 'GB34'],
                                  'synergies': [   'Yang-Igniting Moxa pair (CV4 Guanyuan + GV14 Dazhui) drives '
                                                   'internal warming energy into the core.',
                                                   'Damp-Expelling Earth pair (SP9 Yinlingquan + ST36 Zusanli) '
                                                   'vaporizes interstitial fluid stagnation.',
                                                   'Hui-Meeting Sinew master (GB34 Yanglingquan) softens chronic '
                                                   'fibromyalgic myofascial trigger points.'],
                                  'cautions': 'TREATMENT TOLERANCE WARNING: Fibromyalgia patients have central nervous '
                                              'system sensitization and hyperalgesia. Avoid overly aggressive manual '
                                              'manipulation or excessive needle retention during initial visits to '
                                              'prevent post-treatment flare-ups. Warm needle or indirect moxibustion '
                                              'is exceptionally well-tolerated.'}},
    {   'id': 'CASE-035',
        'title': 'Patient Intake: 46yo Male (Cervical Radiculopathy & Thoracic Outlet Syndrome - C6 Dermatome)',
        'category': 'Musculoskeletal & Neurological',
        'patient': {   'age': 46,
                       'gender': 'Male',
                       'occupation': 'Architectural Draftsman',
                       'chief_complaint': 'Sharp burning electric pain shooting from the lower cervical spine through '
                                          'the left shoulder down the lateral forearm into the thumb and index finger '
                                          'for 6 weeks.',
                       'history': 'Spends 8–10 hours daily bent over computer CAD screens with forward head posture. '
                                  'Pain began as a dull ache in the left neck and scapula, progressing to acute '
                                  'lancinating pain down the arm. Waking at night from tingling and numbness in the '
                                  "thumb and index finger (C6 dermatome). Positive Spurling's test (axial compression "
                                  'with neck extension and left lateral flexion reproduces radicular shooting pain '
                                  "down arm). Positive Adson's test (radial pulse diminishes upon neck extension and "
                                  'rotation toward affected side).',
                       'four_examinations': {   'inspection': 'Guarded posture with head tilted slightly rightward to '
                                                              'relieve left nerve root compression; atrophy of left '
                                                              'thenar eminence; Dark Reddish-Purple tongue body with '
                                                              'stasis petechiae along lateral borders.',
                                                'auscultation_olfaction': 'Grimacing and holding left arm across '
                                                                          'chest; normal breath sounds.',
                                                'inquiry': 'Sharp stabbing pain worse with neck extension and turning; '
                                                           'numbness in thumb; drop in grip strength when holding '
                                                           'tools; pain disrupts sleep when sleeping on left side.',
                                                'palpation': 'Exquisite focal tenderness and radiation upon palpating '
                                                             'left Hua Tuo Jia Ji points at C5-C7; hypertonic taut '
                                                             'bands in anterior scalene and pectoralis minor; '
                                                             'decreased left biceps reflex (2/4 vs 4/4 right); radial '
                                                             'pulse is Wiry (Xian) and Choppy/Hesitant (Se).'}},
        'multiple_choice_questions': [   {   'question_id': 'Q1',
                                             'title': '1. Channel & Bi Syndrome Differentiation',
                                             'prompt': 'What is the primary TCM pattern for sharp shooting '
                                                       'neck-to-hand pain along the Taiyang and Shaoyang/Yangming '
                                                       'channels with numb C6 dermatome, purple tongue, and a '
                                                       'wiry-choppy pulse?',
                                             'options': [   'A. Taiyang and Shaoyang Channel Obstruction with Blood '
                                                            'Stasis and Nerve Root Compression (Bi Zheng / Jing Luo Yu '
                                                            'Zu)',
                                                            'B. Spleen Qi Deficiency with Sinking of Central Qi',
                                                            'C. Exterior Wind-Cold Attack without Stasis',
                                                            'D. Kidney Yin Deficiency with Empty Fire only'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Channel Obstruction with Blood '
                                                                      'Stasis):** Chronic forward head posture causes '
                                                                      'mechanical disc herniation and cervical canal '
                                                                      'stenosis. In TCM, postural strain leads to Qi '
                                                                      'and Blood stagnation in the Taiyang, Shaoyang, '
                                                                      'and Yangming channels. Stagnant blood '
                                                                      'compresses the nerve roots and collaterals, '
                                                                      'producing sharp radicular pain, C6 numbness, '
                                                                      'purple tongue with stasis dots, and a '
                                                                      'wiry-choppy pulse.',
                                                                 'B': '❌ **Incorrect:** Spleen sinking produces organ '
                                                                      'prolapse and watery diarrhea, not '
                                                                      'radiculopathy.',
                                                                 'C': '❌ **Incorrect:** Acute exterior wind does not '
                                                                      'produce C6 sensory deficit or purple tongue '
                                                                      'stasis dots.',
                                                                 'D': '❌ **Incorrect:** Kidney Yin deficiency produces '
                                                                      'hollow lumbago and night sweats.'}},
                                         {   'question_id': 'Q2',
                                             'title': '2. Precision Paravertebral Needle Prescription',
                                             'prompt': 'Which specialized point prescription directly decompresses the '
                                                       'cervical nerve roots and unblocks the affected arm meridians?',
                                             'options': [   'A. Hua Tuo Jia Ji (C5-C7 on left), SI14 (Jianwaishu), '
                                                            'GB21 (Jianjing), LI11 (Quchi), LI4 (Hegu), SJ5 (Waiguan), '
                                                            'LU7 (Lieque)',
                                                            'B. ST25 (Tianshu), ST37 (Shangjuxu), SP9 (Yinlingquan), '
                                                            'CV12 (Zhongwan)',
                                                            'C. BL23 (Shenshu), CV4 (Guanyuan), KI3 (Taixi), GV4 '
                                                            '(Mingmen)',
                                                            'D. BL28 (Pangguangshu), CV3 (Zhongji), BL63 (Jinmen)'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct:** Left Hua Tuo Jia Ji points at '
                                                                      'C5-C7 directly target the exiting dorsal rami '
                                                                      'and relieve disc/radicular edema; SI14 and GB21 '
                                                                      'relieve intense scapular tension; LI11 + LI4 + '
                                                                      'LU7 open the Yangming/Taiyin channels passing '
                                                                      'into the thumb and index finger; and SJ5 '
                                                                      '(Waiguan) opens the Yang Wei Mai.',
                                                                 'B': '❌ **Incorrect:** Abdominal bowel formula.',
                                                                 'C': '❌ **Incorrect:** Lumbar Kidney formula.',
                                                                 'D': '❌ **Incorrect:** Bladder Lin formula.'}},
                                         {   'question_id': 'Q3',
                                             'title': '3. Critical Anatomical Precaution for GB21 (Jianjing)',
                                             'prompt': 'What life-threatening anatomical danger must be strictly '
                                                       'prevented when needling GB21 (Jianjing) at the highest point '
                                                       'of the shoulder trapezius?',
                                             'options': [   'A. Penetrating the apex of the lung causing traumatic '
                                                            'pneumothorax.',
                                                            'B. Puncturing the femoral artery.',
                                                            'C. Damaging the peroneal nerve.',
                                                            'D. Piercing the orbital eyeball.'],
                                             'correct_index': 0,
                                             'explanations': {   'A': '✅ **Correct (Pneumothorax Warning for GB21):** '
                                                                      'GB21 is situated directly over the apex of the '
                                                                      'lung and dome of the pleura. Deep perpendicular '
                                                                      'downward insertion carries an extremely high '
                                                                      'risk of puncturing the apical pleura, resulting '
                                                                      'in traumatic pneumothorax. The needle MUST be '
                                                                      'directed horizontally or obliquely '
                                                                      'anterior/posterior along the trapezius muscle '
                                                                      'belly, NEVER perpendicularly inferiorly '
                                                                      '(Deadman & CARB-TCMPA safety mandatory '
                                                                      'warning).',
                                                                 'B': '❌ **Incorrect:** Femoral artery is in the '
                                                                      'groin.',
                                                                 'C': '❌ **Incorrect:** Peroneal nerve is at the '
                                                                      'knee/fibula.',
                                                                 'D': '❌ **Incorrect:** Eyeball is in the head.'}}],
        'standard_diagnosis': {   'patterns': [   'Cervical Channel Obstruction with Blood Stasis and Nerve Root '
                                                  'Compression (Jing Luo Yu Zu, Bi Zheng / 颈椎病)',
                                                  'Taiyang, Shaoyang, and Yangming Collateral Stagnation (C6 '
                                                  'Radiculopathy)'],
                                  'treatment_principles': [   'Unblock Cervical Collaterals, Invigorate Blood, and '
                                                              'Stop Pain (通经活络，活血化瘀，通络止痛)',
                                                              'Relax Hypertonic Scalene Musculature and Decompress '
                                                              'Nerve Roots (舒筋缓痛)'],
                                  'cardinal_points': [   'Hua Tuo Jia Ji C5-C7',
                                                         'SI14',
                                                         'GB21',
                                                         'LI11',
                                                         'LI4',
                                                         'SJ5',
                                                         'LU7'],
                                  'synergies': [   'Paravertebral Nerve Root Decompressor (Hua Tuo Jia Ji C5-C7) '
                                                   'eliminates localized inflammatory edema around the exiting C6 '
                                                   'root.',
                                                   'Trapezius Tension Releaser (SI14 Jianwaishu + GB21 Jianjing) '
                                                   'relieves shoulder girdle impingement.',
                                                   'Hand Yangming Distal duo (LI11 Quchi + LI4 Hegu) drives channel Qi '
                                                   'through the forearm into the thumb and index finger.'],
                                  'cautions': 'PNEUMOTHORAX DANGER AT GB21: Never puncture GB21 perpendicularly or '
                                              'deeply. Always pinch the trapezius muscle and insert obliquely or '
                                              'transversely. Verify absence of progressive motor deficit; if patient '
                                              'develops rapidly advancing thenar weakness or loss of arm motor '
                                              'control, urgent neurosurgical MRI consultation is required.'}}]

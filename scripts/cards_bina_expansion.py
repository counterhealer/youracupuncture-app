# -*- coding: utf-8 -*-
"""Bina TCM Review Course Flashcard Expansion Deck.

High-yield board exam cards extracted directly from Bina TCM Review Seminars materials:
- Week 13: Medical Red Flags & Urgent Referrals (David Anzaldua, MD)
- Week 14: Pharmacology & Herb-Drug Interactions
- Week 10: Acupuncture Adjunct Modalities (Electro-acupuncture, Scalp, Ear, Korean 4-Needle)
- Week 3: Pan-Canadian Tongue & Pulse Diagnostic Criteria
- Week 6: Treatment Principles (Ben & Biao, Fu Zheng vs Qu Xie)

All points strictly follow the standard bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS_BINA = [
    # =========================================================================
    # 1. WESTERN MEDICINE: MEDICAL RED FLAGS (From Week 13 Handouts)
    # =========================================================================
    {
        "category": "Western Medicine",
        "title": "Red Flag: Chronic Subdural Hematoma",
        "front": "An elderly patient presents with insidious, increasing confusion, mild headache, and unsteady gait weeks after a minor bump to the head. What is the suspected pathology and management?",
        "back": "Suspected Condition: Chronic Subdural Hematoma (SDH).\n\nKey Clinical Features:\n• Slow venous bleeding from bridging veins tearing between dura and arachnoid.\n• Symptoms develop slowly over days, weeks, or months following even trivial head trauma.\n• Gradual cognitive deterioration, fluctuating alertness, unilateral weakness, or personality changes in elderly or anticoagulated patients.\n\n⚠️ Acupuncturist Action:\n• Immediate emergency medical referral for urgent brain CT / MRI scan.\n• Do NOT treat or attribute to simple Kidney Jing deficiency or Phlegm misting the Heart.\n• Delayed diagnosis risks herniation, irreversible coma, and death.",
        "consensus": "Universal neurological red flag in elderly and patients taking blood thinners.",
        "variations": "Acute SDH presents immediately with rapid coma; Chronic SDH is insidious and often misdiagnosed as dementia.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags (David Anzaldua, MD)", "Bickley Bates' Guide to Physical Examination"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Vertebrobasilar Insufficiency (Drop Attack)",
        "front": "A 68-year-old patient experiences a sudden 'drop attack' (sudden fall to the ground without loss of consciousness) upon rotating or hyperextending their neck. What must be ruled out?",
        "back": "Suspected Condition: Vertebrobasilar Insufficiency (VBI) or Cervical Spondylotic Drop Attack.\n\nKey Clinical Features:\n• Transient compression or insufficiency of the vertebral arteries during neck motion, depriving the brainstem and reticular activating system of blood.\n• Other hallmark 5 D's: Dizziness, Diplopia, Dysarthria, Dysphagia, Drop attacks.\n\n⚠️ Acupuncturist Action:\n• Absolute Contraindication: NEVER perform vigorous cervical manipulation, extreme neck rotation, or deep needling near the craniocervical junction.\n• Urgently refer to neurology / vascular surgery for carotid/vertebral Doppler ultrasound and CTA/MRA.\n• Risk of catastrophic posterior circulation ischemic stroke (Wallenberg syndrome).",
        "consensus": "Absolute contraindication to forceful cervical manual therapies and high risk for posterior circulation stroke.",
        "variations": "Drop attacks may also rarely stem from Meniere's disease (Tumarkin's otolithic crisis) or cardiac arrhythmias.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Harrison's Principles of Internal Medicine"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Non-Traumatic Subarachnoid Hemorrhage",
        "front": "A 45-year-old patient presents with a sudden, explosive headache reaching peak intensity within seconds ('thunderclap headache'). What must be ruled out?",
        "back": "Suspected Condition: Non-Traumatic Subarachnoid Hemorrhage (NTSAH), usually due to ruptured berry aneurysm.\n\nKey Clinical Features:\n• Described as 'the worst headache of my entire life' (Thunderclap onset).\n• Accompanying nausea, photophobia, vomiting, syncope, and progressive meningismus (nuchal rigidity).\n• Sentinel bleed: A smaller warning headache may occur days before the catastrophic rupture.\n\n⚠️ Acupuncturist Action:\n• Call 911 / Emergency EMS immediately. Keep patient immobile in supine position.\n• Do NOT attempt acupuncture analgesia (e.g. GB20, LI4) or prescribe pain herbs.\n• Immediate non-contrast head CT and lumbar puncture if CT is negative.",
        "consensus": "True medical emergency with high mortality rate if aneurysm is not secured surgically or endovascularly.",
        "variations": "Reversible Cerebral Vasoconstriction Syndrome (RCVS) also causes thunderclap headache but SAH must always be ruled out first.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Emergency Medicine Board Review"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Temporal Arteritis (Giant Cell Arteritis)",
        "front": "A 72-year-old patient presents with severe unilateral temporal throbbing headache, scalp tenderness when combing hair, and pain when chewing food (jaw claudication). What is the critical risk?",
        "back": "Suspected Condition: Temporal Arteritis (Giant Cell Arteritis - GCA).\n\nKey Clinical Features:\n• Systemic granulomatous vasculitis affecting medium and large arteries, especially branches of the external carotid.\n• Scalp tenderness, prominent tender/cord-like temporal artery, jaw claudication, fever, weight loss, polymyalgia rheumatica.\n• Elevated Erythrocyte Sedimentation Rate (ESR > 50 mm/hr) and C-reactive protein (CRP).\n\n⚠️ Critical Risk & Action:\n• High risk of sudden, irreversible blindness (anterior ischemic optic neuropathy) if untreated!\n• Immediate emergency hospital referral for high-dose systemic corticosteroid therapy and temporal artery biopsy.",
        "consensus": "Ophthalmic and rheumatologic emergency; treatment with steroids must not be delayed for biopsy.",
        "variations": "Often coexists with Polymyalgia Rheumatica (bilateral aching and stiffness in shoulder and pelvic girdles).",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Bickley Bates' Guide"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Acute Appendicitis & Peritonitis 'Honeymoon' Phase",
        "front": "A patient with severe right lower quadrant abdominal pain suddenly reports that the pain has vanished. Within 2 hours, they develop generalized rigidity, high fever, and tachycardia. Explain this progression.",
        "back": "Clinical Phenomenon: Ruptured Appendix followed by Generalized Peritonitis ('The Honeymoon Phase').\n\nProgression Mechanism:\n1. Initial distension and intraluminal pressure in the appendix causes agonizing somatic RLQ pain at McBurney's point.\n2. When the appendix ruptures/perforates, luminal pressure drops precipitously, producing temporary false pain relief ('honeymoon phase').\n3. Within hours, purulent fecal contents leak into the peritoneal cavity, triggering life-threatening generalized peritonitis, abdominal guarding ('board-like abdomen'), rebound tenderness, high fever, and septic shock.\n\n⚠️ Management: Emergency 911 transfer for exploratory laparotomy/appendectomy.",
        "consensus": "Sudden cessation of acute visceral pain in suspected appendicitis is a sign of rupture, NOT recovery.",
        "variations": "In elderly patients, fever and leukocytosis may be blunted, presenting only with confusion and mild abdominal tenderness.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Schwartz's Principles of Surgery"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Paroxysmal Nocturnal Dyspnea (PND)",
        "front": "A 65-year-old cardiac patient awakens abruptly 1-2 hours after falling asleep gasping for air and must sit upright or walk to an open window to breathe. What is the physiological mechanism?",
        "back": "Suspected Condition: Paroxysmal Nocturnal Dyspnea (PND) from Left-Sided Congestive Heart Failure (CHF).\n\nPhysiological Mechanism:\n• In the supine position during sleep, dependent edema from the lower extremities is resorbed into the intravascular space, dramatically increasing venous return (preload).\n• The failing left ventricle cannot pump this increased volume, leading to pulmonary capillary hypertension and interstitial pulmonary edema.\n\nAssociated Signs:\n• Orthopnea (requires 3+ pillows to sleep), bibasilar pulmonary rales/crackles, S3 gallop, elevated jugular venous distension (JVD).\n• Referral: Urgent cardiology evaluation for diuretic adjustment, echocardiography, and ACE inhibitors.",
        "consensus": "Pathognomonic indicator of decompensated left ventricular heart failure requiring medical management.",
        "variations": "Must be differentiated from nocturnal asthma (which typically features expiratory wheezing rather than crackles).",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Harrison's Internal Medicine"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Deep Vein Thrombosis & Pulmonary Embolism",
        "front": "A patient presents with unilateral calf swelling, redness, warmth, and calf pain on dorsiflexion of the foot (positive Homan's sign) after a long flight. What is the urgent protocol?",
        "back": "Suspected Condition: Deep Vein Thrombosis (DVT) with risk of Pulmonary Embolism (PE).\n\nKey Diagnostic Features:\n• Virchow's Triad: Venous stasis (prolonged travel, immobilization), endothelial injury (surgery, trauma), and hypercoagulability (malignancy, oral contraceptives, smoking).\n• Unilateral calf circumference discrepancy > 3 cm.\n\n⚠️ Urgent Management:\n• Absolute Contraindication: NEVER massage, needle the affected calf (e.g. BL57, BL40), or apply heat/cupping (risks dislodging clot!).\n• Immediate referral to Emergency Department for venous duplex ultrasound and D-dimer.\n• Dislodged thrombus travels to pulmonary arterial bed causing acute Pulmonary Embolism (sudden dyspnea, pleuritic chest pain, hemoptysis, tachycardia, syncope).",
        "consensus": "Massaging or needle trauma to an active DVT can dislodge an embolus directly into the pulmonary circulation.",
        "variations": "Homan's sign has low sensitivity and specificity; diagnostic ultrasound is the definitive gold standard.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Bates' Guide"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Acute Epiglottitis",
        "front": "A 4-year-old child presents with high fever, sore throat, inability to swallow saliva (drooling), inspiratory stridor, and sits upright leaning forward with chin thrust ('tripod position'). What is the immediate priority?",
        "back": "Suspected Condition: Acute Epiglottitis (most commonly Haemophilus influenzae type B or Streptococcus).\n\nKey Clinical Features:\n• The 4 D's: Drooling, Dysphagia, Dysphonia (muffled voice), Dyspnea.\n• Severe supraglottic swelling can rapidly occlude the airway causing total asphyxiation and death within minutes.\n\n⚠️ Immediate Priority & Action:\n• DO NOT examine the pharynx with a tongue depressor or attempt oral inspection (can trigger complete laryngospasm and immediate airway closure!).\n• Keep child calm; do not separate from parents.\n• Call 911 immediately for emergency hospital transport with equipment ready for immediate endotracheal intubation or tracheostomy.",
        "consensus": "Airway emergency of the highest order. Never provoke the child or use instruments in the posterior pharynx.",
        "variations": "Differentiated from Viral Croup (which features a barking seal cough and responds to cool mist/corticosteroids).",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "Nelson Textbook of Pediatrics"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Red Flag: Spinal Malignancy",
        "front": "What clinical features in a low back pain patient raise high suspicion for spinal malignancy or metastatic disease?",
        "back": "Red Flags for Spinal Malignancy:\n• Age > 50 or < 20 years with new-onset back pain.\n• History of prior cancer (especially prostate, breast, lung, kidney, thyroid - 'BLT with a Kosher Pickle').\n• Constant, unremitting dull ache that is severe at night and NOT relieved by lying down or resting.\n• Unexplained significant weight loss (> 10 lbs in a few months).\n• Pain accompanied by localized exquisite spinal percussion tenderness.\n• Failure to improve after 4–6 weeks of conservative care.\n\n⚠️ Action: Urgent spinal MRI and laboratory workup (ESR, CRP, CBC, protein electrophoresis). Do not perform spinal manipulation.",
        "consensus": "Night pain unrelieved by rest is the hallmark red flag differentiating malignancy from benign mechanical back strain.",
        "variations": "Multiple myeloma frequently presents as osteolytic back pain with anemia and hypercalcemia in older adults.",
        "sources": json.dumps(["TCM Review Seminars: Medical Red Flags", "American College of Radiology Guidelines"]),
        "importance_level": 1
    },

    # =========================================================================
    # 2. PHARMACOLOGY & HERB-DRUG INTERACTIONS (From Week 14 Handouts)
    # =========================================================================
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Warfarin & Blood Invigorating Herbs",
        "front": "What is the mechanism of Warfarin (Coumadin), how is its therapeutic effect monitored, and which Chinese herbs are strictly contraindicated or require extreme caution?",
        "back": "Western Mechanism:\n• Vitamin K antagonist that inhibits hepatic synthesis of clotting factors II, VII, IX, X.\n• Monitored clinically via the International Normalized Ratio (INR; therapeutic target typically 2.0–3.0).\n\n⚠️ Critical Herb Interactions:\n• High-Risk Invigorate Blood Herbs: Dang Gui (Radix Angelicae Sinensis), Dan Shen (Radix Salviae Miltiorrhizae), Tao Ren (Semen Persicae), Hong Hua (Flos Carthami), Chuan Xiong (Rhizoma Chuanxiong), San Qi (Radix Notoginseng), Shui Zhi (Leech).\n• Combined use potentiates anticoagulant effect, driving INR > 4.0, triggering spontaneous intracranial, gastrointestinal, or urinary tract hemorrhages.\n• Herbs that decrease Warfarin efficacy: St. John's Wort, high-dose Vitamin K rich herbs.",
        "consensus": "Potent blood-activating Chinese herbs should never be co-administered with Warfarin without strict MD supervision and frequent INR monitoring.",
        "variations": "Dan Shen has documented competitive binding and direct pharmacological synergy with Warfarin in multiple clinical trials.",
        "sources": json.dumps(["TCM Review Seminars: Pharmacology", "Stockley's Herbal Medicines Interactions"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Corticosteroids & TCM Adverse Patterns",
        "front": "What are the common long-term adverse effects of systemic corticosteroids (e.g. Prednisone), and what TCM patterns do they produce?",
        "back": "Western Adverse Effects:\n• Iatrogenic Cushingoid features: Moon face, buffalo hump, central obesity, striae.\n• Osteoporosis & avascular necrosis of the femoral head.\n• Hyperglycemia (steroid-induced diabetes), hypertension, fluid retention.\n• Immunosuppression, impaired wound healing, increased infection susceptibility.\n• Adrenal suppression: Abrupt cessation causes life-threatening Addisonian crisis.\n\nTCM Pattern Equivalent:\n• Prolonged steroid use severely consumes Kidney Yin and Jing, generating False Heat / Empty Heat.\n• Secondary Yang Deficiency develops due to adrenal exhaustion.\n• Spleen Qi deficiency with Damp accumulation manifests as central fluid retention.",
        "consensus": "Patients on long-term steroids must be tapered slowly by their physician; abrupt cessation is dangerous.",
        "variations": "Acupuncturists must take extreme precautions with clean needle technique due to suppressed cellular immunity.",
        "sources": json.dumps(["TCM Review Seminars: Pharmacology", "Goodman & Gilman's Pharmacological Basis of Therapeutics"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Diuretics & Gan Cao (Licorice) Interaction",
        "front": "Why is the co-administration of Loop/Thiazide Diuretics (e.g. Furosemide, Hydrochlorothiazide) with large doses of Gan Cao (Licorice) clinically hazardous?",
        "back": "Western Diuretic Mechanism:\n• Promotes renal excretion of sodium, water, and potassium (hypokalemia risk).\n\nGan Cao (Radix Glycyrrhizae) Mechanism:\n• Glycyrrhizin inhibits 11-beta-hydroxysteroid dehydrogenase (11-beta-HSD2), allowing cortisol to over-activate mineralocorticoid receptors.\n• Causes pseudo-hyperaldosteronism: Sodium retention, potassium excretion, hypertension, and edema.\n\n⚠️ Combined Hazard:\n• Synergistic severe Potassium Depletion (Hypokalemia, K+ < 3.0 mEq/L).\n• Can trigger fatal cardiac arrhythmias, muscle paralysis, and digitalis toxicity in cardiac patients taking Digoxin.",
        "consensus": "High doses or prolonged use of Gan Cao must be avoided in patients taking potassium-wasting diuretics.",
        "variations": "Potassium-sparing diuretics (e.g. Spironolactone) have the opposite effect (risk of hyperkalemia).",
        "sources": json.dumps(["TCM Review Seminars: Pharmacology", "Stockley's Herbal Medicines Interactions"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Beta-Blockers & Masking of Hypoglycemia",
        "front": "What vital clinical warning must an acupuncturist know regarding diabetic patients taking Beta-Adrenergic Antagonists (Beta-Blockers, e.g. Metoprolol, Atenolol)?",
        "back": "Western Mechanism:\n• Block beta-1 and/or beta-2 adrenergic receptors, reducing heart rate, cardiac output, and renin secretion for hypertension and angina.\n\n⚠️ Critical Clinical Warning in Diabetes:\n• Beta-blockers mask almost all early sympathetic warning signs of Acute Hypoglycemia!\n• Symptoms masked: Tachycardia, palpitations, tremors, anxiety, diaphoresis.\n• Only symptom that remains unmasked: Sweating (diaphoresis) or sudden neurological neuroglycopenia (confusion, dizziness, loss of consciousness).\n• Acupuncturists must ensure diabetic patients on beta-blockers have consumed food prior to treatment to avoid clinic hypoglycemic shock.",
        "consensus": "Beta-blockers dangerously blunt adrenergic physiological warning signs of low blood glucose.",
        "variations": "Non-selective beta blockers (e.g. Propranolol) also inhibit glycogenolysis, prolonging hypoglycemic episodes.",
        "sources": json.dumps(["TCM Review Seminars: Pharmacology", "American Diabetes Association Standards"]),
        "importance_level": 1
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: NSAIDs & Gastric Mucosal Bleeding",
        "front": "Explain the mechanism of NSAID-induced gastric ulceration and the clinical implications for acupuncturists evaluating epigastric pain.",
        "back": "Western Mechanism:\n• Non-Steroidal Anti-Inflammatory Drugs (e.g. Ibuprofen, Naproxen, Meloxicam) inhibit Cyclooxygenase (COX-1 and COX-2) enzymes.\n• COX-1 inhibition blocks synthesis of protective prostaglandins (PGE2, PGI2) in gastric mucosa, decreasing mucus/bicarbonate secretion and reducing mucosal blood flow.\n\nClinical Implications for Epigastric Pain:\n• Epigastric burning or gnawing pain in an NSAID user is frequently drug-induced peptic ulcer disease rather than simple Liver Qi invading Stomach.\n• Red Flag Signs of Upper GI Bleeding: Melena (black tarry stools), hematemesis (coffee-ground emesis), orthostatic dizziness, pallor.\n• Management: Refer to MD for endoscopy, discontinue NSAIDs, switch to acetaminophen or acupuncture analgesia.",
        "consensus": "Chronic NSAID therapy is the leading cause of non-H. pylori peptic ulceration and GI bleeding in chronic pain patients.",
        "variations": "Selective COX-2 inhibitors (e.g. Celecoxib) reduce gastric ulcer risk but increase cardiovascular thrombotic risk.",
        "sources": json.dumps(["TCM Review Seminars: Pharmacology", "Harrison's Internal Medicine"]),
        "importance_level": 1
    },

    # =========================================================================
    # 3. ACUPUNCTURE ADJUNCT MODALITIES & KOREAN 4-NEEDLE (Week 10 Handouts)
    # =========================================================================
    {
        "category": "Meridians and Points",
        "title": "Korean 4-Needle: Spleen Tonification & Sedation Formula",
        "front": "What are the specific points used in the Korean Four-Needle (Saam) technique for Spleen Tonification (SP Deficiency) and Spleen Sedation (SP Excess)?",
        "back": "Spleen Earth Meridian Rules:\n\n1. Spleen Tonification Formula (脾虚补法):\n• Principle: Tonify Mother (Fire) + Sedate Controller (Wood / Grandmother).\n• Tonify Mother: SP2 (Dadu / 大都, Fire on self) + HT8 (Shaofu / 少府, Fire on Heart).\n• Sedate Controller: SP1 (Yinbai / 隐白, Wood on self) + LR1 (Dadun / 大敦, Wood on Liver).\n\n2. Spleen Sedation Formula (脾实泻法):\n• Principle: Sedate Child (Metal) + Tonify Controller (Wood).\n• Sedate Child: SP5 (Shangqiu / 商丘, Metal on self) + LU8 (Jingqu / 经渠, Metal on Lung).\n• Tonify Controller: SP1 (Yinbai / 隐白, Wood on self) + LR1 (Dadun / 大敦, Wood on Liver).",
        "consensus": "Classical Korean Saam formula strictly balancing the Generating (Sheng) and Controlling (Ke) cycles.",
        "variations": "PC8 may be substituted for HT8 as Fire Mother on Yin Fire meridians depending on Korean school lineage.",
        "sources": json.dumps(["TCM Review Seminars: Korean 4-Needle Technique", "Saam Acupuncture Secret Methods"]),
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "Korean 4-Needle: Liver Tonification & Sedation Formula",
        "front": "What are the Korean Four-Needle (Saam) points for Liver Tonification (Liver Blood/Yin Deficiency) and Liver Sedation (Liver Fire/Excess)?",
        "back": "Liver Wood Meridian Rules:\n\n1. Liver Tonification Formula (肝虚补法):\n• Principle: Tonify Mother (Water) + Sedate Controller (Metal / Grandmother).\n• Tonify Mother: LR8 (Ququan / 曲泉, Water on self) + KD10 (Yingu / 阴谷, Water on Kidney).\n• Sedate Controller: LR4 (Zhongfeng / 中封, Metal on self) + LU8 (Jingqu / 经渠, Metal on Lung).\n\n2. Liver Sedation Formula (肝实泻法):\n• Principle: Sedate Child (Fire) + Tonify Controller (Metal).\n• Sedate Child: LR2 (Xingjian / 行间, Fire on self) + HT8 (Shaofu / 少府, Fire on Heart).\n• Tonify Controller: LR4 (Zhongfeng / 中封, Metal on self) + LU8 (Jingqu / 经渠, Metal on Lung).",
        "consensus": "Extremely high yield on Pan-Canadian and CALE board examinations.",
        "variations": "For Liver Fire sedation, sedating LR2 + HT8 forcefully clears hyperactive fire from both wood and fire axes.",
        "sources": json.dumps(["TCM Review Seminars: Korean 4-Needle Technique", "CAM 3rd Edition"]),
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Electro-Acupuncture: Frequency Guidelines & Clinical Selection",
        "front": "Outline the clinical applications and neurochemical mechanisms of Low Frequency, High Frequency, and Dense-Disperse Electro-Acupuncture (EA).",
        "back": "Electro-Acupuncture Frequency Parameters:\n\n1. Low Frequency (2–5 Hz / Continuous):\n• Neurochemistry: Stimulates release of Beta-Endorphins and Enkephalins in CSF.\n• Indications: Chronic dull pain, motor weakness, paralysis, post-stroke flaccidity, tissue regeneration, bell's palsy (chronic stage).\n\n2. High Frequency (50–100 Hz / Continuous):\n• Neurochemistry: Stimulates release of Dynorphin in the spinal cord.\n• Indications: Acute sharp pain, severe spasms, joint inflammation, anesthesia.\n\n3. Dense-Disperse (Alternating 2 Hz and 100 Hz):\n• Neurochemistry: Simultaneously releases Endorphins, Enkephalins, and Dynorphin; prevents neurological habituation/accommodation.\n• Indications: Supreme for sciatica, chronic stubborn musculoskeletal pain, joint arthralgia, and postoperative pain.",
        "consensus": "Dense-disperse frequency is the gold standard for clinical pain management because it avoids nerve adaptation.",
        "variations": "Intermittent mode (pulse-pause) is chosen when treating flaccid paralysis to simulate voluntary muscle contraction without exhausting motor units.",
        "sources": json.dumps(["TCM Review Seminars: Acupuncture Modalities", "Han Ji-Sheng Neurochemical Pain Studies"]),
        "importance_level": 1
    },
    {
        "category": "Safety and Ethics",
        "title": "Electro-Acupuncture: Absolute Contraindications & Precautions",
        "front": "What are the absolute contraindications and hazardous electrode configurations for Electro-Acupuncture (EA)?",
        "back": "⚠️ Absolute Contraindications & Safety Hazards:\n\n1. Cardiac Pacemakers & Implanted Cardioverter Defibrillators (ICD):\n• Absolute contraindication anywhere on the body (electrical interference can cause fatal device malfunction).\n\n2. Crossing the Transthoracic Midline / Heart:\n• NEVER place one lead on the anterior chest and one on the posterior back, or across both arms (e.g. PC6 left to PC6 right), as current passing through the heart can induce ventricular fibrillation.\n\n3. Trans-Cranial / Carotid Sinus / Brainstem:\n• Never cross current across the brain or over the carotid sinus (severe vasovagal syncope, profound bradycardia, cardiac arrest).\n\n4. Other Cautions:\n• History of epilepsy/seizures; active malignancy site; deep vein thrombosis; over abdominal/lumbar regions in pregnant women.",
        "consensus": "Crossing the chest or using EA in patients with pacemakers are major malpractice and regulatory violations.",
        "variations": "Modern shielded pacemakers are less vulnerable, but national board standards maintain an absolute universal ban.",
        "sources": json.dumps(["TCM Review Seminars: Modalities", "Clean Needle Technique (CNT) 7th Edition"]),
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "Scalp Acupuncture: MS6 Motor Line Somatotopic Mapping",
        "front": "Describe the location of MS6 Dingnie Qianxiexian (Anterior Oblique Line of Vertex-Temporal / Motor Line) and the clinical divisions of its Upper 1/5, Middle 2/5, and Lower 2/5.",
        "back": "Location: From Qianshencong (Sishenchong / EX-HN1, 1 cun anterior to GV20) obliquely to GB6 (Xuanli).\n\nSomatotopic Functional Divisions:\n• Upper 1/5 (Apex): Paraplegia, hemiplegia, weakness or spasticity of the Contralateral Lower Limb and Trunk; urinary incontinence.\n• Middle 2/5: Motor impairment or paralysis of the Contralateral Upper Limb, hand, and fingers.\n• Lower 2/5 (Base): Central facial palsy, motor aphasia, impaired speech, salivation, dysphagia (swallowing).\n\nTechnique: Thread subaponeurotically at 15–30 degree angle. Twirl rapidly at 200 rpm without lifting or thrusting. Treat Contralateral side in unilateral hemiplegia.",
        "consensus": "Inverted homunculus somatotopy: foot/leg at top (upper 1/5), hand/arm in middle, face/tongue at bottom.",
        "variations": "For bilateral paralysis or internal systemic disorders, needle bilaterally.",
        "sources": json.dumps(["TCM Review Seminars: Scalp & Ear for Pan-Canadian", "Jiao Shunfa Scalp Acupuncture"]),
        "importance_level": 1
    },
    {
        "category": "Meridians and Points",
        "title": "Auricular Acupuncture: Master Points & NADA Protocol",
        "front": "What are the 5 points in the standard NADA (National Acupuncture Detoxification Association) protocol, and what are their primary indications?",
        "back": "NADA 5-Point Ear Protocol:\n1. Sympathetic (交感 - Inferior antihelix crus): Regulates autonomic nervous system, relieves visceral spasm, dilates blood vessels, reduces sympathetic stress flight/fight.\n2. Shenmen (神门 - Triangular fossa apex): Grounds spirit, calms anxiety, relieves pain, alleviates restlessness and insomnia.\n3. Kidney (肾 - Superior to Liver, under concha ridge): Strengthens willpower (Zhi), resolves deep fear, repairs Jing and post-detox adrenal exhaustion.\n4. Liver (肝 - Postero-inferior to Spleen in cavum conchae): Resolves anger/irritability, smooths stagnant Qi, detoxifies blood and metabolizes chemicals.\n5. Lung (肺 - Superior and inferior to Heart point in cavum conchae): Resolves grief/sadness, regulates respiration, opens pores to eliminate toxins.\n\nIndications: Substance withdrawal, smoking cessation, PTSD, acute psychological trauma, stress regulation.",
        "consensus": "Worldwide standard for clinical addiction recovery, trauma relief, and stress reduction.",
        "variations": "Point Zero (umbilicus reflex at root of helix) is often paired to re-establish total homeostatic balance.",
        "sources": json.dumps(["TCM Review Seminars: Scalp & Ear", "NADA Protocol Guidelines"]),
        "importance_level": 1
    },

    # =========================================================================
    # 4. PAN-CANADIAN TONGUE & PULSE CRITERIA (From Week 3 Handouts)
    # =========================================================================
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Wiry (Xian) vs Tight (Jin) Mai",
        "front": "Contrast the tactile sensation and clinical etiologies of a Wiry Pulse (Xian Mai) versus a Tight Pulse (Jin Mai).",
        "back": "1. Wiry Pulse (Xian Mai / 弦脉):\n• Tactile Feel: Taut, straight, and hard like pressing a stretched guitar string. Hits the fingers with clean straight resilience.\n• Etiologies: Liver and Gallbladder disorders, Liver Qi Stagnation, Phlegm retention, Damp accumulation, severe pain, normal in Spring.\n\n2. Tight Pulse (Jin Mai / 紧脉):\n• Tactile Feel: Tense, strong, vibrating from side to side like a taut, twisted rope (more forceful and twisting than Wiry).\n• Etiologies: Severe Cold (Exterior Wind-Cold or Interior Full Cold), severe acute cramping pain, Food Retention with cold.\n\nKey Board Distinction:\n• Wiry = Liver disharmony or Phlegm (long, straight, taut).\n• Tight = Cold and severe pain (twisting, vibrating, contracting force).",
        "consensus": "A Tight pulse fundamentally reflects Cold contraction; a Wiry pulse reflects Qi constraint or Phlegm.",
        "variations": "A floating tight pulse indicates Exterior Wind-Cold (Shanghan Taiyang); a deep tight pulse indicates Interior Cold with severe abdominal pain.",
        "sources": json.dumps(["TCM Review Seminars: Pulse Diagnosis", "Maciocia Foundations"]),
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Pulse Differentiation: Knotted (Jie), Intermittent (Dai), Hurried (Cu)",
        "front": "Compare the 3 classic irregular/arrhythmic pulses: Knotted (Jie Mai), Intermittent (Dai Mai), and Hurried/Abrupt (Cu Mai).",
        "back": "1. Knotted Pulse (Jie Mai / 结脉):\n• Rhythm: Slow arrival with IRREGULAR (unpredictable) missed beats / pauses.\n• Etiologies: Cold obstructing Heart Qi/Blood, Phlegm-Blood stagnation, Heart Yang deficiency.\n\n2. Hurried / Abrupt Pulse (Cu Mai / 促脉):\n• Rhythm: Rapid arrival with IRREGULAR (unpredictable) missed beats / pauses.\n• Etiologies: Extreme Heat agitating Heart Shen, Phlegm-Heat, Heart Fire, Stagnation.\n\n3. Intermittent Pulse (Dai Mai / 代脉):\n• Rhythm: Normal or slow arrival with REGULAR (predictable) missed beats that pause for long intervals.\n• Etiologies: Serious exhaustion of Zang-Fu Organ Qi (especially Heart and Spleen), severe fear/fright, advanced wind stroke.",
        "consensus": "Regular pause = Intermittent (Dai, Zang exhaustion); Irregular slow pause = Knotted (Jie); Irregular rapid pause = Hurried (Cu).",
        "variations": "Western correlation: Jie and Cu = premature ventricular contractions (PVCs); Dai = heart block, atrial flutter with fixed block.",
        "sources": json.dumps(["TCM Review Seminars: Pulse Diagnosis", "CAM 3rd Edition"]),
        "importance_level": 1
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Differentiation: Swollen Tongue Body Patterns",
        "front": "What are the clinical differentiations of a Swollen Tongue Body with Pale Color vs Normal Color vs Red Color?",
        "back": "Swollen Tongue Body Form (胖大舌):\n\n1. Pale & Wet with Teeth Marks:\n• Pathology: Spleen and/or Kidney Yang Deficiency leading to failure of fluid transformation and internal Accumulation of Dampness/Phlegm.\n\n2. Normal Color & Swollen:\n• Pathology: Middle Burner Damp-Heat or Spleen Dampness without severe Yang cold.\n\n3. Red or Deep Red & Swollen:\n• Pathology: Extreme Fire and Toxic Heat in the Heart and Spleen, or Alcohol Heat consuming fluids.\n\n4. Swollen Edges (Liver area):\n• Pathology: Severe Liver Fire or Liver Qi Stagnation generating internal heat.\n\n5. Swollen Tip (Heart area):\n• Pathology: Severe Heart Fire blazing or emotional agitation.",
        "consensus": "Pale swollen = Yang deficiency with dampness; Red swollen = Full fire/toxin.",
        "variations": "Partially swollen tongues indicate organ-specific fluid stagnation or fire depending on regional anatomy.",
        "sources": json.dumps(["TCM Review Seminars: Tongue Diagnosis", "CAM 3rd Edition"]),
        "importance_level": 1
    },

    # =========================================================================
    # 5. TREATMENT PRINCIPLES: BEN & BIAO (From Week 6 Handouts)
    # =========================================================================
    {
        "category": "Illness",
        "title": "Treatment Principles: Root (Ben) vs Manifestation (Biao) Priorities",
        "front": "State the 3 clinical rules governing when to treat the Root (Ben), the Manifestation (Biao), or Both Simultaneously (Biao Ben Tong Zhi).",
        "back": "Root (Ben / 本) vs Manifestation (Biao / 标) Clinical Rules:\n\n1. Treat Biao Urgently in Acute Emergencies (急则治其标):\n• When secondary manifestation symptoms are life-threatening or agonizing.\n• Examples: Severe acute hemorrhaging/bleeding (must stop bleeding first before tonifying Qi/Blood deficiency); severe acute dyspnea/asthmatic crisis; urinary retention/constipation with acute obstruction; severe agonizing headache.\n\n2. Treat Ben in Chronic / Non-Emergency Conditions (缓则治其本):\n• When manifestations are mild, stable, or secondary.\n• Example: Mild chronic knee ache due to Kidney deficiency -> tonify Kidney directly.\n\n3. Treat Both Ben and Biao Simultaneously (标本同治):\n• When both root and branch are equally prominent.\n• Example: Spleen Qi deficiency (Ben) causing severe Dampness accumulation (Biao) -> Tonify Spleen while simultaneously drying Dampness.",
        "consensus": "Life-threatening acute emergencies always take priority over root constitution.",
        "variations": "Stopping bleeding in hemorrhage is the quintessential board exam example of 'treating Biao first in emergencies'.",
        "sources": json.dumps(["TCM Review Seminars: Treatment Principles", "Yellow Emperor's Inner Classic"]),
        "importance_level": 1
    },
    {
        "category": "Illness",
        "title": "Treatment Principles: Contrary (Zheng Zhi) vs Non-Contrary (Fan Zhi)",
        "front": "Explain the difference between Treatment by Contraries (Zheng Zhi / Regular Treatment) and Treatment by Non-Contraries (Fan Zhi / Indirect Treatment).",
        "back": "1. Treatment by Contraries (正治 / Regular Treatment - 'Treating Cold with Heat'):\n• Standard rule: Treat the clinical nature of the disease with herbs/points of the opposing nature.\n• Warm Cold patterns (寒者热之); Cool Heat patterns (热者寒之); Tonify Deficiency (虚者补之); Drain Excess (实者泻之).\n\n2. Treatment by Non-Contraries (反治 / Indirect Treatment / Follow the Disease):\n• Used in complex cases of True Pathology with False External Manifestations:\n• Treating Heat with Heat (热因热用): In True Cold with False Heat (Yin Excess pushing Yang outward / Dai Yang syndrome). Must use warm/hot herbs (e.g. Si Ni Tang) despite red cheeks/thirst.\n• Treating Cold with Cold (寒因寒用): In True Heat with False Cold (Extreme interior heat with cold extremities / Jueyin Reversal). Must use cold herbs (e.g. Bai Hu Tang) despite cold limbs.\n• Tonify for Fullness (塞因塞用): In True Deficiency causing pseudo-fullness (e.g. severe Spleen deficiency causing abdominal distension).\n• Drain for Diarrhea (通因通用): In True Heat or Stasis causing watery diarrhea (e.g. Damp-Heat dysentery or stasis lochia).",
        "consensus": "Non-contrary treatment addresses the hidden true root when external manifestations present misleading polar symptoms.",
        "variations": "Frequently tested in Shang Han Lun Jueyin stage and Shao Yin false-heat syndromes.",
        "sources": json.dumps(["TCM Review Seminars: Treatment Principles", "Maciocia Foundations"]),
        "importance_level": 1
    }
]

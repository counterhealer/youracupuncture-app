"""Western Medicine Flashcards (32 high-yield clinical cards).

Covers emergency red flags, physical examination signs, vital signs, cardiovascular,
neurological, orthopedic, endocrine, lab tests, pharmacology, and bloodborne pathogens.
"""

import json

CARDS = [
    {
        "category": "Western Medicine",
        "title": "Red Flag: Cauda Equina Syndrome",
        "front": "What are the hallmark clinical signs of Cauda Equina Syndrome, and what is the urgent management protocol for an acupuncturist?",
        "back": "Hallmark Signs:\n• Saddle anesthesia (sensory loss in perineum, buttocks, inner thighs).\n• Sudden loss of bowel or bladder control (urinary retention or fecal incontinence).\n• Progressive bilateral lower extremity motor weakness or paralysis.\n• Severe low back pain with bilateral radiculopathy.\n\n⚠️ Management Protocol:\n• Immediate emergency medical emergency (Surgical Red Flag).\n• Do NOT treat with acupuncture.\n• Immediately arrange emergency medical transport to the nearest Emergency Department for urgent MRI and surgical decompression within 24–48 hours to prevent permanent neurological deficit.",
        "consensus": "Universal surgical red flag requiring immediate hospital emergency department referral.",
        "variations": "Textbooks note that delayed decompression beyond 48 hours significantly increases the risk of permanent bladder/bowel incontinence and sexual dysfunction.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Bickley Bates' Guide to Physical Examination"])
    },
    {
        "category": "Western Medicine",
        "title": "Stroke Recognition: FAST Protocol",
        "front": "Outline the FAST protocol for acute stroke recognition and the vital timeline window for thrombolysis (tPA).",
        "back": "FAST Protocol:\n• F - Face Drooping: One side of the face droops or is numb; uneven smile.\n• A - Arm Weakness: One arm is weak or numb; drift when arms are raised.\n• S - Speech Difficulty: Slurred speech, unable to speak, or difficulty comprehending.\n• T - Time to call 911: Call emergency medical services immediately.\n\n⚠️ Critical Window:\n• Intravenous thrombolysis (tPA) window is typically within 3 to 4.5 hours from the exact 'last known well' time.\n• Acupuncturist must record the exact onset time, keep patient calm and supine, withhold oral fluids/food, and call 911 immediately.",
        "consensus": "Immediate 911 dispatch. Never attempt needle retention or delay transport during acute ischemic window.",
        "variations": "Endovascular mechanical thrombectomy may be performed up to 24 hours in selected patients with large vessel occlusions.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "American Heart Association Guidelines"])
    },
    {
        "category": "Western Medicine",
        "title": "Myocardial Infarction: Classic vs Atypical Signs",
        "front": "What are the classic versus atypical symptoms of Acute Myocardial Infarction (MI), particularly in female and diabetic patients?",
        "back": "Classic Symptoms (Typical):\n• Crushing substernal chest pressure, heaviness, or squeezing sensation ('elephant on chest').\n• Radiation to left arm, neck, jaw, or shoulder.\n• Diaphoresis (cold sweats), dyspnea, nausea, and lightheadedness.\n\nAtypical Symptoms (Common in Women, Elderly, and Diabetics):\n• Unexplained shortness of breath without prominent chest pain.\n• Epigastric burning, nausea, indigestion, or abdominal pain (easily mistaken for GERD or food stagnation).\n• Overwhelming profound fatigue, generalized weakness, or acute sleep disturbance.\n• Silent MI in diabetic patients due to autonomic neuropathy.",
        "consensus": "Any unexplained acute dyspnea, diaphoresis, and upper body pain warrants immediate emergency EMS activation.",
        "variations": "Diabetic autonomic neuropathy can completely mask chest discomfort, presenting solely as sudden weakness or confusion.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Harrison's Principles of Internal Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Deep Vein Thrombosis (DVT) & Pulmonary Embolism",
        "front": "What are the clinical findings of Deep Vein Thrombosis (DVT) in the calf/leg, and what life-threatening complication must be guarded against?",
        "back": "Clinical Signs of DVT:\n• Unilateral leg swelling (calf circumference difference > 3 cm).\n• Erythema, localized warmth, and tenderness along deep venous system.\n• Dull aching pain worsened by weight-bearing.\n• Traditional Homan's sign (calf pain on dorsiflexion) is neither sensitive nor specific and can theoretically dislodge a clot.\n\n⚠️ Life-Threatening Complication:\n• Pulmonary Embolism (PE): Clot dislodges and occludes pulmonary arterial tree.\n• PE Signs: Sudden onset pleuritic chest pain, tachypnea, acute dyspnea, tachycardia, hemoptysis, syncope.\n• Contraindication: NEVER apply deep massage, vigorous tuina, or deep needling directly over suspected DVT site.",
        "consensus": "Unilateral calf edema and erythema require urgent D-dimer and compression Doppler ultrasound.",
        "variations": "Wells Criteria is the standard western clinical scoring system used to determine pre-test probability of DVT.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Wells Clinical Prediction Rules"])
    },
    {
        "category": "Western Medicine",
        "title": "Vital Signs: Adult Normal Reference Ranges",
        "front": "List standard adult resting reference ranges for Blood Pressure, Heart Rate, Respiratory Rate, Body Temperature, and Oxygen Saturation.",
        "back": "Normal Resting Reference Ranges:\n• Blood Pressure (BP): Normal < 120/80 mmHg; Elevated 120–129/<80; Stage 1 HTN 130–139 or 80–89; Stage 2 HTN ≥ 140 or ≥ 90; Hypertensive Crisis > 180 and/or > 120 mmHg.\n• Heart Rate (Pulse): 60 – 100 beats per minute (Bradycardia < 60 bpm; Tachycardia > 100 bpm).\n• Respiratory Rate (RR): 12 – 20 breaths per minute at rest (Tachypnea > 20 bpm).\n• Temperature: 36.5°C – 37.5°C (97.7°F – 99.5°F) orally; Fever generally defined as ≥ 38.0°C (100.4°F).\n• Oxygen Saturation (SpO2): 95% – 100% on room air (SpO2 < 90% indicates hypoxemia requiring supplemental O2).",
        "consensus": "Mandatory baseline vital sign measurements in clinical assessment before invasive procedures.",
        "variations": "Athletes may have resting heart rates in the 40s–50s (physiological bradycardia) without pathology.",
        "sources": json.dumps(["Royal TCM WM-01 Basic of Western Medicine", "Bates' Guide to Physical Examination"])
    },
    {
        "category": "Western Medicine",
        "title": "Orthostatic Hypotension: Criteria & Clinical Protocol",
        "front": "What defines Orthostatic Hypotension, and how does it relate to needle fainting (vasovagal reaction)?",
        "back": "Definition & Diagnostic Criteria:\n• A sustained drop in Systolic Blood Pressure of ≥ 20 mmHg, OR\n• A sustained drop in Diastolic Blood Pressure of ≥ 10 mmHg\n• Within 2 to 3 minutes of standing from a supine or seated position (often accompanied by tachycardia or lightheadedness).\n\nRelevance to Acupuncture:\n• Patients rising too quickly after a 30-minute acupuncture treatment frequently experience orthostatic pooling.\n• Predisposes to post-treatment syncope, falls, and trauma.\n• Protocol: Instruct patient to sit on treatment table edge for 1–2 minutes before standing; evaluate dizziness prior to discharge.",
        "consensus": "Common cause of dizziness, especially in elderly, dehydrated, or patients taking anti-hypertensive medications.",
        "variations": "Autonomic neuropathy (e.g. Parkinson's, Diabetes) presents with orthostatic hypotension lacking compensatory tachycardia.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Merck Manual of Diagnosis and Therapy"])
    },
    {
        "category": "Western Medicine",
        "title": "Cranial Nerves: Key Functions & Examination",
        "front": "List the 12 cranial nerves in order, noting key motor/sensory functions and high-yield physical examination findings.",
        "back": "Cranial Nerves (CN I - XII):\n• CN I (Olfactory): Smell (sensory).\n• CN II (Optic): Visual acuity, visual fields, pupillary light reflex afferent (sensory).\n• CN III (Oculomotor): Eye movements (superior, inferior, medial recti, inferior oblique), pupillary constriction (motor).\n• CN IV (Trochlear): Superior oblique muscle (down and in) (motor).\n• CN V (Trigeminal): Facial sensation (V1, V2, V3) & muscles of mastication (mixed).\n• CN VI (Abducens): Lateral rectus muscle (abduction of eye) (motor).\n• CN VII (Facial): Muscles of facial expression, anterior 2/3 tongue taste, lacrimation/salivation (mixed).\n• CN VIII (Vestibulocochlear): Hearing (Weber/Rinne) and vestibular balance (sensory).\n• CN IX (Glossopharyngeal): Posterior 1/3 tongue taste, swallowing, gag reflex afferent (mixed).\n• CN X (Vagus): Palate elevation, vocal cords, parasympathetic viscera (mixed).\n• CN XI (Accessory): Sternocleidomastoid and Trapezius shrug/turn (motor).\n• CN XII (Hypoglossal): Tongue protrusion and symmetry (motor; tongue deviates towards lesion side).",
        "consensus": "Essential baseline neurological examination for headaches, facial palsy, stroke, and dizziness.",
        "variations": "Bell's Palsy affects lower and upper face (forehead wrinkle lost); central stroke spares the forehead due to bilateral cortical innervation.",
        "sources": json.dumps(["Royal TCM WM-01 & WM-02", "Netter's Clinical Anatomy"])
    },
    {
        "category": "Western Medicine",
        "title": "Upper vs Lower Motor Neuron Lesions",
        "front": "Distinguish between Upper Motor Neuron (UMN) and Lower Motor Neuron (LMN) lesions in terms of tone, reflexes, atrophy, and Babinski sign.",
        "back": "Clinical Comparison:\n• Muscle Tone: UMN = Spastic / Hypertonic (clasp-knife rigidity); LMN = Flaccid / Hypotonic.\n• Deep Tendon Reflexes (DTRs): UMN = Hyperreflexia (grades 3+ to 4+, clonus present); LMN = Hyporeflexia or Areflexia (grades 0 to 1+).\n• Muscle Atrophy: UMN = Minimal / Disuse atrophy only; LMN = Severe, rapid, marked neurogenic atrophy.\n• Fasciculations: UMN = Absent; LMN = Present (muscle twitches).\n• Pathological Reflexes (Babinski sign): UMN = Positive (dorsiflexion of great toe with fanning of other toes); LMN = Negative (normal plantar flexion).",
        "consensus": "Fundamental differentiation for motor weakness, spinal cord lesions, stroke, and peripheral neuropathies.",
        "variations": "Acute UMN lesions (spinal shock) may initially present with transient flaccidity and hyporeflexia before developing spasticity.",
        "sources": json.dumps(["Royal TCM WM-01 Basic of Western Medicine", "Clinical Neuroanatomy"])
    },
    {
        "category": "Western Medicine",
        "title": "Appendicitis: Diagnostic Physical Signs",
        "front": "Identify the key physical examination signs for acute appendicitis (McBurney's, Rovsing's, Psoas, Obturator).",
        "back": "Key Physical Signs:\n• McBurney's Point Tenderness: Maximal tenderness 1/3 the distance from Anterior Superior Iliac Spine (ASIS) to the umbilicus.\n• Rovsing's Sign: Palpation/pressure in the Left Lower Quadrant elicits pain in the Right Lower Quadrant (referred peritoneal irritation).\n• Psoas Sign: Increased RLQ pain with passive extension of the right hip while in left lateral decubitus (retrocecal appendix irritating iliopsoas muscle).\n• Obturator Sign: Increased RLQ pain with passive internal rotation of the flexed right hip (pelvic appendix irritating internal obturator muscle).\n• Rebound Tenderness (Blumberg Sign): Pain upon sudden release of deep palpation indicating localized or generalized peritonitis.",
        "consensus": "Acute surgical abdomen. Must be referred immediately to hospital emergency department without oral intake.",
        "variations": "Atypical presentations are common in children, pregnant women (appendix displaced superiorly), and the elderly.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Schwartz's Principles of Surgery"])
    },
    {
        "category": "Western Medicine",
        "title": "Cholecystitis: Murphy's Sign & Charcot's Triad",
        "front": "Explain the performance and significance of Murphy's Sign, and differentiate acute cholecystitis from ascending cholangitis (Charcot's Triad).",
        "back": "Murphy's Sign:\n• Technique: Palpate deeply beneath the right costal margin at the midclavicular line while the patient inhales deeply.\n• Positive Finding: Sudden inspiratory arrest (sharp catch in breath) due to severe pain as the inflamed gallbladder touches the examining fingers.\n• Significance: Highly indicative of Acute Cholecystitis.\n\nAscending Cholangitis (Biliary Tree Infection):\n• Charcot's Triad: 1. RUQ abdominal pain, 2. Jaundice, 3. High fever with chills.\n• Reynolds' Pentad (Septic Shock): Charcot's triad + Hypotension + Altered Mental Status (urgent life-threatening surgical emergency).",
        "consensus": "Positive Murphy's sign warrants urgent abdominal ultrasound and liver function blood work.",
        "variations": "Elderly patients with acute cholecystitis may have an absent Murphy's sign and blunted inflammatory response.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Current Medical Diagnosis and Treatment"])
    },
    {
        "category": "Western Medicine",
        "title": "Orthopedic Tests: Cervical Radiculopathy",
        "front": "Describe Spurling's Test and the Cervical Distraction Test for cervical nerve root compression.",
        "back": "Spurling's Test (Neck Compression):\n• Technique: Patient seated; neck laterally flexed towards the symptomatic side. Examiner applies gentle downward axial pressure to the top of the head.\n• Positive Finding: Reproduction of sharp radicular pain or paresthesia radiating down the ipsilateral arm.\n• Significance: Indicates cervical nerve root compression (disc herniation or foraminal stenosis).\n\nCervical Distraction Test:\n• Technique: Examiner places hands under patient's occiput and chin/mastoid and applies steady upward axial traction (approx. 10–15 kg).\n• Positive Finding: Relief or marked reduction of cervical and radiating arm pain.\n• Significance: Confirms nerve root decompression by opening neural foramina.",
        "consensus": "Core clinical orthopedic cluster for assessing cervical spondylotic radiculopathy.",
        "variations": "Spurling's test has high specificity (approx. 90%) but lower sensitivity (around 30–50%).",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Magee Orthopedic Physical Assessment"])
    },
    {
        "category": "Western Medicine",
        "title": "Orthopedic Tests: Lumbar Radiculopathy",
        "front": "Explain the Straight Leg Raise (SLR / Lasegue's) Test, Braggard's test, and the Crossed SLR test.",
        "back": "Straight Leg Raise (SLR / Lasegue):\n• Technique: Patient supine; examiner slowly elevates symptomatic leg passively with knee extended.\n• Positive Finding: Reproduction of radiating pain down the leg below the knee between 30° and 70° of hip flexion.\n• Braggard's Confirmation: Lower leg slightly until pain resolves, then dorsiflex foot. Recurrence of pain confirms dural/neural tension (L4-S1 nerve roots).\n\nCrossed Straight Leg Raise (Well Leg Raise):\n• Technique: Elevation of the asymptomatic leg.\n• Positive Finding: Reproduction of radicular pain in the contralateral (affected) leg.\n• Significance: Highly specific (around 90%) for a large central or paracentral lumbar disc herniation.",
        "consensus": "Standard clinical assessment for L4, L5, and S1 disc herniation and sciatic nerve compromise.",
        "variations": "Pain occurring only beyond 70° is typically due to hamstring tightness rather than true dural nerve root compression.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Magee Orthopedic Physical Assessment"])
    },
    {
        "category": "Western Medicine",
        "title": "Orthopedic Tests: Shoulder Impingement & Rotator Cuff",
        "front": "Outline Neer's Test, Hawkins-Kennedy Test, and the Empty Can (Jobe's) Test for shoulder pathology.",
        "back": "Subacromial Impingement Tests:\n• Neer's Test: Patient arm internally rotated (thumb down); examiner passively flexes arm forward overhead while stabilizing scapula. Pain indicates subacromial bursitis or supraspinatus impingement.\n• Hawkins-Kennedy Test: Arm flexed forward to 90° and elbow flexed to 90°; examiner forcefully internally rotates shoulder. Pain indicates impingement of supraspinatus tendon against coracoacromial ligament.\n\nRotator Cuff Tendon Testing:\n• Empty Can (Jobe's) Test: Arms abducted to 90° in scapular plane (30° forward), thumbs pointing down ('emptying a can'). Patient resists downward pressure. Weakness and pain indicate Supraspinatus tendon tear or severe tendinopathy.",
        "consensus": "Clinical triad for evaluating subacromial shoulder pain and rotator cuff tears before needling.",
        "variations": "Inability to maintain abduction at 90° with sudden arm drop indicates the 'Drop Arm Test' positive for full-thickness rotator cuff tear.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Magee Orthopedic Physical Assessment"])
    },
    {
        "category": "Western Medicine",
        "title": "Carpal Tunnel Syndrome: Phalen's & Tinel's Signs",
        "front": "Describe Phalen's Test, Tinel's Sign, and the anatomical contents of the Carpal Tunnel.",
        "back": "Diagnostic Tests:\n• Phalen's Test: Patient holds wrists in maximum unforced flexion (dorsa of hands pressed together) for 60 seconds. Positive if tingling, numbness, or burning paresthesia in median nerve distribution (thumb, index, middle, lateral ring finger).\n• Tinel's Sign: Light percussion over the palmar aspect of the flexor retinaculum at the wrist. Positive if electric tingling shoots into median nerve fingers.\n\nCarpal Tunnel Contents:\n• 9 Tendons: 4 flexor digitorum superficialis, 4 flexor digitorum profundus, 1 flexor pollicis longus.\n• 1 Nerve: Median Nerve (vulnerable to compression).\n• Note: Ulnar artery and ulnar nerve pass outside the carpal tunnel through Guyon's canal.",
        "consensus": "Primary compressive neuropathy of the upper extremity. Atrophy of thenar eminence indicates chronic severe denervation.",
        "variations": "Reverse Phalen's test (prayer position in maximum extension for 60s) also increases intracarpal tunnel pressure.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Netter's Orthopaedics"])
    },
    {
        "category": "Western Medicine",
        "title": "Diabetes Mellitus: Diagnostic Criteria & HbA1c",
        "front": "State the current laboratory diagnostic criteria for Diabetes Mellitus (Fasting Plasma Glucose, HbA1c, OGTT, Random Glucose).",
        "back": "Diagnostic Criteria (any ONE of the following, confirmed on repeat testing unless unequivocal symptoms exist):\n1. Hemoglobin A1c (HbA1c): ≥ 6.5% (Pre-diabetes: 5.7% – 6.4%; Normal < 5.7%).\n2. Fasting Plasma Glucose (FPG): ≥ 7.0 mmol/L (≥ 126 mg/dL) after an 8-hour fast (Pre-diabetes: 5.6–6.9 mmol/L; Normal < 5.6 mmol/L).\n3. 2-Hour Oral Glucose Tolerance Test (OGTT): ≥ 11.1 mmol/L (≥ 200 mg/dL) using 75g glucose load.\n4. Random Plasma Glucose: ≥ 11.1 mmol/L (≥ 200 mg/dL) in a patient with classic symptoms of hyperglycemia (polyuria, polydipsia, unexplained weight loss).",
        "consensus": "HbA1c reflects 3-month glycemic control based on erythrocyte lifespan.",
        "variations": "Hemoglobinopathies, hemolytic anemia, and recent blood transfusion can falsely lower HbA1c readings.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Diabetes Canada Clinical Practice Guidelines"])
    },
    {
        "category": "Western Medicine",
        "title": "Hypoglycemia vs Diabetic Ketoacidosis (DKA)",
        "front": "Contrast the signs, onset, and clinical emergency management of Hypoglycemia versus Diabetic Ketoacidosis (DKA).",
        "back": "Comparison:\n• Hypoglycemia (Blood Glucose < 4.0 mmol/L / 70 mg/dL):\n  - Onset: Sudden (minutes).\n  - Signs: Diaphoresis (cold clammy skin), tremor, tachycardia, palpitations, anxiety, confusion, slurred speech, hunger, seizures.\n  - Management: 'Rule of 15' - 15g fast-acting carbohydrates (juice, glucose tabs), recheck glucose in 15 min; glucagon or IV dextrose if unconscious.\n\n• Diabetic Ketoacidosis (DKA) (Hyperglycemia > 13.9 mmol/L with ketoacidosis):\n  - Onset: Gradual (hours to days).\n  - Signs: Kussmaul respirations (deep rapid breathing), fruity/acetone breath odor, dehydration, flushed dry skin, nausea/vomiting, abdominal pain, altered consciousness.\n  - Management: Emergency hospital transfer for IV fluids, potassium repletion, and continuous IV insulin.",
        "consensus": "When uncertain in an altered diabetic patient, always treat for hypoglycemia first, as acute brain hypoglycemia causes rapid irreversible neuronal death.",
        "variations": "Hypoglycemia unawareness can occur in patients on beta-blockers because sympathetic symptoms (tachycardia, tremor) are masked.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Harrison's Principles of Internal Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Complete Blood Count (CBC): High-Yield Values",
        "front": "Interpret key components of the Complete Blood Count (CBC): White Blood Cells (WBC), Hemoglobin (Hb), and Platelets.",
        "back": "Reference Values & Clinical Significance:\n• White Blood Cell (WBC): 4.0 – 11.0 x 10^9/L.\n  - Leukocytosis (> 11.0): Bacterial infection, acute inflammation, tissue necrosis, leukemia.\n  - Leukopenia (< 4.0): Viral infections, bone marrow suppression, autoimmune disorders.\n\n• Hemoglobin (Hb):\n  - Males: 135 – 175 g/L (13.5 – 17.5 g/dL); Females: 120 – 155 g/L (12.0 – 15.5 g/dL).\n  - Anemia: Fatigue, pallor, exertional dyspnea, tachycardia, orthostatic lightheadedness.\n\n• Platelet Count (PLT): 150 – 400 x 10^9/L.\n  - Thrombocytopenia (< 150): Increased bleeding and bruising risk.\n  - Acupuncture Safety: Puncturing caution when PLT < 50 x 10^9/L; contraindicated for deep needling if PLT < 20 x 10^9/L due to spontaneous bleeding/hematoma.",
        "consensus": "Crucial baseline lab test when assessing fatigue, infection, and bleeding risk prior to acupuncture.",
        "variations": "Neutrophil 'left shift' (increased immature band cells > 10%) signifies acute severe bacterial infection.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Laposata's Laboratory Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Anticoagulants & Antiplatelets",
        "front": "List common anticoagulant and antiplatelet drugs, their mechanisms, and clinical needling precautions.",
        "back": "Drug Classes:\n• Anticoagulants:\n  - Warfarin (Coumadin): Vitamin K antagonist (monitored via INR, therapeutic range typically 2.0–3.0).\n  - Direct Oral Anticoagulants (DOACs): Rivaroxaban (Xarelto), Apixaban (Eliquis), Dabigatran (Pradaxa) - Factor Xa and thrombin inhibitors.\n  - Heparins: LMWH (Enoxaparin / Lovenox).\n• Antiplatelets:\n  - Aspirin (acetylsalicylic acid), Clopidogrel (Plavix), Ticagrelor.\n\n⚠️ Needling Precautions:\n• Prolonged bleeding and extensive bruising/hematoma formation risk.\n• Use thinner gauge needles (38 to 40 gauge / 0.18–0.16 mm).\n• Avoid deep needling into vascular or inaccessible muscular spaces (e.g., deep popliteal, retrobulbar, pterygoid fossa).\n• Apply direct, prolonged pressure with sterile cotton upon withdrawal (minimum 60–90 seconds); do NOT rub.",
        "consensus": "Anticoagulated patients are not contraindicated for acupuncture, but require meticulous technique and prolonged compression.",
        "variations": "DOACs do not have routine INR monitoring, but have predictable anticoagulant peaks 2–4 hours after dosing.",
        "sources": json.dumps(["Royal TCM WM-03 & COM-06 Safety", "Goodman & Gilman's Pharmacological Basis of Therapeutics"])
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Corticosteroids & NSAIDs",
        "front": "What adverse effects of long-term Corticosteroids and NSAIDs are relevant to the acupuncture clinician?",
        "back": "Adverse Effects Relevant to Acupuncture:\n• Corticosteroids (e.g. Prednisone, Dexamethasone):\n  - Skin atrophy and capillary fragility ('paper-thin skin', easy tearing, bruising with minor needle insertion).\n  - Immunosuppression: Blunted inflammatory response, increased susceptibility to skin/tissue infection.\n  - Osteoporosis: Increased fracture risk with manual therapies or heavy cupping.\n  - Hyperglycemia and delayed wound healing.\n\n• NSAIDs (e.g. Ibuprofen, Naproxen, Celecoxib, Meloxicam):\n  - Gastrointestinal mucosal injury: Gastritis, peptic ulcer disease, occult GI bleeding (iron-deficiency anemia).\n  - Renal vasoconstriction: Exacerbation of hypertension and renal insufficiency.\n  - Reversible platelet dysfunction: Mild increase in needling bleeding/bruising.",
        "consensus": "Patients on long-term steroid therapy require gentle needling, strict asepsis, and avoidance of vigorous physical techniques.",
        "variations": "Sudden cessation of long-term systemic corticosteroids can induce acute adrenal crisis (hypotension, shock).",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Katzung Basic & Clinical Pharmacology"])
    },
    {
        "category": "Western Medicine",
        "title": "Infection Control: Bloodborne Pathogens",
        "front": "Compare Hepatitis B (HBV), Hepatitis C (HCV), and HIV regarding transmission risk via contaminated sharps and environmental stability.",
        "back": "Comparison:\n• Hepatitis B Virus (HBV):\n  - Needlestick transmission risk from infected source: Approx. 30% (highest risk).\n  - Environmental stability: Extremely resilient; can survive in dried blood on surfaces for at least 7 days.\n  - Prevention: Highly effective 3-dose vaccine series (mandatory for healthcare workers); Post-Exposure Prophylaxis (PEP) includes HBIG and vaccine.\n\n• Hepatitis C Virus (HCV):\n  - Needlestick transmission risk: Approx. 3%.\n  - Environmental stability: Survives on environmental surfaces for up to 3 weeks.\n  - Prevention: No vaccine currently available; direct-acting antivirals for chronic infection.\n\n• Human Immunodeficiency Virus (HIV):\n  - Needlestick transmission risk: Approx. 0.3%.\n  - Environmental stability: Extremely fragile outside host; rapidly inactivated by drying and disinfectants.\n  - Prevention: Post-exposure prophylaxis (PEP) within 72 hours for 28 days.",
        "consensus": "HBV presents the greatest occupational infectious risk to acupuncturists due to viral load and environmental durability.",
        "variations": "Universal / Standard Precautions dictate that all blood and bodily fluids must be treated as potentially infectious regardless of known status.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CDC Bloodborne Infectious Diseases Guidelines"])
    },
    {
        "category": "Western Medicine",
        "title": "Thyroid Disorders: Hypo vs Hyperthyroidism",
        "front": "Differentiate Hypothyroidism and Hyperthyroidism by clinical features and thyroid function laboratory tests (TSH, Free T4).",
        "back": "Clinical Comparison:\n• Hypothyroidism (Hashimoto's Thyroiditis most common):\n  - Features: Weight gain, cold intolerance, fatigue, constipation, dry coarse skin, bradycardia, periorbital edema, delayed deep tendon reflex relaxation.\n  - Labs: Primary Hypothyroidism = Elevated TSH, Low Free T4/T3.\n\n• Hyperthyroidism (Graves' Disease most common):\n  - Features: Weight loss, heat intolerance, palpitations, tachycardia, tremors, diarrhea, exophthalmos (Graves'), warm moist skin, hyperreflexia.\n  - Labs: Primary Hyperthyroidism = Suppressed/Low TSH (<0.01 mIU/L), Elevated Free T4/T3.",
        "consensus": "TSH is the most sensitive initial screening test for primary thyroid disorders.",
        "variations": "Subclinical hypothyroidism presents with mildly elevated TSH but normal Free T4 levels.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Harrison's Principles of Internal Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Renal Panel: BUN, Creatinine, and eGFR",
        "front": "Interpret Serum Creatinine, Blood Urea Nitrogen (BUN), and estimated Glomerular Filtration Rate (eGFR) in assessing kidney function.",
        "back": "Laboratory Markers:\n• Serum Creatinine: 60 – 110 μmol/L (0.7 – 1.2 mg/dL).\n  - Waste product of muscle metabolism; best index of renal clearance.\n  - Elevation indicates impaired renal filtration.\n• Blood Urea Nitrogen (BUN): 2.5 – 7.1 mmol/L (7 – 20 mg/dL).\n  - Elevated in renal failure, gastrointestinal bleeding, high protein intake, and dehydration.\n  - BUN:Creatinine ratio > 20:1 indicates prerenal azotemia / dehydration.\n• Estimated GFR (eGFR): Normal ≥ 90 mL/min/1.73m².\n  - Chronic Kidney Disease Stage 3: 30–59 mL/min.\n  - End-stage renal disease (ESRD / Stage 5): < 15 mL/min (requires dialysis or transplant).",
        "consensus": "Essential markers for monitoring renal disease, hypertension impact, and drug excretion.",
        "variations": "Creatinine generation is dependent on muscle mass; elderly or sarcopenic patients may have 'normal' creatinine despite significantly reduced GFR.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "National Kidney Foundation Guidelines"])
    },
    {
        "category": "Western Medicine",
        "title": "Liver Function Tests (LFTs): ALT, AST, Bilirubin, Albumin",
        "front": "Differentiate hepatocellular injury from cholestasis using liver enzymes (ALT, AST, ALP, GGT, Bilirubin).",
        "back": "Enzyme Patterns:\n• Hepatocellular Injury Pattern:\n  - ALT (Alanine Aminotransferase) and AST (Aspartate Aminotransferase) prominently elevated (often > 5–10x normal).\n  - ALT is more specific to liver tissue than AST.\n  - AST:ALT ratio > 2:1 strongly suggests alcoholic liver disease.\n\n• Cholestatic Pattern (Biliary Obstruction / Stasis):\n  - Alkaline Phosphatase (ALP) and GGT (Gamma-Glutamyl Transferase) prominently elevated.\n  - Elevation of direct (conjugated) bilirubin causing jaundice, dark urine, and pale acholic stools.\n\n• Liver Synthetic Function:\n  - Serum Albumin and Prothrombin Time (PT/INR) reflect true liver synthetic capacity (impaired in cirrhosis).",
        "consensus": "Differentiating hepatocellular vs obstructive jaundice directs surgical vs medical referral.",
        "variations": "Isolated ALP elevation with normal GGT indicates non-hepatic origin (bone growth, fracture healing, Paget's disease).",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Laposata's Laboratory Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Respiratory Pathology: Pneumonia vs Bronchitis vs Asthma",
        "front": "Distinguish between Acute Bronchitis, Community-Acquired Pneumonia, and Bronchial Asthma on physical examination and auscultation.",
        "back": "Differential Auscultation & Examination:\n• Community-Acquired Pneumonia:\n  - Signs: High fever, productive cough (purulent/rust-colored sputum), tachypnea, pleuritic chest pain.\n  - Auscultation: Localized inspiratory crackles (rales), bronchial breath sounds, increased tactile fremitus, dullness to percussion over consolidation, positive egophony ('E to A').\n\n• Acute Bronchitis:\n  - Signs: Cough lasting 1–3 weeks, usually viral, absence of consolidation.\n  - Auscultation: Clear breath sounds or scattered coarse rhonchi that clear with coughing; no dullness to percussion.\n\n• Bronchial Asthma:\n  - Signs: Episodic dyspnea, chest tightness, prolonged expiratory phase.\n  - Auscultation: Bilateral, diffuse, high-pitched expiratory wheezes; hyperresonance on percussion.",
        "consensus": "Presence of localized crackles, fever, and egophony warrants urgent chest X-ray to confirm pneumonia.",
        "variations": "A 'silent chest' in acute severe asthma (absent wheezing) is a life-threatening sign of impending respiratory arrest due to air movement failure.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Bates' Guide to Physical Examination"])
    },
    {
        "category": "Western Medicine",
        "title": "Cardiovascular Pathology: Heart Failure (Left vs Right)",
        "front": "Contrast the clinical manifestations of Left-Sided Heart Failure versus Right-Sided Heart Failure.",
        "back": "Clinical Comparison:\n• Left-Sided Heart Failure (Pulmonary Congestion):\n  - Symptoms: Dyspnea on exertion, orthopnea (shortness of breath when lying flat, needing multiple pillows), Paroxysmal Nocturnal Dyspnea (PND), dry cough, pink frothy sputum.\n  - Physical Signs: Bilateral bibasilar inspiratory crackles (rales), S3 gallop, laterally displaced apical impulse (PMI).\n\n• Right-Sided Heart Failure (Systemic Venous Congestion):\n  - Symptoms: Peripheral edema, abdominal bloating, right upper quadrant discomfort, fatigue.\n  - Physical Signs: Jugular Venous Distension (JVD) > 3 cm above sternal angle, dependent bilateral pitting ankle/pretibial edema, hepatomegaly, ascites, positive hepatojugular reflux.\n  - Most common cause of right heart failure is pre-existing left heart failure.",
        "consensus": "BNP (B-type Natriuretic Peptide) is the premier blood test for diagnosing acute heart failure exacerbation.",
        "variations": "Cor Pulmonale is isolated right ventricular failure resulting from primary pulmonary hypertension or severe chronic lung disease (COPD).",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Harrison's Principles of Internal Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Gastroenterology: Peptic Ulcer vs GERD",
        "front": "Differentiate Gastric Ulcer, Duodenal Ulcer, and Gastroesophageal Reflux Disease (GERD) by pain timing and meals.",
        "back": "Clinical Differentiation:\n• Gastric Ulcer:\n  - Pain Location: Epigastrium, burning or aching.\n  - Meal Relationship: Pain worsens immediately after eating (food stimulates gastric acid on open ulcer). Patients often avoid food, leading to weight loss.\n  - Etiology: H. pylori, NSAIDs; higher risk of malignancy.\n\n• Duodenal Ulcer:\n  - Meal Relationship: Pain improves with food/antacids and returns 2 to 4 hours postprandially ('pain-food-relief' cycle). Classically awakens patient at night (2–3 AM).\n  - Weight: Patients may eat frequently to relieve pain, leading to weight gain.\n\n• GERD:\n  - Symptoms: Retrosternal burning pyrosis ('heartburn') radiating upward, sour regurgitation, globus sensation, chronic nocturnal cough, worse when supine after meals.",
        "consensus": "Alarm features (dysphagia, vomiting, hematemesis, weight loss, age > 55) require urgent upper endoscopy.",
        "variations": "Perforated ulcer presents with sudden severe epigastric pain, board-like abdominal rigidity, and free air under diaphragm on erect chest X-ray.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Current Medical Diagnosis and Treatment"])
    },
    {
        "category": "Western Medicine",
        "title": "Dermatology: Malignant Melanoma (ABCDE Criteria)",
        "front": "State the ABCDE criteria for early identification of suspected Malignant Melanoma on the skin.",
        "back": "ABCDE Clinical Criteria:\n• A - Asymmetry: One half of the mole or lesion does not match the other half.\n• B - Border: Irregular, scalloped, notched, or poorly defined edges.\n• C - Color: Variegated color across lesion (shades of brown, black, white, red, or blue).\n• D - Diameter: Greater than 6 mm (approx. pencil eraser size), although melanomas can be smaller.\n• E - Evolving: Any lesion that is changing in size, shape, elevation, color, or developing new symptoms (bleeding, itching, crusting).\n\n⚠️ Acupuncture Precaution:\n• NEVER puncture through, needle into, or apply moxa/cupping over an undiagnosed pigmented skin lesion.\n• Promptly refer to physician / dermatologist for excisional biopsy.",
        "consensus": "High-index of suspicion is required during skin inspection prior to needle insertion.",
        "variations": "Nodular melanoma may lack ABCDE features and present as an elevated, firm, rapidly growing (EFG) symmetric papule.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Fitzpatrick's Dermatology in General Medicine"])
    },
    {
        "category": "Western Medicine",
        "title": "Neurology: Dermatomes Key Sensory Landmarks",
        "front": "List the classic sensory dermatome landmarks for C6, C7, C8, T4, T10, L4, L5, and S1.",
        "back": "Key Dermatomal Landmarks:\n• C6: Thumb and radial aspect of the forearm.\n• C7: Middle finger (central hand).\n• C8: Little finger and ulnar aspect of the hand.\n• T4: Level of the nipples.\n• T10: Level of the umbilicus.\n• L4: Medial lower leg, medial malleolus, and big toe.\n• L5: Dorsum of the foot, web space between 1st and 2nd toes, lateral calf.\n• S1: Lateral malleolus, lateral border of foot, little toe, and sole/heel.\n• S2-S4: Perineum and perianal region ('saddle area' - cauda equina).",
        "consensus": "Essential topographical landmarks for localizing spinal cord and nerve root radicular lesions.",
        "variations": "There is significant overlap between adjacent dermatomes; sensory loss is most distinct in the autonomous sensory zones (e.g. index finger for C7, great toe web for L5).",
        "sources": json.dumps(["Royal TCM WM-01 Basic of Western Medicine", "Netter's Clinical Anatomy"])
    },
    {
        "category": "Western Medicine",
        "title": "Orthopedics: Knee Ligament & Meniscal Tests",
        "front": "Describe Lachman's test, Anterior Drawer test, McMurray's test, and Apley's grind test for knee injuries.",
        "back": "Knee Examination Tests:\n• Anterior Cruciate Ligament (ACL):\n  - Lachman's Test: Knee flexed to 20°–30°; examiner translates tibia anteriorly while stabilizing femur. Increased translation and soft end-feel indicates ACL tear (most sensitive test, ~85%).\n  - Anterior Drawer Test: Knee flexed to 90°; tibia pulled anteriorly. Less sensitive due to hamstring guarding.\n\n• Meniscal Tears:\n  - McMurray's Test: Knee fully flexed; tibia rotated externally (medial meniscus) or internally (lateral meniscus) while extending knee with valgus/varus stress. Palpable click or joint line pain indicates tear.\n  - Apley's Grind Test: Patient prone, knee flexed to 90°; downward axial compression with internal/external rotation causes joint line pain.",
        "consensus": "Acute hemarthrosis within 2 hours of a knee 'pop' injury indicates ACL tear until proven otherwise.",
        "variations": "The Pivot-Shift test is the most specific test for ACL insufficiency under anesthesia.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Magee Orthopedic Physical Assessment"])
    },
    {
        "category": "Western Medicine",
        "title": "Pharmacology: Beta-Blockers & Antihypertensives",
        "front": "Explain the mechanism of Beta-Blockers (e.g., Metoprolol, Atenolol) and their influence on pulse assessment and exercise.",
        "back": "Pharmacology & Clinical Effects:\n• Mechanism: Antagonism of Beta-1 adrenergic receptors in the heart; decreases heart rate, myocardial contractility, and cardiac output; decreases renin release.\n• Impact on Pulse Diagnosis:\n  - Artificially slows resting heart rate (bradycardia, often 50–60 bpm).\n  - Blunts pulse strength and rate acceleration. Acupuncturist must not misinterpret drug-induced slow pulse as pure Yang deficiency or internal cold without checking medication history.\n• Other Antihypertensives:\n  - ACE Inhibitors (e.g. Ramipril, Lisinopril): Associated with chronic dry hacking cough (accumulation of bradykinin), which can be mistaken for Lung Yin deficiency cough.\n  - Calcium Channel Blockers (e.g. Amlodipine): Frequently cause dependent bilateral pretibial/ankle edema.",
        "consensus": "Medication reconciliation is essential to prevent misdiagnosis of drug side effects as TCM patterns.",
        "variations": "Non-selective beta-blockers (e.g. Propranolol) are contraindicated in asthma due to bronchospasm via Beta-2 antagonism.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "Katzung Basic & Clinical Pharmacology"])
    },
    {
        "category": "Western Medicine",
        "title": "Medical Emergencies: Anaphylaxis Management",
        "front": "What are the clinical diagnostic criteria for Anaphylaxis, and what is the immediate first-line medical intervention?",
        "back": "Diagnostic Criteria (Acute onset involving TWO or more systems after allergen exposure):\n1. Skin/Mucosa: Generalized hives (urticaria), pruritus, flushing, swollen lips/tongue/uvula (angioedema).\n2. Respiratory: Dyspnea, wheezing, stridor (laryngeal edema), hypoxemia.\n3. Cardiovascular: Hypotension (Systolic BP < 90 mmHg), syncope, tachycardia.\n4. Gastrointestinal: Severe crampy abdominal pain, vomiting, diarrhea.\n\n⚠️ Immediate First-Line Medical Intervention:\n• Epinephrine (Adrenaline) 1:1,000 (1 mg/mL) Intramuscular (IM) into the anterolateral mid-thigh immediately (Adult dose: 0.3 – 0.5 mg; Pediatric: 0.01 mg/kg or 0.15 mg EpiPen Jr).\n• Call 911 immediately.\n• Place patient supine with legs elevated (unless respiratory distress dictates sitting upright); never stand or walk.\n• Repeat epinephrine in 5–15 minutes if symptoms persist.",
        "consensus": "Epinephrine is the ONLY life-saving first-line medication for anaphylaxis. Antihistamines and steroids are second-line adjunctive therapies only.",
        "variations": "Biphasic anaphylaxis can recur up to 72 hours later (typically 8–10 hours) without re-exposure, necessitating emergency observation.",
        "sources": json.dumps(["Royal TCM WM-03 Clinical Medicine", "World Allergy Organization Guidelines"])
    },
    {
        "category": "Western Medicine",
        "title": "Red Flags: Acute Abdomen Differentiation",
        "front": "List the clinical red flags that distinguish an 'Acute Surgical Abdomen' from functional abdominal pain.",
        "back": "Acute Surgical Abdomen Red Flags:\n• Sudden onset of severe, unrelenting abdominal pain (lasting > 6 hours).\n• Involuntary abdominal muscular guarding or 'board-like' rigidity.\n• Marked rebound tenderness (Blumberg's sign) indicating widespread peritonitis.\n• High fever with chills, tachycardia, and hypotension (signs of sepsis).\n• Inability to keep fluids down, absent bowel sounds (paralytic ileus), or high-pitched tinkling rushes with distension (mechanical obstruction).\n• Presence of pulsatile abdominal mass (suspected Abdominal Aortic Aneurysm - AAA rupture risk).\n• Syncope or severe dizziness accompanying acute abdominal or pelvic pain (ectopic pregnancy rupture in women of childbearing age).\n\n⚠️ Protocol: Zero oral intake (NPO), withhold analgesics that mask symptoms, call 911 / urgent surgical emergency referral.",
        "consensus": "Involuntary guarding and rebound tenderness are universal surgical indicators requiring immediate hospital transfer.",
        "variations": "Rupturing AAA can present with sudden severe tearing back/flank pain mimicking severe renal colic or acute lumbago.",
        "sources": json.dumps(["Royal TCM WM-02 Diagnostics", "Cope's Early Diagnosis of the Acute Abdomen"])
    }
]

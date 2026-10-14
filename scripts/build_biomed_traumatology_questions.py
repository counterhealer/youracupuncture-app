# -*- coding: utf-8 -*-
"""
Builder script to generate 75 high-yield Biomedicine & Traumatology board questions
extracted from Royal TCM WM-02 Diagnostics & TCM-10 Traumatology course materials:
1. 25 Laboratory Examinations & Diagnostic Values (CBC, Liver/Renal, Coagulation, Cardiac, Urinalysis, Endocrine)
2. 25 Physical Examination & Clinical Signs (Vital signs, Abdominal signs, Thoracic sounds, Neuro reflexes)
3. 25 Traumatology & Orthopedic Physical Exam (Spine, Shoulder, Elbow, Wrist, Hip, Knee, Ankle, Fractures)
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "exam_questions.json")

# Load existing questions
with open(DATA_FILE, "r", encoding="utf-8") as f:
    existing_questions = json.load(f)

start_id = max(q["id"] for q in existing_questions if isinstance(q.get("id"), int)) + 1
print(f"Current question count: {len(existing_questions)}. Starting new questions at ID {start_id}...")

NEW_QUESTIONS = [
    # -------------------------------------------------------------------------
    # PART 1: LABORATORY EXAMINATIONS & DIAGNOSTIC VALUES (25 QUESTIONS)
    # -------------------------------------------------------------------------
    {
        "id": start_id,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A complete blood count (CBC) reveals a hemoglobin of 8.8 g/dL, hematocrit of 28%, and a Mean Corpuscular Volume (MCV) of 68 fL (normal 80–100 fL). Which condition is most strongly indicated by this microcytic hypochromic pattern?",
        "options": [
            "Vitamin B12 or Folate Deficiency Anemia",
            "Iron Deficiency Anemia",
            "Aplastic Anemia",
            "Acute Hemolytic Anemia"
        ],
        "answer": 1,
        "explanation": "Option B is correct. An MCV below 80 fL indicates microcytic anemia, which is characteristically caused by iron deficiency anemia, thalassemia, or chronic lead poisoning. In iron deficiency, serum ferritin is low. Option A (B12/folate deficiency) causes macrocytic anemia with MCV > 100 fL. Options C and D typically present as normocytic normochromic anemia (MCV 80–100 fL)."
    },
    {
        "id": start_id + 1,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 32-year-old female presents with sudden high fever, productive cough with rust-colored sputum, and right lower chest pain. Her white blood cell (WBC) count is 16,500/μL with 88% neutrophils and 12% band forms (left shift). What does this laboratory pattern indicate?",
        "options": [
            "Acute systemic viral infection",
            "Acute bacterial infection (e.g., lobar pneumonia)",
            "Allergic asthma exacerbation",
            "Chronic myelogenous leukemia"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Marked leukocytosis (> 10,000/μL) with neutrophilia (> 70%) and a 'shift to the left' (presence of immature band neutrophils > 5%) is the classic laboratory hallmark of acute bacterial infection, such as pneumococcal lobar pneumonia. Option A (viral infections) typically shows lymphocytosis with normal or decreased WBC. Option C causes eosinophilia. Option D shows extreme leukocytosis (> 50,000/μL) with basophilia."
    },
    {
        "id": start_id + 2,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A cancer patient undergoing chemotherapy requests acupuncture for chemotherapy-induced nausea. A review of their morning lab report reveals a platelet count of 28,000/μL (normal 150,000–450,000/μL). What is the mandatory clinical action?",
        "options": [
            "Perform standard acupuncture with smaller 36-gauge needles",
            "Defer all needle insertion due to high risk of spontaneous hematoma and internal bleeding",
            "Perform electroacupuncture at 100 Hz to stimulate bone marrow megakaryocytes",
            "Apply strong cupping and bloodletting at BL40 to clear chemotherapy toxins"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Severe thrombocytopenia with platelets < 50,000/μL represents a major bleeding hazard; needle puncture can induce severe subcutaneous hematomas or uncontrolled bleeding. Platelets < 20,000/μL carries high risk of spontaneous intracranial hemorrhage. Needle insertion, cupping, and gua sha are contraindicated. Non-invasive acupressure (e.g. PC6 wrist bands) may be used safely."
    },
    {
        "id": start_id + 3,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 68-year-old female presents with a severe unilateral throbbing headache, scalp tenderness when brushing her hair, and jaw claudication when chewing. Her Erythrocyte Sedimentation Rate (ESR / 西医血沉) is 108 mm/h (normal < 30 mm/h). What is the primary biomedical diagnosis and mandatory referral?",
        "options": [
            "Tension-type headache; treat with GB20 and Taiyang",
            "Trigeminal neuralgia; refer for neurology outpatient clinic",
            "Temporal Arteritis (Giant Cell Arteritis); send immediately to the Emergency Department for corticosteroids to prevent permanent blindness",
            "Osteoarthritis of the temporomandibular joint; prescribe local heat and moxibustion"
        ],
        "answer": 2,
        "explanation": "Option C is correct. Massive elevation of ESR (> 100 mm/h) or C-reactive protein (CRP) in an elderly patient with headache, scalp tenderness, and jaw claudication is the classic presentation of Temporal Arteritis (Giant Cell Arteritis). It requires immediate same-day hospital transfer for high-dose systemic corticosteroids (prednisone) to prevent irreversible ischemic optic neuropathy and sudden bilateral blindness."
    },
    {
        "id": start_id + 4,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with mechanical heart valves is taking Warfarin (Coumadin). Their monthly International Normalized Ratio (INR) is measured at 4.6 (therapeutic target 2.0–3.0). Which statement regarding acupuncture and herbal safety is TRUE?",
        "options": [
            "Needling and herbal therapy can proceed normally as INR 4.6 is optimal",
            "The patient is at high risk of fatal hemorrhage; withhold all blood-invigorating herbs (e.g., Dan Shen, Dang Gui, San Qi) and notify the prescribing physician immediately",
            "Prescribe heavy doses of Gan Cao (Licorice) to raise blood pressure",
            "Recommend high doses of Ginkgo Biloba (Bai Guo) to prevent clotting"
        ],
        "answer": 1,
        "explanation": "Option B is correct. An INR > 4.0 places the patient at dangerous risk for spontaneous bleeding, gastrointestinal hemorrhage, and hemorrhagic stroke. Chinese herbs that vigorously activate blood and inhibit platelet aggregation (Dan Shen, Dang Gui, Tao Ren, Hong Hua, San Qi, Shui Zhi) or contain coumarin derivatives will compound this risk. The prescribing physician must be notified immediately."
    },
    {
        "id": start_id + 5,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "Which laboratory biomarker is considered the gold standard for ruling in or ruling out Acute Myocardial Infarction (AMI) due to its exceptional cardiac specificity and prolonged elevation (up to 10–14 days)?",
        "options": [
            "Total Creatine Kinase (CK)",
            "Cardiac Troponin I or T (cTnI / cTnT)",
            "Lactate Dehydrogenase (LDH)",
            "Myoglobin"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Cardiac Troponin I (cTnI) and Troponin T (cTnT) are regulatory contractile proteins uniquely specific to the myocardium. Following acute myocardial infarction, troponins rise within 3–4 hours, peak around 24 hours, and remain elevated for 10–14 days. CK-MB (Option A) returns to baseline in 48–72 hours. Myoglobin (Option D) rises earliest (1–2h) but lacks cardiac specificity."
    },
    {
        "id": start_id + 6,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 72-year-old patient with bilateral ankle edema, orthopnea, and paroxysmal nocturnal dyspnea has a serum B-type Natriuretic Peptide (BNP) level of 850 pg/mL (normal < 100 pg/mL). What clinical condition does this strongly support?",
        "options": [
            "Decompensated Congestive Heart Failure (CHF)",
            "Acute Glomerulonephritis",
            "Chronic Obstructive Pulmonary Disease without cor pulmonale",
            "Deep Vein Thrombosis"
        ],
        "answer": 0,
        "explanation": "Option A is correct. BNP is synthesized and released by ventricular myocytes in direct response to increased ventricular wall tension, stretching, and volume overload. A BNP > 400 pg/mL has over 95% predictive accuracy for acute decompensated congestive heart failure (CHF) and reliably differentiates cardiac dyspnea from primary pulmonary causes."
    },
    {
        "id": start_id + 7,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 48-year-old male with a history of chronic alcohol abuse presents with jaundice, dark urine, and spider angiomas. Blood chemistry reveals AST (SGOT) 280 U/L and ALT (SGPT) 120 U/L. What is the diagnostic significance of this AST/ALT ratio > 2.0 (De Ritis ratio)?",
        "options": [
            "Characteristic of Alcoholic Hepatitis / Alcoholic Liver Disease",
            "Characteristic of Acute Viral Hepatitis A or B",
            "Indicates Biliary Atresia or gallstones",
            "Indicates Acute Pancreatitis"
        ],
        "answer": 0,
        "explanation": "Option A is correct. While ALT is generally higher than AST in viral hepatitis and non-alcoholic fatty liver disease (AST/ALT ratio < 1), an AST to ALT ratio greater than 2.0 with AST < 500 U/L is strongly suggestive of Alcoholic Liver Disease/Hepatitis. This occurs because alcohol reduces hepatic pyridoxal-5-phosphate (vitamin B6), which suppresses ALT synthesis more severely than AST."
    },
    {
        "id": start_id + 8,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 52-year-old female presents with severe right upper quadrant colic after eating fried chicken, followed by yellowing of the sclera, dark tea-colored urine, and clay-colored (acholic) pale stools. Which laboratory findings are most expected?",
        "options": [
            "Elevated unconjugated (indirect) bilirubin with normal urine bilirubin",
            "Markedly elevated conjugated (direct) bilirubin and positive urine bilirubin (Obstructive Jaundice)",
            "Elevated blood urea nitrogen with normal liver enzymes",
            "Decreased alkaline phosphatase (ALP) with normal bilirubin"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Clay-colored (acholic) pale stools combined with dark tea-colored urine and jaundice are hallmarks of post-hepatic obstructive jaundice (e.g., choledocholithiasis / gallstone obstructing the common bile duct). Conjugated (direct) bilirubin cannot enter the duodenum and backs up into the bloodstream, where it is water-soluble and excreted in the urine. Alkaline phosphatase (ALP) and GGT are also markedly elevated."
    },
    {
        "id": start_id + 9,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with chronic cirrhosis presents with progressive abdominal distension. Abdominal examination reveals shifting dullness, fluid wave, and serum albumin of 2.1 g/dL (normal 3.5–5.0 g/dL). What is the primary pathophysiological mechanism causing this ascites?",
        "options": [
            "Decreased plasma colloid oncotic pressure due to impaired hepatic albumin synthesis",
            "Excessive lymphatic drainage from thoracic duct obstruction",
            "Severe systemic arteriolar vasoconstriction",
            "High urinary excretion of potassium"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Albumin is synthesized exclusively by the liver and accounts for approximately 80% of plasma colloid oncotic pressure. In end-stage cirrhosis, marked hypoalbuminemia (< 2.5 g/dL) decreases capillary oncotic pressure, allowing plasma fluid to extravasate into the peritoneal cavity and interstitial tissues, creating ascites and peripheral edema."
    },
    {
        "id": start_id + 10,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "Which serum laboratory value is the most accurate and reliable indicator for assessing chronic renal function and determining the stage of Chronic Kidney Disease (CKD)?",
        "options": [
            "Blood Urea Nitrogen (BUN) alone",
            "Serum Uric Acid level",
            "Estimated Glomerular Filtration Rate (eGFR) calculated from Serum Creatinine",
            "Urine specific gravity"
        ],
        "answer": 2,
        "explanation": "Option C is correct. While BUN is easily affected by hydration status, protein intake, and GI bleeding, the Estimated Glomerular Filtration Rate (eGFR) derived from serum creatinine (using CKD-EPI or MDRD formulas) reflects the functional filtering capacity of nephrons and serves as the clinical gold standard for classifying Chronic Kidney Disease from Stage 1 (>90 mL/min) to Stage 5 (<15 mL/min)."
    },
    {
        "id": start_id + 11,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Easy",
        "exam": "Pan-Canadian Board Exam",
        "question": "According to the American Diabetes Association (ADA) and Canadian Diabetes clinical guidelines, which laboratory finding diagnostic of Diabetes Mellitus?",
        "options": [
            "Fasting plasma glucose ≥ 126 mg/dL (7.0 mmol/L) on two separate occasions",
            "Glycated hemoglobin (HbA1c) of 5.8%",
            "Random plasma glucose of 140 mg/dL with no symptoms",
            "2-hour postprandial glucose of 135 mg/dL during OGTT"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Diabetes Mellitus is diagnosed by: 1) Fasting plasma glucose ≥ 126 mg/dL (7.0 mmol/L) confirmed on repeat testing; 2) HbA1c ≥ 6.5%; 3) 2-hour plasma glucose ≥ 200 mg/dL (11.1 mmol/L) during a 75g OGTT; or 4) Random plasma glucose ≥ 200 mg/dL in a patient with classic symptoms of hyperglycemia (polyuria, polydipsia, weight loss)."
    },
    {
        "id": start_id + 12,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A routine urinalysis of a 28-year-old male with acute facial puffiness and dark 'cola-colored' urine reveals 3+ protein, 4+ blood, and Red Blood Cell (RBC) casts on microscopic sediment. What pathology do RBC casts specifically identify?",
        "options": [
            "Lower urinary tract infection (cystitis)",
            "Acute Glomerulonephritis (glomerular injury)",
            "Renal stone in the distal ureter",
            "Benign prostatic hyperplasia"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Red Blood Cell (RBC) casts are formed in the renal tubules when erythrocytes pass through a damaged glomerular basement membrane and become entrapped in Tamm-Horsfall mucoprotein. Their presence is pathognomonic for glomerular bleeding, most classically Acute Post-Streptococcal Glomerulonephritis or rapidly progressive glomerulonephritis."
    },
    {
        "id": start_id + 13,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 35-year-old female presents with fatigue, cold intolerance, weight gain, constipation, and periorbital edema. Laboratory blood work shows elevated Thyroid Stimulating Hormone (TSH: 14.2 μIU/mL, normal 0.4–4.0) and decreased Free Thyroxine (Free T4: 0.4 ng/dL, normal 0.8–1.8). What is the diagnosis?",
        "options": [
            "Primary Hyperthyroidism (Graves' disease)",
            "Primary Hypothyroidism (e.g., Hashimoto's thyroiditis)",
            "Pituitary / Secondary Hypothyroidism",
            "Subclinical Hypothyroidism"
        ],
        "answer": 1,
        "explanation": "Option B is correct. High TSH accompanied by low Free T4 confirms Primary Hypothyroidism, most commonly due to autoimmune Hashimoto's thyroiditis. The anterior pituitary gland detects deficient circulating thyroid hormones and secretes excess TSH via negative feedback. Option C (Secondary) would present with low or inappropriately normal TSH and low T4. Option D shows high TSH with normal Free T4."
    },
    {
        "id": start_id + 14,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "Which serological marker indicates active chronic infection and high viral infectivity in a patient diagnosed with Hepatitis B virus (HBV)?",
        "options": [
            "Anti-HBs (Hepatitis B surface antibody)",
            "HBsAg (Hepatitis B surface antigen) and HBeAg (Hepatitis B envelope antigen)",
            "Anti-HAV IgM",
            "Anti-HCV IgG"
        ],
        "answer": 1,
        "explanation": "Option B is correct. HBsAg is the primary hallmark of active HBV infection (persisting > 6 months defines chronic infection). HBeAg is a marker of active viral replication and maximum infectivity. In contrast, Anti-HBs (Option A) indicates recovery and clinical immunity (either from cleared infection or immunization). Clean Needle Technique protocols mandate strict precautions."
    },
    {
        "id": start_id + 15,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with severe acute retrosternal chest pain has a normal ECG. 3 hours later, their plasma D-Dimer is markedly elevated at 2,400 ng/mL (normal < 500 ng/mL). What critical thromboembolic condition must be urgently ruled out?",
        "options": [
            "Pulmonary Embolism (PE) or Deep Vein Thrombosis (DVT)",
            "Acute Appendicitis",
            "Gouty Arthritis",
            "Duodenal Peptic Ulcer"
        ],
        "answer": 0,
        "explanation": "Option A is correct. D-Dimer is a degradation product of cross-linked fibrin created when plasmin dissolves a blood clot. A positive D-Dimer has very high sensitivity (>95%) for venous thromboembolism (DVT and Pulmonary Embolism). An elevated D-Dimer with chest pain or dyspnea requires immediate emergency department evaluation with CT pulmonary angiography."
    },
    {
        "id": start_id + 16,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 55-year-old male presents with sudden excruciating pain, erythema, and marked swelling of the first metatarsophalangeal (MTP) joint. His serum uric acid level is 9.4 mg/dL (normal 3.5–7.2 mg/dL). What is the primary diagnosis and joint name?",
        "options": [
            "Pseudogout of the knee joint",
            "Acute Gouty Arthritis (Podagra / 痛风)",
            "Septic arthritis of the ankle joint",
            "Osteoarthritis Heberden's node"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Hyperuricemia (> 7.0 mg/dL) with acute monoarthritis of the 1st MTP joint (classically termed Podagra) is the hallmark presentation of acute Gouty Arthritis. In TCM traumatology and acupuncture, this location corresponds directly to Spleen 3 (Taibai) and Spleen 4 (Gongsun), representing damp-heat and blood stasis accumulation."
    },
    {
        "id": start_id + 17,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 42-year-old female presents with symmetrical pain and morning stiffness lasting > 1 hour in both hands (MCP and PIP joints). Which laboratory test has the highest diagnostic specificity (> 95%) for confirming Rheumatoid Arthritis (RA)?",
        "options": [
            "Rheumatoid Factor (RF) alone",
            "Anti-Cyclic Citrullinated Peptide Antibody (Anti-CCP / 抗CCP抗体)",
            "Complete Blood Count (CBC)",
            "Serum Albumin"
        ],
        "answer": 1,
        "explanation": "Option B is correct. While Rheumatoid Factor (RF) is sensitive (~70%), it can be positive in healthy elderly, Sjogren's, and lupus. Anti-CCP antibodies possess equal sensitivity (~75%) but markedly superior specificity (>95%) for Rheumatoid Arthritis and predict progressive joint erosions. Both RF and Anti-CCP are included in the ACR/EULAR diagnostic criteria."
    },
    {
        "id": start_id + 18,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 24-year-old female presents with malar butterfly rash, photosensitivity, mouth ulcers, joint aches, and proteinuria. Which autoantibody screening test is the most sensitive initial test for Systemic Lupus Erythematosus (SLE)?",
        "options": [
            "Antinuclear Antibody (ANA) by Immunofluorescence (>98% sensitivity)",
            "Anti-Smooth Muscle Antibody (ASMA)",
            "Anti-Centromere Antibody",
            "Rheumatoid Factor"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Antinuclear Antibody (ANA) is positive in over 98% of patients with active Systemic Lupus Erythematosus (SLE), making it the supreme initial screening test. A negative ANA essentially rules out SLE. If ANA is positive, disease-specific confirmatory testing follows with Anti-dsDNA (correlates with lupus nephritis) and Anti-Smith (Sm) antibodies."
    },
    {
        "id": start_id + 19,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "In assessing a patient with acute severe epigastric pain radiating directly through to the back, which serum pancreatic enzyme level is more specific and remains elevated longer for the diagnosis of Acute Pancreatitis?",
        "options": [
            "Serum Amylase",
            "Serum Lipase",
            "Alkaline Phosphatase",
            "Serum Potassium"
        ],
        "answer": 1,
        "explanation": "Option B is correct. While both serum amylase and serum lipase rise rapidly within 4–8 hours of acute pancreatitis, serum Lipase has higher sensitivity and specificity (85–100%) because amylase is also produced by salivary glands and other organs. Lipase also remains elevated for 8–14 days, whereas amylase normalizes within 3–5 days."
    },
    {
        "id": start_id + 20,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Easy",
        "exam": "Pan-Canadian Board Exam",
        "question": "A routine dipstick urinalysis shows trace glucose, negative ketones, 3+ leukocyte esterase, and positive nitrites. The patient reports burning upon urination, urgency, and frequency. What does this indicate?",
        "options": [
            "Diabetic ketoacidosis",
            "Acute Bacterial Urinary Tract Infection (Cystitis)",
            "Glomerular amyloidosis",
            "Renal cell carcinoma"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Leukocyte esterase indicates the presence of white blood cells (pyuria), and a positive nitrite test indicates that Gram-negative bacteria (predominantly *Escherichia coli*) have reduced dietary nitrates to nitrites. Combined with dysuria, urgency, and frequency, this confirms an acute bacterial UTI (TCM Lin syndrome)."
    },
    {
        "id": start_id + 21,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 60-year-old male with chronic hypertension undergoes routine blood work. His serum creatinine is 1.8 mg/dL and BUN is 42 mg/dL. He is taking Lisinopril (an ACE inhibitor). Which electrolyte abnormality must be monitored most closely with ACE inhibitors?",
        "options": [
            "Hypokalemia (low potassium)",
            "Hyperkalemia (elevated serum potassium > 5.0 mEq/L)",
            "Hyponatremia (low sodium)",
            "Hypercalcemia (elevated calcium)"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Angiotensin-Converting Enzyme (ACE) inhibitors inhibit aldosterone secretion in the adrenal cortex. Because aldosterone promotes potassium excretion in exchange for sodium in the distal tubule, blocking it leads to potassium retention and Hyperkalemia. Concomitant use with potassium-rich herbs or potassium-sparing diuretics increases cardiac arrhythmia risks."
    },
    {
        "id": start_id + 22,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "An emergency lumbar puncture is performed on a 19-year-old college student with sudden fever, severe headache, nuchal rigidity, and petechial skin rash. The cerebrospinal fluid (CSF) analysis reveals cloudy appearance, marked polymorphonuclear neutrophilia, elevated opening pressure, elevated protein (180 mg/dL), and decreased glucose (< 20 mg/dL). What is the diagnosis?",
        "options": [
            "Viral / Aseptic Meningitis",
            "Acute Bacterial Meningitis (e.g., *Neisseria meningitidis*)",
            "Multiple Sclerosis exacerbation",
            "Normal pressure hydrocephalus"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The classic triad of bacterial meningitis CSF findings is: 1) Low glucose (< 40 mg/dL or CSF/serum ratio < 0.4 due to bacterial consumption); 2) High protein (> 100 mg/dL); and 3) Marked polymorphonuclear neutrophilic pleocytosis (> 1,000/μL). Viral meningitis typically presents with normal glucose and lymphocytic pleocytosis. Immediate IV antibiotics are life-saving."
    },
    {
        "id": start_id + 23,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "What is the primary clinical significance of detecting microscopic microalbuminuria (30–300 mg/24 hours) in a patient with a 10-year history of Type 2 Diabetes Mellitus?",
        "options": [
            "Indicates complete remission of kidney pathology",
            "Serves as the earliest detectable clinical sign of Diabetic Nephropathy and high cardiovascular risk",
            "Indicates urinary tract bladder stone formation",
            "Reflects excessive dietary intake of carbohydrate"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Normal urinary albumin excretion is < 30 mg/day. Microalbuminuria (30–300 mg/day) represents early, reversible glomerular capillary damage and is the earliest clinical marker of diabetic nephropathy as well as an independent risk factor for systemic cardiovascular events. Starting ACE inhibitors or ARBs at this stage slows progression to macroalbuminuria."
    },
    {
        "id": start_id + 24,
        "category": "Biomedical Labs & Western Diagnostics",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 56-year-old male with chronic back pain has an asymptomatic screening Fecal Occult Blood Test (FOBT / 便隐血试验) that returns positive. His CBC shows a microcytic anemia (Hgb 10.2 g/dL, MCV 72 fL). What is the mandatory clinical recommendation?",
        "options": [
            "Prescribe Spleen-tonifying herbs and retest stool in 6 months",
            "Advise immediate colonoscopy to rule out Colorectal Adenocarcinoma or advanced adenoma",
            "Reassure the patient that hemorrhoids are the sole cause",
            "Perform moxibustion on CV8 and ST36"
        ],
        "answer": 1,
        "explanation": "Option B is correct. In patients over 50 years of age, unexplained iron deficiency anemia and a positive fecal occult blood test (FOBT) is Colorectal Cancer until proven otherwise. Right-sided colon carcinomas typically present with occult bleeding, microcytic anemia, and fatigue without visible red blood in stools. Immediate gastroenterology referral for full diagnostic colonoscopy is mandatory."
    },

    # -------------------------------------------------------------------------
    # PART 2: PHYSICAL EXAMINATION & CLINICAL SIGNS (25 QUESTIONS)
    # -------------------------------------------------------------------------
    {
        "id": start_id + 25,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient presents for chronic knee pain. Routine vital signs measurement reveals a blood pressure of 196/124 mmHg. The patient complains of a throbbing occipital headache, blurred vision, and chest tightness. What is this clinical state classified as, and what is the proper action?",
        "options": [
            "Stage 1 Hypertension; proceed with acupuncture needling at LV3 and KD1",
            "Hypertensive Urgency; give patient a cup of hot green tea and re-measure in 1 hour",
            "Hypertensive Emergency (危象) with acute target organ damage; call 911 EMS immediately for hospital emergency transfer",
            "White-coat hypertension; ignore the reading and treat knee pain"
        ],
        "answer": 2,
        "explanation": "Option C is correct. Severe blood pressure elevation (Systolic > 180 mmHg or Diastolic > 120 mmHg) accompanied by signs of acute target-organ damage (headache, encephalopathy, visual disturbances, chest pain, dyspnea) constitutes a Hypertensive Emergency. Immediate 911 dispatch is required for monitored parenteral IV antihypertensives to prevent fatal stroke, aortic dissection, or acute heart failure."
    },
    {
        "id": start_id + 26,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "During abdominal palpation of a 44-year-old female with acute right hypochondriac pain, the examiner places a hand beneath the right costal margin at the midclavicular line and asks the patient to inhale deeply. The patient suddenly gasps and arrests inspiration due to sharp pain. What is this physical sign?",
        "options": [
            "McBurney's Sign",
            "Positive Murphy's Sign (墨菲征阳性 / 急性胆囊炎)",
            "Courvoisier's Sign",
            "Rovsing's Sign"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Murphy's Sign is performed by palpating the right subcostal area while the patient takes a deep breath. As the descending diaphragm pushes the inflamed gallbladder against the examiner's fingers, the patient experiences sharp pain and catches their breath (inspiratory arrest). It has >95% sensitivity for Acute Cholecystitis. McBurney's sign (Option A) indicates appendicitis."
    },
    {
        "id": start_id + 27,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "Where is McBurney's point anatomically located on abdominal physical examination, and what condition does localized tenderness at this site suggest?",
        "options": [
            "Midpoint between the sternal notch and umbilicus; Peptic ulcer",
            "One-third of the distance along a line drawn from the Right Anterior Superior Iliac Spine (ASIS) to the umbilicus; Acute Appendicitis",
            "Two inches lateral to the left side of the umbilicus; Diverticulitis",
            "Right midclavicular line at the costal margin; Hepatitis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. McBurney's point lies one-third of the distance from the Right Anterior Superior Iliac Spine (ASIS) to the umbilicus. Maximum tenderness, guarding, and localized rigidity at McBurney's point indicates acute appendicitis. In TCM point location, this corresponds closely to Lanweixue (阑尾穴), located 2 cun distal to ST36 on the right lower leg."
    },
    {
        "id": start_id + 28,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "In a patient suspected of having acute appendicitis, deep palpation and pressure in the Left Lower Quadrant (LLQ) reproduces sharp pain in the Right Lower Quadrant (RLQ). What is the name of this referred physical sign?",
        "options": [
            "Psoas Sign",
            "Rovsing's Sign (罗夫辛征)",
            "Obturator Sign",
            "Blumberg's Sign"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Rovsing's sign is positive when deep pressure and palpation in the left lower quadrant (LLQ / descending colon) causes referred pain in the right lower quadrant (RLQ). Retrograde gas displacement towards the cecum stretches the inflamed appendix and overlying peritoneum, confirming acute appendicitis."
    },
    {
        "id": start_id + 29,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "During abdominal examination, the examiner presses deeply and slowly into the patient's abdomen, then abruptly and quickly withdraws the examining hand. The patient cries out in acute agonizing pain. What does this positive Rebound Tenderness (Blumberg's Sign) indicate?",
        "options": [
            "Mild functional irritable bowel syndrome",
            "Acute Peritoneal Inflammation / Peritonitis (腹膜炎)",
            "Chronic Spleen Qi deficiency",
            "Simple gastric hyperacidity"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Rebound tenderness (Blumberg's sign) occurs when rapid release of deep palpation produces greater pain than the initial compression. It is the hallmark physical examination sign of peritoneal irritation and peritonitis, signaling visceral rupture, perforation, or intra-abdominal abscess that warrants urgent surgical evaluation."
    },
    {
        "id": start_id + 30,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 58-year-old male presents with sudden left-sided facial weakness. On examination, he is unable to smile on the left side, but he CAN still wrinkle his forehead symmetrically and close both eyes tightly. What does this physical presentation differentiate?",
        "options": [
            "Peripheral facial nerve palsy (Bell's Palsy)",
            "Central Upper Motor Neuron (UMN) lesion (e.g., Acute Cerebral Stroke / CVA)",
            "Trigeminal neuralgia",
            "Myasthenia gravis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Because the upper facial motor nucleus in the pons receives bilateral cortical innervation, an Upper Motor Neuron (UMN) central stroke spares the forehead (the patient CAN still wrinkle their forehead and close both eyes tightly). In contrast, a Lower Motor Neuron (LMN) peripheral lesion (Bell's palsy) paralyzes the entire half of the face, including the forehead and orbicularis oculi."
    },
    {
        "id": start_id + 31,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "When stroking the lateral plantar surface of an adult patient's foot with a blunt instrument, the great toe extends (dorsiflexes) while the other four toes fan out. What is this sign, and what does it indicate?",
        "options": [
            "Normal plantar reflex in adults",
            "Positive Babinski Sign (巴宾斯基征) indicating Pyramidal Tract / Upper Motor Neuron lesion",
            "Sciatic nerve peripheral neuropathy",
            "Cerebellar vermis lesion"
        ],
        "answer": 1,
        "explanation": "Option B is correct. In adults and children over 2 years of age, normal plantar stimulation produces plantarflexion (curling down) of all toes. Great toe dorsiflexion with fanning of the outer digits is the positive Babinski sign, which is pathognomonic for damage to the corticospinal (pyramidal) tract / Upper Motor Neuron lesion."
    },
    {
        "id": start_id + 32,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 21-year-old college student presents with sudden high fever, excruciating headache, and photophobia. On physical examination, passive flexion of the patient's neck causes involuntary reflexive flexion of both knees and hips. What is this physical sign?",
        "options": [
            "Kernig's Sign",
            "Brudzinski's Neck Sign (布鲁津斯基征 / 脑膜刺激征)",
            "Chvostek's Sign",
            "Trousseau's Sign"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Brudzinski's neck sign is positive when passive flexion of the neck induces involuntary flexion of the hips and knees. Together with Kernig's sign (inability to extend knee when hip is flexed 90°) and nuchal rigidity, it forms the classic triad of Meningeal Irritation signs indicative of acute bacterial meningitis or subarachnoid hemorrhage."
    },
    {
        "id": start_id + 33,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with suspected retrocecal appendicitis lies on their left side. The examiner passively extends the patient's right hip backwards while stabilizing the pelvis. The patient experiences sharp abdominal pain in the RLQ. What is this test?",
        "options": [
            "Psoas Sign (腰大肌试验)",
            "Obturator Sign",
            "Murphy's Sign",
            "Carnett's Sign"
        ],
        "answer": 0,
        "explanation": "Option A is correct. The Psoas sign (Cope's psoas test) involves passive extension of the right thigh with the patient in left lateral recumbency. This stretches the iliopsoas muscle; if an inflamed appendix lies retrocecally in contact with the psoas fascia, severe RLQ pain is provoked. The Obturator sign (Option B) involves internal rotation of the flexed hip."
    },
    {
        "id": start_id + 34,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 30-year-old male develops sudden right-sided chest pain and shortness of breath following deep acupuncture needling at BL13. On physical examination, percussion over the right hemithorax yields a loud, drumming hyperresonant (tympanic) note, and breath sounds are absent. What is this clinical emergency?",
        "options": [
            "Lobar pneumonia",
            "Pneumothorax (气胸)",
            "Pleural effusion",
            "Atelectasis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Free air in the pleural space (pneumothorax) acts as an acoustic resonator, producing percussion hyperresonance (tympanitic sound) and absent or markedly diminished vesicular breath sounds on auscultation. Pleural effusion (Option C) and lobar pneumonia (Option A) produce a dull percussion note."
    },
    {
        "id": start_id + 35,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "During cardiac auscultation with the stethoscope diaphragm at the 2nd right intercostal space (aortic area), the examiner hears a harsh, crescendo-decrescendo systolic murmur that radiates bilaterally into the carotid arteries. What valvular lesion does this characterize?",
        "options": [
            "Mitral Regurgitation",
            "Aortic Stenosis (主动脉瓣狭窄)",
            "Aortic Regurgitation",
            "Tricuspid Stenosis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Aortic Stenosis produces a harsh midsystolic crescendo-decrescendo ejection murmur heard best at the right 2nd intercostal space, classically radiating upwards into the carotid arteries. Mitral regurgitation (Option A) produces a holosystolic blowing murmur heard loudest at the apex radiating to the left axilla."
    },
    {
        "id": start_id + 36,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "In a patient presenting with progressive painless jaundice, physical palpation reveals a non-tender, smooth, distended gallbladder. What classical diagnostic aphorism does this represent (Courvoisier's Sign)?",
        "options": [
            "The jaundice is caused by benign gallstones (choledocholithiasis)",
            "Painless palpable gallbladder with jaundice is strongly indicative of Malignant Biliary Obstruction (e.g., Pancreatic Head Carcinoma)",
            "Indicates acute calculous cholecystitis",
            "Indicates hemolytic transfusion reaction"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Courvoisier's Law states that in the presence of painless jaundice, a palpably enlarged gallbladder is unlikely to be caused by gallstones (because chronic gallstone disease fibroses the gallbladder wall, preventing dilation). Instead, it strongly points to a malignant neoplasm of the pancreatic head, ampulla of Vater, or common bile duct obstructing flow."
    },
    {
        "id": start_id + 37,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Easy",
        "exam": "Pan-Canadian Board Exam",
        "question": "When testing a patient's deep tendon reflexes, the patellar reflex produces a normal brisk contraction of the quadriceps with visible forward kick of the lower leg. How is this normal physiological reflex graded?",
        "options": [
            "0 (Absent)",
            "1+ (Diminished)",
            "2+ (Normal / Average)",
            "4+ (Hyperactive with clonus)"
        ],
        "answer": 2,
        "explanation": "Option C is correct. Deep tendon reflexes are graded on a 0 to 4+ scale: 0 = absent; 1+ = hypoactive / diminished; 2+ = normal physiological response; 3+ = hyperactive without clonus; 4+ = hyperactive with sustained clonus (indicative of upper motor neuron pathology)."
    },
    {
        "id": start_id + 38,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "During a neurological cranial nerve examination, light shone into the patient's right pupil causes normal constriction of the right pupil (direct light reflex), but the left pupil remains dilated and fixed. When light is shone into the left pupil, the right pupil constricts normally, but the left pupil still does not react. Which cranial nerve is impaired?",
        "options": [
            "Right Optic Nerve (CN II)",
            "Left Oculomotor Nerve (CN III / 动眼神经传出支损伤)",
            "Left Trochlear Nerve (CN IV)",
            "Bilateral Abducens Nerve (CN VI)"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The pupillary light reflex requires the afferent limb (Optic Nerve CN II) to sense light and the efferent limb (Oculomotor Nerve CN III parasympathetic fibers) to constrict the pupil (sphincter pupillae). Because shining light in either eye causes the right eye to constrict, sensory afferents are intact bilaterally; the left pupil's inability to constrict under any circumstance confirms an efferent Left CN III lesion."
    },
    {
        "id": start_id + 39,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient stands with feet placed together and arms at their side. They remain stable with eyes open, but when they close their eyes, they immediately sway violently and lose their balance. What is this sign (Romberg Test), and what system does it assess?",
        "options": [
            "Positive Romberg Sign indicating loss of Dorsal Column Proprioception (Sensory Ataxia)",
            "Cerebellar Ataxia",
            "Vestibular schwannoma only",
            "Malingering"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Balance relies on three sensory inputs: vision, proprioception (dorsal column/medial lemniscus), and vestibular apparatus. A patient with impaired proprioception compensates using vision; closing the eyes removes visual compensation, causing instability and swaying (Positive Romberg sign / Sensory Ataxia). Cerebellar ataxia causes instability even with eyes open."
    },
    {
        "id": start_id + 40,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 58-year-old male with a 40-pack-year smoking history presents with chronic cough. Examination of the hands shows bulbous enlargement of the distal fingertips, sponginess of the nail bed, and a Lovibond angle between the nail plate and proximal nail fold > 180°. What is this physical sign called?",
        "options": [
            "Koilonychia (Spoon nails)",
            "Digital Clubbing (杵状指)",
            "Beau's lines",
            "Splinter hemorrhages"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Digital clubbing (Hippocratic fingers / 杵状指) is characterized by proliferation of subungual connective tissue, leading to an increased Lovibond profile angle (> 180°) and loss of Schamroth's window. It is strongly linked to chronic intrathoracic hypoxia, bronchogenic carcinoma, bronchiectasis, idiopathic pulmonary fibrosis, and infective endocarditis."
    },
    {
        "id": start_id + 41,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "On examination of the neck, a hard, painless, fixed lymph node is palpated in the Left Supraclavicular Fossa (Virchow's Node / 魏尔啸淋巴结). What is the primary clinical significance of this finding?",
        "options": [
            "Benign bacterial pharyngitis",
            "Metastatic abdominal malignancy (e.g., Gastric Carcinoma / 'Troisier's sign')",
            "Local cervical muscle spasm",
            "Allergic rhinitis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Virchow's node (Troisier's sign) is an enlargement of the left supraclavicular lymph node, which receives lymphatic drainage from the thoracic duct carrying lymph from the abdomen and pelvis. A hard, non-tender, fixed left supraclavicular node is a classic red flag for metastatic gastrointestinal malignancy, particularly gastric adenocarcinoma."
    },
    {
        "id": start_id + 42,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with suspected deep vein thrombosis (DVT) is examined. Which physical sign or test involves forceful passive dorsiflexion of the patient's foot with knee extended to elicit calf pain, although it is no longer recommended due to risk of dislodging a clot?",
        "options": [
            "Homans' Sign (霍曼斯征)",
            "Lasegue's Sign",
            "Babinski Sign",
            "Trousseau's Sign"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Homans' sign is positive when passive ankle dorsiflexion elicits calf pain, classically attributed to deep vein thrombosis (DVT). However, modern medical standards avoid this test and forbid calf massage because forceful manipulation can dislodge a thrombus into the inferior vena cava, causing a fatal Pulmonary Embolism (PE). Immediate duplex venous ultrasound is indicated."
    },
    {
        "id": start_id + 43,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "An infant is brought to the clinic with high fever, barking seal-like cough, and an alarming high-pitched harsh sound heard during inspiration without a stethoscope. What is this respiratory sound called, and what does it indicate?",
        "options": [
            "Expiratory wheezing from asthma",
            "Inspiratory Stridor (喉鸣) indicating Upper Airway Obstruction / Laryngeal Edema (Medical Emergency)",
            "Vesicular breath sounds",
            "Pleural friction rub"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Stridor is a harsh, high-pitched, predominantly inspiratory sound generated by turbulent airflow through a narrowed extrathoracic upper airway (larynx, trachea). In pediatrics, stridor with barking cough indicates acute laryngotracheobronchitis (Croup) or life-threatening Epiglottitis, representing a red flag medical emergency for airway compromise."
    },
    {
        "id": start_id + 44,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient presents with extreme weakness. On physical examination, the examiner lightly taps over the facial nerve just anterior to the external ear canal, causing an involuntary spasm/twitch of the ipsilateral facial and lip muscles (Chvostek's Sign). What metabolic abnormality does this indicate?",
        "options": [
            "Severe Hypocalcemia (低钙血症) or Hypomagnesemia",
            "Severe Hyperkalemia",
            "Metabolic Acidosis",
            "Hypernatremia"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Chvostek's sign is an abnormal reaction to mechanical stimulation of the facial nerve (CN VII) resulting in twitching of facial muscles. It indicates neuromuscular hyperexcitability (tetany) secondary to acute Hypocalcemia (ionized calcium < 1.1 mmol/L) or hypomagnesemia, frequently occurring after thyroid/parathyroid surgery."
    },
    {
        "id": start_id + 45,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 64-year-old male with acute severe chest pain radiating to the interscapular region of the back has a blood pressure of 180/100 mmHg in the right arm, but 120/70 mmHg in the left arm (a difference > 20 mmHg systolic), accompanied by asymmetric radial pulses. What life-threatening catastrophe must be immediately ruled out?",
        "options": [
            "Acute Aortic Dissection (主动脉夹层破裂)",
            "Benign musculoskeletal thoracic back sprain",
            "Pericarditis",
            "Costochondritis"
        ],
        "answer": 0,
        "explanation": "Option A is correct. A marked difference in blood pressure between arms (> 20 mmHg systolic) paired with pulse asymmetry and tearing/ripping retrosternal chest pain radiating to the interscapular back is the classical presentation of Acute Aortic Dissection. Dissection of the aortic arch compromises the origin of the left subclavian or brachiocephalic arteries. Immediate 911 transfer is vital."
    },
    {
        "id": start_id + 46,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "During lung examination, the examiner places the stethoscope over the right lower lung lobe and asks the patient to say 'E-E-E'. Through the stethoscope, the sound is heard clearly as a nasal 'A-A-A'. What is this sign (Egophony), and what does it indicate?",
        "options": [
            "Lobar Lung Consolidation (e.g., Bacterial Lobar Pneumonia / 肺实变)",
            "Normal healthy lung parenchyma",
            "Pneumothorax",
            "Pulmonary emphysema"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Egophony (the 'E-to-A' sign) occurs when sound transmission is enhanced through dense, solidified, airless lung tissue rather than normal spongy alveolar tissue. High-frequency components pass readily through consolidated tissue, converting the spoken vowel 'E' into a nasal-sounding 'A'. It is diagnostic of lobar pneumonia consolidation."
    },
    {
        "id": start_id + 47,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "During vital sign evaluation, a patient's radial pulse rate is counted at 68 beats per minute, while simultaneous cardiac apical auscultation reveals a heart rate of 96 beats per minute. What is this clinical discrepancy called (Pulse Deficit / 脉搏短绌)?",
        "options": [
            "Normal physiological sinus arrhythmia",
            "Pulse Deficit, characteristically diagnostic of Atrial Fibrillation (房颤)",
            "Third-degree complete heart block",
            "Water-hammer pulse"
        ],
        "answer": 1,
        "explanation": "Option B is correct. A Pulse Deficit exists when the apical heart rate exceeds the peripheral radial pulse rate. It occurs because rapid, erratic, disorganized contractions in Atrial Fibrillation (AFib) fail to produce sufficient ventricular stroke volume to generate a palpable peripheral arterial pulse wave. In TCM, this corresponds to an irregular Arrhythmic Knotted or Abrupt pulse."
    },
    {
        "id": start_id + 48,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 35-year-old female presents with severe generalized joint aching and fatigue. When her blood pressure cuff is inflated above systolic pressure for 3 minutes, her hand involuntarily undergoes carpopedal spasm (flexion of wrist and MCP joints, extension of IP joints, adduction of thumb - 'obstetrician hand'). What is this sign?",
        "options": [
            "Trousseau's Sign of Latent Tetany (特鲁索征 / 低钙血症)",
            "Chvostek's Sign",
            "Phalen's Sign",
            "Kernig's Sign"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Trousseau's sign of latent tetany is elicited by occluding the brachial artery with a blood pressure cuff inflated 20 mmHg above systolic pressure for 3 minutes. The resulting ischemia triggers hyperexcitability of peripheral nerves, producing painful carpopedal spasm ('main d'accoucheur'). It is more sensitive and specific for Hypocalcemia than Chvostek's sign."
    },
    {
        "id": start_id + 49,
        "category": "Biomedical Physical Exam & Clinical Signs",
        "difficulty": "Easy",
        "exam": "Pan-Canadian Board Exam",
        "question": "What is the normal physiological respiratory rate (RR) for a healthy resting adult at room temperature?",
        "options": [
            "6 to 10 breaths per minute",
            "12 to 20 breaths per minute",
            "24 to 32 breaths per minute",
            "35 to 45 breaths per minute"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The standard normal adult respiratory rate is 12 to 20 breaths per minute at rest. A respiratory rate greater than 20–24 bpm is termed tachypnea, commonly seen in fever, acidosis, hypoxemia, or anxiety. A rate less than 10–12 bpm is bradypnea, signaling central nervous system depression or opioid intoxication."
    },

    # -------------------------------------------------------------------------
    # PART 3: TRAUMATOLOGY & ORTHOPEDIC PHYSICAL EXAM (25 QUESTIONS)
    # -------------------------------------------------------------------------
    {
        "id": start_id + 50,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 46-year-old carpenter presents with shooting neck and right arm pain. While the patient is seated, the examiner extends and laterally rotates the patient's cervical spine towards the right, then applies axial downward compression on the head, reproducing sharp shooting pain into the right thumb and index finger. What test is this?",
        "options": [
            "Spurling's Test (Neck Compression Test / 压颈试验)",
            "Lhermitte's Sign",
            "Adson's Test",
            "Wright's Hyperabduction Test"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Spurling's test (cervical foraminal compression) narrows the intervertebral neural foramina. Reproduction of shooting pain or paresthesias radiating into a specific dermatome confirms cervical nerve root impingement (cervical radiculopathy). Pain radiating to the thumb and index finger corresponds to the C6 nerve root."
    },
    {
        "id": start_id + 51,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 55-year-old accountant complains of progressive neck stiffness, severe clumsy fingers (inability to button shirts or hold chopsticks), and an unsteady spastic gait described as 'walking on soft cotton'. Neurological exam reveals hyperreflexia and positive Hoffman's sign. Which subtype of Cervical Spondylosis is this?",
        "options": [
            "Neck type (颈型颈椎病)",
            "Radicular type (神经根型)",
            "Spinal Cord / Myelopathy type (脊髓型颈椎病)",
            "Vertebral Artery type (椎动脉型)"
        ],
        "answer": 2,
        "explanation": "Option C is correct. Cervical Spondylotic Myelopathy (Spinal Cord Type / 脊髓型) occurs when central spinal canal stenosis compresses the cervical spinal cord. Hallmarks include upper extremity fine motor clumsiness (buttoning, writing), spastic lower extremity gait ('walking on cotton'), hyperreflexia, and upper motor neuron signs (Hoffman, Babinski). Chiropractic thrusts and violent cervical manipulation are strictly contraindicated."
    },
    {
        "id": start_id + 52,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 62-year-old female presents with sudden episodic rotational vertigo, tinnitus, and nausea that occurs exclusively when she turns her head quickly to the left or extends her neck backwards. She experienced a sudden 'drop attack' (falling without losing consciousness) when looking up. Which Cervical Spondylosis subtype does this characterize?",
        "options": [
            "Sympathetic type",
            "Vertebral Artery type (椎动脉型颈椎病 / VBI)",
            "Spinal cord type",
            "Neck muscular type"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Vertebral Artery Type cervical spondylosis is caused by osteophytic compression of the vertebral artery in the transverse foramina during neck rotation or hyperextension, compromising posterior cerebral circulation (Vertebrobasilar Insufficiency / VBI). Classic hallmarks are rotational dizziness, nystagmus, drop attacks, and visual blurring triggered by head turning. Cervical rotatory thrusts are forbidden."
    },
    {
        "id": start_id + 53,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A tennis player complains of persistent pain on the lateral aspect of the right elbow that worsens when shaking hands or lifting a coffee cup. Physical examination reveals exquisite tenderness over the lateral epicondyle, and severe pain is provoked when the patient extends and radially deviates the wrist against resistance (Cozen's Test). What is the pathology?",
        "options": [
            "Medial epicondylitis (Golfer's Elbow)",
            "Lateral Epicondylitis (Tennis Elbow / 肱骨外上髁炎 / 网球肘)",
            "Olecranon bursitis",
            "Radial head fracture"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Lateral epicondylitis (Tennis Elbow) involves repetitive micro-trauma and angiofibroblastic degeneration of the Extensor Carpi Radialis Brevis (ECRB) tendon at its origin on the lateral humeral epicondyle. Cozen's test (resisted wrist extension) and Mill's test (passive wrist flexion with extended elbow) are the classic provocative tests. TCM points: LI11, LI10, LI12, Ashi."
    },
    {
        "id": start_id + 54,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 34-year-old postpartum mother presents with severe pain over the radial side of her right wrist that worsens when lifting her baby. Examination reveals tenderness over the radial styloid process. When she tucks her thumb into her palm, makes a fist, and the examiner passively ulnar-deviates her wrist (Finkelstein's Test), she cries out in excruciating pain. What is the diagnosis?",
        "options": [
            "Carpal Tunnel Syndrome",
            "De Quervain's Tenosynovitis (桡骨茎突狭窄性腱鞘炎)",
            "Scaphoid bone fracture",
            "Ganglion cyst of wrist"
        ],
        "answer": 1,
        "explanation": "Option B is correct. De Quervain's tenosynovitis is stenosing tenosynovitis of the first dorsal extensor compartment of the wrist, housing the Abductor Pollicis Longus (APL) and Extensor Pollicis Brevis (EPB) tendons. Finkelstein's test is pathognomonic. In acupuncture, this involves the Hand Taiyin (LU7) and Yangming (LI5) channels."
    },
    {
        "id": start_id + 55,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A dental hygienist presents with nocturnal numbness and burning tingling in the thumb, index, and middle fingers of her right hand that wakes her from sleep. She finds relief by shaking her hand ('flick sign'). Symptoms are reproduced when she holds the dorsal surfaces of her flexed wrists together at 90° for 60 seconds (Phalen's Test). What nerve is compressed?",
        "options": [
            "Ulnar Nerve in the Guyon canal",
            "Median Nerve in the Carpal Tunnel (腕管综合征)",
            "Radial Nerve in the spiral groove",
            "Musculocutaneous Nerve"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Carpal Tunnel Syndrome results from compression of the Median Nerve beneath the transverse carpal ligament at the volar wrist. It selectively affects the sensory territory of the median nerve (palmar surface of digits 1, 2, 3, and radial half of 4). Phalen's test and Tinel's sign over the volar carpal tunnel (near PC7) are the primary diagnostic physical exams."
    },
    {
        "id": start_id + 56,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "During a shoulder examination, the patient's arm is placed at 90° abduction and 30° horizontal forward flexion in the scapular plane with the thumb pointing downward toward the floor. The patient is unable to resist downward pressure applied by the examiner due to severe pain and weakness (Empty Can / Jobe's Test). Which rotator cuff muscle/tendon is isolated and injured?",
        "options": [
            "Subscapularis muscle",
            "Supraspinatus muscle and tendon (冈上肌)",
            "Infraspinatus muscle",
            "Teres minor muscle"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The Empty Can test (Jobe's test) isolates the supraspinatus tendon by placing it in line with the scapular plane with internal rotation. Pain or weakness indicates supraspinatus tendinopathy, impingement, or a partial/full-thickness rotator cuff tear. TCM point correlation: SI12 (Bingfeng), LI15 (Jianyu), TE14 (Jianliao)."
    },
    {
        "id": start_id + 57,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 50-year-old diabetic female presents with global right shoulder stiffness. She cannot reach behind her head to comb her hair, nor can she reach behind her lumbar back to fasten her bra (Apley's Scratch Test is markedly restricted in all planes). Passive and active external rotation and abduction are equally restricted. What is the diagnosis?",
        "options": [
            "Acromioclavicular joint separation",
            "Adhesive Capsulitis (Frozen Shoulder / 漏肩风 / 五十肩)",
            "Cervical radiculopathy",
            "Biceps long head subluxation"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Adhesive Capsulitis (Frozen Shoulder) is characterized by insidious painful restriction of BOTH active and passive glenohumeral motion in a capsular pattern (external rotation most limited, followed by abduction, then internal rotation). It is particularly prevalent in diabetics. TCM distal empirical point: ST38 (Tiaokou) needled through to BL57 with active arm movement."
    },
    {
        "id": start_id + 58,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 38-year-old male presents with sharp lower back pain radiating down the posterior right thigh and lateral calf into the great toe after lifting a heavy generator. Straight Leg Raise (SLR / Lasegue's) on the right produces shooting pain at 40°. Which test differentiates true neural root impingement from tight hamstring muscles?",
        "options": [
            "Bragard's Sign (dorsiflexing the ankle with the leg lowered 5° below painful SLR angle)",
            "Thomas Test",
            "Trendelenburg Test",
            "McMurray's Test"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Bragard's sign is performed by lowering the raised leg just below the angle where SLR pain occurred, then passively dorsiflexing the patient's foot. Because dorsiflexion places traction on the sciatic/tibial nerve without stretching the hamstring muscles, reproduction of radicular shooting pain confirms true neural root tension (lumbar disc herniation)."
    },
    {
        "id": start_id + 59,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "During a Straight Leg Raise test on a patient with left lower back pain and left sciatica, the examiner raises the ASYMPTOMATIC RIGHT (healthy) straight leg. The patient suddenly cries out because shooting radicular pain is triggered down the SYMPTOMATIC LEFT leg. What is this sign (Crossed SLR / Well-Leg Raise), and what does it indicate?",
        "options": [
            "Malingering or psychogenic pain",
            "Highly specific (>90%) for a large central or paracentral lumbar disc herniation",
            "Tight contralateral piriformis muscle",
            "Sacroiliac sprain"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The Crossed Straight Leg Raise (Well-Leg Raising Test / Fajersztajn's sign) occurs when lifting the unaffected leg provokes radicular pain in the contralateral affected leg. It pulls the dural sac downward and stretches the contralateral root over the disc fragment; it has exceptionally high specificity (>90%) for large central, extruded, or sequestered lumbar disc herniation."
    },
    {
        "id": start_id + 60,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 45-year-old male with severe L4–L5 disc herniation is examined. Neurological motor testing reveals weakness of ankle dorsiflexion and difficulty walking on his heels (Foot Drop). Sensory testing reveals numbness over the dorsum of the foot and great toe web space. Deep tendon reflexes are normal. Which specific nerve root is compressed?",
        "options": [
            "L3 nerve root",
            "L4 nerve root",
            "L5 nerve root (L5神经根受压)",
            "S1 nerve root"
        ],
        "answer": 2,
        "explanation": "Option C is correct. The L5 nerve root innervates the Extensor Hallucis Longus and Tibialis Anterior/Extensor Digitorum, causing weakness of great toe extension and ankle dorsiflexion (difficulty heel-walking). Sensory distribution covers the anterolateral lower leg, dorsum of foot, and 1st web space. Because L5 has no prominent deep tendon reflex, patellar (L4) and Achilles (S1) reflexes remain normal."
    },
    {
        "id": start_id + 61,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient with acute lumbosacral disc herniation presents with bilateral sciatica, saddle anesthesia (loss of sensation in the buttocks, perineum, and inner thighs), and sudden urinary retention with overflow incontinence. What is this critical condition?",
        "options": [
            "Piriformis syndrome",
            "Cauda Equina Syndrome (马尾综合征 / 需急诊减压手术)",
            "Uncomplicated lumbago",
            "Meralgia paresthetica"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Cauda Equina Syndrome is an absolute orthopedic and neurosurgical emergency caused by massive central disc herniation or canal-occupying mass compressing the lumbosacral nerve roots. Hallmarks are: 1) Saddle anesthesia; 2) Bladder/bowel dysfunction (urinary retention or fecal incontinence); 3) Progressive motor weakness in both legs. Surgical decompression within 24–48 hours is mandatory to prevent permanent paralysis."
    },
    {
        "id": start_id + 62,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A long-distance truck driver complains of deep, burning right buttock pain that radiates down the posterior thigh, but DOES NOT have lumbar spinal pain or tenderness. The pain is reproduced when his hip is flexed to 60° and adducted with internal rotation (FAIR Test / Piriformis Test). What is the diagnosis?",
        "options": [
            "Piriformis Syndrome (梨状肌综合征)",
            "L4–L5 Lumbar Disc Herniation",
            "Trochanteric bursitis",
            "Femoral neck fracture"
        ],
        "answer": 0,
        "explanation": "Option A is correct. Piriformis syndrome is an extra-spinal entrapment neuropathy where hypertrophy, spasm, or trauma of the piriformis muscle compresses the underlying sciatic nerve in the greater sciatic notch. The FAIR test (Flexion, Adduction, Internal Rotation) stretches the piriformis across the nerve, reproducing buttock pain and sciatica without spinal signs. Primary point: GB30 (Huantiao)."
    },
    {
        "id": start_id + 63,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "In performing Patrick's (FABER) test, the patient's hip is placed in Flexion, Abduction, and External Rotation (foot resting on contralateral knee). Downward pressure on the flexed knee produces pain in the anterior groin. What does anterior groin pain specifically indicate?",
        "options": [
            "Sacroiliac joint dysfunction",
            "Intra-articular Hip Joint Pathology (e.g., Hip Osteoarthritis / 髋关节病变)",
            "Hamstring muscle tear",
            "Piriformis syndrome"
        ],
        "answer": 1,
        "explanation": "Option B is correct. In the FABER (Patrick's) test, anterior groin pain indicates pathology within the hip joint itself (osteoarthritis, femoral acetabular impingement, labral tear, avascular necrosis). In contrast, posterior pelvic or buttock pain on the same maneuver points to Sacroiliac (SI) joint pathology (sacroiliitis or SI ligament strain)."
    },
    {
        "id": start_id + 64,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient stands on one leg (the right leg) for 30 seconds. The examiner observes that the pelvis on the opposite, unsupported left side drops downwards instead of staying level. What is this sign (Trendelenburg Test), and what muscle weakness does it demonstrate?",
        "options": [
            "Weakness of the left quadriceps muscle",
            "Weakness of the Gluteus Medius on the stance (right) leg, innervated by the Superior Gluteal Nerve (L5)",
            "Weakness of the right gastrocnemius muscle",
            "Hamstring avulsion"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The Trendelenburg test evaluates the hip abductors, primarily the Gluteus Medius on the weight-bearing (stance) side. When the stance gluteus medius is weak or paralyzed (superior gluteal nerve or L5 radiculopathy), it fails to stabilize the pelvis, causing the pelvis on the opposite non-weight-bearing side to sag downwards. Acupuncture point: GB29 (Juliao) and GB30 (Huantiao)."
    },
    {
        "id": start_id + 65,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A soccer player sustains a non-contact pivoting knee injury accompanied by an audible 'pop', immediate joint effusion (hemarthrosis within 2 hours), and inability to bear weight. Which physical examination test at 20°–30° knee flexion is the GOLD STANDARD clinical test for confirming an Anterior Cruciate Ligament (ACL) tear?",
        "options": [
            "McMurray's Test",
            "Lachman's Test (拉赫曼试验 / 诊断前交叉韧带断裂金标准)",
            "Apley's Distraction Test",
            "Clark's Patellar Sign"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Lachman's test (performed at 20°–30° flexion with anterior translation of the tibia) is the gold standard clinical examination for Anterior Cruciate Ligament (ACL / 前交叉韧带) tears, boasting superior sensitivity (~85–95%) compared to the 90° anterior drawer test. A soft, mushy end-feel and excessive forward translation confirm rupture."
    },
    {
        "id": start_id + 66,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 28-year-old basketball player complains of medial knee joint line pain and knee 'locking' when crouching. During examination, the knee is fully flexed, the foot is externally rotated, and valgus stress is applied as the knee is extended. The examiner feels a palpable pop and joint line tenderness. What test is this?",
        "options": [
            "Lachman's Test",
            "McMurray's Test for Medial Meniscus Tear (麦克马瑞试验 / 半月板撕裂)",
            "Thompson's Test",
            "Finkelstein's Test"
        ],
        "answer": 1,
        "explanation": "Option B is correct. McMurray's test evaluates the menisci. External rotation of the tibia combined with valgus stress during knee extension compresses the posterior horn of the Medial Meniscus, producing a palpable or audible click/thud and joint line pain. Internal rotation with varus stress tests the Lateral Meniscus."
    },
    {
        "id": start_id + 67,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A patient is prone with knee flexed at 90°. The examiner applies downward axial compression to the heel while rotating the tibia, producing severe pain. When the examiner stabilizes the thigh and applies upward distraction with rotation, NO pain is produced. What does this Apley's Compression Test specifically indicate?",
        "options": [
            "Collateral ligament sprain",
            "Meniscus Injury / Tear (半月板损伤)",
            "Patellar tendinitis",
            "Popliteal Baker's cyst"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Apley's maneuver differentiates meniscal injuries from collateral ligament tears. Downward axial compression pinches the meniscus between the femoral condyle and tibial plateau; pain with compression indicates a Meniscus Tear. In contrast, distraction relieves meniscal pressure while stretching collateral ligaments; pain with distraction indicates ligament sprain."
    },
    {
        "id": start_id + 68,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A runner complains of deep, diffuse aching behind her kneecap that worsens when walking down stairs or sitting for long periods in a movie theater ('movie-goer sign'). The examiner applies downward pressure on the superior pole of the patella while the patient contracts her quadriceps, eliciting sharp retropatellar crepitus and pain (Clark's Sign). What is the diagnosis?",
        "options": [
            "Patellar tendon rupture",
            "Patellofemoral Pain Syndrome / Chondromalacia Patellae (髌骨软化症)",
            "Anterior cruciate ligament tear",
            "Medial collateral ligament tear"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Clark's test (Patellar Grind Test) compresses the patellar articular cartilage against the femoral trochlea during active quadriceps contraction. Pain, grinding, and inability to maintain contraction confirms Chondromalacia Patellae / Patellofemoral Pain Syndrome (PFPS). Primary acupuncture points: Heding, ST35 (Dubi), Neixiyan, SP10 (Xuehai), ST34 (Liangqiu)."
    },
    {
        "id": start_id + 69,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A 42-year-old weekend warrior playing squash felt a sudden, violent sensation 'like being kicked in the back of the ankle', followed by immediate inability to push off on his right foot. While the patient is prone with feet over the edge of the examination table, the examiner squeezes the right calf muscle; the foot DOES NOT plantarflex (Thompson's Test Positive). What is the diagnosis?",
        "options": [
            "Ankle inversion sprain",
            "Complete Rupture of the Achilles Tendon (跟腱完全断裂 / 需急诊骨科转诊)",
            "Gastrocnemius minor muscle strain",
            "Plantar fasciitis"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The Thompson (Simmonds) test is the definitive clinical test for complete Achilles Tendon Rupture. Squeezing the calf compresses the gastrocnemius/soleus complex; if the tendon is intact, the foot involuntarily plantarflexes. Absence of foot movement indicates complete discontinuity of the tendon. This is an urgent orthopedic surgical referral; acupuncture needling must not delay repair."
    },
    {
        "id": start_id + 70,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "What is the single most common mechanism of injury in acute ankle sprains, and which ligament is most frequently torn?",
        "options": [
            "Eversion mechanism; Deltoid ligament",
            "Inversion and plantarflexion mechanism; Anterior Talofibular Ligament (ATFL / 距腓前韧带)",
            "Dorsiflexion mechanism; Calcaneofibular ligament",
            "External rotation; Syndesmotic ligament"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Over 85% of ankle sprains occur via an Inversion and Plantarflexion mechanism. The Anterior Talofibular Ligament (ATFL) is the weakest lateral ligament and the first to tear, followed by the Calcaneofibular Ligament (CFL). TCM channels: Foot Shaoyang (GB40 Qiuxu) and Foot Taiyang (BL60, BL62)."
    },
    {
        "id": start_id + 71,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "Which of the following physical examination signs is classified as a PATHOGNOMONIC definitive sign of a bone fracture rather than a simple contusion or soft-tissue sprain?",
        "options": [
            "Localized swelling and ecchymosis",
            "Severe localized tenderness to light palpation",
            "Bone crepitus (骨擦音), abnormal mobility, and gross visible deformity (畸形与异常活动)",
            "Mild antalgic gait"
        ],
        "answer": 2,
        "explanation": "Option C is correct. In traumatology and orthopedics, general signs of injury (swelling, pain, ecchymosis, functional impairment) can occur in simple sprains. The three UNIQUE, pathognomonic clinical signs of a Bone Fracture are: 1) Gross anatomical deformity (e.g., silver-fork deformity in Colles fracture); 2) Abnormal mobility in a non-joint segment; and 3) Palpable or audible bone crepitus (bone fragments rubbing together)."
    },
    {
        "id": start_id + 72,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "Following a tibia fracture reduction and cast placement, a 26-year-old male develops deep, unyielding, disproportionate calf pain that is NOT relieved by opioid analgesics. Passive stretching of the toes provokes excruciating pain, and the calf compartment feels tense and 'woody'. What life-threatening orthopedic emergency is this?",
        "options": [
            "Normal post-reduction fracture ache",
            "Acute Compartment Syndrome (骨筋膜室综合征 / 需急诊行筋膜切开减压术)",
            "Cellulitis",
            "Complex Regional Pain Syndrome Type I"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Acute Compartment Syndrome occurs when interstitial tissue pressure within an enclosed osteofascial compartment exceeds capillary perfusion pressure, causing muscle and nerve ischemia. The '6 Ps' are: Pain out of proportion, Pain on passive stretch (earliest/most sensitive sign), Paresthesia, Pallor, Poikilothermia, and Pulselessness (late). Immediate emergency surgical fasciotomy is required to prevent amputation."
    },
    {
        "id": start_id + 73,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Medium",
        "exam": "Pan-Canadian Board Exam",
        "question": "A middle-aged runner complains of intense, stabbing heel pain during the first few steps out of bed in the morning that gradually improves after walking for 15 minutes, but worsens after prolonged standing. Physical exam reveals exquisite tenderness over the medial tubercle of the calcaneus. What is the diagnosis?",
        "options": [
            "Achilles tendinitis",
            "Plantar Fasciitis (跖筋膜炎 / 跟痛症)",
            "Calcaneal stress fracture",
            "Tarsal tunnel syndrome"
        ],
        "answer": 1,
        "explanation": "Option B is correct. Plantar Fasciitis (Calcaneodynia / 跟痛症) is characterized by severe start-up pain upon initial weight-bearing in the morning (as the contracted plantar aponeurosis is acutely stretched), with pinpoint tenderness over the anteromedial calcaneus. TCM points: Shimian (EX-LE / 失眠穴 at center of heel), KD3 (Taixi), BL60 (Kunlun), Ashi with moxibustion."
    },
    {
        "id": start_id + 74,
        "category": "Traumatology & Orthopedic Physical Exam",
        "difficulty": "Hard",
        "exam": "Pan-Canadian Board Exam",
        "question": "A high school student is screened for scoliosis. The examiner has the patient bend forward at the waist with knees straight and arms hanging loose towards the floor (Adams Forward Bend Test). The examiner observes a unilateral thoracic rib hump and paraspinal asymmetry that DOES NOT flatten out. What does this confirm?",
        "options": [
            "Postural / Functional scoliosis due to muscle imbalance",
            "Structural Scoliosis (结构性脊柱侧凸) with fixed vertebral body rotation",
            "Ankylosing spondylitis",
            "Lumbar facet joint sprain"
        ],
        "answer": 1,
        "explanation": "Option B is correct. The Adams Forward Bend Test differentiates structural from functional scoliosis. When bending forward, functional (postural or antalgic) curves straighten out and disappear. In contrast, Structural Scoliosis involves fixed vertebral rotation; the rotating vertebral bodies push the ribs upward on the convexity, creating an unmistakable, permanent unilateral rib hump."
    }
]

print(f"Generated {len(NEW_QUESTIONS)} new board exam questions.")

# Append to existing
combined = existing_questions + NEW_QUESTIONS

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {DATA_FILE}!")
print(f"Total questions in exam bank now: {len(combined)}")

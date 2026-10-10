"""Safety and Ethics Flashcards (35 high-yield clinical safety & jurisprudence cards).

Covers Clean Needle Technique (CNT), Pneumothorax prevention & signs,
visceral & CNS hazards (DU15/16), ophthalmic safety (BL1), arterial precautions,
management of complications (fainting, stuck, bent, broken needles), moxa burns,
pregnancy contraindications, informed consent, confidentiality (PIPEDA),
professional boundaries, and medical record retention laws.
All points strictly use bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS = [
    {
        "category": "Safety and Ethics",
        "title": "Clean Needle Technique (CNT): Core Standards",
        "front": "List the foundational principles of Clean Needle Technique (CNT) that must be maintained in every clinical acupuncture encounter.",
        "back": "Clean Needle Technique (CNT) Core Principles:\n1. Hand Hygiene: Thorough handwashing with liquid soap and running water for at least 20 seconds, or alcohol-based hand rub (>60% alcohol), immediately before touching clean equipment or needling, and immediately after treatment.\n2. Single-Use Disposable Needles: Use ONLY sterile, pre-packaged, single-use filiform needles. Never reuse or re-sterilize needles. Inspect package integrity and expiry date.\n3. Skin Preparation: Clean patient's skin at needle sites using a fresh 70% isopropyl alcohol swab; wipe in firm circular motions outward or single downward sweep, and ALLOW TO AIR DRY COMPLETELY before puncturing.\n4. Clean Field Establishment: Maintain an uncontaminated clean field (e.g., sterile tray, clean paper barrier). Clean items never touch uncleaned surfaces.\n5. Sharps Disposal: Immediately discard used needles and guide tubes into an approved, rigid, puncture-resistant biohazard sharps container located within arm's reach of the treatment table.",
        "consensus": "Universal mandatory legal standard for acupuncture licensure across North America (CTCMA, NCCAOM).",
        "variations": "Never palpate the cleaned point again with an uncleaned finger; if palpation is necessary, palpate through sterile cotton or re-clean the site.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM Clean Needle Technique Manual 7th Ed."])
    },
    {
        "category": "Safety and Ethics",
        "title": "Pneumothorax: High-Risk Points & Safe Angles",
        "front": "Which acupoints carry the highest risk of causing Traumatic Pneumothorax, and what are the strict needling depth and angle rules for the thorax?",
        "back": "High-Risk Acupoints for Pneumothorax:\n• Infraclavicular & Apical: LU1 (Zhongfu / 中府), LU2 (Yunmen / 云门), ST12 (Quepen / 缺盆).\n• Shoulder Trapezius: GB21 (Jianjing / 肩井).\n• Paraspinal Upper Thoracic: BL11 (Dazhu / 大杼) through BL21 (Weishu / 胃俞).\n• Posterior Upper Back & Scapula: SI14 (Jianwaishu / 肩外俞), SI15 (Jianzhongshu / 肩中俞), BL41 through BL50.\n• Lateral Chest / Ribs: SP17 (Shidou / 食窦), SP18 (Tianxi / 天溪), GB24 (Riyue / 日月), LV14 (Qimen / 期门).\n\n⚠️ Strict Safe Needling Rules:\n1. NEVER insert needles PERPENDICULARLY into the thoracic wall, intercostal spaces, lung apex (ST12), or trapezius apex (GB21).\n2. Puncture OBLIQUELY or TRANSVERSELY along the contour of the ribs, or medially towards the spine for Back-Shu points (BL11–BL21) at an angle of 30° to 45°.\n3. Maximum depth: 0.5 to 0.8 cun (in thin, elderly, or emaciated patients, the pleural cavity is only 1.5 to 2.0 cm beneath the skin surface).\n4. Patients with chronic emphysema or COPD have hyperinflated lungs and barrel chests, placing the pleura dangerously close to the skin.",
        "consensus": "Traumatic pneumothorax is the single most common life-threatening adverse event reported in malpractice claims against acupuncturists.",
        "variations": "Needling GB21 posteriorly towards the scapular spine rather than straight down eliminates apical lung penetration risk.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Pneumothorax: Clinical Signs & Immediate Emergency Protocol",
        "front": "What are the clinical signs of an acute Pneumothorax post-acupuncture, and what is the acupuncturist's immediate emergency protocol?",
        "back": "Clinical Signs of Pneumothorax (may develop immediately or up to several hours later):\n• Sudden sharp, stabbing chest pain worsened by deep breathing or coughing.\n• Progressive dyspnea (shortness of breath) and tachypnea (rapid breathing).\n• Non-productive, persistent dry hacking cough.\n• Tachycardia, anxiety, diaphoresis (cold sweats), and restlessness.\n• Cyanosis (bluish tint of lips, nail beds, and skin) in severe or tension pneumothorax.\n• Decreased or absent breath sounds on the affected side upon auscultation; hyperresonance on percussion.\n\n⚠️ Immediate Emergency Protocol:\n1. Stop treatment immediately and gently withdraw all needles.\n2. Keep the patient calm, quiet, and seated in a semi-Fowler's position (semi-upright at 45°); do NOT allow the patient to walk, exert themselves, or leave the clinic unescorted.\n3. Call 911 (Emergency Medical Services) immediately; report suspected traumatic pneumothorax from needling.\n4. Administer supplemental oxygen if available and trained.\n5. Monitor and record vital signs (BP, pulse, respiration, SpO2) until paramedics arrive.",
        "consensus": "Never send a patient with suspected pneumothorax home to 'rest and see if it gets better.' Immediate emergency hospital evaluation and chest X-ray are legally required.",
        "variations": "A small apical pneumothorax (<15%) may be managed conservatively with observation, but a tension pneumothorax is immediately fatal without needle thoracostomy.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Bickley Bates' Guide to Physical Examination", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "CNS Danger Points: DU15 (Yamen) & DU16 (Fengfu)",
        "front": "State the anatomical danger, strict needle angle, and depth limits for DU15 (Yamen) and DU16 (Fengfu).",
        "back": "CNS Danger Points: DU15 (Yamen / 哑门) & DU16 (Fengfu / 风府):\n• Location:\n  - DU15: Posterior midline, 0.5 cun superior to the posterior hairline, in the depression below the spinous process of C1 (atlas).\n  - DU16: Posterior midline, 1.0 cun superior to the posterior hairline, in the depression directly below the external occipital protuberance.\n\n⚠️ Anatomical Danger:\n• Directly deep to these points lies the atlanto-occipital membrane, the foramen magnum, and the Medulla Oblongata / Brainstem (containing the vital cardiovascular and respiratory control centers) and the spinal cord.\n\n⚠️ Strict Needling Rules:\n1. Insert needle strictly PERPENDICULAR or SLIGHTLY INFERIOR (downward towards the larynx/throat) to a depth of ONLY 0.5 to 0.8 cun.\n2. NEVER ANGLE THE NEEDLE SUPERIORLY (upward towards the crown or occiput).\n3. Superior or excessively deep insertion (>1.0 cun) enters the foramen magnum and penetrates the medulla oblongata, causing instant respiratory arrest, brainstem hemorrhage, and death.\n4. Moxibustion is classically contraindicated at DU15.",
        "consensus": "Universal critical anatomical safety warning across all global acupuncture jurisdictions.",
        "variations": "Instruct the patient to keep head in neutral or slight flexion; do NOT allow patient to hyperextend the neck during needle insertion.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Safety and Ethics",
        "title": "Ophthalmic Needling Safety: BL1 (Jingming) & ST1 (Chengqi)",
        "front": "Detail the specialized safety rules, insertion technique, and hematoma prevention protocol for BL1 (Jingming) and ST1 (Chengqi).",
        "back": "Ophthalmic Points: BL1 (Jingming / 睛明) & ST1 (Chengqi / 承泣):\n• Needling Protocol:\n  1. Patient must be in a relaxed supine position with eyes closed.\n  2. For BL1: Gently push the eyeball laterally with clean gloved finger to expose medial orbital wall. For ST1: Gently push the eyeball superiorly with finger to expose inferior orbital rim.\n  3. Puncture SLOWLY 0.5 - 1.0 cun along the bony orbital wall.\n  4. STRICTLY PROHIBITED: Lifting, thrusting, violent twisting, rotating, or electroacupuncture manipulation in the orbital cavity.\n\n⚠️ Immediate Hematoma Prevention upon Needle Withdrawal:\n• Upon removing the needle, immediately place a sterile dry cotton ball over the puncture site and apply DIRECT, FIRM, STEADY PRESSURE for 1 to 2 MINUTES without rubbing or massaging.\n• Rationale: The retrobulbar space contains delicate ophthalmic venous plexuses. Failure to compress causes retrobulbar hemorrhage and hematoma ('black eye'), which can elevate intraocular pressure and damage the optic nerve.",
        "consensus": "Mandatory standard of care: slow unmanipulated insertion and minimum 1–2 minutes firm compression upon removal.",
        "variations": "CAM limits needle depth to 0.3–0.7 cun; Deadman emphasizes slow insertion without needle guide tube to feel tissue resistance.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Safety and Ethics",
        "title": "Visceral Puncture: Bladder, Liver, Spleen, and Peritoneal Cavity",
        "front": "What mandatory precautions must be taken before puncturing the lower abdomen (CV2, CV3) and upper abdomen (ST21, LV14, LR13) to prevent organ puncture?",
        "back": "Visceral Puncture Precautions:\n• Urinary Bladder (CV2 Qugu, CV3 Zhongji, CV4 Guanyuan):\n  - Hazard: A distended urinary bladder rises out of the pelvic cavity into the lower abdomen; deep needling can puncture the bladder wall, leaking urine into peritoneal cavity and causing peritonitis.\n  - Mandatory Precaution: Patient MUST empty bladder immediately prior to acupuncture treatment.\n\n• Liver and Gallbladder (Right ST21, Right LV14, Right LV13):\n  - Hazard: Hepatomegaly or an enlarged gallbladder extends beneath the right costal margin; deep perpendicular needling risks hepatic laceration, internal bleeding, and bile peritonitis.\n  - Mandatory Precaution: Gently palpate right upper quadrant for hepatomegaly prior to needling; use oblique insertion 0.5–0.8 cun only.\n\n• Spleen (Left LV14, Left LV13, SP14):\n  - Hazard: Splenomegaly (e.g. from mononucleosis, cirrhosis) enlarges the fragile spleen into the left hypochondrium; deep needling causes splenic rupture and massive internal hemorrhage.\n  - Mandatory Precaution: Palpate for splenomegaly; strictly avoid deep needling into left costal margin.",
        "consensus": "Mandatory pre-needling physical assessment: empty bladder and palpate for organomegaly before abdominal needling.",
        "variations": "Instruct patient to breathe out during abdominal needle insertion to relax abdominal musculature.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Needle Fainting (Yun Zhen / Vasovagal Syncope): Protocol",
        "front": "List the predisposing factors, early warning signs, and immediate clinical emergency management protocol for Needle Fainting (Yun Zhen).",
        "back": "Needle Fainting (Yun Zhen - 晕针 / Vasovagal Syncope):\n• Predisposing Factors: First-time acupuncture, severe emotional anxiety/fear, hunger, fasting, dehydration, extreme fatigue, sitting upright during treatment, heavy needle stimulation.\n\n• Early Warning Signs:\n  - Sudden pallor, dizzy lightheadedness, cold clammy sweat on forehead/palms, nausea, blurred vision, palpitations, yawning, restlessness, thready/weak pulse.\n\n⚠️ Immediate Management Protocol:\n1. Stop treatment immediately and WITHDRAW ALL NEEDLES promptly.\n2. Help patient lie completely flat in a supine position; elevate patient's legs 15–30 degrees above heart level (Trendelenburg position) to increase venous return to the brain.\n3. Loosen tight clothing around the neck, chest, and waist; ensure fresh air ventilation.\n4. Provide warm water or warm sugar/glucose water once conscious and alert.\n5. Press or needle emergency acupoints:\n   - DU26 (Shuigou / 水沟): Firm thumbnail press or needle obliquely upward.\n   - PC6 (Neiguan / 内关): Firm bilateral acupressure to stabilize heart rate.\n   - ST36 (Zusanli / 足三里): Firm acupressure.\n6. Monitor blood pressure and pulse. If unconsciousness persists for >1–2 minutes, call 911 immediately.",
        "consensus": "The most frequent acute adverse event in acupuncture practice. All patients receiving first-time acupuncture should be treated in the supine or prone position.",
        "variations": "Never treat a first-time patient while they are seated in a chair; fainting in a chair causes rapid head drop, injury, and prolonged cerebral ischemia.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CAM 3rd Ed.", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Complications: Stuck Needle (Zhi Zhen) Management",
        "front": "What causes a Stuck Needle (Zhi Zhen), and how should an acupuncturist safely release and remove it without injury?",
        "back": "Stuck Needle (Zhi Zhen - 滞针):\n• Causes:\n  1. Local muscle spasm or sudden patient movement during needle retention.\n  2. Excessive unidirectional needle twirling/rotation (>360 degrees) causing connective tissue fibers to wrap tightly around the needle shaft.\n\n⚠️ Safe Removal Protocol:\n1. Reassure the patient and instruct them to take slow, deep breaths to relax surrounding musculature.\n2. If caused by excessive rotation: Gently twirl the needle in the OPPOSITE DIRECTION to unwind the trapped connective tissue fibers, then withdraw.\n3. If caused by muscle spasm:\n   - Leave the needle in place untouched for a few minutes; the muscle spasm will naturally subside.\n   - Gently massage, rub, or tap the skin and muscle adjacent to the needle site to release muscular tension.\n   - Puncture a secondary needle 1–2 cm away from the stuck needle; this diverts local Qi and releases the spasm around the first needle.\n4. NEVER pull forcefully on a stuck needle, as this causes severe pain, tissue tearing, needle bending, or needle breakage.",
        "consensus": "Unwinding opposite to rotation and tapping adjacent skin are standard universal techniques.",
        "variations": "Leaving the needle untouched for 5 minutes is usually sufficient for spontaneous muscle relaxation.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CAM 3rd Ed."])
    },
    {
        "category": "Safety and Ethics",
        "title": "Complications: Bent Needle (Wan Zhen) & Broken Needle (Zhe Zhen)",
        "front": "Detail the management protocols for a Bent Needle (Wan Zhen) and the three scenarios of a Broken Needle (Zhe Zhen).",
        "back": "Complications Management:\n• Bent Needle (Wan Zhen - 弯针):\n  - Causes: Patient changes posture while needles are retained, muscular spasm, or needle struck by external force.\n  - Management: Restore patient to original position before movement. Never pull forcefully or rotate a bent needle. Slowly withdraw the needle following the EXACT CURVE and direction of the bend.\n\n• Broken Needle (Zhe Zhen - 折针):\n  - Causes: Poor quality needle, galvanic corrosion at junction of shaft and handle, sudden violent spasm, or forceful pulling on a bent needle.\n  - Scenario 1 (Part of shaft still protrudes above skin): Instruct patient to remain completely still. Grasp the exposed shaft firmly with sterile forceps or tweezers and withdraw.\n  - Scenario 2 (Broken end is flush with skin surface): Press gently down on the surrounding tissue around the puncture site with fingers until the broken tip emerges; grasp with forceps and extract.\n  - Scenario 3 (Broken end is completely buried beneath skin surface): Instruct patient to remain COMPLETELY MOTIONLESS. Mark the exact location with surgical marker. Do NOT massage or manipulate the area. IMMEDIATELY transport patient to hospital emergency surgical department for surgical removal under fluoroscopy.",
        "consensus": "Never insert a needle all the way to its handle; always leave at least 1/4 to 1/3 of the needle shaft exposed above the skin surface.",
        "variations": "The junction between handle and shaft is the weakest structural point of an acupuncture needle.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CAM 3rd Ed.", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Pregnancy Contraindicated Points: Complete Safety Summary",
        "front": "List all acupoints strictly contraindicated in pregnancy, organized by mechanism, trimester, and anatomical region.",
        "back": "Pregnancy Contraindicated Points Summary:\n1. Distal Points with Powerful Descending & Uterine-Stimulating Actions:\n   - LI4 (Hegu / 合谷): Yuan-Source of Large Intestine; descends Qi strongly.\n   - SP6 (Sanyinjiao / 三阴交): Crossing of 3 Leg Yin; stimulates uterine contractions and moves blood.\n   - BL60 (Kunlun / 昆仑): Powerful downward descending Qi action.\n   - BL67 (Zhiyin / 至阴): Turns breech fetus, stimulates uterine motility.\n   - GB21 (Jianjing / 肩井): Powerfully descends Qi from upper body downward.\n\n2. Lower Abdominal Points:\n   - CV1 through CV7 (specifically CV3, CV4, CV5), ST28, ST29, ST30, SP12, SP13.\n   - 1st Trimester: Strictly contraindicated on entire lower abdomen below umbilicus.\n   - 2nd & 3rd Trimesters: Strictly contraindicated on entire abdomen (upper and lower abdomen).\n\n3. Lumbosacral Points:\n   - Sacral Foramina: BL31, BL32, BL33, BL34 (Ba Liao - 八髎).\n   - Lower Lumbar: BL23 through BL28, DU3, DU4.\n   - Puncturing over sacrum or lower back induces uterine contractions and miscarriage.",
        "consensus": "Universal absolute contraindications during pregnancy taught across all accredited colleges.",
        "variations": "In overdue, prolonged, or difficult labor, LI4, SP6, and BL67 may be deliberately utilized under obstetric supervision to promote delivery.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture", "CAM 3rd Ed."])
    },
    {
        "category": "Safety and Ethics",
        "title": "Informed Consent: Essential Legal Elements (COM-02)",
        "front": "What are the essential legal elements of valid Informed Consent in acupuncture practice under Canadian/provincial jurisprudence?",
        "back": "Essential Legal Elements of Informed Consent (COM-02 Jurisprudence):\n1. Voluntariness: Consent must be given freely and voluntarily, without coercion, duress, or undue influence.\n2. Mental Capacity: Patient must possess decision-making capacity to understand the nature, purpose, risks, and alternatives of the proposed treatment.\n3. Disclosure of Nature and Purpose: Clear explanation of what acupuncture, moxibustion, cupping, or tuina involves in plain, understandable language.\n4. Disclosure of Material and Special Risks: Must explicitly disclose common and rare serious risks, including:\n   - Pain, minor bleeding, bruising (hematoma).\n   - Dizziness, lightheadedness, or fainting (syncope).\n   - Infection risk (controlled by single-use sterile disposable needles).\n   - Rare serious risk of Pneumothorax with chest/back needling.\n   - Moxa burn risks, cupping marks/bruises.\n5. Disclosure of Alternative Treatments: Alternative therapies and the consequences of refusing treatment.\n6. Opportunity to Ask Questions: Patient must have all questions answered.\n7. Ongoing Nature: Consent is NOT a one-time paper signature; it is an ongoing dialogue. Patient retains the right to withdraw consent at any time during treatment.",
        "consensus": "Universal medico-legal requirement before performing any invasive clinical procedure.",
        "variations": "For mature minors (infants/children who understand), capacity determines consent rather than strict chronological age in many Canadian provinces.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics & Jurisprudence", "Health Care Consent Act (HCCA)", "CTCMA Bylaws"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Confidentiality & Privacy: PIPEDA & Mandatory Exceptions",
        "front": "Explain the patient confidentiality obligations under Canadian privacy legislation (PIPEDA / PIPA) and list the mandatory legal exceptions where confidentiality MUST be breached.",
        "back": "Confidentiality Obligations & Mandatory Exceptions (COM-02):\n• General Privacy Duty:\n  - Acupuncturists are legally and ethically bound to maintain absolute confidentiality of all personal health information (PHI).\n  - All paper charts must be locked in double-secured filing cabinets; electronic records must be encrypted, password-protected, and backed up securely under PIPEDA (Personal Information Protection and Electronic Documents Act).\n\n⚠️ Mandatory Exceptions (Where Practitioner MUST Breach Confidentiality):\n1. Suspected Child Abuse or Neglect: Immediate mandatory reporting to Child Protection Services (CAS / MCFD) is required by law if physical abuse, sexual abuse, or neglect of a child (<19 years) is suspected.\n2. Imminent Risk of Serious Harm or Death: Clear, imminent threat of serious bodily harm or suicide to the patient or an identifiable third party ('Duty to Warn / Duty to Protect').\n3. Mandatory Reportable Communicable Diseases: Reporting specified infectious diseases (e.g. active tuberculosis, measles, cholera) to Public Health authorities.\n4. Court Subpoena or Search Warrant: Official court order legally compelling medical records disclosure.\n5. Fitness to Drive: In certain jurisdictions, reporting conditions causing sudden loss of consciousness (e.g., uncontrolled epilepsy).",
        "consensus": "Child abuse reporting supersedes all doctor-patient privilege; failure to report is a criminal offense.",
        "variations": "Acupuncturist should disclose only the minimum necessary information required by the legal obligation.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics & Jurisprudence Handbook", "PIPEDA Federal Privacy Standards"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Professional Boundaries: Dual Relationships & Zero Tolerance",
        "front": "Define professional boundaries in the therapeutic relationship and explain the regulatory stance on sexual abuse of patients (Zero Tolerance).",
        "back": "Professional Boundaries & Regulatory Law (COM-02 Jurisprudence):\n• Definition of Professional Boundaries:\n  - The invisible line that separates the professional therapeutic relationship from a personal, social, or romantic relationship.\n  - The acupuncturist holds inherent fiduciary power and authority; the patient is inherently vulnerable.\n\n• Dual Relationships:\n  - Occur when a practitioner has a second relationship with a patient (e.g. social friendship, romantic partner, business partner, employer/employee).\n  - Precaution: Avoid dual relationships whenever possible; they impair clinical objectivity and create conflicts of interest.\n\n⚠️ Zero Tolerance Policy on Sexual Abuse of Patients:\n1. Absolute Prohibition: Any sexual intercourse, sexual touching, sexualized comments, flirtation, or dating between a registered acupuncturist and a patient is classified by health regulatory colleges as SEXUAL ABUSE.\n2. Patient Consent is Legally Irrelevant: Under health professions legislation (e.g., Regulated Health Professions Act), a patient CANNOT legally consent to a sexual relationship with their healthcare provider. The power imbalance renders consent invalid.\n3. Mandatory Penalty: Mandatory permanent revocation of professional registration/license for a minimum statutory period (typically 5 years to life), plus potential criminal charges.",
        "consensus": "Universal zero-tolerance standard across all Canadian healthcare regulatory colleges.",
        "variations": "A minimum cooling-off period of at least one year (and full termination of the professional relationship) is required before any social or dating relationship could even be contemplated.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics Handbook", "CTCMA Professional Boundaries Guidelines", "RHPA Standards"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Medical Record Keeping: Retention Periods & SOAP Notes",
        "front": "State the legal requirements for clinical record keeping (SOAP notes) and mandatory record retention durations under Canadian jurisprudence.",
        "back": "Medical Record Keeping Requirements (COM-02 Jurisprudence):\n• Record Retention Periods (Mandatory Standards):\n  - Adult Patients: Patient clinical records, billing files, and consent forms must be securely retained for a MINIMUM of 10 YEARS (or 16 years in some provinces) from the date of the last treatment/entry.\n  - Pediatric Patients (Minors under 18/19 years): Records must be retained for 10 YEARS AFTER THE PATIENT REACHES THE AGE OF MAJORITY (e.g. 10 years after 18th/19th birthday = retain until age 28 or 29).\n  - Destruction: Must be conducted securely (cross-cut shredding or certified electronic data wiping) to prevent identity theft.\n\n• Clinical Documentation Standard: SOAP Note Format:\n  - S - Subjective: Patient's Chief Complaint, pain rating (1-10), onset, location, modality, changes since last visit.\n  - O - Objective: Tongue signs, pulse signs, visual observations, palpation findings, orthopedic tests, blood pressure.\n  - A - Assessment: TCM Pattern Differentiation (Bian Zheng), Western diagnostic impressions, clinical progress.\n  - P - Plan: Acupoints used, needle techniques, depth, retention time, moxa/cupping, adverse reactions (if any), patient response, home advice, treatment plan for next visit.\n  - Notes must be recorded contemporaneously (within 24 hours), dated, signed, and never erased or whited out (corrections must be a single strikethrough with initials and date).",
        "consensus": "Mandatory standard of practice: 'If it wasn't written down in the clinical record, it didn't happen' in the eyes of the law.",
        "variations": "Electronic Medical Record (EMR) software must maintain a permanent, unalterable audit trail of every entry and modification.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics & Jurisprudence Handbook", "CTCMA Record Keeping Guidelines"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Sharps Safety & Biohazard Waste Management",
        "front": "State the safety rules for sharps containers, disposal protocols, and the 'Never Recap' rule in acupuncture practice.",
        "back": "Sharps Safety & Biohazard Disposal Rules:\n• The 'Never Recap' Rule:\n  - NEVER recap, bend, break, shear, or manually manipulate used acupuncture needles before disposal.\n  - Recapping by hand is the primary cause of accidental contaminated needlestick injuries among healthcare workers.\n\n• Sharps Container Standards:\n  - Must be rigid, puncture-resistant, leak-proof on sides and bottom, sealable, and clearly labeled with the universal BIOHAZARD symbol.\n  - Must be located within arm's reach of the treatment table and at eye level/accessible height.\n  - Drop used needles directly into the container immediately upon removal from the patient's skin.\n\n• The 'Three-Quarters Full' Rule:\n  - Sharps containers must be permanently locked and disposed of when filled to the 3/4 FULL line (or designated fill line).\n  - NEVER force, push, cram, or shake needles down into an overfilled container; protruding needles create severe puncture hazards.\n  - Disposal must be conducted via a licensed medical biohazard waste disposal contractor.",
        "consensus": "Standard universal biohazard protocol required by OSHA, Canadian Public Health, and CNT guidelines.",
        "variations": "Cotton balls with visible blood or bodily fluid must be discarded in a biohazard waste bag; dry cotton balls may be placed in regular trash if not saturated.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM Clean Needle Technique Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Moxibustion Safety: Burn Prevention & Burn Management",
        "front": "What are the fire safety rules for moxibustion, burn prevention measures, and clinical management of first- and second-degree moxa burns?",
        "back": "Moxibustion Safety & Burn Management (COM-06 Safety):\n• Prevention & Fire Safety:\n  - NEVER leave a patient unattended while moxa is burning.\n  - Maintain constant manual monitoring: practitioner's index and middle fingers should rest on patient's skin adjacent to the point to constantly gauge heat intensity.\n  - Extinguishing: Fully extinguish moxa sticks in a dedicated moxa snuffer or airtight glass/metal container; never tap hot ashes onto carpet or flammable surfaces.\n  - Ventilation: Ensure adequate air exhaust/HEPA filtration to prevent smoke inhalation and triggering fire alarms.\n\n• Clinical Burn Management:\n  - First-Degree Burn (Erythema / Redness without blistering):\n    - Immediately cool the area with cool (not ice-cold) sterile running water or saline for 10–15 minutes. Apply burn dressing or sterile aloe vera.\n  - Second-Degree Burn (Small Blister < 1 cm):\n    - Disinfect with antiseptic; do NOT pop or puncture the blister (intact skin serves as a sterile natural biological barrier against infection). Apply sterile non-adherent dressing.\n  - Large Blister (> 1 cm) or Broken Blister:\n    - Drain fluid with sterile syringe needle under strict aseptic conditions, leaving the blister roof intact as a protective cover; apply sterile antibacterial ointment and refer for medical evaluation if signs of secondary bacterial infection appear (increasing erythema, purulent discharge, lymphangitis).",
        "consensus": "Constant tactile monitoring and dedicated snuffers are mandatory fire/burn prevention rules.",
        "variations": "Diabetic neuropathy patients with impaired thermal sensation have extreme burn risk and require extra vigilance.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM Clean Needle Technique Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Cupping Safety: Blister Prevention & Contraindications",
        "front": "State the safety rules for Fire Cupping, suction duration limits, blister management, and absolute clinical contraindications for cupping.",
        "back": "Cupping Therapy Safety Standards (COM-06 Safety):\n• Fire Cupping Technique:\n  - Dip cotton ball in 70% or 91% alcohol, squeeze out excess alcohol thoroughly (excess alcohol dripping onto patient's skin causes catastrophic chemical/thermal burns).\n  - Light cotton, insert flame into cup for 1–2 seconds to evacuate air, and place immediately onto skin.\n  - Never heat the rim of the glass cup.\n\n• Suction & Duration Limits:\n  - Stationary cupping duration: Typically 5 to 10 minutes maximum (up to 15 minutes in robust patients). Prolonged suction (>15–20 minutes) causes extensive epidermal blistering.\n  - Moving Cupping (Zou Guan): Always apply generous massage oil or lubricant; move along muscle bellies.\n\n• Absolute Contraindications for Cupping:\n  1. Over active skin lesions, open wounds, eczema, psoriasis, ulcerations, or sunburn.\n  2. Patients with severe bleeding disorders, severe purpura, or deep vein thrombosis (DVT).\n  3. Abdomen and lumbosacral region during pregnancy.\n  4. Directly over major superficial blood vessels (carotid, femoral, popliteal) or varicose veins.\n  5. Patients with high fever, acute convulsions, or severe cardiac disease.",
        "consensus": "Squeezing out excess alcohol before lighting is the premier safeguard against fire cupping burns.",
        "variations": "Educate patient beforehand that cupping marks (Sha / ecchymosis) are expected therapeutic petechiae, not true tissue bruises, and resolve in 3–7 days.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Electroacupuncture (EA): Cardiac Pacemaker & Transthoracic Cautions",
        "front": "What are the absolute contraindications and electrical circuit pathway rules for Electroacupuncture (EA)?",
        "back": "Electroacupuncture Safety Standards (COM-06 Safety):\n• Absolute Contraindication: CARDIAC PACEMAKERS & IMPLANTABLE DEFIBRILLATORS (ICDs):\n  - Electroacupuncture is strictly contraindicated in patients with cardiac pacemakers, ICDs, or internal neurostimulators.\n  - Mechanism: Electrical currents can interfere with cardiac sensing circuits, causing fatal ventricular pacing inhibition or triggering inappropriate defibrillator shocks.\n\n• Transthoracic Circuit Rule (NEVER CROSS THE HEART):\n  - NEVER place electroacupuncture leads across the chest or posterior thorax such that the electrical current pathway crosses the heart (e.g., bilateral lead from left arm to right arm, or left anterior chest to right upper back).\n  - Transthoracic electrical currents can induce fatal cardiac arrhythmias (Ventricular Fibrillation).\n\n• Other High-Risk Sites:\n  - Avoid crossing the spine/spinal cord transversely.\n  - Avoid the anterior neck (carotid sinus region) to prevent severe bradycardia and hypotension.\n  - Avoid crossing the brainstem.\n  - Contraindicated in active epilepsy / seizure disorders, and over active malignant tumors.",
        "consensus": "Pacemakers and crossing the cardiac axis are universal absolute contraindications for electroacupuncture.",
        "variations": "Always turn stimulation intensity dials to zero BEFORE connecting leads and turning machine on, and before turning machine off.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Deadman Manual of Acupuncture", "CCAOM CNT Manual"])
    },
    {
        "category": "Safety and Ethics",
        "title": "Regulatory Jurisprudence: Mandatory Reporting of Sexual Abuse",
        "front": "What is an acupuncturist's legal obligation if they learn that another regulated health professional has sexually abused a patient?",
        "back": "Mandatory Reporting Obligations (COM-02 Jurisprudence):\n• Legal Duty to Report:\n  - Under health professions regulation (e.g. Regulated Health Professions legislation across Canadian provinces), a registered acupuncturist who has reasonable grounds to believe that another regulated health professional has committed sexual abuse of a patient MUST file a written report to the registrar of that professional's regulatory College.\n\n• Filing Timeline:\n  - The report must be submitted in writing within 30 DAYS of forming the belief (or immediately if there is reason to believe the professional continues to pose an immediate danger to patients).\n\n• Required Information in Report:\n  - The name of the health professional suspected of abuse.\n  - An objective, factual summary of the suspected misconduct.\n  - If the victim consents: The victim's name (if the victim does NOT consent to their name being disclosed, the report must STILL be submitted with the victim's name omitted).\n\n• Penalties for Failure to Report:\n  - Failure to file a mandatory report of sexual abuse is an act of professional misconduct subject to disciplinary hearings, heavy fines (often up to $25,000–$50,000), and potential license suspension.",
        "consensus": "Mandatory reporting of sexual abuse is a statutory legal obligation with zero practitioner discretion.",
        "variations": "Practitioners reporting in good faith are granted statutory immunity from civil defamation lawsuits.",
        "sources": json.dumps(["Royal TCM COM-02 Ethics & Jurisprudence Handbook", "Regulated Health Professions Act (RHPA)", "CTCMA Bylaws"])
    }
]

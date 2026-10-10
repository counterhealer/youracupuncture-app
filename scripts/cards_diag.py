"""Diagnosis Flashcards (35 high-yield diagnostic cards).

Covers the Four Examinations, Shen observation, facial colors, tongue body color,
tongue shape, tongue coating, 28 classic pulses, Eight Principles, Zang-Fu differentiation,
Six Stages, and Four Levels.
"""

import json

CARDS = [
    {
        "category": "Diagnosis",
        "title": "Observation of Shen: Having Shen, Lacking Shen, False Shen",
        "front": "Distinguish between 'Having Shen' (You Shen), 'Lacking Shen' (Shi Shen), and 'False Shen' (Dai Shen - 假神).",
        "back": "Clinical Comparison:\n• Having Shen (You Shen - 有神):\n  - Manifestation: Bright alert eyes, clear consciousness, resonant voice, radiant complexion, calm steady breathing.\n  - Prognosis: Vital Qi is intact; disease is mild or prognosis is favorable.\n\n• Lacking Shen (Shi Shen - 失神):\n  - Manifestation: Dull listless eyes, mental confusion or coma, feeble speech, withered dull complexion, labored breathing.\n  - Prognosis: Exhaustion of Essential Qi; serious condition with guarded prognosis.\n\n• False Shen (Dai Shen - 假神):\n  - Manifestation: A critically ill, bedridden patient with chronic exhaustion of Zheng Qi who suddenly exhibits transient 'improvement'—sudden lucid speech, bright red cheeks like makeup ('floating red'), ravenous appetite, desire to see family.\n  - Mechanism: Separation of Yin and Yang; last vestige of Yang Qi floating outward prior to death ('flaring of dying embers'). Immediate medical emergency.",
        "consensus": "Universal TCM principle for evaluating disease severity and vital vitality.",
        "variations": "False Shen requires differentiating from true recovery: true recovery is gradual with concurrent improvement in pulse, tongue, and physical strength.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics of TCM", "Maciocia Foundations of Chinese Medicine"])
    },
    {
        "category": "Diagnosis",
        "title": "Facial Complexion: The Five Colors (Wu Se - 五色)",
        "front": "What pathological patterns are indicated by the Five Facial Colors: Green/Blue, Red, Yellow, White, and Black?",
        "back": "The Five Colors & Pattern Indications:\n1. Green / Blue (Qing - 青): Liver patterns, Cold invasion, Severe pain, Blood stasis, Infantile convulsions.\n2. Red (Chi - 赤): Heat patterns.\n   - Whole face bright red: Excess Full Heat (Yangming).\n   - Malar flush (red cheekbones) with afternoon fever: Empty Deficiency Heat (Yin deficiency).\n3. Yellow (Huang - 黄): Spleen deficiency, Dampness accumulation.\n   - Bright orange-yellow ('tangerine'): Yang Jaundice (Damp-Heat).\n   - Dull dark smoky yellow: Yin Jaundice (Cold-Damp).\n   - Pale sallow yellow without gloss: Spleen Qi and Blood deficiency.\n4. White / Pale (Bai - 白): Deficiency patterns (Qi/Blood deficiency), Cold patterns, Severe blood loss.\n5. Black / Dark (Hei - 黑): Kidney deficiency (Yin or Yang), Cold stagnation, Severe chronic blood stasis, Water retention (dark rings around eyes).",
        "consensus": "Classic diagnostic observation from Huangdi Neijing Suwen Chapter 10.",
        "variations": "Look for luster and moisture (vitality): any color with luster has a better prognosis than a dull, withered complexion.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Body Color: Pale vs Red vs Crimson vs Purple",
        "front": "Interpret the four primary tongue body colors: Pale, Red, Deep Red (Crimson), and Purple.",
        "back": "Tongue Body Colors:\n• Pale Tongue (Dan Bai She - 淡白舌):\n  - Indicates: Deficiency of Qi and Blood, or Yang Deficiency with Interior Cold.\n  - Pale & wet/swollen = Yang deficiency; Pale & thin/dry = Blood deficiency.\n\n• Red Tongue (Hong She - 红舌):\n  - Indicates: Heat patterns.\n  - Red with thick yellow coat = Excess Interior Heat.\n  - Red with little or peeled coat, cracks = Deficiency Heat (Yin deficiency).\n\n• Deep Red / Crimson Tongue (Jiang She - 绛舌):\n  - Indicates: Extreme heat.\n  - In exogenous febrile diseases: Heat has invaded the Ying (Nutritive) or Xue (Blood) levels.\n  - In chronic diseases: Severe Yin collapse with rampant empty fire.\n\n• Purple Tongue (Zi She - 紫舌):\n  - Indicates: Blood stasis.\n  - Reddish-purple / dry = Heat congealing blood stasis.\n  - Bluish-purple / moist = Cold congealing blood stasis.",
        "consensus": "Tongue body color reflects the true state of the organs, blood, and thermal nature (heat vs cold).",
        "variations": "Tongue body color is the most reliable tongue parameter because it changes slowly and is less prone to temporary food staining than the coating.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Tongue Diagnosis in Chinese Medicine"])
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Shape: Swollen with Teeth Marks",
        "front": "What is the clinical significance of a swollen tongue body with teeth marks (scalloped edges)?",
        "back": "Clinical Significance:\n• Primary Pathology: Spleen Qi Deficiency failing to transform and transport body fluids, leading to internal Dampness accumulation.\n• Mechanisms:\n  - The tongue swells due to fluid retention and presses against the lateral dental arches, creating indented teeth marks.\n• Clinical Differentiations:\n  - Swollen, pale, wet tongue with teeth marks: Spleen and Kidney Yang Deficiency with cold-damp water retention.\n  - Swollen, red tongue with teeth marks and greasy yellow coat: Spleen-Stomach Damp-Heat or Phlegm-Heat.\n  - Swollen lateral edges only: Liver Qi stagnation or Liver Blood deficiency.",
        "consensus": "One of the most frequently observed tongue signs in clinical practice.",
        "variations": "Severe swelling filling the entire mouth and preventing speech is termed 'Lotus flower tongue' or toxic heat swelling.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Tongue Diagnosis"])
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Shape: Deviated, Stiff, and Trembling",
        "front": "What do a deviated tongue, a stiff (rigid) tongue, and a trembling tongue indicate regarding internal wind and neurological pathology?",
        "back": "Pathological Indications:\n• Deviated Tongue (Wai Xie She - 歪斜舌):\n  - The tongue slants to one side upon protrusion.\n  - Indicates: Internal Liver Wind, Wind-Phlegm obstructing channels, or impending/manifest Wind-Stroke (Zhong Feng - CVA/TIA).\n  - Neurological correlation: Cranial Nerve XII (Hypoglossal) lesion; tongue deviates toward the side of the lesion.\n\n• Stiff / Rigid Tongue (Jiang She - 强硬舌):\n  - Lack of flexibility, difficult speech, unable to protrude or move freely.\n  - Indicates: High fever scorching body fluids (heat invading Pericardium), turbid phlegm clouding the orifices, or severe internal wind pre-stroke.\n\n• Trembling Tongue (Chan Dou She - 颤动舌):\n  - Involuntary shaking or quivering upon protrusion.\n  - Indicates: Chronic Qi/Blood deficiency failing to nourish sinews, or Liver Wind stirring.",
        "consensus": "Immediate red-flag warning signs for cerebrovascular disease and neurological wind.",
        "variations": "Trembling in a pale tongue = Qi/Yang deficiency; trembling in a deep red tongue = Extreme heat stirring wind.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Tongue Diagnosis"])
    },
    {
        "category": "Diagnosis",
        "title": "Tongue Coating: Thickness, Moisture, and Greasiness",
        "front": "Interpret what tongue coating thickness, moisture, and greasiness (turbidity) reveal about pathogens and fluids.",
        "back": "Tongue Coating Characteristics:\n• Thickness (Thin vs Thick):\n  - Thin coat: Normal, or early exterior attack (pathogen is superficial, Zheng Qi is uninjured).\n  - Thick coat: Pathogen has entered the interior, or severe food stagnation, phlegm, or dampness.\n  - Progression: Thin becoming thick = disease worsening/penetrating; Thick becoming thin = disease resolving.\n\n• Moisture (Moist vs Dry):\n  - Normal moist: Sufficient body fluids and unimpaired Stomach Yin.\n  - Overly wet / slippery: Cold-damp or Yang deficiency failing to transform water.\n  - Dry / rough: Heat consuming body fluids, or severe Yin depletion.\n\n• Greasiness (Greasy / Turbid vs Peeled):\n  - Greasy (Ni Tai - 腻苔): Fine sticky granules that cannot be scraped off; indicates Phlegm, Dampness, or Food Retention.\n  - Peeled / Mirror (Guang Bo Tai - 光剥苔): Complete absence of coating; indicates total exhaustion of Stomach Yin and Kidney fluids.",
        "consensus": "Tongue coating reflects the strength of the pathogen, digestion, and the state of Stomach Qi.",
        "variations": "True coat (has root, grows from tongue surface) vs False coat (floats on surface, easily scraped off like curd).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Tongue Diagnosis"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Floating (Fu) vs Deep (Chen)",
        "front": "Compare the sensation, depth, and clinical indications of the Floating Pulse (Fu Mai) and Deep Pulse (Chen Mai).",
        "back": "Comparison:\n• Floating Pulse (Fu Mai - 浮脉):\n  - Sensation: Felt with light touch on the superficial surface; becomes weaker or diminishes under heavy pressure.\n  - Indications: Exterior patterns (exterior wind-cold or wind-heat attacks). The body's defensive (Wei) Qi moves outward to fight the pathogen.\n  - Exception (Deficiency Floating): Floating, large, empty under deep pressure indicates severe Yin/Blood exhaustion with floating Yang.\n\n• Deep Pulse (Chen Mai - 沉脉):\n  - Sensation: Not felt on superficial touch; felt clearly only with heavy pressure near the tendon and bone.\n  - Indications: Interior patterns.\n  - Deep & forceful = Interior Excess (cold, heat, food stagnation, phlegm).\n  - Deep & weak/thin = Interior Deficiency (Yang deficiency, Qi deficiency).",
        "consensus": "Fundamental depth parameter determining exterior vs interior disease location.",
        "variations": "A hidden pulse (Fu Mai) is even deeper than a deep pulse, requiring extreme bone pressure to palpate.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies (Bin Hu Mai Xue)"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Slow (Chi) vs Rapid (Shuo)",
        "front": "Compare the rates, sensations, and clinical indications of the Slow Pulse (Chi Mai) and Rapid Pulse (Shuo Mai).",
        "back": "Comparison:\n• Slow Pulse (Chi Mai - 迟脉):\n  - Rate: Less than 60 beats per minute (or less than 4 beats per breath of the practitioner).\n  - Indications: Cold patterns.\n  - Slow & forceful: Interior Excess Cold (cold congealing, food stagnation).\n  - Slow & weak: Interior Deficiency Cold (Yang Qi deficiency failing to warm and propel blood).\n  - Physiological note: Well-trained endurance athletes may exhibit normal physiological slow pulse.\n\n• Rapid Pulse (Shuo Mai - 数脉):\n  - Rate: Greater than 90–100 beats per minute (or more than 5 beats per breath).\n  - Indications: Heat patterns.\n  - Rapid & forceful/surging: Excess Full Heat (blazing fire, Yangming organ heat).\n  - Rapid & thin/thready: Deficiency Empty Heat (Yin deficiency with rising deficiency fire).",
        "consensus": "Primary pulse parameter determining the thermal nature (Cold vs Heat) of disease.",
        "variations": "A rapid pulse with extreme debility and cold limbs can signify False Heat, True Cold (extreme Yang collapse).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Slippery (Hua) vs Wiry (Xian)",
        "front": "Contrast the physical tactile sensations and clinical indications of the Slippery Pulse (Hua Mai) and Wiry Pulse (Xian Mai).",
        "back": "Tactile Sensation & Indications:\n• Slippery Pulse (Hua Mai - 滑脉):\n  - Sensation: Extremely smooth and rounded, sliding smoothly under fingers 'like pearls rolling on a porcelain basin' or 'greased ball bearings'.\n  - Indications:\n    1. Pathological: Phlegm accumulation, Dampness retention, Food stagnation, Excess interior heat.\n    2. Physiological: Normal in healthy pregnancy (after 1st month due to abundant Qi and Blood), and in vigorously healthy young adults.\n\n• Wiry / String-Taut Pulse (Xian Mai - 弦脉):\n  - Sensation: Straight, long, stiff, and taut under fingers, 'like pressing on the tuned string of a violin or guitar'. It pushes back firmly without yielding.\n  - Indications:\n    1. Liver and Gallbladder disharmonies (Liver Qi stagnation, Liver Fire, Liver Yang rising).\n    2. Pain syndromes (acute or chronic pain produces channel spasm).\n    3. Phlegm-rheum (Tan Yin) retention and malaria.",
        "consensus": "The two most prevalent pathological pulse shapes encountered in modern clinical practice.",
        "variations": "In elderly patients with severe arteriosclerosis, the pulse may feel artificially wiry due to hardened vessel walls.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies", "Maciocia Foundations"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Tight (Jin) vs Choppy (Se)",
        "front": "Contrast the feel and clinical significance of the Tight Pulse (Jin Mai) and Choppy Pulse (Se Mai).",
        "back": "Tactile Sensation & Indications:\n• Tight Pulse (Jin Mai - 紧脉):\n  - Sensation: Taut, strong, vibrating, twisting under the fingers like a stretched twisted rope or cord.\n  - Indications: Severe Cold patterns (Cold contracts vessels), Severe acute pain (e.g. renal colic, acute lumbago), Food retention.\n  - Floating & tight = Exterior Wind-Cold (Shanghan Taiyang attack).\n  - Deep & tight = Interior Cold congealing.\n\n• Choppy / Hesitant Pulse (Se Mai - 涩脉):\n  - Sensation: Rough, uneven, hesitant, sluggish, 'like a light knife gently scraping bamboo' or 'water flowing over sand'. The opposite of slippery.\n  - Indications:\n    1. Choppy & forceful: Blood stasis, Qi stagnation, phlegm obstruction.\n    2. Choppy & weak/fine: Severe Blood deficiency, Essence exhaustion, body fluid depletion.",
        "consensus": "Key pulses indicating vascular contraction from cold/pain vs impaired blood fluidity from stasis/depletion.",
        "variations": "A choppy pulse is a definitive diagnostic marker for chronic blood stasis in gynecological and cardiovascular disorders.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Irregular Pulses: Knotted (Jie), Hurried (Cu), Intermittent (Dai)",
        "front": "Differentiate the three classic arrhythmic pulses: Knotted (Jie Mai), Hurried (Cu Mai), and Intermittent (Dai Mai).",
        "back": "Comparison of Irregular Pulses:\n• Knotted Pulse (Jie Mai - 结脉):\n  - Rate: Slow rate.\n  - Rhythm: Irregularly irregular missing beats (stops at irregular, unpredictable intervals).\n  - Indications: Yin excess, Cold congealing Qi/Blood, Phlegm-Blood stasis, Heart Qi/Yang deficiency.\n\n• Hurried / Abrupt Pulse (Cu Mai - 促脉):\n  - Rate: Rapid rate.\n  - Rhythm: Irregularly irregular missing beats (rapid pulse that halts unpredictably).\n  - Indications: Blazing Yang Heat, Excess fire, Phlegm-Heat, Heart Blood stasis.\n\n• Intermittent Pulse (Dai Mai - 代脉):\n  - Rate: Regularly irregular missing beats (stops after a fixed, predictable number of beats, e.g. every 3rd or 4th beat, with long pauses).\n  - Indications: Severe exhaustion of Zang-organ Qi (especially Heart and Spleen), severe heart damage, traumatic injury with severe pain/fright.",
        "consensus": "Essential pulse differentiation for cardiac arrhythmias and organ collapse.",
        "variations": "Western biomedical correlation: Atrial fibrillation (Cu/Jie), Premature Ventricular Contractions / Bigeminy (Dai).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies"])
    },
    {
        "category": "Diagnosis",
        "title": "Eight Principles (Ba Gang - 八纲辨证)",
        "front": "List the Eight Principles and explain how they form four complementary pairs to categorize all diseases.",
        "back": "The Eight Principles (Ba Gang):\n1. Location: Exterior (Biao - 表) vs Interior (Li - 里).\n   - Determines whether pathogen is on superficial skin/muscles or has penetrated the Zang-Fu organs.\n2. Nature: Cold (Han - 寒) vs Heat (Re - 热).\n   - Determines thermal character: Cold slows, contracts, chills (pale, slow pulse); Heat speeds, expands, burns (red, rapid pulse).\n3. Condition / Strength: Deficiency (Xu - 虚) vs Excess (Shi - 实).\n   - Determines balance between vital Zheng Qi and pathogenic Xie Qi: Deficiency = weakness of Zheng Qi; Excess = strength of Xie Qi.\n4. General Category: Yin (阴) vs Yang (阳).\n   - Master categorization: Interior, Cold, Deficiency = YIN; Exterior, Heat, Excess = YANG.",
        "consensus": "The master overarching diagnostic framework of Traditional Chinese Medicine.",
        "variations": "True Cold with False Heat, and True Heat with False Cold occur in severe or late-stage collapse.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Liver Patterns: Qi Stagnation vs Yang Rising vs Liver Fire",
        "front": "Differentiate Liver Qi Stagnation, Liver Yang Rising, and Liver Fire Blazing by symptoms, tongue, and pulse.",
        "back": "Differential Comparison:\n• Liver Qi Stagnation (Gan Qi Yu Jie - 肝气郁结):\n  - Symptoms: Hypochondriac distension, frequent sighing, moodiness, irritability, plum-pit throat (globus), PMS, breast distension, irregular menses.\n  - Tongue: Normal or slightly red edges with thin white coat.\n  - Pulse: Wiry (Xian).\n\n• Liver Yang Rising (Gan Yang Shang Kang - 肝阳上亢):\n  - Symptoms: Throbbing temporal headache, dizziness, tinnitus, red face, anger, insomnia, lower back/knee weakness (underlying Yin def).\n  - Tongue: Red body, especially lateral edges; thin coat.\n  - Pulse: Wiry and rapid, or wiry-thin.\n\n• Liver Fire Blazing (Gan Huo Shang Yan - 肝火上炎):\n  - Symptoms: Severe burning headache, bloodshot eyes, extreme thirst, bitter taste in mouth, tinnitus like ocean waves, dark yellow urine, constipation, epistaxis.\n  - Tongue: Red or crimson body with thick yellow dry coat.\n  - Pulse: Wiry, rapid, and forcefully full (Shi).",
        "consensus": "Critical ladder of Liver pathology from simple stagnation to deficient rising to rampant fire.",
        "variations": "Liver Yang Rising is a root-deficiency, branch-excess pattern (Kidney/Liver Yin def root); Liver Fire is pure excess.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Foundations"])
    },
    {
        "category": "Diagnosis",
        "title": "Spleen Patterns: Qi Deficiency vs Qi Sinking vs Not Controlling Blood",
        "front": "Distinguish between Spleen Qi Deficiency, Spleen Qi Sinking, and Spleen Failing to Control Blood.",
        "back": "Differential Comparison:\n• Spleen Qi Deficiency (Pi Qi Xu - 脾气虚):\n  - Core Symptoms: Poor appetite, abdominal bloating worse after meals, fatigue, loose stools, sallow complexion, limb weakness.\n  - Tongue: Pale, swollen with teeth marks, thin white coat.\n  - Pulse: Weak (Ruo) or Deficient (Xu), especially in middle position.\n\n• Spleen Qi Sinking (Pi Xu Xia Xian - 脾虚下陷):\n  - Core Symptoms: Spleen Qi deficiency symptoms PLUS bearing-down sensation in abdomen, organ prolapse (uterus, stomach, rectum, bladder), chronic watery diarrhea, dizziness from clear Yang failing to ascend.\n  - Tongue: Pale with teeth marks; Pulse: Weak, soft, thready.\n\n• Spleen Failing to Control Blood (Pi Bu Tong Xue - 脾不统血):\n  - Core Symptoms: Spleen Qi deficiency symptoms PLUS chronic bleeding (petechiae, purpura, blood in stool, menorrhagia, flooding and trickling) with pale, thin blood.\n  - Tongue: Very pale; Pulse: Thin, weak, thready.",
        "consensus": "Progressive manifestations of Spleen Qi impairment in digestion, ascension, and vascular containment.",
        "variations": "Bleeding from Spleen deficiency is pale and watery; bleeding from Blood Heat is profuse, bright red or purple.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Kidney Patterns: Kidney Yin Deficiency vs Kidney Yang Deficiency",
        "front": "Contrast Kidney Yin Deficiency and Kidney Yang Deficiency by clinical presentation, thermal signs, tongue, and pulse.",
        "back": "Differential Comparison:\n• Kidney Yin Deficiency (Shen Yin Xu - 肾阴虚):\n  - Thermal Nature: Empty Heat (insufficient water to cool fire).\n  - Symptoms: Sore weak lumbar/knees, dizziness, tinnitus, five-palm heat (heat in palms, soles, chest), night sweats (Dao Han), tidal afternoon fever, malar flush, dry mouth, nocturnal emissions with erotic dreams.\n  - Tongue: Red body, dry, little or no coating (peeled), transverse cracks.\n  - Pulse: Thin (Xi) and Rapid (Shuo), weak at proximal (Chi) position.\n\n• Kidney Yang Deficiency (Shen Yang Xu - 肾阳虚):\n  - Thermal Nature: Deficiency Cold (insufficient Mingmen fire to warm body).\n  - Symptoms: Cold lower back and knees, aversion to cold, cold limbs, pale complexion, impotence, premature ejaculation, clear profuse urination, nocturia, dawn diarrhea (cock-crow diarrhea), lower limb edema.\n  - Tongue: Pale, swollen, wet with thin white coating.\n  - Pulse: Deep (Chen), Slow (Chi), and Weak (Ruo), particularly in right proximal position.",
        "consensus": "The fundamental dichotomy of constitutional pre-heaven deficiency in Chinese medicine.",
        "variations": "Long-standing Yin deficiency damages Yang, and chronic Yang deficiency depletes Yin, resulting in Kidney Yin and Yang Dual Deficiency.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Foundations of Chinese Medicine"])
    },
    {
        "category": "Diagnosis",
        "title": "Six Stages (Shanghan Lun): Progression from Taiyang to Jueyin",
        "front": "Outline the Six Stages (Liu Jing Bian Zheng) of exogenous cold invasion in order, noting key symptoms for each stage.",
        "back": "The Six Stages (Shanghan Lun):\n1. Taiyang: Most superficial stage (Bladder & Small Intestine).\n   - Taiyang Zhong Feng (Wind attack): Aversion to wind, sweating, floating moderate pulse.\n   - Taiyang Shang Han (Cold attack): Aversion to cold, no sweating, severe headache, body aches, floating tight pulse.\n2. Yangming: Interior full heat stage (Stomach & Large Intestine).\n   - Four Bigs: Big fever, Big sweat, Big thirst, Big pulse. No aversion to cold, aversion to heat.\n3. Shaoyang: Half-interior, half-exterior (Gallbladder & Sanjiao).\n   - Alternating chills and fever, hypochondriac fullness, bitter taste in mouth, dry throat, blurry vision, wiry pulse.\n4. Taiyin: Greater Yin stage (Spleen deficiency cold).\n   - Abdominal fullness, vomiting, diarrhea, abdominal pain relieved by warmth/pressure, pale tongue, slow weak pulse.\n5. Shaoyin: Lesser Yin stage (Heart & Kidney collapse).\n   - Shaoyin Cold: Extreme aversion to cold, curled posture, cold limbs, diarrhea with undigested food, faint minute pulse.\n   - Shaoyin Heat: Insomnia, dry mouth, red tongue tip, thin rapid pulse.\n6. Jueyin: Terminal Yin stage (Liver & Pericardium - extreme disharmony of Yin and Yang).\n   - Heat above, cold below: Thirst, gas/heat rushing to heart, hunger without desire to eat, vomiting of roundworms, cold extremities.",
        "consensus": "The classical Han Dynasty cold-pathogen staging framework established by Zhang Zhongjing.",
        "variations": "Transmission can skip stages (Chuan Jing) or attack interior directly (Zhi Zhong).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Zhang Zhongjing Shanghan Lun"])
    },
    {
        "category": "Diagnosis",
        "title": "Four Levels (Wenbing): Wei, Qi, Ying, Xue",
        "front": "Outline the Four Levels of warm disease progression (Wen Bing Bian Zheng) from superficial to deep.",
        "back": "The Four Levels (Wenbing):\n1. Wei Level (Defensive Level):\n   - Pathogen on exterior (skin, hair, lungs).\n   - Symptoms: Fever, slight aversion to wind/cold, sore throat, cough, sweating, floating rapid pulse, red tongue tip/edges with thin white coat.\n2. Qi Level (Interior Heat Level):\n   - Pathogen entered interior organs; vital Qi fights vigorously.\n   - Symptoms: High fever without chills, profuse sweat, intense thirst, dark urine, red tongue with thick yellow coat, rapid forceful pulse (Four Bigs).\n3. Ying Level (Nutritive Level):\n   - Pathogen invades deep body fluids and begins disturbing the Pericardium/Shen.\n   - Symptoms: Fever worse at night, restlessness, insomnia, delirium, dry mouth with little desire to drink, crimson/deep red tongue with peeled coat, thready rapid pulse.\n4. Xue Level (Blood Level):\n   - Deepest, most critical level; heat scorches blood vessels and stirs wind.\n   - Symptoms: High nocturnal fever, mania, delirium, convulsions (wind), macular skin eruptions (petechiae/purpura), bleeding from orifices (hematemesis, epistaxis, bloody stools), dark crimson or purple tongue with no coat.",
        "consensus": "Qing Dynasty framework established by Ye Tianshi for febrile infectious diseases.",
        "variations": "Ying level affects the mind (restlessness/delirium); Xue level affects blood extravasation (hemorrhage/purpura) and internal wind.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Ye Tianshi Wen Re Lun"])
    },
    {
        "category": "Diagnosis",
        "title": "Radial Pulse Positions: Cun, Guan, Chi Organ Correspondence",
        "front": "State the anatomical positions of Cun, Guan, and Chi on both wrists and their corresponding internal Zang-Fu organs.",
        "back": "Radial Pulse Positions & Organ Correspondence:\n• Anatomical Locations:\n  - Guan (Bar): Opposite the radial styloid process.\n  - Cun (Inch): Distal to the radial styloid process (closest to the wrist crease).\n  - Chi (Cubit): Proximal to the radial styloid process (towards the elbow).\n\n• Left Wrist Organ Correspondence:\n  - Left Cun (Inch): Heart (superficial: Small Intestine).\n  - Left Guan (Bar): Liver (superficial: Gallbladder).\n  - Left Chi (Cubit): Kidney Yin (superficial: Urinary Bladder).\n\n• Right Wrist Organ Correspondence:\n  - Right Cun (Inch): Lung (superficial: Large Intestine).\n  - Right Guan (Bar): Spleen (superficial: Stomach).\n  - Right Chi (Cubit): Kidney Yang / Mingmen (superficial: Sanjiao).",
        "consensus": "Universal standard of 3-position radial pulse palpation codified in Nan Jing.",
        "variations": "Some classical lineages place pericardium at Left Cun and abdomen/intestines at both Chi positions.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Nan Jing Chapter 18", "Li Shizhen Pulse Studies"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Empty (Xu) vs Full (Shi)",
        "front": "Contrast the tactile feel and clinical significance of the Empty/Deficient Pulse (Xu Mai) versus Full/Excess Pulse (Shi Mai).",
        "back": "Tactile Sensation & Indications:\n• Empty / Deficient Pulse (Xu Mai - 虚脉):\n  - Sensation: Feels relatively large and soft on superficial palpation, but yields and feels completely hollow, empty, and weak under heavier pressure.\n  - Indications: General deficiency of Qi and Blood.\n  - Reflection: Zheng Qi is depleted; cannot fill or sustain the blood vessels.\n\n• Full / Excess Pulse (Shi Mai - 实脉):\n  - Sensation: Big, hard, long, and forceful at ALL THREE depths (superficial, middle, and deep); resists finger pressure vigorously.\n  - Indications: Excess Full patterns (Excess Heat, Phlegm accumulation, severe Food retention, Qi/Blood stagnation).\n  - Reflection: Both Zheng Qi and pathogenic Xie Qi are fighting aggressively.",
        "consensus": "Fundamental baseline parameter assessing the strength of vital Qi versus pathogen.",
        "variations": "An empty pulse in a severe fever indicates that the pathogen is overwhelming an exhausted body.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies"])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Thready (Xi) vs Surging (Hong)",
        "front": "Compare the sensation and clinical indications of the Thready/Fine Pulse (Xi Mai) and Surging/Flooding Pulse (Hong Mai).",
        "back": "Tactile Sensation & Indications:\n• Thready / Fine Pulse (Xi Mai - 细脉 / 微脉):\n  - Sensation: Extremely thin, narrow, and delicate like a fine silk thread under the finger, but clear and distinct.\n  - Indications: Deficiency of Blood, Deficiency of Yin, or Internal Dampness encumbering vessels.\n  - Reflection: Insufficient blood to fill the vessel diameter.\n\n• Surging / Flooding Pulse (Hong Mai - 洪脉):\n  - Sensation: Extremely broad, large, and overflowing, arriving with tremendous force like 'ocean waves crashing ashore', and departing with diminishing force.\n  - Indications: Extreme Full Heat at the Qi level (Yangming heat), summer-heat.\n  - Accompanies the Four Bigs: Big fever, big sweat, big thirst, big surging pulse.",
        "consensus": "Hallmark pulse indicators for volume depletion/Yin deficiency vs raging interior heat.",
        "variations": "A thready and rapid pulse is the classic signature of Kidney Yin deficiency with empty heat.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies", "CAM 3rd Ed."])
    },
    {
        "category": "Diagnosis",
        "title": "Classic Pulses: Soggy (Ru) vs Weak (Ruo)",
        "front": "Differentiate between the Soggy/Soft Pulse (Ru Mai) and the Weak Pulse (Ruo Mai).",
        "back": "Tactile Sensation & Indications:\n• Soggy / Soft Pulse (Ru Mai - 濡脉 / 软脉):\n  - Depth & Feel: Felt SUPERFICIALLY; extremely soft, floating, fine, and spongy, 'like a thread floating on water' or 'a piece of wet cotton wool'; disappears when pressed deeply.\n  - Indications: Dampness retention combined with Qi deficiency, or Essence depletion.\n  - Mechanism: Spleen deficiency produces dampness, which floats upward and makes vessels soft.\n\n• Weak Pulse (Ruo Mai - 弱脉):\n  - Depth & Feel: Felt only DEEPLY near the bone; extremely thin, soft, and lacking force; cannot be felt on the surface.\n  - Indications: Dual Deficiency of both Qi and Blood, or Yang deficiency.\n  - Mechanism: Insufficient Yang Qi to raise the pulse to the surface, and insufficient Blood to fill the vessel.",
        "consensus": "Key distinction: Soggy is superficial and indicates dampness; Weak is deep and indicates Qi/Blood deficiency.",
        "variations": "Ru Mai is frequently felt in gastrointestinal disorders involving summer dampness or Spleen dampness.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Li Shizhen Pulse Studies"])
    },
    {
        "category": "Diagnosis",
        "title": "Heart Patterns: Heart Blood Deficiency vs Heart Yin Deficiency",
        "front": "Differentiate Heart Blood Deficiency from Heart Yin Deficiency by symptoms, thermal signs, tongue, and pulse.",
        "back": "Differential Comparison of Heart Patterns:\n• Heart Blood Deficiency (Xin Xue Xu - 心血虚):\n  - Common Symptoms: Palpitations, dizziness, insomnia, dream-disturbed sleep, poor memory, anxiety, easily startled.\n  - Specific Deficiency Signs: Pale dull complexion, pale lips, no heat signs.\n  - Tongue: Pale body, thin white coat.\n  - Pulse: Thin (Xi) and Weak (Ruo).\n\n• Heart Yin Deficiency (Xin Yin Xu - 心阴虚):\n  - Common Symptoms: Palpitations, insomnia, dream-disturbed sleep, poor memory, anxiety.\n  - Specific Empty Heat Signs: Five-palm heat, tidal fever, night sweats, malar flush, dry mouth and throat, restlessness.\n  - Tongue: Red body (especially red tip with red prickles/dots), dry, little or no coating.\n  - Pulse: Thin (Xi) and Rapid (Shuo).",
        "consensus": "Core cardiovascular/psycho-emotional pattern differentiation in TCM.",
        "variations": "Heart Yin deficiency represents a deeper depletion with internal heat disturbing the Shen.",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Maciocia Foundations"])
    },
    {
        "category": "Diagnosis",
        "title": "San Jiao Pattern Differentiation (Upper, Middle, Lower Jiao)",
        "front": "Outline the San Jiao Pattern Differentiation (San Jiao Bian Zheng) developed by Wu Jutong for warm-damp febrile diseases.",
        "back": "San Jiao Pattern Differentiation (Wu Jutong - 温病条辨):\n1. Upper Jiao (Shang Jiao - Lung & Pericardium):\n   - Pathogen attacks head, throat, chest, lungs, and pericardium.\n   - Symptoms: Fever, chills, headache, cough, sore throat, or heat penetrating pericardium (delirium, slurred speech, crimson tongue).\n\n2. Middle Jiao (Zhong Jiao - Spleen & Stomach):\n   - Pathogen lodges in the digestive organs.\n   - Yangming Heat: High fever, profuse sweating, constipation, dry mouth, red tongue, forceful pulse.\n   - Taiyin Damp-Heat: Heaviness of head/body, epigastric fullness, nausea, sticky yellow coat, soggy pulse.\n\n3. Lower Jiao (Xia Jiao - Kidney & Liver):\n   - Pathogen burns deep Yin fluids of Liver and Kidney in late stages.\n   - Symptoms: Low-grade continuous fever, flushed cheeks, five-palm heat, dry mouth, hearing loss, trembling limbs/convulsions (wind from Yin collapse), crimson peeled tongue, thin rapid or floating empty pulse.",
        "consensus": "Qing Dynasty warm-disease framework for evaluating vertical depth and anatomical progression of febrile diseases.",
        "variations": "Upper Jiao is like a mist (disperses); Middle Jiao is like a foam (macerates); Lower Jiao is like a drain (discharges).",
        "sources": json.dumps(["Royal TCM TCM-02 Diagnostics", "Wu Jutong Wen Bing Tiao Bian"])
    }
]

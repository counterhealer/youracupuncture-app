"""Paediatrics Flashcards (25 high-yield clinical cards).

Covers physiological and pathological characteristics of children,
index finger vein inspection (Xiao Er Zhi Wen), crying & fontanelle diagnosis,
acute/chronic convulsions, pediatric diarrhea, malnutrition (Gan syndrome & Sifeng),
enuresis, pediatric needling safety & fontanelle cautions, and Xiao Er Tui Na.
All points strictly use bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS = [
    {
        "category": "Paediatrics",
        "title": "Pediatric Physiology: 'Pure Yang' and 'Delicate Zang-Fu'",
        "front": "Explain the classic physiological principles of 'Pure Yang' (Chun Yang) and 'Delicate Zang-Fu' (Zang Fu Jiao Nen) in traditional Chinese paediatrics.",
        "back": "Classic Pediatric Physiology Principles:\n• 'Pure Yang' (Chun Yang - 纯阳):\n  - Meaning: Does NOT mean children have excess fire or fever. It signifies rapid growth, vigorous vitality, and dynamic developmental potential ('like the rising sun' or 'sprouting plant').\n  - Yang Qi is abundant and active, driving rapid physical, cognitive, and cellular development.\n\n• 'Delicate Zang-Fu, Immature Qi' (Zang Fu Jiao Nen, Xing Qi Wei Chong - 脏腑娇嫩，形气未充):\n  - Meaning: Anatomical structures and physiological organ functions are tender, fragile, and not yet fully matured.\n  - Three Particularly Vulnerable Organs:\n    1. Spleen is naturally insufficient (Pi Chang Bu Zu): Digestive system is weak, easily injured by improper feeding, overeating, or cold foods.\n    2. Lung is naturally delicate (Fei Chang Bu Zu): Defensive (Wei) Qi is weak, easily attacked by exterior wind-cold and wind-heat.\n    3. Kidney is naturally underdeveloped (Shen Chang Bu Zu): Pre-heaven Jing and bones/teeth/marrow are still forming.\n  - Two Naturally Abundant Organs:\n    1. Liver naturally has excess Qi (Gan Chang You Yu): Easily frightened, prone to high-fever convulsions and wind.\n    2. Heart naturally has excess Fire (Xin Chang You Yu): Easily agitated, sensitive Shen, prone to night terrors.",
        "consensus": "The cornerstone physiological doctrine formulated by Ming Dynasty pediatrician Wan Quan.",
        "variations": "Because Spleen, Lung, and Kidney are inherently delicate in children, treatment must always protect Post-Heaven digestion and avoid harsh purging.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Wan Quan Yu Ying Jia Mi", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Pathology: 'Rapid Onset and Rapid Transformation'",
        "front": "Describe the classic pathological characteristics of children: 'Rapid onset and transformation' (Fa Bing Rong Yi, Chuan Bian Xun Su) and 'Quick recovery' (Yi Qu Kang Fu).",
        "back": "Pediatric Pathological Characteristics:\n• Easily Contracted Disease (Fa Bing Rong Yi - 发病容易):\n  - Because defensive Qi and digestive power are tender, children fall ill quickly upon minor exposure to external pathogens or dietary errors.\n\n• Rapid Transmission and Transformation (Chuan Bian Xun Su - 传变迅速):\n  - Pathogens penetrate rapidly without lingering on the exterior:\n    1. Easily transforms into Heat (Han Yi Hua Re): A simple wind-cold attack can transform into interior blazing heat within hours.\n    2. Easily generates Phlegm (Yi Sheng Tan): Delicate lungs and spleen quickly produce copious bronchial phlegm.\n    3. Easily stirs Wind (Yi Dong Feng): High fever easily crosses into the Liver channel, precipitating febrile seizures (convulsions).\n    4. Easily leads to sudden collapse (Yi Zhi Tuo): Severe vomiting/diarrhea rapidly produces life-threatening dehydration and fluid/Yang collapse.\n\n• Quick Recovery (Zang Qi Qing Ling, Yi Qu Kang Fu - 脏气清灵，易趋康复):\n  - Positive Counterpart: Children's vital Qi is pure and free of chronic emotional blockages or decades of toxic accumulation. Once the correct treatment is administered, recovery is exceptionally fast and complete.",
        "consensus": "Explains why pediatric illnesses escalate into emergencies rapidly, but also resolve with remarkable speed.",
        "variations": "Requires vigilant monitoring of infant vital signs, hydration, and fever spikes.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Wan Quan Pediatric Classics"])
    },
    {
        "category": "Paediatrics",
        "title": "Xiao Er Zhi Wen: Index Finger Superficial Vein Inspection",
        "front": "Detail the Three Bars (Feng, Qi, Ming) and color differentiation used in Index Finger Vein Inspection (Xiao Er Zhi Wen) for infants under 3 years old.",
        "back": "Index Finger Vein Inspection (小儿指纹) [Children under 3 years]:\n• Technique: Practitioner holds the child's index finger and gently strokes the radial aspect with thumb from the distal tip towards the palm, observing the superficial venule.\n\n• The Three Bars (San Guan - 三关) [Location & Severity]:\n  1. Wind Bar (Feng Guan - 风关): Proximal phalanx (closest to palm). Indicates mild, superficial disease; pathogen is on exterior.\n  2. Qi Bar (Qi Guan - 气关): Middle phalanx. Indicates deeper, interior disease; pathogen has entered the Zang-Fu organs.\n  3. Life Bar (Ming Guan - 命关): Distal phalanx (near fingernail). Indicates severe, critical, life-threatening disease.\n  - Vein passing through Ming Guan to tip of nail ('Tou Guan She Jia' - 透关射甲): Imminent danger, extreme emergency.\n\n• Color Differentiation:\n  - Red (Fresh Red): Exterior Cold pattern.\n  - Purple: Interior Heat pattern.\n  - Blue / Dark Blue: Liver Wind, Fright, Severe Pain, Convulsions.\n  - Pale / Light: Deficiency pattern (Qi and Blood deficiency).\n  - Black / Dark Purple: Severe Blood Stasis, critical toxin.\n\n• Depth & Shape:\n  - Superficial / Visible: Exterior pattern; Deep / Submerged: Interior pattern.\n  - Straight / Fine: Mild disease; Bent / Distended / Branched: Severe pathology.",
        "consensus": "Classic diagnostic method substituting for radial pulse palpation in uncooperative infants under 3 years.",
        "variations": "Radial pulse examination in infants is unreliable due to rapid heart rate and emotional agitation; finger venule inspection directly reflects peripheral circulation.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed.", "Maciocia Foundations"])
    },
    {
        "category": "Paediatrics",
        "title": "Fontanelle Observation: Bulging vs Sunken vs Delayed Closure",
        "front": "Interpret what Bulging Fontanelle, Sunken Fontanelle, and Delayed Fontanelle Closure indicate in pediatric pathology.",
        "back": "Observation of Fontanelles (Wang Xin Men - 望囟门):\n• Normal Development:\n  - Anterior fontanelle normally closes between 12 and 18 months of age.\n  - Posterior fontanelle normally closes between 2 and 4 months.\n\n• Bulging Fontanelle (Xin Tian Gao Tu - 囟填 / Elevated Fontanelle):\n  - Presentation: Anterior fontanelle is tense, raised, full, and pulsating vigorously.\n  - Indicates: Excess Heat fire, Fire-Toxin blazing, Phlegm-Heat covering the orifices, or intracranial pressure (meningitis, encephalitis).\n  - Urgent western medical emergency referral.\n\n• Sunken Fontanelle (Xin Xian Ao Ao - 囟陷 / Depressed Fontanelle):\n  - Presentation: Anterior fontanelle is deeply pitted or sunken below surrounding cranial bones.\n  - Indicates: Severe dehydration and fluid depletion from profuse vomiting/diarrhea, or extreme exhaustion of Spleen/Kidney Yuan Qi.\n\n• Delayed Fontanelle Closure (Jie Lu - 解颅 / Open Skull):\n  - Presentation: Fontanelle remains open and wide past 2 years of age, accompanied by enlarged head, poor bone formation.\n  - Indicates: Congenital Kidney Essence (Jing) Deficiency, Rickets, or hydrocephalus.",
        "consensus": "Crucial cranial inspection in all pediatric assessments under 2 years of age.",
        "variations": "NEVER needle points directly over or adjacent to open fontanelles (DU22 Xinhui is strictly contraindicated until fontanelle is ossified).",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Royal TCM COM-06 Safety Handbook"])
    },
    {
        "category": "Paediatrics",
        "title": "Acute Infantile Convulsions (Ji Jing Feng): Emergency Protocol",
        "front": "What are the clinical manifestations of Acute Infantile Convulsions (Ji Jing Feng) and the emergency acupuncture rescue protocol?",
        "back": "Acute Infantile Convulsions (急惊风 - Febrile Seizures / Encephalitis):\n• Four Cardinal Signs (Si Zheng):\n  1. Heat (Re): High fever (frequently > 39.5°C / 103°F).\n  2. Phlegm (Tan): Stertorous breathing with rattling phlegm, foaming at the mouth.\n  3. Fright (Jing): Agitation, fear, night screaming preceding convulsions.\n  4. Wind (Feng): Upward gazing eyes (strabismus/nystagmus), trismus (clenched teeth), sudden loss of consciousness, opisthotonos, tetanic muscle spasms of extremities.\n\n⚠️ Emergency Acupuncture Rescue Protocol:\n• Goal: Clear heat, extinguish wind, unblock orifices, stop spasms.\n• Primary Emergency Points:\n  - DU26 (Shuigou / 水沟): Puncture obliquely upward 0.3–0.5 cun with vigorous reducing method, or pinch firmly with thumbnail to restore consciousness.\n  - Shixuan (EX-UE11 / Ten Fingertips): Prick with three-edged needle to express 1–2 drops of blood from each fingertip to rapidly purge toxic heat.\n  - LV3 (Taichong / 太冲) + LI4 (Hegu / 合谷): The Four Gates, to extinguish internal wind and stop spasms.\n  - DU20 (Baihui / 百会) + Yintang (印堂): Calms the Shen and pacifies wind.\n  - ST40 (Fenglong / 丰隆): Resolves phlegm clouding the sensory orifices.\n\n• Emergency Medical Management: Ensure open airway, prevent aspiration (turn to side), do not insert objects between clenched teeth, monitor temperature, call 911.",
        "consensus": "DU26 and Shixuan bleeding are universal emergency interventions for acute pediatric febrile convulsions.",
        "variations": "Chronic Infantile Convulsions (Man Jing Feng) presents with low fever, pale face, feeble twitching, and requires moxa and tonification of Spleen/Kidney Yang.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Malnutrition (Gan Ji / Gan Syndrome) & Sifeng (EX-UE10)",
        "front": "Describe the clinical features of Pediatric Malnutrition (Gan Ji) and the specialized pricking technique at Sifeng (EX-UE10).",
        "back": "Pediatric Malnutrition (疳积 - Gan Syndrome / Food Accumulation):\n• Clinical Features:\n  - Chronic emaciation, withered dry skin, protruding distended abdomen ('potbelly with thin limbs'), visible superficial abdominal veins, voracious yet abnormal appetite (pica: eating dirt, paper, raw rice), irritability, restless sleep, teeth grinding.\n  - Etiology: Severe damage to Spleen and Stomach from chronic improper feeding, overfeeding sweets/grease, or intestinal parasites.\n\n• Specialized Pricking Technique at Sifeng (EX-UE10 - 四缝 / Four Seams):\n  - Location: On the palmar surface, in the transverse creases of the proximal interphalangeal (PIP) joints of the 2nd, 3rd, 4th, and 5th fingers (bilateral, 8 points total).\n  - Technique: Disinfect skin thoroughly with 70% alcohol. Prick each point 0.1 - 0.2 cun with a sterile disposable lancet.\n  - Squeeze firmly to express a few drops of yellowish-white, translucent, sticky, viscous lymphatic fluid (or a drop of blood) until clear serum or blood emerges. Wipe clean with sterile cotton ball.\n  - Repeat once or twice weekly for 3 to 5 treatments.\n  - Mechanism: Powerfully fortifies Spleen, harmonizes middle jiao, dissolves food accumulation, and eliminates childhood Gan accumulation.",
        "consensus": "Sifeng pricking is the single most celebrated empirical treatment in Chinese pediatric medicine worldwide.",
        "variations": "The more turbid and copious the yellowish fluid expressed, the more severe the food accumulation and the greater the therapeutic response.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Needling Safety: Non-Retention & Fontanelle Rules",
        "front": "State the special needle gauges, insertion techniques, retention rules, and fontanelle safety laws for pediatric acupuncture.",
        "back": "Pediatric Needling Safety Rules:\n• Needle Gauge & Selection:\n  - Use ultra-fine, flexible needles: 36 to 40 gauge (0.18 mm to 0.16 mm), short lengths (0.5 cun / 13 mm).\n\n• Flying Needle Technique (Fei Zhen - 飞针 / Non-Retention Method):\n  - For infants and children under 3–5 years: Needles are NOT retained.\n  - Technique: Rapid insertion, immediate gentle twirling to elicit mild de qi sensation, and instantaneous withdrawal ('Fast in, fast out').\n  - Children are easily frightened and cannot remain still; retained needles bend, break, or cause severe emotional trauma.\n  - For older children (6–12 years): Short retention of 5 to 10 minutes maximum while parent stays present.\n\n⚠️ Fontanelle Safety Laws:\n• NEVER puncture points directly over or immediately adjacent to unclosed fontanelles (DU22 Xinhui is strictly contraindicated in infants under 2 years).\n• Needling an open fontanelle risks direct penetration of the sagittal sinus and cerebral cortex, causing intracranial hemorrhage and death.\n• Avoid heavy electrical stimulation; minimize needle quantity (2 to 4 points maximum per session).",
        "consensus": "Zero needle retention and strict avoidance of open fontanelles are mandatory universal pediatric standards.",
        "variations": "For very young infants, non-invasive Pediatric Tuina (Xiao Er Tui Na) is strongly preferred over filiform acupuncture needles.",
        "sources": json.dumps(["Royal TCM COM-06 Safety Handbook", "Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Xiao Er Tui Na: Five Core Pediatric Massage Techniques",
        "front": "Describe the location, massage technique, and indications for Push Tianmen, Push Kangong, Knead Taiyang, Clear Tianheshui, and Push Banmen.",
        "back": "Core Pediatric Tuina Points & Manipulations (小儿推拿):\n1. Push Tianmen (Tui Tian Men - 推天门):\n   - Location: From Yintang (midpoint between eyebrows) straight up along the midline to anterior hairline.\n   - Technique: Use both thumbs to push alternately straight upward 50–100 times.\n   - Actions: Expels wind, clears head, relieves fever, calms the Shen, relieves fright.\n\n2. Push Kangong (Tui Kan Gong - 推坎宫):\n   - Location: Along the eyebrow arches from inner brow to outer brow (Taiyang).\n   - Technique: Push with both thumbs outward from inner canthus along eyebrows 50–100 times.\n   - Actions: Relieves fever, clears headache, soothes eye inflammation.\n\n3. Knead Taiyang (Rou Tai Yang - 揉太阳):\n   - Location: In the temples.\n   - Technique: Knead gently in circular motion 50–100 times.\n   - Actions: Expels wind, relieves headache, stops convulsions.\n\n4. Clear Tianheshui (Qing Tian He Shui - 清天河水):\n   - Location: On the anterior forearm, from the transverse wrist crease straight up the midline to the cubital crease.\n   - Technique: Use index and middle fingers to push straight upward from wrist to elbow 100–300 times.\n   - Actions: The PREMIER pediatric technique for clearing Heart fire, reducing high fevers, and soothing night crying.\n\n5. Push Banmen (Tui Ban Men - 推板门):\n   - Location: On the thenar eminence of the palm.\n   - Technique: Rub or knead with thumb 100–200 times.\n   - Actions: Harmonizes Spleen and Stomach, resolves food accumulation, stops vomiting and diarrhea.",
        "consensus": "The most widely practiced non-invasive pediatric therapeutic system in Chinese medicine.",
        "variations": "Tianheshui: Pushing from wrist to elbow cools fever; pushing from elbow to wrist warms interior cold.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Xiao Er Tui Na Handbook", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Enuresis (Bedwetting): Kidney vs Spleen/Lung Deficiency",
        "front": "Differentiate Pediatric Enuresis (Xiao Er Yi Niao) between Kidney Qi Deficiency and Lung/Spleen Qi Deficiency, detailing point prescriptions.",
        "back": "Differential Comparison of Pediatric Enuresis (小儿遗尿 - Bedwetting):\n• Definition: Involuntary urination during sleep in children aged 3–5 years and older.\n\n• Kidney Qi Deficiency (Shen Qi Bu Zu):\n  - Symptoms: Frequent involuntary nocturnal bedwetting, waking up after wetting bed, copious pale urine, cold limbs, pale complexion, sore lower back, poor bone development, pale tongue with thin white coat, deep weak pulse.\n  - Treatment Principle: Tonify Kidney Qi, warm Mingmen, astringe urine.\n  - Primary Points: BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), REN4 (Guanyuan / 关元), KI3 (Taixi / 太溪), SP6 (Sanyinjiao / 三阴交), with indirect moxibustion.\n\n• Lung and Spleen Qi Deficiency (Fei Pi Qi Xu):\n  - Symptoms: Bedwetting occurring during deep sleep, daytime urinary frequency or urgency, chronic fatigue, poor appetite, loose stools, spontaneous sweating, pale tongue with teeth marks, thin weak pulse.\n  - Treatment Principle: Fortify Spleen, boost Lung Qi, consolidate water passages.\n  - Primary Points: BL20 (Pishu / 脾俞), BL13 (Feishu / 肺俞), REN12 (Zhongwan / 中脘), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), DU20 (Baihui / 百会 - to raise sinking Qi).",
        "consensus": "Moxibustion over REN4 and BL23 is highly effective for pediatric nocturnal enuresis.",
        "variations": "In cases of Liver fire harassing the lower jiao, the child wets the bed with dark yellow smelly urine and exhibits temper tantrums (Point: LV2, SP9).",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Nie Ji (Pinching the Spine): Technique and Indications",
        "front": "Explain the technique, direction, and clinical indications for the pediatric spine pinching method Nie Ji (捏脊).",
        "back": "Spine Pinching Method (Nie Ji Fa - 捏脊疗法):\n• Patient Posture: Child lies prone with back fully exposed and relaxed.\n\n• Technique:\n  - Practitioner uses the radial sides of both index fingers and both thumbs to grasp, roll, and pinch the skin and subcutaneous tissue overlying the vertebral column.\n  - Starting Point: Begin at the coccyx / sacrum (Changqiang DU1 area).\n  - Progression: Squeeze and roll the skin upward along the Du Mai spine all the way to DU14 (Dazhui / 7th cervical vertebra).\n  - 'Pinch Three, Lift One' (San Nie Yi Ti): On the 3rd to 5th pass, gently lift the pinched fold of skin upward every 3rd step with an audible gentle snap.\n  - Perform 3 to 5 passes daily or every other day.\n\n• Actions & Indications:\n  - Powerfully stimulates the Governing Vessel (Du Mai) and bilateral inner Bladder lines (Back-Shu points of all Zang-Fu organs).\n  - Strengthens Spleen, harmonizes Stomach, boosts immunity, regulates digestion.\n  - Chief indication: Malnutrition (Gan syndrome), chronic poor appetite, recurring colds, enuresis, chronic diarrhea, and infant insomnia.",
        "consensus": "One of the most effective and beloved physical therapies in Chinese pediatric medicine.",
        "variations": "Contraindicated over areas of active skin infection, burns, or spinal deformities.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Xiao Er Tui Na Clinical Handbook"])
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Diarrhea (Xiao Er Xie Xie): Four Patterns",
        "front": "Differentiate Pediatric Diarrhea caused by Food Injury, Cold-Damp, Damp-Heat, and Spleen Deficiency.",
        "back": "Differential Comparison of Pediatric Diarrhea (小儿泄泻):\n• Food Injury Diarrhea (Shang Shi Xie - Most Common in Weaning):\n  - Stools: Foul, sour rotten smell like rotten eggs, containing curdled undigested milk or food lumps, accompanied by abdominal distension and pain relieved after stool.\n  - Tongue: Thick greasy coating; Treatment: Harmonize stomach, dissolve food stagnation (Points: Banmen tuina, REN12 Zhongwan, ST25 Tianshu, ST36 Zusanli).\n\n• Cold-Damp Diarrhea (Feng Han Xie):\n  - Stools: Watery, pale, frothy with little odor, accompanied by abdominal pain relieved by warmth, cold limbs, pale tongue with white coat.\n  - Treatment: Warm middle jiao, scatter cold (Points: Moxa on REN8 Shenque, ST25 Tianshu, ST36 Zusanli).\n\n• Damp-Heat Diarrhea (Shi Re Xie):\n  - Stools: Frequent explosive watery yellow stools with foul smell, burning erythema around anus, fever, thirst, dark scanty urine, yellow greasy coat.\n  - Treatment: Clear heat, resolve dampness (Points: Clear Tianheshui tuina, ST25 Tianshu, ST37 Shangjuxu, SP9 Yinlingquan).\n\n• Spleen Deficiency Diarrhea (Pi Xu Xie):\n  - Stools: Chronic loose stools containing undigested food grains occurring immediately after eating, pale sallow face, emaciation, fatigue.\n  - Treatment: Fortify Spleen, tonify Qi (Points: Nie Ji spine rolling, BL20 Pishu, ST36 Zusanli, SP3 Taibai).",
        "consensus": "Food injury from improper weaning is the most frequent trigger of acute pediatric diarrhea.",
        "variations": "Dehydration is rapid in infants; sunken fontanelle and dry lips demand immediate oral rehydration therapy.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed."])
    },
    {
        "category": "Paediatrics",
        "title": "Xiao Er Tui Na: Tui San Guan & Qing Liu Fu",
        "front": "Describe the location, manipulation, and clinical indications for Pushing the Three Passes (Tui San Guan) and Clearing the Six Fu (Qing Liu Fu).",
        "back": "Core Pediatric Tuina Manipulations:\n• Pushing the Three Passes (Tui San Guan - 推三关):\n  - Location: On radial border of forearm, straight line from transverse wrist crease to cubital crease (Yangming line).\n  - Manipulation: Use radial edge of thumb or index/middle fingers to push straight upward from wrist towards elbow 100–300 times.\n  - Action: Strongly warms Yang Qi, dispels cold, supplements Qi and Blood.\n  - Indications: Deficiency cold patterns, chronic diarrhea, aversion to cold, pale complexion, lack of sweat in exterior cold.\n\n• Clearing the Six Fu (Qing Liu Fu - 清六腑):\n  - Location: On ulnar border of forearm, straight line from cubital crease (elbow) down to transverse wrist crease.\n  - Manipulation: Use index and middle fingers to push straight downward from elbow towards wrist 100–300 times.\n  - Action: The PREMIER pediatric technique for clearing extreme excess interior heat, purging fire toxin, cooling blood, and reducing high fevers and constipation.\n  - Indications: High fever, restlessness, delirium, severe sore throat, dysentery, red face, thirst.\n\n• Clinical Symmetry: San Guan warms and tonifies upward; Liu Fu purges and cools downward.",
        "consensus": "The most famous pair of linear forearm manipulations in traditional pediatric tuina.",
        "variations": "Never apply Qing Liu Fu in cold deficiency patterns, as it is intensely cooling.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "Xiao Er Tui Na Clinical Handbook"])
    },
    {
        "category": "Paediatrics",
        "title": "Pediatric Night Crying (Ye Ti): Spleen Cold vs Heart Heat vs Fright",
        "front": "Differentiate Pediatric Night Crying (Ye Ti - 夜啼) caused by Spleen Cold, Heart Heat, and Sudden Fright.",
        "back": "Differential Comparison of Pediatric Night Crying (夜啼):\n• Spleen Deficiency Cold (Pi Han Ye Ti):\n  - Crying Pattern: Cries continuously at night with a dull, low, weak wailing sound; stops crying during the day; curls body up in bed, desires abdominal pressure/warmth from mother's chest.\n  - Symptoms: Cold hands and feet, pale face and lips, anorexia, loose stools, pale tongue with white coat.\n  - Treatment: Warm middle jiao, scatter cold, fortify Spleen (Points: Moxa on REN8 Shenque, ST36 Zusanli, Push Banmen, Tui San Guan).\n\n• Heart Heat (Xin Re Ye Ti):\n  - Crying Pattern: Loud, intense, resonant crying throughout the night; face flushed red, feverish body temperature, agitated tossing and turning, cries when seeing light.\n  - Symptoms: Red lips, dark concentrated urine, constipation, red tongue tip with prickly dots.\n  - Treatment: Clear Heart fire, soothe Shen (Points: Clear Tianheshui tuina, HT7 Shenmen, PC6 Neiguan, Clear Xin Jing tuina).\n\n• Fright / Terror (Jing Kong Ye Ti):\n  - Crying Pattern: Sudden waking with terrified screaming, trembling, clinging desperately to mother, eyes darting in terror.\n  - Symptoms: Greenish stool, purplish-blue vein at index finger Feng Guan.\n  - Treatment: Settle fright, pacify Shen (Points: Push Tianmen, Knead Taiyang, Yintang, LV3 Taichong).",
        "consensus": "Classic differentiation for infant sleep disturbance and night crying.",
        "variations": "Night crying from Spleen cold occurs because Yin cold predominates at night, contracting the intestines.",
        "sources": json.dumps(["Royal TCM TCM-09 Paediatrics", "CAM 3rd Ed."])
    }
]

"""Gynecology Flashcards (30 high-yield clinical cards).

Covers menstrual physiology, 4-phase cycle regulation, dysmenorrhea, amenorrhea,
Beng Lou (flooding & trickling), leukorrhea, pregnancy conditions & contraindications,
breech turning, postpartum care, menopause, infertility, and PCOS.
All points strictly use bilingual format: CODE (Pinyin / Hanzi).
"""

import json

CARDS = [
    {
        "category": "Gynecology",
        "title": "Gynecological Physiology: Tian Gui, Chong, Ren, and Bao Gong",
        "front": "Explain the physiological roles of Tian Gui, the Chong Mai, the Ren Mai, and the Uterus (Bao Gong) in female reproduction.",
        "back": "Gynecological Physiology:\n• Tian Gui (天癸 - Heavenly Gui):\n  - Essence derived from Kidney Jing that matures at puberty (age 14 / '2x7' in Suwen Ch. 1) to enable menstruation and fertility, and wanes at menopause (age 49 / '7x7').\n\n• Chong Mai (冲脉 - Sea of Blood):\n  - Originates in the Uterus; connects with the Stomach channel (Sea of Water & Grain) and Kidney channel.\n  - Regulates the volume and flow of blood to the Uterus; ensures adequate reservoir for menstruation and fetal nourishment.\n\n• Ren Mai (任脉 - Sea of Yin):\n  - Governs all Yin channels; commands conception, pregnancy, and nourishing the fetus ('Ren' means to nurture/carry).\n\n• Bao Gong (胞宫 - Uterus):\n  - Extraordinary Fu organ: acts like a Zang (stores blood/fetus during pregnancy) and like a Fu (discharges menses and delivers child during labor).\n  - Connected to Heart via Bao Mai (Uterine Vessel) and to Kidneys via Bao Luo (Uterine Collateral).",
        "consensus": "Foundational paradigm for understanding all gynecological health and pathology in TCM.",
        "variations": "Heart governs Blood and commands discharge of menses through Bao Mai; Kidneys store Jing and provide Tian Gui through Bao Luo.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology in Chinese Medicine"])
    },
    {
        "category": "Gynecology",
        "title": "Four Phases of the Menstrual Cycle: Treatment Principles",
        "front": "Detail the physiological state and acupuncture treatment principles for each of the Four Phases of the Menstrual Cycle.",
        "back": "The Four Phases of the Menstrual Cycle:\n1. Phase 1: Menstrual Phase (Days 1–4/5) [Blood moving downward]:\n   - State: Blood discharging; Chong and Ren are emptying; downward Qi movement.\n   - Treatment Principle: Move Blood, regulate Qi, ensure complete discharge without stasis.\n   - Points: SP6 (Sanyinjiao / 三阴交), SP10 (Xuehai / 血海), CV3 (Zhongji / 中极), LV3 (Taichong / 太冲).\n\n2. Phase 2: Post-Menstrual Phase / Follicular (Days 5–12) [Yin and Blood rebuilding]:\n   - State: Uterine blood is empty; Yin and Blood are regenerating under Kidney Jing.\n   - Treatment Principle: Nourish Blood, tonify Kidney Yin, nourish liver.\n   - Points: KI3 (Taixi / 太溪), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), BL23 (Shenshu / 肾俞), ST36 (Zusanli / 足三里), Zigong (EX-CA1).\n\n3. Phase 3: Mid-Cycle / Ovulatory Phase (Days 13–16) [Yin peaks and converts to Yang]:\n   - State: Ovulation occurs; rapid transformation from Yin to Yang; cervix opens.\n   - Treatment Principle: Promote Yang, invigorate Blood to rupture follicle, unblock Chong/Ren.\n   - Points: REN4 (Guanyuan / 关元), BL23 (Shenshu / 肾俞), SP6 (Sanyinjiao / 三阴交), Zigong (EX-CA1), KI6 (Zhaohai / 照海).\n\n4. Phase 4: Pre-Menstrual / Luteal Phase (Days 17–28) [Yang Qi abundant, Qi prepares to move]:\n   - State: Yang Qi warms uterus; Qi moves to prepare for shedding; Liver Qi easily stagnates (PMS).\n   - Treatment Principle: Warm Kidney Yang, soothe Liver Qi, regulate Chong/Ren.\n   - Points: LV3 (Taichong / 太冲), PC6 (Neiguan / 内关), CV4 (Guanyuan / 关元), BL23 (Shenshu / 肾俞).",
        "consensus": "Modern TCM reproductive protocol pioneered by Dr. Xia Guicheng for fertility and cycle regulation.",
        "variations": "Never over-invigorate blood during Phase 2 (post-menses), as it damages newly regenerating Yin and Blood.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Dysmenorrhea (Tong Jing): Excess vs Deficiency Differentiation",
        "front": "Contrast Excess Dysmenorrhea (Cold Coagulation, Qi/Blood Stagnation) versus Deficiency Dysmenorrhea (Qi/Blood Deficiency, Kidney/Liver Deficiency).",
        "back": "Differential Comparison of Dysmenorrhea (痛经):\n• Excess Dysmenorrhea (Shi Tong):\n  - Pain Timing: Pain begins BEFORE or during the FIRST 1–2 days of menstruation.\n  - Nature of Pain: Severe, sharp, distending, or cramping pain that is AGGRAVATED BY PRESSURE (refuses touch).\n  - Cold Coagulation: Relieved by application of warmth/hot water bottle; dark purplish blood with large clots; cold limbs, pale/purple tongue, deep tight pulse.\n  - Qi/Blood Stagnation: Severe pre-menstrual distension, breast tenderness; pain relieved once clots pass; dark clotted blood, wiry pulse.\n  - Points: SP8 (Diji / 地机 - Xi-Cleft for acute pain), SP6 (Sanyinjiao / 三阴交), CV3 (Zhongji / 中极), Zigong (EX-CA1), LV3 (Taichong / 太冲), Moxa on CV4.\n\n• Deficiency Dysmenorrhea (Xu Tong):\n  - Pain Timing: Pain starts TOWARDS THE END OF or AFTER menstruation has ceased.\n  - Nature of Pain: Dull, continuous, dragging ache that is RELIEVED BY PRESSURE (desires massage/firm touch) and warmth; relieved by rest.\n  - Accompanied by: Fatigue, dizziness, pale sallow face, scanty pale thin blood, pale tongue, thin weak pulse.\n  - Points: REN4 (Guanyuan / 关元), ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), BL23 (Shenshu / 肾俞).",
        "consensus": "The timing of pain (before/during menses vs after menses) and response to pressure (refuses vs desires) is the definitive diagnostic key.",
        "variations": "SP8 (Diji) is the premier emergency Xi-Cleft point to needle for acute, incapacitating menstrual cramps.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed.", "Maciocia Obstetrics & Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Zigong (EX-CA1): Location, Needling Technique, and Actions",
        "front": "State the anatomical location, needling angle and depth, and primary clinical indications for the extra point Zigong (子宫).",
        "back": "Extra Point Zigong (EX-CA1 - 子宫 / Palace of the Child):\n• Location: On the lower abdomen, 4 cun inferior to the umbilicus (level with REN3), 3 cun lateral to the anterior midline.\n\n• Actions:\n  - Warms and tonifies the Uterus and lower jiao.\n  - Regulates Qi and Blood in Chong and Ren vessels.\n  - Treats infertility (primary and secondary), uterine prolapse, irregular menstruation, dysmenorrhea, and abnormal uterine bleeding.\n\n• Needling Technique:\n  - Perpendicular insertion 0.8 - 1.2 cun.\n  - For uterine prolapse: Puncture obliquely towards the pubic symphysis/inguinal canal 1.5 - 2.0 cun until a sensation radiating into the perineum is achieved.\n  - Moxibustion (indirect or warm needle) is highly effective for Cold Uterus (Gong Han) causing infertility or dysmenorrhea.\n  - Cautions: Empty urinary bladder prior to needling; contraindicated in pregnancy.",
        "consensus": "Premier empirical acupuncture point for female reproductive disorders and infertility worldwide.",
        "variations": "Commonly combined with SP6 (Sanyinjiao) and CV4 (Guanyuan) as the core triad for reproductive medicine.",
        "sources": json.dumps(["CAM 3rd Ed.", "Deadman Manual of Acupuncture"])
    },
    {
        "category": "Gynecology",
        "title": "Beng Lou (Flooding and Trickling): Four Patterns & SP1 Moxibustion",
        "front": "Define Beng Lou (Abnormal Uterine Bleeding), compare its four primary patterns, and describe the empirical moxa protocol at SP1 (Yinbai).",
        "back": "Beng Lou (崩漏 - Flooding and Trickling):\n• Definition: Beng (Flooding) = sudden, profuse, heavy uterine bleeding like an overflowing dam; Lou (Trickling) = continuous, dribbling, unceasing bleeding beyond the normal cycle.\n\nFour Major Patterns:\n1. Blood Heat: Profuse or trickling bright red or deep purple sticky blood with clots; fever, thirst, dark urine, red tongue, rapid slippery pulse. (Points: SP10, LI11, CV3, KI2).\n2. Spleen Qi Sinking: Heavy or prolonged trickling of pale, thin, watery blood; extreme fatigue, shortness of breath, sallow face, pale tongue with teeth marks, weak pulse. (Points: DU20, REN6, ST36, BL20).\n3. Blood Stasis: Intermittent trickling of dark purplish blood with sharp stabbing abdominal pain, purple clots; tongue purple, choppy wiry pulse. (Points: SP8, BL17, SP10, CV3).\n4. Kidney Deficiency: Yin deficiency (bright red scanty trickling, night sweats) vs Yang deficiency (pale cold trickling, cold back, nocturia).\n\n⚠️ Empirical Moxibustion Protocol at SP1 (Yinbai / 隐白):\n• Location: Medial corner of big toe nail, 0.1 cun posterior.\n• Technique: Direct or indirect moxibustion (moxa cone or stick) applied for 10–15 minutes until skin is flushed.\n• Mechanism: Spleen governs blood and controls extravasation; moxibustion on Spleen Jing-Well point astringes and stops bleeding immediately across all deficiency bleeding patterns.",
        "consensus": "SP1 moxibustion is the single most celebrated emergency remedy for uterine hemorrhage in Chinese medicine.",
        "variations": "Combine SP1 with LR1 (Dadun) moxibustion if emotional Liver constraint or Blood Heat is the underlying driver.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed.", "Maciocia Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Leukorrhea (Dai Xia): Cold-Damp vs Spleen vs Damp-Heat",
        "front": "Differentiate Leukorrhea (Morbid Vaginal Discharge) caused by Spleen Deficiency, Kidney Yang Deficiency, and Damp-Heat.",
        "back": "Differential Comparison of Leukorrhea (带下病):\n• Spleen Deficiency (Pi Xu Dai Xia):\n  - Discharge: Copious, white or light yellow, thin, odorless discharge.\n  - Accompanying: Sallow complexion, fatigue, loose stools, poor appetite, pale swollen tongue with teeth marks, weak pulse.\n  - Points: BL20 (Pishu / 脾俞), SP9 (Yinlingquan / 阴陵泉), GB26 (Daimai / 带脉), REN6 (Qihai / 气海), ST36 (Zusanli / 足三里).\n\n• Kidney Yang Deficiency (Shen Yang Xu Dai Xia):\n  - Discharge: Profuse, clear, watery, cold discharge like egg white, continuous unceasing dribbling.\n  - Accompanying: Severe cold lumbar/knees, frequent clear nocturia, pale wet tongue, deep weak slow pulse.\n  - Points: BL23 (Shenshu / 肾俞), REN4 (Guanyuan / 关元), DU4 (Mingmen / 命门), GB26 (Daimai / 带脉), KI7 (Fuliu / 复溜) with moxa.\n\n• Damp-Heat in Lower Jiao (Shi Re Dai Xia):\n  - Discharge: Thick, yellow or green, purulent, foul-smelling or fishy discharge, accompanied by intense vaginal itching (pruritus vulvae), burning on urination.\n  - Accompanying: Red tongue with thick greasy yellow coating, slippery rapid pulse.\n  - Points: SP9 (Yinlingquan / 阴陵泉), LV8 (Ququan / 曲泉), LV5 (Ligou / 蠡沟 - Luo point for genital itching), CV3 (Zhongji / 中极), BL32 (Ciliao / 次髎).",
        "consensus": "GB26 (Daimai - level with umbilicus directly below 11th rib) binds the Dai Mai vessel to astringe discharge in all patterns.",
        "variations": "LV5 is the specific Luo-Connecting point indicated for genital pruritus and herpes lesions.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Morning Sickness (Hyperemesis Gravidarum): Etiology & Points",
        "front": "What is the TCM etiology of Morning Sickness (Zhu Tai / E Zu) and what is the safe acupuncture prescription?",
        "back": "Clinical Protocol for Morning Sickness (恶阻 / 妊娠呕吐):\n• TCM Etiology:\n  - During pregnancy, menstrual blood ceases flowing downward and gathers in the Chong and Ren vessels to nurture the fetus.\n  - Blood becomes abundant in the lower jiao, causing Chong Mai Qi to rebel upwards.\n  - Chong Mai attaches to the Stomach; upward rebelling Qi invades the Stomach, causing Stomach Qi to fail to descend and vomit.\n\n• Primary Patterns:\n  1. Disharmony between Liver and Stomach: Vomiting bitter/sour fluid, irritability, rib-side distension, wiry pulse.\n  2. Spleen-Stomach Deficiency: Vomiting clear fluid or food immediately after eating, severe fatigue, pale tongue, slippery weak pulse.\n\n• Safe Point Prescription:\n  - PC6 (Neiguan / 内关 - master anti-emetic, calms Chong Mai).\n  - ST36 (Zusanli / 足三里 - descends Stomach Qi, fortifies digestion).\n  - REN12 (Zhongwan / 中脘 - Front-Mu of Stomach; needle gently perpendicularly 0.5–0.8 cun; strictly avoid deep insertion).\n  - SP4 (Gongsun / 公孙 - Master of Chong Mai).\n\n⚠️ Contraindications: Strictly avoid LI4, SP6, GB21, and all lower abdominal points (CV3, CV4, CV5).",
        "consensus": "PC6 is universally recognized in both TCM and Western obstetrics (acupressure wristbands) as safe and effective for pregnancy nausea.",
        "variations": "Moxibustion on middle jiao points is avoided in Liver-Stomach heat patterns.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed.", "American College of Obstetricians and Gynecologists (ACOG)"])
    },
    {
        "category": "Gynecology",
        "title": "Breech Presentation: BL67 (Zhiyin) Moxibustion Protocol",
        "front": "State the gestational window, mechanism, application protocol, and safety parameters for using BL67 (Zhiyin) moxibustion to correct breech presentation.",
        "back": "Breech Presentation Protocol (Tai Wei Bu Zheng - 胎位不正):\n• Optimal Gestational Window:\n  - Weeks 32 to 34 (highest success rate, approx. 70–80%). Less effective after week 36 due to limited intrauterine space and engaged fetal head.\n\n• Point: BL67 (Zhiyin / 至阴) [Bilateral Jing-Well point on lateral aspect of 5th toe].\n\n• Technique & Protocol:\n  - Use a smokeless or standard moxa stick.\n  - Apply indirect moxa (bird-pecking or circular method) over bilateral BL67 held 2–3 cm away until local skin is flushed and warm (never burn skin).\n  - Duration: 15 to 20 minutes daily for 7 to 10 consecutive days.\n  - Patient posture: Sitting comfortably or in knee-chest position, with loose clothing.\n\n• Mechanism:\n  - Bladder channel connects with Kidneys and uterus; Jing-Well point invigorates Yang Qi, stimulates maternal adrenocortical secretion, increases placental prostaglandins, and elevates fetal heart movement and spontaneous uterine tone, encouraging the fetus to somersault.\n\n⚠️ Safety & Contraindications:\n• Contraindicated if placenta previa, multiple gestation (twins), severe pre-eclampsia, uterine anomalies, or previous classical Cesarean scar.\n• Verify fetal position by ultrasound or Leopold maneuvers before and after treatment.",
        "consensus": "The most widely researched TCM obstetric protocol with proven clinical efficacy.",
        "variations": "If fetus rotates to cephalic position before the 10 days are completed, cease moxibustion immediately to prevent turning back.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Cardini & Weixin JAMA Breech Study", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Menopausal Syndrome: Kidney Yin vs Kidney Yang Deficiency",
        "front": "Differentiate Menopausal Syndrome (Jue Jing Qian Hou Zhu Zheng) between Kidney Yin Deficiency with Empty Heat and Kidney Yin & Yang Dual Deficiency.",
        "back": "Differential Comparison of Menopausal Syndrome (绝经前后诸证):\n• Kidney Yin Deficiency with Empty Heat (Shen Yin Xu Huo Wang):\n  - Symptoms: Severe hot flashes, night sweats, blushing red face, palpitations, dizziness, tinnitus, insomnia, irritability, dry vaginal mucosa, sore lower back, dry stool.\n  - Tongue: Red body, dry, peeled coating (scanty or absent coat), transverse cracks.\n  - Pulse: Thin (Xi) and Rapid (Shuo), weak at proximal (Chi) position.\n  - Points: KI3 (Taixi / 太溪), KI6 (Zhaohai / 照海), SP6 (Sanyinjiao / 三阴交), HT6 (Yinxi / 阴郄 - Xi-Cleft for night sweats), HT7 (Shenmen / 神门), BL23 (Shenshu / 肾俞).\n\n• Kidney Yin and Yang Dual Deficiency (Yin Yang Liang Xu):\n  - Symptoms: Hot flashes and night sweats alternating with chills, cold lower back and knees, cold hands and feet, edema of ankles/face, extreme fatigue, depression, frequent clear urination.\n  - Tongue: Pale or slightly red with teeth marks, thin white coat.\n  - Pulse: Deep, thin, and weak in both proximal positions.\n  - Points: BL23 (Shenshu / 肾俞), DU4 (Mingmen / 命门), REN4 (Guanyuan / 关元), KI3 (Taixi / 太溪), SP6 (Sanyinjiao / 三阴交), ST36 (Zusanli / 足三里), with gentle indirect moxa on lumbar points.",
        "consensus": "Menopause represents the natural physiological exhaustion of Tian Gui and Kidney Jing.",
        "variations": "HT6 + KI7 is the classic empirical point combination for stopping debilitating menopausal night sweats.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Insufficient Lactation (Hypogalactia): Deficiency vs Stagnation",
        "front": "Differentiate Insufficient Lactation (Que Ru) caused by Qi & Blood Deficiency versus Liver Qi Stagnation.",
        "back": "Differential Comparison of Insufficient Lactation (缺乳):\n• Qi and Blood Deficiency (Qi Xue Xu Ru):\n  - Breast Appearance: Soft, flaccid, unswollen breasts; scanty or absent breast milk, milk is thin and watery.\n  - Accompanying: Severe postpartum fatigue, pale sallow complexion, poor appetite, dizziness, pale tongue, thin weak pulse.\n  - Treatment Principle: Tonify Qi, nourish Blood, generate breast milk.\n  - Points: SI1 (Shaoze / 少泽), REN17 (Danzhong / 膻中), ST18 (Rugen / 乳根), ST36 (Zusanli / 足三里), BL20 (Pishu / 脾俞), SP6 (Sanyinjiao / 三阴交).\n\n• Liver Qi Stagnation (Gan Qi Yu Jie):\n  - Breast Appearance: Swollen, distended, painful, firm breasts with palpable hardness; milk does not flow freely or trickles with difficulty.\n  - Accompanying: Emotional distress, irritability, depression, sighing, hypochondriac fullness, wiry pulse, normal tongue with slightly red edges.\n  - Treatment Principle: Soothe Liver Qi, open breast channels, unblock milk flow.\n  - Points: SI1 (Shaoze / 少泽), REN17 (Danzhong / 膻中), ST18 (Rugen / 乳根), LV3 (Taichong / 太冲), GB34 (Yanglingquan / 阳陵泉), GB21 (Jianjing / 肩井).\n\n• SI1 (Shaoze / 少泽) Empirical Specialization:\n  - Jing-Well point of Small Intestine channel; master empirical point on the body for promoting lactation in both excess and deficiency patterns.",
        "consensus": "SI1, REN17, and ST18 form the universal local-distal triad for lactation disorders.",
        "variations": "Pricking SI1 to express 1–2 drops of blood is particularly effective for acute stagnation with breast engorgement.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed.", "Deadman Manual"])
    },
    {
        "category": "Gynecology",
        "title": "Early Menstruation (Yue Jing Xian Qi): Blood Heat vs Qi Deficiency",
        "front": "Differentiate Early Menstruation (menses arriving > 7 days early) caused by Heat in the Blood versus Qi Deficiency.",
        "back": "Differential Comparison of Early Menstruation (月经先期):\n• Heat in the Blood (Xue Re):\n  - Bleeding: Profuse, bright red or dark purple, thick/sticky blood with clots.\n  - Symptoms: Flushed face, thirst, irritability, restlessness, dark urine, constipation.\n  - Tongue: Red with yellow coat; Pulse: Rapid, slippery.\n  - Points: SP10 (Xuehai / 血海), LI11 (Quchi / 曲池), KI2 (Rangu / 然谷 - Ying-Spring for heat), CV3 (Zhongji / 中极).\n\n• Qi Deficiency (Qi Xu - Spleen Qi Failing to Control Blood):\n  - Bleeding: Profuse or scanty, pale thin watery blood without clots.\n  - Symptoms: Fatigue, shortness of breath, palpitations, sallow complexion, poor appetite, loose stools.\n  - Tongue: Pale, swollen with teeth marks; Pulse: Weak, deficient.\n  - Points: ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), REN6 (Qihai / 气海), DU20 (Baihui / 百会).",
        "consensus": "Early menses is caused either by Heat forcing blood to move prematurely or Qi failing to hold blood in vessels.",
        "variations": "If caused by Liver Qi stagnation transforming into fire, add LV2 (Xingjian) and LV3 (Taichong).",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Late Menstruation (Yue Jing Hou Qi): Blood Deficiency vs Cold",
        "front": "Differentiate Late Menstruation (menses delayed > 7 days) caused by Blood Deficiency, Cold Congealing, and Qi Stagnation.",
        "back": "Differential Comparison of Late Menstruation (月经后期):\n• Blood Deficiency (Xue Xu):\n  - Bleeding: Scanty, pale pink, thin watery discharge.\n  - Symptoms: Dull complexion, dizzy spells, blurry vision, palpitations, insomnia, dry skin, pale tongue, thin weak pulse.\n  - Points: ST36 (Zusanli / 足三里), SP6 (Sanyinjiao / 三阴交), BL20 (Pishu / 脾俞), REN4 (Guanyuan / 关元), BL17 (Geshu / 膈俞).\n\n• Cold Congealing in Uterus (Han Ning Bao Gong):\n  - Bleeding: Scanty, dark purple blood with clots, accompanied by lower abdominal cold cramping pain relieved by warmth.\n  - Symptoms: Aversion to cold, cold limbs, pale/purplish tongue, deep slow or tight pulse.\n  - Points: Moxa on REN4 (Guanyuan / 关元), ST29 (Guilai / 归来), SP6 (Sanyinjiao / 三阴交), SP8 (Diji / 地机).\n\n• Qi Stagnation (Qi Zhi):\n  - Bleeding: Scanty, dark blood with clots, accompanied by lower abdominal distension and breast swelling.\n  - Symptoms: Mental depression, sighing, wiry pulse.\n  - Points: LV3 (Taichong / 太冲), REN6 (Qihai / 气海), SP6 (Sanyinjiao / 三阴交), ST25 (Tianshu / 天枢).",
        "consensus": "ST29 (Guilai) is the premier local point for warming the lower abdomen and bringing back delayed menses.",
        "variations": "Always rule out pregnancy before treating acute delayed menstruation.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    },
    {
        "category": "Gynecology",
        "title": "Female Infertility (Bu Yun): Kidney Yang vs Kidney Yin vs Phlegm-Damp",
        "front": "Differentiate Female Infertility (Bu Yun) caused by Kidney Yang Deficiency (Cold Uterus), Kidney Yin Deficiency, and Phlegm-Dampness (PCOS).",
        "back": "Differential Comparison of Infertility (不孕症):\n• Kidney Yang Deficiency / Cold Uterus (Gong Han Bu Yun):\n  - Manifestation: Long delayed cycles or amenorrhea, low basal body temperature (BBT) in luteal phase, cold lower abdomen and feet, sore lower back, clear profuse urine, pale tongue, deep slow weak pulse.\n  - Treatment Principle: Warm Kidney Yang, warm Uterus, nourish Jing.\n  - Points: Moxa on DU4 (Mingmen / 命门), REN4 (Guanyuan / 关元), BL23 (Shenshu / 肾俞), Zigong (EX-CA1), KI3 (Taixi / 太溪).\n\n• Kidney Yin Deficiency (Shen Yin Xu Bu Yun):\n  - Manifestation: Scanty bright red menses, dry vaginal tract, hot flashes, night sweats, sore lumbar, dizziness, red tongue with scanty coat, thin rapid pulse.\n  - Treatment Principle: Nourish Kidney Yin, clear empty heat, nourish Tian Gui.\n  - Points: KI3 (Taixi / 太溪), KI6 (Zhaohai / 照海), SP6 (Sanyinjiao / 三阴交), REN4 (Guanyuan / 关元), Zigong (EX-CA1).\n\n• Phlegm-Dampness / PCOS (Tan Shi Bu Yun):\n  - Manifestation: Obesity, delayed cycles or amenorrhea, profuse white sticky leukorrhea, hirsutism, sticky mouth taste, puffy face, swollen tongue with greasy white coat, slippery pulse.\n  - Treatment Principle: Transform phlegm, dissolve dampness, fortify Spleen, unblock oviducts.\n  - Points: ST40 (Fenglong / 丰隆), SP9 (Yinlingquan / 阴陵泉), REN12 (Zhongwan / 中脘), Zigong (EX-CA1), ST28 (Shuidao / 水道).",
        "consensus": "Zigong (EX-CA1) combined with CV4 and SP6 forms the universal core acupuncture prescription for female fertility.",
        "variations": "ST28 (Shuidao) promotes transformation of fluid stagnation in polycystic ovaries.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "Maciocia Obstetrics & Gynecology"])
    },
    {
        "category": "Gynecology",
        "title": "Threatened Miscarriage / Restless Fetus (Tai Dong Bu An)",
        "front": "What are the clinical signs of Threatened Miscarriage (Tai Dong Bu An) and the safe acupuncture protocol to secure the fetus?",
        "back": "Threatened Miscarriage (胎动不安 - Restless Fetus):\n• Clinical Manifestations:\n  - Scanty vaginal bleeding (pink or dark brown trickling) during early pregnancy accompanied by dull lower abdominal ache or dragging lumbar soreness, without cervical dilation.\n\n• Primary Etiologies:\n  1. Kidney Deficiency: Sore weak lower back, frequent urination, pale tongue, deep weak pulse (Kidney Jing fails to anchor fetus).\n  2. Spleen Qi Sinking: Bearing down feeling in lower abdomen, fatigue, poor appetite, pale tongue with teeth marks.\n  3. Blood Heat: Bright red blood, dry mouth, thirst, yellow urine, red tongue, rapid slippery pulse.\n\n• Safe Acupuncture Protocol (To Secure Chong & Ren):\n  - DU20 (Baihui / 百会): Raises sinking Yang Qi and anchors the fetus.\n  - ST36 (Zusanli / 足三里): Fortifies Spleen, tonifies Post-Heaven Qi and Blood.\n  - KI3 (Taixi / 太溪): Gently tonifies Kidney Yin and Yang.\n  - SP10 (Xuehai / 血海): Harmonizes blood (gentle tonification).\n\n⚠️ Strict Safety Warnings:\n• NEVER needle lower abdomen, lumbosacral region, or contraindicated points (LI4, SP6, BL60, BL67, GB21).\n• Perform minimal stimulation without lifting or thrusting; refer for immediate obstetric ultrasound to confirm fetal viability and rule out ectopic pregnancy.",
        "consensus": "Minimal distal needling with DU20 and ST36 to raise Qi; absolute avoidance of local abdominal points.",
        "variations": "Severe sharp unilateral pain with syncope is an ectopic pregnancy emergency requiring immediate 911 dispatch.",
        "sources": json.dumps(["Royal TCM TCM-08 Gynecology", "CAM 3rd Ed."])
    }
]

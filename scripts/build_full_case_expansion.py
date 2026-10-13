# -*- coding: utf-8 -*-
"""Generate Full 35-Case Clinical Expansion for modules/cases_bank.py."""

import sys
import pprint
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from modules.cases_bank import CLINICAL_CASES

print(f"Loaded {len(CLINICAL_CASES)} cases from modules/cases_bank.py.")

EXTENSIONS = {
    "CASE-001": [
        {
            "question_id": "Q4",
            "title": "4. Point Modifications for Secondary Symptoms (随证配穴)",
            "prompt": "If this 36-year-old attorney develops severe premenstrual breast distension and severe insomnia with restless tossing, which secondary point modifications should be added to the prescription?",
            "options": [
                "A. Add CV17 (Danzhong) and GB41 (Zulinqi) for breast distension; add HT7 (Shenmen) and Anmian for insomnia.",
                "B. Add BL23 (Shenshu) and DU4 (Mingmen) for breast distension; add KD1 (Yongquan) for insomnia.",
                "C. Add LU11 (Shaoshang) and LI1 (Shangyang) bleeding technique for breast distension.",
                "D. Add ST25 (Tianshu) and ST37 (Shangjuxu) for breast distension; add CV4 (Guanyuan) for insomnia."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** CV17 (Hui-Meeting of Qi) unbinds chest and breast Qi stagnation; GB41 (Confluent point of Dai Mai) specifically treats breast distension and hypochondriac pain associated with Shaoyang/Liver disharmony. HT7 (Yuan-Source of Heart) and Anmian (Extra point) calm the Shen and settle restless sleep.",
                "B": "❌ **Incorrect:** BL23 and DU4 strongly warm Kidney Yang and Mingmen Fire, which would exacerbate Liver Fire and sleep restlessness.",
                "C": "❌ **Incorrect:** Bleeding LU11 and LI1 drains acute high fever and sore throat in Wind-Heat invasions, which is completely irrelevant for breast distension.",
                "D": "❌ **Incorrect:** ST25 and ST37 treat large intestine disorders (diarrhea and dysentery), not emotional breast distension or sleep disturbances."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and premier classical herbal formulation for this patient's presentation of Liver Qi Stagnation transforming into Fire with secondary Spleen disharmony?",
            "options": [
                "A. Principle: Warm Kidney Yang and disperse cold. Formula: Jin Gui Shen Qi Wan (Golden Book Kidney Qi Pill).",
                "B. Principle: Soothe Liver Qi, clear heat, nourish blood, and harmonize Spleen. Formula: Dan Zhi Xiao Yao San (Free and Easy Wanderer with Moutan and Gardenia).",
                "C. Principle: Tonify Qi and Blood. Formula: Ba Zhen Tang (Eight Treasures Decoction).",
                "D. Principle: Drain Damp-Heat from Lower Jiao. Formula: Ba Zheng San (Eight Herb Powder for Rectification)."
            ],
            "correct_index": 1,
            "explanations": {
                "A": "❌ **Incorrect:** Warming Kidney Yang with Jin Gui Shen Qi Wan is contraindicated because the patient suffers from excess Liver Fire and heat.",
                "B": "✅ **Correct:** Dan Zhi Xiao Yao San (Jia Wei Xiao Yao San) is the premier formula across all TCM board exams for Liver Qi stagnation transforming into heat with premenstrual tension, irritability, red tongue sides, and wiry pulse.",
                "C": "❌ **Incorrect:** Ba Zhen Tang addresses concurrent Qi and Blood deficiency, lacking the critical Chai Hu, Mu Dan Pi, and Zhi Zi needed to dredge Liver Qi and clear constrained fire.",
                "D": "❌ **Incorrect:** Ba Zheng San treats acute damp-heat dysuria (urinary tract infection) in the Bladder, not Liver Qi migraines or PMS."
            }
        }
    ],

    "CASE-002": [
        {
            "question_id": "Q4",
            "title": "4. Point Modifications for Accompanying Symptoms (随证配穴)",
            "prompt": "If this 68-year-old woodworker reports that cold weather causes severe knee stiffness and weak ankles in addition to his lower back pain, which point combination is the premier addition?",
            "options": [
                "A. Prick BL40 (Weizhong) and LI11 (Quchi) to bleed.",
                "B. Add GB34 (Yanglingquan), ST35 (Dubi), and Xiyan (EX-LE5) with warm moxibustion.",
                "C. Add LU5 (Chize) and LU7 (Lieque) with deep reducing technique.",
                "D. Add ST44 (Neiting) and LI4 (Hegu) to clear stomach fire."
            ],
            "correct_index": 1,
            "explanations": {
                "A": "❌ **Incorrect:** Bleeding BL40 and LI11 releases toxic heat and blood stasis, which would further deplete an elderly patient suffering from Yang deficiency cold.",
                "B": "✅ **Correct:** GB34 (Hui-Meeting of Sinews) relaxes tendons, while ST35 and Xiyan (Eyes of the Knee) directly warm and unblock the knee joint collaterals. Warm needle moxibustion dispels local cold and restores joint mobility.",
                "C": "❌ **Incorrect:** Lung channel points treat upper respiratory disorders and exterior wind, not degenerative knee bi cold.",
                "D": "❌ **Incorrect:** ST44 and LI4 purge Yangming heat and toothache, which is inappropriate for lower limb cold stiffness."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classic herbal prescription for this patient's chronic lower back ache due to Kidney Yang Deficiency with Mingmen Fire decline?",
            "options": [
                "A. Principle: Nourish Kidney Yin and clear empty fire. Formula: Zhi Bai Di Huang Wan.",
                "B. Principle: Clear Damp-Heat from lower burner. Formula: Er Miao San.",
                "C. Principle: Warm and tonify Kidney Yang, replenish Mingmen Fire, and strengthen bones/sinews. Formula: You Gui Wan (Restore the Right Pill) or Jin Gui Shen Qi Wan.",
                "D. Principle: Invigorate Blood and dissolve stasis. Formula: Tao Hong Si Wu Tang."
            ],
            "correct_index": 2,
            "explanations": {
                "A": "❌ **Incorrect:** Zhi Bai Di Huang Wan nourishes Yin and drains empty fire (for night sweats and five-palm heat), which would worsen cold and nocturia.",
                "B": "❌ **Incorrect:** Er Miao San clears damp-heat in the lower extremities, not constitutional Yang depletion.",
                "C": "✅ **Correct:** You Gui Wan / Jin Gui Shen Qi Wan is the benchmark classic prescription to warm Kidney Yang, replenish primal essence, and relieve cold low back pain and frequent clear nocturia.",
                "D": "❌ **Incorrect:** Tao Hong Si Wu Tang is indicated for blood stasis dysmenorrhea or traumatic bruising, not chronic Kidney Yang deficiency."
            }
        }
    ],

    "CASE-003": [
        {
            "question_id": "Q4",
            "title": "4. Immediate Empirical Point Strategy (经验要穴与对穴)",
            "prompt": "While the patient is unable to bend forward due to acute severe lumbar muscle spasm, which distal empirical point pairing should be stimulated with active mobilization (Dong Qi technique)?",
            "options": [
                "A. Yaotongxue (EX-UE7) on the dorsum of the hand and/or GV26 (Shuigou / Renzhong), having the patient slowly rotate and flex the waist during needle manipulation.",
                "B. Perpendicular deep puncture into bilateral KD1 (Yongquan) with 30-minute static needle retention.",
                "C. Direct moxibustion on CV8 (Shenque) and CV4 (Guanyuan).",
                "D. Retain needles at SP6 (Sanyinjiao) and ST36 (Zusanli) in strict supine stillness."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Yaotongxue (EX-UE7) and GV26 (Shuigou) are the classic empirical rescue points for acute lumbar sprain. Applying the Dynamic Needling (Dong Qi) technique—vigorously stimulating the distal points while instructing the patient to gently move and stretch the lumbar spine—immediately relieves muscle guarding.",
                "B": "❌ **Incorrect:** KD1 is too painful and inappropriate for lumbar sprain mobilization.",
                "C": "❌ **Incorrect:** Moxa on CV8 and CV4 treats Yang collapse and chronic cold, not acute mechanical lumbar sprain with blood stasis.",
                "D": "❌ **Incorrect:** SP6 and ST36 tonify Spleen and Blood, failing to address acute mechanical lumbar stagnation."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classic formula for acute lumbar sprain with localized Qi stagnation and Blood stasis?",
            "options": [
                "A. Principle: Invigorate Blood, dispel stasis, unblock channels, and alleviate pain. Formula: Shen Tong Zhu Yu Tang (Drive Out Blood Stasis from a Painful Body) or Huo Luo Xiao Ling Dan.",
                "B. Principle: Tonify Qi and nourish blood. Formula: Ba Zhen Tang.",
                "C. Principle: Clear heat and drain dampness. Formula: Yin Chen Hao Tang.",
                "D. Principle: Warm the channels and disperse cold. Formula: Dang Gui Si Ni Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Shen Tong Zhu Yu Tang is Wang Qing-Ren's classic formula specifically designed for body pain, severe joint/back stiffness, and traumatic blood stasis in the channels.",
                "B": "❌ **Incorrect:** Ba Zhen Tang is a tonifying formula for chronic fatigue and pale complexion, not acute trauma.",
                "C": "❌ **Incorrect:** Yin Chen Hao Tang is the premier formula for Yang jaundice and hepatitis, completely unrelated to orthopedic sprains.",
                "D": "❌ **Incorrect:** Dang Gui Si Ni Tang treats Cold in the channels causing Raynaud's syndrome or cold extremities."
            }
        }
    ],

    "CASE-004": [
        {
            "question_id": "Q4",
            "title": "4. Distal Empirical Point Modifications (随证配穴)",
            "prompt": "For acute severe cervical muscle spasm with restricted neck rotation, which distal empirical point on the hand is specific for neck stiffness?",
            "options": [
                "A. Luozhen (EX-UE8) on the dorsum of the hand between the 2nd and 3rd metacarpal bones, accompanied by SI3 (Houxi).",
                "B. SP4 (Gongsun) and PC6 (Neiguan).",
                "C. ST44 (Neiting) and ST45 (Lidui).",
                "D. KD1 (Yongquan) and KD2 (Rangu)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Luozhen (EX-UE8) literally translates to 'Stiff Neck Point' and is the premier empirical point for acute torticollis and cervical neck pain. SI3 (Houxi, Confluent point of Du Mai) opens the spine and neck.",
                "B": "❌ **Incorrect:** SP4 and PC6 open Chong Mai and Yin Wei Mai for chest, epigastrium, and stomach conditions.",
                "C": "❌ **Incorrect:** ST44 and ST45 drain stomach heat and toothache.",
                "D": "❌ **Incorrect:** KD1 and KD2 ground Kidney fire, not acute cervical muscular stiffness."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for cervical spondylosis due to Wind-Cold-Damp Bi obstructing the Taiyang and Shaoyang channels?",
            "options": [
                "A. Principle: Dispel Wind, scatter Cold, eliminate Dampness, unblock cervical channels, and relieve spasm. Formula: Ge Gen Tang (Kudzu Decoction) or Juan Bi Tang.",
                "B. Principle: Nourish Kidney Yin. Formula: Liu Wei Di Huang Wan.",
                "C. Principle: Purge Fire and loosen bowels. Formula: Da Cheng Qi Tang.",
                "D. Principle: Clear Heat from Qi level. Formula: Bai Hu Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Ge Gen Tang specifically releases the muscle layer and guides herbs to the nape of the neck and upper back. Juan Bi Tang removes generalized Wind-Cold-Damp obstruction.",
                "B": "❌ **Incorrect:** Liu Wei Di Huang Wan is for Yin deficiency, not acute exterior Wind-Cold bi.",
                "C": "❌ **Incorrect:** Da Cheng Qi Tang treats severe interior heat constipation in Yangming bowel syndrome.",
                "D": "❌ **Incorrect:** Bai Hu Tang treats the Four Bigs (high fever, profuse sweating, extreme thirst, flooding pulse)."
            }
        }
    ],

    "CASE-005": [
        {
            "question_id": "Q4",
            "title": "4. Channel Course Point Modification (循经配穴)",
            "prompt": "If this 45-year-old construction worker has sciatica radiation extending down the lateral aspect of the leg to the lateral malleolus and 4th toe, which channel points should be emphasized?",
            "options": [
                "A. Gallbladder channel points: GB30 (Huantiao), GB34 (Yanglingquan), GB39 (Xuanzhong), and GB41 (Zulinqi).",
                "B. Spleen channel points: SP6 (Sanyinjiao), SP9 (Yinlingquan), and SP10 (Xuehai).",
                "C. Lung channel points: LU5 (Chize), LU7 (Lieque), and LU9 (Taiyuan).",
                "D. Heart channel points: HT3 (Shaohai), HT7 (Shenmen), and HT8 (Shaofu)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Radiating pain along the lateral thigh, fibular neck, lateral malleolus, and 4th toe follows the exact trajectory of the Foot-Shaoyang Gallbladder channel. GB30, GB34, GB39, and GB41 are the primary points.",
                "B": "❌ **Incorrect:** The Spleen channel runs along the medial aspect of the lower leg.",
                "C": "❌ **Incorrect:** The Lung channel is located on the upper limb (radial arm).",
                "D": "❌ **Incorrect:** The Heart channel is located on the medial arm."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for chronic sciatica due to Wind-Cold-Damp Bi with underlying Liver and Kidney deficiency?",
            "options": [
                "A. Principle: Dispel Wind-Damp, scatter Cold, unblock channels, and supplement Liver and Kidney. Formula: Du Huo Ji Sheng Tang (Angelica Pubescens and Sangjisheng Decoction).",
                "B. Principle: Clear toxic heat from blood. Formula: Wu Wei Xiao Du Yin.",
                "C. Principle: Dry dampness in Middle Jiao. Formula: Ping Wei San.",
                "D. Principle: Tonify Lung Qi. Formula: Bu Fei Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Du Huo Ji Sheng Tang is the premier historical formula for chronic lower back and sciatic leg pain caused by pathogenic Wind-Cold-Damp lodging in patients with Liver/Kidney weakness.",
                "B": "❌ **Incorrect:** Wu Wei Xiao Du Yin treats toxic boils, carbuncles, and localized skin infections.",
                "C": "❌ **Incorrect:** Ping Wei San treats food stagnation and dampness in the Stomach/Spleen.",
                "D": "❌ **Incorrect:** Bu Fei Tang treats chronic constitutional Lung Qi deficiency cough."
            }
        }
    ],

    "CASE-006": [
        {
            "question_id": "Q4",
            "title": "4. Distal Empirical Point Strategy (远端经验配穴)",
            "prompt": "Which distal empirical point on the lower leg has a specific action for frozen shoulder (Lou Jian Feng) and should be needle-manipulated while the patient gently moves the affected shoulder?",
            "options": [
                "A. ST38 (Tiaokou), punctured deeply 1.5 - 2.0 cun towards BL57 (Chengshan) with active shoulder mobilization (Dong Qi method).",
                "B. SP9 (Yinlingquan) with shallow 0.2 cun puncture.",
                "C. LR3 (Taichong) with 30-minute moxibustion.",
                "D. KD1 (Yongquan) with perpendicular deep puncture."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** ST38 (Tiaokou) is the single most celebrated empirical distal point for frozen shoulder across modern and classical literature. Deep puncture directed toward BL57 combined with active arm abduction immediately restores range of motion.",
                "B": "❌ **Incorrect:** SP9 resolves dampness in the lower burner.",
                "C": "❌ **Incorrect:** LR3 soothes Liver Qi, but lacks the specific distal channel dynamic for periarthritis humeroscapularis.",
                "D": "❌ **Incorrect:** KD1 treats acute shock or hypertension, not frozen shoulder."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for frozen shoulder (Fifty-Year Shoulder) due to Qi and Blood stagnation complicated by Wind-Cold invasion?",
            "options": [
                "A. Principle: Unblock channels, invigorate Blood, dispel Cold, and eliminate Dampness from shoulder joint. Formula: Juan Bi Tang (Remove Painful Obstruction Decoction).",
                "B. Principle: Clear Liver Fire. Formula: Long Dan Xie Gan Tang.",
                "C. Principle: Purge Lower Burner heat. Formula: Tiao Wei Cheng Qi Tang.",
                "D. Principle: Astringe spontaneous sweat. Formula: Yu Ping Feng San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Juan Bi Tang is the primary prescription to unblock joint bi obstruction, warm the collaterals, and invigorate Blood in the upper limbs and shoulders.",
                "B": "❌ **Incorrect:** Long Dan Xie Gan Tang drains toxic damp-heat from Liver/Gallbladder.",
                "C": "❌ **Incorrect:** Tiao Wei Cheng Qi Tang purges gastrointestinal heat constipation.",
                "D": "❌ **Incorrect:** Yu Ping Feng San tonifies Wei Qi to prevent frequent exterior viral infections."
            }
        }
    ],

    "CASE-007": [
        {
            "question_id": "Q4",
            "title": "4. Local & Systematic Point Modifications (局部配穴与对穴)",
            "prompt": "For this 62-year-old retired woman with degenerative knee osteoarthritis presenting with joint effusion (swelling) and localized medial pain, which point set should be combined?",
            "options": [
                "A. Local: Xiyan (EX-LE5), Heding (EX-LE2), and ST35 (Dubi); Distal/Spleen: SP9 (Yinlingquan) to drain fluid dampness.",
                "B. Upper limb points: LI4, LI11, and TE5.",
                "C. Head points: DU20, Sishencong, and Taiyang.",
                "D. Chest points: CV17, CV14, and ST18."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Xiyan (Neixiyan + Waixiyan/ST35) and Heding frame the patella and unblock the articular capsule. SP9 (He-Sea of Spleen) is the premier point to resolve intra-articular dampness and joint effusion.",
                "B": "❌ **Incorrect:** Upper limb points treat elbow, wrist, or shoulder disorders, not knee osteoarthritis.",
                "C": "❌ **Incorrect:** Scalp points treat cognitive and headache disorders.",
                "D": "❌ **Incorrect:** Chest points treat cardiac and respiratory disorders."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for chronic knee bi syndrome due to Liver and Kidney deficiency with local Cold-Damp accumulation?",
            "options": [
                "A. Principle: Nourish Liver and Kidney, strengthen sinews and bones, dispel Wind-Cold-Damp, and alleviate joint pain. Formula: Du Huo Ji Sheng Tang (Angelica Pubescens and Sangjisheng Decoction).",
                "B. Principle: Clear Heat from Ying level. Formula: Qing Ying Tang.",
                "C. Principle: Purge Lung Phlegm. Formula: Ting Li Da Zao Xie Fei Tang.",
                "D. Principle: Clear Damp-Heat in Urinary Bladder. Formula: Ba Zheng San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Du Huo Ji Sheng Tang tonifies Liver and Kidney Yin/Yang to nourish degenerated cartilage and bone while warming the channels and expelling joint cold-dampness.",
                "B": "❌ **Incorrect:** Qing Ying Tang treats Wen Bing febrile delirious diseases.",
                "C": "❌ **Incorrect:** Ting Li Da Zao Xie Fei Tang drains severe pulmonary edema and pleurisy.",
                "D": "❌ **Incorrect:** Ba Zheng San treats acute UTI."
            }
        }
    ],

    "CASE-008": [
        {
            "question_id": "Q4",
            "title": "4. Local & Channel Strategy (局部阿是与经筋配穴)",
            "prompt": "In treating lateral epicondylitis (tennis elbow) affecting the extensor carpi radialis brevis tendon, which local point combination on the Hand-Yangming channel is classic?",
            "options": [
                "A. Local Ah Shi points at the lateral epicondyle + LI11 (Quchi) + LI10 (Shousanli) + LI12 (Zhouliao), using distal LI4 (Hegu) to open the channel.",
                "B. LU5 (Chize) and LU11 (Shaoshang) with bleeding.",
                "C. HT3 (Shaohai) and HT7 (Shenmen).",
                "D. PC3 (Quze) and PC6 (Neiguan)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Lateral epicondylitis is localized directly along the Hand-Yangming Large Intestine channel. LI11, LI10, LI12, and local Ah Shi points relieve extensor tendon tension, while distal LI4 unblocks the Yangming meridian.",
                "B": "❌ **Incorrect:** Lung points are located anteriorly at the bicipital tendon, not the lateral epicondyle.",
                "C": "❌ **Incorrect:** Heart points lie on the medial epicondyle (golfer's elbow).",
                "D": "❌ **Incorrect:** Pericardium points lie in the anterior middle cubital fossa."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Therapeutic Modality (治法与理疗)",
            "prompt": "Which treatment modality and principle is most effective for chronic lateral epicondylalgia with localized tendon thickening and cold stiffness?",
            "options": [
                "A. Principle: Unblock Yangming collaterals, invigorate Blood, and relax tendons. Modality: Local needle manipulation with indirect moxibustion (or warm needle moxa) and gentle plum blossom tapping around the tendon insertion.",
                "B. Principle: Clear toxic heat. Modality: Deep perpendicular puncture through the brachial artery.",
                "C. Principle: Purge Lower Burner. Modality: Strong purging electroacupuncture across the spine.",
                "D. Principle: Tonify Kidney Yang. Modality: Vigorous scarring moxa on the face."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Local moxibustion, warm needle technique, and plum blossom tapping stimulate microcirculation, collagen remodeling, and pain relief in chronic tendon degeneration.",
                "B": "❌ **Incorrect:** Puncturing major arteries is malpractice and extremely dangerous.",
                "C": "❌ **Incorrect:** Purging electroacupuncture across the spine does not address local tendon pathology.",
                "D": "❌ **Incorrect:** Scarring moxa on the face is strictly contraindicated."
            }
        }
    ],

    "CASE-009": [
        {
            "question_id": "Q4",
            "title": "4. Facial Symptom-Specific Point Pairings (循症局部配穴)",
            "prompt": "For this 32-year-old female teacher with acute Bell's Palsy, what specific point techniques should be used for: (1) Inability to close the eye, and (2) Deviation of the mouth?",
            "options": [
                "A. For eye closure: BL2 (Zanzhu) through-and-through to Yuyao, and GB14 (Yangbai) through to Yuyao; For mouth deviation: ST4 (Dicang) through-and-through to ST6 (Jiache).",
                "B. Deep perpendicular insertion into BL1 (Jingming) 2.5 cun.",
                "C. Strong electroacupuncture across the eyeball.",
                "D. Direct scarring moxibustion over the facial nerve trunk."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Subcutaneous through-and-through (Tou Zhen) needling from ST4 to ST6 restores buccinator muscle tone and corrects oral deviation. Joining BL2/GB14 towards Yuyao restores orbicularis oculi contraction to enable eye closure.",
                "B": "❌ **Incorrect:** Puncturing BL1 to 2.5 cun risks intraorbital hemorrhage and globe puncture.",
                "C": "❌ **Incorrect:** Electroacupuncture across the eyeball is strictly contraindicated.",
                "D": "❌ **Incorrect:** Scarring moxibustion on the face causes permanent disfigurement."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for acute peripheral facial paralysis (Bell's Palsy) due to Wind-Cold attacking the facial Yangming and Shaoyang channels?",
            "options": [
                "A. Principle: Expel Wind, scatter Cold, unblock facial channels, and relax sinews. Formula: Qian Zheng San (Lead Upright Powder) or Xiao Feng San.",
                "B. Principle: Clear Damp-Heat in Gallbladder. Formula: Long Dan Xie Gan Tang.",
                "C. Principle: Nourish Kidney Yin. Formula: Liu Wei Di Huang Wan.",
                "D. Principle: Warm the Middle Jiao. Formula: Li Zhong Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Qian Zheng San (composed of Bai Fu Zi, Bai Jiang Can, and Quan Xie) is the historical gold-standard formula specifically formulated to expel Wind, unblock facial collaterals, and correct oral/ocular deviation.",
                "B": "❌ **Incorrect:** Long Dan Xie Gan Tang drains toxic damp-heat, which is inappropriate for exterior wind-cold.",
                "C": "❌ **Incorrect:** Liu Wei Di Huang Wan treats constitutional Kidney Yin deficiency.",
                "D": "❌ **Incorrect:** Li Zhong Wan treats middle burner deficiency cold diarrhea."
            }
        }
    ],

    "CASE-010": [
        {
            "question_id": "Q4",
            "title": "4. Xi-Cleft & Night Sweat Point Modifications (急症与盗汗配穴)",
            "prompt": "If this 67-year-old retired patient suffers from acute distressing nocturnal palpitations accompanied by drenching night sweats, which point pairing is the premier addition?",
            "options": [
                "A. HT6 (Yinxi, Xi-Cleft of Heart) combined with KD7 (Fuliu, Jing-River of Kidney).",
                "B. LI1 (Shangyang) and LU11 (Shaoshang) bleeding.",
                "C. ST44 (Neiting) and ST45 (Lidui).",
                "D. GB34 (Yanglingquan) and BL40 (Weizhong)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** HT6 (Yinxi, Xi-Cleft of Heart) and KD7 (Fuliu, Metal/Mother point of Kidney) is the classic board exam combination to nourish Yin, stop acute cardiac palpitations, and arrest night sweats.",
                "B": "❌ **Incorrect:** Bleeding LI1 and LU11 treats acute sore throat in high fever, not night sweats.",
                "C": "❌ **Incorrect:** ST44 and ST45 purge stomach fire.",
                "D": "❌ **Incorrect:** GB34 and BL40 treat musculoskeletal lower back/knee disorders."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for chronic insomnia due to Heart and Kidney Disharmony (Xin Shen Bu Jiao) with Yin Deficiency and Empty Fire flaring?",
            "options": [
                "A. Principle: Enrich Kidney Yin, clear Heart Fire, calm the Shen, and harmonize Water and Fire. Formula: Tian Wang Bu Xin Dan (Emperor of Heaven's Special Pill to Tonify the Heart) or Huang Lian E Jiao Tang.",
                "B. Principle: Dispel exterior Wind-Cold. Formula: Ma Huang Tang.",
                "C. Principle: Purge Yangming bowel heat. Formula: Tiao Wei Cheng Qi Tang.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Tian Wang Bu Xin Dan and Huang Lian E Jiao Tang nourish Kidney Yin (E Jiao, Sheng Di Huang) while draining excessive Heart fire (Huang Lian) to re-establish communication between Water and Fire.",
                "B": "❌ **Incorrect:** Ma Huang Tang treats acute exterior wind-cold without sweating.",
                "C": "❌ **Incorrect:** Tiao Wei Cheng Qi Tang treats gastrointestinal constipation.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms Kidney Yang, which would worsen insomnia and night sweats."
            }
        }
    ],

    "CASE-011": [
        {
            "question_id": "Q4",
            "title": "4. Auditory & Tinnitus Point Modifications (耳窍随证配穴)",
            "prompt": "For this 48-year-old executive experiencing severe low-pitched roaring tinnitus and a heavy sensation of ear fullness during vertigo attacks, which point set specifically opens the ear orifices?",
            "options": [
                "A. SJ17 (Yifeng), GB2 (Tinghui), SI19 (Tinggong), and ST40 (Fenglong) to dissolve turbid phlegm obstructing the clear orifices.",
                "B. BL40 (Weizhong) and BL60 (Kunlun).",
                "C. CV4 (Guanyuan) and CV6 (Qihai).",
                "D. LU9 (Taiyuan) and LU5 (Chize)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** The periauricular trio (SJ17, GB2, SI19) directly opens the ear portals and disperses local Shaoyang phlegm-heat. ST40 (Fenglong) is essential to dissolve the turbid phlegm misting the sensory orifices.",
                "B": "❌ **Incorrect:** BL40 and BL60 treat lumbar and occipital pain, not auditory vertigo.",
                "C": "❌ **Incorrect:** CV4 and CV6 warm lower dantian, lacking local ascending action for ear fullness.",
                "D": "❌ **Incorrect:** LU9 and LU5 treat respiratory phlegm, not inner ear vestibular hydrops."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for Meniere's disease / vertigo due to Liver Yang Rising accompanied by Upward Disturbance of Phlegm-Turbidity?",
            "options": [
                "A. Principle: Subdue Liver Yang, extinguish Wind, strengthen Spleen, dry Dampness, and transform Phlegm. Formula: Ban Xia Bai Zhu Tian Ma Tang (Pinellia, Atractylodes and Gastrodia Decoction) or Tian Ma Gou Teng Yin.",
                "B. Principle: Purge Cold accumulation. Formula: Da Huang Fu Zi Tang.",
                "C. Principle: Tonify Lung Qi. Formula: Bu Fei Tang.",
                "D. Principle: Warm Kidney Yang. Formula: You Gui Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Ban Xia Bai Zhu Tian Ma Tang is the classic prescription for wind-phlegm vertigo (dizziness with heavy head and nausea), while Tian Ma Gou Teng Yin calms Liver Yang.",
                "B": "❌ **Incorrect:** Da Huang Fu Zi Tang treats cold accumulation intestinal obstruction.",
                "C": "❌ **Incorrect:** Bu Fei Tang treats chronic lung deficiency.",
                "D": "❌ **Incorrect:** You Gui Wan warms Kidney Yang, which would flare internal heat."
            }
        }
    ],

    "CASE-012": [
        {
            "question_id": "Q4",
            "title": "4. Acute Bronchospasm Empirical Pairings (平喘定惊经验穴)",
            "prompt": "During an acute paroxysmal asthma attack with severe expiratory wheezing and chest constriction, which empirical extra point and channel pairing provides immediate bronchodilation?",
            "options": [
                "A. Dingchuan (EX-B1, 0.5 cun lateral to GV14) combined with LU5 (Chize, He-Sea) and CV22 (Tiantu).",
                "B. ST36 (Zusanli) and SP3 (Taibai) with deep tonification.",
                "C. KD1 (Yongquan) and KD3 (Taixi).",
                "D. LI4 (Hegu) and LR3 (Taichong) with gentle retention."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Dingchuan (literally 'Calm Wheezing') is the premier empirical extra point for acute asthma and bronchospasm. Paired with LU5 (He-Sea point to drain Lung heat/phlegm) and CV22 (descends rebellious throat Qi), it relieves wheezing.",
                "B": "❌ **Incorrect:** ST36 and SP3 tonify Spleen Earth, which is a chronic recovery strategy, not acute rescue.",
                "C": "❌ **Incorrect:** KD1 and KD3 nourish Kidney water, lacking immediate bronchodilatory power.",
                "D": "❌ **Incorrect:** Four Gates opens Qi circulation generally but is not specific for acute bronchial constriction."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for bronchial asthma due to Phlegm-Heat Obstructing the Lung complicated by Exterior Wind-Cold constriction?",
            "options": [
                "A. Principle: Diffuse Lung Qi, clear Phlegm-Heat, descend rebellious Qi, and arrest wheezing. Formula: Ding Chuan Tang (Arrest Wheezing Decoction).",
                "B. Principle: Clear Heat from Xue level. Formula: Xi Jiao Di Huang Tang.",
                "C. Principle: Tonify Heart Blood. Formula: Si Wu Tang.",
                "D. Principle: Dispel Cold from Liver channel. Formula: Nuan Gan Jian."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Ding Chuan Tang uses Ma Huang to release the exterior and open the lungs, coupled with Bai Guo, Huang Qin, and Sang Bai Pi to clear interior phlegm-heat and calm asthma.",
                "B": "❌ **Incorrect:** Xi Jiao Di Huang Tang treats severe blood level heat hemorrhage and purpura.",
                "C": "❌ **Incorrect:** Si Wu Tang is a basic blood tonifying prescription for pale menses.",
                "D": "❌ **Incorrect:** Nuan Gan Jian warms the Liver channel for cold hernia in the scrotum."
            }
        }
    ],

    "CASE-013": [
        {
            "question_id": "Q4",
            "title": "4. Spleen-Lung Phlegm Point Modifications (健脾化痰配穴)",
            "prompt": "To treat this 42-year-old accountant's productive chronic cough where 'The Spleen is the source of phlegm and the Lung is the container of phlegm', which point formula simultaneously addresses both organs?",
            "options": [
                "A. BL13 (Feishu) and LU9 (Taiyuan) for the Lung; BL20 (Pishu), CV12 (Zhongwan), ST36 (Zusanli), and ST40 (Fenglong) for the Spleen.",
                "B. Bleeding LI11 (Quchi) and LU11 (Shaoshang).",
                "C. DU14 (Dazhui) and ST44 (Neiting) with strong purging.",
                "D. CV4 (Guanyuan) and CV3 (Zhongji) with electrical stimulation."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** BL13 and LU9 tonify Lung Qi and restore descending. BL20, CV12, and ST36 strengthen Spleen transformation so dampness is not generated, while ST40 specifically dissolves existing phlegm.",
                "B": "❌ **Incorrect:** Bleeding LI11 and LU11 clears high febrile heat, which would injure Spleen Qi.",
                "C": "❌ **Incorrect:** DU14 and ST44 purge excess fire.",
                "D": "❌ **Incorrect:** CV4 and CV3 treat lower abdominal and urogenital disorders."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for chronic productive cough with profuse white sticky sputum due to Spleen Deficiency with Damp Phlegm?",
            "options": [
                "A. Principle: Fortify the Spleen, dry Dampness, dissolve Phlegm, regulate Qi, and stop coughing. Formula: Er Chen Tang (Two-Aged Herb Decoction) or Liu Jun Zi Tang (Six Gentlemen Decoction).",
                "B. Principle: Clear toxic fire. Formula: Huang Lian Jie Du Tang.",
                "C. Principle: Purge Yangming bowel excess. Formula: Da Cheng Qi Tang.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Er Chen Tang (Ban Xia, Ju Hong, Fu Ling, Zhi Gan Cao) is the foundational prescription across Chinese medicine to dry dampness and transform phlegm. Adding Si Jun Zi Tang components yields Liu Jun Zi Tang to tonify Spleen Qi.",
                "B": "❌ **Incorrect:** Huang Lian Jie Du Tang drains extreme toxic heat, which would freeze cold phlegm.",
                "C": "❌ **Incorrect:** Da Cheng Qi Tang purges bowel feces.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan treats Kidney Yang cold."
            }
        }
    ],

    "CASE-014": [
        {
            "question_id": "Q4",
            "title": "4. Acid Regurgitation & Rebellious Qi Point Pairings (和胃降逆配穴)",
            "prompt": "For this 40-year-old manager with severe epigastric burning, acid regurgitation, and frequent belching triggered by work anger, which point pairing specifically drains Stomach Fire and descends rebellious Stomach Qi?",
            "options": [
                "A. ST44 (Neiting, Ying-Spring of Stomach) combined with PC6 (Neiguan, Confluent of Yin Wei Mai) and CV12 (Zhongwan).",
                "B. BL23 (Shenshu) and DU4 (Mingmen) with moxa.",
                "C. LU7 (Lieque) and KD6 (Zhaohai).",
                "D. HT7 (Shenmen) and SP6 (Sanyinjiao)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** ST44 (Ying-Spring Water point on Yangming Earth) is the supreme point to clear Stomach Fire, acid regurgitation, and toothache. PC6 harmonizes the middle burner and descends rebellious Qi to arrest nausea and belching; CV12 is the Front-Mu of Stomach.",
                "B": "❌ **Incorrect:** BL23 and DU4 warm Kidney Yang, which would aggravate burning heartburn.",
                "C": "❌ **Incorrect:** LU7 and KD6 treat throat, lung, and yin qiao conditions.",
                "D": "❌ **Incorrect:** HT7 and SP6 tonify Heart and Spleen for insomnia, lacking anti-reflux dynamics."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for epigastric burning pain and acid regurgitation due to Liver Qi Invading the Stomach transforming into Heat?",
            "options": [
                "A. Principle: Soothe Liver Qi, purge Liver Fire, harmonize Stomach, and descend rebellious acid. Formula: Zuo Jin Wan (Left Metal Pill) or Chai Hu Shu Gan San combined with Qing Wei San.",
                "B. Principle: Warm the Middle Jiao. Formula: Li Zhong Wan.",
                "C. Principle: Tonify Kidney Yin. Formula: Liu Wei Di Huang Wan.",
                "D. Principle: Astringe sweat. Formula: Mu Li San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Zuo Jin Wan (Huang Lian and Wu Zhu Yu in a 6:1 ratio) is the classic formula specifically formulated to treat Liver Fire invading the Stomach with acid regurgitation, hypochondriac pain, and bitter taste.",
                "B": "❌ **Incorrect:** Li Zhong Wan treats middle jiao deficiency cold.",
                "C": "❌ **Incorrect:** Liu Wei Di Huang Wan treats constitutional Kidney Yin deficiency.",
                "D": "❌ **Incorrect:** Mu Li San treats spontaneous and night sweating."
            }
        }
    ],

    "CASE-015": [
        {
            "question_id": "Q4",
            "title": "4. Moxibustion Strategy for Cockcrow Diarrhea (五更泄灸法配穴)",
            "prompt": "Which point and modality combination is the clinical gold standard to warm the Mingmen Gate of Life and arrest intractable daybreak diarrhea occurring between 3:00 AM and 5:00 AM?",
            "options": [
                "A. Indirect moxibustion (salt on umbilicus at CV8 / Shenque) plus warm needle moxibustion on CV4 (Guanyuan), BL20 (Pishu), BL23 (Shenshu), and ST36 (Zusanli).",
                "B. Bleeding LI11 (Quchi) and LU11 (Shaoshang).",
                "C. Deep reducing puncture on ST44 (Neiting) and LR2 (Xingjian).",
                "D. Cold wet cupping over the abdomen."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Daybreak diarrhea (Wu Geng Xie) is caused by Kidney Yang failing to warm Spleen Earth before dawn. Indirect moxibustion on CV8 (salt), CV4, BL20, and BL23 directly replenishes lower burner primal Yang and restores bowel control.",
                "B": "❌ **Incorrect:** Bleeding drains toxic heat and would precipitate Yang collapse in chronic diarrhea.",
                "C": "❌ **Incorrect:** Sedating ST44 and LR2 purges fire, which would severely aggravate cold diarrhea.",
                "D": "❌ **Incorrect:** Cold wet cupping introduces more cold pathogens into an already depleted abdomen."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for daybreak diarrhea (cockcrow diarrhea) due to Spleen and Kidney Yang Deficiency?",
            "options": [
                "A. Principle: Warm and supplement Spleen and Kidney Yang, astringe intestines, and stop chronic diarrhea. Formula: Si Shen Wan (Four Miracle Pill).",
                "B. Principle: Clear toxic heat in Large Intestine. Formula: Bai Tou Weng Tang.",
                "C. Principle: Purge Damp-Heat dysentery. Formula: Shao Yao Tang.",
                "D. Principle: Clear Heat from Ying level. Formula: Qing Ying Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Si Shen Wan (Bu Gu Zhi, Wu Zhu Yu, Rou Dou Kou, Wu Wei Zi) is the celebrated historical prescription specifically created to treat daybreak diarrhea by warming Mingmen fire and binding the intestines.",
                "B": "❌ **Incorrect:** Bai Tou Weng Tang treats hot amoebic dysentery with bloody pus.",
                "C": "❌ **Incorrect:** Shao Yao Tang treats damp-heat dysenteric diarrhea with tenesmus.",
                "D": "❌ **Incorrect:** Qing Ying Tang treats Wen Bing nutritive level heat."
            }
        }
    ],

    "CASE-016": [
        {
            "question_id": "Q4",
            "title": "4. Xi-Cleft Point for Acute Dysmenorrhea (郄穴止痛配穴)",
            "prompt": "During acute severe spasmodic dysmenorrhea with dark clotted menses and unbearable lower abdominal cramping, which Xi-Cleft point on the Spleen channel should be immediately stimulated with strong reducing technique?",
            "options": [
                "A. SP8 (Diji), located 3 cun inferior to SP9 on the medial border of the tibia.",
                "B. SP3 (Taibai), the Yuan-Source point.",
                "C. SP1 (Yinbai), the Jing-Well point.",
                "D. SP9 (Yinlingquan), the He-Sea point."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** SP8 (Diji) is the Xi-Cleft point of the Spleen channel. Xi-Cleft points have a supreme empirical ability to arrest acute pain and regulate Blood disorders; SP8 is the number one emergency point for severe dysmenorrhea.",
                "B": "❌ **Incorrect:** SP3 tonifies Spleen Qi chronically, lacking acute analgesic potency.",
                "C": "❌ **Incorrect:** SP1 with moxa stops abnormal uterine bleeding, not spasmodic cramping.",
                "D": "❌ **Incorrect:** SP9 resolves dampness."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for primary dysmenorrhea due to Cold Coagulation and Blood Stasis in the Uterus?",
            "options": [
                "A. Principle: Warm the channels, disperse cold, invigorate blood, and dispel stasis to alleviate pain. Formula: Shao Fu Zhu Yu Tang (Drive Out Blood Stasis from the Lower Abdomen Decoction) or Wen Jing Tang.",
                "B. Principle: Clear toxic heat. Formula: Huang Lian Jie Du Tang.",
                "C. Principle: Nourish Kidney Yin. Formula: Zuo Gui Wan.",
                "D. Principle: Dry dampness in Middle Jiao. Formula: Ping Wei San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Shao Fu Zhu Yu Tang (Xiao Hui Xiang, Gan Jiang, Rou Gui, Dang Gui, Chuan Xiong, Chi Shao, Pu Huang, Wu Ling Zhi, Yan Hu Suo, Mo Yao) specifically warms the lower abdomen, dissolves dark clots, and stops cramping.",
                "B": "❌ **Incorrect:** Huang Lian Jie Du Tang drains fire, which would freeze uterine blood.",
                "C": "❌ **Incorrect:** Zuo Gui Wan nourishes Yin, lacking blood-moving and warming herbs.",
                "D": "❌ **Incorrect:** Ping Wei San treats food dampness in the stomach."
            }
        }
    ],

    "CASE-017": [
        {
            "question_id": "Q4",
            "title": "4. Surround the Dragon Needling Technique (围刺法配穴)",
            "prompt": "What specific needling method is celebrated for acute Herpes Zoster (Shingles) to halt the spread of the rash along the intercostal nerve dermatome?",
            "options": [
                "A. 'Surrounding the Dragon' (Wei Ci): Puncturing obliquely around the borders and 'head' and 'tail' of the lesion towards the center, combined with Hua Tuo Jiaji points at the corresponding thoracic spinal segments.",
                "B. Direct deep puncture into the center of fluid-filled vesicles.",
                "C. Vigorous scarring moxibustion over the open blisters.",
                "D. Perpendicular deep puncture into the pleura."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** 'Surrounding the Dragon' (Wei Ci) consists of placing oblique needles around the perimeter of the eruption directed towards the center. This clears local toxic heat, halts blister progression, and when paired with Hua Tuo Jiaji points, prevents post-herpetic neuralgia.",
                "B": "❌ **Incorrect:** Piercing the center of active vesicles spreads viral exudate and increases risk of secondary bacterial infection.",
                "C": "❌ **Incorrect:** Scarring moxa over open vesicles causes severe thermal burns and infection.",
                "D": "❌ **Incorrect:** Puncturing into the pleura causes traumatic pneumothorax."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for acute Herpes Zoster (She Chuan Cang) due to Liver and Gallbladder Damp-Heat with Toxic Fire?",
            "options": [
                "A. Principle: Drain Liver and Gallbladder Fire, clear Damp-Heat, and purge toxic fire. Formula: Long Dan Xie Gan Tang (Gentiana Drain the Liver Decoction).",
                "B. Principle: Warm Kidney Yang. Formula: You Gui Wan.",
                "C. Principle: Tonify Spleen Qi. Formula: Shen Ling Bai Zhu San.",
                "D. Principle: Nourish Heart Yin. Formula: Tian Wang Bu Xin Dan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Long Dan Xie Gan Tang is the gold standard formula for acute Herpes Zoster with fiery burning blister pain, red tongue with yellow greasy coat, and wiry rapid pulse.",
                "B": "❌ **Incorrect:** You Gui Wan warms Kidney Yang, which would severely aggravate burning shingles.",
                "C": "❌ **Incorrect:** Shen Ling Bai Zhu San treats chronic spleen deficiency diarrhea.",
                "D": "❌ **Incorrect:** Tian Wang Bu Xin Dan treats chronic yin deficiency insomnia."
            }
        }
    ],

    "CASE-018": [
        {
            "question_id": "Q4",
            "title": "4. Pancreatic Empirical Point Modification (胰俞经验配穴)",
            "prompt": "Which empirical extra point on the upper back is specific for Diabetes / Xiao Ke (Wasting and Thirsting) and regulates pancreatic endocrine function?",
            "options": [
                "A. Weiwanxiashu (EX-B3 / Yishu), located 1.5 cun lateral to the lower border of the spinous process of the 8th thoracic vertebra (T8).",
                "B. BL11 (Dazhu) at T1.",
                "C. BL15 (Xinshu) at T5.",
                "D. BL28 (Pangguangshu) at S2."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Weiwanxiashu (EX-B3, also known as Yishu / Pancreas Shu) is located at T8, 1.5 cun lateral to the spine. It is the premier empirical point for diabetes mellitus (Xiao Ke), regulating blood glucose and pancreatic function.",
                "B": "❌ **Incorrect:** BL11 is the Hui-Meeting point of Bones.",
                "C": "❌ **Incorrect:** BL15 is the Back-Shu of Heart.",
                "D": "❌ **Incorrect:** BL28 is the Back-Shu of Bladder."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for Middle Jiao Xiao Ke due to Stomach Heat Blazing with Yin fluid consumption (polyphagia, rapid hunger, dry mouth, weight loss)?",
            "options": [
                "A. Principle: Clear Stomach Fire, enrich Kidney and Stomach Yin, and generate body fluids. Formula: Yu Nu Jian (Jade Woman Decoction).",
                "B. Principle: Warm the Middle Burner. Formula: Li Zhong Tang.",
                "C. Principle: Purge Cold accumulation. Formula: Da Huang Fu Zi Tang.",
                "D. Principle: Dispel exterior Wind-Cold. Formula: Jing Fang Bai Du San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Yu Nu Jian (Shi Gao, Zhi Mu, Sheng Di Huang, Mai Men Dong, Niu Xi) specifically clears blazing Stomach Heat while nourishing Yin fluids, making it the classic formula for middle jiao wasting and thirsting.",
                "B": "❌ **Incorrect:** Li Zhong Tang warms spleen cold, which would fan stomach fire.",
                "C": "❌ **Incorrect:** Da Huang Fu Zi Tang treats cold obstipation.",
                "D": "❌ **Incorrect:** Jing Fang Bai Du San treats early wind-cold exterior infections."
            }
        }
    ],

    "CASE-019": [
        {
            "question_id": "Q4",
            "title": "4. Trigeminal Branch-Specific Modifications (三叉神经分支配穴)",
            "prompt": "For this 55-year-old bank teller with trigeminal neuralgia, how should the point selection be customized if the trigger zone is in: (1) The Maxillary branch (V2 - cheek/upper jaw), versus (2) The Mandibular branch (V3 - lower jaw/chin)?",
            "options": [
                "A. For V2 (Maxillary): ST2 (Sibai), LI20 (Yingxiang), and ST3 (Juliao); For V3 (Mandibular): ST5 (Daying), ST6 (Jiache), and ST7 (Xiaguan).",
                "B. For V2: BL1 (Jingming) and BL2 (Zanzhu); For V3: DU20 (Baihui) and Sishencong.",
                "C. For V2: LU5 (Chize); For V3: PC6 (Neiguan).",
                "D. For V2: ST36 (Zusanli); For V3: SP6 (Sanyinjiao)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Trigeminal neuralgia point prescriptions must precisely target the affected branch: ST2, LI20, ST3 lie over the infraorbital foramen (V2 Maxillary nerve), while ST5, ST6, ST7 lie over the mental foramen and masseter (V3 Mandibular nerve).",
                "B": "❌ **Incorrect:** BL1 and BL2 correspond to the Ophthalmic branch (V1), not V2 or V3.",
                "C": "❌ **Incorrect:** Upper limb points alone cannot precisely stimulate local facial nerve branches.",
                "D": "❌ **Incorrect:** Lower limb points provide distal balancing but do not address local neuropathic trigger zones."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for trigeminal neuralgia due to Stomach Fire and Wind-Heat attacking the facial Yangming channels?",
            "options": [
                "A. Principle: Purge Stomach Fire, clear Wind-Heat, unblock collaterals, and alleviate facial spasmodic pain. Formula: Qing Wei San (Clear the Stomach Powder) combined with Qian Zheng San.",
                "B. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan.",
                "C. Principle: Tonify Spleen Qi. Formula: Bu Zhong Yi Qi Tang.",
                "D. Principle: Nourish Heart Blood. Formula: Gui Pi Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Qing Wei San (Huang Lian, Sheng Di Huang, Mu Dan Pi, Dang Gui, Sheng Ma) drains Stomach Fire and cools Blood, while Qian Zheng San expels Wind and stops facial nerve spasms.",
                "B": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms Kidney Yang, exacerbating facial fire.",
                "C": "❌ **Incorrect:** Bu Zhong Yi Qi Tang treats organ prolapse and qi deficiency.",
                "D": "❌ **Incorrect:** Gui Pi Tang treats spleen-heart insomnia and amnesia."
            }
        }
    ],

    "CASE-020": [
        {
            "question_id": "Q4",
            "title": "4. Hemiplegic Motor Recovery Point Strategy (中风偏瘫经筋配穴)",
            "prompt": "For this 68-year-old stroke patient with upper extremity flaccidity and hand contracture, which channel distribution and point set is standard for restoring motor function?",
            "options": [
                "A. Hand-Yangming Large Intestine channel points: LI15 (Jianyu), LI11 (Quchi), LI10 (Shousanli), LI4 (Hegu), combined with Baxie (EX-UE9).",
                "B. Hand-Shaoyin Heart channel points: HT3, HT7, HT9.",
                "C. Foot-Taiyin Spleen channel points: SP1, SP3, SP9.",
                "D. Foot-Shaoyin Kidney channel points: KD1, KD3, KD7."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** In post-stroke rehabilitation, Yangming channels are celebrated as having 'Abundant Qi and Abundant Blood' (Duo Qi Duo Xue). Focusing on LI15, LI11, LI10, LI4, and Baxie restores motor nerve conduction and tendon flexibility in the paretic arm.",
                "B": "❌ **Incorrect:** Heart points alone do not cover the extensors of the arm.",
                "C": "❌ **Incorrect:** Spleen points are located on the leg, not the paretic arm.",
                "D": "❌ **Incorrect:** Kidney points are located on the lower extremity."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for post-stroke hemiplegia due to Qi Deficiency and Blood Stasis obstructing the channels and collaterals?",
            "options": [
                "A. Principle: Strongly tonify original Qi, invigorate Blood, dispel stasis, and unblock channels. Formula: Bu Yang Huan Wu Tang (Tonify Yang to Restore Five-Tenths Decoction).",
                "B. Principle: Purge Gallbladder Fire. Formula: Long Dan Xie Gan Tang.",
                "C. Principle: Clear Heat from Ying level. Formula: Qing Ying Tang.",
                "D. Principle: Warm Kidney Yang. Formula: You Gui Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Bu Yang Huan Wu Tang (with massive dose of Huang Qi 60-120g plus Dang Gui Wei, Chi Shao, Chuan Xiong, Tao Ren, Hong Hua, Di Long) is the world-renowned historic formula for post-stroke hemiplegia and facial paralysis.",
                "B": "❌ **Incorrect:** Long Dan Xie Gan Tang drains damp-heat, which would deplete Qi.",
                "C": "❌ **Incorrect:** Qing Ying Tang treats Wen Bing fever.",
                "D": "❌ **Incorrect:** You Gui Wan treats kidney yang collapse without blood-activating herbs."
            }
        }
    ],

    "CASE-021": [
        {
            "question_id": "Q4",
            "title": "4. Menopausal Hot Flash & Night Sweat Pairings (潮热盗汗配穴)",
            "prompt": "If this 51yo librarian suffers from severe nocturnal hot flashes and drenching night sweats that awaken her multiple times each night, which point combination specifically controls Yin deficiency sweat?",
            "options": [
                "A. HT6 (Yinxi, Xi-Cleft of Heart) combined with KD7 (Fuliu, Jing-River of Kidney) and KD6 (Zhaohai).",
                "B. LI11 (Quchi) and LU11 (Shaoshang) with bleeding.",
                "C. ST44 (Neiting) and ST45 (Lidui).",
                "D. BL40 (Weizhong) and BL60 (Kunlun)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** HT6 (Yinxi) and KD7 (Fuliu) is the textbook synergy for stopping night sweats. KD6 (Confluent of Yin Qiao) nourishes Kidney Yin and moistens dryness to subdue hot flashes.",
                "B": "❌ **Incorrect:** Bleeding LI11/LU11 treats acute fever and sore throat.",
                "C": "❌ **Incorrect:** ST44/ST45 drains stomach heat toothache.",
                "D": "❌ **Incorrect:** BL40/BL60 treats lower back and neck disorders."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for menopausal syndrome due to Kidney Yin Deficiency with Empty Fire flaring?",
            "options": [
                "A. Principle: Nourish Kidney Yin, enrich body fluids, clear empty heat, and calm the Shen. Formula: Zhi Bai Di Huang Wan (Anemarrhena, Phellodendron and Rehmannia Pill) or Zuo Gui Wan.",
                "B. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan.",
                "C. Principle: Purge Damp-Heat from Gallbladder. Formula: Long Dan Xie Gan Tang.",
                "D. Principle: Dry dampness in Middle Jiao. Formula: Ping Wei San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Zhi Bai Di Huang Wan (Liu Wei Di Huang Wan plus Zhi Mu and Huang Bai) specifically drains empty fire flaring from depleted Kidney Yin, relieving hot flashes, night sweats, and vaginal dryness.",
                "B": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms Kidney Yang, which would increase hot flashes.",
                "C": "❌ **Incorrect:** Long Dan Xie Gan Tang drains excess damp-heat.",
                "D": "❌ **Incorrect:** Ping Wei San treats food stagnation."
            }
        }
    ],

    "CASE-022": [
        {
            "question_id": "Q4",
            "title": "4. Antipruritic Point Synergy for Urticaria (祛风止痒配穴)",
            "prompt": "To stop intense generalized itching and resolve widespread hives, which celebrated point synergy acts on the Blood level to expel Wind ('To treat Wind, first treat Blood; once Blood moves, Wind naturally dies')?",
            "options": [
                "A. SP10 (Xuehai, Sea of Blood) paired with BL17 (Geshu, Hui-Meeting of Blood), LI11 (Quchi), and SP6 (Sanyinjiao).",
                "B. CV4 (Guanyuan) and CV6 (Qihai).",
                "C. ST36 (Zusanli) and SP3 (Taibai).",
                "D. KD1 (Yongquan) and KD3 (Taixi)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** '治风先治血，血行风自灭' (To treat Wind, first treat Blood; when Blood moves, Wind spontaneously extinguishes). SP10 and BL17 invigorate and cool Blood, while LI11 dispels exterior Wind-Heat and clears skin rashes.",
                "B": "❌ **Incorrect:** CV4 and CV6 warm and tonify primal Qi, lacking cutaneous antipruritic power.",
                "C": "❌ **Incorrect:** ST36 and SP3 tonify digestion.",
                "D": "❌ **Incorrect:** KD1 and KD3 nourish Kidney water."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for acute urticaria (hives) due to Wind-Heat Invading the Skin and Blood Level?",
            "options": [
                "A. Principle: Dispel Wind, clear Heat, cool Blood, and stop itching. Formula: Xiao Feng San (Eliminate Wind Powder).",
                "B. Principle: Warm the Middle Jiao. Formula: Li Zhong Wan.",
                "C. Principle: Purge Cold accumulation. Formula: Da Huang Fu Zi Tang.",
                "D. Principle: Tonify Kidney Yang. Formula: You Gui Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Xiao Feng San (Jing Jie, Fang Feng, Niu Bang Zi, Chan Tui, Cang Zhu, Ku Shen, Shi Gao, Zhi Mu, Sheng Di Huang, Dang Gui, Hei Zhi Ma) is the premier dermatological formula for acute itchy wheals and hives.",
                "B": "❌ **Incorrect:** Li Zhong Wan treats spleen cold.",
                "C": "❌ **Incorrect:** Da Huang Fu Zi Tang treats cold obstipation.",
                "D": "❌ **Incorrect:** You Gui Wan treats kidney yang deficiency."
            }
        }
    ],

    "CASE-023": [
        {
            "question_id": "Q4",
            "title": "4. Emergency Resuscitation Technique (晕针急救刺灸法)",
            "prompt": "When a needle fainting reaction (vasovagal syncope) occurs, what is the immediate needle manipulation and patient positioning protocol?",
            "options": [
                "A. Immediately withdraw all needles; position patient supine with feet slightly elevated; pinch or puncture GV26 (Shuigou / Renzhong) obliquely upward with strong stimulation, and press PC6 (Neiguan).",
                "B. Leave all needles in and twist them vigorously to increase stimulation.",
                "C. Instruct the patient to stand up immediately and walk briskly.",
                "D. Apply ice packs to the neck and chest."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Clean Needle Technique (CNT) standard: Immediately remove all needles, place patient flat with legs elevated to promote cerebral perfusion, provide warm water, and stimulate GV26 and PC6 to revive consciousness.",
                "B": "❌ **Incorrect:** Leaving needles in and twisting them will intensify vasovagal shock.",
                "C": "❌ **Incorrect:** Standing up causes orthostatic pooling and secondary syncope/fall injury.",
                "D": "❌ **Incorrect:** Ice packs induce peripheral vasoconstriction and shivering shock."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Clinical Prevention & Vital Signs Protocol (预防与生命体征)",
            "prompt": "To prevent needle syncope in clinical practice according to professional acupuncture safety standards, what clinical protocol must always be enforced?",
            "options": [
                "A. Verify the patient has eaten within 2-4 hours, avoid treating patients in an upright sitting posture if anxious or fatigued, use gentle technique on initial visits, and monitor pulse/pallor.",
                "B. Require all patients to fast for 12 hours prior to treatment.",
                "C. Puncture at least 30 needles on the first visit to test tolerance.",
                "D. Apply strong electroacupuncture to anxious patients."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Hunger, extreme fatigue, emotional nervousness, and upright sitting posture are the leading clinical triggers of vasovagal fainting. Confirming nutritional intake and treating in supine posture prevents syncope.",
                "B": "❌ **Incorrect:** Fasting increases hypoglycemia and dramatically increases fainting risk.",
                "C": "❌ **Incorrect:** Over-needling triggers nervous system shock.",
                "D": "❌ **Incorrect:** Strong electroacupuncture in anxious patients induces panic."
            }
        }
    ],

    "CASE-024": [
        {
            "question_id": "Q4",
            "title": "4. Hemoptysis & Xi-Cleft Point Modification (咳血与郄穴配穴)",
            "prompt": "If this 24-year-old cystic fibrosis patient experiences acute coughing of blood-streaked sputum (hemoptysis), which Xi-Cleft point of the Lung channel must be prioritized to arrest pulmonary capillary bleeding?",
            "options": [
                "A. LU6 (Kongzui), located 7 cun proximal to the wrist crease on the line connecting LU9 and LU5.",
                "B. LU1 (Zhongfu).",
                "C. LU9 (Taiyuan).",
                "D. LU11 (Shaoshang)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** LU6 (Kongzui) is the Xi-Cleft point of the Lung channel. Xi-Cleft points treat acute emergency disorders and acute bleeding; LU6 is the premier point in TCM to stop coughing of blood (hemoptysis) and acute asthma.",
                "B": "❌ **Incorrect:** LU1 is Front-Mu point, regulating lung qi chronically.",
                "C": "❌ **Incorrect:** LU9 is Yuan-Source point, tonifying lung qi and vessels.",
                "D": "❌ **Incorrect:** LU11 treats acute sore throat fever."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for chronic cough with blood-streaked sputum and emaciation due to Lung and Kidney Yin Deficiency with Empty Fire flaring?",
            "options": [
                "A. Principle: Nourish Lung and Kidney Yin, clear Empty Heat, moisten dryness, and arrest hemoptysis. Formula: Bai He Gu Jin Tang (Lily Bulb Decoction to Preserve Metal).",
                "B. Principle: Clear toxic heat. Formula: Huang Lian Jie Du Tang.",
                "C. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan.",
                "D. Principle: Dry dampness in Middle Jiao. Formula: Ping Wei San."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Bai He Gu Jin Tang (Bai He, Sheng Di Huang, Shu Di Huang, Mai Men Dong, Xuan Shen, Bei Mu, Jie Geng, Dang Gui, Bai Shao, Gan Cao) is the celebrated formula to nourish pulmonary and renal Yin and stop hemoptysis.",
                "B": "❌ **Incorrect:** Huang Lian Jie Du Tang treats toxic fire.",
                "C": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms Kidney Yang, which would worsen lung bleeding.",
                "D": "❌ **Incorrect:** Ping Wei San treats food stagnation."
            }
        }
    ],

    "CASE-025": [
        {
            "question_id": "Q4",
            "title": "4. Fluid Lubrication Point Synergy (润肠通便配穴)",
            "prompt": "For this 89-year-old bedridden woman with severe constipation due to fluid and blood depletion, which point pairing promotes bowel peristalsis and generates intestinal fluids without harsh purging?",
            "options": [
                "A. TE6 (Zhigou) combined with KD6 (Zhaohai), ST25 (Tianshu), and BL20 (Pishu).",
                "B. Bleeding LI1 (Shangyang) and ST45 (Lidui).",
                "C. Sedating LI11 and ST44.",
                "D. BL40 (Weizhong) with plum blossom bleeding."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** TE6 (Zhigou) regulates San Jiao Qi circulation in the intestines, while KD6 (Zhaohai) generates fluids ('Zeng Ye Xing Zhou' - increasing fluids to move the boat). ST25 regulates the Large Intestine, and BL20 supports Spleen transport.",
                "B": "❌ **Incorrect:** Bleeding Jing-Well points treats acute coma, not geriatric constipation.",
                "C": "❌ **Incorrect:** Sedating LI11/ST44 purges heat but fails to generate dry fluids.",
                "D": "❌ **Incorrect:** Bleeding BL40 releases blood stasis, which would deplete elderly blood."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for geriatric constipation due to Blood and Yin Deficiency with Intestinal Dryness?",
            "options": [
                "A. Principle: Nourish Blood, enrich Yin, moisten the intestines, and promote bowel movement. Formula: Run Chang Wan (Moisten the Intestines Pill) or Ma Zi Ren Wan (Hemp Seed Pill).",
                "B. Principle: Drastically purge cold. Formula: San Wu Bei Ji Wan.",
                "C. Principle: Drain toxic fire. Formula: Xie Xin Tang.",
                "D. Principle: Warm Kidney Yang. Formula: You Gui Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Run Chang Wan (Huo Ma Ren, Tao Ren, Dang Gui, Sheng Di Huang, Zhi Ke) gently lubricates the dry intestinal canal without harsh purging, making it the classic formula for elderly constipation.",
                "B": "❌ **Incorrect:** San Wu Bei Ji Wan is a harsh toxic emergency purgative.",
                "C": "❌ **Incorrect:** Xie Xin Tang treats toxic fire bleeding.",
                "D": "❌ **Incorrect:** You Gui Wan treats kidney yang deficiency."
            }
        }
    ],

    "CASE-026": [
        {
            "question_id": "Q4",
            "title": "4. Empirical Biliary Colic Point Modification (胆囊穴经验配穴)",
            "prompt": "For this 47-year-old chef with acute biliary colic, right hypochondriac pain, and positive Murphy's sign, which empirical extra point is specific for gallbladder disorders?",
            "options": [
                "A. Dannangxue (EX-LE6), located 1.0 to 2.0 cun inferior to GB34 (Yanglingquan) on the right leg, combined with GB24 (Riyue, Front-Mu) and LR14 (Qimen).",
                "B. Lanweixue (EX-LE7) at ST36.",
                "C. Yaotongxue (EX-UE7) on the hand.",
                "D. Zigong (EX-CA1) on the abdomen."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Dannangxue (EX-LE6) is the celebrated empirical point for acute cholecystitis, gallstones, and biliary colic. Palpated on the right leg below GB34, it immediately relieves biliary spasm and sphincter of Oddi hypertension.",
                "B": "❌ **Incorrect:** Lanweixue is specific for appendicitis, not cholecystitis.",
                "C": "❌ **Incorrect:** Yaotongxue treats acute lumbar sprain.",
                "D": "❌ **Incorrect:** Zigong treats uterine prolapse and infertility."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for acute cholecystitis / biliary colic due to Liver and Gallbladder Damp-Heat with Stone Obstruction?",
            "options": [
                "A. Principle: Clear Heat, drain Dampness, soothe Liver Qi, unblock Gallbladder, and expel stones. Formula: Da Chai Hu Tang (Major Bupleurum Decoction) or Long Dan Xie Gan Tang.",
                "B. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan.",
                "C. Principle: Tonify Spleen Qi. Formula: Shen Ling Bai Zhu San.",
                "D. Principle: Nourish Heart Yin. Formula: Tian Wang Bu Xin Dan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Da Chai Hu Tang harmonizes Shaoyang and purges Yangming excess, relieving acute biliary colic, jaundice, and nausea. Long Dan Xie Gan Tang drains toxic damp-heat.",
                "B": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms kidney yang, worsening acute inflammation.",
                "C": "❌ **Incorrect:** Shen Ling Bai Zhu San treats chronic spleen deficiency diarrhea.",
                "D": "❌ **Incorrect:** Tian Wang Bu Xin Dan treats insomnia."
            }
        }
    ],

    "CASE-027": [
        {
            "question_id": "Q4",
            "title": "4. Hematuric Dysuria Point Modifications (血淋凉血止血配穴)",
            "prompt": "For this 33-year-old nurse with acute bloody dysuria (Xue Lin), burning micturition, and visible red urine, which point set specifically cools Blood and arrests hematuria?",
            "options": [
                "A. SP10 (Xuehai) paired with BL28 (Pangguangshu), CV3 (Zhongji), and SP9 (Yinlingquan).",
                "B. CV4 (Guanyuan) and DU4 (Mingmen) with moxibustion.",
                "C. LU7 (Lieque) and BL60 (Kunlun).",
                "D. ST36 (Zusanli) and SP3 (Taibai)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** SP10 (Sea of Blood) cools blood heat and arrests hematuria. CV3 (Front-Mu of Bladder) and BL28 (Back-Shu of Bladder) clear local urinary heat, while SP9 drains toxic dampness.",
                "B": "❌ **Incorrect:** Moxa on CV4/DU4 adds Yang fire, which would exacerbate bleeding and urinary burning.",
                "C": "❌ **Incorrect:** LU7 and BL60 treat exterior headaches, not acute hematuria.",
                "D": "❌ **Incorrect:** ST36 and SP3 tonify Spleen digestion."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for acute bloody dysuria (Xue Lin) due to Lower Jiao Damp-Heat injuring urinary capillaries?",
            "options": [
                "A. Principle: Clear Heat, drain Dampness, cool Blood, and stop hematuria. Formula: Xiao Ji Yin Zi (Cephalanoplos Decoction) or Ba Zheng San.",
                "B. Principle: Warm Kidney Yang. Formula: You Gui Wan.",
                "C. Principle: Tonify Spleen Qi. Formula: Bu Zhong Yi Qi Tang.",
                "D. Principle: Dispel exterior Wind-Cold. Formula: Ma Huang Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Xiao Ji Yin Zi (Xiao Ji, Ou Jie, Pu Huang, Sheng Di Huang, Hua Shi, Mu Tong, Zhu Ling, Dan Zhu Ye) is the celebrated formula specifically created for heat-induced hematuria and painful bloody urination.",
                "B": "❌ **Incorrect:** You Gui Wan warms kidney yang, worsening acute urinary fire.",
                "C": "❌ **Incorrect:** Bu Zhong Yi Qi Tang treats organ prolapse.",
                "D": "❌ **Incorrect:** Ma Huang Tang treats exterior cold."
            }
        }
    ],

    "CASE-028": [
        {
            "question_id": "Q4",
            "title": "4. Ocular Point Modifications for Retinopathy (眼底内障配穴)",
            "prompt": "For this 63-year-old watchmaker with diabetic retinopathy presenting with blurry vision and eye fatigue due to Liver and Kidney Yin deficiency, which local and distal points brighten the eyes?",
            "options": [
                "A. BL1 (Jingming), GB20 (Fengchi), Taiyang, BL18 (Ganshu), BL23 (Shenshu), and KD3 (Taixi).",
                "B. LI11 (Quchi) and ST44 (Neiting) with strong purging.",
                "C. SP1 (Yinbai) and LU11 (Shaoshang) bleeding.",
                "D. CV8 (Shenque) and CV4 (Guanyuan) with scarring moxa."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** BL1 (Bright Eyes) is the premier local point for retinal nourishment. GB20 guides clear Yang to the eyes. BL18 (Liver Shu) and BL23 (Kidney Shu) treat the root essence deficiency (Liver opens to eyes; Kidney rules Water/Essence).",
                "B": "❌ **Incorrect:** Purging LI11/ST44 treats high fever toothache, not retinal degeneration.",
                "C": "❌ **Incorrect:** Bleeding SP1/LU11 treats acute emergency fever.",
                "D": "❌ **Incorrect:** Scarring moxa on the abdomen does not treat retinal microvascular disease."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for diabetic ocular complications due to Liver and Kidney Yin Deficiency with Essence depletion?",
            "options": [
                "A. Principle: Nourish Liver and Kidney Yin, secure Essence, and brighten the eyes. Formula: Qi Ju Di Huang Wan (Lycium Fruit, Chrysanthemum and Rehmannia Pill) or Ming Mu Di Huang Wan.",
                "B. Principle: Purge Cold accumulation. Formula: San Wu Bei Ji Wan.",
                "C. Principle: Clear Damp-Heat in Gallbladder. Formula: Long Dan Xie Gan Tang.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Qi Ju Di Huang Wan (Liu Wei Di Huang Wan plus Gou Qi Zi and Ju Hua) is the classic ophthalmology formula to nourish Kidney water and Liver blood to restore visual acuity.",
                "B": "❌ **Incorrect:** San Wu Bei Ji Wan is a harsh purgative.",
                "C": "❌ **Incorrect:** Long Dan Xie Gan Tang drains acute damp-heat fire.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms kidney yang."
            }
        }
    ],

    "CASE-029": [
        {
            "question_id": "Q4",
            "title": "4. Emergency Hemostatic Moxibustion (隐白灸法止血配穴)",
            "prompt": "For this 41-year-old social worker with acute continuous pale uterine bleeding (Beng Lou), which empirical point and modality is celebrated for stopping uterine hemorrhage?",
            "options": [
                "A. Direct or indirect moxibustion on SP1 (Yinbai, Jing-Well of Spleen), paired with DU20 (Baihui) to raise sunken Yang and CV6 (Qihai).",
                "B. Bleeding LI1 (Shangyang) and LU11 (Shaoshang).",
                "C. Deep reducing puncture into SP10 (Xuehai).",
                "D. Electroacupuncture across the groin."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Moxibustion on SP1 (Yinbai) is the supreme empirical technique in Chinese gynecology to stop uterine bleeding by fortifying the Spleen's function of controlling Blood. DU20 raises sunken Yang Qi to secure Chong and Ren.",
                "B": "❌ **Incorrect:** Bleeding Jing-Well points treats high fever, not uterine bleeding.",
                "C": "❌ **Incorrect:** Strong reducing on SP10 breaks blood stasis, which could worsen severe hemorrhage.",
                "D": "❌ **Incorrect:** Electroacupuncture across the groin is contraindicated in active uterine hemorrhage."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for uterine flooding and trickling (Beng Lou) due to Spleen Failing to Control Blood (Pi Bu Tong Xue)?",
            "options": [
                "A. Principle: Tonify Spleen Qi, raise sunken Yang, strengthen Chong and Ren, and arrest uterine hemorrhage. Formula: Gu Chong Tang (Stabilize the Gushing Decoction) or Gui Pi Tang (Restore the Spleen Decoction).",
                "B. Principle: Clear toxic heat. Formula: Huang Lian Jie Du Tang.",
                "C. Principle: Drain Liver Fire. Formula: Long Dan Xie Gan Tang.",
                "D. Principle: Warm the channels and break stasis. Formula: Wen Jing Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Gu Chong Tang (Zhang Xi-Chun's classic with Bai Zhu, Huang Qi, Shan Zhu Yu, Duan Long Gu, Duan Mu Li, Hai Piao Xiao) specifically tonifies Qi to hold Blood and astringes torrential menses.",
                "B": "❌ **Incorrect:** Huang Lian Jie Du Tang treats toxic fire.",
                "C": "❌ **Incorrect:** Long Dan Xie Gan Tang treats liver damp-heat.",
                "D": "❌ **Incorrect:** Wen Jing Tang treats cold blood stasis dysmenorrhea."
            }
        }
    ],

    "CASE-030": [
        {
            "question_id": "Q4",
            "title": "4. Micro-Needling Strategy for Facial Spasm (面肌痉挛浅刺配穴)",
            "prompt": "In treating involuntary hemifacial spasm (twitching of orbicularis oculi and zygomaticus muscles), what needle technique must be observed to avoid triggering hyperactive twitches?",
            "options": [
                "A. Gentle shallow subcutaneous insertion into local points (GB14, Yuyao, ST4, ST6, Ashi) with fine needles (0.16mm-0.20mm), strictly avoiding strong electroacupuncture.",
                "B. Deep perpendicular puncture with strong electroacupuncture at 100 Hz continuous wave.",
                "C. Puncturing deeply into the facial nerve trunk with heavy pecking manipulation.",
                "D. Vigorous scarring moxibustion over the temple."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Facial spasm involves hypersensitive motor nerve hyperexcitability. High-frequency electroacupuncture or heavy manipulation can trigger intractable facial contracture; gentle shallow threading (Tou Zhen) relaxes hypertonic fascial planes.",
                "B": "❌ **Incorrect:** 100 Hz electroacupuncture aggravates facial muscle tetany and spasms.",
                "C": "❌ **Incorrect:** Pecking the facial nerve trunk risks permanent axonal transection.",
                "D": "❌ **Incorrect:** Scarring moxa on the face is strictly contraindicated."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for hemifacial spasm due to Wind-Phlegm and Blood Stasis obstructing the facial collaterals?",
            "options": [
                "A. Principle: Extinguish internal Wind, dissolve Phlegm, nourish Blood, relax sinews, and alleviate facial spasms. Formula: Shao Yao Gan Cao Tang (Peony and Licorice Decoction) combined with Qian Zheng San.",
                "B. Principle: Clear Damp-Heat in Gallbladder. Formula: Long Dan Xie Gan Tang.",
                "C. Principle: Purge Yangming bowel excess. Formula: Da Cheng Qi Tang.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Shao Yao Gan Cao Tang (Bai Shao 30g + Zhi Gan Cao 10g) is the celebrated classical formula to nourish Blood, soften tendons, and relieve acute muscle spasms across Chinese medicine.",
                "B": "❌ **Incorrect:** Long Dan Xie Gan Tang drains excess damp-heat fire.",
                "C": "❌ **Incorrect:** Da Cheng Qi Tang purges constipation.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms kidney yang."
            }
        }
    ],

    "CASE-031": [
        {
            "question_id": "Q4",
            "title": "4. Emergency Cardiac Management Protocol (胸痹心痛急救程序)",
            "prompt": "When this 71yo patient presents with sudden severe crushing substernal chest pressure radiating down the left arm with cyanotic lips and diaphoresis, what is the mandatory immediate clinical action?",
            "options": [
                "A. EMERGENCY RED FLAG: Immediately activate 911 / emergency EMS dispatch; keep patient in resting semi-Fowler position; monitor vitals and needle PC6 (Neiguan) + CV17 (Danzhong) while waiting for paramedics.",
                "B. Tell the patient to lie flat and retain needles for 60 minutes.",
                "C. Perform vigorous cupping over the anterior chest.",
                "D. Give the patient cold ice water to drink."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** True Heart Pain / Acute Coronary Syndrome is an absolute medical emergency with high immediate mortality. The acupuncturist must dispatch 911 immediately while maintaining airway and stimulating PC6 to support coronary perfusion.",
                "B": "❌ **Incorrect:** Delaying EMS transport while retaining needles is medical negligence.",
                "C": "❌ **Incorrect:** Cupping over the anterior chest during acute myocardial infarction is dangerous.",
                "D": "❌ **Incorrect:** Cold drinks cause vagal spasms and worsen cardiac shock."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Post-Acute Classical Herbal Formula Strategy (活血通脉方剂)",
            "prompt": "Following emergency hospital coronary stabilization, what classical formula is standard to invigorate Heart Blood, unblock coronary collateral stasis, and prevent recurrent angina?",
            "options": [
                "A. Principle: Invigorate Blood, dissolve stasis, unblock coronary vessels, and alleviate thoracic pain. Formula: Guan Xin Er Hao (Coronary Heart Disease Formula No. 2) or Dan Shen Yin.",
                "B. Principle: Purge Lower Burner. Formula: Tiao Wei Cheng Qi Tang.",
                "C. Principle: Dispel exterior Wind-Cold. Formula: Ma Huang Tang.",
                "D. Principle: Clear toxic fire. Formula: Wu Wei Xiao Du Yin."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Dan Shen Yin (Dan Shen, Tan Xiang, Sha Ren) and Guan Xin Er Hao (Dan Shen, Chuan Xiong, Chi Shao, Hong Hua, Jiang Xiang) are the premier formulas for coronary blood stasis and angina pectoris.",
                "B": "❌ **Incorrect:** Tiao Wei Cheng Qi Tang treats constipation.",
                "C": "❌ **Incorrect:** Ma Huang Tang treats acute exterior cold.",
                "D": "❌ **Incorrect:** Wu Wei Xiao Du Yin treats boils and abscesses."
            }
        }
    ],

    "CASE-032": [
        {
            "question_id": "Q4",
            "title": "4. Acute Mania Ghost Point & Jing-Well Bleeding (狂证鬼穴急救配穴)",
            "prompt": "For this 29yo male exhibiting acute manic agitation, incoherent shouting, and uncontrollable violent hyperactivity, which classical point strategy drains excess phlegm-fire and awakens the Shen?",
            "options": [
                "A. Prick Twelve Jing-Well points (bleed) to drain heat, combined with Sun Si-Miao Ghost Points: GV26 (Shuigou / Ghost Palace), PC8 (Laogong / Ghost Cave), and ST40 (Fenglong).",
                "B. Tonify BL23 (Shenshu) and DU4 (Mingmen) with moxa.",
                "C. Retain needles at SP6 (Sanyinjiao) and ST36 (Zusanli) for 2 hours.",
                "D. Puncture KD1 (Yongquan) with deep heating needles."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Pricking the Twelve Jing-Well points drains extreme Yang fire and calms acute mania. Sun Si-Miao's Ghost Points (GV26, PC8) clear phlegm-fire agitating the Heart, and ST40 dissolves turbid phlegm misting the mind.",
                "B": "❌ **Incorrect:** Moxa on BL23/DU4 feeds Yang fire and intensifies psychotic agitation.",
                "C": "❌ **Incorrect:** Tonifying SP6/ST36 fails to clear violent acute mania.",
                "D": "❌ **Incorrect:** Heating needles worsen fire."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for manic psychosis (Kuang Zheng) due to Phlegm-Fire Agitating the Shen?",
            "options": [
                "A. Principle: Purge Fire, dissolve Phlegm, open the sensory orifices, and anchor the Shen. Formula: Meng Shi Gun Tan Wan (Vaporize Phlegm Pill) or Sheng Tie Luo Yin.",
                "B. Principle: Tonify Spleen Qi. Formula: Si Jun Zi Tang.",
                "C. Principle: Warm Kidney Yang. Formula: You Gui Wan.",
                "D. Principle: Nourish Lung Yin. Formula: Sha Shen Mai Dong Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Meng Shi Gun Tan Wan (Meng Shi, Da Huang, Huang Qin, Chen Xiang) and Sheng Tie Luo Yin are the premier historical formulas to aggressively purge stubborn phlegm-fire agitating the brain and psyche.",
                "B": "❌ **Incorrect:** Si Jun Zi Tang is for mild spleen qi deficiency.",
                "C": "❌ **Incorrect:** You Gui Wan warms kidney yang.",
                "D": "❌ **Incorrect:** Sha Shen Mai Dong Tang treats dry cough."
            }
        }
    ],

    "CASE-033": [
        {
            "question_id": "Q4",
            "title": "4. Sifeng Extra Point Technique for Infantile Malnutrition (四缝点刺配穴)",
            "prompt": "In treating this 4yo boy with infantile malnutrition (Gan Ji), food accumulation, and pot-bellied emaciation, what specific technique at Sifeng (EX-UE10) is mandatory?",
            "options": [
                "A. Prick Sifeng (EX-UE10) on the palmar aspect of the 2nd to 5th proximal interphalangeal joints with a three-edged needle, and squeeze out yellow lymphatic/viscous fluid.",
                "B. Insert 2.0 cun perpendicularly into Sifeng and retain for 30 minutes.",
                "C. Apply scarring moxibustion to Sifeng.",
                "D. Apply strong continuous electroacupuncture to the child's fingers."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Pricking Sifeng (EX-UE10) to express a small droplet of clear or yellowish viscous fluid is the classic, world-renowned pediatric treatment for Gan Ji (infantile malnutrition and food stagnation), regulating Spleen Qi and appetite.",
                "B": "❌ **Incorrect:** Puncturing 2.0 cun into a toddler's fingers causes severe tissue injury.",
                "C": "❌ **Incorrect:** Scarring moxa on a 4yo causes burns and scars.",
                "D": "❌ **Incorrect:** Strong electroacupuncture on pediatric digits is traumatic."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for infantile malnutrition (Xiao Er Gan Ji) due to Food Stagnation impairing Spleen transportation?",
            "options": [
                "A. Principle: Dissolve food accumulation, eliminate stagnation, harmonize Spleen and Stomach, and clear latent heat. Formula: Fei Er Wan (Fat Baby Pill) or Bao He Wan (Preserve Harmony Pill).",
                "B. Principle: Clear Heat from Xue level. Formula: Xi Jiao Di Huang Tang.",
                "C. Principle: Purge Cold accumulation. Formula: San Wu Bei Ji Wan.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Fei Er Wan and Bao He Wan are the historical gold-standard pediatric formulas to dissolve fermented food accumulation, eliminate intestinal parasites, and restore Spleen digestion in toddlers.",
                "B": "❌ **Incorrect:** Xi Jiao Di Huang Tang treats toxic purpura.",
                "C": "❌ **Incorrect:** San Wu Bei Ji Wan is a toxic purgative.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms adult kidney yang."
            }
        }
    ],

    "CASE-034": [
        {
            "question_id": "Q4",
            "title": "4. Great Luo of Spleen for Generalized Myalgia (大包大络配穴)",
            "prompt": "For this 38-year-old yoga instructor suffering from widespread fibromyalgia tender points and body-wide myalgia ('When the Great Luo of Spleen is deficient, all the 365 joints are loose and painful'), which point is primary?",
            "options": [
                "A. SP21 (Dabao, Great Luo-Connecting point of Spleen), located on the mid-axillary line in the 6th intercostal space, combined with BL17 (Geshu).",
                "B. LI1 (Shangyang) bleeding.",
                "C. ST45 (Lidui) with moxibustion.",
                "D. KD1 (Yongquan) with deep puncture."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Ling Shu (Spiritual Pivot) Chapter 10 dictates: 'The Great Luo of Spleen is Dabao... when deficient, all joints of the body ache.' SP21 governs all collateral channels and fascia, making it premier for generalized fibromyalgia pain.",
                "B": "❌ **Incorrect:** LI1 bleeding treats acute throat fever.",
                "C": "❌ **Incorrect:** ST45 treats stomach fire toothache.",
                "D": "❌ **Incorrect:** KD1 treats acute shock."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for fibromyalgia due to Spleen and Kidney Yang Deficiency with Fixed Cold-Damp Bi?",
            "options": [
                "A. Principle: Warm Spleen and Kidney Yang, dispel Cold-Damp, unblock channels, and relieve generalized myalgia. Formula: Du Huo Ji Sheng Tang or Huang Qi Gui Zhi Wu Wu Tang.",
                "B. Principle: Clear Damp-Heat in Gallbladder. Formula: Long Dan Xie Gan Tang.",
                "C. Principle: Purge Yangming bowel excess. Formula: Da Cheng Qi Tang.",
                "D. Principle: Clear Heat from Ying level. Formula: Qing Ying Tang."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Du Huo Ji Sheng Tang tonifies the root (Liver and Kidney) while expelling cold-damp bi from the muscular fascia. Huang Qi Gui Zhi Wu Wu Tang harmonizes Ying and Wei to relieve muscle numbness and fatigue.",
                "B": "❌ **Incorrect:** Long Dan Xie Gan Tang drains damp-heat.",
                "C": "❌ **Incorrect:** Da Cheng Qi Tang treats constipation.",
                "D": "❌ **Incorrect:** Qing Ying Tang treats fever."
            }
        }
    ],

    "CASE-035": [
        {
            "question_id": "Q4",
            "title": "4. Cervical Nerve Root Decompression Strategy (华佗夹脊颈椎配穴)",
            "prompt": "For this 46-year-old contractor with C6 cervical radiculopathy causing numbness and electric shooting pain radiating into the thumb and index finger, which point combination directly targets the C6 nerve root and Hand-Yangming channel?",
            "options": [
                "A. Hua Tuo Jiaji at C5-C6 segments (0.5 cun lateral to spinous processes) combined with LI15 (Jianyu), LI11 (Quchi), and LI4 (Hegu).",
                "B. BL40 (Weizhong) and BL60 (Kunlun).",
                "C. HT7 (Shenmen) and HT3 (Shaohai).",
                "D. SP6 (Sanyinjiao) and SP9 (Yinlingquan)."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Hua Tuo Jiaji points at C5-C6 directly decompress the C6 spinal nerve root origin. The radiating numbness into the thumb and index finger follows the Hand-Yangming Large Intestine channel (LI15, LI11, LI4), providing combined root and branch treatment.",
                "B": "❌ **Incorrect:** BL40 and BL60 treat lower back and sciatica.",
                "C": "❌ **Incorrect:** Heart points follow the C8/T1 dermatome into the little finger.",
                "D": "❌ **Incorrect:** Spleen points are located on the leg."
            }
        },
        {
            "question_id": "Q5",
            "title": "5. Treatment Principle & Classical Herbal Formula (治法与方药)",
            "prompt": "What is the primary treatment principle and classical formula for cervical radiculopathy due to Channel Obstruction with Blood Stasis and Cold-Damp invasion?",
            "options": [
                "A. Principle: Unblock cervical collaterals, dispel Wind-Cold-Damp, invigorate Blood, and relieve nerve root compression pain. Formula: Ge Gen Tang (Kudzu Decoction) combined with Shen Tong Zhu Yu Tang.",
                "B. Principle: Clear toxic heat. Formula: Huang Lian Jie Du Tang.",
                "C. Principle: Purge Lower Burner. Formula: Tiao Wei Cheng Qi Tang.",
                "D. Principle: Warm Kidney Yang. Formula: Jin Gui Shen Qi Wan."
            ],
            "correct_index": 0,
            "explanations": {
                "A": "✅ **Correct:** Ge Gen Tang specifically guides medicinals to the cervical spine and relaxes the scalene/trapezius muscles. Shen Tong Zhu Yu Tang dissolves localized blood stasis decompressing the pinched nerve root.",
                "B": "❌ **Incorrect:** Huang Lian Jie Du Tang treats toxic fire.",
                "C": "❌ **Incorrect:** Tiao Wei Cheng Qi Tang treats constipation.",
                "D": "❌ **Incorrect:** Jin Gui Shen Qi Wan warms kidney yang."
            }
        }
    ]
}

# Now inject Q4 and Q5 into each case in CLINICAL_CASES
updated_count = 0
for case in CLINICAL_CASES:
    cid = case["id"]
    if cid in EXTENSIONS:
        current_mcqs = case.get("multiple_choice_questions", [])
        # Check if Q4 already exists
        existing_qids = {q["question_id"] for q in current_mcqs}
        new_qs_to_add = [q for q in EXTENSIONS[cid] if q["question_id"] not in existing_qids]
        if new_qs_to_add:
            case["multiple_choice_questions"].extend(new_qs_to_add)
            updated_count += 1
            print(f"Added {len(new_qs_to_add)} questions to {cid} (total now: {len(case['multiple_choice_questions'])})")

print(f"\nUpdated {updated_count} cases. Writing back to modules/cases_bank.py...")

# Format and save
cases_bank_path = BASE_DIR / "modules" / "cases_bank.py"
header_cases = '''"""Pan-Canadian Examination Clinical Case Bank for Acupuncturists.

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

CLINICAL_CASES: List[Dict[str, Any]] = '''

formatted_cases = pprint.pformat(CLINICAL_CASES, indent=4, width=120, sort_dicts=False)

with open(cases_bank_path, "w", encoding="utf-8") as f:
    f.write(header_cases + formatted_cases + "\n")

print("Successfully updated modules/cases_bank.py with expanded questions!")

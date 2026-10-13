# -*- coding: utf-8 -*-
"""Full 35-Case Clinical Expansion Script: Injects Q4 and Q5 to every case."""

import sys
import pprint
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from modules.cases_bank import CLINICAL_CASES

print(f"Loaded {len(CLINICAL_CASES)} cases from modules/cases_bank.py.")

# Full dictionary of Q4 and Q5 for all 35 cases
ALL_EXTENSIONS = {
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
    ]
}

print(f"Defined specific extensions for initial batch of cases.")

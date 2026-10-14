# -*- coding: utf-8 -*-
"""
Helper script to add Orthopedic Special Tests & Traumatology Guide into modules/study_guides.py
Adds 35 board-tested physical examinations across 8 body regions:
1. Cervical Spine & Neck (Spurling, Distraction, Lhermitte, Jackson, Bakody)
2. Shoulder & Rotator Cuff (Neer, Hawkins-Kennedy, Empty Can/Jobe, Drop Arm, Speed, Yergason, Apley Scratch)
3. Elbow & Forearm (Cozen, Mill, Golfer's Elbow / Reverse Cozen)
4. Wrist & Hand (Phalen, Reverse Phalen, Tinel at wrist & elbow, Finkelstein)
5. Lumbar Spine & Sacroiliac (SLR / Lasegue, Bragard, Crossed SLR, Slump, Kemp)
6. Hip & Pelvis (Patrick FABER, Thomas, Trendelenburg, Piriformis FAIR)
7. Knee Joint & Meniscus/Ligaments (Lachman, Anterior/Posterior Drawer, McMurray, Apley, Valgus/Varus, Clark)
8. Ankle & Foot (Thompson, Talar Tilt, Anterior Drawer Ankle)
"""

import sys
import re

STUDY_GUIDES_PATH = "modules/study_guides.py"

with open(STUDY_GUIDES_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Prepare ORTHOPEDIC_TESTS_DATA code
ortho_data_code = '''
# =============================================================================
# 8. ORTHOPEDIC SPECIAL TESTS & TRAUMATOLOGY MATRIX (35 BOARD TESTS)
# =============================================================================
ORTHOPEDIC_TESTS_DATA = [
    {
        "name": "Spurling's Test (Neck Compression Test / 压颈试验)",
        "region": "Cervical Spine & Neck",
        "procedure": "Patient seated. Examiner extends, laterally flexes patient's cervical spine towards the symptomatic side, and applies firm downward axial compression on the vertex of the head.",
        "positive_sign": "Reproduction of sharp radicular pain or electric paresthesia radiating down the ipsilateral arm into the specific cervical dermatome (C5–T1).",
        "pathology": "Cervical radiculopathy / nerve root compression caused by posterolateral cervical disc herniation or neuroforaminal osteophyte encroachment.",
        "tcm_bridging": "Affects Taiyang (Bladder/SI) or Shaoyang (GB/SJ) channels. Points: Huatuojiaji (C4–C7), GB20, SI3 (opens Du Mai), BL10, Ashi. Electroacupuncture: 2 Hz continuous mode across affected segment."
    },
    {
        "name": "Cervical Distraction Test (颈椎牵引试验)",
        "region": "Cervical Spine & Neck",
        "procedure": "Patient seated or supine. Examiner places one hand under patient's chin and other hand around occiput, then gently applies vertical upward axial traction.",
        "positive_sign": "Relief or significant reduction of radicular neck and arm pain/numbness as neural foramina are widened.",
        "pathology": "Cervical nerve root compression; confirms positive Spurling's test.",
        "tcm_bridging": "Channels: Du Mai & Taiyang. Points: DU14, BL11 (Hui of Bones), GB21, SI14, Bailao. Tuina gentle axial distraction."
    },
    {
        "name": "Lhermitte's Sign (Barber Chair Sign / 勒米特征)",
        "region": "Cervical Spine & Neck",
        "procedure": "Patient seated or long-sitting. Examiner actively or passively flexes patient's head and neck forward touching chin to chest.",
        "positive_sign": "Sudden, brief electric shock-like sensation shooting down the spine into the torso and lower extremities.",
        "pathology": "Cervical spinal cord compression, severe cervical myelopathy, multiple sclerosis (MS) plaque, or subacute combined degeneration.",
        "tcm_bridging": "⚠️ MEDICAL RED FLAG: Immediate neurological referral / MRI. Avoid aggressive cervical thrusting or manipulation."
    },
    {
        "name": "Shoulder Abduction Test / Bakody's Sign (肩外展试验)",
        "region": "Cervical Spine & Neck",
        "procedure": "Patient actively abducts symptomatic arm and rests hand/forearm on top of their head.",
        "positive_sign": "Relief or marked reduction of radicular neck and radiating arm pain.",
        "pathology": "Extradural cervical nerve root compression (most commonly C5–C6 disc herniation), as abduction slackens lower cervical roots.",
        "tcm_bridging": "Points: Huatuojiaji C5-C6, LI15, LI11, SI3, TE5."
    },
    {
        "name": "Jackson's Compression Test (杰克逊压头试验)",
        "region": "Cervical Spine & Neck",
        "procedure": "Patient seated with head in neutral position, then laterally flexed to each side. Examiner applies downward axial compression on the head.",
        "positive_sign": "Localized or radiating neck pain on the side of lateral flexion.",
        "pathology": "Cervical foraminal stenosis, nerve root impingement, or facet joint capsulitis.",
        "tcm_bridging": "Points: GB20, DU14, SI14, BL11, Ashi."
    },
    {
        "name": "Neer's Impingement Sign (尼尔撞击试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Examiner stabilizes patient's scapula with one hand, then forcibly and passively elevates the pronated arm through forward flexion to full overhead elevation.",
        "positive_sign": "Sharp localized subacromial or anterior-lateral shoulder pain between 70° and 120°.",
        "pathology": "Subacromial impingement syndrome: Greater tuberosity of humerus jams the supraspinatus tendon and subacromial bursa against the anteroinferior acromion.",
        "tcm_bridging": "Channels: Hand Yangming (LI) & Hand Shaoyang (TE). Points: LI15, TE14, Jianneiling, Ashi. Moxa on LI15 relieves subacromial bursa damp-cold."
    },
    {
        "name": "Hawkins-Kennedy Impingement Test (霍金斯撞击试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Examiner flexes patient's shoulder to 90° forward and flexes elbow to 90°, then forcefully internally rotates the humerus.",
        "positive_sign": "Subacromial pain reproduced as supraspinatus tendon is driven against coracoacromial ligament.",
        "pathology": "Subacromial impingement / supraspinatus tendinitis.",
        "tcm_bridging": "Points: LI15, TE14, GB34 (Hui of Sinews), LI11, Jianneiling. Dense-disperse electroacupuncture (2/100 Hz)."
    },
    {
        "name": "Empty Can Test / Jobe's Test (空罐试验 / 冈上肌试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Shoulder abducted 90° and horizontally adducted 30° in the scapular plane with thumb pointed downward towards floor ('emptying a can'). Patient resists downward pressure applied by examiner.",
        "positive_sign": "Weakness or pronounced pain in anterolateral shoulder.",
        "pathology": "Supraspinatus tendon tendinopathy or partial/full-thickness tear.",
        "tcm_bridging": "Points: SI12 (Bingfeng - supraspinatus trigger point), LI15, TE14, Ashi. Needle SI12 obliquely towards spine."
    },
    {
        "name": "Drop Arm Test (落臂试验 / 冈上肌完全撕裂试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Examiner passively abducts patient's arm to 90° and instructs patient to slowly and smoothly lower the arm back down to their side.",
        "positive_sign": "Patient cannot lower arm slowly; arm suddenly drops uncontrollably to the side from 90° with severe pain.",
        "pathology": "Full-thickness, massive rotator cuff rupture (primarily supraspinatus and infraspinatus).",
        "tcm_bridging": "⚠️ Orthopedic surgical referral indicated if traumatic complete rupture. Acupuncture for post-operative rehabilitation: LI15, SI11, GB34."
    },
    {
        "name": "Speed's Test (斯皮德二头肌试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Arm extended forward at 90° shoulder flexion, elbow extended, forearm fully supinated. Patient attempts to flex shoulder against examiner's downward resistance.",
        "positive_sign": "Sharp localized pain in the bicipital groove on the anterior aspect of the humerus.",
        "pathology": "Long head of biceps brachii tendinitis or superior labral (SLAP) tear.",
        "tcm_bridging": "Channels: Hand Taiyin (Lung) & Hand Yangming. Points: LU3 (Tianfu), LU4 (Xiabai), Jianneiling, Ashi at bicipital groove."
    },
    {
        "name": "Yergason's Test (叶加森试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "Patient flexes elbow to 90° with forearm pronated. Patient attempts to actively supinate forearm and externally rotate shoulder against examiner's firm resistance.",
        "positive_sign": "Pain localized in the bicipital groove, or a palpable tendon 'pop' or snap.",
        "pathology": "Bicipital tenosynovitis or transverse humeral ligament rupture causing biceps tendon instability.",
        "tcm_bridging": "Points: Jianneiling, LU3, LI14, GB34 (Hui of Sinews)."
    },
    {
        "name": "Apley's Scratch Test (阿普利摸背试验)",
        "region": "Shoulder & Rotator Cuff",
        "procedure": "1. Reach hand over shoulder to touch opposite superior scapula (abduction + external rotation). 2. Reach behind lumbar back to touch inferior scapula (adduction + internal rotation).",
        "positive_sign": "Marked bilateral asymmetry and restriction of movement.",
        "pathology": "Adhesive capsulitis (Frozen Shoulder / 漏肩风 / 五十肩) or severe rotator cuff contracture.",
        "tcm_bridging": "Points: LI15, TE14, SI9, SI10, ST38 (Tiaokou needle through to BL57 while patient actively moves shoulder joint)."
    },
    {
        "name": "Cozen's Test (考森试验 / 网球肘试验)",
        "region": "Elbow & Forearm",
        "procedure": "Examiner stabilizes patient's elbow, patient makes a fist, pronates forearm, and forcefully extends and radially deviates the wrist against examiner's resistance.",
        "positive_sign": "Severe sharp pain provoked at the lateral epicondyle of the humerus and common extensor tendon origin.",
        "pathology": "Lateral epicondylitis (Tennis Elbow / 肱骨外上髁炎) of extensor carpi radialis brevis.",
        "tcm_bridging": "Channels: Hand Yangming (LI). Points: LI11 (Quchi), LI10 (Shousanli), LI12 (Zhouliao), Ashi at epicondyle. Needle perpendicular with moxibustion."
    },
    {
        "name": "Mill's Test (密尔试验)",
        "region": "Elbow & Forearm",
        "procedure": "Examiner passively flexes the patient's fingers and wrist, fully pronates the forearm, and then slowly extends the elbow completely.",
        "positive_sign": "Sudden sharp tugging pain at the lateral humeral epicondyle.",
        "pathology": "Confirms lateral epicondylitis (Tennis Elbow).",
        "tcm_bridging": "Points: LI11, LI10, Ashi, LU5."
    },
    {
        "name": "Golfer's Elbow Test / Reverse Cozen's (高尔夫球肘试验)",
        "region": "Elbow & Forearm",
        "procedure": "Patient supinates forearm and attempts to forcefully flex the wrist against examiner's downward resistance.",
        "positive_sign": "Severe pain localized over the medial epicondyle of the humerus.",
        "pathology": "Medial epicondylitis (Golfer's Elbow / 肱骨内上髁炎) of common flexor tendon origin.",
        "tcm_bridging": "Channels: Hand Shaoyin (Heart) & Hand Taiyin. Points: HT3 (Shaohai), PC3 (Quze), SI8 (Xiaohai), Ashi."
    },
    {
        "name": "Phalen's Test / Wrist Flexion Test (法伦试验 / 屈腕试验)",
        "region": "Wrist & Hand",
        "procedure": "Patient presses dorsal surfaces of both hands together with wrists flexed at 90° for 60 continuous seconds, holding elbows horizontal.",
        "positive_sign": "Paresthesia, numbness, or tingling in the thumb, index, middle finger, and radial half of ring finger (median nerve distribution).",
        "pathology": "Carpal Tunnel Syndrome (CTS / 腕管综合征) due to median nerve compression under transverse carpal ligament.",
        "tcm_bridging": "Channels: Hand Jueyin (PC) & Taiyin (LU). Points: PC7 (Daling), PC6 (Neiguan), LU9, Baxie. Avoid deep direct needling into median nerve."
    },
    {
        "name": "Reverse Phalen's Test / Prayer Test (反法伦试验 / 祈祷试验)",
        "region": "Wrist & Hand",
        "procedure": "Patient presses palmar surfaces of both hands together in maximal wrist extension (prayer posture) for 60 seconds.",
        "positive_sign": "Reproduction of median nerve paresthesias.",
        "pathology": "Carpal Tunnel Syndrome.",
        "tcm_bridging": "Points: PC7, PC6, LI4, Baxie."
    },
    {
        "name": "Tinel's Sign at Wrist & Elbow (提内尔征 / 神经叩击试验)",
        "region": "Wrist & Hand",
        "procedure": "Examiner lightly taps with fingertip or reflex hammer over the volar carpal tunnel (wrist) or cubital tunnel (elbow groove between olecranon & medial epicondyle).",
        "positive_sign": "Tingling, pins-and-needles sensation shooting distally into the respective nerve sensory distribution.",
        "pathology": "Nerve entrapment / neuropathy (Median nerve at wrist = Carpal Tunnel; Ulnar nerve at elbow = Cubital Tunnel Syndrome).",
        "tcm_bridging": "Median: PC6, PC7. Ulnar: SI8, HT7, SI3. Electroacupuncture: 2 Hz continuous."
    },
    {
        "name": "Finkelstein's Test (芬克斯坦试验 / 握拳尺偏试验)",
        "region": "Wrist & Hand",
        "procedure": "Patient tucks thumb into palm and tightly curls four fingers over thumb into a fist. Examiner then passively and firmly ulnar-deviates the wrist.",
        "positive_sign": "Excruciating sharp pain over the radial styloid process.",
        "pathology": "De Quervain's Tenosynovitis (桡骨茎突狭窄性腱鞘炎) of abductor pollicis longus (APL) and extensor pollicis brevis (EPB) tendons.",
        "tcm_bridging": "Channels: Hand Taiyin (Lung) & Yangming (LI). Points: LU7 (Lieque), LI5 (Yangxi), LI4 (Hegu), Ashi. Thread needle along tendon sheath."
    },
    {
        "name": "Straight Leg Raise Test / Lasegue's Sign (直腿抬高试验 / 拉塞格征)",
        "region": "Lumbar Spine & Sacroiliac",
        "procedure": "Patient supine with legs flat. Examiner slowly lifts the symptomatic relaxed leg with knee fully locked in extension until pain is provoked.",
        "positive_sign": "Shooting radicular sciatic pain radiating below the knee between 30° and 70° of elevation.",
        "pathology": "Lumbar intervertebral disc herniation (L4–L5 or L5–S1) causing L5 or S1 nerve root traction.",
        "tcm_bridging": "Channels: Foot Taiyang (Bladder) & Shaoyang (GB). Points: BL23, BL25, BL40 (Weizhong), BL60, GB30 (Huantiao), Huatuojiaji L4-S1. Electroacupuncture dense-disperse."
    },
    {
        "name": "Bragard's Sign (布拉加德征 / 直腿抬高加强试验)",
        "region": "Lumbar Spine & Sacroiliac",
        "procedure": "Lower the raised leg 5° just below the painful angle of positive SLR, then forcefully passively dorsiflex the patient's foot.",
        "positive_sign": "Immediate reproduction of shooting radicular sciatic pain down the leg.",
        "pathology": "Differentiates true neural compression (disc herniation) from muscular hamstring tightness (tight hamstrings do not hurt with ankle dorsiflexion).",
        "tcm_bridging": "Points: BL40, BL57 (Chengshan), BL60 (Kunlun)."
    },
    {
        "name": "Crossed Straight Leg Raise / Well-Leg Raise (健侧直腿抬高试验)",
        "region": "Lumbar Spine & Sacroiliac",
        "procedure": "Examiner lifts the ASYMPTOMATIC (healthy) straight leg.",
        "positive_sign": "Severe shooting radicular pain is triggered in the CONTRALATERAL (symptomatic) leg.",
        "pathology": "Highly specific (>90%) for large central or paracentral lumbar disc herniation or axillary disc prolapse.",
        "tcm_bridging": "⚠️ High-grade disc prolapse. Avoid aggressive spinal manipulation. Points: BL25, Huatuojiaji, GB30, BL40."
    },
    {
        "name": "Slump Test (崩塌试验 / 脊髓神经张力试验)",
        "region": "Lumbar Spine & Sacroiliac",
        "procedure": "Patient seated, slumped thoracolumbar spine, neck flexed to chest, knee extended, and ankle dorsiflexed. Examiner gently adds cervical overpressure.",
        "positive_sign": "Reproduction of radicular neurological leg pain, relieved upon cervical neck extension.",
        "pathology": "Dural irritation, spinal stenosis, or nerve root adherence.",
        "tcm_bridging": "Points: DU26, BL40, BL60, Yaotongxue."
    },
    {
        "name": "Kemp's Test / Quadrant Test (坎普试验 / 腰椎旋转后伸试验)",
        "region": "Lumbar Spine & Sacroiliac",
        "procedure": "Patient seated or standing. Examiner guides patient's torso into combined extension, lateral bending, and rotation towards the affected side while applying axial downward force.",
        "positive_sign": "Localized low back pain (facet joint syndrome) or radicular leg pain (foraminal nerve root encroachment).",
        "pathology": "Lumbar facet arthropathy or foraminal spinal stenosis.",
        "tcm_bridging": "Channels: Foot Taiyang & Du Mai. Points: BL23, BL25, BL26, Yaoyan, Huatuojiaji. Moxibustion over facet joints."
    },
    {
        "name": "Patrick's Test / FABER Test (帕特里克试验 / 4字试验)",
        "region": "Hip & Pelvis",
        "procedure": "Patient supine. Examiner places foot of tested leg onto contralateral knee (Flexion, ABduction, External Rotation creating figure '4'). Examiner presses down gently on tested knee and opposite ASIS.",
        "positive_sign": "Groin pain indicates hip joint pathology (osteoarthritis); posterior buttock/sacral pain indicates sacroiliac joint dysfunction/sacroiliitis.",
        "pathology": "Hip osteoarthritis, avascular necrosis of femoral head, or sacroiliitis (ankylosing spondylitis).",
        "tcm_bridging": "Hip: GB29, GB30, SP10. Sacroiliac: BL27, BL28, BL31-34 (Baliao), Ashi."
    },
    {
        "name": "Thomas Test (托马斯试验 / 屈髋挛缩试验)",
        "region": "Hip & Pelvis",
        "procedure": "Patient supine. Patient pulls one knee tightly to chest to flatten lumbar lordosis. Examiner observes contralateral leg resting on table.",
        "positive_sign": "The contralateral extended leg involuntarily lifts off the table, indicating hip flexion contracture.",
        "pathology": "Iliopsoas contracture / psoas spasm, hip osteoarthritis.",
        "tcm_bridging": "Points: ST30 (Qichong), SP12 (Chongmen), GB30, BL23."
    },
    {
        "name": "Trendelenburg Test (特伦德伦堡征 / 臀中肌试验)",
        "region": "Hip & Pelvis",
        "procedure": "Patient stands unsupported on one leg for 30 seconds while examiner observes the pelvic horizontal level from behind.",
        "positive_sign": "The pelvis on the UNSUPPORTED (lifted) side drops downward instead of staying level or tilting upward.",
        "pathology": "Gluteus medius weakness or paralysis on the STANCE leg, superior gluteal nerve lesion, or L5 nerve root pathology.",
        "tcm_bridging": "Channels: Foot Shaoyang (GB). Points: GB29 (Juliao), GB30 (Huantiao), GB34 (Yanglingquan). Motor point stimulation."
    },
    {
        "name": "Piriformis Test / FAIR Test (梨状肌紧张试验 / FAIR试验)",
        "region": "Hip & Pelvis",
        "procedure": "Patient sidelying with tested hip flexed to 60° and knee flexed to 90°. Examiner stabilizes pelvis and pushes knee down into adduction and internal rotation (FAIR: Flexion, Adduction, Internal Rotation).",
        "positive_sign": "Severe pain in deep buttock radiating down posterior thigh.",
        "pathology": "Piriformis Syndrome (梨状肌综合征) compressing the sciatic nerve.",
        "tcm_bridging": "Points: GB30 (Huantiao - deep perpendicular insertion 2.0-3.0 cun to elicit sciatic de qi), BL54 (Zhibian), Ashi."
    },
    {
        "name": "Lachman's Test (拉赫曼试验 / 前交叉韧带试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient supine, knee flexed to 20°–30°. Examiner stabilizes distal femur with one hand and pulls proximal tibia anteriorly with the other hand.",
        "positive_sign": "Increased anterior tibial translation with a soft, mushy, indistinct end-feel. Gold standard test for ACL tear.",
        "pathology": "Anterior Cruciate Ligament (ACL / 前交叉韧带) rupture.",
        "tcm_bridging": "Acute tear: Surgical evaluation. Chronic/Post-op: ST35, Neixiyan, Heding, GB34, SP9, BL40."
    },
    {
        "name": "Anterior & Posterior Drawer Test of Knee (膝关节前后抽屉试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient supine, knee flexed to 90°, foot stabilized on table. Examiner grasps proximal tibia with both hands and firmly pulls anteriorly (ACL) then pushes posteriorly (PCL).",
        "positive_sign": "Excessive forward displacement (>6mm) indicates ACL rupture; excessive backward sag indicates PCL rupture.",
        "pathology": "Cruciate ligament tears.",
        "tcm_bridging": "Points: Heding, Xiyan, GB34, SP10, BL40."
    },
    {
        "name": "McMurray's Test (麦克马瑞试验 / 半月板旋转试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient supine, knee fully flexed. Examiner holds heel and palpates joint line. For Medial Meniscus: Externally rotate tibia and apply valgus stress while extending knee. For Lateral Meniscus: Internally rotate tibia and apply varus stress while extending knee.",
        "positive_sign": "A distinct, painful click, 'thunk', or pop palpable along the joint line with sharp pain.",
        "pathology": "Meniscal tear (半月板撕裂).",
        "tcm_bridging": "Points: ST35 (Dubi), Neixiyan, SP9 (medial meniscus), GB34 (lateral meniscus), Ashi."
    },
    {
        "name": "Apley's Compression & Distraction Test (阿普利研磨与牵拉试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient prone with knee flexed to 90°. Examiner presses down axially on heel while rotating tibia (Compression). Examiner then stabilizes thigh and pulls tibia upward while rotating (Distraction).",
        "positive_sign": "Pain with Compression = Meniscus injury; Pain with Distraction = Collateral ligament sprain.",
        "pathology": "Differentiates meniscal damage from collateral ligament strain.",
        "tcm_bridging": "Points: BL40, Heding, Xiyan, SP9, GB34."
    },
    {
        "name": "Valgus & Varus Stress Tests of Knee (膝关节侧向应力试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient supine. Examiner tests knee at 0° and 30° of flexion. Valgus: Examiner pushes knee medially while pulling ankle laterally (MCL). Varus: Examiner pushes knee laterally while pulling ankle medially (LCL).",
        "positive_sign": "Medial joint gap/pain = Medial Collateral Ligament tear; Lateral joint gap/pain = Lateral Collateral Ligament tear.",
        "pathology": "Knee collateral ligament sprain / rupture.",
        "tcm_bridging": "MCL: SP9, SP10, LV8. LCL: GB34, GB33, ST35. Local moxibustion."
    },
    {
        "name": "Clark's Sign / Patellar Grind Test (克拉克征 / 髌骨研磨试验)",
        "region": "Knee Joint & Ligaments",
        "procedure": "Patient supine with knee extended. Examiner presses down firmly on superior pole of patella with web of hand, then instructs patient to contract quadriceps muscle.",
        "positive_sign": "Severe retropatellar pain and coarse crepitus, patient cannot maintain quadriceps contraction.",
        "pathology": "Chondromalacia Patellae / Patellofemoral Pain Syndrome (PFPS / 髌骨软化症).",
        "tcm_bridging": "Points: Heding, Liangqiu (ST34), Xuehai (SP10), ST35, Neixiyan."
    },
    {
        "name": "Thompson's Test / Simmonds' Test (汤普森试验 / 跟腱挤压试验)",
        "region": "Ankle & Foot",
        "procedure": "Patient prone with feet hanging off end of examination table. Examiner firmly squeezes the calf belly (gastrocnemius / soleus).",
        "positive_sign": "ABSENCE of involuntary plantarflexion of the foot (the foot does NOT twitch or move downward).",
        "pathology": "COMPLETE RUPTURE of the Achilles Tendon (跟腱完全断裂). Absolute surgical emergency.",
        "tcm_bridging": "⚠️ URGENT SURGICAL REFERRAL. Never attempt to treat acute full Achilles tendon rupture with acupuncture."
    },
    {
        "name": "Talar Tilt & Anterior Drawer Test of Ankle (踝关节倾斜与抽屉试验)",
        "region": "Ankle & Foot",
        "procedure": "Examiner stabilizes distal tibia and inverts the talus (Talar Tilt) or pulls the calcaneus forward (Drawer).",
        "positive_sign": "Excessive lateral ankle gapping or anterior subluxation with sulcus sign.",
        "pathology": "Anterior Talofibular Ligament (ATFL) and Calcaneofibular Ligament (CFL) sprain/tear (Inversion ankle sprain).",
        "tcm_bridging": "Channels: Foot Taiyang & Shaoyang. Points: GB40 (Qiuxu), BL60 (Kunlun), BL62 (Shenmai), Ashi. Bleed local venules."
    }
]
'''

# 2. Add Orthopedic option to selectbox
old_options = '"🎯 Root vs Manifestation (Ben & Biao) Treatment Principles Matrix (标本缓急与治则配属全解矩阵)"'
new_options = '"🎯 Root vs Manifestation (Ben & Biao) Treatment Principles Matrix (标本缓急与治则配属全解矩阵)",\n            "🦴 Orthopedic Special Tests & Traumatology Guide (骨伤科体格检查与特殊试验全纲)"'

# 3. Prepare Orthopedic rendering code
ortho_render_code = '''
    # =========================================================================
    # GUIDE 16: ORTHOPEDIC SPECIAL TESTS & TRAUMATOLOGY GUIDE
    # =========================================================================
    elif sheet_choice.startswith("🦴 Orthopedic Special Tests"):
        render_clean_html("""
        <div style="background: #111827; border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 14px 18px; margin-bottom: 18px;">
            <div style="font-weight: 800; font-size: 1.15rem; color: #38bdf8;">🦴 骨伤科物理检查与神经学特殊试验全景指南 (Orthopedic Special Tests)</div>
            <div style="font-size: 0.88rem; color: #cbd5e1; margin-top: 4px;">
                Comprehensive physical examination maneuvers, positive diagnostic indicators, and corresponding TCM acupuncture channel protocols across 8 anatomical regions.
            </div>
        </div>
        """)

        col_search, col_filter = st.columns([2, 1])
        with col_search:
            ortho_query = st.text_input("🔍 Search Tests (by Name, Joint, Maneuver, or Pathology):", value="", key="ortho_search").strip().lower()
        with col_filter:
            ortho_region = st.selectbox(
                "Filter by Anatomical Region:",
                options=[
                    "All Regions",
                    "Cervical Spine & Neck",
                    "Shoulder & Rotator Cuff",
                    "Elbow & Forearm",
                    "Wrist & Hand",
                    "Lumbar Spine & Sacroiliac",
                    "Hip & Pelvis",
                    "Knee Joint & Ligaments",
                    "Ankle & Foot"
                ],
                key="ortho_region_select"
            )

        filtered_tests = []
        for t in ORTHOPEDIC_TESTS_DATA:
            if ortho_region != "All Regions" and t["region"] != ortho_region:
                continue
            if ortho_query:
                combined_text = f"{t['name']} {t['region']} {t['procedure']} {t['positive_sign']} {t['pathology']} {t['tcm_bridging']}".lower()
                if ortho_query not in combined_text:
                    continue
            filtered_tests.append(t)

        st.caption(f"Showing **{len(filtered_tests)}** of 35 Orthopedic Special Tests")

        for t in filtered_tests:
            render_clean_html(f"""
            <div style="background: #111827; border: 1.5px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 18px 22px; margin-bottom: 14px; box-shadow: 0 4px 14px rgba(0,0,0,0.25);">
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                    <span style="color: #ffffff; font-size: 1.15rem; font-weight: 800;">{t['name']}</span>
                    <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 0.74rem; font-weight: 800; padding: 2px 10px; border-radius: 4px;">
                        {t['region']}
                    </span>
                </div>
                
                <div style="font-size: 0.86rem; color: #cbd5e1; line-height: 1.5; margin-bottom: 8px;">
                    <strong>🩺 Testing Procedure:</strong> {t['procedure']}
                </div>

                <div style="background: rgba(239, 68, 68, 0.12); border-left: 3px solid #ef4444; padding: 8px 12px; border-radius: 4px; font-size: 0.84rem; color: #fca5a5; line-height: 1.45; margin-bottom: 8px;">
                    <strong>⚠️ Positive Sign:</strong> {t['positive_sign']}
                </div>

                <div style="font-size: 0.84rem; color: #fde68a; line-height: 1.45; margin-bottom: 8px;">
                    <strong>🎯 Primary Pathology / Rule Out:</strong> {t['pathology']}
                </div>

                <div style="background: rgba(16, 185, 129, 0.12); border-left: 3px solid #10b981; padding: 8px 12px; border-radius: 4px; font-size: 0.84rem; color: #a7f3d0; line-height: 1.45;">
                    <strong>⚡ TCM Channel & Acupuncture Protocol:</strong><br/>
                    {t['tcm_bridging']}
                </div>
            </div>
            """)
'''

# Check if already present
if "ORTHOPEDIC_TESTS_DATA" not in code:
    # Insert ortho data before render_study_guides_tab
    render_func_marker = "def render_study_guides_tab():"
    code = code.replace(render_func_marker, ortho_data_code + "\n\n" + render_func_marker)
    
    # Replace selectbox options
    code = code.replace(old_options, new_options)
    
    # Append render code at the end
    code = code + "\n" + ortho_render_code

    with open(STUDY_GUIDES_PATH, "w", encoding="utf-8") as f:
        f.write(code)
    print("Successfully appended Orthopedic Special Tests Guide to modules/study_guides.py!")
else:
    print("ORTHOPEDIC_TESTS_DATA already present in modules/study_guides.py.")

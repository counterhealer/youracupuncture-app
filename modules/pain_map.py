# -*- coding: utf-8 -*-
"""Interactive 2D External Pain Map & Musculoskeletal Acupuncture Module.

Provides an interactive 2D anatomical pain map covering the human body (Anterior, Posterior,
and Cranial views). Clicking on any region in pain delivers comprehensive clinical treatment
protocols including:
- Channel / Meridian affected (Six Divisions & Channel Sinews / Jingjin)
- TCM Bi Syndrome Differential (Wind, Cold, Damp, Heat, Blood Stasis, Deficiency)
- Primary Local Points (Ashi & anatomical target points)
- Distal & Balance Method Points (Dr. Tan Balance Method, Master Tung, Classical Distal)
- Needling Techniques, Electro-Acupuncture frequencies (2Hz vs 100Hz)
- Moxibustion, Cupping, Gua Sha, Topical Liniments (Zheng Gu Shui, Die Da Gao)
- Red Flag referral warnings
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import date


# =============================================================================
# CLINICAL PAIN CONDITIONS DATABASE (28 REGIONS & CONDITIONS)
# =============================================================================
PAIN_DATABASE: Dict[str, Dict[str, Any]] = {
    # --- HEAD & CRANIAL PAIN ---
    "head_frontal": {
        "id": "head_frontal",
        "name": "Frontal / Forehead Headache & Sinus Pain",
        "chinese": "阳明头痛 (Yangming Headache)",
        "region_group": "Head & Face",
        "view": "Anterior / Front",
        "anatomical_zone": "Forehead, Glabella, Supraorbital margin",
        "meridian": "Hand & Foot Yangming (Large Intestine & Stomach Channels)",
        "bi_type": "Wind-Heat, Wind-Cold, or Stomach Fire Blazing",
        "western_correlates": "Tension headache, Frontal sinusitis, Eyestrain, Trigeminal neuralgia (V1)",
        "description": "Pain localized to the forehead, eyebrows, and bridge of nose, often throbbing or accompanied by heavy sinus pressure and orbital tension.",
        "local_points": [
            {"code": "Yintang", "name": "Yintang (印堂)", "depth": "0.3-0.5 cun subcutaneous downwards", "technique": "Harmonizing", "rationale": "Calms Shen, opens nasal passages, relieves frontal heaviness."},
            {"code": "ST8", "name": "Touwei (头维)", "depth": "0.5-1.0 cun subcutaneous posteriorly", "technique": "Reducing", "rationale": "Corner of forehead; drains Yangming fire and headache."},
            {"code": "BL2", "name": "Zanzhu (攒竹)", "depth": "0.3-0.5 cun subcutaneous downwards/transverse", "technique": "Reducing", "rationale": "Clears sinus congestion, relieves supraorbital pain."},
            {"code": "Yuyao", "name": "Yuyao (鱼腰)", "depth": "0.3-0.5 cun transverse", "technique": "Reducing", "rationale": "Midpoint of eyebrow; relieves frontal orbital throbbing."}
        ],
        "distal_points": [
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Command Point of Face & Head", "technique": "Reducing (泻法)", "rationale": "Primary distal point for all Yangming headaches and frontal pain."},
            {"code": "ST44", "name": "Neiting (内庭)", "role": "Ying-Spring Point (Water)", "technique": "Reducing (泻法)", "rationale": "Clears Stomach fire causing throbbing forehead heat."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point", "technique": "Harmonizing", "rationale": "Regulates Stomach channel and guides energy downward."},
            {"code": "LU7", "name": "Lieque (列缺)", "role": "Command of Head/Neck (Luo)", "technique": "Harmonizing", "rationale": "Dispels exterior wind causing sinus congestion."}
        ],
        "modalities": {
            "electro": "Not typically indicated on face; if used, 2 Hz microcurrent at Yintang-ST8 for 15 min.",
            "moxa": "Contraindicated if acute sinus heat/fever; beneficial for chronic cold-induced sinus congestion.",
            "cupping": "Gentle silicone facial flash cupping along forehead to hairline.",
            "guasha": "Light Gua Sha from center of forehead outwards toward temples.",
            "topical": "Apply White Flower Oil (Bai Hua You) or Peppermint oil to temples and hairline."
        },
        "red_flags": "Sudden explosive 'thunderclap' headache, fever with stiff neck (meningismus), visual loss, or temporal artery tenderness in elderly (temporal arteritis)."
    },
    "head_temporal": {
        "id": "head_temporal",
        "name": "Temporal Headache & Migraine",
        "chinese": "少阳头痛 (Shaoyang Headache / Migraine)",
        "region_group": "Head & Face",
        "view": "Anterior / Front",
        "anatomical_zone": "Temples, Lateral head, Parietal-temporal junction",
        "meridian": "Foot-Shaoyang (Gallbladder) & Hand-Shaoyang (San Jiao)",
        "bi_type": "Liver Fire Rising, Liver Yang Rising, or Shaoyang Wind",
        "western_correlates": "Migraine without/with aura, Cluster headache, TMJ-referred pain, Tension headache",
        "description": "Unilateral or bilateral throbbing, pulsating temporal pain often accompanied by nausea, photosensitivity, phonophobia, and irritability.",
        "local_points": [
            {"code": "Taiyang", "name": "Taiyang (太阳)", "depth": "0.3-0.5 cun perpendicular or prick to bleed", "technique": "Reducing / Bleeding", "rationale": "Primary empirical point for temporal headaches; bleed 1-2 drops for throbbing migraine."},
            {"code": "GB8", "name": "Shuaigu (率谷)", "depth": "0.5-0.8 cun subcutaneous posteriorly", "technique": "Reducing", "rationale": "Located 1.5 cun above ear apex; pacifies Gallbladder wind in temporal area."},
            {"code": "GB20", "name": "Fengchi (风池)", "depth": "0.8-1.2 cun towards opposite tip of nose", "technique": "Reducing", "rationale": "Subdues ascending Liver fire and relaxes suboccipital tension."}
        ],
        "distal_points": [
            {"code": "GB41", "name": "Zulinqi (足临泣)", "role": "Shu-Stream / Confluent of Dai Mai", "technique": "Reducing (泻法)", "rationale": "Specific distal point for temporal and lateral head pain."},
            {"code": "SJ5", "name": "Waiguan (外关)", "role": "Luo / Confluent of Yang Wei", "technique": "Reducing (泻法)", "rationale": "Coupled with GB41 to open the Shaoyang channel network."},
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source Point", "technique": "Reducing (泻法)", "rationale": "Subdues Liver Yang and pacifies rising heat."},
            {"code": "GB43", "name": "Xiaxi (侠溪)", "role": "Ying-Spring Point (Water)", "technique": "Reducing", "rationale": "Clears Gallbladder channel heat."}
        ],
        "modalities": {
            "electro": "Dense-disperse 2/100 Hz between GB20 and Taiyang at low intensity for 20 minutes.",
            "moxa": "Contraindicated (excess heat/wind ascending).",
            "cupping": "Stationary cupping at upper trapezius (GB21) to descend blood pressure and tension.",
            "guasha": "Gua Sha descending down the side of neck from GB20 to GB21.",
            "topical": "Tiger Balm or Po Sum On oil massaged into Taiyang and mastoid process."
        },
        "red_flags": "New onset migraine in patient > 50, unilateral pupil dilation, persistent focal neurological deficit, or worst headache of life."
    },
    "head_occiput": {
        "id": "head_occiput",
        "name": "Occipital Headache & Suboccipital Tension",
        "chinese": "太阳头痛 (Taiyang Headache)",
        "region_group": "Head & Face",
        "view": "Posterior / Back",
        "anatomical_zone": "Occiput, Base of skull, Suboccipital triangle",
        "meridian": "Foot-Taiyang (Urinary Bladder) & Du Meridian",
        "bi_type": "Wind-Cold invading Taiyang, Cervical Qi/Blood Stagnation",
        "western_correlates": "Cervicogenic headache, Suboccipital muscle spasm, Greater occipital neuralgia",
        "description": "Tight, constricting band or pulling ache at the back of the head radiating from the neck, exacerbated by desk work, stress, or cold wind.",
        "local_points": [
            {"code": "GB20", "name": "Fengchi (风池)", "depth": "0.8-1.2 cun towards nose tip", "technique": "Harmonizing", "rationale": "Relaxes rectus capitis and obliquus capitis suboccipital muscles."},
            {"code": "BL10", "name": "Tianzhu (天柱)", "depth": "0.5-0.8 cun perpendicular", "technique": "Reducing", "rationale": "Clears occipital congestion and relaxes the trapezius tendon anchor."},
            {"code": "DU16", "name": "Fengfu (风府)", "depth": "0.5-0.8 cun perpendicular (Do not angle upwards)", "technique": "Reducing", "rationale": "Expels exterior wind from the occiput."},
            {"code": "DU20", "name": "Baihui (百会)", "depth": "0.5-0.8 cun transverse posteriorly", "technique": "Harmonizing", "rationale": "Lifts clear Yang and regulates cranial pressure."}
        ],
        "distal_points": [
            {"code": "BL60", "name": "Kunlun (昆仑)", "role": "Jing-River Point (Fire)", "technique": "Reducing (泻法)", "rationale": "Primary distal point for Taiyang occipital and lower back pain."},
            {"code": "SI3", "name": "Houxi (后溪)", "role": "Shu-Stream / Confluent of Du Mai", "technique": "Reinforcing / Reducing", "rationale": "Opens the entire posterior spinal axis and occiput."},
            {"code": "BL62", "name": "Shenmai (申脉)", "role": "Confluent of Yang Qiao", "technique": "Harmonizing", "rationale": "Relaxes tight posterior muscular chains."},
            {"code": "LU7", "name": "Lieque (列缺)", "role": "Command Point of Head & Nape", "technique": "Harmonizing", "rationale": "Releases exterior wind and stiff nape."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between BL10 and GB20 for 20 minutes to release suboccipital spasm.",
            "moxa": "Warm moxa stick around occiput if pain is aggravated by cold weather.",
            "cupping": "Sliding cupping from suboccipital ridge down to T7 along Bladder channel.",
            "guasha": "Downward scraping along neck and upper back with warming liniment.",
            "topical": "Zheng Gu Shui or warming herbal heat plaster on posterior neck."
        },
        "red_flags": "Neck stiffness preventing chin-to-chest touching with fever, thunderclap onset, or history of recent cervical manipulation/trauma (vertebral dissection risk)."
    },
    "tmj_jaw": {
        "id": "tmj_jaw",
        "name": "Temporomandibular Joint (TMJ) & Jaw Pain",
        "chinese": "颊痛 / 牙关紧闭 (Jaw Bi / Clenching)",
        "region_group": "Head & Face",
        "view": "Anterior / Front",
        "anatomical_zone": "Masseter, Temporomandibular joint capsule, Zygomatic arch",
        "meridian": "Stomach (Foot-Yangming), Small Intestine (Hand-Taiyang), San Jiao",
        "bi_type": "Wind-Cold invasion, Liver Qi Stagnation with clenching, Stomach Heat",
        "western_correlates": "TMJ Dysfunction, Bruxism, Masseter spasm, Myofascial pain syndrome",
        "description": "Clicking, popping, or locked jaw with tenderness when chewing, opening mouth, or chronic nighttime teeth grinding.",
        "local_points": [
            {"code": "ST7", "name": "Xiaguan (下关)", "depth": "0.5-1.0 cun perpendicular (mouth closed)", "technique": "Harmonizing", "rationale": "Directly penetrates into the TMJ capsule and lateral pterygoid."},
            {"code": "ST6", "name": "Jiache (颊车)", "depth": "0.5-0.8 cun oblique towards ST7", "technique": "Harmonizing / Reducing", "rationale": "Located directly on belly of masseter muscle; releases spasm."},
            {"code": "SJ17", "name": "Yifeng (翳风)", "depth": "0.5-1.0 cun perpendicular anteriorly", "technique": "Harmonizing", "rationale": "Behind earlobe; releases deep posterior jaw tension."},
            {"code": "SI19", "name": "Tinggong (听宫)", "depth": "0.5-1.0 cun (open mouth slightly)", "technique": "Harmonizing", "rationale": "Opens anterior TMJ joint space."}
        ],
        "distal_points": [
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Command of Face/Jaw", "technique": "Reducing (泻法)", "rationale": "Primary distal point for all jaw, dental, and facial tension."},
            {"code": "ST44", "name": "Neiting (内庭)", "role": "Ying-Spring Point", "technique": "Reducing", "rationale": "Clears local inflammatory heat in the jaw."},
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source Point", "technique": "Reducing", "rationale": "Relieves stress-related nocturnal teeth grinding (bruxism)."}
        ],
        "modalities": {
            "electro": "2 Hz gentle pulse between ST7 and ST6 for 15 minutes to release chronic masseter hypertonicity.",
            "moxa": "Warm moxa stick held 2 inches away from ST6/ST7 if cold makes jaw stiff.",
            "cupping": "Very small facial silicone cup along masseter.",
            "guasha": "Gentle upward scraping along jawline toward ear.",
            "topical": "Warm moist compress over the jaw before bedtime."
        },
        "red_flags": "Jaw pain radiating down left arm with chest tightness (cardiac angina), inability to swallow saliva, or trismus following dental infection."
    },

    # --- NECK & SHOULDER PAIN ---
    "neck_cervical": {
        "id": "neck_cervical",
        "name": "Stiff Neck & Cervical Spine Spondylosis",
        "chinese": "落枕 / 颈椎病 (Luozhen / Cervical Bi)",
        "region_group": "Neck & Shoulder",
        "view": "Posterior / Back",
        "anatomical_zone": "C1-C7 cervical vertebrae, Paraspinal musculature, Splenius capitis",
        "meridian": "Du Mai, Foot-Taiyang (Urinary Bladder), Hand-Shaoyang",
        "bi_type": "Wind-Cold-Damp Bi, Qi & Blood Stagnation from awkward sleep posture",
        "western_correlates": "Acute torticollis (wry neck), Cervical radiculopathy, Facet joint arthrosis",
        "description": "Acute or chronic restricted neck rotation, stiffness waking up in the morning, pain radiating into upper trapezius or down the arm.",
        "local_points": [
            {"code": "Luozhen", "name": "Luozhen (落枕)", "depth": "0.5-0.8 cun on dorsum of hand", "technique": "Reducing while patient moves neck!", "rationale": "The single most famous empirical point in TCM for acute stiff neck."},
            {"code": "Jiaji (C4-C7)", "name": "Hua Tuo Jiaji (华佗夹脊)", "depth": "0.5-1.0 cun perpendicular", "technique": "Harmonizing", "rationale": "Directly targets cervical nerve root exits and deep paraspinals."},
            {"code": "Bailao", "name": "Jing Bailao (颈百劳)", "depth": "0.5-0.8 cun perpendicular", "technique": "Harmonizing / Moxa", "rationale": "2 cun above C7, 1 cun lateral; relieves deep cervical fatigue and stiffness."},
            {"code": "GB21", "name": "Jianjing (肩井)", "depth": "0.3-0.5 cun posterior/oblique (Caution: Apex of lung!)", "technique": "Harmonizing", "rationale": "Relieves severe muscular spasm of upper trapezius."}
        ],
        "distal_points": [
            {"code": "SI3", "name": "Houxi (后溪)", "role": "Master Point of Du Mai", "technique": "Reducing (泻法) with neck motion", "rationale": "Unblocks the entire posterior cervical and spinal axis."},
            {"code": "BL60", "name": "Kunlun (昆仑)", "role": "Taiyang Distal Anchor", "technique": "Reducing", "rationale": "Draws Qi downward away from compressed cervical joints."},
            {"code": "SJ5", "name": "Waiguan (外关)", "role": "Luo-Connecting Point", "technique": "Reducing", "rationale": "Frees lateral rotation of the neck."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between cervical Jiaji points for 20 minutes.",
            "moxa": "Warm moxa roll over Bailao and upper back for Cold-induced stiffness.",
            "cupping": "Stationary or sliding cupping along Bladder meridian and trapezius.",
            "guasha": "Gua Sha along the posterior neck down to T4 with herbal oil.",
            "topical": "Zheng Gu Shui applied before warm heating pad."
        },
        "red_flags": "Progressive numbness, weakness, or loss of dexterity in hands (cervical myelopathy), or Lhermitte's sign (electric shock down spine upon neck flexion)."
    },
    "shoulder_anterior": {
        "id": "shoulder_anterior",
        "name": "Anterior Shoulder & Bicipital Tendinitis",
        "chinese": "肩前痛 (Anterior Shoulder Bi)",
        "region_group": "Neck & Shoulder",
        "view": "Anterior / Front",
        "anatomical_zone": "Bicipital groove, Coracoid process, Anterior deltoid",
        "meridian": "Hand-Yangming (Large Intestine) & Hand-Taiyin (Lung)",
        "bi_type": "Wind-Cold-Damp Bi, Qi and Blood Stagnation from repetitive overhead reach",
        "western_correlates": "Biceps long head tendinitis, Subscapularis tendinopathy, Frozen shoulder (Early phase)",
        "description": "Sharp anterior shoulder pain aggravated by lifting arm forward, carrying grocery bags, or putting on a jacket.",
        "local_points": [
            {"code": "Jianneiling", "name": "Jianneiling (肩内陵)", "depth": "0.8-1.2 cun perpendicular", "technique": "Harmonizing", "rationale": "Primary extra point midway between anterior axillary fold and LI15; targets bicipital tendon."},
            {"code": "LI15", "name": "Jianyu (肩髃)", "depth": "0.8-1.5 cun oblique downwards", "technique": "Harmonizing", "rationale": "Cardinal point for all shoulder pathologies in the Yangming channel."},
            {"code": "LU1", "name": "Zhongfu (中府)", "depth": "0.5-0.8 cun oblique lateral (Caution: Pneumothorax!)", "technique": "Harmonizing", "rationale": "Releases pectoralis minor attachment and anterior capsule."}
        ],
        "distal_points": [
            {"code": "ST38", "name": "Tiaokou (条口)", "role": "Empirical Distal Shoulder Point", "technique": "Deep needle towards BL57 with shoulder movement!", "rationale": "The most effective distal balance point for shoulder abduction/flexion restrictions."},
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing", "rationale": "Distal point on Yangming channel regulating shoulder pain."},
            {"code": "LI11", "name": "Quchi (曲池)", "role": "He-Sea Point", "technique": "Harmonizing", "rationale": "Clears local inflammatory stagnation."}
        ],
        "modalities": {
            "electro": "2 Hz EA between Jianneiling and LI15 for 20 minutes.",
            "moxa": "Warm-needle acupuncture (温针灸) on LI15 if shoulder feels stiff and cold.",
            "cupping": "Flash cupping around anterior deltoid; avoid deep bone prominence.",
            "guasha": "Gentle scraping down the anterior arm along the Large Intestine channel.",
            "topical": "Die Da Yao Jiu liniment rubbed vigorously into anterior joint line."
        },
        "red_flags": "Inability to lift arm after fall/trauma (acute full-thickness rotator cuff tear) or unprovoked nocturnal shoulder pain with fever."
    },
    "shoulder_lateral_subacromial": {
        "id": "shoulder_lateral_subacromial",
        "name": "Lateral Shoulder & Subacromial Impingement",
        "chinese": "肩髃风 / 漏肩风 (Frozen Shoulder / Rotator Cuff Bi)",
        "region_group": "Neck & Shoulder",
        "view": "Anterior / Front",
        "anatomical_zone": "Subacromial space, Supraspinatus tendon, Lateral deltoid",
        "meridian": "Hand-Yangming (Large Intestine) & Hand-Shaoyang (San Jiao)",
        "bi_type": "Wind-Cold-Dampness settling in joint capsule, Liver/Kidney Yin/Blood deficiency in middle age (50-year shoulder / 五十肩)",
        "western_correlates": "Supraspinatus tendinopathy, Subacromial bursitis, Adhesive capsulitis",
        "description": "Pain radiating into lateral upper arm, inability to sleep on the affected side, painful arc between 60° and 120° abduction.",
        "local_points": [
            {"code": "LI15", "name": "Jianyu (肩髃)", "depth": "0.8-1.5 cun into subacromial space", "technique": "Harmonizing", "rationale": "Key point in anterior depression of acromion."},
            {"code": "SJ14", "name": "Jianliao (肩髎)", "depth": "0.8-1.5 cun into posterior acromial depression", "technique": "Harmonizing", "rationale": "Paired with LI15 as the two primary pillars of the shoulder joint."},
            {"code": "Jianqian", "name": "Jianqian / Jianneiling", "depth": "0.8-1.2 cun", "technique": "Harmonizing", "rationale": "Anterior shoulder triangle balance point."},
            {"code": "Ashi", "name": "Supraspinatus Ashi Point", "depth": "0.5-0.8 cun oblique", "technique": "Harmonizing", "rationale": "Direct release of myofascial trigger point in supraspinatus fossa."}
        ],
        "distal_points": [
            {"code": "ST38", "name": "Tiaokou (条口)", "role": "Master Distal Balance Point", "technique": "1.5-2.0 cun with active shoulder abduction", "rationale": "Transmits strong sensation through Yangming channel to free the shoulder."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "Hui-Meeting Point for Sinews", "technique": "Harmonizing", "rationale": "Relaxes tendon tension and restores joint range of motion."},
            {"code": "SJ5", "name": "Waiguan (外关)", "role": "Luo-Connecting Point", "technique": "Harmonizing", "rationale": "Clears stagnation along the lateral Shaoyang shoulder."}
        ],
        "modalities": {
            "electro": "Dense-disperse 2/100 Hz between LI15 and SJ14 for 20 minutes.",
            "moxa": "Warm needle moxibustion (温针) directly on LI15 and SJ14 is the gold standard for Frozen Shoulder.",
            "cupping": "Stationary cupping over deltoid muscle belly.",
            "guasha": "Downward scraping along lateral deltoid.",
            "topical": "Herbal plaster (e.g. 701 Die Da Gao) applied overnight."
        },
        "red_flags": "Sudden loss of external rotation strength after minor strain (acute tendon rupture), or signs of septic bursitis (erythema, warmth, systemic fever)."
    },

    # --- ELBOW, WRIST & HAND ---
    "elbow_lateral": {
        "id": "elbow_lateral",
        "name": "Lateral Elbow (Tennis Elbow)",
        "chinese": "肘劳 (Elbow Strain / Lateral Epicondylitis)",
        "region_group": "Elbow, Wrist & Hand",
        "view": "Anterior / Front",
        "anatomical_zone": "Lateral epicondyle of humerus, Extensor carpi radialis brevis tendon",
        "meridian": "Hand-Yangming (Large Intestine Channel)",
        "bi_type": "Repetitive strain Qi & Blood Stagnation, Wind-Cold Bi",
        "western_correlates": "Lateral epicondylitis, Extensor tendon origin microtears, Radial tunnel syndrome",
        "description": "Sharp pain on the outer elbow when gripping objects, lifting a kettle, shaking hands, or typing on a keyboard.",
        "local_points": [
            {"code": "LI11", "name": "Quchi (曲池)", "depth": "0.8-1.2 cun perpendicular", "technique": "Harmonizing / Reducing", "rationale": "He-Sea Earth point; clears inflammation and frees the Large Intestine channel."},
            {"code": "LI10", "name": "Shousanli (手三里)", "depth": "0.8-1.2 cun perpendicular into extensor belly", "technique": "Harmonizing", "rationale": "Relieves deep myofascial trigger point tension in extensor carpi radialis."},
            {"code": "LI12", "name": "Zhouliao (肘髎)", "depth": "0.5-0.8 cun perpendicular into lateral epicondylar ridge", "technique": "Harmonizing", "rationale": "Directly targets tendon insertion onto bone."},
            {"code": "LU5", "name": "Chize (尺泽)", "depth": "0.5-1.0 cun", "technique": "Harmonizing", "rationale": "Balances tension on radial side of cubital fossa."}
        ],
        "distal_points": [
            {"code": "LI4", "name": "Hegu (合谷)", "role": "Yuan-Source Point", "technique": "Reducing", "rationale": "Clears channel stagnation throughout the lower arm."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "Hui-Meeting for Sinews", "technique": "Reinforcing", "rationale": "Systemic nourishment and relaxation for tendon insertions."},
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "Homologous Yangming Opposite Joint", "technique": "Reinforcing", "rationale": "Dr. Tan knee-elbow balance system (Knee balances Elbow)."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between LI11 and LI10 for 20 minutes.",
            "moxa": "Sparingly used moxa roll or mini-moxa directly over lateral epicondyle attachment.",
            "cupping": "Small silicone sliding cup along forearm extensors.",
            "guasha": "Cross-fiber scraping over extensor muscle belly (avoid scraping directly on bone).",
            "topical": "Zheng Gu Shui rub or herbal Arnica/Die Da liniment."
        },
        "red_flags": "Numbness radiating into ring and small fingers (cubital tunnel) or inability to extend wrist (radial nerve palsy / wrist drop)."
    },
    "wrist_carpal": {
        "id": "wrist_carpal",
        "name": "Carpal Tunnel & Wrist Pain",
        "chinese": "腕劳 / 腕管综合征 (Carpal Tunnel Syndrome)",
        "region_group": "Elbow, Wrist & Hand",
        "view": "Anterior / Front",
        "anatomical_zone": "Flexor retinaculum, Transverse carpal ligament, Median nerve path",
        "meridian": "Hand-Jueyin (Pericardium) & Hand-Taiyin (Lung)",
        "bi_type": "Phlegm-Dampness obstructing channels, Qi & Blood Stagnation",
        "western_correlates": "Carpal tunnel syndrome, Flexor tenosynovitis, Repetitive strain injury (RSI)",
        "description": "Numbness, tingling, pins and needles in thumb, index, and middle fingers, worse at night and after typing or driving.",
        "local_points": [
            {"code": "PC7", "name": "Daling (大陵)", "depth": "0.3-0.5 cun perpendicular (Caution: Median nerve!)", "technique": "Harmonizing (gentle insertion)", "rationale": "Located at proximal wrist crease; unblocks flexor retinaculum."},
            {"code": "PC6", "name": "Neiguan (内关)", "depth": "0.5-0.8 cun perpendicular between tendons", "technique": "Harmonizing", "rationale": "Relieves median nerve entrapment and forearm muscle tension."},
            {"code": "LU7", "name": "Lieque (列缺)", "depth": "0.3-0.5 cun oblique proximally", "technique": "Harmonizing", "rationale": "Frees radial styloid and abductor pollicis longus."},
            {"code": "LI5", "name": "Yangxi (阳溪)", "depth": "0.3-0.5 cun in anatomical snuffbox", "technique": "Harmonizing", "rationale": "Relieves radial wrist tension and De Quervain's tenosynovitis."}
        ],
        "distal_points": [
            {"code": "SP9", "name": "Yinlingquan (阴陵泉)", "role": "He-Sea Point (Water)", "technique": "Reducing", "rationale": "Drains internal dampness causing synovial swelling inside the carpal tunnel."},
            {"code": "ST40", "name": "Fenglong (丰隆)", "role": "Empirical Phlegm Point", "technique": "Reducing", "rationale": "Resolves chronic phlegm and tissue edema."},
            {"code": "LR3", "name": "Taichong (太冲)", "role": "Yuan-Source Point", "technique": "Harmonizing", "rationale": "Soothes sinews and unblocks peripheral microcirculation."}
        ],
        "modalities": {
            "electro": "Microcurrent only across PC6 to PC7 (avoid strong motor twitch on median nerve).",
            "moxa": "Indirect warm moxa over wrist crease for cold/damp numbness.",
            "cupping": "Silicone cup on forearm flexor bellies 2-3 inches proximal to wrist.",
            "guasha": "Gua Sha along anterior forearm flexors from elbow to wrist.",
            "topical": "Warm herbal hand soak (Gui Zhi, Hong Hua, Tou Gu Cao)."
        },
        "red_flags": "Thenar muscle wasting (atrophy of thumb pad base) or permanent loss of sensation in thumb/index finger (surgical decompression indication)."
    },

    # --- SPINE & BACK PAIN ---
    "back_upper_trapezius": {
        "id": "back_upper_trapezius",
        "name": "Upper Back & Trapezius / Rhomboid Pain",
        "chinese": "背痛 / 肩胛间区痛 (Interscapular Bi)",
        "region_group": "Spine & Back",
        "view": "Posterior / Back",
        "anatomical_zone": "Upper/middle trapezius, Rhomboids, Levator scapulae, T1-T6 paraspinals",
        "meridian": "Foot-Taiyang (Urinary Bladder Channel - Inner & Outer Lines), Du Mai",
        "bi_type": "Wind-Cold-Damp Bi, Postural Qi Stagnation, Heart/Lung emotional tension",
        "western_correlates": "Upper crossed syndrome, Myofascial trigger points, Thoracic facet syndrome",
        "description": "Deep burning, aching ache between the shoulder blades, chronic knotting in trapezius, exacerbated by sitting at computers and stress.",
        "local_points": [
            {"code": "GB21", "name": "Jianjing (肩井)", "depth": "0.3-0.5 cun posterior (Caution: Lung apex!)", "technique": "Harmonizing", "rationale": "Highest point of shoulder; releases upper trapezius knot."},
            {"code": "BL13", "name": "Feishu (肺俞)", "depth": "0.5-0.8 cun oblique towards spine", "technique": "Harmonizing", "rationale": "T3 level; releases upper thoracic paraspinals."},
            {"code": "BL43", "name": "Gaohuangshu (膏肓俞)", "depth": "0.5-0.8 cun oblique towards spine", "technique": "Reinforcing / Moxa", "rationale": "T4 outer line between spine and scapula; famous point for chronic deep exhaustion and knotting."},
            {"code": "SI11", "name": "Tianzong (天宗)", "depth": "0.5-0.8 cun in center of infraspinatus fossa", "technique": "Harmonizing", "rationale": "Powerful trigger point relieving referred pain between shoulder blades."}
        ],
        "distal_points": [
            {"code": "SI3", "name": "Houxi (后溪)", "role": "Master Point of Du Mai", "technique": "Reducing", "rationale": "Opens the entire upper thoracic spine and scapular region."},
            {"code": "BL60", "name": "Kunlun (昆仑)", "role": "Taiyang Distal Anchor", "technique": "Reducing", "rationale": "Draws tension down along the Bladder meridian lines."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "Hui-Meeting for Sinews", "technique": "Harmonizing", "rationale": "Relaxes chronic muscular contractions."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between BL13 and BL43 for 20 minutes.",
            "moxa": "Warm needle or moxa stick directly on Gaohuangshu (BL43).",
            "cupping": "Sliding cupping along inner and outer Bladder lines from T1 to T8 with herbal oil.",
            "guasha": "Gua Sha over upper trapezius and interscapular region produces immediate release.",
            "topical": "Apply Zheng Gu Shui followed by moist heat."
        },
        "red_flags": "Crushing chest pain radiating to left shoulder blade (myocardial infarction), mid-thoracic pain with fever (discitis), or unremitting night pain."
    },
    "back_lower_lumbar": {
        "id": "back_lower_lumbar",
        "name": "Lower Back Pain & Lumbar Strain / Disc Herniation",
        "chinese": "腰痛 / 肾虚腰痛 (Lumbar Pain / Yaotong)",
        "region_group": "Spine & Back",
        "view": "Posterior / Back",
        "anatomical_zone": "L1-L5 lumbar vertebrae, Quadratus lumborum, Erector spinae, Sacroiliac joint",
        "meridian": "Foot-Taiyang (Urinary Bladder Channel), Du Mai, Dai Mai",
        "bi_type": "Kidney Deficiency (chronic), Acute Blood Stagnation (sprain), Wind-Cold-Dampness",
        "western_correlates": "Acute lumbar muscle sprain, Lumbar disc herniation (L4-L5/L5-S1), Degenerative disc disease",
        "description": "Aching, stiffness, or sharp stabbing in the lower back, difficulty bending forward or standing up from a chair, sensation of vulnerability or cold in lumbar spine.",
        "local_points": [
            {"code": "BL23", "name": "Shenshu (肾俞)", "depth": "0.8-1.2 cun perpendicular towards spine", "technique": "Reinforcing + Moxa (Chronic) / Reducing (Acute)", "rationale": "L2 level; Kidney Back-Shu point nourishing the root of lumbar strength."},
            {"code": "BL25", "name": "Dachangshu (大肠俞)", "depth": "0.8-1.2 cun perpendicular", "technique": "Harmonizing", "rationale": "L4 level; crucial point for lower lumbar vertebral stability."},
            {"code": "DU3", "name": "Yaoyangguan (腰阳关)", "depth": "0.5-1.0 cun perpendicular between L4-L5", "technique": "Harmonizing / Moxa", "rationale": "Lumbar Yang Gate; unblocks spinal canal circulation."},
            {"code": "BL52", "name": "Zhishi (志室)", "depth": "0.5-0.8 cun perpendicular into quadratus lumborum", "technique": "Harmonizing", "rationale": "L2 outer line; releases deep quadratus lumborum muscle spasm."},
            {"code": "Shiqizhui", "name": "Shiqizhui (十七椎)", "depth": "0.8-1.2 cun below L5 spinous process", "technique": "Harmonizing", "rationale": "Empirical extra point for severe discogenic lower back pain."}
        ],
        "distal_points": [
            {"code": "BL40", "name": "Weizhong (委中)", "role": "Command Point of Lumbar & Back", "technique": "Reducing / Bleeding", "rationale": "'For pain in the back and lumbar, seek Weizhong.' Bleed dark veins for acute stabbing blood stasis."},
            {"code": "Yaotongxue", "name": "Yaotongxue (腰痛穴)", "role": "Empirical Lumbar Extra Points", "technique": "Oblique insertion with active lumbar movement!", "rationale": "2 points on dorsum of hand; patient rotates lower back while needles are manipulated."},
            {"code": "BL60", "name": "Kunlun (昆仑)", "role": "Taiyang Distal Anchor", "technique": "Reducing", "rationale": "Frees the entire posterior kinetic chain."},
            {"code": "DU26", "name": "Renzhong (人中)", "role": "Acute Lumbar Sprain Rescue", "technique": "Needle upwards with patient walking/moving back", "rationale": "Restores Du Mai central axis communication in acute sprain."}
        ],
        "modalities": {
            "electro": "2 Hz EA between BL23 and BL25 for 25 minutes gives profound muscular analgesia.",
            "moxa": "Warm-needle acupuncture or moxa box over sacrum/lumbar spine for Kidney Yang deficiency.",
            "cupping": "Stationary cupping along L1-S1 Bladder meridian; wet cupping for dark blood stasis.",
            "guasha": "Downward scraping along lumbar erector spinae.",
            "topical": "Zheng Gu Shui or warm castor oil pack over lower back."
        },
        "red_flags": "Bowel or bladder incontinence / saddle anesthesia around groin (Cauda Equina Emergency!), progressive foot drop, or history of cancer with new back pain."
    },

    # --- HIP & LOWER EXTREMITY PAIN ---
    "hip_sciatica": {
        "id": "hip_sciatica",
        "name": "Sciatica & Piriformis Syndrome / Gluteal Pain",
        "chinese": "坐骨神经痛 / 痹证 (Sciatic Bi)",
        "region_group": "Hip & Lower Extremity",
        "view": "Posterior / Back",
        "anatomical_zone": "Greater trochanter, Piriformis muscle, Sciatic nerve pathway down posterior thigh",
        "meridian": "Foot-Shaoyang (Gallbladder) & Foot-Taiyang (Urinary Bladder)",
        "bi_type": "Wind-Cold-Damp Bi, Qi & Blood Stagnation in Gluteal Channels",
        "western_correlates": "Sciatica, Piriformis syndrome, L5/S1 radiculopathy, Deep gluteal syndrome",
        "description": "Electric, burning, or aching pain shooting from the buttock down the back or side of the thigh into the calf and foot, aggravated by sitting.",
        "local_points": [
            {"code": "GB30", "name": "Huantiao (环跳)", "depth": "2.0-3.5 cun deep needle towards external genitalia", "technique": "Needle to obtain electric Deqi shooting to foot!", "rationale": "Primary master point for sciatica; directly penetrates piriformis and sciatic nerve sheath."},
            {"code": "BL54", "name": "Zhibian (秩边)", "depth": "2.0-3.0 cun perpendicular", "technique": "Needle to obtain sensation radiating to leg", "rationale": "4th sacral foramen level; unblocks deep gluteal nerve branches."},
            {"code": "GB29", "name": "Juliao (居髎)", "depth": "1.0-1.5 cun perpendicular", "technique": "Harmonizing", "rationale": "Anterior to greater trochanter; frees hip flexor and tensor fasciae latae."}
        ],
        "distal_points": [
            {"code": "BL40", "name": "Weizhong (委中)", "role": "Command Point of Lower Back", "technique": "Reducing", "rationale": "Clears posterior sciatic pathway in popliteal fossa."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "Hui-Meeting Point for Sinews", "technique": "Harmonizing", "rationale": "Relaxes nerve sheath and sinews along the lateral leg."},
            {"code": "BL60", "name": "Kunlun (昆仑)", "role": "Taiyang Anchor Point", "technique": "Reducing", "rationale": "Releases tension around lateral malleolus and heel."},
            {"code": "GB41", "name": "Zulinqi (足临泣)", "role": "Shu-Stream (Wood)", "technique": "Harmonizing", "rationale": "Clears lateral foot numbness along the Gallbladder meridian."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between GB30 and BL40 gives intense therapeutic motor release.",
            "moxa": "Warm moxa stick over GB30 and sacrum if pain worsens in rainy or cold weather.",
            "cupping": "Heavy stationary cupping over GB30, BL54, and gluteus medius.",
            "guasha": "Scraping down the IT band and lateral hamstring.",
            "topical": "Apply herbal liniment (Po Sum On) with deep thumb ischemic compression on trigger points."
        },
        "red_flags": "Progressive foot drop (inability to dorsiflex foot), numbness around anus and genitals, or loss of bowel/bladder sphincter tone."
    },
    "knee_patellofemoral": {
        "id": "knee_patellofemoral",
        "name": "Anterior Knee & Patellofemoral / Osteoarthritis",
        "chinese": "鹤膝风 / 膝关节痹 (Crane Knee Bi / Knee Osteoarthritis)",
        "region_group": "Hip & Lower Extremity",
        "view": "Anterior / Front",
        "anatomical_zone": "Infrapatellar fat pad, Patellar tendon, Retropatellar cartilage",
        "meridian": "Foot-Yangming (Stomach), Foot-Taiyin (Spleen), Foot-Jueyin (Liver)",
        "bi_type": "Wind-Cold-Damp Bi, Liver/Kidney Yin & Blood Deficiency, Phlegm-Fluid retention",
        "western_correlates": "Patellofemoral syndrome, Knee osteoarthritis, Jumper's knee (Patellar tendinitis)",
        "description": "Aching, crepitus, stiffness, and pain going up and down stairs, swelling inside the knee capsule, or difficulty fully bending or straightening the leg.",
        "local_points": [
            {"code": "ST35", "name": "Dubi / Waixiyan (犊鼻/外膝眼)", "depth": "0.8-1.2 cun directed towards center of joint", "technique": "Harmonizing", "rationale": "Lateral eye of knee; directly enters the synovial joint space."},
            {"code": "Neixiyan", "name": "Neixiyan (内膝眼)", "depth": "0.8-1.2 cun directed towards center of joint", "technique": "Harmonizing", "rationale": "Paired with ST35 as 'Eyes of the Knee' (Xi Yan); unblocks knee joint capsule."},
            {"code": "Heding", "name": "Heding (鹤顶)", "depth": "0.5-0.8 cun perpendicular/oblique", "technique": "Harmonizing / Moxa", "rationale": "At midpoint of superior patellar border; releases quadriceps tendon insertion."},
            {"code": "ST34", "name": "Liangqiu (梁丘)", "depth": "0.8-1.2 cun perpendicular", "technique": "Harmonizing", "rationale": "Xi-Cleft point of Stomach; stops acute knee inflammation and swelling."}
        ],
        "distal_points": [
            {"code": "ST36", "name": "Zusanli (足三里)", "role": "He-Sea Point (Earth)", "technique": "Reinforcing + Moxa", "rationale": "Builds local circulation and strengthens quadriceps tone."},
            {"code": "SP9", "name": "Yinlingquan (阴陵泉)", "role": "He-Sea Point (Water)", "technique": "Reducing", "rationale": "Primary point to drain joint effusion (water on the knee)."},
            {"code": "GB34", "name": "Yanglingquan (阳陵泉)", "role": "Hui-Meeting Point for Sinews", "technique": "Harmonizing", "rationale": "Stabilizes collateral ligaments and sinew strength."},
            {"code": "SP10", "name": "Xuehai (血海)", "role": "Sea of Blood", "technique": "Harmonizing", "rationale": "Invigorates blood and dispels pathogenic wind from the knee."}
        ],
        "modalities": {
            "electro": "Dense-disperse 2/100 Hz across Xiyan (ST35 to Neixiyan) for 20 minutes.",
            "moxa": "Warm-needle acupuncture (温针灸) on Xiyan and Heding is extremely effective for degenerative arthritis.",
            "cupping": "Cupping over quadriceps bellies above the knee (avoid patella bone).",
            "guasha": "Gentle scraping around the patella perimeter.",
            "topical": "Warm herbal compress with Sanqi and Hong Hua."
        },
        "red_flags": "Hot, bright red, fluctuant joint with fever (septic arthritis), locked knee unable to bend after twist (meniscal tear flap), or inability to bear weight."
    },
    "ankle_achilles": {
        "id": "ankle_achilles",
        "name": "Achilles Tendinitis & Heel Pain / Plantar Fasciitis",
        "chinese": "足跟痛 / 跟腱炎 (Heel Bi / Achilles Strain)",
        "region_group": "Hip & Lower Extremity",
        "view": "Posterior / Back",
        "anatomical_zone": "Achilles tendon, Retrocalcaneal bursa, Plantar aponeurosis",
        "meridian": "Foot-Taiyang (Urinary Bladder) & Foot-Shaoyin (Kidney Channel)",
        "bi_type": "Kidney Deficiency failing to nourish bones/marrow, Blood Stasis from overuse",
        "western_correlates": "Achilles tendinopathy, Plantar fasciitis, Calcaneal spur, Haglund's deformity",
        "description": "First-step morning heel pain when getting out of bed, tenderness pinching the Achilles tendon, pain after running or prolonged standing.",
        "local_points": [
            {"code": "BL60", "name": "Kunlun (昆仑)", "depth": "0.5-0.8 cun between lateral malleolus and Achilles", "technique": "Harmonizing", "rationale": "Fire point of Bladder; clears inflammation in Achilles tendon."},
            {"code": "KD3", "name": "Taixi (太溪)", "depth": "0.5-0.8 cun between medial malleolus and Achilles", "technique": "Reinforcing", "rationale": "Yuan-Source point; nourishes Kidney essence and tendon attachment to calcaneus."},
            {"code": "Shimian", "name": "Shimian (失眠/足跟穴)", "depth": "0.3-0.5 cun perpendicular into plantar heel center", "technique": "Harmonizing / Moxa", "rationale": "Empirical extra point located directly in the center of the heel pad."},
            {"code": "KD1", "name": "Yongquan (涌泉)", "depth": "0.5-0.8 cun perpendicular in anterior third of sole", "technique": "Reinforcing", "rationale": "Stretches plantar fascia and descends Kidney energy."}
        ],
        "distal_points": [
            {"code": "PC7", "name": "Daling (大陵)", "role": "Dr. Tan Balance Method (Wrist balances Heel)", "technique": "Reducing on opposite wrist", "rationale": "Pericardium Jueyin balances Kidney Shaoyin; wrist crease directly mirrors heel!"},
            {"code": "BL57", "name": "Chengshan (承山)", "role": "Gastrocnemius Muscle Bellies", "technique": "Harmonizing", "rationale": "Relaxes calf muscle tension that exerts traction on the Achilles and heel."},
            {"code": "BL40", "name": "Weizhong (委中)", "role": "Command of Back & Lower Leg", "technique": "Reducing", "rationale": "Releases posterior kinetic chain."}
        ],
        "modalities": {
            "electro": "2 Hz low frequency between BL60 and KD3 across the Achilles tendon.",
            "moxa": "Direct moxibustion (7 cones of rice-grain moxa) over plantar heel tender point (Shimian).",
            "cupping": "Stationary cupping over calf muscle belly (BL57).",
            "guasha": "Gua Sha along the plantar fascia and Achilles tendon with warming balm.",
            "topical": "Herbal foot soak in warm vinegar and Carthamus (Hong Hua) broth."
        },
        "red_flags": "Sudden 'pop' or sensation of being kicked in calf followed by inability to perform single-leg heel raise (acute Achilles tendon rupture - positive Thompson test)."
    }
}


# =============================================================================
# TAB RENDER FUNCTION
# =============================================================================
def render_clean_html(html_str: str):
    """Strip all leading and trailing whitespace from every line and render with st.html."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.html(cleaned, unsafe_allow_javascript=True)


def render_pain_map_tab():
    """Render the Interactive 2D Pain Map & External Pain Management tab."""
    # Custom styling
    render_clean_html("""
    <style>
    .pain-card {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
    }
    .pain-badge {
        font-size: 0.76rem;
        font-weight: 800;
        padding: 3px 8px;
        border-radius: 4px;
        text-transform: uppercase;
    }
    .pain-btn-active {
        background: #007ba7 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    /* Hidden trigger buttons for reliable SVG map click dispatch */
    div[data-testid="stVerticalBlock"]:has(> div[class*="st-key-pain_trigger_"]),
    div[class*="st-key-pain_trigger_"] {
        position: absolute !important;
        opacity: 0 !important;
        pointer-events: none !important;
        height: 0px !important;
        width: 0px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    /* SVG Map hotspot hover & interaction styling */
    .pain-hotspot {
        transition: transform 0.18s ease, filter 0.18s ease;
    }
    .pain-hotspot:hover {
        filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.95)) drop-shadow(0 0 14px rgba(0, 123, 167, 0.6));
        cursor: pointer;
    }
    .pain-hotspot:hover rect {
        fill: #0284c7 !important;
        stroke: #38bdf8 !important;
    }
    .pain-hotspot:hover text {
        fill: #ffffff !important;
        font-weight: 800 !important;
    }
    .active-hotspot rect {
        fill: #0284c7 !important;
        stroke: #38bdf8 !important;
        filter: drop-shadow(0 0 6px #38bdf8);
    }
    .active-hotspot text {
        fill: #ffffff !important;
        font-weight: 800 !important;
    }
    </style>
    """)

    # Header Card
    render_clean_html("""
    <div style="background: #0f172a; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 5px solid #007ba7; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);">
        <h2 style="color: #ffffff !important; font-size: 1.6rem; font-weight: 800; margin: 0 0 6px 0;">
            📍 Interactive 2D Pain Map & Musculoskeletal Treatment (痛症辨证)
        </h2>
        <p style="color: #cbd5e1 !important; font-size: 0.95rem; margin: 0;">
            Select any region in pain on the anatomical body map or categorized regional selector below to access comprehensive acupuncture point protocols, Dr. Tan Balance Method distal points, needling techniques, electro-acupuncture frequencies, and moxibustion guidelines.
        </p>
    </div>
    """)

    # Session State Initialization
    if "selected_pain_id" not in st.session_state:
        st.session_state.selected_pain_id = "back_lower_lumbar"

    # Hidden trigger buttons for reliable SVG map click dispatching across all filters
    with st.container():
        for pid in PAIN_DATABASE.keys():
            if st.button(pid, key=f"pain_trigger_{pid}"):
                st.session_state.selected_pain_id = pid
                p_group = PAIN_DATABASE[pid]["region_group"]
                if st.session_state.get("pain_group_filter") not in ["All Body Regions", p_group]:
                    st.session_state["pain_group_filter"] = "All Body Regions"
                if st.session_state.get("pain_search_input"):
                    st.session_state["pain_search_input"] = ""
                st.rerun()

    # REGIONAL CATEGORY BAR & QUICK SELECTOR
    regional_groups = {
        "Head & Face": ["head_frontal", "head_temporal", "head_occiput", "tmj_jaw"],
        "Neck & Shoulder": ["neck_cervical", "shoulder_anterior", "shoulder_lateral_subacromial"],
        "Elbow, Wrist & Hand": ["elbow_lateral", "wrist_carpal"],
        "Spine & Back": ["back_upper_trapezius", "back_lower_lumbar"],
        "Hip & Lower Extremity": ["hip_sciatica", "knee_patellofemoral", "ankle_achilles"]
    }

    # Search Bar & Filter
    col_search, col_group = st.columns([1.5, 1.5])
    with col_search:
        search_kw = st.text_input(
            "🔍 Search Pain Area or Condition (e.g. Migraine, Sciatica, Tennis Elbow, Knee)",
            value="",
            key="pain_search_input"
        ).strip().lower()
    with col_group:
        group_filter = st.selectbox(
            "Filter Body Region",
            options=["All Body Regions"] + list(regional_groups.keys()),
            index=0,
            key="pain_group_filter"
        )

    # Filtered conditions list
    filtered_pains = []
    for pid, pdata in PAIN_DATABASE.items():
        if group_filter != "All Body Regions" and pdata["region_group"] != group_filter:
            continue
        if search_kw:
            match_str = f"{pdata['name']} {pdata['chinese']} {pdata['western_correlates']} {pdata['anatomical_zone']}".lower()
            if search_kw not in match_str:
                continue
        filtered_pains.append(pid)

    # If active selection is not in filtered, default to first available
    if filtered_pains and st.session_state.selected_pain_id not in filtered_pains:
        st.session_state.selected_pain_id = filtered_pains[0]

    # INTERACTIVE 2D ANATOMICAL MAP CANVAS
    def generate_pain_map_svg(active_pain_id: str) -> str:
        svg_hotspots = {
            # Anterior View (Front) - Center x = 265
            "head_frontal": {
                "x": 265, "y": 50, "label": "Forehead & Sinus", "zone": "Frontal / Glabella",
                "view": "front", "text_anchor": "start", "lx": 365, "ly": 48
            },
            "head_temporal": {
                "x": 240, "y": 60, "label": "Temples / Migraine", "zone": "Temporal / Taiyang",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 55
            },
            "tmj_jaw": {
                "x": 248, "y": 92, "label": "TMJ & Jaw Pain", "zone": "Mandible / ST7",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 92
            },
            "shoulder_anterior": {
                "x": 208, "y": 146, "label": "Ant. Shoulder / Biceps", "zone": "Deltopectoral / LU1",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 140
            },
            "shoulder_lateral_subacromial": {
                "x": 178, "y": 158, "label": "Rotator Cuff / Lat. Shoulder", "zone": "Subacromial / LI15",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 175
            },
            "elbow_lateral": {
                "x": 158, "y": 235, "label": "Tennis Elbow", "zone": "Lateral Epicondyle / LI11",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 230
            },
            "wrist_carpal": {
                "x": 146, "y": 315, "label": "Carpal Tunnel / Wrist", "zone": "Volar Wrist / PC7",
                "view": "front", "text_anchor": "end", "lx": 144, "ly": 315
            },
            "knee_patellofemoral": {
                "x": 302, "y": 450, "label": "Patella / Knee OA", "zone": "Eyes of Knee / ST35",
                "view": "front", "text_anchor": "start", "lx": 365, "ly": 450
            },

            # Posterior View (Back) - Center x = 795
            "head_occiput": {
                "x": 795, "y": 66, "label": "Occipital Headache", "zone": "Suboccipital / BL10",
                "view": "back", "text_anchor": "start", "lx": 875, "ly": 62
            },
            "neck_cervical": {
                "x": 795, "y": 118, "label": "Cervical / Stiff Neck", "zone": "C-Spine / Dazhui",
                "view": "back", "text_anchor": "start", "lx": 875, "ly": 115
            },
            "back_upper_trapezius": {
                "x": 748, "y": 155, "label": "Trapezius / Rhomboid", "zone": "Upper Scapular / GB21",
                "view": "back", "text_anchor": "end", "lx": 675, "ly": 155
            },
            "back_lower_lumbar": {
                "x": 795, "y": 275, "label": "Lower Lumbar Strain", "zone": "L2-L5 / Yaoyan / BL23",
                "view": "back", "text_anchor": "start", "lx": 875, "ly": 275
            },
            "hip_sciatica": {
                "x": 755, "y": 345, "label": "Sciatica / Piriformis", "zone": "Gluteal / GB30",
                "view": "back", "text_anchor": "end", "lx": 675, "ly": 345
            },
            "ankle_achilles": {
                "x": 758, "y": 565, "label": "Achilles / Heel Pain", "zone": "Achilles Tendon / BL60",
                "view": "back", "text_anchor": "end", "lx": 675, "ly": 565
            }
        }

        markers_markup = []
        for pid, pt in svg_hotspots.items():
            is_active = (pid == active_pain_id)
            active_class = "active-hotspot" if is_active else ""

            # Visual properties
            line_color = "#38bdf8" if is_active else "rgba(200, 150, 102, 0.45)"
            line_dash = "none" if is_active else "2 2"
            badge_fill = "#0284c7" if is_active else "#182234"
            badge_border = "#38bdf8" if is_active else "rgba(255, 255, 255, 0.2)"
            text_color = "#ffffff" if is_active else "#cbd5e1"
            pulse_color = "#38bdf8" if is_active else "#c89666"

            badge_w = 132
            badge_h = 24
            if pt["text_anchor"] == "end":
                rect_x = pt["lx"] - badge_w
                text_x = pt["lx"] - 8
            else:
                rect_x = pt["lx"]
                text_x = pt["lx"] + 8
            rect_y = pt["ly"] - 14
            text_y = pt["ly"] + 2

            escaped_label = pt["label"].replace('&', '&amp;')

            if is_active:
                pulse_element = f"""
                <circle cx="{pt['x']}" cy="{pt['y']}" r="18" fill="none" stroke="{pulse_color}" stroke-width="2.5">
                    <animate attributeName="r" values="8;24;8" dur="2s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.9;0.1;0.9" dur="2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="{pt['x']}" cy="{pt['y']}" r="8" fill="{pulse_color}" stroke="#ffffff" stroke-width="2"/>
                """
            else:
                pulse_element = f"""
                <circle cx="{pt['x']}" cy="{pt['y']}" r="12" fill="none" stroke="{pulse_color}" stroke-width="1.2" opacity="0.6">
                    <animate attributeName="r" values="6;16;6" dur="3s" repeatCount="indefinite"/>
                    <animate attributeName="opacity" values="0.6;0.15;0.6" dur="3s" repeatCount="indefinite"/>
                </circle>
                <circle cx="{pt['x']}" cy="{pt['y']}" r="5.5" fill="{pulse_color}" stroke="#0f172a" stroke-width="1.5"/>
                """

            markers_markup.append(f"""
            <g id="spot-{pid}" class="pain-hotspot {active_class}" onclick="window.selectPainArea('{pid}')" style="cursor: pointer;">
                <!-- Transparent Hit Target for Effortless Mouse & Touch Clicking -->
                <circle cx="{pt['x']}" cy="{pt['y']}" r="26" fill="transparent"/>
                {pulse_element}
                <line x1="{pt['x']}" y1="{pt['y']}" x2="{pt['lx']}" y2="{pt['ly']}" stroke="{line_color}" stroke-width="1.4" stroke-dasharray="{line_dash}"/>
                <rect x="{rect_x}" y="{rect_y}" width="{badge_w}" height="{badge_h}" rx="6" fill="{badge_fill}" stroke="{badge_border}" stroke-width="1.2"/>
                <text x="{text_x}" y="{text_y}" fill="{text_color}" font-size="10.5" font-weight="700" font-family="-apple-system, sans-serif" text-anchor="{pt['text_anchor']}">
                    {escaped_label}
                </text>
            </g>
            """)

        all_markers_html = "".join(markers_markup)

        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    body {{
        margin: 0;
        padding: 0;
        background: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #ffffff;
        overflow: hidden;
    }}
    .pain-hotspot {{
        transition: transform 0.18s ease, filter 0.18s ease;
    }}
    .pain-hotspot:hover {{
        filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.95)) drop-shadow(0 0 14px rgba(0, 123, 167, 0.6));
        cursor: pointer;
    }}
    .pain-hotspot:hover rect {{
        fill: #0284c7 !important;
        stroke: #38bdf8 !important;
    }}
    .pain-hotspot:hover text {{
        fill: #ffffff !important;
        font-weight: 800 !important;
    }}
    .active-hotspot rect {{
        fill: #0284c7 !important;
        stroke: #38bdf8 !important;
        filter: drop-shadow(0 0 6px #38bdf8);
    }}
    .active-hotspot text {{
        fill: #ffffff !important;
        font-weight: 800 !important;
    }}
</style>
</head>
<body>
    <div style="background: #0f172a; border: 1.5px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; padding: 0 6px;">
            <span style="font-size: 0.88rem; color: #38bdf8; font-weight: 700;">
                👆 <strong>Interactive Anatomical Pain Map:</strong> Click any glowing pain hotspot on the body to instantly inspect its acupuncture protocol.
            </span>
            <span style="font-size: 0.78rem; color: #94a3b8; font-family: monospace;">
                14 Active Trigger Zones
                </span>
            </div>

            <svg viewBox="0 0 1060 640" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-height: 620px; background: #0b1120; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);">
                <defs>
                    <linearGradient id="humanSkinGrad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#1e293b"/>
                        <stop offset="50%" stop-color="#172235"/>
                        <stop offset="100%" stop-color="#0f172a"/>
                    </linearGradient>
                </defs>

                <!-- Medical Grid Lines -->
                <g stroke="rgba(255,255,255,0.04)" stroke-width="1">
                    <line x1="530" y1="20" x2="530" y2="620" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4 4"/>
                    <line x1="40" y1="160" x2="1020" y2="160"/>
                    <line x1="40" y1="320" x2="1020" y2="320"/>
                    <line x1="40" y1="460" x2="1020" y2="460"/>
                </g>

                <!-- Header Labels -->
                <rect x="185" y="16" width="160" height="26" rx="6" fill="#182234" stroke="#007ba7" stroke-width="1.2"/>
                <text x="265" y="33" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif" letter-spacing="1">ANTERIOR (FRONT VIEW)</text>

                <rect x="715" y="16" width="160" height="26" rx="6" fill="#182234" stroke="#c89666" stroke-width="1.2"/>
                <text x="795" y="33" fill="#fde68a" font-size="11" font-weight="800" text-anchor="middle" font-family="-apple-system, sans-serif" letter-spacing="1">POSTERIOR (BACK VIEW)</text>

                <!-- 1. ANTERIOR HUMAN SILHOUETTE (Center x = 265) -->
                <g id="anterior-anatomy" fill="url(#humanSkinGrad)" stroke="#38bdf8" stroke-width="1.4">
                    <!-- Head & Cranium (Anatomical Oval with Jawline) -->
                    <path d="M 265,34 C 244,34 233,48 233,68 C 233,86 240,99 249,106 L 246,134 L 284,134 L 281,106 C 290,99 297,86 297,68 C 297,48 286,34 265,34 Z"/>
                    
                    <!-- Facial Landmark Contours -->
                    <path d="M 252,60 Q 257,58 261,60 M 269,60 Q 273,58 278,60" stroke="rgba(255,255,255,0.25)" stroke-width="1" fill="none"/>
                    <path d="M 265,60 L 265,76 L 261,81 L 269,81" stroke="rgba(255,255,255,0.22)" stroke-width="1" fill="none"/>
                    <path d="M 258,92 Q 265,95 272,92" stroke="rgba(255,255,255,0.25)" stroke-width="1" fill="none"/>

                    <!-- Neck & SCM (Sternocleidomastoid) Lines -->
                    <path d="M 248,112 Q 256,124 262,134 M 282,112 Q 274,124 268,134" stroke="rgba(255,255,255,0.26)" stroke-width="1.2" fill="none"/>

                    <!-- Torso, Arms & Lower Body (Complete Anatomical Musculoskeletal Contour) -->
                    <path d="M 246,134 
                             C 228,136 205,140 182,146 
                             C 172,151 164,162 161,176 
                             C 158,190 156,206 154,222 
                             C 152,234 148,248 144,266 
                             C 140,284 136,301 132,314 
                             C 128,326 124,338 121,348 
                             C 119,356 122,362 126,362 
                             C 130,362 133,356 135,348 
                             C 137,338 140,324 143,314 
                             C 146,301 150,284 154,266 
                             L 158,236 
                             C 162,222 166,210 172,198 
                             C 176,190 182,186 190,184 
                             L 194,212 
                             C 197,235 202,258 208,278 
                             C 212,290 216,304 218,318 
                             L 218,351 
                             C 212,374 206,406 202,438 
                             C 199,461 198,481 200,504 
                             C 202,526 206,554 210,578 
                             C 212,590 214,600 218,604 
                             C 222,608 230,608 234,602 
                             C 236,596 236,586 234,574 
                             C 232,551 230,526 228,501 
                             C 226,476 226,454 228,438 
                             C 230,406 237,376 247,351 
                             L 265,351 
                             L 283,351 
                             C 293,376 300,406 302,438 
                             C 304,454 304,476 302,501 
                             C 300,526 298,551 296,574 
                             C 294,586 294,596 296,602 
                             C 300,608 308,608 312,604 
                             C 316,600 318,590 320,578 
                             C 324,554 328,526 330,504 
                             C 332,481 331,461 328,438 
                             C 324,406 318,374 312,351 
                             L 312,318 
                             C 314,304 318,290 322,278 
                             C 328,258 333,235 336,212 
                             L 340,184 
                             C 348,186 354,190 358,198 
                             C 364,210 368,222 372,236 
                             L 376,266 
                             C 380,284 384,301 387,314 
                             C 390,324 393,338 395,348 
                             C 397,356 400,362 404,362 
                             C 408,362 411,356 409,348 
                             C 406,338 402,326 398,314 
                             C 394,301 390,284 386,266 
                             C 382,248 378,234 376,222 
                             C 374,206 372,190 369,176 
                             C 366,162 358,151 348,146 
                             C 325,140 302,136 284,134 Z" 
                          fill="url(#humanSkinGrad)" stroke="#38bdf8" stroke-width="1.3"/>

                    <!-- Clavicles (Collarbones) -->
                    <path d="M 265,138 C 251,136 230,140 206,148 M 265,138 C 279,136 300,140 324,148" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" fill="none"/>
                    
                    <!-- Pectoral Muscular Curves -->
                    <path d="M 230,158 C 235,182 258,190 265,190 C 272,190 295,182 300,158" stroke="rgba(56,189,248,0.25)" stroke-width="1.2" fill="none"/>
                    
                    <!-- Sternal Line (Ren Meridian / CV axis) -->
                    <line x1="265" y1="138" x2="265" y2="285" stroke="rgba(255,255,255,0.2)" stroke-width="1.2" stroke-dasharray="3 3"/>
                    
                    <!-- Navel (Umbilicus / CV8 Shenque) -->
                    <circle cx="265" cy="270" r="2.5" fill="#38bdf8" stroke="rgba(255,255,255,0.6)" stroke-width="1"/>

                    <!-- Kneecaps (Patellae & Eyes of Knee) -->
                    <ellipse cx="228" cy="450" rx="8" ry="10" fill="none" stroke="rgba(56,189,248,0.45)" stroke-width="1.3"/>
                    <ellipse cx="302" cy="450" rx="8" ry="10" fill="none" stroke="rgba(56,189,248,0.45)" stroke-width="1.3"/>
                </g>

                <!-- 2. POSTERIOR HUMAN SILHOUETTE (Center x = 795) -->
                <g id="posterior-anatomy" fill="url(#humanSkinGrad)" stroke="#c89666" stroke-width="1.4">
                    <!-- Occipital Skull -->
                    <path d="M 795,34 C 774,34 763,48 763,68 C 763,86 770,99 779,106 L 776,134 L 814,134 L 811,106 C 820,99 827,86 827,68 C 827,48 816,34 795,34 Z"/>

                    <!-- Neck & C7 Vertebra (Dazhui DU14) -->
                    <circle cx="795" cy="128" r="2.8" fill="#fde68a" stroke="rgba(255,255,255,0.5)" stroke-width="1"/>

                    <!-- Full Continuous Posterior Body -->
                    <path d="M 776,134 
                             C 758,136 735,140 712,146 
                             C 702,151 694,162 691,176 
                             C 688,190 686,206 684,222 
                             C 682,234 678,248 674,266 
                             C 670,284 666,301 662,314 
                             C 658,326 654,338 651,348 
                             C 649,356 652,362 656,362 
                             C 660,362 663,356 665,348 
                             C 667,338 670,324 673,314 
                             C 676,301 680,284 684,266 
                             L 688,236 
                             C 692,222 696,210 702,198 
                             C 706,190 712,186 720,184 
                             L 724,212 
                             C 727,235 732,258 738,278 
                             C 742,290 746,304 748,318 
                             L 748,351 
                             C 742,374 736,406 732,438 
                             C 729,461 728,481 730,504 
                             C 732,526 736,554 740,578 
                             C 742,590 744,600 748,604 
                             C 752,608 760,608 764,602 
                             C 766,596 766,586 764,574 
                             C 762,551 760,526 758,501 
                             C 756,476 756,454 758,438 
                             C 760,406 767,376 777,351 
                             L 795,351 
                             L 813,351 
                             C 823,376 830,406 832,438 
                             C 834,454 834,476 832,501 
                             C 830,526 828,551 826,574 
                             C 824,586 824,596 826,602 
                             C 830,608 838,608 842,604 
                             C 846,600 848,590 850,578 
                             C 854,554 858,526 860,504 
                             C 862,481 861,461 858,438 
                             C 854,406 848,374 842,351 
                             L 842,318 
                             C 844,304 848,290 852,278 
                             C 858,258 863,235 866,212 
                             L 870,184 
                             C 878,186 884,190 888,198 
                             C 894,210 898,222 902,236 
                             L 906,266 
                             C 910,284 914,301 917,314 
                             C 920,324 923,338 925,348 
                             C 927,356 930,362 934,362 
                             C 938,362 941,356 939,348 
                             C 936,338 932,326 928,314 
                             C 924,301 920,284 916,266 
                             C 912,248 908,234 906,222 
                             C 904,206 902,190 899,176 
                             C 896,162 888,151 878,146 
                             C 855,140 832,136 814,134 Z" 
                          fill="url(#humanSkinGrad)" stroke="#c89666" stroke-width="1.3"/>

                    <!-- Trapezius Muscle Diamond -->
                    <path d="M 795,128 L 748,152 L 795,215 L 842,152 Z" stroke="rgba(200,150,102,0.25)" stroke-width="1.2" fill="none"/>

                    <!-- Scapulae (Shoulder Blades) -->
                    <path d="M 755,158 L 742,198 L 762,198 Z" stroke="rgba(255,255,255,0.25)" stroke-width="1.2" fill="none"/>
                    <path d="M 835,158 L 848,198 L 828,198 Z" stroke="rgba(255,255,255,0.25)" stroke-width="1.2" fill="none"/>

                    <!-- Spinal Column Axis (Du Meridian) -->
                    <line x1="795" y1="128" x2="795" y2="335" stroke="rgba(200,150,102,0.32)" stroke-width="1.4" stroke-dasharray="3 3"/>

                    <!-- Gluteal Cleft & Fold -->
                    <path d="M 795,315 L 795,351" stroke="rgba(255,255,255,0.28)" stroke-width="1.3"/>
                    <path d="M 760,351 C 778,354 795,351 795,351 C 795,351 812,354 830,351" stroke="rgba(200,150,102,0.22)" stroke-width="1.2" fill="none"/>

                    <!-- Popliteal Creases (Behind Knees / Weizhong BL40) -->
                    <line x1="752" y1="450" x2="768" y2="450" stroke="rgba(255,255,255,0.25)" stroke-width="1.2"/>
                    <line x1="822" y1="450" x2="838" y2="450" stroke="rgba(255,255,255,0.25)" stroke-width="1.2"/>

                    <!-- Achilles Tendons -->
                    <line x1="758" y1="540" x2="758" y2="575" stroke="rgba(200,150,102,0.4)" stroke-width="2"/>
                    <line x1="832" y1="540" x2="832" y2="575" stroke="rgba(200,150,102,0.4)" stroke-width="2"/>
                </g>

                <!-- 3. INTERACTIVE HOTSPOTS LAYER WITH DIRECT CLICK HANDLER -->
                {all_markers_html}
            </svg>

            <!-- Direct Click Event Dispatcher Script -->
            <script>
            window.selectPainArea = function(pid) {{
                try {{
                    var allSpots = document.querySelectorAll('.pain-hotspot');
                    for (var i = 0; i < allSpots.length; i++) {{
                        allSpots[i].classList.remove('active-hotspot');
                    }}
                    var spotEl = document.getElementById('spot-' + pid);
                    if (spotEl) {{
                        spotEl.classList.add('active-hotspot');
                    }}
                    
                    var targetDoc = null;
                    try {{
                        if (window.parent && window.parent.document) {{
                            targetDoc = window.parent.document;
                        }}
                    }} catch(err) {{
                        targetDoc = null;
                    }}
                    if (!targetDoc) {{
                        targetDoc = document;
                    }}

                    var btn = targetDoc.querySelector('.st-key-pain_btn_' + pid + ' button') || 
                              targetDoc.querySelector('.st-key-pain_trigger_' + pid + ' button');
                    if (btn) {{
                        btn.click();
                        return;
                    }}
                    
                    var allBtns = targetDoc.querySelectorAll('button');
                    for (var j = 0; j < allBtns.length; j++) {{
                        var b = allBtns[j];
                        var p = b.closest ? b.closest('[class*="st-key-pain_btn_' + pid + '"]') : null;
                        if (p || (b.id && (b.id.indexOf('pain_btn_' + pid) !== -1 || b.id.indexOf('pain_trigger_' + pid) !== -1))) {{
                            b.click();
                            return;
                        }}
                    }}
                }} catch(e) {{
                    console.error('Error selecting pain area:', e);
                }}
            }};
            </script>
        </div>
    </body>
    </html>
    """

    # Display Anatomical Interactive SVG Map using st.iframe
    st.iframe(generate_pain_map_svg(st.session_state.selected_pain_id), height=665)

    render_clean_html("""
    <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 10px; padding: 12px 18px; margin: 12px 0 12px 0;">
        <span style="font-size: 1rem; font-weight: 700; color: #38bdf8;">Select Pain Area Below to Inspect Clinical Protocol:</span>
    </div>
    """)

    # Visual Region Selector Buttons in Grid
    cols_btn = st.columns(4)
    for idx, pid in enumerate(filtered_pains):
        c = cols_btn[idx % 4]
        pdata = PAIN_DATABASE[pid]
        is_selected = (pid == st.session_state.selected_pain_id)
        btn_type = "primary" if is_selected else "secondary"
        if c.button(
            f"{'📍 ' if is_selected else ''}{pdata['name'].split('(')[0].split('&')[0].strip()}",
            type=btn_type,
            use_container_width=True,
            key=f"pain_btn_{pid}"
        ):
            st.session_state.selected_pain_id = pid
            st.rerun()

    st.write("")

    # ACTIVE PAIN PROTOCOL CARD DISPLAY
    active_id = st.session_state.selected_pain_id
    if active_id not in PAIN_DATABASE:
        active_id = "back_lower_lumbar"
    
    active_pain = PAIN_DATABASE[active_id]

    render_clean_html(f"""
    <div style="background: #111827; border: 2px solid #007ba7; border-radius: 12px; padding: 22px 26px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
            <div>
                <span style="background: rgba(0, 123, 167, 0.35); color: #38bdf8; font-size: 0.75rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; text-transform: uppercase;">
                    {active_pain['region_group']} · {active_pain['view']}
                </span>
                <span style="background: rgba(200, 150, 102, 0.25); color: #fde68a; font-size: 0.75rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; margin-left: 6px;">
                    {active_pain['bi_type']}
                </span>
                <h3 style="color: #ffffff !important; font-size: 1.55rem; font-weight: 800; margin: 8px 0 2px 0;">
                    {active_pain['name']}
                </h3>
                <div style="color: #c89666; font-size: 1.1rem; font-weight: 700;">
                    {active_pain['chinese']}
                </div>
            </div>
            <div style="text-align: right; background: #182234; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 8px 14px;">
                <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;">Channel Division</div>
                <div style="font-size: 0.95rem; font-weight: 800; color: #38bdf8;">{active_pain['meridian']}</div>
            </div>
        </div>

        <div style="display: flex; gap: 16px; margin: 12px 0 8px 0; font-size: 0.88rem; color: #cbd5e1;">
            <div><strong>Anatomical Site:</strong> {active_pain['anatomical_zone']}</div>
            <div><strong>Western Correlates:</strong> <span style="color: #e2e8f0;">{active_pain['western_correlates']}</span></div>
        </div>

        <div style="font-size: 0.95rem; color: #cbd5e1; line-height: 1.55; margin-top: 8px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 10px;">
            {active_pain['description']}
        </div>
    </div>
    """)

    # TWO COLUMNS: LOCAL POINTS VS DISTAL BALANCE POINTS
    col_local, col_distal = st.columns(2)

    with col_local:
        render_clean_html("""
        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 4px solid #38bdf8; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff !important;">📍 Primary Local Points (Ashi & Anatomical Targets)</div>
            <div style="font-size: 0.8rem; color: #cbd5e1;">Needling into and surrounding the direct site of pain.</div>
        </div>
        """)

        for pt in active_pain["local_points"]:
            render_clean_html(f"""
            <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px 14px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #38bdf8; font-size: 1.02rem;">{pt['code']} · {pt['name']}</span>
                    <span style="font-size: 0.75rem; font-weight: 700; color: #c89666; background: rgba(200, 150, 102, 0.2); padding: 2px 6px; border-radius: 4px;">{pt['technique']}</span>
                </div>
                <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 4px;">
                    <strong>Depth & Angle:</strong> {pt['depth']}
                </div>
                <div style="font-size: 0.86rem; color: #e2e8f0; line-height: 1.45;">
                    {pt['rationale']}
                </div>
            </div>
            """)

    with col_distal:
        render_clean_html("""
        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 4px solid #c89666; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff !important;">🌐 Master Distal & Balance Method Points (Dr. Tan / Master Tung)</div>
            <div style="font-size: 0.8rem; color: #cbd5e1;">Contralateral & channel-balancing points manipulated during patient movement.</div>
        </div>
        """)

        for pt in active_pain["distal_points"]:
            render_clean_html(f"""
            <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px 14px; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 800; color: #c89666; font-size: 1.02rem;">{pt['code']} · {pt['name']}</span>
                    <span style="font-size: 0.75rem; font-weight: 700; color: #38bdf8; background: rgba(0, 123, 167, 0.2); padding: 2px 6px; border-radius: 4px;">{pt['role']}</span>
                </div>
                <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 4px;">
                    <strong>Needling Method:</strong> {pt['technique']}
                </div>
                <div style="font-size: 0.86rem; color: #e2e8f0; line-height: 1.45;">
                    {pt['rationale']}
                </div>
            </div>
            """)

    # CLINICAL ADJUNCTIVE MODALITIES & RED FLAGS
    st.write("")
    c_mod, c_flag = st.columns([1.2, 0.8])

    with c_mod:
        render_clean_html("""
        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 4px solid #484eb2; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 800; color: #ffffff !important;">⚡ Adjunctive Physical Modalities Protocol</div>
            <div style="font-size: 0.8rem; color: #cbd5e1;">Electro-acupuncture, Moxibustion, Cupping, Gua Sha, and Topicals.</div>
        </div>
        """)

        mods = active_pain["modalities"]
        render_clean_html(f"""
        <div style="background: #111827; border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 14px 18px; font-size: 0.88rem; line-height: 1.6;">
            <div style="margin-bottom: 8px;"><strong style="color: #38bdf8;">Electro-Acupuncture (EA):</strong> <span style="color: #e2e8f0;">{mods['electro']}</span></div>
            <div style="margin-bottom: 8px;"><strong style="color: #c89666;">Moxibustion (灸法):</strong> <span style="color: #e2e8f0;">{mods['moxa']}</span></div>
            <div style="margin-bottom: 8px;"><strong style="color: #34d399;">Cupping (拔罐):</strong> <span style="color: #e2e8f0;">{mods['cupping']}</span></div>
            <div style="margin-bottom: 8px;"><strong style="color: #c7d2fe;">Gua Sha (刮痧):</strong> <span style="color: #e2e8f0;">{mods['guasha']}</span></div>
            <div><strong style="color: #fca5a5;">Topical Liniments & Plasters:</strong> <span style="color: #e2e8f0;">{mods['topical']}</span></div>
        </div>
        """)

    with c_flag:
        render_clean_html("""
        <div style="background: #182234; border: 1px solid rgba(255, 255, 255, 0.12); border-left: 4px solid #ef4444; border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
            <div style="font-size: 1.05rem; font-weight: 800; color: #ef4444 !important;">⚠️ Clinical Red Flags & Referral Warnings</div>
            <div style="font-size: 0.8rem; color: #cbd5e1;">Conditions mandating immediate emergency or surgical evaluation.</div>
        </div>
        """)

        render_clean_html(f"""
        <div style="background: rgba(239, 68, 68, 0.1); border: 1.5px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 16px 18px;">
            <div style="font-size: 0.88rem; color: #fca5a5; line-height: 1.55; font-weight: 500;">
                {active_pain['red_flags']}
            </div>
            <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 12px; border-top: 1px solid rgba(239, 68, 68, 0.2); padding-top: 8px;">
                <em>Always perform physical motor, sensory, reflex, and vascular tests before needle insertion.</em>
            </div>
        </div>
        """)

    # 1-Click SOAP Note Generation for Musculoskeletal Pain Condition
    st.write("")
    curr_pain_id = st.session_state.selected_pain_id
    if st.button(f"📋 Generate Clinical SOAP Note for {active_pain['name']}", key=f"btn_soap_pain_{curr_pain_id}", use_container_width=True):
        pts_list = active_pain.get("local_points", []) + active_pain.get("distal_points", [])
        pts_str = ", ".join([f"{pt['code']} ({pt['name']})" for pt in pts_list]) if pts_list else "Local and distal points"
        mods_dict = active_pain.get("modalities", {})
        
        st.session_state.soap_data = {
            "patient_name": "Encounter #" + curr_pain_id.upper()[:8],
            "patient_age": 35,
            "patient_gender": "Male",
            "visit_date": str(date.today()),
            "chief_complaint": f"Acute/Subacute pain localized to {active_pain.get('anatomical_zone', 'affected area')}. Diagnosed as {active_pain['name']} ({active_pain.get('chinese', '')}).",
            "duration": "1-3 weeks",
            "modalities": "Aggravated by movement, weight-bearing, and cold; relieved by rest, gentle warmth, and compression.",
            "secondary_symptoms": f"Restricted range of motion in {active_pain.get('anatomical_zone', 'affected area')}, localized muscular guarding.",
            "tongue_body": "Slight dusky or normal pale red",
            "tongue_coat": "Thin white coat",
            "pulse_qualities": "Wiry (弦) or Tight (紧) matching channel pain",
            "palpation_findings": f"Local Ah Shi tenderness and trigger points at {active_pain.get('anatomical_zone', 'affected area')}; channel palpation positive.",
            "tcm_diagnosis": f"{active_pain['name']} - Bi Syndrome / Qi & Blood Stagnation ({active_pain.get('chinese', '')})",
            "eight_principles": "Interior/Exterior, Excess, Cold/Wind, Stagnation",
            "pathogenesis": f"Channel Qi and Blood stasis in {active_pain.get('meridian', 'local channels')}; localized blockage of microcirculation (不通则痛).",
            "western_correlate": active_pain.get("western_correlates", ""),
            "primary_points": pts_str,
            "needle_technique": f"Local and distal balancing needling. De Qi obtained. Electro-acupuncture: {mods_dict.get('electro', 'Standard')}.",
            "retention_time": "25-30 minutes",
            "adjunctive_modalities": f"Cupping: {mods_dict.get('cupping', 'Indicated')}. Moxa: {mods_dict.get('moxa', 'Indicated')}.",
            "herbal_formula": "Huo Luo Xiao Ling Dan (活络效灵丹) or Shen Tong Zhu Yu Tang (身痛逐瘀汤)",
            "lifestyle_diet": f"Topical: {mods_dict.get('topical', 'Herbal liniment')}. Ergonomic adjustments, avoid direct cold drafts.",
            "treatment_course": "2-3 sessions per week for 2-4 weeks; reassess range of motion weekly."
        }
        st.session_state.target_nav_tab = "SOAP Notes"
        st.rerun()

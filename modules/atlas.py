# -*- coding: utf-8 -*-
"""Acupuncture Atlas & Clinical Explorer Module.

Faithfully modeled directly after https://acupuntura.com/en/atlas/:
- Swiss-style modern minimalist medical typography and responsive layout
- Monolith header with live statistics and WHO/CEIMEC evidence-based standards
- Full-width Swiss Meridian Grid Cards with giant Chinese character watermarks
- Meridian Point Explorer: Clicking a meridian pops up its complete sequence of points
  with thumbnails, Pinyin, Hanzi, translation, indication tags, and Danger/Caution/Safe badges
- Deep Clinical Point Profile (modeled after https://acupuntura.com/en/atlas/stomach/ST-36/):
  * High-Resolution Clinical Point Location Photography with click-to-zoom Lightbox
  * Visual Needle Depth gauge with highlighted insertion range
  * Clinical Safety Precautions alert box
  * Location, practical Cun palpation guide (steps 1, 2, 3), and anatomical landmarks
  * TCM energetics, Five-Element functions, and organ clock
  * Clinical indications, evidence-based symptoms, and classical point combinations
  * Previous / Next point sequential navigation
- Multi-Script Instant Global Search (Code, Pinyin, Hanzi, English, Clinical Conditions)
"""

import json
from pathlib import Path
from typing import Dict, Any

MODULE_DIR = Path(__file__).resolve().parent
STATIC_DIR = MODULE_DIR.parent / "static"

def get_atlas_dataset() -> Dict[str, Any]:
    """Load complete 429-point dataset and 16 meridians from static JSON."""
    meridians_file = STATIC_DIR / "atlas_meridians.json"
    points_file = STATIC_DIR / "atlas_points.json"

    if meridians_file.exists() and points_file.exists():
        with open(meridians_file, "r", encoding="utf-8") as f_m:
            meridians = json.load(f_m)
        with open(points_file, "r", encoding="utf-8") as f_p:
            points = json.load(f_p)
        return {"meridians": meridians, "points": points}
    
    # Fallback to minimal dataset if static files are missing
    return {"meridians": [], "points": {}}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Acupuncture Atlas — Classical Points & 14 Meridians</title>
<style>
/* Swiss Medical Minimalist Design System */
:root {
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    --bg-page: #f8fafc;
    --bg-surface: #ffffff;
    --bg-surface-low: #f1f5f9;
    --bg-surface-high: #e2e8f0;
    --border-subtle: #e2e8f0;
    --border-strong: #cbd5e1;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --text-dim: #94a3b8;
    --accent-blue: #007ba7;
    --accent-blue-subtle: #e0f2fe;
    --accent-fawn: #c89666;
    --accent-fawn-subtle: #faf6f0;
    --accent-violet: #484eb2;
    --accent-violet-subtle: #eef0fb;
    --signal-danger: #ef4444;
    --signal-danger-bg: #fef2f2;
    --signal-danger-border: #fca5a5;
    --signal-caution: #d97706;
    --signal-caution-bg: #fffbeb;
    --signal-caution-border: #fcd34d;
    --signal-safe: #10b981;
    --signal-safe-bg: #ecfdf5;
    --signal-safe-border: #6ee7b7;
    --card-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05);
    --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
}

[data-theme="dark"] {
    --bg-page: #0b0f19;
    --bg-surface: #111827;
    --bg-surface-low: #1f2937;
    --bg-surface-high: #374151;
    --border-subtle: #1f2937;
    --border-strong: #374151;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
    --accent-blue: #38bdf8;
    --accent-blue-subtle: #082f49;
    --accent-fawn: #deb887;
    --accent-fawn-subtle: #231e18;
    --accent-violet: #7b80d9;
    --accent-violet-subtle: #181938;
    --signal-danger: #f87171;
    --signal-danger-bg: #450a0a;
    --signal-danger-border: #7f1d1d;
    --signal-caution: #fbbf24;
    --signal-caution-bg: #451a03;
    --signal-caution-border: #78350f;
    --signal-safe: #34d399;
    --signal-safe-bg: #064e3b;
    --signal-safe-border: #065f46;
    --card-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
    --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body {
    font-family: var(--font-sans);
    background-color: transparent !important;
    color: var(--text-primary);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    overflow: hidden !important;
    height: auto !important;
    min-height: 0 !important;
}

/* App Wrapper - Desktop Full Screen Integration */
.atlas-wrapper {
    max-width: 1520px;
    width: 100%;
    margin: 0 auto;
    padding: 8px 4px 32px 4px;
}

/* Stats Ribbon Bar */
.stats-ribbon {
    border: 1px solid var(--border-subtle);
    background-color: var(--bg-surface-low);
    margin-top: 0;
    margin-bottom: 16px;
    border-radius: 8px;
}

.stats-container {
    padding: 8px 12px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 14px;
    font-size: 0.8rem;
    font-family: var(--font-mono);
}

.stat-item {
    display: flex;
    align-items: baseline;
    gap: 5px;
}

.stat-val {
    font-weight: 800;
    color: var(--text-primary);
}

.stat-lbl {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
}

.stat-sep {
    color: var(--border-strong);
}

.guide-modal-btn {
    background: var(--accent-fawn-subtle);
    border: 1px solid #e8ded2;
    color: #8c5e35;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    white-space: nowrap;
    margin-left: 8px;
    transition: all 0.15s ease;
}
.guide-modal-btn:hover {
    background: #f5ece1;
    border-color: var(--accent-fawn);
    color: #6e4522;
}

/* Search Bar */
.search-box {
    position: relative;
    display: flex;
    align-items: center;
    background: var(--bg-surface);
    border: 2px solid var(--border-strong);
    border-radius: 10px;
    padding: 8px 14px;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
    margin-bottom: 14px;
}

.search-box:focus-within {
    border-color: var(--accent-blue);
    box-shadow: 0 0 0 3px var(--accent-blue-subtle);
}

.search-icon {
    font-size: 1rem;
    margin-right: 10px;
    color: var(--text-muted);
}

.search-input {
    flex: 1;
    border: none;
    background: transparent;
    font-size: 0.95rem;
    color: var(--text-primary);
    outline: none;
    font-family: inherit;
}

.search-input::placeholder {
    color: var(--text-dim);
}

.search-clear-btn {
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 1rem;
    cursor: pointer;
    padding: 4px 8px;
    display: none;
}
.search-clear-btn:hover {
    color: var(--text-primary);
}

/* Filter Chips Bar */
.filter-chips-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    margin-bottom: 18px;
}

.filter-group-label {
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-right: 4px;
    font-family: var(--font-mono);
}

.filter-chip {
    padding: 4px 10px;
    font-size: 0.76rem;
    font-weight: 600;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--bg-surface);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s ease;
}

.filter-chip:hover {
    background: var(--accent-blue-subtle);
    color: var(--accent-blue);
    border-color: var(--accent-blue);
}

.filter-chip.active {
    background: var(--accent-blue);
    color: #ffffff;
    border-color: var(--accent-blue);
    box-shadow: 0 2px 6px rgba(0, 123, 167, 0.25);
}

.filter-chip.chip-major {
    color: #8c5e35;
    border-color: #e8ded2;
    background: #faf6f0;
}
.filter-chip.chip-major.active {
    background: var(--accent-fawn);
    color: white;
    border-color: var(--accent-fawn);
}

.filter-chip.chip-risk {
    color: #b91c1c;
    border-color: #fca5a5;
    background: #fee2e2;
}
.filter-chip.chip-risk.active {
    background: #b91c1c;
    color: white;
}

/* Breadcrumb Navigation */
.breadcrumb-nav {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.8rem;
    font-family: var(--font-mono);
    color: var(--text-muted);
    margin-bottom: 16px;
}

.breadcrumb-btn {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--text-primary);
    cursor: pointer;
    transition: all 0.15s ease;
}
.breadcrumb-btn:hover {
    background: var(--accent-blue-subtle);
    border-color: var(--accent-blue);
    color: var(--accent-blue);
}

/* Content Area */
.content-area {
    width: 100%;
}

/* -------------------------------------------------------------
   VIEW A: SWISS MERIDIAN CARDS GRID (HUB)
   ------------------------------------------------------------- */
.section-header-bar {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    border-bottom: 2px solid var(--accent-blue);
    padding-bottom: 8px;
    margin-bottom: 16px;
}

.section-title-h2 {
    font-size: 1.1rem;
    font-weight: 900;
    letter-spacing: -0.02em;
    text-transform: uppercase;
    color: var(--text-primary);
}

.section-counter {
    font-family: var(--font-mono);
    font-weight: 800;
    font-size: 0.9rem;
    color: var(--text-muted);
}

.meridians-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 14px;
}

@media (max-width: 640px) {
    .meridians-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
}

@media (max-width: 420px) {
    .meridians-grid {
        grid-template-columns: 1fr;
    }
}

.swiss-card {
    position: relative;
    overflow: hidden;
    background-color: var(--bg-surface);
    border: 2px solid var(--border-strong);
    border-radius: 10px;
    padding: 16px;
    min-height: 155px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
    transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: var(--card-shadow);
}

.swiss-card:hover {
    border-color: var(--accent-blue);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 123, 167, 0.12);
}

.card-watermark {
    position: absolute;
    bottom: -15px;
    right: -6px;
    font-size: 6.5rem;
    font-weight: 900;
    line-height: 0.8;
    color: var(--text-primary);
    opacity: 0.045;
    user-select: none;
    pointer-events: none;
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
}

.card-top-row {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-pts-badge {
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 800;
    color: var(--text-primary);
}

.card-pts-badge span {
    font-weight: 500;
    color: var(--text-muted);
    font-size: 0.7rem;
    margin-left: 2px;
    text-transform: uppercase;
}

.card-arrow {
    color: var(--text-muted);
    font-size: 1rem;
    transition: transform 0.15s ease;
}
.swiss-card:hover .card-arrow {
    transform: translateX(4px);
    color: var(--accent-blue);
}

.card-code {
    position: relative;
    z-index: 2;
    font-family: var(--font-mono);
    font-size: 2.7rem;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -0.05em;
    color: var(--text-primary);
    margin: 8px 0;
}

.card-bottom-row {
    position: relative;
    z-index: 2;
    padding-top: 10px;
    border-top: 1px solid var(--border-subtle);
}

.card-name-line {
    display: flex;
    align-items: center;
    gap: 6px;
}

.card-element-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

.card-eng-name {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-primary);
}

.card-chinese-name {
    font-size: 0.75rem;
    color: var(--text-muted);
    margin-top: 2px;
    padding-left: 14px;
}

/* -------------------------------------------------------------
   VIEW B: MERIDIAN POINTS EXPLORER
   ------------------------------------------------------------- */
.meridian-banner {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: var(--card-shadow);
}

.banner-top-flex {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 12px;
}

.banner-title-box {
    display: flex;
    align-items: baseline;
    gap: 12px;
}

.banner-code {
    font-family: var(--font-mono);
    font-size: 2.2rem;
    font-weight: 900;
    line-height: 1;
    color: var(--text-primary);
}

.banner-chinese {
    font-size: 1.4rem;
    font-weight: 300;
    color: var(--text-dim);
}

.banner-meta-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
}

.banner-eng-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
}

.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 3px 8px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    background: var(--bg-surface-low);
    color: var(--text-secondary);
    border: 1px solid var(--border-strong);
}

.switcher-nav-btns {
    display: flex;
    gap: 6px;
}

.nav-cycle-btn {
    width: 36px;
    height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--bg-surface);
    color: var(--text-primary);
    cursor: pointer;
    font-size: 0.95rem;
    font-weight: bold;
    transition: all 0.15s ease;
}
.nav-cycle-btn:hover {
    background: var(--bg-surface-low);
    border-color: var(--text-primary);
}

.channel-points-stack {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(460px, 1fr));
    gap: 10px;
}

@media (max-width: 860px) {
    .channel-points-stack {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
}

/* Point Row Card in Channel Explorer */
.point-row-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 10px;
    padding: 10px 14px;
    cursor: pointer;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
    gap: 12px;
}

.point-row-card:hover {
    border-color: var(--accent-blue);
    transform: translateX(3px);
    box-shadow: 0 4px 14px rgba(0, 123, 167, 0.12);
}

.point-row-left {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
}

/* Thumbnail on Point Row */
.pt-thumb-box {
    width: 60px;
    height: 60px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border-strong);
    flex-shrink: 0;
    background: var(--bg-surface-low);
    display: flex;
    align-items: center;
    justify-content: center;
}

.pt-thumb-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

.point-code-block {
    font-family: var(--font-mono);
    font-weight: 900;
    font-size: 0.95rem;
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 6px;
    padding: 4px 8px;
    min-width: 58px;
    text-align: center;
    color: var(--text-primary);
    flex-shrink: 0;
}

.point-info-group {
    min-width: 0;
}

.point-name-line {
    display: flex;
    align-items: baseline;
    gap: 8px;
    flex-wrap: wrap;
}

.pt-code-pill {
    font-family: var(--font-mono);
    font-weight: 900;
    font-size: 0.88rem;
    color: var(--text-primary);
}

.pt-pinyin {
    font-weight: 800;
    font-size: 0.92rem;
    color: var(--accent-blue);
}

.pt-hanzi {
    font-size: 0.88rem;
    color: var(--text-muted);
}

.pt-star-major {
    font-size: 0.68rem;
    font-weight: 800;
    padding: 1px 6px;
    border-radius: 10px;
    background: #fef3c7;
    color: #b45309;
    border: 1px solid #fde68a;
}

.pt-category-chip {
    font-size: 0.68rem;
    font-weight: 600;
    padding: 1px 6px;
    border-radius: 4px;
    background: var(--bg-surface-low);
    color: var(--text-secondary);
}

.pt-english-line {
    font-size: 0.78rem;
    color: var(--text-secondary);
    margin-top: 2px;
}

.pt-tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: 4px;
}

.pt-tag {
    font-size: 0.68rem;
    background: var(--bg-surface-low);
    color: var(--text-muted);
    border-radius: 12px;
    padding: 1px 6px;
}

/* Safety Pills */
.safety-pill {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.72rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 20px;
    border: 1px solid transparent;
    flex-shrink: 0;
}

.safety-pill.danger {
    background: var(--signal-danger-bg);
    color: var(--signal-danger);
    border-color: var(--signal-danger-border);
}

.safety-pill.caution {
    background: var(--signal-caution-bg);
    color: var(--signal-caution);
    border-color: var(--signal-caution-border);
}

.safety-pill.safe {
    background: var(--signal-safe-bg);
    color: var(--signal-safe);
    border-color: var(--signal-safe-border);
}

/* -------------------------------------------------------------
   VIEW C: POINT DETAIL PROFILE (ST-36 STYLE)
   ------------------------------------------------------------- */
.point-detail-container {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 20px;
    box-shadow: var(--card-shadow);
}

.pdp-header-bar {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 2px solid var(--accent-blue);
    padding-bottom: 14px;
    margin-bottom: 18px;
    flex-wrap: wrap;
    gap: 12px;
}

.pdp-title-flex {
    display: flex;
    align-items: baseline;
    gap: 10px;
    flex-wrap: wrap;
}

.pdp-code-main {
    font-family: var(--font-mono);
    font-size: 2.6rem;
    font-weight: 900;
    line-height: 1;
    color: var(--accent-blue);
    display: flex;
    align-items: center;
    gap: 8px;
}

.pdp-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: inline-block;
}

.pdp-pinyin-main {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text-primary);
}

.pdp-hanzi-main {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text-muted);
}

.pdp-eng-subtitle {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-top: 4px;
}

.pdp-badges-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 10px;
}

.pdp-nav-pair {
    display: flex;
    gap: 6px;
}

.pdp-grid-split {
    display: grid;
    grid-template-columns: 360px 1fr;
    gap: 28px;
    align-items: start;
}

@media (max-width: 900px) {
    .pdp-grid-split {
        grid-template-columns: 1fr;
        gap: 18px;
    }
}

.tab-grid-2col {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 14px;
    margin-bottom: 12px;
}

@media (max-width: 768px) {
    .tab-grid-2col {
        grid-template-columns: 1fr;
        gap: 10px;
    }
}

/* Left Column: Clinical Point Photo + Depth Gauge + Safety */
.pdp-left-col {
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: sticky;
    top: 10px;
}

/* Clinical Point Location Photo Card */
.point-photo-card {
    background: var(--bg-surface-low);
    border: 2px solid var(--border-strong);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--card-shadow);
}

.point-photo-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 1 / 1;
    background: #000;
    cursor: zoom-in;
    overflow: hidden;
}

.point-photo-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.25s ease, filter 0.25s ease;
}

.point-photo-wrapper:hover .point-photo-img {
    transform: scale(1.04);
    filter: brightness(1.06);
}

.point-photo-overlay {
    position: absolute;
    bottom: 8px;
    right: 8px;
    background: rgba(15, 23, 42, 0.78);
    backdrop-filter: blur(4px);
    color: white;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 0.7rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 4px;
    pointer-events: none;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.point-photo-caption {
    padding: 8px 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--text-muted);
    border-top: 1px solid var(--border-subtle);
    background: var(--bg-surface);
}

.photo-caption-title {
    color: var(--text-primary);
}

.photo-caption-code {
    font-family: var(--font-mono);
    color: var(--accent-blue);
}

.point-photo-fallback-card {
    background: var(--bg-surface-low);
    border: 2px dashed var(--border-strong);
    border-radius: 12px;
    padding: 24px 16px;
    text-align: center;
}

.fallback-icon {
    font-size: 2rem;
    margin-bottom: 6px;
}

.fallback-title {
    font-weight: 800;
    font-size: 0.9rem;
    color: var(--text-primary);
}

.fallback-sub {
    font-size: 0.76rem;
    color: var(--text-muted);
    margin-top: 4px;
}

/* Needle Depth Gauge */
.depth-gauge-card {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 14px;
}

.gauge-header-label {
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 8px;
    font-family: var(--font-mono);
}

.gauge-track-bar {
    position: relative;
    height: 8px;
    background: var(--border-strong);
    border-radius: 4px;
    overflow: hidden;
    margin: 8px 0;
}

.gauge-fill-active {
    position: absolute;
    top: 0;
    bottom: 0;
    background: var(--accent-blue);
    border-radius: 4px;
}

.gauge-scale-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.74rem;
    font-family: var(--font-mono);
    color: var(--text-muted);
}

.gauge-target-span {
    color: var(--accent-blue);
    font-weight: 800;
}

.gauge-technique-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-top: 6px;
}

.precautions-alert-card {
    border: 2px solid;
    border-radius: 10px;
    padding: 14px;
}

.precautions-alert-card.danger {
    background: var(--signal-danger-bg);
    border-color: var(--signal-danger-border);
    color: var(--signal-danger);
}

.precautions-alert-card.caution {
    background: var(--signal-caution-bg);
    border-color: var(--signal-caution-border);
    color: var(--signal-caution);
}

.precautions-alert-card.safe {
    background: var(--signal-safe-bg);
    border-color: var(--signal-safe-border);
    color: var(--signal-safe);
}

.precaution-title {
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-mono);
}

.precaution-text {
    font-size: 0.8rem;
    line-height: 1.45;
    color: var(--text-primary);
}

.mini-meta-card {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 0.78rem;
    line-height: 1.5;
    color: var(--text-secondary);
}

/* Right Column: Tabbed Content */
.pdp-right-col {
    min-width: 0;
}

.tabs-header-bar {
    display: flex;
    border-bottom: 2px solid var(--border-strong);
    margin-bottom: 16px;
    gap: 4px;
}

.tab-nav-btn {
    padding: 8px 16px;
    font-size: 0.82rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: transparent;
    border: none;
    border-bottom: 3px solid transparent;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s ease;
    margin-bottom: -2px;
}

.tab-nav-btn:hover {
    color: var(--text-primary);
}

.tab-nav-btn.active {
    color: var(--accent-blue);
    border-bottom-color: var(--accent-blue);
}

.tab-pane-content {
    display: none;
}
.tab-pane-content.active {
    display: block;
}

.info-section-block {
    margin-bottom: 16px;
}

.section-block-label {
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: var(--font-mono);
}

.section-block-body {
    font-size: 0.88rem;
    line-height: 1.6;
    color: var(--text-primary);
}

.palpation-step-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 8px;
    font-size: 0.86rem;
    line-height: 1.5;
}

.step-num-bubble {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--text-primary);
    color: var(--bg-surface);
    font-size: 0.72rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
}

.action-check-item {
    display: flex;
    gap: 8px;
    align-items: baseline;
    font-size: 0.86rem;
    line-height: 1.5;
    margin-bottom: 6px;
}

.action-check-icon {
    color: var(--accent-blue);
    font-weight: 900;
}

.combo-item-card {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 10px 12px;
    margin-bottom: 8px;
}

.combo-pts-title {
    font-family: var(--font-mono);
    font-weight: 800;
    font-size: 0.88rem;
    color: var(--accent-blue);
}

.combo-ind-desc {
    font-size: 0.82rem;
    color: var(--text-secondary);
    margin-top: 2px;
}

/* Adjacent points bottom navigation */
.adjacent-bottom-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 24px;
    padding-top: 16px;
    border-top: 1px solid var(--border-subtle);
}

.adj-btn {
    display: flex;
    flex-direction: column;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--bg-surface-low);
    color: var(--text-primary);
    cursor: pointer;
    transition: all 0.15s ease;
    text-align: left;
}
.adj-btn:hover {
    border-color: var(--text-primary);
    background: var(--bg-surface);
}

.adj-btn.next {
    text-align: right;
}

.adj-sub {
    font-size: 0.7rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
}

.adj-code {
    font-size: 0.95rem;
    font-weight: 800;
    color: var(--accent-blue);
    margin-top: 2px;
}

/* -------------------------------------------------------------
   VIEW D: SEARCH RESULTS
   ------------------------------------------------------------- */
.search-results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
    gap: 12px;
}

@media (max-width: 860px) {
    .search-results-grid {
        grid-template-columns: 1fr;
        gap: 8px;
    }
}

.search-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 12px 14px;
    cursor: pointer;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
    display: flex;
    gap: 12px;
    align-items: center;
}

.search-card:hover {
    border-color: var(--text-primary);
    transform: translateY(-2px);
    box-shadow: var(--card-hover-shadow);
}

.search-card-main {
    flex: 1;
    min-width: 0;
}

.search-card-top {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 4px;
}

.search-card-code {
    font-family: var(--font-mono);
    font-weight: 900;
    font-size: 1.05rem;
    color: var(--text-primary);
}

.search-card-names {
    font-weight: 700;
    font-size: 0.88rem;
    color: var(--text-primary);
}

.search-card-eng {
    font-size: 0.76rem;
    color: var(--text-muted);
}

.search-card-loc {
    font-size: 0.74rem;
    color: var(--text-secondary);
    margin-top: 4px;
    line-height: 1.35;
}

/* -------------------------------------------------------------
   PHOTO LIGHTBOX MODAL
   ------------------------------------------------------------- */
.photo-lightbox-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(8px);
    z-index: 99999;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
    animation: fadeIn 0.15s ease;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.lightbox-dialog {
    background: var(--bg-surface);
    border: 2px solid var(--border-strong);
    border-radius: 14px;
    max-width: 640px;
    width: 100%;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    display: flex;
    flex-direction: column;
}

.lightbox-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border-subtle);
    background: var(--bg-surface-low);
}

.lightbox-title {
    font-family: var(--font-mono);
    font-weight: 800;
    font-size: 0.95rem;
    color: var(--text-primary);
}

.lightbox-close-btn {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    color: var(--text-primary);
    width: 32px;
    height: 32px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.15s ease;
}
.lightbox-close-btn:hover {
    background: var(--signal-danger-bg);
    color: var(--signal-danger);
    border-color: var(--signal-danger);
}

.lightbox-img-wrap {
    width: 100%;
    aspect-ratio: 1 / 1;
    background: #000;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.lightbox-img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
}

.lightbox-footer {
    padding: 10px 16px;
    font-size: 0.78rem;
    color: var(--text-muted);
    border-top: 1px solid var(--border-subtle);
    background: var(--bg-surface);
    display: flex;
    justify-content: space-between;
}

</style>
</head>
<body>

<div class="atlas-wrapper">
    <!-- Search Input Bar with Guide Modal trigger -->
    <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="globalSearchInput" class="search-input" placeholder="Search by name, pinyin, or condition (e.g. ST36, Zusanli, headache, cough)..." />
        <button id="searchClearBtn" class="search-clear-btn" onclick="clearSearch()">✕</button>
        <button onclick="openGuideModal()" class="guide-modal-btn" title="View Atlas Guide & Clinical Tips">
            ℹ️ Guide & Tips
        </button>
    </div>

    <!-- Filter Chips Row -->
    <div class="filter-chips-row" id="filterChipsRow">
        <span class="filter-group-label">Region:</span>
        <button class="filter-chip active" onclick="setRegion('ALL', this)">All</button>
        <button class="filter-chip" onclick="setRegion('Head', this)">Head</button>
        <button class="filter-chip" onclick="setRegion('Neck', this)">Neck</button>
        <button class="filter-chip" onclick="setRegion('Chest', this)">Chest</button>
        <button class="filter-chip" onclick="setRegion('Abdomen', this)">Abdomen</button>
        <button class="filter-chip" onclick="setRegion('Back', this)">Back</button>
        <button class="filter-chip" onclick="setRegion('Upper Limb', this)">Upper Limb</button>
        <button class="filter-chip" onclick="setRegion('Lower Limb', this)">Lower Limb</button>
        
        <span class="filter-group-label" style="margin-left: 10px;">Special:</span>
        <button class="filter-chip chip-major" onclick="setSpecial('major', this)">★ Major</button>
        <button class="filter-chip chip-risk" onclick="setSpecial('risk', this)">⚠ Risk</button>
    </div>

    <!-- Main Dynamic Content Container -->
    <main class="content-area" id="mainContentArea">
        <!-- Rendered dynamically by JavaScript -->
    </main>
</div>

<!-- Photo Lightbox Modal -->
<div id="photoLightboxModal" class="photo-lightbox-modal" onclick="closePhotoModal(event)">
    <div class="lightbox-dialog" onclick="event.stopPropagation()">
        <div class="lightbox-header">
            <span id="lightboxTitle" class="lightbox-title">Point Landmark Photo</span>
            <button class="lightbox-close-btn" onclick="closePhotoModal()" title="Close (Esc)">✕</button>
        </div>
        <div class="lightbox-img-wrap">
            <img id="lightboxImg" class="lightbox-img" src="" alt="Enlarged point anatomy photograph" />
        </div>
        <div class="lightbox-footer">
            <span>📍 Clinical Anatomical Landmark & Needling Verification</span>
            <span style="font-family:var(--font-mono);">Press ESC to close</span>
        </div>
    </div>
</div>

<!-- Atlas Guide & Clinical Tips Modal -->
<div id="atlasGuideModal" class="photo-lightbox-modal" onclick="closeGuideModal(event)">
    <div class="lightbox-dialog" style="max-width: 700px; max-height: 85vh; overflow-y: auto;" onclick="event.stopPropagation()">
        <div class="lightbox-header">
            <span class="lightbox-title">ℹ️ Acupuncture Atlas Explorer Guide & Clinical Tips</span>
            <button class="lightbox-close-btn" onclick="closeGuideModal()" title="Close (Esc)">✕</button>
        </div>
        <div style="padding: 24px; font-size: 0.88rem; line-height: 1.65; color: var(--text-primary); display: flex; flex-direction: column; gap: 16px;">
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span style="font-size: 1.3rem;">🧭</span>
                <div>
                    <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 2px;">Primary Meridians Hub</div>
                    <div style="color: var(--text-secondary);">Explore all 14 classical meridians + Extra Points with Swiss-style cards displaying point counts, Five-Element colors, and giant Chinese character watermarks.</div>
                </div>
            </div>
            
            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span style="font-size: 1.3rem;">👤</span>
                <div>
                    <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 2px;">Interactive Anatomical Body Map</div>
                    <div style="color: var(--text-secondary);">Toggle between <strong>Anterior</strong> and <strong>Posterior</strong> views. Click any anatomical zone (<em>Head, Neck, Chest, Abdomen, Back, Upper Limb, Lower Limb</em>) to immediately filter meridians and points situated in that region.</div>
                </div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span style="font-size: 1.3rem;">🔍</span>
                <div>
                    <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 2px;">Multi-Script Search</div>
                    <div style="color: var(--text-secondary);">Search instantly by alphanumeric code (<code style="background:var(--bg-surface-low); padding:2px 6px; border-radius:4px; font-family:var(--font-mono);">ST36</code>, <code style="background:var(--bg-surface-low); padding:2px 6px; border-radius:4px; font-family:var(--font-mono);">LI4</code>, <code style="background:var(--bg-surface-low); padding:2px 6px; border-radius:4px; font-family:var(--font-mono);">BL23</code>), Pinyin (<em>Zusanli</em>, <em>Hegu</em>), Chinese Hanzi (<em>足三里</em>, <em>合谷</em>), English translation, or clinical indication (<em>headache</em>, <em>asthma</em>, <em>sciatica</em>, <em>gastritis</em>).</div>
                </div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span style="font-size: 1.3rem;">⚡</span>
                <div>
                    <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 2px;">Meridian Point Explorer</div>
                    <div style="color: var(--text-secondary);">Click any channel card to drill down into its complete sequence of points, tagged with Five-Element classifications, clinical indication pills, and safety warning badges.</div>
                </div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
                <span style="font-size: 1.3rem;">📍</span>
                <div>
                    <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 2px;">Deep Clinical Point Profiles & Real Anatomical Photos</div>
                    <div style="color: var(--text-secondary);">
                        Click any point to open its comprehensive evidence-based clinical dossier:
                        <ul style="margin: 6px 0 0 18px; padding: 0;">
                            <li><strong>Needle Depth Gauge:</strong> Visual scale with exact safe depth ranges (e.g. <em>1.0–1.5 cun</em>, perpendicular).</li>
                            <li><strong>Clinical Safety Precautions:</strong> Clear alerts for pneumothorax, arterial avoidance, or pregnancy contraindications.</li>
                            <li><strong>Three Dedicated Tabs:</strong> Classical location & practical palpation steps, TCM energetic actions, and evidence-based indications with classical combinations.</li>
                            <li><strong>Photo Landmark Verification:</strong> Click any photo thumbnail to view enlarged anatomical photographs confirming needle placement.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="lightbox-footer" style="padding: 12px 20px; background: var(--bg-surface-low); border-top: 1px solid var(--border-subtle); display: flex; justify-content: flex-end;">
            <button onclick="closeGuideModal()" style="background: var(--accent-blue); color: #ffffff; border: none; padding: 6px 16px; border-radius: 6px; font-weight: 600; cursor: pointer;">Got It</button>
        </div>
    </div>
</div>

<!-- Embedded Dataset -->
<script>
const DATA = __DATA_PAYLOAD__;

// Application State
let appState = {
    view: 'hub',            // 'hub' | 'meridian' | 'point' | 'search'
    activeMeridianId: null, // e.g. 'LU'
    activePointCode: null,  // e.g. 'LU-1'
    searchQuery: '',
    currentRegion: 'ALL',
    currentSpecial: null,   // null | 'major' | 'risk'
    activeTab: 'loc'        // 'loc' | 'tcm' | 'west'
};

// DOM References
const searchInput = document.getElementById('globalSearchInput');
const searchClearBtn = document.getElementById('searchClearBtn');
const filterChipsRow = document.getElementById('filterChipsRow');
const mainContentArea = document.getElementById('mainContentArea');
const photoLightboxModal = document.getElementById('photoLightboxModal');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxTitle = document.getElementById('lightboxTitle');

// ------------------------------------------------------------------
// DYNAMIC HEIGHT SYNCHRONIZATION & SEAMLESS STREAMLIT EMBEDDING
// ------------------------------------------------------------------
function syncHeight() {
    requestAnimationFrame(() => {
        const wrapper = document.querySelector('.atlas-wrapper');
        if (!wrapper) return;
        
        // Compute exact content height from the wrapper's bounding box
        const rectHeight = Math.ceil(wrapper.getBoundingClientRect().height);
        const targetHeight = Math.max(700, rectHeight + 36);

        // 1. Direct same-origin iframe styling (allows dynamic collapsing)
        try {
            if (window.frameElement) {
                window.frameElement.style.height = targetHeight + 'px';
                window.frameElement.style.overflow = 'hidden';
                window.frameElement.height = targetHeight;
            }
        } catch (e) {}

        // 2. Send Streamlit setFrameHeight message via postMessage
        try {
            window.parent.postMessage({
                isStreamlitMessage: true,
                type: 'streamlit:setFrameHeight',
                height: targetHeight
            }, '*');
        } catch (e) {}
    });
}

// Pre-collapse iframe height on view transitions so parent container releases old maximum height
function prepareViewTransition() {
    try {
        if (window.frameElement) {
            window.frameElement.style.height = '850px';
        }
    } catch(e) {}
    scrollToAtlasTop();
}

// Cleanup on unload to prevent height leakage
window.addEventListener('beforeunload', () => {
    try {
        if (window.frameElement) {
            window.frameElement.style.height = '0px';
        }
    } catch (e) {}
});

// Announce component ready to Streamlit
try {
    window.parent.postMessage({
        isStreamlitMessage: true,
        type: 'streamlit:componentReady',
        apiVersion: 1
    }, '*');
} catch (e) {}

// Robust smooth scroll to top of Atlas in the main webpage
function scrollToAtlasTop() {
    // 1. Native scrollIntoView on the iframe element itself (handled by browser window)
    try {
        if (window.frameElement && typeof window.frameElement.scrollIntoView === 'function') {
            window.frameElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    } catch (e) {}

    // 2. Parent Streamlit viewport containers
    try {
        if (window.parent && window.parent !== window && window.parent.document) {
            const pDoc = window.parent.document;
            const scrollContainers = [
                pDoc.querySelector('[data-testid="stAppViewContainer"]'),
                pDoc.querySelector('[data-testid="stMain"]'),
                pDoc.querySelector('section.main'),
                pDoc.querySelector('.main'),
                pDoc.documentElement,
                pDoc.body
            ];
            scrollContainers.forEach(container => {
                if (container) {
                    try {
                        if (typeof container.scrollTo === 'function') {
                            container.scrollTo({ top: 0, behavior: 'smooth' });
                        }
                        container.scrollTop = 0;
                    } catch(err) {}
                }
            });
            try {
                window.parent.scrollTo({ top: 0, behavior: 'smooth' });
            } catch(err) {}
        }
    } catch(e) {}

    // 3. Fallback inner window scroll
    try {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (e) {}
}

// Observe DOM mutations / resizes
if (window.ResizeObserver) {
    const resizeObserver = new ResizeObserver(() => {
        syncHeight();
    });
    const wrap = document.querySelector('.atlas-wrapper');
    if (wrap) resizeObserver.observe(wrap);
}

window.addEventListener('resize', syncHeight);
window.addEventListener('load', () => {
    syncHeight();
    setTimeout(syncHeight, 150);
    setTimeout(syncHeight, 400);
});

// Theme Toggle
function toggleTheme() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        document.getElementById('themeBtn').innerText = '🌙 Dark Mode';
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('themeBtn').innerText = '☀️ Light Mode';
    }
}

// Photo Lightbox Handlers
window.openPhotoModal = function(imgSrc, title) {
    if (!imgSrc) return;
    lightboxImg.src = imgSrc;
    lightboxTitle.innerText = title || 'Point Landmark Photo';
    photoLightboxModal.style.display = 'flex';
};

window.closePhotoModal = function(e) {
    photoLightboxModal.style.display = 'none';
    lightboxImg.src = '';
};

// Guide Modal Handlers
window.openGuideModal = function() {
    const modal = document.getElementById('atlasGuideModal');
    if (modal) modal.style.display = 'flex';
};

window.closeGuideModal = function(e) {
    const modal = document.getElementById('atlasGuideModal');
    if (modal) modal.style.display = 'none';
};

// Keyboard escape to close modals
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (photoLightboxModal.style.display === 'flex') {
            closePhotoModal();
        }
        const guideModal = document.getElementById('atlasGuideModal');
        if (guideModal && guideModal.style.display === 'flex') {
            closeGuideModal();
        }
    }
});

// Search Input Listener
searchInput.addEventListener('input', (e) => {
    const q = e.target.value.trim().toLowerCase();
    appState.searchQuery = q;
    if (q.length > 0) {
        searchClearBtn.style.display = 'block';
        appState.view = 'search';
    } else {
        searchClearBtn.style.display = 'none';
        if (appState.activePointCode) {
            appState.view = 'point';
        } else if (appState.activeMeridianId) {
            appState.view = 'meridian';
        } else {
            appState.view = 'hub';
        }
    }
    render();
});

function clearSearch() {
    searchInput.value = '';
    searchClearBtn.style.display = 'none';
    appState.searchQuery = '';
    if (appState.activePointCode) {
        appState.view = 'point';
    } else if (appState.activeMeridianId) {
        appState.view = 'meridian';
    } else {
        appState.view = 'hub';
    }
    render();
}

// Filter Actions
function setRegion(regionName, btn) {
    appState.currentRegion = regionName;
    document.querySelectorAll('#filterChipsRow button').forEach(b => {
        if (!b.classList.contains('chip-major') && !b.classList.contains('chip-risk')) {
            b.classList.remove('active');
        }
    });
    btn.classList.add('active');
    render();
}

function setSpecial(specType, btn) {
    if (appState.currentSpecial === specType) {
        appState.currentSpecial = null;
        btn.classList.remove('active');
    } else {
        appState.currentSpecial = specType;
        document.querySelectorAll('.chip-major, .chip-risk').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    render();
}

// Navigation Actions
window.openMeridian = function(mId) {
    appState.view = 'meridian';
    appState.activeMeridianId = mId;
    appState.activePointCode = null;
    clearSearch();
    prepareViewTransition();
    render();
    setTimeout(scrollToAtlasTop, 30);
    setTimeout(scrollToAtlasTop, 120);
};

window.closeMeridian = function() {
    appState.view = 'hub';
    appState.activeMeridianId = null;
    appState.activePointCode = null;
    clearSearch();
    prepareViewTransition();
    render();
    setTimeout(scrollToAtlasTop, 30);
    setTimeout(scrollToAtlasTop, 120);
};

window.openPoint = function(ptCode) {
    appState.view = 'point';
    appState.activePointCode = ptCode;
    const pt = DATA.points[ptCode];
    if (pt) {
        appState.activeMeridianId = pt.channelId;
    }
    clearSearch();
    prepareViewTransition();
    render();
    setTimeout(scrollToAtlasTop, 30);
    setTimeout(scrollToAtlasTop, 120);
};

window.backToMeridian = function() {
    if (appState.activeMeridianId) {
        appState.view = 'meridian';
        appState.activePointCode = null;
    } else {
        appState.view = 'hub';
    }
    prepareViewTransition();
    render();
    setTimeout(scrollToAtlasTop, 30);
    setTimeout(scrollToAtlasTop, 120);
};

window.switchTab = function(tabId) {
    appState.activeTab = tabId;
    document.querySelectorAll('.tab-nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane-content').forEach(p => p.classList.remove('active'));
    
    const activeBtn = document.getElementById('tab-btn-' + tabId);
    const activePane = document.getElementById('tab-pane-' + tabId);
    if (activeBtn) activeBtn.classList.add('active');
    if (activePane) activePane.classList.add('active');
    syncHeight();
    setTimeout(syncHeight, 80);
};

// ------------------------------------------------------------------
// RENDER DISPATCHER
// ------------------------------------------------------------------
function render() {
    if (appState.view === 'search' && appState.searchQuery.length > 0) {
        renderSearchResults();
    } else if (appState.view === 'point' && appState.activePointCode) {
        renderPointDetail(appState.activePointCode);
    } else if (appState.view === 'meridian' && appState.activeMeridianId) {
        renderMeridianPoints(appState.activeMeridianId);
    } else {
        renderHubMeridians();
    }
    syncHeight();
    setTimeout(syncHeight, 100);
    setTimeout(syncHeight, 350);
}

// ------------------------------------------------------------------
// VIEW A: HUB MERIDIANS GRID
// ------------------------------------------------------------------
function renderHubMeridians() {
    const filteredMeridians = DATA.meridians.filter(m => {
        if (appState.currentRegion === 'ALL') return true;
        return Object.values(DATA.points).some(p => p.channelId === m.id && p.region.toLowerCase().includes(appState.currentRegion.toLowerCase()));
    });

    let html = `
    <div class="section-header-bar">
        <h2 class="section-title-h2">Primary Meridians</h2>
        <span class="section-counter">${filteredMeridians.length} Channels</span>
    </div>
    <div class="meridians-grid">`;

    filteredMeridians.forEach(m => {
        html += `
        <div class="swiss-card" onclick="openMeridian('${m.id}')" title="Explore ${m.name} Meridian (${m.totalPoints} points)">
            <div class="card-watermark">${m.watermark}</div>
            <div class="card-top-row">
                <div class="card-pts-badge">${m.totalPoints}<span>pts</span></div>
                <div class="card-arrow">→</div>
            </div>
            <div class="card-code">${m.id}</div>
            <div class="card-bottom-row">
                <div class="card-name-line">
                    <span class="card-element-dot" style="background-color: ${m.color};"></span>
                    <span class="card-eng-name">${m.name}</span>
                </div>
                <div class="card-chinese-name">${m.chinese}</div>
            </div>
        </div>`;
    });

    html += `</div>`;
    mainContentArea.innerHTML = html;
}

// ------------------------------------------------------------------
// VIEW B: MERIDIAN POINTS EXPLORER
// ------------------------------------------------------------------
function renderMeridianPoints(mId) {
    const m = DATA.meridians.find(item => item.id === mId) || DATA.meridians[0];
    const pts = Object.values(DATA.points).filter(p => p.channelId === mId);

    // Apply Region / Special Filters if any
    const displayPts = pts.filter(p => {
        if (appState.currentRegion !== 'ALL' && !p.region.toLowerCase().includes(appState.currentRegion.toLowerCase())) {
            return false;
        }
        if (appState.currentSpecial === 'major' && p.tier !== 1) return false;
        if (appState.currentSpecial === 'risk' && p.safetyLevel !== 'danger') return false;
        return true;
    });

    // Prev / Next Meridians
    const mIdx = DATA.meridians.findIndex(item => item.id === mId);
    const prevM = DATA.meridians[(mIdx - 1 + DATA.meridians.length) % DATA.meridians.length];
    const nextM = DATA.meridians[(mIdx + 1) % DATA.meridians.length];

    let html = `
    <!-- Breadcrumb -->
    <nav class="breadcrumb-nav">
        <button class="breadcrumb-btn" onclick="closeMeridian()">← Atlas Hub</button>
        <span>/</span>
        <span style="font-weight: 700; color: var(--text-primary);">${m.name} (${m.id})</span>
    </nav>

    <!-- Meridian Hero Banner -->
    <div class="meridian-banner">
        <div class="banner-top-flex">
            <div>
                <div class="banner-title-box">
                    <span class="banner-code">${m.id}</span>
                    <span class="banner-chinese">${m.chinese}</span>
                </div>
                <div class="banner-meta-row">
                    <span class="banner-eng-name">${m.name}</span>
                    <span class="badge-pill"><span class="card-element-dot" style="background:${m.color};"></span>${m.element} (${m.elementChinese})</span>
                    <span class="badge-pill">${m.polarity}</span>
                    <span class="badge-pill">${m.totalPoints} Points</span>
                    <span class="badge-pill">⏰ ${m.organTime}</span>
                </div>
            </div>
            <div class="switcher-nav-btns">
                <button class="nav-cycle-btn" onclick="openMeridian('${prevM.id}')" title="Previous: ${prevM.name}">←</button>
                <button class="nav-cycle-btn" onclick="openMeridian('${nextM.id}')" title="Next: ${nextM.name}">→</button>
            </div>
        </div>
        <p style="font-size: 0.84rem; color: var(--text-secondary); margin-top: 10px; line-height: 1.5;">${m.overview || 'Classical meridian pathway circulation according to WHO acupuncture standard.'}</p>
    </div>

    <!-- Channel Section Header -->
    <div class="section-header-bar">
        <h2 class="section-title-h2">${m.name} Points</h2>
        <span class="section-counter">${displayPts.length} of ${pts.length}</span>
    </div>

    <div class="channel-points-stack">`;

    if (displayPts.length === 0) {
        html += `<div style="text-align:center;padding:40px;color:var(--text-muted);background:var(--bg-surface);border-radius:10px;">No points match the selected filter in this channel.</div>`;
    } else {
        displayPts.forEach(pt => {
            const safetyClass = pt.safetyLevel === 'danger' ? 'danger' : (pt.safetyLevel === 'caution' ? 'caution' : 'safe');
            const safetyText = pt.safetyLevel === 'danger' ? '🔴 Danger' : (pt.safetyLevel === 'caution' ? '🟡 Caution' : '🟢 Safe');
            
            html += `
            <div class="point-row-card" onclick="openPoint('${pt.code}')">
                <div class="point-row-left">
                    ${pt.hasImage ? `
                    <div class="pt-thumb-box">
                        <img class="pt-thumb-img" src="${pt.image}" alt="${pt.code}" loading="lazy" onload="syncHeight()" onerror="this.onerror=null; this.src='${pt.remoteImage}'; this.onerror=function(){this.parentElement.style.display='none';}; syncHeight();" />
                    </div>
                    ` : `
                    <div class="point-code-block">${pt.code}</div>
                    `}
                    <div class="point-info-group">
                        <div class="point-name-line">
                            <span class="pt-code-pill">${pt.code}</span>
                            <span class="pt-pinyin">${pt.pinyin}</span>
                            <span class="pt-hanzi">${pt.hanzi}</span>
                            ${pt.tier === 1 ? '<span class="pt-star-major">★ Major</span>' : ''}
                            ${pt.category ? `<span class="pt-category-chip">${pt.category}</span>` : ''}
                        </div>
                        <div class="pt-english-line">${pt.english}</div>
                        <div class="pt-tags-row">
                            ${pt.tags.slice(0, 4).map(t => `<span class="pt-tag">#${t}</span>`).join('')}
                        </div>
                    </div>
                </div>
                <div class="safety-pill ${safetyClass}">${safetyText}</div>
            </div>`;
        });
    }

    html += `</div>`;
    mainContentArea.innerHTML = html;
}

// ------------------------------------------------------------------
// VIEW C: POINT DETAIL PROFILE (ST-36 STYLE)
// ------------------------------------------------------------------
function renderPointDetail(ptCode) {
    const pt = DATA.points[ptCode];
    if (!pt) {
        renderHubMeridians();
        return;
    }

    const m = DATA.meridians.find(item => item.id === pt.channelId) || { color: '#0284c7', name: 'Channel', chinese: '', element: '', elementChinese: '', organTime: '' };
    const ptKeys = Object.keys(DATA.points).filter(k => DATA.points[k].channelId === pt.channelId);
    const currIdx = ptKeys.indexOf(ptCode);
    const prevCode = pt.prevPoint || (currIdx > 0 ? ptKeys[currIdx - 1] : ptKeys[ptKeys.length - 1]);
    const nextCode = pt.nextPoint || (currIdx < ptKeys.length - 1 ? ptKeys[currIdx + 1] : ptKeys[0]);

    // Needle depth math for gauge bar
    const maxLimit = pt.depthMaxLimit || 3.0;
    const fillLeft = Math.max(0, Math.min(100, (pt.depthMin / maxLimit) * 100));
    const fillWidth = Math.max(10, Math.min(100 - fillLeft, ((pt.depthMax - pt.depthMin) / maxLimit) * 100));

    const safetyClass = pt.safetyLevel === 'danger' ? 'danger' : (pt.safetyLevel === 'caution' ? 'caution' : 'safe');
    const safetyText = pt.safetyLevel === 'danger' ? '🔴 Danger' : (pt.safetyLevel === 'caution' ? '🟡 Caution' : '🟢 Safe');

    let html = `
    <!-- Breadcrumbs -->
    <nav class="breadcrumb-nav">
        <button class="breadcrumb-btn" onclick="closeMeridian()">← Atlas Hub</button>
        <span>/</span>
        <button class="breadcrumb-btn" onclick="backToMeridian()">← ${m.name} (${pt.channelId})</button>
        <span>/</span>
        <span style="font-weight: 700; color: var(--text-primary);">${pt.code}</span>
    </nav>

    <div class="point-detail-container">
        <!-- Header Bar -->
        <div class="pdp-header-bar">
            <div>
                <div class="pdp-title-flex">
                    <div class="pdp-code-main">
                        <span class="pdp-dot" style="background-color: ${m.color};"></span>
                        ${pt.code}
                    </div>
                    <span class="pdp-pinyin-main">${pt.pinyin}</span>
                    <span class="pdp-hanzi-main">${pt.hanzi}</span>
                </div>
                <div class="pdp-eng-subtitle">${pt.english}</div>
                <div class="pdp-badges-row">
                    ${pt.tier === 1 ? '<span class="filter-chip chip-major active">★ Major Point</span>' : ''}
                    ${pt.category ? `<span class="badge-pill">${pt.category}</span>` : ''}
                    <span class="badge-pill">${pt.region}</span>
                    <span class="safety-pill ${safetyClass}">${safetyText}</span>
                </div>
            </div>
            <div class="pdp-nav-pair">
                <button class="nav-cycle-btn" onclick="openPoint('${prevCode}')" title="Previous: ${prevCode}">← ${prevCode}</button>
                <button class="nav-cycle-btn" onclick="openPoint('${nextCode}')" title="Next: ${nextCode}">${nextCode} →</button>
            </div>
        </div>

        <!-- 2-Column Split Layout -->
        <div class="pdp-grid-split">
            <!-- Left Column: Point Photo + Needle Depth Gauge + Safety Alert -->
            <div class="pdp-left-col">
                <!-- Clinical Point Location Photography -->
                ${pt.hasImage ? `
                <div class="point-photo-card">
                    <div class="point-photo-wrapper" onclick="openPhotoModal('${pt.image}', '${pt.code} ${pt.pinyin} (${pt.hanzi}) — Anatomical Landmark')">
                        <img class="point-photo-img" src="${pt.image}" alt="${pt.code} ${pt.pinyin} location photo" loading="eager" onload="syncHeight()" onerror="this.onerror=null; this.src='${pt.remoteImage}'; this.onerror=function(){this.parentElement.parentElement.style.display='none';}; syncHeight();" />
                        <div class="point-photo-overlay">
                            <span>🔍 Click to zoom</span>
                        </div>
                    </div>
                    <div class="point-photo-caption">
                        <span class="photo-caption-title">📍 Anatomical Landmark</span>
                        <span class="photo-caption-code">${pt.code}</span>
                    </div>
                </div>
                ` : `
                <div class="point-photo-fallback-card">
                    <div class="fallback-icon">📍</div>
                    <div class="fallback-title">${pt.code} · ${pt.region}</div>
                    <div class="fallback-sub">Landmark palpation steps on right panel</div>
                </div>
                `}

                <!-- Visual Needle Depth Gauge -->
                <div class="depth-gauge-card">
                    <div class="gauge-header-label">Needle Insertion Depth</div>
                    <div class="gauge-track-bar">
                        <div class="gauge-fill-active" style="left: ${fillLeft}%; width: ${fillWidth}%;"></div>
                    </div>
                    <div class="gauge-scale-labels">
                        <span>0</span>
                        <span class="gauge-target-span">${pt.depthMin}–${pt.depthMax} cun</span>
                        <span>${maxLimit} cun</span>
                    </div>
                    <div class="gauge-technique-label">💉 ${pt.technique}</div>
                </div>

                <!-- Precautions Warning Box -->
                <div class="precautions-alert-card ${safetyClass}">
                    <div class="precaution-title">
                        <span>⚠️ Clinical Precautions</span>
                    </div>
                    <div class="precaution-text">${pt.safetyWarning}</div>
                </div>

                <!-- Quick Metadata Overview -->
                <div class="mini-meta-card">
                    <div><strong>Meridian:</strong> ${m.name} (${m.chinese})</div>
                    <div><strong>Element:</strong> ${m.element} (${m.elementChinese})</div>
                    <div><strong>Circulation:</strong> ⏰ ${m.organTime}</div>
                </div>
            </div>

            <!-- Right Column: Clinical Content Tabs -->
            <div class="pdp-right-col">
                <div class="tabs-header-bar">
                    <button class="tab-nav-btn ${appState.activeTab === 'loc' ? 'active' : ''}" id="tab-btn-loc" onclick="switchTab('loc')">📍 Location</button>
                    <button class="tab-nav-btn ${appState.activeTab === 'tcm' ? 'active' : ''}" id="tab-btn-tcm" onclick="switchTab('tcm')">⚡ TCM Energetics</button>
                    <button class="tab-nav-btn ${appState.activeTab === 'west' ? 'active' : ''}" id="tab-btn-west" onclick="switchTab('west')">🩺 Western & Clinical</button>
                </div>

                <!-- Tab 1: Location -->
                <div class="tab-pane-content ${appState.activeTab === 'loc' ? 'active' : ''}" id="tab-pane-loc">
                    <div class="info-section-block">
                        <div class="section-block-label">📍 Location (WHO Classical Standard)</div>
                        <div class="section-block-body">${pt.locationClassical}</div>
                    </div>

                    <div class="tab-grid-2col">
                        <div class="info-section-block">
                            <div class="section-block-label">🧭 Practical Palpation Guide</div>
                            <div>
                                ${pt.howToFind.map((s, idx) => `
                                <div class="palpation-step-row">
                                    <div class="step-num-bubble">${idx + 1}</div>
                                    <div>${s.replace(/^\d+\.\s*/, '')}</div>
                                </div>`).join('')}
                            </div>
                        </div>

                        <div>
                            <div class="info-section-block">
                                <div class="section-block-label">🔬 Anatomy & Innervation</div>
                                <div class="section-block-body">${pt.anatomy}</div>
                            </div>

                            <div class="info-section-block">
                                <div class="section-block-label">📜 Etymology & Name Meaning</div>
                                <div class="section-block-body">${pt.etymology}</div>
                            </div>
                        </div>
                    </div>

                    ${pt.clinicalNotes ? `
                    <div class="info-section-block">
                        <div class="section-block-label">💡 Clinical Pearls & Classical Notes</div>
                        <div class="section-block-body" style="font-size:0.84rem;color:var(--text-secondary);">${pt.clinicalNotes}</div>
                    </div>` : ''}
                </div>

                <!-- Tab 2: TCM Energetics -->
                <div class="tab-pane-content ${appState.activeTab === 'tcm' ? 'active' : ''}" id="tab-pane-tcm">
                    <div class="tab-grid-2col">
                        <div class="info-section-block">
                            <div class="section-block-label">⚡ TCM Actions & Functions</div>
                            <div>
                                ${pt.actions.map(a => `
                                <div class="action-check-item">
                                    <span class="action-check-icon">✓</span>
                                    <div>${a}</div>
                                </div>`).join('')}
                            </div>
                        </div>

                        <div class="info-section-block">
                            <div class="section-block-label">🏷️ Channel & Five-Element Category</div>
                            <div class="section-block-body">
                                <strong>Channel:</strong> ${m.name} (${m.chinese})<br>
                                <strong>Element:</strong> ${m.element} (${m.elementChinese})<br>
                                <strong>Classification:</strong> ${pt.category || 'Primary Channel Point'}
                            </div>
                        </div>
                    </div>

                    ${pt.tcmIndications && pt.tcmIndications.length > 0 ? `
                    <div class="info-section-block">
                        <div class="section-block-label">📜 Classical Indications</div>
                        <div class="pt-tags-row" style="margin-top:6px;">
                            ${pt.tcmIndications.slice(0, 15).map(t => `<span class="pt-tag" style="padding:3px 8px;font-size:0.75rem;">${t}</span>`).join('')}
                        </div>
                    </div>` : ''}
                </div>

                <!-- Tab 3: Western & Clinical -->
                <div class="tab-pane-content ${appState.activeTab === 'west' ? 'active' : ''}" id="tab-pane-west">
                    <div class="tab-grid-2col">
                        <div>
                            <div class="info-section-block">
                                <div class="section-block-label">🩺 Evidence-Based Indications</div>
                                <div class="pt-tags-row" style="margin-top:6px;">
                                    ${pt.tags.map(t => `<span class="pt-tag" style="padding:4px 8px;font-size:0.78rem;">#${t}</span>`).join('')}
                                </div>
                            </div>

                            ${pt.westernIndications && pt.westernIndications.length > 0 ? `
                            <div class="info-section-block">
                                <div class="section-block-label">🔬 Clinical Biomedical Associations</div>
                                <div class="section-block-body">
                                    ${pt.westernIndications.join(', ')}
                                </div>
                            </div>` : ''}
                        </div>

                        <div class="info-section-block">
                            <div class="section-block-label">🤝 Classical Point Combinations</div>
                            <div>
                                ${pt.combinations.map(c => `
                                <div class="combo-item-card">
                                    <div class="combo-pts-title">${c.points}</div>
                                    <div class="combo-ind-desc">${c.indication}</div>
                                </div>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom Adjacent Switcher -->
        <div class="adjacent-bottom-grid">
            <button class="adj-btn" onclick="openPoint('${prevCode}')">
                <span class="adj-sub">← Previous Point</span>
                <span class="adj-code">${prevCode}</span>
            </button>
            <button class="adj-btn next" onclick="openPoint('${nextCode}')">
                <span class="adj-sub">Next Point →</span>
                <span class="adj-code">${nextCode}</span>
            </button>
        </div>
    </div>`;

    mainContentArea.innerHTML = html;
}

// ------------------------------------------------------------------
// VIEW D: GLOBAL MULTI-SCRIPT SEARCH RESULTS
// ------------------------------------------------------------------
function renderSearchResults() {
    const query = appState.searchQuery.toLowerCase();
    const matched = Object.values(DATA.points).filter(p => {
        return p.code.toLowerCase().includes(query) ||
               p.cleanCode.toLowerCase().includes(query) ||
               p.pinyin.toLowerCase().includes(query) ||
               p.hanzi.includes(query) ||
               p.english.toLowerCase().includes(query) ||
               p.tags.some(t => t.toLowerCase().includes(query)) ||
               p.locationClassical.toLowerCase().includes(query) ||
               p.actions.some(a => a.toLowerCase().includes(query));
    });

    let html = `
    <div class="section-header-bar">
        <h2 class="section-title-h2">Search Results: "${appState.searchQuery}"</h2>
        <span class="section-counter">${matched.length} points</span>
    </div>
    <div class="search-results-grid">`;

    if (matched.length === 0) {
        html += `<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted); background:var(--bg-surface); border-radius:10px;">No acupuncture points found matching "${appState.searchQuery}". Try searching by code (e.g. ST36), Pinyin (Zusanli), or clinical symptom (cough, headache).</div>`;
    } else {
        matched.forEach(pt => {
            const safetyClass = pt.safetyLevel === 'danger' ? 'danger' : (pt.safetyLevel === 'caution' ? 'caution' : 'safe');
            const safetyText = pt.safetyLevel === 'danger' ? '🔴 Danger' : (pt.safetyLevel === 'caution' ? '🟡 Caution' : '🟢 Safe');
            
            html += `
            <div class="search-card" onclick="openPoint('${pt.code}')">
                ${pt.hasImage ? `
                <div class="pt-thumb-box" style="width:52px;height:52px;">
                    <img class="pt-thumb-img" src="${pt.image}" alt="${pt.code}" loading="lazy" onload="syncHeight()" onerror="this.onerror=null; this.src='${pt.remoteImage}'; this.onerror=function(){this.parentElement.style.display='none';}; syncHeight();" />
                </div>
                ` : ''}
                <div class="search-card-main">
                    <div class="search-card-top">
                        <span class="search-card-code">${pt.code}</span>
                        <span class="safety-pill ${safetyClass}" style="font-size:0.68rem;padding:2px 6px;">${safetyText}</span>
                    </div>
                    <div class="search-card-names">${pt.pinyin} (${pt.hanzi})</div>
                    <div class="search-card-eng">${pt.english}</div>
                    <div class="search-card-loc">${pt.locationClassical.substring(0, 75)}...</div>
                    <div class="pt-tags-row" style="margin-top:6px;">
                        ${pt.tags.slice(0, 3).map(t => `<span class="pt-tag">#${t}</span>`).join('')}
                    </div>
                </div>
            </div>`;
        });
    }

    html += `</div>`;
    mainContentArea.innerHTML = html;
}

// Initial Mount
render();
</script>
</body>
</html>"""

def generate_atlas_html() -> str:
    """Generate self-contained interactive Acupuncture Atlas application."""
    dataset = get_atlas_dataset()
    data_json = json.dumps(dataset, ensure_ascii=False)
    return HTML_TEMPLATE.replace("__DATA_PAYLOAD__", data_json)

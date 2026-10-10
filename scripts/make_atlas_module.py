# -*- coding: utf-8 -*-
"""Generate modules/atlas.py cleanly using template substitution."""

import json

with open("d:/TCM/acupuncture_app/static/atlas_meridians.json", "r", encoding="utf-8") as f:
    meridians = json.load(f)

with open("d:/TCM/acupuncture_app/static/atlas_points.json", "r", encoding="utf-8") as f:
    points = json.load(f)

meridians_str = json.dumps(meridians, indent=2, ensure_ascii=False)
points_str = json.dumps(points, indent=2, ensure_ascii=False)
data_payload_str = json.dumps({"meridians": meridians, "points": points}, ensure_ascii=False)

html_template = """<!DOCTYPE html>
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
    --accent-blue: #0284c7;
    --accent-blue-subtle: #e0f2fe;
    --signal-danger: #ef4444;
    --signal-danger-bg: #fef2f2;
    --signal-caution: #f59e0b;
    --signal-caution-bg: #fffbeb;
    --signal-safe: #10b981;
    --signal-safe-bg: #ecfdf5;
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
    --signal-danger: #f87171;
    --signal-danger-bg: #450a0a;
    --signal-caution: #fbbf24;
    --signal-caution-bg: #451a03;
    --signal-safe: #34d399;
    --signal-safe-bg: #064e3b;
    --card-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.3);
    --card-hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-sans);
    background-color: var(--bg-page);
    color: var(--text-primary);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
}

/* Header / Monolith Hero */
.atlas-header {
    max-width: 1280px;
    margin: 0 auto;
    padding: 24px 20px 16px 20px;
}

.atlas-category-tag {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent-blue);
    margin-bottom: 6px;
    font-family: var(--font-mono);
}

.atlas-title {
    font-size: clamp(2rem, 4vw, 2.85rem);
    font-weight: 900;
    letter-spacing: -0.04em;
    line-height: 1.05;
    color: var(--text-primary);
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
}

.atlas-title-text span {
    color: var(--accent-blue);
}

.theme-toggle-btn {
    font-size: 0.8rem;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    background: var(--bg-surface);
    color: var(--text-primary);
    cursor: pointer;
    transition: all 0.15s ease;
}
.theme-toggle-btn:hover {
    background: var(--bg-surface-low);
}

.atlas-subtitle {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-top: 6px;
    font-family: var(--font-mono);
}

/* Stats Ribbon */
.stats-ribbon {
    border-top: 1px solid var(--border-subtle);
    border-bottom: 1px solid var(--border-subtle);
    background-color: var(--bg-surface-low);
    margin-top: 14px;
}

.stats-container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 10px 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 16px;
    font-size: 0.82rem;
    font-family: var(--font-mono);
}

.stat-item {
    display: flex;
    align-items: baseline;
    gap: 6px;
}

.stat-val {
    font-weight: 800;
    color: var(--text-primary);
}

.stat-lbl {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
}

.stat-sep {
    color: var(--border-strong);
}

/* Main App Wrapper */
.atlas-main {
    max-width: 1280px;
    margin: 0 auto;
    padding: 20px;
}

/* Search & Filter Bar */
.search-filter-section {
    margin-bottom: 20px;
}

.search-input-box {
    position: relative;
    display: flex;
    align-items: center;
    background: var(--bg-surface);
    border: 2px solid var(--border-strong);
    border-radius: 10px;
    padding: 10px 14px;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
}

.search-input-box:focus-within {
    border-color: var(--accent-blue);
    box-shadow: 0 0 0 3px var(--accent-blue-subtle);
}

.search-icon {
    font-size: 1rem;
    color: var(--text-muted);
    margin-right: 10px;
}

.search-field {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    font-size: 0.95rem;
    color: var(--text-primary);
    font-family: var(--font-sans);
}

.search-field::placeholder {
    color: var(--text-dim);
}

.search-kbd {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    padding: 2px 6px;
    border-radius: 4px;
    color: var(--text-muted);
}

.search-clear-btn {
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 1rem;
    cursor: pointer;
    padding: 0 4px;
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
    gap: 8px;
    margin-top: 12px;
}

.chip-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-right: 4px;
}

.filter-chip {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 6px;
    padding: 5px 11px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s ease;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.filter-chip:hover {
    background: var(--bg-surface-low);
    color: var(--text-primary);
}

.filter-chip.active {
    background: var(--text-primary);
    color: var(--bg-surface);
    border-color: var(--text-primary);
}

.filter-chip.chip-danger.active {
    background: var(--signal-danger);
    border-color: var(--signal-danger);
    color: #ffffff;
}

/* Content Layout (Body Map + Dynamic Content Area) */
.atlas-grid-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 28px;
    align-items: start;
    margin-top: 10px;
}

@media (max-width: 900px) {
    .atlas-grid-layout {
        grid-template-columns: 1fr;
    }
}

/* Left Column: Interactive Anatomical Body Map */
.body-map-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 16px;
    box-shadow: var(--card-shadow);
    position: sticky;
    top: 20px;
}

.view-toggle-wrap {
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
}

.view-toggle-group {
    display: inline-flex;
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 3px;
}

.view-btn {
    padding: 5px 14px;
    font-size: 0.76rem;
    font-weight: 600;
    border-radius: 6px;
    border: none;
    background: transparent;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.15s ease;
}

.view-btn.active {
    background: var(--text-primary);
    color: var(--bg-surface);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.body-svg-box {
    position: relative;
    width: 100%;
    aspect-ratio: 1696 / 2528;
    background: var(--bg-surface-low);
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border-subtle);
}

.body-svg {
    width: 100%;
    height: 100%;
    display: block;
}

.region-hitbox {
    cursor: pointer;
    transition: all 0.2s ease;
    outline: none;
}

.region-hitbox:hover {
    fill: url(#regionHoverGrad) !important;
    stroke: var(--accent-blue) !important;
    stroke-width: 6 !important;
}

.region-hitbox.active {
    fill: url(#regionActiveGrad) !important;
    stroke: var(--accent-blue) !important;
    stroke-width: 8 !important;
}

.region-badge-info {
    margin-top: 12px;
    text-align: center;
    font-size: 0.78rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
}

.region-active-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent-blue-subtle);
    color: var(--accent-blue);
    padding: 4px 10px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 0.76rem;
    border: 1px solid var(--accent-blue);
}

/* Right Column: Dynamic Content Area */
.content-area {
    min-width: 0;
}

/* State A: Primary Meridians Swiss Grid */
.meridians-section-header {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    border-bottom: 2px solid var(--text-primary);
    padding-bottom: 8px;
    margin-bottom: 16px;
}

.section-h2 {
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-transform: uppercase;
}

.section-count {
    font-family: var(--font-mono);
    font-weight: 700;
    font-size: 0.9rem;
    color: var(--text-muted);
}

.meridians-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 14px;
}

/* Swiss Meridian Card */
.swiss-card {
    position: relative;
    overflow: hidden;
    background-color: var(--bg-surface);
    border: 2px solid var(--border-strong);
    border-radius: 12px;
    padding: 18px;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: var(--card-shadow);
}

.swiss-card:hover {
    border-color: var(--text-primary);
    transform: translateY(-2px);
    box-shadow: var(--card-hover-shadow);
}

.card-watermark {
    position: absolute;
    bottom: -18px;
    right: -8px;
    font-size: 7.5rem;
    font-weight: 900;
    line-height: 0.8;
    color: var(--text-primary);
    opacity: 0.04;
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

.card-pt-count {
    font-family: var(--font-mono);
    font-size: 0.8rem;
    font-weight: 800;
    color: var(--text-primary);
}

.card-pt-count span {
    font-weight: 400;
    color: var(--text-muted);
    font-size: 0.72rem;
    margin-left: 2px;
    text-transform: uppercase;
}

.card-chevron {
    font-size: 0.9rem;
    color: var(--text-muted);
    transition: transform 0.15s ease, color 0.15s ease;
}

.swiss-card:hover .card-chevron {
    color: var(--accent-blue);
    transform: translateX(3px);
}

.card-code {
    position: relative;
    z-index: 2;
    font-family: var(--font-mono);
    font-size: 3rem;
    font-weight: 900;
    letter-spacing: -0.05em;
    line-height: 1;
    color: var(--text-primary);
    margin: 8px 0;
}

.card-bottom-row {
    position: relative;
    z-index: 2;
    padding-top: 10px;
    border-top: 1px solid var(--border-subtle);
}

.card-name-wrap {
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-elem-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}

.card-eng-name {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-primary);
}

.card-chinese-name {
    font-size: 0.76rem;
    color: var(--text-muted);
    margin-top: 2px;
    margin-left: 16px;
    letter-spacing: 0.02em;
}

/* State B: Meridian Point Explorer */
.breadcrumb-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-bottom: 16px;
}

.breadcrumb-back {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    color: var(--accent-blue);
    font-weight: 700;
    cursor: pointer;
    background: none;
    border: none;
    font-size: 0.82rem;
    font-family: var(--font-sans);
}
.breadcrumb-back:hover {
    text-decoration: underline;
}

.meridian-hero {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: var(--card-shadow);
}

.m-hero-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 12px;
}

.m-hero-title {
    display: flex;
    align-items: baseline;
    gap: 12px;
}

.m-hero-code {
    font-family: var(--font-mono);
    font-size: 2.5rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: var(--text-primary);
}

.m-hero-chinese {
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text-muted);
}

.m-hero-meta {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 8px;
    flex-wrap: wrap;
}

.m-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 0.74rem;
    font-weight: 700;
    font-family: var(--font-mono);
    border: 1px solid var(--border-strong);
    background: var(--bg-surface-low);
}

.m-nav-btns {
    display: flex;
    gap: 6px;
}

.nav-arrow-btn {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    border: 1px solid var(--border-strong);
    background: var(--bg-surface);
    color: var(--text-primary);
    cursor: pointer;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.15s ease;
}
.nav-arrow-btn:hover {
    border-color: var(--accent-blue);
    color: var(--accent-blue);
}

/* Points List in Channel */
.channel-points-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.point-row-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 14px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
}

.point-row-card:hover {
    border-color: var(--accent-blue);
    transform: translateX(3px);
}

.pt-row-main {
    display: flex;
    align-items: center;
    gap: 14px;
    flex: 1;
    min-width: 0;
}

.pt-code-badge {
    font-family: var(--font-mono);
    font-size: 0.95rem;
    font-weight: 800;
    color: var(--text-primary);
    min-width: 65px;
}

.pt-name-wrap {
    display: flex;
    align-items: baseline;
    gap: 8px;
}

.pt-pinyin {
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-primary);
}

.pt-hanzi {
    font-size: 0.85rem;
    color: var(--text-muted);
}

.pt-eng-trans {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-top: 2px;
}

.pt-tags-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-top: 6px;
}

.tag-pill {
    font-size: 0.68rem;
    font-family: var(--font-mono);
    padding: 1px 6px;
    border-radius: 4px;
    background: var(--bg-surface-low);
    color: var(--text-muted);
}

.safety-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.74rem;
    font-weight: 700;
    flex-shrink: 0;
}

.safety-pill.danger {
    background: var(--signal-danger-bg);
    color: var(--signal-danger);
    border: 1px solid var(--signal-danger);
}

.safety-pill.caution {
    background: var(--signal-caution-bg);
    color: var(--signal-caution);
    border: 1px solid var(--signal-caution);
}

.safety-pill.safe {
    background: var(--signal-safe-bg);
    color: var(--signal-safe);
    border: 1px solid var(--signal-safe);
}

/* State C: Full Point Detail Profile (acupuntura.com/en/atlas/stomach/ST-36/) */
.point-detail-page {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 14px;
    padding: 24px;
    box-shadow: var(--card-hover-shadow);
}

.pdp-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 2px solid var(--border-subtle);
    padding-bottom: 18px;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 14px;
}

.pdp-title-box {
    display: flex;
    align-items: baseline;
    gap: 12px;
    flex-wrap: wrap;
}

.pdp-code {
    font-family: var(--font-mono);
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: var(--text-primary);
    line-height: 1;
}

.pdp-pinyin {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
}

.pdp-hanzi {
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text-muted);
}

.pdp-eng {
    font-size: 1rem;
    color: var(--text-secondary);
    margin-top: 4px;
    font-weight: 500;
}

.pdp-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 10px;
}

.pdp-layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 24px;
}

@media (max-width: 820px) {
    .pdp-layout {
        grid-template-columns: 1fr;
    }
}

/* Left Detail Column */
.gauge-card {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 14px;
}

.gauge-title {
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-bottom: 8px;
}

.depth-track {
    height: 8px;
    background: var(--bg-surface-high);
    border-radius: 4px;
    position: relative;
    overflow: hidden;
    margin: 10px 0;
}

.depth-fill {
    position: absolute;
    height: 100%;
    background: var(--accent-blue);
    border-radius: 4px;
}

.gauge-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    font-family: var(--font-mono);
    color: var(--text-muted);
}

.gauge-tech {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--accent-blue);
    margin-top: 8px;
}

.precaution-alert-box {
    border: 2px solid;
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 14px;
}

.precaution-alert-box.danger {
    background: var(--signal-danger-bg);
    border-color: var(--signal-danger);
    color: var(--signal-danger);
}

.precaution-alert-box.caution {
    background: var(--signal-caution-bg);
    border-color: var(--signal-caution);
    color: var(--signal-caution);
}

.precaution-alert-box.safe {
    background: var(--signal-safe-bg);
    border-color: var(--signal-safe);
    color: var(--signal-safe);
}

.alert-header {
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 6px;
}

.alert-body {
    font-size: 0.82rem;
    color: var(--text-primary);
    line-height: 1.4;
}

/* Right Detail Column: Tabs */
.tabs-nav {
    display: flex;
    border-bottom: 2px solid var(--border-subtle);
    gap: 4px;
    margin-bottom: 16px;
}

.tab-btn {
    padding: 8px 16px;
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    border: none;
    background: transparent;
    color: var(--text-muted);
    cursor: pointer;
    position: relative;
    transition: all 0.15s ease;
}

.tab-btn:hover {
    color: var(--text-primary);
}

.tab-btn.active {
    color: var(--accent-blue);
}

.tab-btn.active::after {
    content: "";
    position: absolute;
    bottom: -2px;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--accent-blue);
}

.tab-pane {
    display: none;
}
.tab-pane.active {
    display: block;
}

.detail-section {
    margin-bottom: 18px;
}

.detail-section-title {
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    font-family: var(--font-mono);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.detail-p {
    font-size: 0.92rem;
    color: var(--text-primary);
    line-height: 1.6;
}

.step-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.step-item {
    font-size: 0.88rem;
    color: var(--text-secondary);
    padding: 6px 10px;
    background: var(--bg-surface-low);
    border-radius: 6px;
    border-left: 3px solid var(--accent-blue);
}

.combo-card {
    background: var(--bg-surface-low);
    border: 1px solid var(--border-strong);
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
}

.combo-pts {
    font-family: var(--font-mono);
    font-weight: 800;
    font-size: 0.88rem;
    color: var(--accent-blue);
}

.combo-desc {
    font-size: 0.82rem;
    color: var(--text-secondary);
    margin-top: 3px;
}

/* Global Search Results Grid */
.search-results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 12px;
}

.search-res-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    padding: 14px;
    cursor: pointer;
    transition: all 0.15s ease;
    box-shadow: var(--card-shadow);
}
.search-res-card:hover {
    border-color: var(--accent-blue);
    transform: translateY(-2px);
    box-shadow: var(--card-hover-shadow);
}
</style>
</head>
<body>

<!-- Header / Monolith Hero -->
<header class="atlas-header">
    <div class="atlas-category-tag">CLASSICAL POINTS · 14 MERIDIANS · WHO STANDARD</div>
    <div class="atlas-title">
        <div class="atlas-title-text">ACUPUNCTURE <span>ATLAS.</span></div>
        <button class="theme-toggle-btn" id="theme-btn">🌓 Toggle Dark</button>
    </div>
    <div class="atlas-subtitle">361+ POINTS · 14 MERIDIANS · 五行 5 ELEMENTS · WHO & CEIMEC STANDARD</div>
</header>

<!-- Stats Ribbon -->
<section class="stats-ribbon">
    <div class="stats-container">
        <div class="stat-item"><span class="stat-val">361+</span> <span class="stat-lbl">Points</span></div>
        <span class="stat-sep">·</span>
        <div class="stat-item"><span class="stat-val">14</span> <span class="stat-lbl">Meridians</span></div>
        <span class="stat-sep">·</span>
        <div class="stat-item"><span class="stat-val">五行</span> <span class="stat-lbl">5 Elements</span></div>
        <span class="stat-sep">·</span>
        <div class="stat-item"><span class="stat-val">WHO</span> <span class="stat-lbl">Standard</span></div>
    </div>
</section>

<!-- Main Interactive Content Area -->
<main class="atlas-main">
    <!-- Search Bar & Region Filters -->
    <section class="search-filter-section">
        <div class="search-input-box">
            <span class="search-icon">🔍</span>
            <input type="text" id="atlas-search" class="search-field" placeholder="Search by name (Zusanli), code (ST36), pinyin, or condition (headache, asthma)..." autocomplete="off" spellcheck="false">
            <button class="search-clear-btn" id="search-clear">✕</button>
            <kbd class="search-kbd">/</kbd>
        </div>

        <!-- Filter Chips Row -->
        <div class="filter-chips-row">
            <span class="chip-label">Region</span>
            <button class="filter-chip active" data-region="ALL">All</button>
            <button class="filter-chip" data-region="Head">Head</button>
            <button class="filter-chip" data-region="Neck">Neck</button>
            <button class="filter-chip" data-region="Chest">Chest</button>
            <button class="filter-chip" data-region="Abdomen">Abdomen</button>
            <button class="filter-chip" data-region="Back">Back</button>
            <button class="filter-chip" data-region="Upper Limb">Upper Limb</button>
            <button class="filter-chip" data-region="Lower Limb">Lower Limb</button>

            <span class="chip-label" style="margin-left: 12px;">Special</span>
            <button class="filter-chip" data-special="major">★ Major</button>
            <button class="filter-chip chip-danger" data-special="risk">⚠ Risk</button>
        </div>
    </section>

    <!-- Layout: Body Map on Left, Dynamic View on Right -->
    <div class="atlas-grid-layout">
        <!-- Left: Interactive Anatomical Body Map -->
        <aside class="body-map-card">
            <div class="view-toggle-wrap">
                <div class="view-toggle-group">
                    <button class="view-btn active" id="btn-ant">Anterior</button>
                    <button class="view-btn" id="btn-post">Posterior</button>
                </div>
            </div>

            <div class="body-svg-box">
                <svg viewBox="0 0 1696 2528" class="body-svg" id="body-map-svg" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <!-- Translucent Glow Gradients (acupuntura.com standard) -->
                        <linearGradient id="regionActiveGrad" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.38" />
                            <stop offset="100%" stop-color="#34d399" stop-opacity="0.25" />
                        </linearGradient>
                        <linearGradient id="regionHoverGrad" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.18" />
                            <stop offset="100%" stop-color="#34d399" stop-opacity="0.12" />
                        </linearGradient>
                    </defs>

                    <!-- Anatomical Silhouette Layer -->
                    <g id="body-silhouette" fill="#cbd5e1" opacity="0.55" stroke="#94a3b8" stroke-width="4">
                        <!-- Head -->
                        <path d="M 767,133 C 804,115 886,115 923,133 C 960,170 969,220 965,266 C 960,308 946,331 923,354 L 767,354 C 744,331 730,308 726,266 C 721,220 730,170 767,133 Z" />
                        <!-- Neck -->
                        <path d="M 776,354 L 914,354 L 923,464 L 767,464 Z" />
                        <!-- Chest & Shoulders -->
                        <path d="M 767,464 L 923,464 L 1079,524 L 1116,827 L 583,827 L 611,524 Z" />
                        <!-- Abdomen / Lower Torso -->
                        <path d="M 583,827 L 1116,827 L 1089,1268 L 611,1268 Z" />
                        <!-- Arms -->
                        <path d="M 1089,565 L 1162,588 L 1180,827 L 1217,1010 L 1263,1176 L 1327,1295 L 1148,1304 L 1125,1102 L 1112,919 L 1098,735 Z M 607,565 L 534,588 L 515,827 L 479,1010 L 433,1176 L 368,1295 L 548,1304 L 570,1102 L 584,919 L 598,735 Z" />
                        <!-- Legs -->
                        <path d="M 611,1268 L 749,1268 L 758,1516 L 767,1745 L 776,1975 L 772,2296 L 767,2462 L 666,2462 L 675,2296 L 671,1975 L 657,1745 L 638,1516 Z M 1089,1268 L 951,1268 L 942,1516 L 932,1745 L 923,1975 L 928,2296 L 932,2462 L 1033,2462 L 1024,2296 L 1029,1975 L 1043,1745 L 1061,1516 Z" />
                    </g>

                    <!-- Interactive Region Hitboxes (Exact coordinates from acupuntura.com/en/atlas/) -->
                    <g id="hitboxes-layer">
                        <!-- Head -->
                        <path d="M 767,133 C 804,115 886,115 923,133 C 960,170 969,220 965,266 C 960,308 946,331 923,354 L 767,354 C 744,331 730,308 726,266 C 721,220 730,170 767,133 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Head" />
                        <!-- Neck -->
                        <path d="M 776,354 L 914,354 L 923,464 L 767,464 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Neck" />
                        <!-- Chest (Anterior) / Upper Back (Posterior) -->
                        <path id="hb-chest" d="M 767,464 L 923,464 L 1079,524 L 1116,827 L 583,827 L 611,524 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Chest" />
                        <!-- Abdomen (Anterior) / Lower Back (Posterior) -->
                        <path id="hb-abdomen" d="M 583,827 L 1116,827 L 1089,1268 L 611,1268 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Abdomen" />
                        <!-- Upper Limb -->
                        <path d="M 1089,565 L 1162,588 L 1180,827 L 1217,1010 L 1263,1176 L 1327,1295 L 1148,1304 L 1125,1102 L 1112,919 L 1098,735 Z M 607,565 L 534,588 L 515,827 L 479,1010 L 433,1176 L 368,1295 L 548,1304 L 570,1102 L 584,919 L 598,735 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Upper Limb" />
                        <!-- Lower Limb -->
                        <path d="M 611,1268 L 749,1268 L 758,1516 L 767,1745 L 776,1975 L 772,2296 L 767,2462 L 666,2462 L 675,2296 L 671,1975 L 657,1745 L 638,1516 Z M 1089,1268 L 951,1268 L 942,1516 L 932,1745 L 923,1975 L 928,2296 L 932,2462 L 1033,2462 L 1024,2296 L 1029,1975 L 1043,1745 L 1061,1516 Z" fill="transparent" stroke="transparent" stroke-width="4" class="region-hitbox" data-reg="Lower Limb" />
                    </g>
                </svg>
            </div>

            <div class="region-badge-info" id="region-status">
                <span>Click body region to filter</span>
            </div>
        </aside>

        <!-- Right: Dynamic Views (Hub Grid / Meridian Explorer / Point Profile / Search) -->
        <section class="content-area" id="content-area">
            <!-- Populated via JavaScript -->
        </section>
    </div>
</main>

<script>
// Load Dataset
const DATA = __DATA_PAYLOAD__;

// Application State
let currentRegion = 'ALL';
let currentSpecial = null;
let currentSearch = '';
let activeMeridianId = null;
let activePointCode = null;
let currentBodyView = 'anterior';

// DOM Elements
const contentArea = document.getElementById('content-area');
const searchInput = document.getElementById('atlas-search');
const searchClearBtn = document.getElementById('search-clear');
const regionStatus = document.getElementById('region-status');
const btnAnt = document.getElementById('btn-ant');
const btnPost = document.getElementById('btn-post');

// Theme Switcher
document.getElementById('theme-btn').addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    document.documentElement.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
});

// Search Handler
searchInput.addEventListener('input', (e) => {
    currentSearch = e.target.value.trim().toLowerCase();
    searchClearBtn.style.display = currentSearch ? 'block' : 'none';
    render();
});

searchClearBtn.addEventListener('click', () => {
    searchInput.value = '';
    currentSearch = '';
    searchClearBtn.style.display = 'none';
    render();
});

window.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
    } else if (e.key === 'Escape') {
        if (activePointCode) {
            activePointCode = null;
            render();
        } else if (activeMeridianId) {
            activeMeridianId = null;
            render();
        }
    }
});

// Filter Chips Handlers
document.querySelectorAll('.filter-chip[data-region]').forEach(chip => {
    chip.addEventListener('click', () => {
        currentRegion = chip.getAttribute('data-region');
        document.querySelectorAll('.filter-chip[data-region]').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        highlightSvgRegion(currentRegion);
        render();
    });
});

document.querySelectorAll('.filter-chip[data-special]').forEach(chip => {
    chip.addEventListener('click', () => {
        const sp = chip.getAttribute('data-special');
        if (currentSpecial === sp) {
            currentSpecial = null;
            chip.classList.remove('active');
        } else {
            document.querySelectorAll('.filter-chip[data-special]').forEach(c => c.classList.remove('active'));
            currentSpecial = sp;
            chip.classList.add('active');
        }
        render();
    });
});

// Body Map View Toggle (Anterior / Posterior)
btnAnt.addEventListener('click', () => setBodyView('anterior'));
btnPost.addEventListener('click', () => setBodyView('posterior'));

function setBodyView(view) {
    currentBodyView = view;
    btnAnt.classList.toggle('active', view === 'anterior');
    btnPost.classList.toggle('active', view === 'posterior');

    const hbChest = document.getElementById('hb-chest');
    const hbAbdomen = document.getElementById('hb-abdomen');
    if (view === 'posterior') {
        hbChest.setAttribute('data-reg', 'Back');
        hbAbdomen.setAttribute('data-reg', 'Back');
    } else {
        hbChest.setAttribute('data-reg', 'Chest');
        hbAbdomen.setAttribute('data-reg', 'Abdomen');
    }
    highlightSvgRegion(currentRegion);
}

// SVG Region Click / Hover Handlers
document.querySelectorAll('.region-hitbox').forEach(el => {
    el.addEventListener('click', () => {
        const reg = el.getAttribute('data-reg');
        if (currentRegion === reg) {
            currentRegion = 'ALL';
        } else {
            currentRegion = reg;
        }
        // Update Chips UI
        document.querySelectorAll('.filter-chip[data-region]').forEach(c => {
            c.classList.toggle('active', c.getAttribute('data-region') === currentRegion);
        });
        highlightSvgRegion(currentRegion);
        render();
    });
});

function highlightSvgRegion(reg) {
    document.querySelectorAll('.region-hitbox').forEach(el => el.classList.remove('active'));
    if (reg !== 'ALL') {
        document.querySelectorAll(`.region-hitbox[data-reg="${reg}"]`).forEach(el => el.classList.add('active'));
        regionStatus.innerHTML = `<span class="region-active-pill">${reg} Region Active <span onclick="clearRegion(event)" style="cursor:pointer;margin-left:4px;">✕</span></span>`;
    } else {
        regionStatus.innerHTML = `<span>Click body region to filter</span>`;
    }
}

window.clearRegion = function(e) {
    e.stopPropagation();
    currentRegion = 'ALL';
    document.querySelectorAll('.filter-chip[data-region]').forEach(c => {
        c.classList.toggle('active', c.getAttribute('data-region') === 'ALL');
    });
    highlightSvgRegion('ALL');
    render();
};

// RENDER CONTROLLER
function render() {
    // 1. If Global Search is active
    if (currentSearch.length >= 2) {
        renderSearchResults();
        return;
    }

    // 2. If Point Profile is active
    if (activePointCode) {
        renderPointProfile(activePointCode);
        return;
    }

    // 3. If Meridian Explorer is active
    if (activeMeridianId) {
        renderMeridianExplorer(activeMeridianId);
        return;
    }

    // 4. Default: Hub Grid View
    renderMeridiansHub();
}

// View A: Primary Meridians Hub Grid ("Swiss Cards")
function renderMeridiansHub() {
    const filteredMeridians = DATA.meridians.filter(m => {
        if (currentRegion === 'ALL') return true;
        return Object.values(DATA.points).some(p => p.channelId === m.id && p.region === currentRegion);
    });

    let html = `
    <div class="meridians-section-header">
        <h2 class="section-h2">Primary Meridians</h2>
        <span class="section-count">${filteredMeridians.length}</span>
    </div>
    <div class="meridians-grid">`;

    filteredMeridians.forEach(m => {
        html += `
        <div class="swiss-card" onclick="openMeridian('${m.id}')">
            <div class="card-watermark">${m.watermark}</div>
            <div class="card-top-row">
                <div class="card-pt-count">${m.totalPoints}<span>pts</span></div>
                <span class="card-chevron">→</span>
            </div>
            <div class="card-code">${m.id}</div>
            <div class="card-bottom-row">
                <div class="card-name-wrap">
                    <span class="card-elem-dot" style="background-color: ${m.color};"></span>
                    <span class="card-eng-name">${m.name}</span>
                </div>
                <div class="card-chinese-name">${m.chinese}</div>
            </div>
        </div>`;
    });

    html += `</div>`;
    contentArea.innerHTML = html;
}

// View B: Meridian Point Explorer
function renderMeridianExplorer(mId) {
    const m = DATA.meridians.find(item => item.id === mId) || DATA.meridians[0];
    const pts = Object.values(DATA.points).filter(p => p.channelId === mId);

    // Apply filters if any
    const displayPts = pts.filter(p => {
        if (currentRegion !== 'ALL' && p.region !== currentRegion) return false;
        if (currentSpecial === 'major' && p.tier !== 1) return false;
        if (currentSpecial === 'risk' && p.safetyLevel !== 'danger') return false;
        return true;
    });

    // Find Prev and Next Meridian
    const mIdx = DATA.meridians.findIndex(item => item.id === mId);
    const prevM = DATA.meridians[(mIdx - 1 + DATA.meridians.length) % DATA.meridians.length];
    const nextM = DATA.meridians[(mIdx + 1) % DATA.meridians.length];

    let html = `
    <nav class="breadcrumb-bar">
        <button class="breadcrumb-back" onclick="closeMeridian()">← Atlas</button>
        <span>/</span>
        <span style="font-weight: 700; color: var(--text-primary);">${m.name} (${m.id})</span>
    </nav>

    <div class="meridian-hero">
        <div class="m-hero-top">
            <div>
                <div class="m-hero-title">
                    <span class="m-hero-code">${m.id}</span>
                    <span class="m-hero-chinese">${m.chinese}</span>
                </div>
                <div class="m-hero-meta">
                    <span style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary);">${m.name}</span>
                    <span class="m-badge"><span style="width:7px;height:7px;border-radius:50%;background:${m.color};"></span>${m.element} (${m.elementChinese})</span>
                    <span class="m-badge">${m.polarity}</span>
                    <span class="m-badge">${m.totalPoints} Points</span>
                    <span class="m-badge">⏰ ${m.organTime}</span>
                </div>
            </div>
            <div class="m-nav-btns">
                <button class="nav-arrow-btn" onclick="openMeridian('${prevM.id}')" title="Previous Meridian: ${prevM.name}">←</button>
                <button class="nav-arrow-btn" onclick="openMeridian('${nextM.id}')" title="Next Meridian: ${nextM.name}">→</button>
            </div>
        </div>
        <p style="font-size: 0.84rem; color: var(--text-secondary); margin-top: 12px; line-height: 1.5;">${m.overview}</p>
    </div>

    <div class="channel-points-list">`;

    if (displayPts.length === 0) {
        html += `<div style="text-align:center;padding:40px;color:var(--text-muted);">No points match the active region or filter in this channel.</div>`;
    } else {
        displayPts.forEach(pt => {
            html += `
            <div class="point-row-card" onclick="openPoint('${pt.code}')">
                <div class="pt-row-main">
                    <span class="pt-code-badge">${pt.code}</span>
                    <div>
                        <div class="pt-name-wrap">
                            <span class="pt-pinyin">${pt.pinyin}</span>
                            <span class="pt-hanzi">${pt.hanzi}</span>
                            <span style="font-size:0.75rem;padding:2px 6px;border-radius:4px;background:var(--bg-surface-low);color:var(--text-secondary);">${pt.category}</span>
                        </div>
                        <div class="pt-eng-trans">${pt.english}</div>
                        <div class="pt-tags-wrap">
                            ${pt.tags.map(t => `<span class="tag-pill">#${t}</span>`).join('')}
                        </div>
                    </div>
                </div>
                <div class="safety-pill ${pt.safetyLevel}">
                    ${pt.safetyLevel === 'danger' ? '🔴 Danger' : (pt.safetyLevel === 'caution' ? '🟡 Caution' : '🟢 Safe')}
                </div>
            </div>`;
        });
    }

    html += `</div>`;
    contentArea.innerHTML = html;
}

// View C: Full Point Detail Profile (acupuntura.com/en/atlas/stomach/ST-36/)
function renderPointProfile(ptCode) {
    const pt = DATA.points[ptCode];
    if (!pt) return;

    const m = DATA.meridians.find(item => item.id === pt.channelId) || { color: '#0284c7', name: 'Channel' };
    const ptKeys = Object.keys(DATA.points).filter(k => DATA.points[k].channelId === pt.channelId);
    const currIdx = ptKeys.indexOf(ptCode);
    const prevCode = ptKeys[(currIdx - 1 + ptKeys.length) % ptKeys.length];
    const nextCode = ptKeys[(currIdx + 1) % ptKeys.length];

    // Needle depth percentage for visual bar
    const fillLeft = (pt.depthMin / pt.depthMaxLimit) * 100;
    const fillWidth = ((pt.depthMax - pt.depthMin) / pt.depthMaxLimit) * 100;

    let html = `
    <nav class="breadcrumb-bar">
        <button class="breadcrumb-back" onclick="activePointCode = null; render();">← ${m.name} (${pt.channelId})</button>
        <span>/</span>
        <span style="font-weight: 700; color: var(--text-primary);">${pt.code}</span>
    </nav>

    <div class="point-detail-page">
        <!-- Header -->
        <div class="pdp-header">
            <div>
                <div class="pdp-title-box">
                    <span class="pdp-code"><span style="width:12px;height:12px;border-radius:50%;display:inline-block;background:${m.color};margin-right:8px;vertical-align:middle;"></span>${pt.code}</span>
                    <span class="pdp-pinyin">${pt.pinyin}</span>
                    <span class="pdp-hanzi">${pt.hanzi}</span>
                </div>
                <div class="pdp-eng">${pt.english}</div>
                <div class="pdp-badges">
                    ${pt.tier === 1 ? '<span class="m-badge" style="background:#fee2e2;color:#b91c1c;border-color:#fca5a5;">★ Major Point</span>' : ''}
                    <span class="m-badge">${pt.category}</span>
                    <span class="m-badge">${pt.region}</span>
                    <span class="safety-pill ${pt.safetyLevel}">${pt.safetyLevel === 'danger' ? '🔴 Danger' : (pt.safetyLevel === 'caution' ? '🟡 Caution' : '🟢 Safe')}</span>
                </div>
            </div>
            <div class="m-nav-btns">
                <button class="nav-arrow-btn" onclick="openPoint('${prevCode}')" title="Previous: ${prevCode}">←</button>
                <button class="nav-arrow-btn" onclick="openPoint('${nextCode}')" title="Next: ${nextCode}">→</button>
            </div>
        </div>

        <!-- PDP Split Layout -->
        <div class="pdp-layout">
            <!-- Left: Needle Depth Gauge & Precautions Alert -->
            <div class="pdp-left-col">
                <!-- Visual Needle Depth Gauge -->
                <div class="gauge-card">
                    <div class="gauge-title">Needle Insertion Depth</div>
                    <div class="depth-track">
                        <div class="depth-fill" style="left: ${fillLeft}%; width: ${fillWidth}%;"></div>
                    </div>
                    <div class="gauge-labels">
                        <span>0 cun</span>
                        <span style="color:var(--accent-blue);font-weight:800;">${pt.depthMin}–${pt.depthMax} cun</span>
                        <span>${pt.depthMaxLimit} cun</span>
                    </div>
                    <div class="gauge-tech">${pt.technique}</div>
                </div>

                <!-- Clinical Safety Precautions Box -->
                <div class="precaution-alert-box ${pt.safetyLevel}">
                    <div class="alert-header">
                        <span>⚠️ Needling Precautions</span>
                    </div>
                    <div class="alert-body">${pt.safetyWarning}</div>
                </div>

                <!-- Anatomical Overview Box -->
                <div class="gauge-card">
                    <div class="gauge-title">🔬 Anatomy & Innervation</div>
                    <div style="font-size:0.82rem;color:var(--text-secondary);line-height:1.5;">${pt.anatomy}</div>
                </div>
            </div>

            <!-- Right: Tabbed Content (Location, TCM, Indications) -->
            <div class="pdp-right-col">
                <div class="tabs-nav">
                    <button class="tab-btn active" onclick="switchTab(this, 'tab-loc')">📍 Location</button>
                    <button class="tab-btn" onclick="switchTab(this, 'tab-tcm')">⚡ TCM Energetics</button>
                    <button class="tab-btn" onclick="switchTab(this, 'tab-ind')">🩺 Clinical Indications</button>
                </div>

                <!-- Tab 1: Location -->
                <div class="tab-pane active" id="tab-loc">
                    <div class="detail-section">
                        <div class="detail-section-title">📍 Classical Location (WHO Standard)</div>
                        <p class="detail-p">${pt.locationClassical}</p>
                    </div>

                    <div class="detail-section">
                        <div class="detail-section-title">🧭 Step-by-Step Practical Palpation</div>
                        <div class="step-list">
                            ${pt.howToFind.map(s => `<div class="step-item">${s}</div>`).join('')}
                        </div>
                    </div>

                    <div class="detail-section">
                        <div class="detail-section-title">📜 Etymology & Name Meaning</div>
                        <p class="detail-p">${pt.etymology}</p>
                    </div>
                </div>

                <!-- Tab 2: TCM Energetics -->
                <div class="tab-pane" id="tab-tcm">
                    <div class="detail-section">
                        <div class="detail-section-title">⚡ TCM Actions & Energetics</div>
                        <div class="step-list">
                            ${pt.actions.map(a => `<div class="step-item">✓ ${a}</div>`).join('')}
                        </div>
                    </div>

                    <div class="detail-section">
                        <div class="detail-section-title">🏷️ Channel & Five-Element Category</div>
                        <p class="detail-p"><strong>Channel:</strong> ${m.name} (${m.chinese})<br>
                        <strong>Element:</strong> ${m.element} (${m.elementChinese})<br>
                        <strong>Category:</strong> ${pt.category}</p>
                    </div>
                </div>

                <!-- Tab 3: Clinical Indications & Combinations -->
                <div class="tab-pane" id="tab-ind">
                    <div class="detail-section">
                        <div class="detail-section-title">🩺 Evidence-Based Indications</div>
                        <div class="pt-tags-wrap" style="margin-bottom: 12px;">
                            ${pt.indications.map(i => `<span class="tag-pill" style="font-size:0.8rem;padding:4px 8px;">${i}</span>`).join('')}
                        </div>
                    </div>

                    <div class="detail-section">
                        <div class="detail-section-title">🤝 Classical Point Combinations</div>
                        ${pt.combinations.map(c => `
                        <div class="combo-card">
                            <div class="combo-pts">${c.points}</div>
                            <div class="combo-desc">${c.indication}</div>
                        </div>`).join('')}
                    </div>
                </div>
            </div>
        </div>
    </div>`;

    contentArea.innerHTML = html;
}

// Tab Switcher inside Point Profile
window.switchTab = function(btn, tabId) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(tabId).classList.add('active');
};

// View D: Live Search Results Grid
function renderSearchResults() {
    const query = currentSearch;
    const matched = Object.values(DATA.points).filter(p => {
        return p.code.toLowerCase().includes(query) ||
               p.cleanCode.toLowerCase().includes(query) ||
               p.pinyin.toLowerCase().includes(query) ||
               p.hanzi.includes(query) ||
               p.english.toLowerCase().includes(query) ||
               p.tags.some(t => t.toLowerCase().includes(query)) ||
               p.locationClassical.toLowerCase().includes(query);
    });

    let html = `
    <div class="meridians-section-header">
        <h2 class="section-h2">Search Results: "${query}"</h2>
        <span class="section-count">${matched.length} points found</span>
    </div>
    <div class="search-results-grid">`;

    if (matched.length === 0) {
        html += `<div style="grid-column: 1/-1; text-align: center; padding: 40px; color: var(--text-muted);">No acupuncture points found matching "${query}".</div>`;
    } else {
        matched.forEach(pt => {
            html += `
            <div class="search-res-card" onclick="openPoint('${pt.code}')">
                <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px;">
                    <span style="font-family:var(--font-mono);font-weight:900;font-size:1.15rem;color:var(--text-primary);">${pt.code}</span>
                    <span class="safety-pill ${pt.safetyLevel}" style="padding:2px 7px;font-size:0.68rem;">${pt.safetyLevel}</span>
                </div>
                <div style="font-weight:700;font-size:0.9rem;color:var(--text-primary);">${pt.pinyin} (${pt.hanzi})</div>
                <div style="font-size:0.78rem;color:var(--text-muted);">${pt.english}</div>
                <div style="font-size:0.75rem;color:var(--text-secondary);margin-top:6px;line-height:1.4;">${pt.locationClassical.substring(0, 85)}...</div>
                <div class="pt-tags-wrap" style="margin-top:8px;">
                    ${pt.tags.slice(0, 3).map(t => `<span class="tag-pill">#${t}</span>`).join('')}
                </div>
            </div>`;
        });
    }

    html += `</div>`;
    contentArea.innerHTML = html;
}

// Navigation Handlers
window.openMeridian = function(mId) {
    activeMeridianId = mId;
    activePointCode = null;
    currentSearch = '';
    searchInput.value = '';
    searchClearBtn.style.display = 'none';
    render();
};

window.closeMeridian = function() {
    activeMeridianId = null;
    activePointCode = null;
    render();
};

window.openPoint = function(ptCode) {
    activePointCode = ptCode;
    render();
};

// Initialize
render();
</script>
</body>
</html>"""

# Now write modules/atlas.py
file_content = f'''# -*- coding: utf-8 -*-
"""Acupuncture Atlas & Clinical Explorer Module.

Modeled directly after https://acupuntura.com/en/atlas/:
- Swiss-style modern minimalist medical typography and responsive layout
- Monolith header with live statistics and WHO/CEIMEC evidence-based standards
- Interactive Anatomical Body Map with Anterior/Posterior toggle and clickable SVG body regions
- Swiss-style Meridian Grid Cards with giant Chinese character watermarks and element badges
- Meridian Point Explorer with fast filtering, danger/caution/safe tags, and symptom badges
- Detailed Point Profile (modeled after https://acupuntura.com/en/atlas/stomach/ST-36/):
  * Visual Needle Depth gauge with highlighted insertion range
  * Clinical Safety Precautions alert box (contraindications, vital organ risks)
  * Location, practical Cun palpation guide, and anatomical landmarks
  * TCM energetics, Five-Element functions, and organ clock
  * Clinical indications, evidence-based symptoms, and classical point combinations
  * Previous / Next point sequential channel navigation
- Instant global multi-script search (Code, Pinyin, Hanzi, English, Clinical Conditions)
"""

import json
from typing import Dict, Any

ATLAS_MERIDIANS = {meridians_str}

ATLAS_POINTS = {points_str}

def get_atlas_dataset() -> Dict[str, Any]:
    """Return canonical meridians and points structured for the Acupuncture Atlas."""
    return {{
        "meridians": ATLAS_MERIDIANS,
        "points": ATLAS_POINTS
    }}

HTML_TEMPLATE = """{html_template}"""

def generate_atlas_html() -> str:
    """Generate self-contained interactive Acupuncture Atlas application."""
    dataset = get_atlas_dataset()
    data_json = json.dumps(dataset, ensure_ascii=False)
    return HTML_TEMPLATE.replace("__DATA_PAYLOAD__", data_json)
'''

with open("d:/TCM/acupuncture_app/modules/atlas.py", "w", encoding="utf-8") as f:
    f.write(file_content)

print("modules/atlas.py successfully created!")

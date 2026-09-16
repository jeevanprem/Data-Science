# -*- coding: utf-8 -*-
"""
Main Builder Script:
Assembles the complete NPTEL Data Science for Engineers Master Study Guide (Weeks 1-8).
Outputs a unified, production-grade HTML file.
"""

import os
import sys

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

print("Beginning compilation of NPTEL Data Science for Engineers Study Guide...")

from guide_modules.week1 import get_week1_content
from guide_modules.week2 import get_week2_content
from guide_modules.week3 import get_week3_content
from guide_modules.week4 import get_week4_content
from guide_modules.week5 import get_week5_content
from guide_modules.week6 import get_week6_content
from guide_modules.week7 import get_week7_content
from guide_modules.week8 import get_week8_content
from guide_modules.exam_cheatsheet import get_exam_cheatsheet_content

def get_header_and_styles():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Science for Engineers | Master Course Study Guide (Weeks 1–8)</title>
    
    <!-- KaTeX for pristine mathematical typesetting -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError : false
        });"></script>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,400;0,700;1,300&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary-navy: #0f2b48;
            --secondary-navy: #183b63;
            --accent-blue: #2563eb;
            --accent-sky: #0284c7;
            --accent-gold: #d97706;
            --accent-gold-light: #fef3c7;
            --bg-page: #f8fafc;
            --bg-card: #ffffff;
            --bg-alt: #f1f5f9;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --text-light: #94a3b8;
            --border-light: #e2e8f0;
            --border-accent: #cbd5e1;
            --success-green: #15803d;
            --success-bg: #f0fdf4;
            --danger-red: #b91c1c;
            --danger-bg: #fef2f2;
            --warning-amber: #b45309;
            --warning-bg: #fffbeb;
            --info-cyan: #0369a1;
            --info-bg: #f0f9ff;
            --purple-strat: #6d28d9;
            --purple-bg: #faf5ff;
            --code-bg: #0f172a;
            --code-text: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-main);
            line-height: 1.65;
            font-size: 15px;
            -webkit-font-smoothing: antialiased;
        }

        /* Layout Architecture */
        .app-container {
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar Navigation */
        .sidebar {
            width: 290px;
            background: var(--primary-navy);
            color: #f8fafc;
            position: fixed;
            top: 0;
            bottom: 0;
            left: 0;
            overflow-y: auto;
            z-index: 100;
            box-shadow: 4px 0 12px rgba(0,0,0,0.15);
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
        }

        .sidebar-header {
            padding: 24px 20px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            background: rgba(0,0,0,0.2);
        }

        .sidebar-brand {
            font-size: 1.15rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sidebar-sub {
            font-size: 0.78rem;
            color: #93c5fd;
            margin-top: 4px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
        }

        .sidebar-instructors {
            font-size: 0.75rem;
            color: #cbd5e1;
            margin-top: 8px;
            font-style: italic;
        }

        .sidebar-tools {
            padding: 14px 18px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .search-box {
            width: 100%;
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.08);
            color: #fff;
            font-size: 0.82rem;
            outline: none;
            transition: all 0.2s;
        }

        .search-box:focus {
            background: rgba(255,255,255,0.15);
            border-color: #60a5fa;
        }

        .btn-toolbar-group {
            display: flex;
            gap: 6px;
        }

        .btn-tool {
            flex: 1;
            background: rgba(255,255,255,0.1);
            color: #e2e8f0;
            border: 1px solid rgba(255,255,255,0.15);
            padding: 6px 8px;
            font-size: 0.72rem;
            border-radius: 4px;
            cursor: pointer;
            text-align: center;
            font-weight: 600;
            transition: all 0.2s;
            text-decoration: none;
        }

        .btn-tool:hover {
            background: var(--accent-blue);
            color: white;
            border-color: var(--accent-blue);
        }

        .nav-list {
            list-style: none;
            padding: 14px 10px;
            overflow-y: auto;
            flex-grow: 1;
        }

        .nav-item {
            margin-bottom: 4px;
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 8px 12px;
            color: #cbd5e1;
            text-decoration: none;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 500;
            transition: all 0.2s;
            gap: 10px;
        }

        .nav-link:hover {
            background: rgba(255,255,255,0.12);
            color: #ffffff;
            transform: translateX(3px);
        }

        .nav-badge {
            background: rgba(255,255,255,0.15);
            color: #93c5fd;
            font-size: 0.68rem;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
            min-width: 26px;
            text-align: center;
        }

        /* Main Content Container */
        .main-wrapper {
            margin-left: 290px;
            flex: 1;
            padding: 40px 48px;
            max-width: 1280px;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, var(--primary-navy) 0%, #1e40af 100%);
            color: white;
            border-radius: 14px;
            padding: 36px 40px;
            margin-bottom: 40px;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
            border-left: 6px solid var(--accent-gold);
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            color: #fef08a;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 12px;
            border: 1px solid rgba(254, 240, 138, 0.3);
        }

        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            margin-bottom: 10px;
            line-height: 1.25;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #bfdbfe;
            max-width: 820px;
            margin-bottom: 18px;
            font-weight: 400;
        }

        .hero-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            font-size: 0.82rem;
            color: #e2e8f0;
            padding-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
        }

        .hero-meta span {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Weekly Module Containers */
        .week-module {
            background: var(--bg-card);
            border-radius: 12px;
            border: 1px solid var(--border-light);
            margin-bottom: 50px;
            box-shadow: var(--shadow-sm);
            overflow: hidden;
            transition: box-shadow 0.2s;
        }

        .week-module:hover {
            box-shadow: var(--shadow-md);
        }

        .module-header {
            background: linear-gradient(to right, #0f2b48, #1e3a5f);
            color: white;
            padding: 24px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px solid var(--accent-gold);
        }

        .module-title-group h2 {
            font-size: 1.45rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .module-pill {
            background: var(--accent-gold);
            color: #0f172a;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 4px;
            text-transform: uppercase;
        }

        .module-lectures {
            font-size: 0.82rem;
            color: #93c5fd;
            margin-top: 4px;
        }

        .module-body {
            padding: 32px 34px;
        }

        /* Sub-sections */
        .section-block {
            margin-bottom: 36px;
        }

        .section-block:last-child {
            margin-bottom: 0;
        }

        .section-heading {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--primary-navy);
            border-bottom: 2px solid var(--border-light);
            padding-bottom: 8px;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .section-heading .badge-indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-blue);
            display: inline-block;
        }

        /* Pedagogical Callout Cards */
        .callout-card {
            border-radius: 8px;
            padding: 16px 20px;
            margin: 18px 0;
            font-size: 0.92rem;
            line-height: 1.6;
            display: flex;
            gap: 14px;
            border-left: 4px solid transparent;
        }

        .callout-icon {
            font-size: 1.3rem;
            line-height: 1;
            flex-shrink: 0;
            margin-top: 2px;
        }

        .callout-content h4 {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .callout-tip {
            background: var(--info-bg);
            border-left-color: var(--info-cyan);
            color: #0c4a6e;
        }
        .callout-tip h4 { color: var(--info-cyan); }

        .callout-trap {
            background: var(--danger-bg);
            border-left-color: var(--danger-red);
            color: #7f1d1d;
        }
        .callout-trap h4 { color: var(--danger-red); }

        .callout-strategy {
            background: var(--purple-bg);
            border-left-color: var(--purple-strat);
            color: #4c1d95;
        }
        .callout-strategy h4 { color: var(--purple-strat); }

        .callout-suggester {
            background: var(--warning-bg);
            border-left-color: var(--accent-gold);
            color: #78350f;
        }
        .callout-suggester h4 { color: var(--accent-gold); }

        /* Tables */
        .table-responsive {
            overflow-x: auto;
            margin: 18px 0;
            border-radius: 8px;
            border: 1px solid var(--border-light);
            box-shadow: var(--shadow-sm);
        }

        table.academic-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            background: #ffffff;
            text-align: left;
        }

        table.academic-table th {
            background: #f1f5f9;
            color: var(--primary-navy);
            padding: 12px 16px;
            font-weight: 700;
            border-bottom: 2px solid var(--border-accent);
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.04em;
        }

        table.academic-table td {
            padding: 11px 16px;
            border-bottom: 1px solid var(--border-light);
            vertical-align: middle;
        }

        table.academic-table tr:last-child td {
            border-bottom: none;
        }

        table.academic-table tr:hover {
            background: #f8fafc;
        }

        .code-cell {
            font-family: 'Fira Code', monospace;
            background: #f1f5f9;
            color: #0f172a;
            padding: 3px 6px;
            border-radius: 4px;
            font-size: 0.82rem;
            font-weight: 500;
        }

        /* Formula Boxes */
        .formula-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 16px;
            margin: 18px 0;
        }

        .formula-card {
            background: #f8fafc;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            padding: 16px 18px;
            transition: all 0.2s;
        }

        .formula-card:hover {
            border-color: #93c5fd;
            background: #ffffff;
            box-shadow: var(--shadow-sm);
        }

        .formula-title {
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--secondary-navy);
            text-transform: uppercase;
            letter-spacing: 0.03em;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .formula-math {
            font-size: 1.05rem;
            padding: 8px 0;
            color: #0f172a;
            text-align: center;
            overflow-x: auto;
        }

        .formula-desc {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 6px;
            line-height: 1.4;
        }

        /* Formula Card Sub-Example Questions */
        .formula-examples {
            margin-top: 12px;
            padding-top: 10px;
            border-top: 1px dashed #cbd5e1;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .formula-example-item {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 8px 10px;
            font-size: 0.81rem;
            line-height: 1.45;
        }

        .formula-example-q {
            font-weight: 600;
            color: var(--primary-navy);
            margin-bottom: 4px;
            display: flex;
            align-items: baseline;
            gap: 6px;
        }

        .formula-example-badge {
            background: #e0f2fe;
            color: #0369a1;
            font-size: 0.68rem;
            font-weight: 700;
            padding: 1px 5px;
            border-radius: 3px;
            text-transform: uppercase;
            flex-shrink: 0;
        }

        .formula-example-a {
            color: #334155;
            background: #f8fafc;
            padding: 5px 8px;
            border-radius: 4px;
            border-left: 2px solid var(--accent-blue);
            font-size: 0.79rem;
        }

        /* Code Blocks */
        pre.r-code {
            background: var(--code-bg);
            color: var(--code-text);
            padding: 16px 20px;
            border-radius: 8px;
            font-family: 'Fira Code', Consolas, Monaco, monospace;
            font-size: 0.85rem;
            line-height: 1.6;
            overflow-x: auto;
            margin: 14px 0;
            border-left: 4px solid #3b82f6;
        }

        code.inline-code {
            font-family: 'Fira Code', monospace;
            background: #e2e8f0;
            color: #0f172a;
            padding: 2px 5px;
            border-radius: 4px;
            font-size: 0.84em;
        }

        /* Practice & Example Questions */
        .question-card {
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            margin: 18px 0;
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }

        .question-header {
            padding: 14px 18px;
            background: #f8fafc;
            border-bottom: 1px solid var(--border-light);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .q-tag {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 3px 8px;
            border-radius: 4px;
            letter-spacing: 0.04em;
        }

        .q-tag-concept { background: #dbeafe; color: #1e40af; }
        .q-tag-calc { background: #fef3c7; color: #92400e; }
        .q-tag-assignment { background: #dcfce7; color: #166534; font-weight: 800; }

        .question-body {
            padding: 18px 20px;
            font-size: 0.94rem;
        }

        .options-list {
            list-style: none;
            margin: 14px 0 10px;
            padding-left: 4px;
        }

        .options-list li {
            padding: 6px 10px;
            margin-bottom: 6px;
            border-radius: 5px;
            font-size: 0.9rem;
            display: flex;
            align-items: flex-start;
            gap: 10px;
            background: #f8fafc;
            border: 1px solid var(--border-light);
        }

        .options-list li.correct-option {
            background: #f0fdf4;
            border-color: #86efac;
            font-weight: 600;
            color: #14532d;
        }

        .opt-bullet {
            font-weight: 700;
            color: var(--secondary-navy);
            min-width: 20px;
        }

        /* Collapsible Solution Drawer */
        details.solution-drawer {
            border-top: 1px solid var(--border-light);
            background: #fafafa;
        }

        details.solution-drawer summary {
            padding: 12px 20px;
            font-weight: 600;
            font-size: 0.86rem;
            color: var(--secondary-navy);
            cursor: pointer;
            user-select: none;
            background: #f1f5f9;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: background 0.2s;
        }

        details.solution-drawer summary:hover {
            background: #e2e8f0;
            color: var(--primary-navy);
        }

        .solution-content {
            padding: 18px 22px;
            background: #ffffff;
            font-size: 0.91rem;
            border-top: 1px solid var(--border-light);
        }

        .step-block {
            margin-bottom: 12px;
            padding-left: 14px;
            border-left: 2px solid #93c5fd;
        }

        .step-title {
            font-weight: 700;
            color: var(--secondary-navy);
            font-size: 0.88rem;
            margin-bottom: 2px;
        }

        .final-answer-box {
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 6px;
            padding: 12px 16px;
            margin-top: 14px;
            font-weight: 600;
            color: #166534;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* Dedicated Assignment Showcase */
        .assignment-showcase {
            background: #ffffff;
            border: 2px solid #3b82f6;
            border-radius: 10px;
            margin: 24px 0 10px;
            overflow: hidden;
            box-shadow: var(--shadow-md);
        }

        .assignment-banner {
            background: linear-gradient(to right, #1d4ed8, #2563eb);
            color: white;
            padding: 14px 20px;
            font-weight: 700;
            font-size: 0.98rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Comprehensive Cheatsheet section */
        .master-cheatsheet {
            background: white;
            border-radius: 12px;
            border: 1px solid var(--border-light);
            padding: 32px;
            margin-top: 50px;
            box-shadow: var(--shadow-sm);
        }

        /* Page Breaks for Printing */
        @media print {
            body {
                background: white;
                color: black;
                font-size: 11pt;
            }
            .sidebar, .sidebar-tools, .btn-toolbar-group, #btn-print, #btn-toggle-solutions {
                display: none !important;
            }
            .main-wrapper {
                margin-left: 0 !important;
                padding: 0 !important;
                max-width: 100% !important;
            }
            .week-module {
                border: 1px solid #ccc;
                box-shadow: none !important;
                page-break-before: always;
            }
            .page-break {
                page-break-before: always;
            }
            details.solution-drawer {
                display: block !important;
            }
            details.solution-drawer[open] summary ~ * {
                display: block !important;
            }
            details.solution-drawer summary {
                background: #eee !important;
                color: black !important;
            }
            pre.r-code {
                background: #f4f4f4 !important;
                color: #111 !important;
                border: 1px solid #ccc !important;
            }
        }

        /* Responsive Mobile Layout */
        @media (max-width: 900px) {
            .sidebar {
                transform: translateX(-100%);
                width: 260px;
            }
            .sidebar.open {
                transform: translateX(0);
            }
            .main-wrapper {
                margin-left: 0;
                padding: 20px 16px;
            }
            .formula-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<div class="app-container">
    <!-- Sidebar Navigation -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-brand">
                <span>📚</span>
                <span>NPTEL Study Guide</span>
            </div>
            <div class="sidebar-sub">Data Science for Engineers</div>
            <div class="sidebar-instructors">Prof. Shankar Narasimhan &amp; Prof. Ragunathan Rengasamy (IIT Madras)</div>
        </div>

        <div class="sidebar-tools">
            <input type="text" id="navSearch" class="search-box" placeholder="🔍 Search topics, formulas, R code..." onkeyup="filterNav()">
            <div class="btn-toolbar-group">
                <button class="btn-tool" id="btn-toggle-solutions" onclick="toggleAllSolutions()">👁️ Toggle Solutions</button>
                <button class="btn-tool" id="btn-print" onclick="window.print()">🖨️ Print / PDF</button>
            </div>
        </div>

        <ul class="nav-list" id="navList">
            <li class="nav-item">
                <a href="#hero" class="nav-link">
                    <span class="nav-badge">0</span>
                    <span>Course Overview</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week1" class="nav-link">
                    <span class="nav-badge">W1</span>
                    <span>Introduction to R Basics</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week2" class="nav-link">
                    <span class="nav-badge">W2</span>
                    <span>Linear Algebra for Data Science</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week3" class="nav-link">
                    <span class="nav-badge">W3</span>
                    <span>Probability &amp; Statistics</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week4" class="nav-link">
                    <span class="nav-badge">W4</span>
                    <span>Optimization: Univariate</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week5" class="nav-link">
                    <span class="nav-badge">W5</span>
                    <span>Multivariate &amp; Constrained Opt</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week6" class="nav-link">
                    <span class="nav-badge">W6</span>
                    <span>Linear Regression (Simple &amp; Multi)</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week7" class="nav-link">
                    <span class="nav-badge">W7</span>
                    <span>Classification &amp; Logistic Reg</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#week8" class="nav-link">
                    <span class="nav-badge">W8</span>
                    <span>KNN &amp; K-Means Clustering</span>
                </a>
            </li>
            <li class="nav-item">
                <a href="#master-exam-cheatsheet" class="nav-link">
                    <span class="nav-badge">★</span>
                    <span>Exam Day Cheatsheet</span>
                </a>
            </li>
        </ul>
    </aside>

    <!-- Main Content Area -->
    <main class="main-wrapper">
        <!-- Hero Banner -->
        <header class="hero-banner" id="hero">
            <span class="hero-badge">Official Curriculum Companion</span>
            <h1 class="hero-title">Data Science for Engineers</h1>
            <p class="hero-subtitle">
                A rigorous, comprehensive master study guide spanning Weeks 1 through 8. Designed with structured theoretical breakdowns, essential formulas, formatted R function reference tables, topic-wise practice questions with full solutions, and dedicated assignment walkthroughs.
            </p>
            <div class="hero-meta">
                <span>🎓 <strong>Instructors:</strong> Prof. Shankar Narasimhan &amp; Prof. Ragunathan Rengasamy</span>
                <span>🏛️ <strong>Institution:</strong> IIT Madras / NPTEL</span>
                <span>⏱️ <strong>Coverage:</strong> Weeks 1–8 (Complete Course Syllabus)</span>
                <span>💻 <strong>Software:</strong> R Programming Environment</span>
            </div>
        </header>
"""

def assemble_guide():
    parts = []
    print("Adding Header and Styles...")
    parts.append(get_header_and_styles())
    
    print("Adding Week 1: Introduction to R...")
    parts.append(get_week1_content())
    
    print("Adding Week 2: Linear Algebra...")
    parts.append(get_week2_content())
    
    print("Adding Week 3: Probability & Statistics...")
    parts.append(get_week3_content())
    
    print("Adding Week 4: Optimization Univariate...")
    parts.append(get_week4_content())
    
    print("Adding Week 5: Multivariate & Constrained Opt...")
    parts.append(get_week5_content())
    
    print("Adding Week 6: Linear Regression...")
    parts.append(get_week6_content())
    
    print("Adding Week 7: Classification & Logistic Regression...")
    parts.append(get_week7_content())
    
    print("Adding Week 8: KNN & K-Means Clustering...")
    parts.append(get_week8_content())
    
    print("Adding Master Exam Cheatsheet & Footer...")
    parts.append(get_exam_cheatsheet_content())
    
    full_html = "".join(parts)
    
    output_filename = "NPTEL_Data_Science_for_Engineers_Study_Guide.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    file_size_kb = os.path.getsize(output_filename) / 1024
    print(f"Successfully generated {output_filename} ({file_size_kb:.2f} KB)!")

if __name__ == "__main__":
    assemble_guide()

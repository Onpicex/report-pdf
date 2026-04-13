---
name: report-pdf
description: Generate professional A4 PDF reports from structured content using HTML + Playwright. Use when producing research reports, analysis documents, deep-dive studies, or any long-form deliverable as a polished PDF. Triggers on "生成PDF报告", "做成报告", "输出PDF", "research report", "generate PDF", "深度研究报告". NOT for simple screenshots, infographics, or slide decks.
---

# Report PDF

Generate magazine-quality A4 PDF reports via HTML → Playwright Chromium → PDF.

## Design System

Reference template: `assets/report-template.html`

### Layout Rules

- **Page**: A4, margins `15mm 13mm 13mm 13mm` (CSS `@page` + Playwright `margin` must match)
- **No forced page breaks** between chapters — content flows naturally, `page-break-inside: avoid` only on tables/cards
- **Cover page**: centered, gradient top bar, `page-break-after: always`
- **TOC page**: dotted leader lines, `page-break-after: always`
- **Body chapters**: no `page-break-before`, use `.chapter` class with `padding-top: 10px`

### Typography

- Font stack: `-apple-system, "PingFang SC", "Hiragino Sans GB", "Noto Sans SC", sans-serif`
- Body: `10.5pt`, line-height `1.85`
- H2: `18pt`, left red border `4px solid var(--c-accent)`
- H3: `13pt`, bottom border
- Paragraph: `text-align: justify`

### Color Tokens

| Token | Value | Use |
|-------|-------|-----|
| `--c-primary` | `#1a1a2e` | headings, dark accents |
| `--c-accent` | `#c0392b` | left borders, highlight numbers |
| `--c-table-head` | `#2c3e50` | table header bg |
| `--c-bg-light` | `#f7f7f7` | blockquote/card bg |

### Component Classes

| Class | Purpose | Variants |
|-------|---------|----------|
| `.insight-card` | Callout/tip box (blue left border) | `.warn` (orange), `.danger` (red), `.success` (green) |
| `.timeline` + `.timeline-item` | Version/event timeline | — |
| `.vs-grid` + `.vs-box` | Side-by-side comparison | `.left` (blue), `.right` (red) |
| `.num` | Highlight numbers | — |
| `blockquote .trans` | Bilingual quote (EN original + CN translation below dashed line) | — |
| `.methodology` | Footer methodology note | — |
| `.source-table` | Compact source/reference table | — |

### Tables

- Dark header (`--c-table-head` white text), zebra striping on even rows
- Font size `9.5pt`, header `9pt`

## Workflow

1. **Read** `assets/report-template.html` for the full CSS + skeleton
2. **Write** complete HTML by replacing `{{TITLE}}`, `{{TOC_ITEMS}}`, `{{BODY}}` etc.
3. **Generate PDF** via `scripts/html_to_pdf.py`:
   ```bash
   python3 scripts/html_to_pdf.py /path/to/report.html /path/to/output.pdf
   ```
   Or inline Playwright call with matching margins.
4. **Send** the PDF to user.

## Content Guidelines (for Chinese reports)

- All English terms annotated with Chinese: `函数调用（function calling）`
- English quotes preserved with `blockquote .trans` Chinese translation below
- Product/person names keep English
- `<strong>` for key terms, `.num` for standout numbers

## Key Lessons (from iteration)

- **CSS `@page margin` and Playwright `margin` must both be set and match** — if CSS has `margin: 0`, Playwright margin is ignored
- **Never use `page-break-before: always` on chapters** — causes massive whitespace; let content flow
- **Use system font stack** — CID fonts (STSong, SimSun) cause kerning/overlap issues in Playwright
- **Playwright `print_background: True`** is required for colored backgrounds to render

# report-pdf

> 生成专业 A4 PDF 报告的 OpenClaw Skill。HTML + Playwright 排版引擎，杂志级排版质量。

## 效果预览

- 🎨 封面 + 目录 + 彩色洞察卡片 + 斑马纹表格
- 📐 A4 精排，页码页脚，自然分页无大面积空白
- 🀄 中英双语友好，CJK 字体渲染无重叠

## 安装

将整个 `report-pdf/` 目录放到你的 OpenClaw workspace skills 目录：

```bash
git clone https://github.com/Onpicex/report-pdf.git ~/.openclaw/workspace/skills/report-pdf
```

### 依赖

- Python 3
- [Playwright](https://playwright.dev/python/) + Chromium

```bash
pip install playwright
playwright install chromium
```

## 文件结构

```
report-pdf/
├── SKILL.md                    # 设计规范 + 工作流 + 踩坑教训
├── assets/
│   └── report-template.html    # CSS 设计系统 + HTML 骨架模板
└── scripts/
    └── html_to_pdf.py          # Playwright PDF 生成脚本
```

## 使用方式

这是一个 **OpenClaw Agent Skill**——你不需要手动操作，只需对 Agent 说：

- "帮我做个 XX 的深度研究报告，输出 PDF"
- "把这篇内容整理成 PDF 报告"
- "generate a research report on XX"

Agent 会自动读取模板、生成 HTML、转 PDF、发给你。

### 手动使用脚本

```bash
python3 scripts/html_to_pdf.py input.html output.pdf
```

## 设计系统

| 特性 | 说明 |
|------|------|
| 页面 | A4，边距 15/13/13/13mm |
| 字体 | PingFang SC → Noto Sans SC → system fallback |
| 主色 | `#1a1a2e`（深蓝）+ `#c0392b`（红色强调） |
| 组件 | 洞察卡片（蓝/橙/红/绿）、版本时间线、对比双栏、引用翻译块 |

## 踩坑记录

这些教训已写入 SKILL.md，Agent 会自动遵守：

1. **CSS `@page margin` 和 Playwright `margin` 必须同时设置且一致**——否则边距失效
2. **不要用 `page-break-before: always`**——章节间会出现大面积空白
3. **用系统字体栈，别用 CID 字体**——STSong/SimSun 在 Playwright 里会字符重叠
4. **`print_background=True`**——不加这个，彩色背景不渲染

## License

MIT

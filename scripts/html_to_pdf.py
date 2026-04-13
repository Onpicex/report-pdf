#!/usr/bin/env python3
"""
HTML → PDF converter using Playwright (Chromium).
Usage: python3 html_to_pdf.py <input.html> [output.pdf]

If output is omitted, replaces .html with .pdf.
Produces A4 PDF with page numbers and print backgrounds.
"""
import sys, os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 html_to_pdf.py <input.html> [output.pdf]")
        sys.exit(1)

    html_path = os.path.abspath(sys.argv[1])
    if len(sys.argv) >= 3:
        pdf_path = os.path.abspath(sys.argv[2])
    else:
        pdf_path = html_path.rsplit('.', 1)[0] + '.pdf'

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "15mm", "bottom": "13mm", "left": "13mm", "right": "13mm"},
            print_background=True,
            display_header_footer=True,
            header_template='<span></span>',
            footer_template='<div style="font-size:8px;color:#999;text-align:center;width:100%;">— <span class="pageNumber"></span> —</div>'
        )
        browser.close()

    size = os.path.getsize(pdf_path)
    print(f"✅ PDF generated: {pdf_path} ({size:,} bytes)")

if __name__ == "__main__":
    main()

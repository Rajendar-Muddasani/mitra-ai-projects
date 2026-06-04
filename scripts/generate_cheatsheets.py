#!/usr/bin/env python3
"""
Generate cheatsheet PDFs from Markdown source files using reportlab.
Source: content/cheatsheets/*.md
Output: /tmp/cheatsheets/*.pdf (then upload to S3 with upload_project_assets.py)

Run: python scripts/generate_cheatsheets.py [--slug python-basics] [--all]
"""

import argparse
import sys
from pathlib import Path

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted
    from reportlab.lib.units import mm
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
except ImportError:
    print("reportlab not installed. Run: pip install reportlab")
    sys.exit(1)

# ── Design tokens (dark teal theme) ──────────────────────────────────────────
BG_DARK    = HexColor("#0d1117")
SURFACE    = HexColor("#161b22")
PRIMARY    = HexColor("#00d4aa")
ACCENT     = HexColor("#f0b429")
TEXT       = HexColor("#e6edf3")
MUTED      = HexColor("#7d8590")
CODE_BG    = HexColor("#0d1117")
CODE_FG    = HexColor("#a5d6ff")

CONTENT_DIR = Path(__file__).parent.parent / "content" / "cheatsheets"
OUTPUT_DIR  = Path("/tmp/cheatsheets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "h1": ParagraphStyle("h1", fontSize=18, textColor=PRIMARY, spaceAfter=8, fontName="Helvetica-Bold"),
        "h2": ParagraphStyle("h2", fontSize=13, textColor=PRIMARY, spaceAfter=4, fontName="Helvetica-Bold", spaceBefore=8),
        "h3": ParagraphStyle("h3", fontSize=10, textColor=ACCENT, spaceAfter=3, fontName="Helvetica-Bold", spaceBefore=6),
        "body": ParagraphStyle("body", fontSize=8.5, textColor=TEXT, leading=13, fontName="Helvetica"),
        "code": ParagraphStyle("code", fontSize=7.5, textColor=CODE_FG, leading=12, fontName="Courier",
                               backColor=CODE_BG, leftIndent=6, rightIndent=6, spaceBefore=3, spaceAfter=3),
        "muted": ParagraphStyle("muted", fontSize=7.5, textColor=MUTED, fontName="Helvetica"),
    }


def markdown_to_elements(md_text: str, styles: dict) -> list:
    elements = []
    in_code_block = False
    code_lines = []

    for line in md_text.split("\n"):
        # Code block toggle
        if line.startswith("```"):
            if in_code_block:
                elements.append(Preformatted("\n".join(code_lines), styles["code"]))
                elements.append(Spacer(1, 2*mm))
                code_lines = []
            in_code_block = not in_code_block
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            elements.append(Spacer(1, 2*mm))
            continue

        if stripped.startswith("# "):
            elements.append(Paragraph(stripped[2:], styles["h1"]))
        elif stripped.startswith("## "):
            elements.append(Paragraph(stripped[3:], styles["h2"]))
        elif stripped.startswith("### "):
            elements.append(Paragraph(stripped[4:], styles["h3"]))
        elif stripped.startswith("| "):
            # skip table header separator rows
            if set(stripped.replace("|","").replace("-","").strip()) == set():
                continue
            # simple table row — add as body text
            cols = [c.strip() for c in stripped.split("|")[1:-1]]
            elements.append(Paragraph(" | ".join(cols), styles["muted"]))
        elif stripped.startswith("- "):
            elements.append(Paragraph(f"• {stripped[2:]}", styles["body"]))
        elif stripped.startswith("1. ") or (len(stripped) > 2 and stripped[0].isdigit() and stripped[1] == "."):
            elements.append(Paragraph(stripped, styles["body"]))
        else:
            elements.append(Paragraph(stripped, styles["body"]))

    return elements


def generate_pdf(slug: str) -> Path:
    source = CONTENT_DIR / f"{slug}.md"
    if not source.exists():
        print(f"  ⚠  Source not found: {source}")
        return None

    output = OUTPUT_DIR / f"{slug}.pdf"
    md_text = source.read_text(encoding="utf-8")
    styles = build_styles()
    elements = markdown_to_elements(md_text, styles)

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=15*mm,
        rightMargin=15*mm,
        topMargin=15*mm,
        bottomMargin=15*mm,
    )

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BG_DARK)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        # Footer
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(15*mm, 8*mm, "mitraaiprojects.com")
        canvas.drawRightString(A4[0]-15*mm, 8*mm, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=on_page, onLaterPages=on_page)
    print(f"  ✅ Generated: {output}")
    return output


def main():
    parser = argparse.ArgumentParser(description="Generate cheatsheet PDFs")
    parser.add_argument("--slug", help="Specific cheatsheet slug to generate")
    parser.add_argument("--all", action="store_true", help="Generate all cheatsheets")
    args = parser.parse_args()

    if args.slug:
        generate_pdf(args.slug)
    elif args.all:
        sources = list(CONTENT_DIR.glob("*.md"))
        print(f"Generating {len(sources)} cheatsheets...")
        for s in sources:
            generate_pdf(s.stem)
    else:
        parser.print_help()
        print("\nExample: python scripts/generate_cheatsheets.py --slug python-basics")
        print("         python scripts/generate_cheatsheets.py --all")


if __name__ == "__main__":
    main()

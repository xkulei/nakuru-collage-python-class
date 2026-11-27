"""Build a printable PDF from the student Markdown handout."""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "STUDENT_HANDOUT.md"
OUTPUT = HERE / "git_github_student_handout.pdf"

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Consolas", r"C:\Windows\Fonts\consola.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold")

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="DocTitle",
        fontName="Arial-Bold",
        fontSize=19,
        leading=24,
        textColor=colors.HexColor("#183153"),
        spaceAfter=14,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        fontName="Arial-Bold",
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor("#1c4c76"),
        spaceBefore=15,
        spaceAfter=7,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyTextCustom",
        fontName="Arial",
        fontSize=9.3,
        leading=13.2,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletCustom",
        parent=styles["BodyTextCustom"],
        leftIndent=17,
        firstLineIndent=-12,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCellCustom",
        fontName="Arial",
        fontSize=8.1,
        leading=10.5,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHeadCustom",
        parent=styles["TableCellCustom"],
        fontName="Arial-Bold",
        textColor=colors.white,
    )
)
styles.add(
    ParagraphStyle(
        name="CodeCustom",
        fontName="Consolas",
        fontSize=8.1,
        leading=11,
        backColor=colors.HexColor("#f1f5f9"),
        leftIndent=6,
        rightIndent=6,
        borderPadding=6,
        spaceBefore=3,
        spaceAfter=9,
    )
)


def normalize(text: str) -> str:
    return (
        text.replace("–", "-")
        .replace("—", "-")
        .replace("‑", "-")
        .replace("→", "->")
        .replace("─", "-")
        .replace("│", "|")
        .replace("└", "+")
        .replace("▲", "^")
        .replace("“", '"')
        .replace("”", '"')
        .replace("’", "'")
    )


def inline(text: str) -> str:
    text = html.escape(normalize(text))
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        lambda match: f'<link href="{match.group(2)}" color="#1769aa">{match.group(1)}</link>',
        text,
    )
    text = re.sub(r"`([^`]+)`", r'<font name="Consolas">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return text


def make_table(lines: list[str], width: float) -> Table:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    columns = max(map(len, rows))
    # Give the explanation column more room in wide three-column tables.
    if columns == 3:
        widths = [width * 0.19, width * 0.42, width * 0.39]
    elif columns == 2:
        widths = [width * 0.3, width * 0.7]
    else:
        widths = [width / columns] * columns
    data = []
    for index, row in enumerate(rows):
        cell_style = styles["TableHeadCustom"] if index == 0 else styles["TableCellCustom"]
        data.append([Paragraph(inline(cell), cell_style) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1c4c76")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f7fb")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#183153")),
            ]
        )
    )
    return table


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d7e1e9"))
    canvas.line(43, 42, A4[0] - 43, 42)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#526273"))
    canvas.drawString(43, 29, "Git and GitHub - student handout")
    canvas.drawRightString(A4[0] - 43, 29, f"Page {doc.page}")
    canvas.restoreState()


def build() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=43,
        leftMargin=43,
        topMargin=46,
        bottomMargin=58,
        title="Git and GitHub: your first project history",
        author="Python class",
    )
    width = A4[0] - 86
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    story = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith("```"):
            index += 1
            block = []
            while index < len(lines) and not lines[index].startswith("```"):
                block.append(normalize(lines[index]))
                index += 1
            story.append(Preformatted("\n".join(block), styles["CodeCustom"] ))
            index += 1
            continue
        if line.startswith("|"):
            block = []
            while index < len(lines) and lines[index].startswith("|"):
                block.append(lines[index])
                index += 1
            story.append(make_table(block, width))
            story.append(Spacer(1, 8))
            continue
        if line.startswith("---"):
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#d7e1e9")))
            index += 1
            continue
        if line.startswith("# "):
            story.append(Paragraph(inline(line[2:]), styles["DocTitle"]))
            index += 1
            continue
        if line.startswith("## "):
            story.append(Paragraph(inline(line[3:]), styles["Section"]))
            index += 1
            continue
        if line.startswith("- ") or re.match(r"^\d+\. ", line):
            marker = "-" if line.startswith("- ") else line.split(".", 1)[0] + "."
            content = line[2:] if marker == "-" else line[len(marker) + 1 :]
            story.append(Paragraph(inline(content), styles["BulletCustom"], bulletText=marker))
            index += 1
            continue
        paragraph = [line]
        index += 1
        while index < len(lines) and lines[index].strip() and not (
            lines[index].startswith(("#", "|", "```", "- ", "---"))
            or re.match(r"^\d+\. ", lines[index])
        ):
            paragraph.append(lines[index])
            index += 1
        story.append(Paragraph(inline(" ".join(paragraph)), styles["BodyTextCustom"]))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    build()

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import json
import textwrap

def create_pdf(occasion, menu):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)  # Use A4 page size

    # Register a font
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))  # Replace with your font file.
    c.setFont('Arial', 12)

    width, height = A4  # Get A4 page dimensions
    margin = 1 * inch  # Margin around the page

    c.drawString(margin, height - margin, f"Menu for: {occasion}")

    y = height - margin - 1 * inch  # Start drawing below the occasion
    line_height = 0.25 * inch  # Adjust line height as needed
    item_margin_left = margin + 0.2 * inch  # Indent items
    text_width = width - 2 * margin  # Available width for text

    if isinstance(menu, str):
        try:
            menu_dict = json.loads(menu)
            for category, items in menu_dict.items():
                c.drawString(margin, y, category)
                y -= 0.5 * inch

                if isinstance(items, list):
                    for item in items:
                        lines = textwrap.wrap(f"• {item}", width=int(text_width / (72 / 12)))
                        for line in lines:
                            c.drawString(item_margin_left, y, line)
                            y -= line_height
                else:
                    lines = textwrap.wrap(items, width=int(text_width / (72 / 12)))
                    for line in lines:
                        c.drawString(item_margin_left, y, line)
                        y -= line_height
        except (json.JSONDecodeError, TypeError):
             lines = textwrap.wrap(menu, width=int(text_width / (72 / 12)))
             for line in lines:
                c.drawString(margin, y, line)
                y -= line_height

    else:
        lines = textwrap.wrap(str(menu), width=int(text_width / (72 / 12)))
        for line in lines:
            c.drawString(margin, y, line)
            y -= line_height

    c.save()
    buffer.seek(0)
    return buffer.getvalue()
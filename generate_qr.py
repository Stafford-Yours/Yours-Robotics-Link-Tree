#!/usr/bin/env python3
"""
Yours Robotics - QR Code Generator for Robot 82 Linktree
Usage:
    python3 generate_qr.py [--url <URL>] [--output <path>]
Example:
    python3 generate_qr.py --url "https://staffordho.github.io/yours/"
"""

import argparse
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

DEFAULT_URL = "https://stafford-yours.github.io/Yours-Robotics-Link-Tree/?token=yours82_open_lid"
DEFAULT_OUTPUT = os.path.join(os.path.dirname(__file__), "robot82_qr_code.png")

def generate_qr(url=DEFAULT_URL, output_path=DEFAULT_OUTPUT):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QR Code inside card
    qr_img = qr.make_image(fill_color="#0f172a", back_color="#ffffff").convert("RGBA")
    qr_w, qr_h = qr_img.size

    # Card canvas with high-DPI dimensions
    card_w = qr_w + 120
    card_h = qr_h + 200
    card = Image.new("RGBA", (card_w, card_h), "#ffffff")
    draw = ImageDraw.Draw(card)

    # Top dark header banner
    draw.rectangle([(0, 0), (card_w, 100)], fill="#0b0f19")

    # Fonts
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 34)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        font_bot = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except Exception:
        font_title = font_sub = font_bot = ImageFont.load_default()

    # Draw Branding Header
    draw.text((card_w // 2, 38), "YOURS ROBOTICS", fill="#38bdf8", font=font_title, anchor="mm")
    draw.text((card_w // 2, 74), "ROBOT A0082 • SCAN & UNLOCK", fill="#94a3b8", font=font_sub, anchor="mm")

    # Paste QR Code
    card.paste(qr_img, (60, 115))

    # Bottom Instructions
    draw.text((card_w // 2, card_h - 60), "Follow to Open Compartment", fill="#0f172a", font=font_title, anchor="mm")
    draw.text((card_w // 2, card_h - 25), "Instagram • YouTube • LinkedIn", fill="#64748b", font=font_bot, anchor="mm")

    # Save styled card
    card.save(output_path, "PNG")
    print(f"[✓] Successfully saved styled QR card: {output_path} ({card_w}x{card_h})")

    # Also save clean square QR without card borders
    raw_path = output_path.replace(".png", "_raw.png")
    qr_clean = qr.make_image(fill_color="#000000", back_color="#ffffff").convert("RGBA")
    qr_clean.save(raw_path, "PNG")
    print(f"[✓] Successfully saved raw high-DPI QR: {raw_path} ({qr_w}x{qr_h})")

    return output_path, raw_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Robot 82 QR Code for Yours Robotics Linktree")
    parser.add_argument("--url", default=DEFAULT_URL, help="Target Linktree URL")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output PNG path")
    args = parser.parse_args()

    generate_qr(args.url, args.output)

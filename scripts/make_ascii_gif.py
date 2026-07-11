import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, "..", "WhatsApp Video 2026-07-12 at 00.30.41.mp4")
OUT = os.path.join(HERE, "..", "avi-ascii.gif")

COLS = 100
ROWS = 53
CELL_W = 8
CELL_H = 15
RAMP = " .`:-=+*cs#%@"

# Tuning parameters
CONTRAST = 1.3
BRIGHTNESS = 1.05
GAMMA = 1.15
WHITE_FLOOR = 0.83

PAD = 20
TITLEBAR_H = 30
STATUS_H = 30
ART_W = COLS * CELL_W
ART_H = ROWS * CELL_H
CANVAS_W = ART_W + PAD * 2
CANVAS_H = TITLEBAR_H + ART_H + STATUS_H + PAD

BG = (13, 17, 23)      # #0d1117
BG2 = (17, 23, 34)     # #111722
FRAME = (48, 54, 61)   # #30363d
TITLE_TEXT = (125, 133, 144)  # #7d8590
INK = (201, 209, 217)   # #c9d1d9

# Load font
try:
    font = ImageFont.truetype("consola.ttf", 12)
except IOError:
    font = ImageFont.load_default()

# Open video
cap = cv2.VideoCapture(INP)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Loaded video: {total_frames} frames, {fps} FPS")

# Downsample to ~10 FPS (take every 3rd frame)
# We will process 90 frames maximum to keep size small (~3 seconds)
frame_indices = range(0, min(total_frames, 90), 3)

gif_frames = []

for f_idx in frame_indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
    ret, frame = cap.read()
    if not ret:
        break
    
    # 1. Grayscale and contrast boosting
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # local-contrast (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.4, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    
    # Convert to PIL
    pil_im = Image.fromarray(gray)
    pil_im = ImageEnhance.Contrast(pil_im).enhance(CONTRAST)
    pil_im = ImageEnhance.Brightness(pil_im).enhance(BRIGHTNESS)
    
    # Resize to COLS x ROWS
    pil_im = pil_im.resize((COLS, ROWS), Image.Resampling.LANCZOS)
    px = pil_im.load()
    
    # Convert pixels to ASCII chars
    ascii_rows = []
    for y in range(ROWS):
        chars = []
        for x in range(COLS):
            lum = px[x, y] / 255.0
            lum = pow(lum, GAMMA)
            if lum >= WHITE_FLOOR:
                chars.append(" ")
                continue
            idx = int((1.0 - lum) * (len(RAMP) - 1) + 0.5)
            idx = max(0, min(len(RAMP) - 1, idx))
            chars.append(RAMP[idx])
        ascii_rows.append("".join(chars))
        
    # Draw terminal frame
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), BG)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([0, 0, CANVAS_W - 1, CANVAS_H - 1], outline=FRAME)
    draw.line([0, TITLEBAR_H, CANVAS_W, TITLEBAR_H], fill=FRAME)
    
    # Titlebar dots
    dots = [(255, 95, 86), (255, 189, 46), (39, 201, 63)] # red, yellow, green
    for i, dotcol in enumerate(dots):
        cx = PAD + i * 16
        cy = TITLEBAR_H // 2
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=dotcol)
        
    # Titlebar text
    draw.text((CANVAS_W // 2, TITLEBAR_H // 2 - 6), "ishaan@github: ~$ ./portrait.sh", fill=TITLE_TEXT, font=font, anchor="mm")
    
    # Draw ASCII lines
    art_top = TITLEBAR_H + PAD * 0.35
    for ry, line in enumerate(ascii_rows):
        y_pos = art_top + ry * CELL_H
        draw.text((PAD, y_pos), line, fill=INK, font=font)
        
    # Status bar
    status_line_y = TITLEBAR_H + ART_H + PAD * 0.35
    draw.line([0, status_line_y, CANVAS_W, status_line_y], fill=FRAME)
    
    status_y = status_line_y + 6
    draw.text((PAD, status_y), "ishaan@github:~$ whoami ", fill=TITLE_TEXT, font=font)
    draw.text((PAD + 185, status_y), "Ishaan", fill=INK, font=font)
    
    # Blinking cursor simulation
    if (f_idx // 3) % 2 == 0:
        draw.rectangle([PAD + 234, status_y, PAD + 242, status_y + 14], fill=INK)
        
    gif_frames.append(img)

cap.release()

# Save as animated GIF
if gif_frames:
    gif_frames[0].save(
        OUT,
        save_all=True,
        append_images=gif_frames[1:],
        duration=100,  # 10 FPS
        loop=0
    )
    print(f"Successfully wrote animated ASCII GIF to {OUT}")
else:
    print("No frames processed!")

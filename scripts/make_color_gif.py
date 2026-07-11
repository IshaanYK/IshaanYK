import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, "..", "WhatsApp Video 2026-07-12 at 00.30.41.mp4")
OUT = os.path.join(HERE, "..", "color-loop.gif")

COLS = 100
ROWS = 53
CELL_W = 8
CELL_H = 15

PAD = 20
TITLEBAR_H = 30
STATUS_H = 30
ART_W = COLS * CELL_W # 800
ART_H = ROWS * CELL_H # 795
CANVAS_W = ART_W + PAD * 2 # 840
CANVAS_H = TITLEBAR_H + ART_H + STATUS_H + PAD # 875

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

print(f"Loaded video for color loop: {total_frames} frames, {fps} FPS")

# Downsample to ~10 FPS (take every 3rd frame)
# We will process 90 frames maximum to keep size small (~3 seconds)
frame_indices = range(0, min(total_frames, 90), 3)

gif_frames = []

for f_idx in frame_indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert BGR (OpenCV) to RGB (PIL)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, c = frame_rgb.shape
    
    # Center crop to target aspect ratio (ART_W / ART_H)
    target_ratio = ART_W / ART_H
    current_ratio = w / h
    
    if current_ratio > target_ratio:
        # Image is wider than target ratio: crop sides
        crop_w = int(h * target_ratio)
        start_x = (w - crop_w) // 2
        cropped = frame_rgb[:, start_x:start_x+crop_w]
    else:
        # Image is taller than target ratio: crop top/bottom
        crop_h = int(w / target_ratio)
        start_y = (h - crop_h) // 2
        cropped = frame_rgb[start_y:start_y+crop_h, :]
        
    # Resize to ART_W x ART_H
    resized = cv2.resize(cropped, (ART_W, ART_H), interpolation=cv2.INTER_AREA)
    pil_resized = Image.fromarray(resized)
    
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
    draw.text((CANVAS_W // 2, TITLEBAR_H // 2 - 6), "ishaan@github: ~$ ./play_video.sh", fill=TITLE_TEXT, font=font, anchor="mm")
    
    # Paste video frame
    art_top = TITLEBAR_H + PAD * 0.35
    img.paste(pil_resized, (PAD, int(art_top)))
    
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
    print(f"Successfully wrote color looping GIF to {OUT}")
else:
    print("No frames processed!")

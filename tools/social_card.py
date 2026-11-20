#!/usr/bin/env python3
"""Makes site/images/social-card.jpg (1200 x 630), the link preview for WhatsApp, social media and chat apps,
from Emily's headshot (© YellowBellyPhoto) with her name. Needs Pillow and the Liberation fonts."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parent.parent
F = "/usr/share/fonts/truetype/liberation/"
W, H, BG, GOLD = 1200, 630, (34, 6, 11), (233, 200, 119)
src = Image.open(ROOT / "site/images/headshot-1400.webp").convert("RGB")
crop = src.crop((0, round(src.height * .02), src.width, round(src.height * .74)))
crop = crop.resize((round(crop.width * H / crop.height), H), Image.LANCZOS)
x0 = W - crop.width + 60
im = Image.new("RGB", (W, H), BG)
im.paste(crop, (x0, 0))
mask = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(mask)
for x in range(W):
    d.line([(x, 0), (x, H)], fill=255 if x < x0 else max(0, 255 - int((x - x0) * 255 / 360)))
im = Image.composite(Image.new("RGB", (W, H), BG), im, mask)
d = ImageDraw.Draw(im)
d.text((70, 150), "BA (HONS) ACTOR-MUSICIAN, GSA 2026", font=ImageFont.truetype(F + "LiberationSans-Bold.ttf", 24), fill=GOLD)
d.text((66, 200), "Emily", font=ImageFont.truetype(F + "LiberationSerif-Bold.ttf", 150), fill=(255, 255, 255))
d.text((150, 350), "Cruz", font=ImageFont.truetype(F + "LiberationSerif-Italic.ttf", 150), fill=GOLD)
d.text((72, 520), "Actor-musician and artist", font=ImageFont.truetype(F + "LiberationSerif-Italic.ttf", 40), fill=(244, 230, 211))
d.rectangle((0, H - 10, W, H), fill=(142, 20, 36))
d.text((W - 330, 18), "Photo © YellowBellyPhoto", font=ImageFont.truetype(F + "LiberationSans-Regular.ttf", 20), fill=(255, 255, 255))
out = ROOT / "site/images/social-card.jpg"
im.save(out, "JPEG", quality=84, optimize=True, progressive=True)
print(out, out.stat().st_size // 1024, "KB")

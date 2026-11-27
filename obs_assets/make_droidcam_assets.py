from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

OUT = Path(__file__).resolve().parent
W, H, SCALE = 1920, 1080, 4
CX, CY, R = W // 2, H // 2, 500

mask = Image.new("RGBA", (W * SCALE, H * SCALE), (0, 0, 0, 0))
draw = ImageDraw.Draw(mask)
draw.ellipse(((CX - R) * SCALE, (CY - R) * SCALE,
              (CX + R) * SCALE, (CY + R) * SCALE), fill=(255, 255, 255, 255))
mask.resize((W, H), Image.Resampling.LANCZOS).save(OUT / "droidcam_circle_mask.png")

ring = Image.new("RGBA", (W * SCALE, H * SCALE), (0, 0, 0, 0))
draw = ImageDraw.Draw(ring)
outer = R + 14
inner = R + 1
draw.ellipse(((CX - outer) * SCALE, (CY - outer) * SCALE,
              (CX + outer) * SCALE, (CY + outer) * SCALE), fill=(255, 255, 255, 255))
draw.ellipse(((CX - inner) * SCALE, (CY - inner) * SCALE,
              (CX + inner) * SCALE, (CY + inner) * SCALE), fill=(0, 0, 0, 0))
ring = ring.resize((W, H), Image.Resampling.LANCZOS)
glow = ring.filter(ImageFilter.GaussianBlur(16))
glow.putalpha(glow.getchannel("A").point(lambda a: int(a * 0.35)))
glow.alpha_composite(ring)
glow.save(OUT / "droidcam_circle_border.png")

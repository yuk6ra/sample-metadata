import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

SUPPLY = 100

for i in range(SUPPLY):
    token_id = i + 1
    text = f"Sample #{token_id}"
    fontsize = 50
    backgroundRGB = (255, 255, 255)

    img = PIL.Image.new('RGB', (300, 300), backgroundRGB)
    draw = PIL.ImageDraw.Draw(img)

    font = PIL.ImageFont.truetype("arial.ttf", size=fontsize)

    draw.text((20,150), text, fill=(0, 0, 0), font=font)

    img.save(f"../images/{token_id}.png")

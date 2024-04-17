from PIL import Image, ImageDraw, ImageFont

image = Image.open('img/img-1.jpg')

d = ImageDraw.Draw(image)
font = ImageFont.truetype('fonts/fot-1.ttf', 44)

text = "Begzod Xurramov"
text_pos = (295,410)
color = (36,27,113)

d.text((296,410), text=text, fill=color, font=font)
d.text((295,411), text=text, fill=color, font=font)

image.save("test1.png")


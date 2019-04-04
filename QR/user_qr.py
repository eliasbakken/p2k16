from PIL import Image, ImageDraw, ImageFont
import qrcode

USER_URL="https://p2k16.bitraf.no/#!/user/"
user_id="100167"
name="Elias"
telephone="46052714"
email="elias.bakken@gmail.com"
offset_x = 40
offset_y = 370

im = qrcode.make(USER_URL+user_id)

background = Image.new('RGBA', (370, 480), (255, 255, 255, 255))

background.paste(im, (0, 0))
draw = ImageDraw.Draw(background)

# get a font
fnt = ImageFont.truetype('Helvetica.ttf', 20)

# draw text, half opacity
draw.text((offset_x,offset_y), "Name: {}".format(name), font=fnt, fill=(0,0,0,255))
draw.text((offset_x,offset_y + 30), "Phone: {}".format(telephone), font=fnt, fill=(0,0,0,255))
draw.text((offset_x,offset_y + 60), "Email: {}".format(email), font=fnt, fill=(0,0,0,255))

del draw

# write to stdout
background.save("user.png")

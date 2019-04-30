#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import qrcode
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster
import paho.mqtt.client as mqtt
import json

USER_URL="https://p2k16.bitraf.no/#!/user/"

offset_x = 40
offset_y = 360
picture_height=470
picture_width=370

model="QL-1060N"
backend="network"
printer="tcp://10.13.37.201"

mqtt_topic="/public/p2k16-dev/label/#"

def make_label(user_id, username, name, telephone, email):
	im = qrcode.make(USER_URL+str(user_id))
	background = Image.new('RGBA', (picture_width, picture_height), (255, 255, 255, 255))
	background.paste(im, (0, 0))
	draw = ImageDraw.Draw(background)
	fnt = ImageFont.truetype('Helvetica.ttf', 16)
	draw.text((offset_x,offset_y), "User name: {}".format(username), font=fnt, fill=(0,0,0,255))
	draw.text((offset_x,offset_y + 20), "Name: {}".format(name), font=fnt, fill=(0,0,0,255))
	draw.text((offset_x,offset_y + 40), "Phone: {}".format(telephone), font=fnt, fill=(0,0,0,255))
	draw.text((offset_x,offset_y + 60), "Email: {}".format(email), font=fnt, fill=(0,0,0,255))
	background.save("user.png")

def print_label():
	qlr = BrotherQLRaster(model)
	qlr.exception_on_warning = True
	kwargs = {}
	kwargs['cut'] = True
	kwargs['images'] = ["user.png"]
	kwargs['label'] = "102"
	instructions = convert(qlr=qlr, **kwargs)
	send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)

def on_connect(client, userdata, flags, rc):
	client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
	user = json.loads(msg.payload)
	make_label(user["id"], user["username"], user["name"], user["phone"], user["email"])
	print_label()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.bitraf.no", 1883, 60)

client.loop_forever()
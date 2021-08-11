from PIL import Image, ImageDraw, ImageFont
import os
import smbus
import subprocess
import time

DISPLAY_OFF_TIMEOUT = 30

i2c0_bus = smbus.SMBus(0)  # access to OLED
cmd_index = 0
current_time = time.time()
display_refresh_time = 0
display_off_time = current_time + DISPLAY_OFF_TIMEOUT
image = Image.new("1", (128, 64))
image_draw = ImageDraw.Draw(image)
image_font8 = ImageFont.truetype("DejaVuSansMono.ttf", 8)
image_font10 = ImageFont.truetype("DejaVuSansMono.ttf", 10)
image_font15 = ImageFont.truetype("DejaVuSansMono.ttf", 15)
image_font25 = ImageFont.truetype("DejaVuSansMono.ttf", 25)




try:
    with open("/sys/class/gpio/export", "w") as file:
		file.write("0\n")  # initialise GPIO 0 (key1)
	with open("/sys/class/gpio/export", "w") as file:
		file.write("2\n")  # initialise GPIO 2 (key2)
	with open("/sys/class/gpio/export", "w") as file:
		file.write("3\n")  # initialise GPIO 3 (key3)
	with open("/sys/class/gpio/gpio0/direction", "w") as file:
		print("aaa")
	with open("/sys/class/gpio/gpio2/direction", "w") as file:
		print("bbb")
	with open("/sys/class/gpio/gpio3/direction", "w") as file:
		print("ccc")
#	i2c0_bus.write_i2c_block_data(0x3C,0x00,[0xAF])


	while True:
		with open("/sys/class/gpio/gpio0/value") as file:
			if file.read(1) == "1":
				print ("butao 01 ligado")

		with open("/sys/class/gpio/gpio2/value") as file:
			if file.read(1) == "1":
				print ("butao 02 ligado")
				time.sleep(0.3)
		with open("/sys/class/gpio/gpio3/value") as file:
			if file.read(1) == "1":
				print ("butao 03 ligado")
			#	exit(0)
				time.sleep(0.3)





except KeyboardInterrupt:
	print(" CTRL+C detected")

finally:
	i2c0_bus.write_i2c_block_data(0x3C, 0x00, [0xAE])  # set display off
	with open("/sys/class/gpio/unexport", "w") as file:
		file.write("0\n")  # release GPIO 0 (key1)
	with open("/sys/class/gpio/unexport", "w") as file:
		file.write("2\n")  # release GPIO 2 (key2)
	with open("/sys/class/gpio/unexport", "w") as file:
		file.write("3\n")  # release GPIO 3 (key3)

	if cmd_index == 99:  # shutdown now if the command index was 99
		os.system("shutdown now")
	else:
		exit(0)



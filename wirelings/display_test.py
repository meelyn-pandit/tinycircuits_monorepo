import time
import board
import busio
from digitalio import DigitalInOut
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import tinycircuits_wireling
wireling = tinycircuits_wireling.Wireling()

# create i2c interface
i2c = busio.I2C(board.SCL, board.SDA)

# wireling port
port = 0
reset_pin = DigitalInOut(wireling.getBoardPin(port))
wireling.selectPort(port)

display = adafruit_ssd1306.SSD1306_I2C(96, 16, i2c, addr=0x3c, reset=reset_pin)

# clear display
display.fill(0)
display.show()

#Set a pixel in the origin 0,0 position
#display.pixel(0, 0, 1)
#display.show()
#time.sleep(1)

# Set a pixel in the middle 64, 16 position
#display.pixel(64, 16, 1)
#display.show()
#time.sleep(1)

#Set a pixel in the opposite 127, 31 position
#display.pixel(127, 31, 1)
#display.show
#display.fill(0)

#Draw text
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

draw.text((0,0), "Hellow!", fill=255)

display.image(image)
display.show()

#Clear display after function done
display.fill(0)
display.show()

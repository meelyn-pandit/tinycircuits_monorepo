# SSD1306 Screen Example
# Displays pixels, lines, shapes, and text to demonstrate displaying basics
# Author: Laverena Wienclaw for TinyCircuits

# Import all board pins.
import time
import board
import busio
from digitalio import DigitalInOut
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

import tinycircuits_wireling
wireling = tinycircuits_wireling.Wireling() # Enable and power Wireling Pi Hat

port = 0 # IMPORTANT: Select ports 0-3
reset_pin = DigitalInOut(wireling.getBoardPin(port)) # A reset line to reset circuitry
wireling.selectPort(port) 

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# The I2C address for these displays is 0x3d or 0x3c, change to match
# A reset line may be required if there is no auto-reset circuitry
#display = adafruit_ssd1306.SSD1306_I2C(72, 40, i2c, addr=0x3c, reset=reset_pin) # 0.42" Screen
#display = adafruit_ssd1306.SSD1306_I2C(96, 16, i2c, addr=0x3c, reset=reset_pin) # 0.69" Screen
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c, reset=reset_pin) # 0.96" Screen

# ----------------------------------------------------------

print("Pixel test")
# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
time.sleep(3)
#display.show()

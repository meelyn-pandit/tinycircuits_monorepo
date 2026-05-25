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
# Toggle Reset pin
print("reset pin", reset_pin)

print("Pixel test")
# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle position.
display.pixel(display.width//2, display.height//2, 1)
# Set a pixel in the opposite corner position.
display.pixel(display.width-1, display.height-1, 1)
display.show()
time.sleep(1)

# ----------------------------------------------------------

print("Lines test")
# we'll draw from corner to corner, lets define all the pair coordinates here
corners = ((0, 0), (0, display.height-1), (display.width-1, 0),
           (display.width-1, display.height-1))

display.fill(0)
for corner_from in corners:
    for corner_to in corners:
        display.line(corner_from[0], corner_from[1],
                     corner_to[0], corner_to[1], 1)
display.show()
time.sleep(1)

# ----------------------------------------------------------

print("Rectangle test")
display.fill(0)
w_delta = display.width / 10
h_delta = display.height / 10
for i in range(11):
    display.rect(0, 0, int(w_delta*i), int(h_delta*i), 1)
display.show()
time.sleep(1)

# ----------------------------------------------------------

print("Text test")
# Create blank image for drawing.
display.fill(0)
image = Image.new('1', (display.width, display.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
font2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)

# Draw the text
draw.text((0, 0), 'Hello!', font=font2, fill=255)
#draw.text((0, 30), 'Hello!', font=font2, fill=255)
#draw.text((34, 46), 'Hello!', font=font2, fill=255)

# Display image
display.image(image)
display.show()

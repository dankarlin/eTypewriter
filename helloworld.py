""""Module that operates the typewriter."""
#!/usr/bin/python
# -*- coding:utf-8 -*-

#!.venv/bin/python
import sys
import io
import keyboard
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from working_test_functions import display_image_8bpp_memory
from IT8951.display import AutoEPDDisplay

print('Initializing EPD...')

# here, spi_hz controls the rate of data transfer to the device, so a higher
# value means faster display refreshes. the documentation for the IT8951 device
# says the max is 24 MHz (24000000), but my device seems to still work as high as
# 80 MHz (80000000)
display = AutoEPDDisplay(vcom=-1.70, rotate='CCW', spi_hz=24000000)

# Ensure this matches your particular screen
WIDTH = 1872
HEIGHT = 1404

# Define font size
FONTSIZE = 80

# Define locations
X_OFFSET=0
Y_OFFSET=0

# Colors
BACKGROUND = (255, 255, 255)
FOREGROUND = (0, 0, 0)

# Font
FONT_FILEPATH = '/usr/share/fonts/TTF/DejaVuSans.ttf'

TEXT = ""

font = ImageFont.truetype(FONT_FILEPATH, size=FONTSIZE)

#Debugging display
print('VCOM set to', display.epd.get_vcom())

while 1:

    # capture with record and add new loop for each space
    recorded = keyboard.record('space')
    RECORDEDSTR = ''.join(list(keyboard.get_typed_strings(recorded)))

    # capture with keyboard read
    #recordedstr = keyboard.read_key(suppress=True)
    #recordedstr = recordedst.replace("space", " ")
    #print (recordedstr)

    TEXT = TEXT + RECORDEDSTR

    # Draw image
    img = Image.new("RGBA", font.getmask(TEXT).size, BACKGROUND)
    draw = ImageDraw.Draw(img)
    draw_point = (0, 0)
    draw.multiline_text(draw_point, TEXT, font=font, fill=FOREGROUND)
    text_window = img.getbbox()
    img = img.crop(text_window)

    # Save file in memory only
    buf = io.BytesIO()
    img.save(buf, format='PNG')

    # Display image from memory
    display_image_8bpp_memory(display, buf)

sys.exit()

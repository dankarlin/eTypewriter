#!/usr/bin/python
# -*- coding:utf-8 -*-

#!.venv/bin/python
import os, sys, random, time, io, queue, keyboard
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from working_test_functions import *

from IT8951.display import AutoEPDDisplay

print('Initializing EPD...')

# here, spi_hz controls the rate of data transfer to the device, so a higher
# value means faster display refreshes. the documentation for the IT8951 device
# says the max is 24 MHz (24000000), but my device seems to still work as high as
# 80 MHz (80000000)
display = AutoEPDDisplay(vcom=-1.70, rotate='CCW', spi_hz=24000000)

# Ensure this matches your particular screen 
width = 1872
height = 1404

# Define font size
fontsize = 80

# Define locations
x_offset=0 
y_offset=0

# Colors
background = (255, 255, 255)
foreground = (0, 0, 0)

# Font
font_filepath = '/usr/share/fonts/TTF/DejaVuSans.ttf'
    
text = ""

#Debugging display
print('VCOM set to', display.epd.get_vcom())

while 1: 
    # read console input and append on enter
    # print ("enter text")
    #recorded = input()
    
    #capture with record and add new loop for each space
    recorded = keyboard.record('space')
    recordedstr = ''.join(list(keyboard.get_typed_strings(recorded)))
    
    #recordedstr = keyboard.read_key(suppress=True)
    #recordedstr = recordedst.replace("space", " ")
    #print (recordedstr)
    
    text = text + recordedstr

    # Draw image
    font = ImageFont.truetype(font_filepath, size=fontsize)
    img = Image.new("RGBA", font.getmask(text).size, background)
    draw = ImageDraw.Draw(img)
    draw_point = (0, 0)
    draw.multiline_text(draw_point, text, font=font, fill=foreground)
    #draw.multiline_text(draw_point, text, font=font, fill=foreground)
    text_window = img.getbbox()
    img = img.crop(text_window)

    # Save file to disk
    #img = img.save ('image.png')

    # Save file in memory only
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    #byte_im = buf.getvalue()

    # Display the image from disk
    # display_image_8bpp(display, 'image.png')

    # Display image from memory
    display_image_8bpp_memory(display, buf)

    #Debug text
    # print('Diplaying image')

    # Wait for 10 seconds 
    #time.sleep(10)
    
exit()
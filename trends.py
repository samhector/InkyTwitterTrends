#!/usr/bin/python3

#-----------------------------------------------------------------------
#
# Original Twitter Trends script by Daniel Jones <d.jones@gold.ac.uk> http://www.erase.net
#
# https://github.com/ideoforms/python-twitter-examples
#
# Script modified to display on Inky pHAT by @samhector
#
#-----------------------------------------------------------------------

import argparse
from twitter import *
from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from inky.auto import auto
inky_display = auto()
inky_display.set_border(inky_display.WHITE)

#-----------------------------------------------------------------------
# load Twitter API credentials from config.py
#-----------------------------------------------------------------------

import sys
sys.path.append(".")
import config


#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# Set some information about our Inky PHAT screen
# You can change the colour if you want, but it's not used
#-----------------------------------------------------------------------

scale_size = 1
padding = 0

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(HankenGroteskMedium, 20)

#-----------------------------------------------------------------------
# Retrieve localised trends. The current value is for the UK.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------

results = twitter.trends.place(_id = config.PlaceID)

trends_string = ""

for location in results:
    for trend in location["trends"][0:5]:
        trends_string += " - %s" % trend["name"] + "\n"

x = 0
y = 0

draw.text((x, y), trends_string, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()

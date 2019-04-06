# InkyTwitterTrends
Pulls locally trending Twitter topics and displays them on a [Pimoroni Inky pHAT](https://shop.pimoroni.com/products/inky-phat)

Original Twitter Trends script by @ideoforms

https://github.com/ideoforms/python-twitter-examples

Script modified to display on Inky pHAT by @samhector

# Setup
## Twitter Dev Account

You'll need a Developer Twitter account. You can apply for access here: https://developer.twitter.com 

They approved my application within a few hours. Once that's been approved, set up a new App and generate an Access token & access token secret. Put these into the config.py file.

## Raspberry Pi and Inky pHAT

Set up a Raspberry Pi with the latest Raspbian and follow the getting started with [Inky pHAT turorial](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat) over at Pimoroni. 

## Script customisation

Edit the location ID in trends.py to display info from the geography you're interested in. By default it's the UK.

Not sure if this is important or not, but you can edit the colour or size of the screen depending on which Inky model you have. If you have the larger one, you might also like to edit the number of results it pulls in to increase it from 5.

## CRON it

Make the script executable by using `chmod +x trends.py`
Then use `crontab -e` to have it execute at regular intervals. I use 15 minutes, but it's a balance of up-to-date data, and preserving the life of your display. 
So, paste this in (change the path) and save your new crontab: `*/15 * * * * /path/to/trends.py`

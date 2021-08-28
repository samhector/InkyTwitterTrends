# InkyTwitterTrends

https://user-images.githubusercontent.com/9306929/131224984-ba4ed0ff-a494-4b6b-84ee-f726e7e35a6e.mov

Pulls locally trending Twitter topics and displays them on a [Pimoroni Inky pHAT](https://shop.pimoroni.com/products/inky-phat)

Original Twitter Trends script by [@ideoforms](https://github.com/ideoforms/) - https://github.com/ideoforms/python-twitter-examples

Script modified to display on Inky pHAT by [@samhector](https://twitter.com/samhector)

# Setup
## Twitter Dev Account

You'll need a Developer Twitter account. You can apply for access here: https://developer.twitter.com 

Once that's been approved, set up a new App and generate your Consumer Keys (API Key & Secret) and Authentication Tokens (Access token & access token secret). 

Put these into the config.py file.

## Raspberry Pi and Inky pHAT

Set up a Raspberry Pi with the latest Raspbian and follow the [Getting Started with Inky pHAT turorial](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat) over at Pimoroni. 

## Script customisation

Edit the location ID in trends.py to display info from the geography you're interested in. By default it's the UK.

Not sure if this is important or not, but you can edit the colour or size of the screen depending on which Inky model you have. If you have the larger one, you might also like to edit the number of results it pulls in to increase it from 5.

## Install the requirements

Using `pip3 install -r requirements.txt`

## Check it works!

Run it using `python3 trends.py`

## Cron it - to make the screen refresh with the latest data regularly

Make the script executable by using `chmod +x trends.py`

Then use `crontab -e` to have it execute at regular intervals. I use 15 minutes, but it's a balance of up-to-date data, and preserving the life of your display. 

So, paste this in (change the path) and save your new crontab: `*/15 * * * * /path/to/trends.py`

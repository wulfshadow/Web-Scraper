# Web-Scraper
In order for Twilio to send you a message when the scraper detects a change, you must either enter your twilio number, your personal number, your account SID, and your account token in place of the corresponding variables, or create a new file to import these numbers from, and change "varscraper" in "from varscraper import *" to the name of this new file.

I didn't get to adding options to my scraper, but by default the scraper chacks for changes every 10 seconds. However, the github page also takes a while to update after a change, so it comes out to somewhere around 30 seconds in all.

import bs4
from bs4 import BeautifulSoup
import requests
import html2text
import time
from varscraper import *
from twilio.rest import Client

page_link = "https://wulfshadow.github.io/Holiday-Contest/"

client = Client(acct_sid, auth_token)

def get_text():
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    text = str(page_content)
    raw_text = html2text.html2text(text)
    return(raw_text)

current_text = get_text()

while True:
    page_text = get_text()
    if(current_text != page_text):
        print("Changed")
        
        message = client.messages \
            .create(
                body='Something has changed on Holiday-Contest!',
                from_= twilio_number,
                to= my_number
            )
        current_text = page_text
    time.sleep(10)
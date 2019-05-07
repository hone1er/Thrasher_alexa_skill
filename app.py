#!/usr/bin/env python3.6
"""Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the recent video
uploads. The code is activated with voice commands via an Amazon Echo, Dot,
or Spot."""

import os
from urllib.request import Request as Req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import html.parser as parser
from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
# URL to Thrasher Magazine's recent videos
my_url = Req("http://www.thrashermagazine.com/articles/videos/", headers={"User-Agent":"Mozilla/5.0"})
# open connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parsing using beautiful soup
page_soup = soup(page_html, "html.parser")
# Grab all post descriptions
descriptions = page_soup.findAll("div", {"class":"post-description"})
# Grab all post titles
titles = page_soup.findAll("div", {"class":"post-thumb-container"})
# This is a link to the Thrasher logo that is displayed when viewing the alexa app or on alexa devices with a screen
img_url = "https://s3-us-west-1.amazonaws.com/thrasherskill/thrasher-logo.png"


def get_info():
# This is a generator that takes titles and descriptions, reformats the html and yields the title and description of the latest videos for Alexa to respond with
    for tit, des in zip(titles, descriptions):
        titled = tit.a.img["alt"].strip()
        title = parser.HTMLParser().unescape(titled)
        description = des.text.strip()
        yield f"{title}. {description}"

# Returns the next videos information
def next_video():
    return next(the_info)

# Restarts the generator object
def restart():
    global the_info
    the_info = get_info()

# Below is the diffent responses the Alexa will provide depending on the ask.intent
@ask.launch
def launch():
    restart()
    words = f"The newest video on Thrasher Magazine is {next_video()} \r\n {follow_up}"
    return question(words) \
      .standard_card(title="Thrasher Magazine",
                    text=words,
                     small_image_url=img_url)

@ask.intent("YesIntent")
def play_next():
    words = f"{next_video()} \r\n {follow_up}"
    return question(words) \
      .standard_card(title="Thrasher Magazine",
                    text=words,
                     small_image_url=img_url)

@ask.intent("AMAZON.FallbackIntent")
def play():
    words = f"{next_video()} \r\n {follow_up}"
    return question(words) \
      .standard_card(title="Thrasher Magazine",
                    text=words,
                     small_image_url=img_url)
                     
@ask.intent("AMAZON.StopIntent")
def stop():
    restart()
    return statement("Ok, goodbye")

@ask.intent("AMAZON.CancelIntent")
def cancel():
    restart()
    return statement("Ok, goodbye")

@ask.intent("NoIntent")
def end_session():
    restart()
    return statement("Ok, check back later")

the_info = get_info()
follow_up = "Would you like to hear what else is playing?"

if __name__ == "__main__":
      app.run()

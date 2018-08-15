#!/usr/bin/env python
"""Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the recent video
uploads. The code is activated with voice commands via an Amazon Echo, Dot,
or Spot."""

from urllib.request import Request as Req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import html.parser as parser
from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
my_url = Req("http://www.thrashermagazine.com/articles/videos/", headers={"User-Agent":"Mozilla/5.0"})
# open connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# html parsing
page_soup = soup(page_html, "html.parser")
descriptions = page_soup.findAll("div", {"class":"post-description"})
titles = page_soup.findAll("div", {"class":"post-thumb-container"})
img_url = "https://s3-us-west-1.amazonaws.com/thrasherskill/thrasher-logo.png"

def get_info():
    for tit, des in zip(titles, descriptions):
        titled = tit.a.img["alt"].strip()
        title = parser.HTMLParser().unescape(titled)
        description = des.text.strip()
        yield f"{title}. {description}"

def next_video():
    return next(the_info)

def restart():
    global the_info
    the_info = get_info()

@ask.launch
def launch():
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
def play_next():
    words = f"{next_video()} \r\n {follow_up}"
    return question(words) \
      .standard_card(title="Thrasher Magazine",
                    text=words,
                     small_image_url=img_url)

@ask.intent("AMAZON.StopIntent")
def stop():
    restart()
    return statement("Goodbye") \
      .standard_card(title="Thrasher Magazine",
                    text=("Goodbye"),
                     small_image_url=img_url)

@ask.intent("AMAZON.CancelIntent")
def cancel():
    restart()
    return statement("Goodbye") \
      .standard_card(title="Thrasher Magazine",
                    text=("Goodbye"),
                     small_image_url=img_url)

@ask.intent("NoIntent")
def end_session():
    restart()
    message = "Ok, check back later"
    return statement(message) \
      .standard_card(title="Thrasher Magazine",
                     text="Ok, check back later",
                      small_image_url=img_url)

the_info = get_info()
follow_up = "Would you like to hear what else is playing?"


if __name__ == "__main__":
    app.run(debug=True)

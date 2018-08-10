#!/usr/bin/env python
"""Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the recent video
 uploads. The code is activated by an Amazon Echo, Dot, or Spot. For testing
 purposes you will need to have someway to connect to developer.amazon.com such
 as ngrok.

To-do
----
Images need to be added to the "YesIntent" response .standardcard for the
echo spot, dot, and Alexa app on phones and tablets to display the image that
matches the current title and description"""



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


def get_info():
    for tit, des in zip(titles, descriptions):
        titled = tit.a.img["alt"].strip()
        title = parser.HTMLParser().unescape(titled)
        description = des.text.strip()
        yield f"{title}. {description}"

# Still trying to work out adding a standard card that returns the image
# associated with the info. Currently the Thrasher Logo is used in place of
# the correct thumbnail. The code below pulls images from Thrasher but the
# image has to be hosted somewhere that fills Amazons requirements. Using
# AWS S3 to store the Logo for now.

# def get_image():
#     for images in titles:
#         image = "".join(["www.thrashermagazine.com" + images.a.img["src"]])
#         yield image


def next_video():
    return next(the_info)

def restart():
    global the_info
    the_info = get_info()
    return ""

@ask.launch
def launch():
    textd="Would you like to hear what videos are playing on thrasher magazine?"
    return question(textd) \
      .standard_card(title="Thrasher Magazine",
                    text=textd,
                     small_image_url="https://s3-us-west-1.amazonaws.com/thrasherskill/thrasher-logo.png")

@ask.intent("YesIntent")
def play_next():
    words = f"{next_video()} \r\n {follow_up}
    return question(words) \
      .standard_card(title="Thrasher Magazine",
                    text=words,
                     small_image_url="https://s3-us-west-1.amazonaws.com/thrasherskill/thrasher-logo.png")

@ask.intent("NoIntent")
def end_session():
    message = f"Ok, check back later{restart()}"
    return statement(message) \
      .simple_card(title="Thrasher Magazine",
                     content="OK, check back later")

the_info = get_info()
follow_up = "Would you like to hear what else is playing?"


if __name__ == "__main__":
    app.run(debug=True)

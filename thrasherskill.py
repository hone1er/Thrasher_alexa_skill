#!/usr/bin/env python
"""Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the recent video
 uploads. The code is activated by an Amazon Echo, Dot, or Spot. For testing
 purposes you will need to have someway to connect to developer.amazon.com such
 as ngrok.

 To-Do
 -----
1. Need the script to reset when the session with the Amazon device ends so next
time it is activated it is back to the top of the list

2. Images need to be added to the "YesIntent" response .standardcard for the
echo spot, dot, and Alexa app on phones and tablets to display the image that
matches the current title and description

3. Text responses for the cards needs to be correctly formatted"""

from urllib.request import Request as Req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, "/")
my_url = Req('http://www.thrashermagazine.com/articles/videos/', headers={'User-Agent':'Mozilla/5.0'})
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
        title = tit.a.img["alt"]
        description = des.text.strip()
        yield ". ".join([title, description])

# Still trying to work out adding a standard card that returns the image
# associated with the info

# def get_image():
#     for images in titles:
#         image = "".join(["www.thrashermagazine.com" + images.a.img["src"]])
#         yield image


def iterate():
    return next(the_info)


@ask.launch
def launch():
    text="Would you like to hear what videos are playing on thrasher magazine?"
    return question(text) \
      .simple_card(title='Thrasher Magazine',
                    content=text)


@ask.intent("YesIntent")
def play_next():
    words = str(iterate()) + "\r\n " + follow_up
    return question(words) \
      .simple_card(title='Thrasher Magazine',
                    content=words)


@ask.intent("NoIntent")
def end_session():
    message = "Ok, check back later"
    return statement(message) \
      .simple_card(title='Thrasher Magazine',
                     content="OK, check back later")


the_info = get_info()
# pic = get_image()
follow_up = "Would you like to hear what else is playing?"



if __name__ == "__main__":
    app.run(debug=True)

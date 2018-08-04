"""Alexa skill that grabs the info on the
most recent uploads and reads it to the user"""


from urllib.request import Request as Req
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
ask = Ask(app, "/")
my_url = Req('http://www.thrashermagazine.com/articles/videos/', headers={'User-Agent': 'Mozilla/5.0'})
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


def get_image():
    for images in titles:
        image = "".join(["www.thrashermagazine.com" + images.a.img["src"]])
        yield image


def iterate():
    return next(the_info)


the_info = get_info()
pic = get_image()
follow_up = "Would you like to hear what else is playing?"

@ask.launch
def launch():
    words = "Would you like to hear what videos are playing on thrasher magazine?"
    return question(words) \
      .simple_card(title='Thrasher Magazine', content=words)


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


if __name__ == "__main__":
    app.run(debug=True)

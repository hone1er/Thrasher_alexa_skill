"""
Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the most recent video
 uploads. The information on the latest video is then returned through an Amazon Alexa enabled device. 
 
 The code is activated by an Amazon Echo, Dot, or Spot. You will need an amazon
 developer account to do any testing. Project is not currently deployed.

 To-Do
 -----
1. Images need to be added to the "YesIntent" response .standardcard for the
echo spot, dot, and Alexa app on phones and tablets to display the image that
matches the current title and description

2. Deploy to AWS Lamba through Zappa


Info on using Flask-ask can be found here:
https://flask-ask.readthedocs.io/en/latest/

Info on developing an Alexa Skill found here:
https://developer.amazon.com/alexa-skills-kit

This was a personal project that allow me to explore and learn more about Flask-ask,
AWS, web scraping, and generators.
"""

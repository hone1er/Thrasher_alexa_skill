"""
Thrasher Magazine Alexa skill

Thrasher Magazine's website is parsed for infomation about the recent video
 uploads. The code is activated by an Amazon Echo, Dot, or Spot. For testing
 purposes you will need to have someway to connect to your developer.amazon.com account such
 as ngrok.

 To-Do
 -----
1. Need the script to reset when the session with the Amazon device ends so next
time it is activated it is back to the top of the list

2. Images need to be added to the "YesIntent" response .standardcard for the
echo spot, dot, and Alexa app on phones and tablets to display the image that
matches the current title and description

3. Text responses for the cards needs to be correctly formatted


Info on using Flask-ask can be found here: 
https://flask-ask.readthedocs.io/en/latest/

Info on developing an Alexa Skill found here:
https://developer.amazon.com/alexa-skills-kit

Feel free to modify the code to work with any website or help work out the problems listed 
in the To-Do list. Or add to the To-Do list if you find issues
"""

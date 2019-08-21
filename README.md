# Thrasher Magazine - Alexa Skill

<img src="icon_108_A2Z.png">


 Thrasher Magazine's website is parsed for infomation about the most recent video
 uploads. The information on the latest video is then returned through an Amazon Alexa enabled device. 
 
 The code is activated by an Amazon Echo, Dot, or Spot.

## Getting Started

The skill is live and available for download at the link below

### Installing

* [Thrasher Video](https://www.amazon.com/dp/B07RLBPR8F/ref=sr_1_1?keywords=thrasher&qid=1557416841&s=digital-skills&sr=1-1-catcorr) - Thrasher Magazine Alexa Skill

Follow the link above and click "Enable Skill"


### Using the skill
#### Invocation
Users say a skill's invocation name to begin an interaction with a particular custom skill.
This skills invocation name is: Skateboard Bible

#### Sample Utterences
```
User: Alexa, ask Skateboard Bible what's new 
User: Alexa, ask Skateboard Bible what's playing on Thrasher
User: Alexa, ask Skateboard Bible to check whats on
User: Alexa, tell Skateboard Bible to check recent uploads
```


## Deployment

Deployed using Zappa and AWS lambda

## Built With

* [Flask_ask](https://flask-ask.readthedocs.io/en/latest/) - The framework used
* [Beautiful_Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Library used to scrape the website
* [zappa](https://www.zappa.io/) - Used to deploy app




## Authors

* **Joseph Villavicencio** - *Initial work* - [hone1er](https://github.com/hone1er)

## License

MIT License

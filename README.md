# chipper

Chipper is a bot to win free chipotle from the ChiptoleTweets account. It uses a tweetshift feed to monitor for new codes. 

# Installation 

Head over to [TweetShift](https://tweetshift.com/)
Sign up for a free account and set it up in the discord server of your choice. 

Set up a new feed for (@ChipotleTweets) and make sure to click `Show only the text content of the Tweet` for the `How should Tweets be displayed?` Question. 
Copy down the discord channel ID of that channel. 

Head over to [Discord Developer Portal](https://discord.com/developers/applications)
Setup a new application with a discord bot. Add that bot to the server with the TweetShift feed. Make sure to copy the bot token because we will need that later. 

Install the needed requirements 
```bash
pip3 install -r requirements.txt
```

Go into system settings and allow for terminal or whereever you run the app to have access to accessibility settings. This is how the bot sends the message. 
![alt text](https://github.com/mdepalma15/chipper/blob/main/ss.png?raw=true)

# Usage

Start the application
```bash
python3 app.py
```

Copy in the information from before and click enter to start!


# What does it do?

This application uses discord.py to monitor a discord channel which has a feed of chiptole's tweets. To do this we will use TweetShift which is a free app. When a new tweet is detected, it will pickup the code and automatically send the code to the chiptole phone number (888222). 




# Talking Shit to Power Purveyors of rude Twitter bots.
**Note: I have no idea if this violates Twitter's terms of service. It probably does. Use at your own risk/I assume no responsibility.**

## Dependencies

You must have [installed Tweepy](http://www.tweepy.org/).

## Instructions

1. Choose your Twitter bot. Right now, it's just "Go Fuck Yourself Donald," which is just about what it sounds like. Soon, who knows. 

2. Download the two files: `gofuckyourselfdonald.py` and `gofuckyourselfdonald.sh`. Keep them somewhere you will remember. (Example: /home/username/bots/)

3. [Register your app](https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/). For the name, I recommend [your username]-tstp. When you receive your keys, keep the page open.

4. Open a terminal (Mac: use spotlight and type in "terminal")

5. Edit the Python file you just downloaded (use a plain text editor; for example, type `gedit gofuckyourselfdonald.py` Copy your authentication keys (from the Twitter App page) into the appropriate place in the Python file you downloaded from here. Save and exit.

6. Edit the Shell file you just downloaded (e.g. `gedit gofuckyourselfdonald.sh`). Change `/path/to/` to the path to the location where you downloaded the python script.

7. Test the script by typing `python gofuckyourselfdonald.py` into your terminal. Check your Twitter account to see if it posted.

7. Make your files executable by entering the following into terminal: `chmod +x gofuckyourselfdonald.sh && chmod +x gofuckyourselfdonald.py`

8. Schedule a repeating action in Cron. Type `crontab -e` into your terminal. Paste the following: `0 * * * * sh path/to/gofuckyourselfdonald.sh`, replacing `path/to/` with the path where you downloaded the Python file. (E.g., `/home/username/Desktop/gofuckyourselfdonald.sh`)

9. Check your Twitter account on the hour. 

10. Stew.

## Caveats

To have this run constantly, install this on a remote server. Otherwise, it will only run when your computer is on awake.

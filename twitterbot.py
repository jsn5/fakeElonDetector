import tweepy
from credentials import *
import editdistance
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
c = tweepy.Cursor(api.search,q='to:'+'elonmusk',since_id='1017463575919693826',include_entities=True).items()

real_screen_name = 'elonmusk'
real_name = 'Elon Musk'

while True:
	try:
		tweet = c.next()
		text = tweet.text
		name = tweet.user.name
		screen_name = tweet.user.screen_name
		tweet_id = tweet.id
		print(tweet_id)
		if screen_name != real_screen_name:
			name_dist = editdistance.eval(real_name, name)
			screen_dist = editdistance.eval(real_screen_name',screen_name)
			if name_dist <= 2 or screen_dist <= 4:
				print("fake found")
				api.update_status("*❗️❗️beep boop❗️❗️* Fake Elon Musk detected❎, report as spam ❎ @elonmusk @{}".format(screen_name), in_reply_to_status_id=tweet_id)
				api.report_spam([screen_name])
	except tweepy.TweepError:
		print("limit reached")
		time.sleep(60*5)
		continue
	except StopIteration:
		print("end of result")
		time.sleep(10)
		c = tweepy.Cursor(api.search,q='to:'+'elonmusk',since_id=tweet_id,include_entities=True).items()
		continue



import random
from twython import Twython
from pathlib import Path

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


messages = open('data.txt','r').read().replace('\n',' ')


#messages = [
#        "I like pie",
#        "Error 404,not found",
#        "I live in a small place, a small device called Raspberry Pi"
#]

messages = random.choice(messages)

twitter.update_status(status=message)
print("Tweeted: {}".format(message))

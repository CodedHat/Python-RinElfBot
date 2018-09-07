import random
from twython import Twython

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



messages = [
        "I like pie",
        "I like pies, bitches!",
        "I like my marshmallow bf",
        "I like his butt...",
]
message = random.choice(messages)

twitter.update_status(status=message)
print("Tweeted: {}".format(message))


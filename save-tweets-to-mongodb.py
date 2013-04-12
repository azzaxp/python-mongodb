#This is a simple Python code to store tweets in MongoDB using Pymongo (Python Driver for Mongo)

import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the twitter database it will create new if twitter database is not already created
db=connection.twitter
tweets = db.tweets

# get the tweets from search api of twitter (here I have used "apple" as key word)
twitapi = urllib2.urlopen("https://search.twitter.com/search.json?q=apple")

# parse the json into python objects
parsed = json.loads(twitapi.read())

# iterate through every tweet item on the page
for item in parsed ['results']:
    # put it in mongo
    tweets.insert(item)

import json

with open('twitterData.json', 'r') as json_data:
    twitter_data = json.load(json_data)

for tweet in twitter_data:
    if 'obama' in tweet['tweet'].lower():
        print(tweet)
from bs4 import BeautifulSoup
import requests
import json

url = 'https://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
tweet_array = []

for tweet in content.find_all('div', attrs={"class": "tweetcontainer"}):
    tweet_object = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweet_array.append(tweet_object)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweet_array, outfile)
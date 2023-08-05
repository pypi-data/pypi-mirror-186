import requests
import json
from bs4 import BeautifulSoup

def followers(username:str):
    profile_url = f"https://github.com/{username}"
    data  =requests.get(url=profile_url)
    page_data = BeautifulSoup(data.content, "html.parser")
    followers = page_data.find(class_ = "text-bold color-fg-default")
    return followers.text


res = followers("nikhil25803")
print(res)
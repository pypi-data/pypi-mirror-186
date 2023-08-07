import json
import requests
from bs4 import BeautifulSoup


def get_followers(username:str):
    data  =requests.get(url="https://github.com/nikhil25803")
    data = BeautifulSoup(data.content, "html.parser")
    followers = data.find(class_ = "text-bold color-fg-default")
    return followers.text



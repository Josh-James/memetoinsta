from instabot import Bot
import json
import random
import requests
from PIL import Image
import math

# logs in to the instagram account and uploads the image 
def login():
    text = "caption"
    bot = Bot()
    bot.login(username="username", password='password')
    bot.upload_photo(photo="/memetoinsta/memes/image.jpg", caption=text)
    bot.logout(username="username", password='password')
login()

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
import random
import requests
from PIL import Image
import os
import json
import math

class mememachine(scrapy.Spider):
    name = 'memes'
    # urls used for the crawler
    start_urls = ["https://www.reddit.com/r/wholesomememes/top/?t=week", 
    "https://www.reddit.com/r/memes/top/?t=week"]

    def parse(self, response):
        # creates a dictionary of several posts based on the 
        # HTML tag type of the posts
        for posts in response.css('div._1qftyZQ2bhqP62lbPjoGAh.Post'):
            yield {
                'name': posts.css('h3._eYtD2XCVieq6emjKBH3m::text').get(),
                'post': posts.css('img._2_tDEnGMLxpM6uOa2kaDB3').attrib['src']
            }
# runs the crawler and retreives the post links, saving it in a json file
def run():
    process = CrawlerProcess({
        'USER_AGENT': 'Chrome/96.0.4664.45',
        'FEED_FORMAT': 'json',
        'FEED_URI': '/memetoinsta/memes/memesresult.json'
    })

    process.crawl(mememachine)
    process.start()

# function picks one of the posts from the dictionary in the json 
# and downloads the image
def imagepick():
    f = open('/memetoinsta/memes/memesresult.json')
    data = json.load(f)
    posts = []
    for i in data:
        posts.append(i)

    post = random.choices(posts)
    for p in post:
        url = p['post']

    r = requests.get(url, allow_redirects=True)
    open('image.jpg', 'wb').write(r.content)
    im = Image.open('image.jpg')
    im.save('/memetoinsta/memes/image.jpg')
# function resizes the image to a size recognized by instagram
def resize(im, min_size=1080, fill_color=(255, 255, 255)):
    # here getting the width and the height of the picture and 
    # after that adjusting it's size for it to fit on a 1080px picture perfectly
    width, height = im.size
    ratio = 1080 / width
    width = width + 0.00
    height = height + 0.00
    width = width * ratio
    height = height * ratio
    height = math.floor(height)
    width = math.floor(width)
    im = im.resize((width, height)) # resizing the picture to width 1080
    # here is some code i got online to create a white picture then paste 
    # my picture on top of it to make the picture square
    if height != width:
        x, y = im.size
        size = max(min_size, x, y)
        new_im = Image.new('RGB', (size, size), fill_color)
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        new_im.save('image.jpg') # returning the new image so that I can save and upload
        new_im = new_im.convert("RGB")
    else:
        print('image is ready for insta')
# checks if the json file with previous links exists
if os.path.exists("/memetoinsta/memes/memesresult.json"):
    # removes previous json file
    os.remove("/memetoinsta/memes/memesresult.json")
    # runs the crawler
    run()
    # runs the imagepick() function
    imagepick()
    # opens and resizes the image from Reddit
    image = open('image.jpg')
    resize(Image.open('image.jpg'))

else:
    # runs and resizes the image if there is no json file
    run()
    imagepick()
    image = open('image.jpg')
    resize(Image.open('image.jpg'))

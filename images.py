from PIL import Image
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib
import os
import json

url = 'your site here'

hdr = {
    'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)

response = urlopen(req)
soup = BeautifulSoup(response, 'html.parser')

image = soup.find_all('img')
i = 0
img_source = []
# SAVE_FOLDER = 'images'
for item in image:
    image_url = item['src']
    # image_url = "https://google.com" + image_url
    image_url = image_url.split("?")[0]
    # print(type(image_url))
    if (image_url.startswith("add some filter string")):
        if (image_url.endswith(".jpg")):
            i += 1
            with open(f'img/images{i}.jpg', 'wb') as f:
                ima = requests.get(image_url, stream=False).content
                f.write(ima)

    # img_rs = requests.get(image_url, stream=True)
    # ima = open(os.path.join('img', os.path.basename(image_url)), 'wb+')
    # for down in img_rs.iter_content():
    #     ima.write(down)

    # except:
    #     print("Some Error Occured")

    # for image in img_source:
    #     webs = requests.get(image)
    #     open('images/' + image.split('/')[-1], 'wb').write(webs.content)
    # print("some error occurred")

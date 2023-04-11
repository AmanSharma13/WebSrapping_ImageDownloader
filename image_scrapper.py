from PIL import Image
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from io import BytesIO
import urllib
import os
import json

url = "your url here"
hdr = {
    'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=hdr)

response = urlopen(req)
soup = BeautifulSoup(response, 'html.parser')

image = soup.find_all('img')
i = 0
print(image)
img_source = []
for item in image:
    image_url = item['src']
    print(image_url)
    # image_url = image_url.split("?")[0]
    # if (image_url.startswith("add some filter string")):
    if (image_url.endswith(".jpg")):
        try:
            i += 1
            r = requests.get(image_url)
            img = Image.open(BytesIO(r.content))
            fp = open(f"img/img{i}.jpg", "wb")
            img.save(fp)
            fp.close()
        except:
            print("something happened")

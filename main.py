import requests
from urllib import parse
import os

"""
background-image: url(/th?id=OHR.Inisheer_EN-IN7964243509_1920x1080.jpg&rf=LaDigue_1920x1080.jpg); opacity: 1;

https://www.bing.com/?toWww=1&redig=B8E0C6151AAD4A94B8FDB35060E102B7

"""

filename = "BingWallpaper"
i = 0
while os.path.exists(filename + f"{i}.jpg"):
    i += 1


url = "https://www.bing.com"
response = requests.get(url)

for div in response.text.split("style="):
    if ".jpg" in div:
        text = div.split(".jpg")[0]
        if "url" in text:
            wallpaper_url = parse.urljoin(url, text.split("url(")[-1]) + ".jpg"
            image = requests.get(wallpaper_url)
            filename1 = filename + f"{i}.jpg"
            i += 1
            with open(filename1, 'wb') as f:
                f.write(image.content)
import requests
from urllib import parse
import os

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
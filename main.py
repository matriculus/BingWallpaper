import requests
from urllib import parse
import os
import tkinter as tk


def getBingWallpaper():
    filename = os.path.join("BingWallpaper")
    i = 0
    while os.path.exists(filename + f"{i}.jpg"):
        i += 1

    url = "https://www.bing.com"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=headers)
    temp = []
    filename1 = ""
    for div in response.text.split("style="):
        if ".jpg" in div:
            text = div.split(".jpg")[0]
            if "url" in text:
                wallpaper_url = parse.urljoin(url, text.split("url(")[-1]) + ".jpg"
                if wallpaper_url in temp:
                    continue
                else:
                    temp.append(wallpaper_url)
                image = requests.get(wallpaper_url)
                filename1 = filename + f"{i}.jpg"
                i += 1
                with open(filename1, 'wb') as f:
                    f.write(image.content)
                
    
    return filename1

if __name__ == "__main__":
    backgroundFile = getBingWallpaper()

class Application(tk.Tk):
    geo = "192x108"
    background = backgroundFile
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Bing Wallpaper!")
        self.config(bg=self.background)
        self.geometry(self.geo)
        self.pack()
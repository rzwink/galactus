import os
import urllib
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup

series = ['3865']
for serie in series:
    try:
        os.mkdir(serie)
    except OSError as error:
        print(error)
    url = "https://www.comics.org/series/" + serie + "/covers/"
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")

    imgs = soup.findAll("img", {"class": "cover_img"})
    for img in imgs:
        imgUrl = img['src'].replace("w100", "w400")
        print(imgUrl)
        urlretrieve(imgUrl, serie + "/" + os.path.basename(imgUrl).split("?")[0])

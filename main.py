# Relu-Python-Task
# author: Aryan Gurung
# date:   18-07-2022

from bs4 import BeautifulSoup
import requests
from lib import title, imgurl, price, detail

def Main():
    # Establishing Connection
    link = 'https://www.amazon.es/dp/000106875X'
    responce = requests.get(link)
    if responce.status_code == 404:
        print(link+"not available")
        pass
    else:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

        source = requests.get(link, headers=headers)
        soup = BeautifulSoup(source.content, "lxml")

        title.getTitle(soup)
        imgurl.getImgurl(soup)
        price.getPrice(soup)
        detail.getDetail(soup)


if __name__ == '__main__':
    Main()
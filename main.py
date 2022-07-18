# Relu-Python-Task
# author: Aryan Gurung
# gurungaryan73@gmail.com
# date:   18-07-2022

from bs4 import BeautifulSoup
import requests
import csv
from lib import title, imgurl, price, detail

def Main():
    #opening csv file (AmazonScrapingSheet.csv)
    with open('AmazonScrapingSheet.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            country = line[3]
            asin    = line[2]
            link    = 'https://www.amazon.{}/dp/{}'.format(country,asin)

            # Checking responce status
            responce = requests.get(link)
            if responce.status_code == 404:
                print(link+" not available\n")
                pass
            else:
                # Establishing Connection
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
                source  = requests.get(link, headers=headers)
                soup    = BeautifulSoup(source.content, "lxml")

                # checks
                checktitle = title.getTitle(soup)
                if checktitle != None:
                    print(link)
                    print("Product Title:",checktitle.string)               
                    imgurl.getImgurl(soup,checktitle)
                    price.getPrice(soup)
                    detail.getDetail(soup)
                else:
                    pass

if __name__ == '__main__':
    Main()
# Relu-Python-Task
# description: get image url
import json

def getImgurl(soup, title):
    # links = soup.find_all("div", {"id":'imgTagWrapperId'})
    # print("Product Image: ",links[0].find('img')['src'])
    for img in soup.find_all("img", src=True):
        print(img['src'])
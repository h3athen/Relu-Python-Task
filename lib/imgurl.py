# Relu-Python-Task
# description: get image url

def getImgurl(soup):
    try:
        links = soup.find_all("div", {"id":'img-canvas'})
        print("Product Image: ",links[0].find('img')['src'])
    except AttributeError:
        print("Image Url Unavailable")
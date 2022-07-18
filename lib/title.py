# Relu-Python-Task
# description: get product title

def getTitle(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'}).string
        print("Product Title:",title)
    except AttributeError:
        print("Product Title Unavailable")
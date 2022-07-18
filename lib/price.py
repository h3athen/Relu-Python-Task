# Relu-Python-Task
# description: get product price

def getPrice(soup):
    try:
        price = soup.find("span", attrs={"id":'price'}).string
        print("Product Price: ",price)
    except AttributeError:
        print("Product Price Unavailable")
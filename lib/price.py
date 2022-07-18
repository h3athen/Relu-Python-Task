# Relu-Python-Task
# description: get product price

def getPrice(soup):
    price = soup.find("span", attrs={"id":'price'})
    print("Product Price: ",price)

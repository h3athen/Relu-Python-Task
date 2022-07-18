# Relu-Python-Task
# description: get product title

def getTitle(soup):
    title = soup.find("span", attrs={"id":'productTitle'})
    return title
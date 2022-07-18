# Relu-Python-Task
# description: get product detail

def getDetail(soup):
    try:
        key = [x.get_text(strip=True).replace('\u200f\n','').replace('\u200e','').replace(':\n','').replace('\n', '').strip() for x in soup.select('ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-none.detail-bullet-list > li > span > span.a-text-bold')][:13]
        value = [x.get_text(strip=True) for x in soup.select('ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-none.detail-bullet-list > li > span > span:nth-child(2)')]
        product_details = {k:v for  k, v, in zip(key, value)}
        print("Product Detail:",product_details)
    except AttributeError:
        print("Product Detail Unavailable")
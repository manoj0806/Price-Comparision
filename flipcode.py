'''project real-time comparision of online products
function for retrival of products from flipkart
date:5 NOV 2020
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name = input("Product name:")
name1 = name.replace(" ", "+")
url = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
for i in range(0,1):
    print('Product Name:')
    try:
        flipkart_name = [soup.select('._3wU53n')[0].getText().strip()]
        flipkart_price=[soup.select('._2rQ-NK')[0].getText().strip()]
        print(flipkart_name[0])
        print(flipkart_price[0])
    except:
        flipkart_name = [soup.select('._2cLu-l')[0].getText().strip()]
        flipkart_price = [soup.select('._1vC4OE')[0].getText().strip()]
        print(flipkart_name[0])
        print(flipkart_price[0])


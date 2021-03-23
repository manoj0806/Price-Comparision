from bs4 import BeautifulSoup
import requests
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/S37.3'}

def amazon(name):
    global amazon
    name1=name.replace(" ","-")
    name2=name.replace(" ","+")
    amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
    res= requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
    print('Product searching on amazon\n')
    soup = BeautifulSoup(res.text,'html.parser')
    amazon_page = soup.select('.a-color-base.a-text-normal')
    amazon_page_length = int(len(amazon_page))
    for i in range(0,amazon_page_length):
        name=name.upper()
        amazon_name=soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()

        if name in amazon_name[0:20]:
            amazon_name=soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
            # amazon_delivery = soup.select('.a-text-bold')[i].getText().strip().upper()
            print("Amazon:")
            print(amazon_name)
            print("Rs:"+amazon_price)
            # print(amazon_delivery)
            break
        else:
            i+=1
            i=int(i)
            if i ==  amazon_page_length:
                print("Product not found")
                amazon_price='0'
                break
    return amazon_price

name= input("product name:")
amazon_price=amazon(name)


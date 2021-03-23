from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/S37.3'}

flipkart=''
amazon=''
ebay=''
croma=''

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
            print("Amazon:")
            print(amazon_name)
            print("Rs:"+amazon_price)
            break
        else:
            i+=1
            i=int(i)
            if i ==  amazon_page_length:
                print("Product not found")
                amazon_price='0'
                break
    return amazon_price


def ebay(name):
    global ebay
    name1= name.replace(" ","+")
    ebay =f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=570.11313&_nkw={name1}&_sacat=0'
    res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=570.11313&_nkw={name1}&_sacat=0',headers=headers)
    print("Product searching on ebay :")
    soup=BeautifulSoup(res.text,'html.parser')
    ebay_price=soup.select('.s-item__price')
    ebay_page_length=int(len(ebay_price))
    for i in range(0,ebay_page_length):
        info=soup.select('.SECONDARY_INFO')[i].getText().strip()
        info=info.upper()
        if info=='BRAND NEW':
            ebay_name = soup.select('.s-item__title')[i].getText().strip()
            name=name.upper()
            ebay_name=ebay_name.upper()
            if name in ebay_name[:25]:
                ebay_price = soup.select('.s-item__price')[i].getText().strip()
                ebay_name = soup.select('.s-item__title')[i].getText().strip()
                print('EBay:')
                print(ebay_name)
                print(ebay_price.replace("INR", "Rs:"))
                print(info)
                ebay_price = ebay_price[0:14]
                break
            else:
                i+=1
                i=int(i)
                if i == ebay_page_length:
                    print("Ebay:No product was found")
                    ebay_price='0'
                    break
    return ebay_price


def croma(name):
    try:
        global croma
        name1 = name.replace(" ","+")
        croma=f'https://www.croma.com/search/?text={name1}'
        res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)
        print("\nSearching in croma.....")
        soup = BeautifulSoup(res.text,'html.parser')
        croma_name = soup.select('h3')

        croma_page_length = int( len(croma_name))
        for i in range (0,croma_page_length):
            name = name.upper()
            croma_name = soup.select('h3')[i].getText().strip().upper()
            if name in croma_name.upper()[:25]:
                croma_name = soup.select('h3')[i].getText().strip().upper()
                croma_price = soup.select('.pdpPrice')[i].getText().strip()
                print(croma_name)
                print(croma_price)
                print("-----------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==croma_page_length:
                    print("Croma: No product Found!")
                    print("-----------------------")
                    croma_price = '0'
                    break
        ##print(croma_price)
        return croma_price
    except:
        print("Croma: No product Found!")
        print("-----------------------")
        croma_price = '0'
    return croma_price




def flipkart(name):
    global flipkart
    name1 = name.replace(" ","+")
    flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    res= requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)

    print("\nSearching in flipkart...")
    soup =BeautifulSoup(res.text,'html.parser')
    flipkart_name= soup.select('._4rR01T')[0].getText().strip()
    flipkart_name= flipkart_name.upper()
    if name.upper() in flipkart_name:
        flipkart_name = soup.select('._30jeq3._1_WHN1')[0].getText().strip()
        flipkart_price = soup.select('._4rR01T')[0].getText().strip()
        print('Flipkart:')
        print(flipkart_name)
        print(flipkart_price)
    else:
        print("Flipkart:Product not found !")
        flipkart_price='0'
    return flipkart_price


def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("Rs.",'')
    g=int(float(f))
    return g

name = input('Product name:\n')
flipkart_price=flipkart(name)
print('-----------------------------------')
amazon_price=amazon(name)
print("----------------")
ebay_price=ebay(name)
print("---------------")
croma_price = croma(name)



print("-----------------------------------")

if flipkart_price==0:
    print('Product not found \n')
else:
    print('flipkart price:',flipkart_price)
if amazon_price==0:
    print('Product not found\n')
else:
    print('amazon price:',amazon_price)
if ebay_price==0:
    print('Product not dound \n')
else:
    print('ebay price:',ebay_price.replace("INR","Rs:"))
if croma_price==0:
    print('Product not found\n')
else:
    print('croma price:',croma_price)



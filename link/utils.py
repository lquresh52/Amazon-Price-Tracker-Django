import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    print('----name----')
    print(name)
    price = soup.select_one(selector="#priceblock_ourprice").getText().replace(',','')
    print('----price----')
    print(price[2:])
    price = float(price[2:])

    return name, price
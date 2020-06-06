import requests
import bs4

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    #
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()

price = getEbayPrice('https://www.ebay.com/itm/Automate-the-Boring-Stuff-With-Python-Practical-Programming-for-Total-Begin-/382591428976')
print('The price is: ' + price)
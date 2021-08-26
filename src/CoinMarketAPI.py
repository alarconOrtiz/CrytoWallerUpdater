from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import PrivateData
from bs4 import BeautifulSoup

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'EUR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': PrivateData.CoinMarket_key, 
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  responseJson = json.loads(response.text)
  #soup = BeautifulSoup(data,'html.parser')
  print()
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
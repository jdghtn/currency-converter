import requests, os

from dotenv import load_dotenv

load_dotenv()

API_KEY =  os.getenv('API_KEY')
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
CURRENCIES = ['EUR', 'USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

def convert_currency(base):
  # split list into single comma separeted string
  currencies = ','.join(CURRENCIES)
  url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'

  try:
    # hit endpoint
    response = requests.get(url)
    
    # convert to json
    data = response.json()

    # return data array
    return data['data']
  except:
    print('Invalid entry.')
    return None

while True:
  base = input('Enter a base currency (q to quit): ').upper()

  if base == 'Q':
    break

  data = convert_currency(base)
  # throws the invalid entry
  if not data:
    continue
  
  # .items() returns the list with all dictionary keys with values
  print(f'1 {base} is equivalent to:\n')

  for ticker, value in data.items():
    # exclude base from the list
    if ticker != base:
      print(f'{ticker}: {value}')
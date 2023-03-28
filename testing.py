import requests
from bs4 import BeautifulSoup

url = 'https://www.earningswhispers.com/epsdetails/aapl'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
doc.prettify()
result = doc.find_all(class_='mainitem')

print(result[0].string)

import requests
from bs4 import BeautifulSoup

url = 'https://www.historicalweatherdata.com/northam-2805953'
response = requests.get(url)
print (response.content)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'table table-striped table-bordered'})
print (table)
#rows = table.find_all('tr')

# for row in rows:
#     cols = row.find_all('td')
#     cols = [col.text.strip() for col in cols]
#     print(cols)
a = soup.find('title')
print(" just table ")
print (a)


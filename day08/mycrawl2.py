import requests
from bs4 import BeautifulSoup

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)  # url의 정보를 가져온다.
response.encoding = 'euc-kr'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('td', class_='st2')

for idx, td in enumerate(tds):
    s_name = td.text
    price = td.parent.find_all("td")[1].text
    print(idx, s_name, price)

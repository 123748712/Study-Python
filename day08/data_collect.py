import requests
from bs4 import BeautifulSoup
from datetime import datetime
from day09.daostock import DaoStock

ds = DaoStock()

s_date = datetime.now().strftime("%Y%m%d_%H%M")

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

response = requests.get(url)
response.encoding = 'euc-kr'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('td', class_='st2')

for idx, td in enumerate(tds):
    s_name = td.text
    price = td.parent.find_all("td")[1].text.replace(",", "")  # 쉼표를 아무것도 없는 빈공간으로 바꿔 int로 변경한다.
    cnt = ds.insert(s_name, price, s_date)
    print(s_name, price, s_date, cnt)

ds.commit()  # insert구문에 commit()을 반복하지 않고 마지막에 한번만 해준다.

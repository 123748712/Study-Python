import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/emp'  # 원하는 정보가 담겨있는 url

response = requests.get(url)  # url의 정보를 가져온다.

if response.status_code == 200:
    html = response.text  # 응답받은 text를 html에 담아준다.
    soup = BeautifulSoup(html, 'html.parser')  # text형태에서 html 형태로 변환(parser) 해준다.
    # print(soup.select("table")) # table 태그만 select해 배열 형태로 가져온다.

    # print(soup.find_all("table")) # find => 1개, find_all => all

    # for i in tr :
    #     td = tr[i].select("td")
    #

    table = soup.select("table")[0]
    tr = table.select("tr")

    for idx, i in enumerate(tr):
        id = i.select("td")[0].get_text()
        name = i.select("td")[1].get_text()
        sex = i.select("td")[2].get_text()
        addr = i.select("td")[3].get_text()
        if (idx > 0):
            print("e_id : {}, e_nm : {}, sex : {}, addr : {}".format(id, name, sex, addr))




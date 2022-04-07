import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3305, user='root',
    password='admin',
    db='python',
    charset='utf8'
)

cur = conn.cursor()

cur.execute('select * from emp')

result = cur.fetchall() # 쿼리 실행 결과를 전부 가져온다.

for e_id, e_nm, sex, addr in result :
    print("e_id :", e_id, "e_nm :", e_nm, "sex :", sex, "addr :", addr)
    print("====================================")

cur.close()
conn.close()
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3305, user='root',
    password='admin',
    db='python',
    charset='utf8'
)

cur = conn.cursor()

e_id = '1'
sql = f"""
    delete from emp
    where e_id = '{e_id}'
"""
cur.execute(sql)
conn.commit()

sql = "select * from emp"
cur.execute(sql)

result = cur.fetchall()
print(result)

cur.close()
conn.close()
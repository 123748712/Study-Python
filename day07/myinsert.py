import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3305, user='root',
    password='admin',
    db='python',
    charset='utf8'
)

cur = conn.cursor()

# sql = "insert into emp (e_id, e_nm, sex, addr) values ('4', '4', '4', '4')"

sql = """insert into emp (e_id, e_nm, sex, addr)
        values (%s, %s, %s, %s)""" # """ => 줄을 바꿔도 전부 문자열처리 가능

cur.execute(sql, ('4', '4', '4', '4'))
conn.commit() # 임시로 저장된 데이터를 확실하게 commit 해준다.

sql = "select * from emp"
cnt = cur.execute(sql) # sql 구문 실행이 성공하면 cnt = 1 반환

result = cur.fetchall()

print(result)

cur.close()
conn.close()
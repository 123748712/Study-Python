import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3305, user='root',
    password='admin',
    db='python',
    charset='utf8'
)

cur = conn.cursor()
e_id = '4'
e_nm = '5'
sex = '5'
addr = '5'
# sql = "insert into emp (e_id, e_nm, sex, addr) values ('4', '4', '4', '4')"
sql = f"""
update emp
    set
        e_nm = '{e_nm}',
        sex = '{sex}',
        addr = '{addr}'
    where e_id = {e_id}
    """

cur.execute(sql)
conn.commit() # 임시로 저장된 데이터를 확실하게 commit 해준다.

sql = "select * from emp"
cnt = cur.execute(sql) # sql 구문 실행이 성공하면 cnt = 1 반환

result = cur.fetchall()

print("cnt", cnt)

cur.close()
conn.close()

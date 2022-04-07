e_id = "1"
e_nm = "1"
sex = "1"
addr = "1"

# f를 붙이면 '{}' 안에 값을 넣어줄 수 있다.
sql = f"""
    update emp
    set
        e_id = '{e_id}',
        e_nm = '{e_nm}',
        sex = '{sex}',
        addr = '{addr}'
    where e_id = '{e_id}'
"""

print(sql)
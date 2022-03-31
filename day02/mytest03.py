# 1에서 45까지의 숫자중 중복없이 6개를 뽑으세요. (로또예제)
import random

lotto = list(range(1, 46))

print(lotto)

for i in range(45) :
    rnd = int(random.random()*45)
    a = lotto[0]
    b = lotto[rnd]

    lotto[0] = b
    lotto[rnd] = a

# print(lotto[0],lotto[1],lotto[2],lotto[3],lotto[4],lotto[5])
print(lotto[:6]) # 처음부터 6번 전까지 배열 출력
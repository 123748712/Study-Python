import random

# random 홀짝 예제

a = random.random()
mine = input("홀짝을 입력하세요.")
if a > 0.5:
    com = "홀"
else:
    com = "짝"
if com == mine:
    result = "이김"
else:
    result = "짐"

print("나 :", mine)
print("컴 :", com)
print("결과 :", result)
# print에 출력하고 싶은 변수가 있다면 , 로 붙여 출력도 가능하다.
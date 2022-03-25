# random 가위바위보 예제
import random

# mine = input("가위바위보를 입력하세요.")
#
# list = ["가위", "바위", "보"]
# com = random.choice(list)
#
# if mine == com :
#     result = "비김"
# else :
#     if mine == "가위" and com == "바위" or mine == "바위" and com == "보" or mine == "보" and com == "가위" :
#         result = "짐"
#     else :
#         result = "이김"
# print("나 :", mine)
# print("컴 :", com)
# print("결과 :", result)


mine = input("가위바위보를 입력해주세요.")
com = "";
result = ""

random = random.random()
if random > 0.66 :
    com = "가위"
if random > 0.33 :
    com = "바위"
else :
    com = "보"

if mine == com :
    result = "비김"
else :
    if mine == "가위" and com == "바위" or mine == "바위" and com == "보" or mine == "보" and com == "가위" :
        result = "짐"
    else :
        result = "이김"

print("나 :", mine)
print("컴 :", com)
print("결과 :", result)
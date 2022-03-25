# 구구단 출력 문제

dan = int(input("출력할 단수를 입력하세요."))

for i in range(1, 10):
    print("{} * {} = {}".format(dan, i, dan * i))
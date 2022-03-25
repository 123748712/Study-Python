# 배수의 합을 구하는 예제

a = int(input("처음 수를 입력해주세요."))
b = int(input("마지막 수를 입력해주세요."))
c = int(input("배수를 입력해주세요."))

arr = range(a, b + 1)

sum = 0
for i in arr :
    if i % c == 0 :
        sum += i
print("{}에서부터 {}까지 {}배수의 합은 {}입니다.".format(a, b, c, sum))
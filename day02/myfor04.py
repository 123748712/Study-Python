# for 예제
first = int(input("처음 수를 입력하세요."))
last = int(input("마지막 수를 입력해주세요."))

arr = list(range(first, last+1))

sum = 0;

for i in arr :
    sum += i
print("{}에서 {}까지의 합은 {}입니다.".format(first, last, sum))
# 문자, 숫자 구분 없이 중괄호 및 파라미터 순서에 맞게 넣어준다.
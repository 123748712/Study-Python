# def add(a, b):
#     return a+b
#
# def minus(a,b):
#     return a-b
#
# def multply(a,b):
#     return a*b
#
# def divide(a,b):
#     return a/b
#
# sum = add(1,5)
# min = minus(1,5)
# mul = multply(1,5)
# div = divide(1, 5)
#
# print("sum :", sum)
# print("min :", min)
# print("mul :", mul)
# print("div :", div)


def addminmuldiv(a,b):
    return a+b, a-b, a*b, a/b

sum,min,mul,div = addminmuldiv(1, 5)

# 리턴 갯수에 맞춰 순서대로 기입

print("sum :", sum)
print("sum :", sum)
print("min :", min)
print("mul :", mul)
print("div :", div)

sum = addminmuldiv(1, 5)

print("sum :", sum)
# 튜플 (작은 배열, []로 index를 지정해서 값을 가져올 수 있음)
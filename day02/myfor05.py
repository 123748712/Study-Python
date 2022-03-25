arr = ["홍길동", "전우치", "김철수"]

# cnt = 0
# for i in arr :
#     print(cnt, i)
#     cnt += 1

# cnt++ 불가능


for idx, i in enumerate(arr) :
    print(idx, i)
# enumerate => index를 동시에 접근하는 함수
# idx, i 를 동시에 접근할 수 있다.
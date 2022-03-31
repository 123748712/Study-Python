# showdan 함수를 통해 입력한 구구단 출력

def showdan(dan):
    for i in range(1, 9+1):
        # print(dan,"*",i,"=",dan*i)
        print("{} * {} = {}".format(dan, i, dan*i))

showdan(5)
class Animal:
    def __init__(self):  # 생성자
        print("Animal : init")
        self.flagLife = True

    def cantBreath(self):
        self.flagLife = False

    def __del__(self):  # 소멸자
        print("Animal : del")

    def __str__(self):  # toString
        return str(self.flagLife)


class Human(Animal): # 괄호 안 상속받을 class 이름을 기입한다.
    def __init__(self):
        print("Human : init")
        super().__init__()  # 부모의 전역변수를 super(). 으로 끌어들여야 한다.
        self.skillLang = 0;

    def useLang(self, cnt):
        self.skillLang += cnt

    def __del__(self):
        print("Human : del")

    def __str__(self):
        return str(self.flagLife) + "," + str(self.skillLang)


if __name__ == '__main__': # main과 동일
    ani = Animal()
    print(ani.flagLife)
    ani.cantBreath()
    print(ani.flagLife)

    hum = Human();
    print(hum.flagLife)
    print(hum.skillLang)
    hum.cantBreath()
    hum.useLang(5)
    print(hum.flagLife)
    print(hum.skillLang)

    print(ani)
    print(hum)  # str 메소드에 입력한 리턴 값이 출력된다.

# init 생성자가 먼저 생성된 후 함수를 실해한다.
# 그 후에 메모리에서 지워지면 자동으로 del 소멸자가 실행된다.
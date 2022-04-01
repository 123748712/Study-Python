class LeeJY:
    def __init__(self):
        self.money = 10000000000

    def earnMoney(self, money):
        self.money += money


class KimKa:
    def __init__(self):
        self.beauty = 99

    def getOlder(self):
        self.beauty += -1


class JoH(LeeJY, KimKa):
    def __init__(self):
        LeeJY.__init__(self)
        KimKa.__init__(self)
        # 다중상속시 super() 가 아닌 상속받을 class 이름을 기입한다.


if __name__ == '__main__':
    # lj = LeeJY()
    # print(lj.money)
    # lj.earnMoney(100)
    # print(lj.money)

    jo = JoH()
    print(jo.money)
    print(jo.beauty)
    jo.earnMoney(100)
    print(jo.money)
    jo.getOlder()
    print(jo.beauty)

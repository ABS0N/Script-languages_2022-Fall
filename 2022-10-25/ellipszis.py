class Ellipszis:
    def __init__(self, sugar1, sugar2):
        self.sugar1 = sugar1
        self.sugar2 = sugar2

    def terulet(self):
        return self.sugar1*self.sugar2*3.14

    def __bool__(self):
        return self.terulet() > 0

    def __lt__(self, other):
        return self.terulet() < other.terulet()

    def __str__(self):
        return "Gomb({r1}, {r2})".format(r1=self.sugar1, r2=self.sugar2())

def main():
    r1 = Ellipszis(5,10)
    r2 = Ellipszis(10,20)
    if r1:                             # r1.__bool__() értéke alapján dönti el
        print("r1 igaznak számít")
    else:
        print("r1 hamisnak számít")
    print("-" * 20)
    print(r1 < r2)                     # r1.__lt__(r2) -t hívja meg nekünk
    print(r2 < r1)


if __name__ == '__main__':
    main()
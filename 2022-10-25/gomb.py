class Gomb:
    def __init__(self, sugar):
        self.sugar = sugar

    def terfogat(self):
        return 4*self.sugar*self.sugar*self.sugar*3.14

    def __bool__(self):
        return self.terfogat() > 0

    def __lt__(self, other):
        return self.terfogat() < other.terfogat()

    def __str__(self):
        return "Gomb({r}, {v})".format(r=self.sugar, v=self.terfogat())

def main():
    r1 = Gomb(5)
    r2 = Gomb(20)
    if r1:                             # r1.__bool__() értéke alapján dönti el
        print("r1 igaznak számít")
    else:
        print("r1 hamisnak számít")
    print("-" * 20)
    print(r1 < r2)                     # r1.__lt__(r2) -t hívja meg nekünk
    print(r2 < r1)


if __name__ == '__main__':
    main()
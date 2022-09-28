

def print_hi(name):
    print(f'Hi, {name}')

    a = [5, 6, 7]
    print(a)
    print(len(a))

    b = [True, 3.14, 2022, 'cc']
    print(b)

    a.append(8)
    print(a)

    c = []
    print(c)
    c.append(1)
    c.append(2)
    c.append(3)
    print(c)

    z = [1, 2] == [1, 2]
    print(z)

    d = a + b
    print(d)

    e = [1,2,3]
    f = e
    f[0] = 100
    print(e[0])

    f = e[:]
    f[0] = 99
    print(f)

    li = [1,2,3]
    for y in li:
        print(y)

    for y in li:
        y *=2

    for y in li:
        print(y)

    size = len(li)
    i = 0
    while i < size:
        li[i] *= 2
        i += 1

    for y in li:
        print(y)

    print(list("python3"))

    li = [1, 2, 3, 4, 5, 6, 7, 8]

    paros = []

    for szam in li:
        if szam % 2 == 0:
            paros.append(szam)

    for szam in paros:
        print(szam)

    print(12 in paros)
    s = "C, C++, Python, Rust"
    print("--" in s)
    print("++" in s)

    print(3, "Hello", True)
    print(3, "Hello", True, sep="")
    print(3, "Hello", True, sep="", end="\t")
    print(3, "Hello", True, sep="--")
    print("hello", end=""); print("world")
    import sys
    print("hello", file=sys.stderr)

    a = [5,8,9,3,1]
    print(a)
    x = a.pop(0)
    print(x)
    print(a)

    x = a.pop() ##alapertelmezetten az utolso elem
    print(x)
    print(a)

    ##Verem: sima list, append()-el belerak, pop()-al kivesz HASZNALHATO!
    ##Sor: sima list, append()-el belerak, pop(0)-al kivesz az elejerol LASSU!!!

    ##IGY KELL SORT CSINALNI HA SZUKSEGES
    from collections import deque
    q = deque([3, 4, 5])
    print(q)
    q.append(6)
    q.append(7)
    print(q)
    q.popleft()
    print(q)
    ##-----------------------------------

    ##ZH-N LESZ REVERSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    a = [3, 21, -2, 3892, 52]
    print(a)
    print(sorted(a))
    print(sorted(a, reverse=True))
    print(sorted(a)[::-1])##Ez nem kell csak fancy
    ##ZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZHZH

    a = sorted(a)
    print(a)

    a = [3, 9, -2, 4]
    print(a)
    a.sort()
    print(a)

    a = [3, 9, -2, 4]
    for e in sorted(a):
        print(e)

    print(a)

    def szoroz(a):
        szum = 1
        for e in a:
            szum *= e
        return szum

    print(szoroz([8, 3, 2]))
    print(szoroz([]))

    a = ["aa", "bb", "cc", "dd"]
    print(a)
    print(":::".join(a))
    s = ":".join(a)
    print(s)
    print(s.split(":"))
    print("sadsadsa          melwmqkrnqlwi             vbjkabxaséq".split())


####################################################################
if __name__ == '__main__':
    print_hi('PyCharm')

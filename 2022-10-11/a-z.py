def abc(s):
    if s == "a-z.py":  # check filename
        n = 97
        for i in range(26):  # write the letters in normal order
            print(chr(n + i), end=" ")

    if s == "z-a.py":  # check filename
        n = 97 + 25  # begin with z
        while n > 96:  # write the letters in inverse order
            print(chr(n), end=" ")
            n -= 1


def main():
    meta = __file__  # asked the path of the file
    path = str(meta).split('\\')  # path is equal of the pieces of the path
    s = path[len(path) - 1]  # the last var in path is the filename
    abc(s)


if __name__ == '__main__':
    main()
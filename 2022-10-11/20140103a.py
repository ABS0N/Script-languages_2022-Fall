def my_function(): #This function use ASCII codes instead of numbers
    a='x'
    b='z'
    c='d'
    print(ord(a)-ord(c), end="")
    print(ord(b)-ord(c), end="")


def main():
    my_function()


if __name__ == '__main__':
    main()
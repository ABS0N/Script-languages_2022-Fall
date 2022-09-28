#!/usr/bin/env python3

MAX = 10
PI = 3.14159

def hello(name, color, obj):
    # geza, kek az eg!
    # C-ben:
    # printf("%s, %s az %s!\n", name, color, obj);
    # v1:
#    print("{0}, {1} az {2}!".format(name, color, obj))
    # v2:
#    print("{}, {} az {}!".format(name, color, obj))
    # v3:
    print("{name}, {szin} az {o}!".format(name=name.capitalize(), szin=color, o=obj))
    # v4:
#    print(f"1 + 1 = {1+1}")
#    print(f"{name}, {color} az {obj}!")


def main():
    hello("geza", "kek", "eg")

    print("--------------------")
    print("-" *20)
    hello("julcsi", "piros","auto")

    a = 'Batman'
    print(a[0])
    print(a[0:3])
    print(a[:3])
    print(a[3:6])
    print(a[3:])
    #negativ indexeles
    print(a[:-3])
    print(a[-3:])
    print(a[-5:-2])
    print(a[1:-2])

main()
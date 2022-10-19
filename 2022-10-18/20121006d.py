def remove_comments(filename):
    f = open(filename, "r", encoding="utf8")
    f2 = open("string1_clean.py", "w")
    sorok = (f.readlines())

    for sor in sorok:
        if not sor.startswith('#') and not sor.startswith('    #'):
            print(sor, end="", file=f2)

    f.close()
    f2.close()


def main():
    filename = "string1.py"
    remove_comments(filename)


if __name__ == '__main__':
    main()
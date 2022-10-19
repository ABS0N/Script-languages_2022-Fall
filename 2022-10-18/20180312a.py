def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(zip(chars, list(range(ord('a'), ord('z')+1))))

    for t in codes:
        print(t)

if __name__ == '__main__':
    main()
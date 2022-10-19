def valid(text, chars):  # This function compare the text and chars characters and return the same.
    result = ""
    for i in text:
        for j in chars:
            if j == i:
                result += j

    return result


def main():
    text = input("Text:")
    chars = input("Chars:")
    result = valid(text, chars)
    print("The same chars: \"" + result + "\"")


if __name__ == '__main__':
    main()
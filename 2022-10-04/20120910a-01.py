def sound_order(word):
    height = ["e", "é", "i", "í", "ü", "ű", "ö", "ő"]
    low = ["a", "á", "o", "ó", "u", "ú"]
    result = ["magas", "mély", "vegyes", "semmilyen"]

    is_height = False
    is_low = False

    for i in word:
        if i in height:
            is_height = True
        if i in low:
            is_low = True

    if is_low == False and is_height == False:
        return result[3]
    if is_low == True and is_height == True:
        return result[2]
    if is_low == True and is_height == False:
        return result[1]
    if is_low == False and is_height == True:
        return result[0]


def main():
    word = input("Kérek egy szót:")
    print("A megadott szó " + sound_order(word) + " hangrendű")


if __name__ == '__main__':
    main()
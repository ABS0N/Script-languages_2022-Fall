from enum import Enum
class Height(Enum):
    e="e"
    é="é"
    i="i"
    í="í"
    ö="ö"
    ő="ő"
    ü="ü"
    ű="ű"

class Low(Enum):
    a="a"
    á="á"
    o="o"
    ó="ó"
    u="u"
    ú="ú"

class Sound_order(Enum):
    result1="magas"
    result2="mély"
    result3="vegyes"
    result4="semmilyen"

def sound_order2(word):
    is_height=False
    is_low=False
    for letter in word:
        for enum in Height:
            if str(letter)==enum.value:
                is_height=True
        for enum in Low:
            if str(letter)==enum.value:
                is_low=True

    if is_low == False and is_height == False:
        return Sound_order.result4.value
    if is_low == True and is_height == True:
        return Sound_order.result3.value
    if is_low == True and is_height == False:
        return Sound_order.result2.value
    if is_low == False and is_height == True:
        return Sound_order.result1.value

def main():
    word = input("Kérek egy szót:")
    print("A megadott szó " + sound_order2(word) + " hangrendű")


if __name__ == '__main__':
    main()
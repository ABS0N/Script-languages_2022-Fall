def checksum():
    f = open("input.txt", "r")
    lines = f.readlines()
    datas=[]
    differents = []
    max = 0
    result = 0

    for line_index in range(len(lines)):
        datas=lines[line_index].split()
        if len(datas)!=0:
            min = int(datas[0])
            max=0
            for number in datas:
                if max<int(number):
                    max=int(number)

                if min>int(number):
                    min=int(number)
            differents.append(max-min)
            result=result+(max-min)
    return result


def main():
    result = str(checksum())
    print("The checksum is: " + result)


if __name__ == '__main__':
    main()
def XOR(input1, input2):
    logical1=bool(input1)
    logical2=bool(input2)

    result=False

    if (logical1==True and logical2==False) or (logical1==False and logical2==True):
        result=True

    return result


def main():
    input1=input("Input1:")
    input2=input("Input2:")

    if (XOR(input1,input2)==True):
        print("XOR returned True")
    else:
        print("XOR returned False")


if __name__ == '__main__':
    main()
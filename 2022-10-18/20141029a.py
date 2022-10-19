INPUT1="""01111001
01101111
01110101
01110100
01110101
00101110
01100010
01100101
00101111
01100100
01010001
01110111
00110100
01110111
00111001
01010111
01100111
01011000
01100011
01010001"""

INPUT2="""01010011
01101111
00100000
01111001
01101111
01110101
00100000
01110100
01101111
01101111
01101011
00100000
01110100
01101000
01100101
00100000
01110100
01101001
01101101
01100101
00100000
01110100
01101111
00100000
01110100
01110010
01100001
01101110
01110011
01101100
01100001
01110100
01100101
00100000
01110100
01101000
01101001
01110011
00111111
00100000
 
01010111
01100101
00100000
01101100
01101111
01110110
01100101
00100000
01111001
01101111
01110101
00101110
"""
def decoder(INPUT):
    multiplies=[128, 64, 32, 16, 8, 4, 2, 1]
    binary_letters=INPUT.split('\n')
    ascii_code_letters=[]

    sum=0
    for i in range(len(binary_letters)):
        sum=0
        temp=binary_letters[i]
        for character_index in range(len(temp)):
            if temp[character_index]=='1':
                sum+=multiplies[character_index]
        ascii_code_letters.append(sum)

    for i in ascii_code_letters:
        print(chr(i), end="")
    print()

def main():
    decoder(INPUT1)
    decoder(INPUT2)



if __name__ == '__main__':
    main()
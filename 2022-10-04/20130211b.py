def main():
    height=input("Height of diamond (should be odd): ")
    if int(height)%2!=0:
        diamond(height)
    else:
        print("Height of diamond should be odd!")

def diamond(height):
    var='*'
    stars= []
    max = 0
    for i in range(int(height)):
        i += 1
        if i % 2 != 0:
            stars.append(var.center(i, '*'))
            if i > max:
                max = i

    max -= 2

    while max > 0:
        stars.append(var.center(max, '*'))
        max -= 2

    for i in stars:
        print(i.center(len(stars),' '))

if __name__ == '__main__':
    main()
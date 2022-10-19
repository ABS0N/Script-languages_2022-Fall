def variant():
    my_list = []
    for i in range(100):
        my_list.append(i + 1)

    sum_of_digits = 0
    for i in my_list:
        var = str(i)
        for j in range(len(var)):
            sum_of_digits += int(var[j])

    return sum_of_digits;


def main():
    var = variant()
    print("The sum of digits from 1 to 100 is:", var)


if __name__ == '__main__':
    main()
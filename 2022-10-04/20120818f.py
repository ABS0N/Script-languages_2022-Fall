def square_of_the_sum():
    sum = 0
    for i in range(100):
        sum += (i+1)

    sum=sum*sum
    return sum

def sum_of_squares():
    sum=0
    for i in range(100):
        sum+=(i+1)*(i+1)

    return sum

def main():
    result1=sum_of_squares()
    result2=square_of_the_sum()

    print("The sum of squares of the first 100 numbers: ",result1)
    print("The sum of squares of the first 100 numbers: ",result2)
    print("The difference: ",result2-result1)

if __name__ == '__main__':
    main()
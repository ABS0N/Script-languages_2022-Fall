def my_function(n):
    input = [number for number in range(n) if number % 3 == 0 or number % 5 == 0] 
    output = sum(input)
    return output

def main():
    n = 1000
    print("The sum of the numbers which are multiples of 3 and 5 from 1 to 1000 is : ", my_function(n))


if __name__ == '__main__':
    main()

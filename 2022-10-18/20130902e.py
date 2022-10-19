from typing import List, Any


def my_function(expression):
    result = True
    brackets = ["(", ")", "[", "]", "{", "}"]
    irregular_brackets = ["(]", "(}", "[)", "[}", "{)", "{]"]
    expression_brackets = []

    for character in expression:
        if character in brackets:
            expression_brackets.append(character)

    if len(expression_brackets) % 2 == 0:
        temp = expression_brackets[0]
        expression_brackets.pop(0)
        while len(expression_brackets) > 0:
            bracket1 = temp
            bracket2 = expression_brackets[0]
            expression_brackets.pop(0)
            temp = bracket1 + bracket2
            if temp in irregular_brackets:
                result = False

            temp = bracket2
    else:
        result = False

    if result:
        print("True")
    else:
        print("False")


def main():
    test1 = "((5+3)*2+1)"  # True
    test2 = "{[(3+1)+2]+}"  # True
    test3 = "(3+{1-1)}"  # False
    test4 = "[1+1]+(2*2)-{3/3}"  # True
    test5 = "(({[(((1)-2)+3)-3]/3}-3)"  # False

    my_function(test1)
    my_function(test2)
    my_function(test3)
    my_function(test4)
    my_function(test5)


if __name__ == '__main__':
    main()
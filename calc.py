def main():
    forumla = input("What do you want to do? \n")
    operator = forumla.index("+")
    firstnum = int(forumla[operator:])
    secondnum = int(forumla[:operator])
    result = addition(firstnum, secondnum)

    print(f"The answer is: {result}")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


if __name__ == '__main__':
    main()
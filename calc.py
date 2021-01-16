def main():
    formula = input('What do you want to do? \n')
    #op_index = get_operator(formula)
    op_index = 1
    operator = formula[op_index]
    numbers = formula.split('*')
    firstnum = float(numbers[0])
    secondnum = float(numbers[1])

    if operator == '+':
        result = addition(firstnum, secondnum)
    elif operator == '-':
        result = subtraction(firstnum, secondnum)
    elif operator == '*':
        result = multiplication(firstnum, secondnum)
    elif operator == '/':
        result = division(firstnum, secondnum)
    elif operator == '%':
        result = modulo(firstnum, secondnum)
    else:
        print(f'No formula found: {formula}')

    print(f'The answer is: {result}')


def get_operator(user_formula):
    return 1


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulo(a, b):
    return a % b


if __name__ == '__main__':
    main()
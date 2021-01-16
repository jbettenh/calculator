def main():
    formula = input('What do you want to do? \n')
    op_index = get_operator(formula)
    operator = formula[op_index]
    numbers = formula.split('*')
    firstnum = convert_input(numbers[0])
    secondnum = convert_input(numbers[1])

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


def convert_input(user_num):
    a = float(user_num)
    return a


def addition(a, b):
    a = convert_input(a)
    b = convert_input(b)
    return a + b


def subtraction(a, b):
    a = convert_input(a)
    b = convert_input(b)
    return a - b


def multiplication(a, b):
    a = convert_input(a)
    b = convert_input(b)
    return a * b


def division(a, b):
    a = convert_input(a)
    b = convert_input(b)
    return a / b


def modulo(a, b):
    a = convert_input(a)
    b = convert_input(b)
    return a % b


if __name__ == '__main__':
    main()
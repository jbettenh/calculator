def main():
    """
    formula = input('What do you want to do? \n')
    op_index = get_operator(formula)
    operator = formula[op_index]
    numbers = formula.split()
    firstnum = convert_input(numbers[0])
    secondnum = convert_input(numbers[1])
    """
    operator = input('What do you want to do? \n')
    first_number = convert_input(input('Enter the first number: \n'))
    second_number = convert_input(input('Enter the second number:  \n'))

    if operator == '+':
        result = addition(first_number, second_number)
    elif operator == '-':
        result = subtraction(first_number, second_number)
    elif operator == '*':
        result = multiplication(first_number, second_number)
    elif operator == '/':
        result = division(first_number, second_number)
    elif operator == '%':
        result = modulo(first_number, second_number)
    else:
        print(f'No formula found: {formula}')

    print(f'The answer is: {result}')


def get_operator(user_formula):
    return 1


def convert_input(user_num):
    try:
        number = float(user_num)
        return number
    except ValueError:
        print(f"Couldn\'t convert {user_num} to a float")


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
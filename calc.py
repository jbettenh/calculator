def main():
    formula = input('What do you want to do? \n')
    components = formula.split()
    if len(components) == 3:
        operator = components[1]
        first_number = convert_input(components[0])
        second_number = convert_input(components[2]) 

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
    else:
        print(f'No formula found: {formula}')


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
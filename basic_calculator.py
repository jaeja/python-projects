
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y
def mod(x, y):
    return x % y
def floor_divide(x, y):
    return x // y
def square_root(x):
    return x ** 0.5
def cube_root(x):
    return x ** (1/3)
def percentage(x, y):
    return (x / y) * 100

print('welcome to this calculator')
while True:
    cont = input('Type yes to continue or no to exit: ').strip().lower()
    if cont != 'yes':
        print('Exiting calculator. Goodbye!')
        break
    print('what operation do you want to perform?')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Power')
    print('6. Modulus')
    print('7. Floor Division')
    print('8. Square Root')
    print('9. Cube Root')
    print('10. Percentage')
    choice = input('Enter choice(1/2/3/4/5/6/7/8/9/10): ')
    if choice in ['1', '2', '3', '4', '6', '7', '10']:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            if num2 != 0:
                print(num1, '/', num2, '=', divide(num1, num2))
            else:
                print('Error! Division by zero.')
        elif choice == '6':
            print(num1, '%', num2, '=', mod(num1, num2))
        elif choice == '7':
            if num2 != 0:
                print(num1, '//', num2, '=', floor_divide(num1, num2))
            else:
                print('Error! Division by zero.')
        elif choice == '10':
            print(f'{num1} is {percentage(num1, num2)}% of {num2}')
    elif choice in ['5', '8', '9']:
        num = float(input('Enter number: '))
        if choice == '5':
            num2 = float(input('Enter the squared ratio: '))
            print(num, '^', num2, '=', power(num, num2))
        elif choice == '8':
            if num >= 0:
                print('Square root of', num, '=', square_root(num))
            else:
                print('Error! Square root of negative number is not defined in real numbers.')
        elif choice == '9':
            print('Cube root of', num, '=', cube_root(num))
    else:
        print('Invalid input')



        
    

num1 = int(input('Enter first number: '))
op = input('Please enter operator e.g +-*/')
num2 = int(input('Enter second number: '))

if op == '+':
    print('The addition is ', num1+num2)
elif op == '-':
    print('The subtraction is ', num1-num2)
elif op == '*':
    print('The multiplication is ', num1*num2)
elif op == '/':
    print('The division is ', num1/num2)
else:
    print('Invalid operator')        
# WAP to create a function add(), which will return addition of two numbers and print the square of calculated addition.

# def add(x, y):
#     z = x + y
#     return z
#
#
# def square(n):
#     return n ** 2
#
#
# a = int(input('Enter first number :'))
# b = int(input('Enter second number: '))
# c = add(a, b)
# print('The addition is ', c)
# print('The square of addition is ', c ** 2)
# print('The square of addition is ', square(c))


# Task 1
# WAP to read two numbers from user, and return addition,
# subtraction, multiplication and division by using return function technique

# def add(x, y):
#     return x+y
#
#
# def sub(x, y):
#     return x-y
#
#
# def div(x, y):
#     return x/y
#
#
# def mul(x, y):
#     return x*y
#
#
# n1 = int(input('Enter first number : '))
# n2 = int(input('Enter second number : '))
# print('Addition is ', add(n1, n2))
# print('Subtraction is ', sub(n1, n2))
# print('Multiplication is ', mul(n1, n2))
# print('Division is ', div(n1, n2))








# Task 2
# WAP to read a number user and print it's square using a function square()
# and assign the calculated square to new function cube() to print the cube
# of a calculated square

def square(n):
    return n**2


def cube(n):
    return n**3


a = int(input('Enter a number : '))
s = square(a)
print('Square is ', s)
print('Cube is ', cube(s))

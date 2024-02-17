# # WAP to create a function Display(), which will print "India" according to parameter.
# def Display(country):
#     for i in range(0,5):
#         print(country)
#
# print("Bharat")
# Display("India")

# def Display(country):
#     for i in range(0, 5):
#         print(country)
#
#
# inp = input('Enter the string : ')
#
# Display(inp)
# Task 1
# def Display(country,n):
#     for i in range(0, n):
#         print(country)
#
#
# inp = input('Enter the string : ')
# n = int(input('Enter number of times : '))
# Display(inp,n)


# Write a program to create a function Square(), which will print the square of a number given by user.
# O/P
# Enter the number : 5
# The Square of a number is : 25

# Task 2
# def Square(n):
#     print('The square of a number is : ',n**2)
#
# n = int(input('Enter the number : '))
# Square(n)

# Task 3
# WAP to read a number from user and print its square and cube using two different function.
# def square(n):
#     print('The square of a number is : ',n**2)
#
# def cube(n):
#     print('The cube of a number is : ',n**3)
#
# n = int(input('Enter the number : '))
# square(n)
# cube(n)

# Task 4
# WAP to read number from user and create a function Checking(),
# which will print whether the number is even or odd.
def Checking(n):
    if n%2==0:
        print('The number is even')
    else:
        print('The number is odd')


n = int(input('Enter the number : '))
Checking(n)
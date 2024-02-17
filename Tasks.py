## Tasks

## Data-types in Python

## 1. WAP that stores a text string in text_variable, displays the text, and shows its data type.
# txt_variable = input('Enter string : ')
# print(txt_variable)
# print(type(txt_variable))

## 2. WAP that stores an int number in int_variable, displays the number, and shows its data type.
# int_variable = int(input('Enter number : '))
# print(int_variable)
# print(type(int_variable))

## 3. WAP that stores a Str string in str_variable, displays the Str, and shows its data type.
# str_variable = input('Enter string : ')
# print(str_variable)
# print(type(str_variable))

## 4. WAP that stores a Float number in float_variable, displays the number, and shows its data type.
# float_variable = float(input('Enter float number : '))
# print(float_variable)
# print(type(float_variable))

## String function

## 1. WAP to calculate and print the length of a given string

## Approach 1 :

## Using len() function
# name = input('Enter name : ')
# print(len(name))
#
# # Approach 2:
#
# # Using for loop
# str_len = 0
# for i in name:
#     str_len += 1
# print("Length of String is ", str_len)
#
# # 2. WAP that takes a string as input and prints the string in uppercase
#
# # Approach 1:
#
# # Using upper() function
# str1 = input('Enter string : ')
# print("String in uppercase using upper", str1.upper())
#
# # Approach 2:
#
# # Using for chr() and ord() and for loop function
# print("String in upper case manually ")
# for i in str1:
#     if i>='a' and i<='z':
#         upper_char = chr(ord(i)-32)
#         print(upper_char,end='')
#     else:
#         print(i,end='')
#
#
# print()
# 3. WAP that reverses a given string and prints the result.

str2 = input('Enter any string : ')

print("The original string is : ", end="")
print(str2)

strg = ""
for i in str2:
    strg = i + strg

print("The reversed string(using loops) is : ", end="")
print(strg)

# 4. WAP to count and print the number of occurrences of a specific character in a string

# Approach 1:

# Using count function
str3 = input('Enter string : ')
ch = input('Search character : ')
print("Count ", str3.count(ch))

# Approach 2:

# Using for loop
c = 0
for i in str3:
    if i == ch:
        c += 1

print('Count is ', c)

# 5. WAP to extract a substring from a given string, given the start and end indices.
str4 = input('Enter the string : ')
start = int(input('Enter start index : '))
end = int(input('Enter end index : '))

# Approach 1
new_str = str4[start:end + 1]
print("New String ", new_str)

# Approach 2
new_str = ""
i = 0
while i < len(str4):
    if i in range(start, end + 1):
        new_str = new_str + str4[i]
    i += 1
print("New String ", new_str)

# Operators in Python

# 1. Arithmetic Operators:

# 1. WAP that takes two numbers as input from the user and calculates their sum. Display the result.
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
addition = n1 + n2
print("Sum is ", addition)

# 2. WAP that prompts the user for two numbers and calculates their difference
# ( subtract the second number from the first ). Display the result
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
sub = n1 - n2
print("Subtraction is ", sub)

# 3. WAP that prompts the user for two numbers and computes their product ( multiplication ). Display the result
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
mul = n1 * n2
print("Multiplication is ", mul)

# 4. Write a Python program (WAP) that takes two numbers as input
# and divides the first number by the second. Handle cases where
# the denominator is zero and display the result.
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
if n2 == 0:
    print('Cannot divide a number by zero')
else:
    div = n1 / n2
    print("Division is ", div)

# 5. Write a Python program (WAP) that reads two numbers from
# the user and calculates the remainder when the first number is
# divided by the second. Display the remainder.
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))

mod = n1 % n2
print("Modulus is ", mod)

# 2. Comparison Operators:

# 1. Write a Python program that prompts the user to enter two
# numbers and checks if they are equal using the == operator.
# Print a message indicating whether the numbers are equal or
# not.
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))

if n1 == n2:
    print('Numbers are equal')
else:
    print('Numbers are not equal')

# 2.  Create a Python program that takes an integer input and checks
# if it is not equal to a predefined constant value using the !=
# operator. Display a message based on the result

constant = 10
n = int(input('Enter any number : '))
if n != constant:
    print('Number is not equal to constant')
else:
    print('Number is equal to constant')

# 3. Write a Python program that calculates the sum of two
# numbers and checks if the result is greater than a specified
# threshold using the > operator. Print a message based on the
# comparison result.

threshold = 100
n1 = int(input('Enter 1st number : '))
n2 = int(input('Enter 2nd number : '))
addition = n1 + n2
if addition > threshold:
    print('Addition of both numbers are greater than the threshold value(100).')
else:
    print('Addition of both numbers are less than the threshold value.')

# 4. . Develop a Python program that prompts the user to enter their
# age and checks if it's less than a legal voting age (e.g., 18) using
# the < operator. Display whether the user is eligible to vote or
# not

age = int(input('Enter your age : '))
if age < 18:
    print('You are not eligible for voting')
else:
    print('You are eligible for voting')

# 5. Create a Python program that calculates the square of a number
# and checks if it's greater than or equal to a predefined constant
# using the >= operator. Print a message based on the
# comparison result

n = int(input('Enter a number : '))
constant = 100
if n**2 >= constant:
    print('The square of number is greater than 100')
else:
    print('The square of number is less than 100')

# 3. Logical Operators:

# 1. Logical AND

# 1. WAP that prompts the user to enter their age and checks if they are both above 18 years old and have a
# valid ID using the logical and operator. Print a message
# indicating if they are eligible for entry.



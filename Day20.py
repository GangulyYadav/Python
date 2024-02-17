# String operations
# 1. len() - count length of string
# name = 'Ganguly Ramkrishnbhai Yadav'
# print(len(name))

# 2. upper() - convert all the characters into uppercase
# print(name.upper())

# 3. lower() - convert all the characters to lowercase
# print(name.lower())

# 4. capitalize() - the first character of the line will be capital
# print(name.capitalize())

# 5. title() - each words first character is capital
# print(name.title())

# 6. replace() - can replace entire string or character
# print(name.replace(name,'yadav'))

# WAP to replace a string laksh with daksh
# a = 'laksh'
# d = a.replace('l','d')
# print(d)
# print(a)

# 7. split() - used to separate the string in different pieces
# print(name.split(' '))

# Write a program to split the data using separator #
# a= 'Ganguly#95294937978#yadavganguly77@gmail.com#Mumbai'
# print(a.split('#'))

# 8. count() - count the number of occurrences for given character in a string\
# syntax
# 1. str.count(char)
# 2. str.count(char,beginning)
# print(name.count('G'))
# print(name.lower().count('g'))


# WAP to count the occurrences of given character in a string
# Enter the string :
# Enter the character to count :
# a = input('Enter the string : ')
# ch = input('Enter the character to count : ')
# print("Total occurrences ",a.count(ch))

# use of syntax to
# print("Total occurrences ",a.count(ch,2))

# 9. find() - used to search the char or string & return position if found
# returns the first occurrence and skips remaining string
# Syntax
# 1. string.find(char)
# 2. string.find(char,beginning)
# name='Ganguly'
# print(name.find('a'))
# print("Character found at",name.find('a',2))



# Task 1
# Enter the string : india
# Enter the character to search : i
# Position Number : 0
# Position Number: 3
# Without using the find()
# stringInput = input('Enter the string : ')
# searchChar = input('Enter the character to search : ')
# i = 0
# while i<len(stringInput):
#     if stringInput[i] == searchChar:
#         print("Position Number : ",i)
#     i+=1
#
# # Using find()
# stringInput = input('Enter the string : ')
# searchChar = input('Enter the character to search : ')
# i=0
# while(i<len(stringInput)):
#     position = stringInput.find(searchChar,i)
#     if position!=-1:
#         print("Position Number : ",position)
#         i = position+1
#     else:
#         i+=1




























# Task 2
# Enter the first number : 10
# Enter the second number : 50

# The list of all even number in the series
# 10 12 14

num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the second number : '))

for i in range(num1,num2+1):
    if i%2==0:
        print(i)














        
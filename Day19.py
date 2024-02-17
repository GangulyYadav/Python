# Task 1
# 1. WAP to read a string from user and print total character 'a'
# Enter the string : bharat
# Total occurrences of a is : 2

# userInput = input('Enter the string : ')
# count = 0
#
# for i in userInput.lower():
#     if i=='a':
#         count+=1
# print(count)

# Task 2
# Enter the string : India is my country
# Enter the character to search : y
# Total occurrences : 2

userInput = input('Enter the string : ')
searchChar = input('Enter the character to search : ')
count = 0

for i in userInput.lower():
    if i==searchChar.lower():
        count+=1
print(count)


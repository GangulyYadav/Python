# i = 1
# while(i<=5):
#     print(i)
#     i+=1

# WAP to print a series from 11 to 20
# i = 11
# while(i<=20):
#     print(i)
#     i+=1
# i = 5
# while(i>=1):
#     print(i)
#     i-=1

# WAP to read a number from user and print the word "India" till number times.
# i=1
# n = int(input('Enter the number: '))
# while(i<=n):
#     print('India')
#     i+=1

# Task 1
# WAP to read two number from user and print the sequence between them
# a = int(input('Enter the first number:'))
# b = int(input('Enter the second number:'))
# while(a<=b):
#     print(a)
#     a+=1








# Task 2
# Convert all the for loop example in while loop

# Task 1
# WAP to print "India" word 20 times using for loop
# for i in range(20):
#     print("India")

# i=1
# while(i<=20):
#     print("India")
#     i+=1

# Task 2
# WAP to print the squares of series 1 to 10
# for i in range(1,11):
#     print(i*i)
#
# i=1
# while(i<=10):
#     print(i**2)
#     i+=1


# Task 3
# WAP to print the cube of series 1 to 10
# for i in range(1,11):
#     print(i*i*i)
# i=1
# while(i<=10):
#     print(i**3)
#     i+=1


# Task 4
# WAP to read a number & print the sum from 1 to that number
# n = int(input('Enter the number : '))
# sumResult = 0
# for i in range(1,n+1):
#     sumResult += i
# print('Sum of numbers till given number is ',sumResult)

# i=1
# sumResult = 0
# n=int(input('Enter the number : '))
# while(i<=n):
#     sumResult += i
#     i+=1
# print('Sum of numbers till given number is ',sumResult)


# Task 5
# WAP to read a name and print the length of that string.
# Enter the name: Ram
# Length of string is : 3
# name = input('Enter the name : ')
# nameLen = 0
# for i in name:
#     nameLen += 1
# print('Length of string is :',nameLen)


name = input('Enter the name : ')
nameLen = 0
while(name):
    nameLen += 1
    name = name[1:]
print('Length of string is :',nameLen)
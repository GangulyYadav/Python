# Write a program to find second minimum of 3 numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
print(f'{a} is second min number') if (a < b and a>c) or (a>b and a<c) else print(f'{b} is second min number.') if (b>c and b<a) or (b<c and b>a) else print(f'{c} is second min number.')

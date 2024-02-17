# Write a program to do the sum of first and last digit of number
n = int(input('Enter number : '))
last = n%10
first = 0
while n > 0:
    first = n%10
    n=n//10
print(f'Sum of fist and last digit is : {first+last}')
    

#Write a program to reverse a given number
n = int(input('Enter number : '))
rn = 0
while n>0:
    r = n%10
    rn = (rn*10)+r
    n = n//10
print(f"Reversed number is : {rn}")
    
            

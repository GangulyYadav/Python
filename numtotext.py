# Write a program to display the number names of the digits of a number entered by
# user, for ex. 231 then op: Two Three One
n = int(input('Enter number : '))
rn=0
rev = n[::-1]
while n>0:
    d = n%10
    rn = (rn*10)+d
    n = n//10

while rn>0:
    d = rn%10
    rn = rn//10
    if d==1:
        print("One",end=" ")
    elif d==2:
        print("Two",end=" ")
    elif d==3:
        print("Three",end=" ")
    elif d==4:
        print("Four",end=" ")
    elif d==5:
        print("Five",end=" ")
    elif d==6:
        print("Six",end=" ")
    elif d==7:
        print("Seven",end=" ")
    elif d==8:
        print("Eight",end=" ")
    elif d==9:
        print("Nine",end=" ")
    else:
        print("Zero",end=" ")

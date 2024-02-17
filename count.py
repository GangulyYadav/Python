# Write a program to count alphabets, digits and specials characters in given string
str1 = input('Enter the string : ')
ac = 0
dc = 0
sc = 0
for ch in str1:
    if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1
print(f'Count of aphabets {ac} and digits {dc} and special character {sc}')

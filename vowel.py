#Write a program to count vowel in given string
str1 = input('Enter string : ')
c = 0
for ch in str1:
    if ch in 'aeiouAEIOU':
        c+=1
print(f'There are {c} vowels.')
        

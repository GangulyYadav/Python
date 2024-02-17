# Write a program to find whether the input year is leap year or not
year = int(input('Enter year: '))
print(f'{year} is leap year.') if year % 4 == 0 else print(f'{year} is not leap year.')

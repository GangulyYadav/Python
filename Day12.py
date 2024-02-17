# a=10
# a=+2
# print(a)

# Task
# Enter the Salary Amount : 10000
# Basic Salary : 5000               salary 50%
# Home Allowance : 2000             Basic Salary 40%
# Other Expenses : 3000             Remaining
#

salary = int(input('Enter the Salary Amount :'))
base = salary*50/100
print('Basic Salary :',base)
ha = base*40/100
print('Home Allowance :',ha)
other = salary - base - ha
print('Other Expenses :',other)
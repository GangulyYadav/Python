# salary = int(input('Enter the salary : '))
# bonus1 = 1000
# bonus2 = 2000
# bonus3 = 3000
# travel = 2000
# tax = 500
#
# if(salary>=10000):
#     p = salary + bonus1 -tax
#     print('Total Salary :',p)
# else:
#     if(salary<5000):
#         p = salary + bonus3 + travel
#         print('Total Salary including bonus and travelling :',p)
#     else:
#         p = salary + bonus2
#         print('Total salary including only bonus :',p)

#
# Task 1
# Enter the package amount : 120000
# Your monthly salary is : 10000

# salary = int(input('Enter the package amount : '))
# print('Your monthly salary is :',salary/12)


# Task 2
# salary = float(input('Enter the package amount : '))
# print('Your monthly salary is :',salary*100000/12)


# Task 3
# Enter the package amount : 120000
# Your monthly salary is : 10000
# Basic salary : 5000
# Home allowance : 40% of basic salary
# Other Expenses :

salary = int(input('Enter the package amount :'))
monthly_sal = salary/12
basic_sal = monthly_sal * 0.5
ha = basic_sal * 0.4
other_expenses = basic_sal - ha
print('Your monthly salary is :',monthly_sal)
print('Basic Salary :',basic_sal)
print('Home allowance is :',ha)
print('Other expenses :',other_expenses)

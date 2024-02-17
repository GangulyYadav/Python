# WAP to read age from user and check whether the user is eligible for voting or not. if age is greater than 150 then print "invalid age"

# age = int(input('Enter the age :'))


# WAP to read marks from student, check whether the student is pass or fail
# and if the marks greater than or equal to 75 then print "Student pass with distincation"
#
# marks = int(input('Enter your marks:'))
#
# if(marks>=35):
#     if(marks>=75):
#         print('Student Pass with Distinction')
#     else:
#         print('Student is pass')
# else:
#     print('Student is fail')


# Task 1
# WAP to read salary and gender from user. if gender is male then bonus is 10%,
# if gender is female then bonus is 20 %
# Enter the salary : 10000
# Enter th Gender : Male

# Total salary with bonus : 11000

# Enter the salary : 10000
# Enter th Gender : Female

# Total salary with bonus : 12000

# salary = int(input('Enter the salary : '))
# gender = input('Enter the Gender : ')
#
# if(gender=="Male"):
#     print('Total salary with bonus : ',salary+(salary*10)/100)
# else:
#     print('Total salary with bonus : ',salary+(salary*20)/100)

# Task 2
# WAP to read salary and gender from employee. if gender is male then bonus is 10%
# if gender is female then bonus is 20%. also deduct the tax of Rs.550/- from every employee.
salary = int(input('Enter the salary : '))
gender = input('Enter the Gender : ')

if(gender=="Male"):
    print('Total salary with tax deduction : ',salary-550+(salary*10)/100)
else:
    print('Total salary with tax deduction : ',salary-550+(salary*20)/100)

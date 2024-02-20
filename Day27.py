# Day 27
# 19th Feb 2024
# Tuple
# It is created using ()
# It's items are ordered/sequence
# It is immutable
# Tuple allows duplicates

# Creating a tuple
# t1 = (1,'2,',"Ganguly","Ganguly",1)
# print(t1)
#
# print(t1[2])

# WAP to create two tuple and join it

# t = ('Ganguly',101,36)
# t2 = ('Yadav',102,99)
# t3 = t + t2
# print(t3)

# Slicing tuple
#
# t_name = ("Ram","Shyam","Vaishnav","Anuj","Hari","Vithhal","Mauli","Krishna")
# print(t_name)
#
# print(t_name[3:1])
#
# print(t_name[3:6])

# Reversing tuple
# syntax : tuplename[::-1]
# print(t_name[::-1])
#
# print(t_name[::-2])

# Task
# 1. WAP to print the cube of all the items in tuple
print('Task 1 : Printing cube of all the items in tuple')
t_num = (10,20,30,40,50)
for i in t_num:
    print(i**3)

# 2. WAP to print sum of all the tuple item
print('\nTask 2 : Doing sum of all the tuple item')
add = 0
for i in t_num:
    add += i
print('\nAddition is : ',add)

# 3. WAP to print the square of all the tuple items
print('\nTask 3 : Printing square of tuple items')
for i in t_num:
    print(i**2)

# 4. WAP to print the tuple in reverse order without using ::-1
print('\nTask 4 : Printing Tuple in Reverse Ordered')
for i in range(len(t_num)-1,-1,-1):
    print(t_num[i])


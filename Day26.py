# empid_list = [145,121,123,111,198]
# print(empid_list)

# Write a program to create a list of 5 empid and access position no. 2
# print(empid_list[2])

# WAP to update the value of empid at position 2
# empid_list[2] = "Ganguly Yadav"
# empid_list[2] = 2.2
# print(empid_list)

# WAP to create a list of 5 empid and delete the value of position no. 1
# del empid_list[1]
# print(empid_list)

# print(empid_list[1])
# del empid_list
# print(empid_list)  # can't do if the list is deleted

# Functions of list
# 1. len(list) - It gives the total length of the list.
# print("Length of the list is ", len(empid_list))

# The list must be of same type
# l1 = ['a','b','c','d','e',"Ganguly"]
# 2. min(list) - Returns item from the list with minimum value.
# print(min(empid_list))
# print(min(l1))

# 3. max(list) - Returns item from the list with maximum value.
# print(max(empid_list))
# print(max(l1))
#
# bl = [True,False,0,1]
# print(min(bl))
# print(max(bl))

# Task 1
# WAP to create a list of 5 number, and print the sum of any two number
list1 = [10,20,9,38,59]
print("Sum of any two number from list is :", list1[0]+list1[3])

# Task 2
# WAP to create a list of 5 numbers and print the square and cube of any one.
list2 = [8,5,9,2,3]
print("Square is ",list2[1]**2)
print("Cube is ",list2[1]**3)

# Task 3
# WAP to create a list of 5 numbers and print the addition of square and cube a number
list3 = [2,4,6,3,1]
print("Addition of square and cube is ", list3[0]**2 + list3[0]**3)
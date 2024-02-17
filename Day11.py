# WAP to read OTP from user and check whether the OTP is valid or not
# OTP = 4563
# RecievedOTP = int(input("Enter OTP "))
# print("Valid OTP: ",OTP==RecievedOTP)





# Task 1
# product = input('Enter the product name : ')
# cost = int(input('Enter the product cost : '))
# quantity = int(input('Enter the quantity: '))
# print('\nFinal bill amount is :',cost*quantity)
#
#




# Task 2
# product = input('Enter the product name : ')
# cost = int(input('Enter the product cost : '))
# quantity = int(input('Enter the quantity: '))
# discount=int(input('Enter the discount: '))
# print('\nFinal bill amount is :',(cost*quantity)-discount)





# task 3
product = input('Enter the product name : ')
cost = int(input('Enter the product cost : '))
quantity = int(input('Enter the quantity: '))
discount=int(input('Enter the discount: '))
tax = int(input('Enter the tax percentage: '))
print('\nFinal bill amount is :',(cost*quantity)-discount+(cost*quantity*tax/100))
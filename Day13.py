# age = int(input('Enter the age :'))
#
# print('Eligible for NDA Admission :',age>=17 and age<=21)

# username = input('Enter the username :')
# password = input('Enter the password :')
# print('Valid user :',username=="admin" and password=="super")

# WAP to read adhar card and pan card status from user and check whether the user is eligible to open bank acc or not.
# Criteria : any one document is compulsory

# adhar = input('Do you have aadhar :')
# pan = input('Do you have PAN :')
# print("Eligible to open account :",adhar=="yes" or pan=="yes")

# WAP to read adhar card and pan card and license status from user
# and check whether the user is eligible to take bike insurance or not. (License is compulsory)

# adhar = input('Do you have aadhar :')
# pan = input('Do you have PAN :')
# licenseStatus = input('Do you have license :')
#
# check = (adhar=="yes" or pan=="yes") and licenseStatus =="yes"
# print("Eligible to take bike insurance",check)
#








# 2. Choose any one subject each from two criteria's
# Language                      Practical Subject
# 1. Marathi                    1. Physics
# 2. English                    2. Chemistry

# Choose Subject for language: marathi
# Choose subject for practical : physics
# Subject confirm : True

language = input('Choose Subject for language :')
subject = input('Choose subject for practical :')
check = (language=="Marathi" or language == "English") and (subject=="Physics" or subject=="Chemistry")
print('Subject confirm :',check)
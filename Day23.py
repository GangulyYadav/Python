# def Display():                        # Function Definition/ Called function
#     for i in range(1,11):
#         print("India")

# Main Program
# Display()  # Calling Function
# print("Bharat")
# Display()
# print("Maharashtra")
# Display()

# Task 1
# WAP to create a function Display(), which can print the word "Maharashtra" 5 times.

# Task 2
# India
# ***
# Maharashtra
# *****
# Amravati
# *******
# WAP to create a function Numbers(), which can print a series from 1 to 10

def Display():
    for i in range(0,5):
        print("Maharashtra")

print('Task 1')
Display()
# -------------------------------------------
def star(num):
    for i in range(0,num):
        print('*', end=' ')
    print()

print('Task 2')
print('India')
star(3)
print('Maharashtra')
star(5)
print('Amravati')
star(7)
# -------------------------------------------
print('Task 3')
def Numbers():
    for i in range(1,11):
        print(i)

Numbers()
print('India')
Numbers()
print('Maharashtra')


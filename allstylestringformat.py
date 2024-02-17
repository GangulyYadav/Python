# Python program to print a number using formatting style
# There are three formatting style in python
# 1. Old style or C style string formatting
# 2. New Style string formatting
# 3. F-string formatting

a = int(input('Enter a'))
print("a = %d"%(a))
print("a = {}".format(a))
print(f"a  = {a:+d}")

# WAP to read number from command line arguments and do their addition
import sys
# We can read the command line argument from the argv object/variable of the sys module
# By default the command line arguments are received in string format
# The first command line argument contains the filename with full path
print(f"You are running {sys.argv[0]}")
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f"Sum of {n1} and {n2} is {n1+n2:+d}")

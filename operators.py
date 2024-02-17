# each varible is considered as an object in python and each object is having certain
# properties and methods 
x=100
y=200
print(x+y)

print(x.__add__(y))
#print(100.__add__(200))
# SyntaxError: invalid decimal literal
print(x.__add__(200))

print(int(100).__add__(200))

print(int(100).__add__(int(200).__add__(300)))

print(int(10).__mul__(20))

print("Hello"*10)
list1=[10,20,30]
print(list1)
list2=list1*2
print(list2)

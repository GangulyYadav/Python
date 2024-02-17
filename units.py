units = int(input('Enter the number of units : '))
if units<=100:
    print(f'Bill amount 0')
elif units>100 and units<=200:
    print(f'Bill amount {(units-100)*5}')
else:
    print(f'Bill amount {500+(units-200)*10}')
    

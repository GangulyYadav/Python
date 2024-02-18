# Pattern 5
for r in range(1,5):
    for c in range(5,0,-1):
        if c <= r:
            print(c,end='')
        else:
            print(' ',end='')
    print()
        

# Pattern 6
for r in range(1,5):
    for c in range(4,0,-1):
        if c>r:
            print(' ',end='')
        else:
            print(5-c,end='')
    print()

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(1,5):
    for j in range(1,1+i):
        print(' ',end='')
    for j in range(1,6-i):
        print(j,end=' ')
    print()


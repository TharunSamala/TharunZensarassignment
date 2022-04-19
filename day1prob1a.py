k=0
for i in range(1,5):
    for j in range(i,i*2):
        if k<=8:
            k+=1
            print(k,end='')
        else:
            print(0)
    print()
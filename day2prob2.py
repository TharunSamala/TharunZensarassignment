for i in range(1,501):
    sum=0
    for j in range(0,len(str(i))):
        sum+=int(str(i)[j])**3
    if sum==i:
        print(i,end=" ")
count=0
print("Those five numbers are:")
for i in range(1,501):
    if i%3==1:
        a=2*((i-1)//3)
        if a%3==1:
            b=2 * ((a - 1) // 3)
            if b%3==1:
                c=2*((b-1)//3)
                if c%3==0:
                    print(i,end=',')
                    count+=1
                    if count==5:
                        break



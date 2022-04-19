a=0
b=1
terms=int(input('enter the number of terms to be printed:'))
if terms<=0:
    print('enter the correct number')
elif terms==1:
    print(a)
elif terms==2:
    print(a,end=',')
    print(b)
else:
    print(a,end=",")
    print(b,end=',')
    for i in range(2,terms):
        c=a+b
        print(c,end=',')
        a=b
        b=c


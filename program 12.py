n=int(input("enter the limit"))
s=0
for i in range(1,n+1):
    print ("enter",i,end='')
    a=int ( input("th number :"))
    s=s+a
avg=s/n
print("the sum of entered numbers :",s)
print("the average of entered numbers :",avg)

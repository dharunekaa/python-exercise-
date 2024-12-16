n=int (input("enter the limit less than 99999999999"))
small=99999999999
for i in range(1,n+1):
    print ("enter",i,end='')
    a=int(input("the number:"))
    if a<small :
        small=a
print("smallest no.is :",small)

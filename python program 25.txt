tp1=eval(input("enter tuple:"))
length=len(tp1)
mean=sum=0
for i in range(0,length):
    sum+=tp1[i]
mean=sum/length
print("given tuple is:",tp1)
print("the mean of given tuple is:",mean)


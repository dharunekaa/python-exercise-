l=[2,58,95,999,65,32,15,1,7,45]
n=int(input("enter the number to be searched :"))
found=0
for x in l:
    if x==n:
        print("item found at position :",l.index(n)+1)
        found=1
    if found==0:
        print("item not found")

              

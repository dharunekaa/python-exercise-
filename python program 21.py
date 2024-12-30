l=[1,2,"two",3,4,"four",5]
s=0
for x in l:
    if type(x)==int:
        s=s+x
print("the sum of integers is:",s)

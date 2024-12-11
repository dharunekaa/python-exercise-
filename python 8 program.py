a=int (input("enter 1st number:"))
b=int (input("enter 2st number:"))
c=input("enter the operation +,-,/,*:")
print("the result is:",end='')
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='*':
    print(a*b)
else:
    print("eoor:wrog poerator entered")


d=int (input("enter number of days:"))
fine=0
if(d<=5):
        fine=d*0.50
        print("fine:",float(fine))
elif(d>5 and d<=10):  
        i=d-5
        fine=(i*5)+(5*0.5)
        print("fine:",float(fine))
elif(d>10 and d<=30):
        i=d-10
        fine=(i*5)+(5*0.5)+(5*1)
        print("fine amount:",float(fine))
else:
        i=d-10
        fine=(i*5)+(5*0.5)+(5+1)
        print("your membership is cancelled")
        print("fine amount(Rs):",float(fine))


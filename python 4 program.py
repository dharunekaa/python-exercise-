import datetime
td=0
now=datetime.datetime.now()
print(now.day)
if now.month==2:
    td=28
elif now.month in(1,3,5,7,8,10,12):
    td=31
else:
    td=30
print("total remaining days in the current month are :",td-now.days)

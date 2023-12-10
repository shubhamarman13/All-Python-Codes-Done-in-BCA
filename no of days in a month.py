x=int(input("enter the month no to know the no of days\n "))
if x==1 or x%2==1:
    print(" it has 31 days ")
elif x==2:
    print("exception and it has 28 days ")

else:
    print("it has 30 days ")
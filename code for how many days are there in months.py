x=int(input("Enter the month number = "))
if x%2==1:
    print(x," has 31 days ")

if x%2==0:
    print(x," has 30 days ")
if x==2:
    print("but",x," is february so it is exception , it has 28 or 29 days")
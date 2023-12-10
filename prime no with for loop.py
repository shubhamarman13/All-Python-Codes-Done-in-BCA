#how to find the prime no with the help of for loop 

num=int(input("enter the number "))
i=2
f=0
while i<+num/2:
    if(num%i==0):
        f=1
        break
if(f==0):
    print(num,"is prime")
else:
    print(num,"is not a prime ")
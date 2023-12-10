# code to check a number is prime or not

n=int(input("enter the number \n"))
count=0   # ye count karega factor ko
i=1     # ye  1 se start hai kyu ki one se count krenge hm factor ko
while i<=n:    # yaha n hoga jo user number input krega wahi
    if n%i==0:
        count = count + 1

    i=i+1
if count==2:
    print("prime")
else:
    print("not prime")
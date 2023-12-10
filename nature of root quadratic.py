print(" we will find the nature of root through this code ")
print("The formula is b**b-4ac")
b=int(input("Enter the value of b\n"))
a=int(input("Enter the value of a\n"))
c=int(input("Enter the value of c\n"))
z=(b**b)-4*a*c
print(z)
if z<0:
    print("imaginary root")
else:
    print("real roots ")
'''A shop will give discount of 10% if the cost of purchased quantity is 100 or more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''
print(" One unit cost 100 rupees")
x= int(input("Enter the quantity you want to purches= "))
y= x*100
if y>=1000:
    print("The amout is=",y-y/100*10)
else:
    print(" The amount is =",y)
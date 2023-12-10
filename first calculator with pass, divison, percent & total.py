x=float(input(" Enter the marks of Maths="))
y=float(input(" Enter the marks of english="))
z=float(input(" Enter the marks of python="))
a=float(input(" Enter the marks of  IT & information="))
b=float(input(" Enter the marks of P.M.O="))
m=x+y+z+a+b
if m>175:
    print(" Pass")
if m<175:
    print("fail")
if m in range(175,249):
 print(" 3rd divison")

if m in range(250, 324):
      print("2nd division")
if m in range(325, 500):
        print(" first divison")

total=m
print("Total marks =",total)
percent=((m/500)*100)
print("Percentage is =",percent)
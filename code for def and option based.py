# code for the def function.. 
def add():
    x= int(input("enter the number="))
    y=int(input("enter the number ="))
    print("sum is = ", x+y)

def sub():
    x= int(input("enter the number"))
    y=int(input("enter the number"))
    print("substraction is=",x-y)
def mult():
    x= int(input(" enter the number="))
    y=int(input("enter the number ="))
    print("multiplication is =",x*y)
def divi():
    x = int(input(" enter the number="))
    y = int(input("enter the number ="))
    print("divison is =", x/y)
def else1():
    print("incorrect choice\n Try again" )
def menu():
    print("\t welcome\n\t___________")
    print("\n salect any option from given\n\t1=add\n\t2=sub\n\t3=multiplication\n\t4=divide")
    x=int(input("enter your choice="))
    if x==1:
        add()
    elif x==2:
        sub()
    elif x==3:
        mult()
    elif x==4:
        divi()
    else:
        else1()
menu()
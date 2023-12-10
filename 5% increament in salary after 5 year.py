'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount '''

print(" Those who have completed 5 years in this company")
x=float(input(" Enter the amout of your salary="))
y=int(input("Enter the no. of years you spend in this company="))
if y>=5:
    print(" Your new salary is =",x+x/100*5)
else:
    print("You have not spend much time in this company \n Your salary is = ",x)
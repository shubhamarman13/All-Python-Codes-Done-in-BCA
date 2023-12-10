#format of name, roll, m1,m2,m3...(marks),"____", avg,total print
name=input("enter name=")
rollno=int(input("enter roll="))
m1=int(input("enter marks 1="))
m2=int(input("enter marks 2="))
m3=int(input("entr marks 3="))
x="---------"
total=(m1+m2+m3)
avg=(m1+m2+m3)/3
print("name:\t%s\nrollno:\t%s\nm1:\t%d\nm2:\t%d\nm3:\t%d\n___________:\t%s\ntotal:\t%d\navg:\t%d\n"%(name,rollno,m1,m2,m3,"",total,avg))
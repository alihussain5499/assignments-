l=[1,3,"f",7]
l1=["a","d","f",9]
l2=l1+l
l2

l2.pop(2)
l2.pop(4)


l3=[1,2,3,4,5]
l3.reverse()
l3

#take  a number reverse it and square each digit and add# 
l=[5,2]
l.reverse()
l
print((l[0]*l[0])+(l[1]*l[1]))


#take a number from user and reverse it and square each digit and add# 
num=input("enter any number  ")
reverse_num=num[-1::-1]
print(reverse_num)
length=len(num)
sum=0
for i in range(0,length):
    num_int=int(num[i])
    num_int=num_int*num_int
    sum=sum+num_int
print(sum)    

#add two numbers with taking input from user , take operator input with user#
a=int(input("enter first number  "))
op=input("enter operator    ")
b=int(input("enter second number  "))
if op=='+':
    print(a+b)    
elif op=="-":
    print(a-b)
elif op=="*"  :
    print(a*b)
elif op=="/":
    print(a/b) 
else:
    print("wrong ")    

#wap to write  a month of a particular year#
import calendar
a=int(input("enetr year "))
b=int(input("enetr month "))
print(calendar.month(a,b))

import calendar
print(calendar.calendar(2017))

#wap to write day  of a month of a particular year #
import datetime
year=int(input("enetr year "))
month=int(input("enetr month "))
date=int(input("enter date   "))
mydate=datetime.date(year,month,date)
print(mydate.strftime("%A"))

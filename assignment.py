name="os isssss"
name.lstrip('os').rstrip()

name="osisssss"
name.lstrip('os').rstrip()

name="os is os how os is os"
name.count("os")

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num2 = num1 +num2
print(num2)

n1=10
n2=20
n2=n1+n2
print(n2)

name="  hi hello how are u  u u u u u u u u u u"
name.count("u")

for i in range(1,9):
    print(i,end="")

var_name=input("enter any string   ")
c=len(var_name)
for i in range(0,c):
    print(var_name[i]+" "+var_name[-i-1])
    c-=1
    
var_string=input("enter any string     ")
for vowel  in var_string :
    if vowel in["a","e","i","o","u"]:
        var_string=var_string.replace(vowel,"")
print(var_string)


var_string=input("enter any string      ")
count=0
for vowel  in var_string :
    if vowel in["a","e","i","o","u"]:
        var_string=var_string.replace(vowel,"")
        count+=1
print(count)

for i in range (0,9):
    for j in range (0,9):
        if(i==0 or i==8 or j==0 or j==8):
            print("",end=" ")
            print(" ")
        elif  (i==1 or i==7 or j==1 or j==7):
            print("4",end=" ")
        elif  (i==2 or i==6 or j==2 or j==6):
            print("3",end=" ")
        elif  (i==3 or i==5 or j==3 or j==5):
            print("2",end=" ")
        elif  (i==4 or i==4 or j==4 or j==4):
            print("1",end=" ")   
        else:
            print(" ")
            
def get_sum(a, b):
    while b:
        a, b = (a ^ b), (a & b) << 1
    return a 

get_sum(5,6)
      
for i in  range(1,8):
     if(i==1): 
        print("1","","","","","","","1",end=" ")
        for j in range(1,8):
            if(i==2):
                print("\n ","2","","","","2",end=" ")  
            elif(i==3):
                print(" \n  ","3","","3",end="")
            elif(i==4 or j==4):
                 print("\n   ","4",end="")
            elif(i==3 or i==5 or j==5 or j==3):
                print(" \n  ","3","","3",end="")
            elif(i== 2 or i==6 or j==2 or j==6):
                print("\n ","2","","","","2",end=" ")  
            elif( i==7 or  j==7):
                print("\n1","","","","","","","1",end=" ")
            
            
            
            
            
            
            
            
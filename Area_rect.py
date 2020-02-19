# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 08:48:56 2018

@author: ali hussain
"""

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
a=int(input("Enter length  :"))
b=int(input("Enter breadth :")) 

obj=Rectangle(a,b)
print(obj.area())   
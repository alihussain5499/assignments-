# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:15:05 2018

@author: ali hussain
"""

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))


s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("%0.2f"%area)
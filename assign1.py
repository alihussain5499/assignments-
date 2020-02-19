# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:02:49 2019

@author: ali hussain
"""

def tfidf(x):
    from sklearn.feature_extraction.text import TfidfVectorizer
    v=TfidfVectorizer()
    ftr=v.fit_transform(x)
    return ftr.toarray()




f=open("D:/mystuff/commentsss.txt")
lines=f.readlines()
text=[]
labels=[]
for line in lines:
    w=line.lower().strip().split(",")
    text.append(w[0])
    labels.append(w[1])
    
    
    
tfidf(text)    
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:12:39 2016

@author: nhern121
"""

def countways(n):
    if n<0:
        return 0
    elif (n==0):
        return 1
    else:
        return countways(n-1)+countways(n-2)+countways(n-3)

vec={}
for i in range(1,501):
    vec[i]=-1

def countwaysDP(n,vec):
    if n<0:
        return 0
    elif n==0:
        return 1
    elif vec[n]>-1:
        return vec[n]
    else:
        vec[n]=countwaysDP(n-1,vec)+countwaysDP(n-2,vec)+countwaysDP(n-3,vec)
    return vec[n]
    

countwaysDP(500,vec)
-[]
###############################################################################
def magicFast(v,start,end):
    if (end<start | start <0 | end>len(v)):
        return -1
    mid=(start+end)/2
    if (v[mid]==mid):
        return mid
    elif (v[mid]>mid):
        return magicFast(v,start,mid-1)
    else:
        return magicFast(v,mid+1,end)
    
    
v=[-40,-20,-1,1,2,3,5,7,9,12,13]

magicFast(v,0,10)

###############################################################################
def getAllSubsets(lst):
    if not lst:
        return [[]]
    withFirst = [ [lst[0]] + rest for rest in getAllSubsets(lst[1:]) ]
    withoutFirst = getAllSubsets(lst[1:])
    return withFirst + withoutFirst
###############################################################################
def getPerms(string):
    if not string:
        return 0
    perms=[]
    if len(string)==0:
        perms.append("")
        return perms
    first=string[0]
    remainder=string[1:len(string)]
    words=getPerms(remainder)
    for word in words:
        for j in range(0,len(word)):
            s=insertChart(word,first,j)
            perms.append(s)
    return perms
    
def insertChart(word,c,i):
    start=word[0:i]
    end=word[i]
    return start+c+end
###############################################################################
    
        
    
    










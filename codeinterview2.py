# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:42:01 2016

@author: nhern121
"""

from sklearn import datasets
iris=datasets.load_iris()
digits = datasets.load_digits()

from sklearn import svm
clf=svm.SVC(gamma=0.001,C=100)

clf.fit(digits.data[:-1], digits.target[:-1])

clf.predict(digits.data[-1:])

###############################################################################

def extendList(val, list=[]):
    list.append(val)
    return list



list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

###############################################################################
def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
###############################################################################
     
def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.

    >>> lst = [4, 5, 1, 6, 3]
    >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.

    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])
###############################################################################
    
    
    ''.join([`x` for x in xrange(101)])
    
###############################################################################
y=0
for x in range(len(a)):
    if a[x]:
        a[x], a[y] = a[y], a[x]
        y+=1
###############################################################################
#selection sort:
def selectionsort(l):
    for i in range(len(l)):
        minindex=i
        for k in range(i+1,len(l)):
            if l[k]<l[minindex]:
                minindex=k
        swap(l,minindex,i)
    return l
                
def swap(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp
###############################################################################



        

    
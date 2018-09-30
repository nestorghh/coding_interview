# 35. Search Insert Position

#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

###################################################################################

def searchInsert(x,target):
	for i in range(0,len(x)):
		if x[i]==target:
			return i
		elif x[i] > target:
			return i
	if x[-1]<target:
		return len(x)
			
x=[1,3,5,6]
target=5
print(searchInsert(x,target))

x=[1,3,5,6]
target=2
print(searchInsert(x,target))

x=[1,3,5,6]
target=7
print(searchInsert(x,target))

x=[1,3,5,6]
target=0
print(searchInsert(x,target))

x=[-5,1,2]
target=0
print(searchInsert(x,target))

#####################################################################################
#Solution with binary search

def searchInsert_efficient(x,target):
	left, right = 0, len(x)-1
	while left<=right:
		center=(left+right)//2
		if x[center]>=target:
			right=center - 1
		else:
			left= center +1
	return left


print('With BYnary search:')
x=[1,3,5,6]
target=5
print(searchInsert(x,target))

x=[1,3,5,6]
target=2
print(searchInsert(x,target))

x=[1,3,5,6]
target=7
print(searchInsert(x,target))

x=[1,3,5,6]
target=0
print(searchInsert(x,target))

x=[-5,1,2]
target=0
print(searchInsert(x,target))




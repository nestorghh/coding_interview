#Array Index & Element Equality
#Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch 
#that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. 
#Analyze the time and space complexities of your solution and explain its correctness.

def index_equals_value_search(arr):
  left, right = 0,len(arr)-1
  
  while left<=right:
    mid = (left+right)//2
    
    if arr[mid]>mid:
      right=mid-1
      
    elif (arr[mid]==mid) and (mid==0 or arr[mid-1]<mid-1):
      return mid
    else: #arr[mid]<mid:
      left=mid+1
    
  return -1
  

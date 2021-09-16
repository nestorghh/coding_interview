#You are given an array arr of N integers. For each index i, you are required 
#to determine the number of contiguous subarrays that fulfill the following conditions:
#The value at index i must be the maximum element in the contiguous subarrays, and
#These contiguous subarrays must either start from or end on index i.

def count_subarrays(arr):
  
  n = len(arr)
  result = [1]*n
  
  for i, x in enumerate(arr):
    
    for di in [-1,1]:
      
      step = 1
      while 0 <= i+di*step < n and arr[i+di*step]<x:
        step+=1
        result[i]+=1
        
  return result

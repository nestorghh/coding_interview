#K-Messed Array Sort
#Given an array of integers arr where each element is at most k 
#places away from its sorted position, code an efficient function 
#sortKMessedArray that sorts arr. For instance, for an input array 
#of size 10 and k = 2, an element belonging to index 6 in the sorted 
#array will be located at either index 4, 5, 6, 7 or 8 in the input array.

#Analyze the time and space complexities of your solution.

import heapq

def sort_k_messed_array(arr, k):
  
  heap = [arr[i] for i in range(0,k+1)] # k elements
  heapq.heapify(heap) 
  
  res=[]

  for i in range(k+1,len(arr)): # O(N-k)
    res.append(heapq.heappop(heap)) # O(1)
    heapq.heappush(heap,arr[i]) # O(logK)
  
  while heap: # O(k)
    res.append(heapq.heappop(heap)) # O(1)

  return res

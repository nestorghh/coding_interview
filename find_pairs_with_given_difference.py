#Given an array arr of distinct integers and a nonnegative integer k, 
#write a function findPairsWithGivenDifference that returns an array of all 
#pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

#Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

def find_pairs_with_given_difference(arr, k):
  d=set() #0, -1 2 , 1
  res=[]
  
  for x in arr:
      d.add(x)
    
  for i in range(len(arr)):
    if (arr[i] + k) in d:
      res.append([arr[i] + k,arr[i]])
      
  return res 
  
  #pass # your code goes here
arr = [0, -1, -2, 2, 1]
k = 1  
print(find_pairs_with_given_difference(arr, k))

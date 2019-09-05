#given an array, find the second maximum. If the maximum is repeated,
function should return the same element as second maximum. 

#Example 1. This should return 60
a=[7,2,60,76,1,1,3]

#Example 2. This should return 76
a=[7,2,60,76,1,1,3,76]

def get_second_max(a):
  maxi=a[0]
  maxi2=a[0]

  for i in range(1,len(a)):
    if a[i]>=maxi:
      maxi2=maxi
      maxi=a[i]

  return maxi2

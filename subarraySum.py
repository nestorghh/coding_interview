#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

def subarraySum(nums,k):
	import collections
	d=collections.defaultdict(int)
	d[0]=1
	cumsum, count = 0, 0

	for i in range(len(nums)):
		cumsum+=nums[i]
		if (cumsum - k)  in d:
			count+=1
		d[cumsum]+=1
	return count
		
print(subarraySum([5,2,1,4],7))



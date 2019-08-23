#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

def sumSubArray(nums,k):
	count=0
	for i in range(len(nums)):
		sum=0
		for j in range(i,len(nums)):
			sum+=nums[j]
			if sum==k:
				count+=1
	return count

print(sumSubArray([1,1,1],2))
			







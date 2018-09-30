# 53. Maximum Subarray

#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
	max_total = 0
	max_local = 0
	
	# if only one element then return that element.
	if len(nums) == 1:
		return nums[0]

	# if all the elements are negative, the solution is the max.
	if all(i<0 for i in nums):
		return max(nums)

	
	for i in range(0,len(nums)):
		#print(i)
		max_local = max_local + nums[i]
		#print(max_local)

		if max_local <0:
			max_local = 0
			#print('max_local negative')
		
		if max_local > max_total:
			max_total = max_local
			#print('max total updated')
			
	return max_total
			
		






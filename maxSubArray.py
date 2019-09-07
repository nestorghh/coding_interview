# 53. Maximum Subarray

###################################################################################################
#Given an integer array nums, find the contiguous subarray 
#(containing at least one number) which has the largest sum and return its sum.

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
			
###################################################################################################		
# Kadane's Algorithm
# Beautiful solution. The idea is that if we know the maximum subarray sum ending at position i
# then the max subarray sum ending at position i+1 is either (a) max subarray sum until i 
#plus element at position i+1 or (b) only the element at position i+1, whichever is the max.

def kadane(nums):
	max_local = nums[0]
	max_total = nums[0]

	for i in range(1,len(nums)):
		max_local = max(nums[i],  max_local + nums[i])
		max_total = max(max_local, max_total)

	return max_total
		
##################################################################################################

#his solution is linear but uses O(n) space
def maxSumSub(nums):
	B=[0]*len(nums)
	for i in range(len(nums)):
		B[i] = max(nums[i],B[i-1]+nums[i])

	return max(B)
		

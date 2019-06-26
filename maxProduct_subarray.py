def maxProduct(nums):
	maxi = [0]*len(nums)
	mini = [0]*len(nums)

	maxi[0]=mini[0]=nums[0]

	for i in range(1,len(nums)):
		if nums[i]>0:
			maxi[i] = max(nums[i], nums[i]*maxi[i-1])
			mini[i] = min(nums[i], nums[i]*mini[i-1])
		else:
			maxi[i] = max(nums[i], nums[i]*mini[i-1])
			mini[i] = min(nums[i], nums[i]*maxi[i-1])
	return max(maxi)


print(maxProduct([2,3,1,4,-6,7,9]))
print(maxProduct([6,-3,-10,0,2]))
print(maxProduct([3,1,-6,-3,2,1,6]))
	





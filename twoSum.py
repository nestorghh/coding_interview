def twoSum(nums,target):
	d={}
	for i in range(0,len(nums)):
		print(target -nums[i])
		if target - nums[i] not in d:
			d[nums[i]]=i
		else:
			return d[target-nums[i]], i


print(twoSum([2,4,5,11,9],6))

#Runtime: 24 ms, faster than 99.83% of Python online submissions for Two Sum.
#Memory Usage: 13.1 MB, less than 34.80% of Python online submissions for Two Sum.

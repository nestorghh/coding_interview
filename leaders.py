def get_leaders(nums):
	
	n, maxfr = len(nums) -1 ,nums[-1]
	leaders = [nums[-1]]

	for i in range(n,-1,-1):
		if nums[i] > maxfr:
			leaders.append(nums[i])
			maxfr = nums[i]
	return leaders
	

def permute(nums):
	if len(nums)==0:
		return []

	if len(nums)==1:
		return [nums]

	l=[]

	for i in range(len(nums)):
		m = nums[i]
		rl = nums[:i] + nums[i+1:] 	

		for p in permute(rl):
			l.append([m]+p)
	return l
			

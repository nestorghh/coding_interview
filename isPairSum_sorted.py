def isPairSum(nums,target):
	
	i, j = 0, len(nums)-1
	
	while i< j:
		if nums[i]+nums[j]==target:
			return [i,j]
		elif nums[i]+nums[j]<target:
			i+=1
		else:
			j-=1
	return [-1,-1]
	
	
print(isPairSum([10,20,35,50,75,80],70))


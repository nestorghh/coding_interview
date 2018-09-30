#3SUM problem
def threesum(nums):
	result=[]
	nums.sort()
	r=len(nums)-1
	for i in range(len(nums)-2):
		l=i+1
		while (l<r):
			sum_=nums[i]+nums[l]+nums[r]
			if (sum_ < 0):
				l=l+1
			if (sum_ > 0):
				r=r-1
			if not sum_:
				result.append([nums[i],nums[l],nums[r]])
				l=l+1
	return result

print(threesum([-25,-10,-7,-3,2,4,8,10]))
print(threesum([10,9,-1,-10,20,-10]))



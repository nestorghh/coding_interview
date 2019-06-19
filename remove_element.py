def removeElement(nums,val):
	count=0
	for i in range(len(nums)):
		if nums[i]!=val:
			nums[count]=nums[i]
			count+=1
		print(nums)
	return count, nums

print(removeElement([3,2,2,3],3))
print('-----------------')
print(removeElement([0,1,2,3,3,0,4,2],2))
print('-----------------')
print(removeElement([0,0,0,0],0))


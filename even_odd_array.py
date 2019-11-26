# Your input is an array of integers, and ou have to reorder its entries 
# so that the even entries appear first.
###########################################################################
def even_odd(nums):
	even, odd = 0 , len(nums)-1
	
	while even<odd:
		if nums[even]%2==0:
			even+=1
		else:
			nums[even], nums[odd] = nums[odd], nums[even]
			odd-=1
	return nums 

print(even_odd([3,7,8,5,4,2]))



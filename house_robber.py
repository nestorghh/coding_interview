
# rethink this. this is incorrect.
def house_robber(nums):
	sum2=0
	for i in range(0,len(nums),2):
		sum2+= nums[i]
		
	return max(sum2, sum(nums)-sum2)

print(house_robber([1,2,3,1]))
print(house_robber([2,7,9,3,1]))
1000 --->9.9
211000--->x

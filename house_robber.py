
# rethink this. this is incorrect.
def house_robber(nums):
	temp=[0]*(len(nums)+1)
	temp[1]=nums[0]
	for i in range(2,len(temp)):
		temp[i] = max(temp[i-1],temp[i-2]+nums[i-1])
	return temp[-1]

print(house_robber([1,2,3,1]))
print(house_robber([2,7,9,3,1]))
print(house_robber([2,1,1,2]))


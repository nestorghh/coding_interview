#single number problem leetcode
#this is my solution. It is correct but not 
#efficient enough for leetcode to let it pass.
def singleNumber(nums):
	for i in range(0,len(nums)):
		if (nums[i]) not  in nums[:i]+nums[i+1:]:
			t=nums[i]
			break
	return t

a=singleNumber([6,7,6,5,7])
b=singleNumber([6,7,7])

print a,b

# let's try another way

#this is the eficient solution I was looking for. Fuck!!
# it's so beautiful. 
def singleNumbereff(nums):
	return 2*sum(set(nums))-sum(nums)




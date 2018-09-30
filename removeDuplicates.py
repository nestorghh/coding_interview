# removeDuplcates problem leetcode.
# Time : O(n)
# Space : O(1)

def removeDuplicates(nums):
	current, nextc = 0,1
	while nextc < len(nums):
		if nums[current]!=nums[nextc]:
			current = current + 1
			nums[current] = nums[nextc]
		nextc = nextc + 1
	return (current + 1), nums

a=removeDuplicates([1,1,2])
b=removeDuplicates([1,1,1,2,2,3,4,5])


print a, b




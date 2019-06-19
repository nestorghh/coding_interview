#Leetcode 215 (Kth ELement in an Array)
#Find the kth largest element in an unsorted array. 
#Note that it is the kth largest element in the sorted order, 
#not the kth distinct element.

def kthlargest(nums,k):
	nums.sort()
	return nums[len(nums)-k]



print(kthlargest([3,2,1,5,6,4],2))
print(kthlargest([3,2,3,1,2,4,5,5,6],4))



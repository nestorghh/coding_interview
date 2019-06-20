def insertionSort(nums):
	for i in range(1,len(nums)):
		valueToInsert = nums[i]
		holePosition = i

		#do comparisons untill finding right position
		while holePosition > 0 and nums[holePosition-1] > valueToInsert:
			nums[holePosition] = nums[holePosition -1]
			holePosition = holePosition -1

		nums[holePosition] = valueToInsert #insert element in the position found above.

	return nums

print(insertionSort([14,33,27,10,35,19,42,44]))
print(insertionSort([14,33,270,101,35,19,42,44]))


#Find median in a streaming of data, i.e, you get one element at a time. Use insertion sort in O(n^2) 
# worst case.
# http://mathworld.wolfram.com/StatisticalMedian.html
def medianFinder(nums,newel):
	#nums is the set of numbers already sorted
	#newel is the new element arriving from the stream
	nums = nums+[newel]
	nums = insertionSort(nums)
	n=len(nums)	

	if n%2==1:
		median = nums[((n+1)//2)-1] # if length is odd, get middle element
	else:
		median = (nums[(n//2)-1] + nums[n//2])/2 #o.w, get average of two middle.

	return nums, median

print(medianFinder([1,2,30,40],3))
print(medianFinder([1,2,30,40,20],9))
print(medianFinder([1,2,30,40,1,1,2,4,32],31))
print(medianFinder([1,2,30,40,2,1,67,12],5))



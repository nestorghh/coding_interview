def twoSumSorted(numbers,target):
	l, r = 0, len(numbers)-1
	
	while(l<r):
		if numbers[l] + numbers[r] == target:
			return l+1, r+1
		elif numbers[l] + numbers[r] < target:
			l+=1
		else:
			r-=1

print(twoSumSorted([1,2,5,9,12],14))

#Runtime: 40 ms, faster than 77.37% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 13.7 MB, less than 20.76% of Python3 online submissions for Two Sum II - Input array issorted.

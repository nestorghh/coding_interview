def hIndex(citations):
	if len(citations)==0:
		return 0
	for i in range(1,len(citations)+1):
		entries=0
		for j in range(citations):
			if citations[j]>i:
				entries+=1
		if entries<i:
			return i-1
	return i 

#Runtime: 296 ms, faster than 5.43% of Python online submissions for H-Index.
#Memory Usage: 12 MB, less than 20.00% of Python online submissions for H-Index.

print(hIndex([3,0,6,1,5])) 

#######################################################################################



def hIndexOpt(citations):
	citations.sort()
	n=len(citations)
	for i,c in enumerate(citations):
		if c >= n-i:
			return n-i
	return 0

print(hIndexOpt([3,0,6,1,5]))


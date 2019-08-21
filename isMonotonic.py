def isMonotonic(A):
	count, count2, k = 0, 0, len(A)-1
	for i in range(len(A)-1):
		if (A[i]-A[i+1])<=0:
			count+=1
		if (A[i]-A[i+1])>=0:
			count2+=1
	return count==k or count2==k
	

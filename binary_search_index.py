#Search a sorted array for a value that is equal to its index

def binary_search_index(A):

	l, u = 0, len(A)-1

	while l<=u:
		m=(l+u)//2
		
		if A[m]==m:
			return m
		elif A[m]>m:
			u=m-1
		else:
			l=m+1
	return -1



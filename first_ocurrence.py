# Search a sorted array for first ocurrence of k.

def binary_search_first(A,k):
	l, u= 0,len(A)-1

	while l<=u:
		m=(l+u)//2
		
		if A[m]<k:
			l=m+1
		elif A[m]>k:
			u=m-1
		else:
			for i in range(m+1):
				if A[i]==k:
					return i
	return -1

print(binary_search_first([-14,-10,2,108,108,243,285,285,285,401],2))

##############################################################################

def binary_search_first_opti(A,k):
	l,u = 0, len(A)-1
	
	while l<=u:
		m=(l+u)//2
		
		if A[m]<k:
			l=m+1
		elif A[m]>k:
			u=m-1
		else:
			if (m-1>0) and (A[m-1]==k):
				u=m-1
			else:
				return m
	return -1


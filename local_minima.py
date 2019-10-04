def get_local_minima(A):
	l, u = 0, len(A)-1

	while l<=u:
		m=(l+u)//2
		#print("l is" + str(l))
		#print("u is" + str(u))
		#print("m is" + str(m))	
		#print("==============")
		if A[m-1]>A[m]<A[m+1]:
			#print('a')
			return A[m]
		elif A[m-1]<A[m]:
			#print('b')
			u=m-1
			if l==u:
				return A[m-1]
		elif A[m+1]<A[m]:
			#print('c')
			l=m+1
			if l==u:
				return A[m+1]
	return -1




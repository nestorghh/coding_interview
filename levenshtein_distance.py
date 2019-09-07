def levenshtein_distance(A,B):
	
	m, n = len(A), len(B)

	T=[[None]* (n+1) for _ in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):

			if i==0 and j==0:
				T[i][j]=0

			elif i==0:
				T[i][j] = 1 + T[i][j-1]
		
			elif j==0:
				T[i][j] = 1 + T[i-1][j]
		
			else:
				if A[i-1]==B[j-1]: # has to do with null row and column
					T[i][j] = T[i-1][j-1]

				else:
					T[i][j] = 1 + min(T[i-1][j-1],T[i-1][j],T[i][j-1])
	return T



def binomial(n,k):

	C=[[0]*(n+1) for _ in range(k+1)]

	for i in range(k+1):
		for j in range(n+1):
			#print(i,j)	
		#	if i==0 and j==0:
		#		C[i][j]=1
			if i==0:
				C[i][j]=1
			elif j==0:
				C[i][j]=0

			elif i==0 and j==0:
				C[i][j]=1
			
			else:
				C[i][j]=C[i][j-1]+C[i-1][j-1]
	print(C)
	return C[k][n]


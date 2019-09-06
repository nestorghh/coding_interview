def transpose(A):
	m = len(A)
	n = len(A[0])
	At=[]

	for j in range(n):
		r=[]
		for i in range(m):
			r.append(A[i][j])
		At.append(r)
	return At


A=[[2,3],[5,4],[1,2]]



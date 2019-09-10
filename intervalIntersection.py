def intervalIntersection(A,B):
	m, n = len(A), len(B)
	i, j = 0, 0
	inter=[]
	
	while  i<m and j<n:
		s=max(A[i][0],B[j][0])
		e=min(A[i][1],B[j][1])

		if s<=e:
			inter.append([s,e])

		if A[i][1]<B[j][1]:
			i+=1
		else:
			j+=1
	return inter


A=[[0,2],[5,10],[13,23],[24,25]]
B=[[1,5],[8,12],[15,24],[25,26]]






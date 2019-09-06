def searchMatrix(matrix,target):
	
	if not matrix:
		return False

	m, n = len(matrix), len(matrix[0])

	i, j = 0, n-1 # start with bottom left corner 

	while 0<=i<m and 0<=j<n:
		if matrix[i][j] > target:
			j-=1
		elif matrix[i][j] < target:
			i+=1
		else:
			return True
	return False
	
	

matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]



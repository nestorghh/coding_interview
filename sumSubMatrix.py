
#Leetcode 304
#Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


def sumSubMatrix(matrix,r1,c1,r2,c2):

	m=len(matrix)
	n=len(matrix[0])

	dp=[[0]*(n+1) for _ in range(m+1)]

	for i in range(1,m+1):
		for j in range(1,n+1):
			dp[i][j] = dp[i-1][j] + dp[i][j-1] +matrix[i-1][j-1] - dp[i-1][j-1]

	r1+=1
	c1+=1
	r2+=1
	c2+=1

	return dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1]+dp[r1-1][c1-1]
	

A=[[2,0,-3,4],[6,3,2,-1],[5,4,7,3],[2,-6,8,1]]	

A=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]



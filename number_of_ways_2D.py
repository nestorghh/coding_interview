# Write a program that counts how many ways you can go
# from the top-left to the bottom right in a 2D array,
# assuming all moves must either go right or down.

def number_of_ways(m,n):
	DP=[[None]*n for _ in range(m)]

	for i in range(m):
		for j in range(n):
			if i==0 or j==0:
				DP[i][j]=1
			else:
				DP[i][j] = DP[i-1][j] + DP[i][j-1]
	return DP[m-1][n-1]







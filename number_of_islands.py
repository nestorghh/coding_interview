def numIslands(grid):
	
	def dfs(grid,i,j):
		m = len(grid)
		n=len(grid[0])

		grid[i][j]=0

		# bottom neighbor
		if i<m-1 and grid[i+1][j]==1:
			dfs(grid,i+1,j)
		
		# up neighbor
		if i>0 and grid[i-1][j]==1:
			dfs(grid,i-1,j)

		# right neighbor
		if j<n-1 and grid[i][j+1]==1:
			dfs(grid,i,j+1)

		# left neighbor
		if j>0 and grid[i][j-1]==1:
			dfs(grid,i,j-1)

		
	# implement main functionality

	m=len(grid)
	n=len(grid[0])

	count=0
	for i in range(m):
		for j in range(n):
			if grid[i][j]==1:
				count+=1
				dfs(grid,i,j)
	return count			



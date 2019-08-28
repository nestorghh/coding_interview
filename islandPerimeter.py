def islandPerimeter(grid):
	peri = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==1:
				peri+= countPerimeter(grid,i,j)
	return peri
			

def countPerimeter(grid,i,j):
	count =0;
	#left case
	if (j-1)<0 or grid[i][j-1]==0:
		count+=1
	#right case
	if ((j+1)>len(grid[0])-1) or grid[i][j+1]==0:
		count+=1

	# upper case
	if (i-1)<0 or grid[i-1][j]==0:
		count+=1

	# lower case
	if ((i+1)>len(grid)-1) or grid[i+1][j]==0:
		count+=1

	return count
	
	



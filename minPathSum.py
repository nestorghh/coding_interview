def minPathSum(grid):
    n=len(grid[0])
    m=len(grid)
    dp = [[0]*n]*m
    
    print(grid)
    print('whatever')
    for i in range(m):
        for j in range(n):
            #dp[i][j]+=grid[i][j]

            if i==0 and j==0:
                grid[i][j]=grid[i][j]

            elif i==0:
                grid[i][j] = grid[i][j] + grid[i][j-1]

            elif j==0:
                grid[i][j] = grid[i][j]  + grid[i-1][j]
                
            else: 
                grid[i][j]= grid[i][j] + min(grid[i-1][j], grid[i][j-1])


    print(dp)
    return grid[m-1][n-1]

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(minPathSum(grid))


#def minPathSum(grid):





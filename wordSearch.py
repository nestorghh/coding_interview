def wordSearch(grid,word):

    def dfs(grid,i,j,current,word):
        m = len(grid)
        n = len(grid[0])

        if current==len(word):
            return True

        if i<0 or j<0 or j>=n or i>=m or grid[i][j]!=word[current]:
            return False

        temp = grid[i][j]
        grid[i][j]=""

        # bottom neighbor
        b = dfs(grid,i+1,j,current+1,word)

        
        # up neighbor

        u = dfs(grid,i-1,j,current+1,word)

        # right neighbor

        r = dfs(grid,i,j+1,current+1,word)

        # left neighbor

        l = dfs(grid,i,j-1,current+1,word)

        grid[i][j]=temp

        return b or u or r or l

        
    # implement main functionality
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]==word[0] and dfs(grid,i,j,0,word):
                return True
                    
    return False





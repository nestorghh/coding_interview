def orangeRotting(grid):
    queue = []

    fresh = 0
    m= len(grid)
    n = len(grid[0])

    # identify rotten an fresh oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i,j,0))
            elif grid[i][j] == 1:
                fresh+=1

    #bfs?
    res=0
    while len(queue)>0:
        x,y,t = queue.pop()

        neighbors = [(1,0), (-1,0), (0,1), (0,-1) ] # right, left, down, up

        for (i,j) in neighbors:
            if 0<=(x+i)<m and 0<=(y+j)<n and grid[x+i][y+j]==1:
                queue.append((x+i,y+j,t+1))
                grid[x+i][y+j]=2
                res = max(res,t+1)
                fresh-=1
    if fresh>0:
        return -1

    return res
                

grid=[[2,1,1],[1,1,0],[0,1,1]]
print(orangeRotting(grid))

grid=[[2,1,1],[0,1,1],[1,0,1]]
print(orangeRotting(grid))

grid=[[0,2]]
print(orangeRotting(grid))



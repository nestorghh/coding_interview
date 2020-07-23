# This functin determines if it is safe to move to position (x,y) from current position.
# It is NOT possible to move to (x,y) if either was visited or it is not a 1.
def isSafe(mat,visited,x,y):

    if mat[x][y]==0 or visited[x][y]:
        return False
    else:
        return True
    

def isValid(x,y):
    return (M > x >= 0) and (N > y >= 0)

def findShortestPath(mat, visited,i,j,x,y,min_dist,dist):

    # if destination is found, update min_dist
    if i==x and j==y:
        return min(dist,min_dist)

    # set (i,j) cell as visited
    visited[i][j]=1

    # bottom
    if isValid(i+1,j) and isSafe(mat,visited,i+1,j):
        min_dist = findShortestPath(mat,visited,i+1,j,x,y,min_dist,dist+1)

    # right
    if isValid(i,j+1) and isSafe(mat,visited,i,j+1):
        min_dist = findShortestPath(mat,visited,i,j+1,x,y,min_dist,dist+1)

    # up
    if isValid(i-1,j) and isSafe(mat,visited,i-1,j):
        min_dist = findShortestPath(mat,visited,i-1,j,x,y,min_dist,dist+1)

    # left 
    if isValid(i,j-1) and isSafe(mat,visited,i,j-1):
        min_dist = findShortestPath(mat,visited,i,j-1,x,y,min_dist,dist+1)

    # backtrack (remove (i,j) from visited matrix)
    visited[i][j]=0

    return min_dist

mat = [
                [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
                                        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                                                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                                                        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                                                                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                                                                        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                                                                                [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                                                                                        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
                                                                                            ]
 


M = N = 10

visited = [[0 for x in range(N)] for y in range(M)]

min_dist = findShortestPath(mat, visited, 0, 0, 7, 5, float('inf'), 0)


if min_dist!= float('inf'):
    print("The shortest path is", min_dist)

else:
    print("No reachable")




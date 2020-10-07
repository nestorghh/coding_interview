def maximalRectangle(matrix):

    if not matrix: return 0


    m = len(matrix)
    n = len(matrix[0])

    left = [0]*n
    right = [0]*n
    height = [0]*n

    maxarea = 0

    for i in range(m):

        print('row ', i)
        input()
        cur_left, cur_right = 0, n 

        for j in range(n):
            print('height ', j)
            if matrix[i][j]=='1': height[j] += 1
            else: height[j]=0
            print('height array ', height)
            input()

        for j in range(n):
            print('left ', j)
            if matrix[i][j] == '1': left[j] = max(left[j],cur_left)
            else:
                left[j]=0
                cur_left = j+1
            print('left array ', left)
            input()

        for j in range(n-1,-1,-1):
            print('right')
            if matrix[i][j]=='1': right[j]=min(right[j], cur_right)
            else:
                right[j]=n
                cur_right = j
            print('right array ', right)
            input()

        for j in range(n):
            print("area ", j )
            maxarea = max(maxarea, height[j] * (right[j] - left[j]))
            print("max area", maxarea)
            input()

    return maxarea


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]







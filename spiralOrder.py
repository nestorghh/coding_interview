# 54. Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all 
# elements of the matrix in spiral order.


M=[[2,4,6,8],[5,9,12,16],[2,11,5,9],[3,2,1,8]]

def spiralOrder(matrix):
	m = len(matrix)
	n = len(matrix[0])

	t , b , l, r = 0, m-1, 0, n-1
	dir = 0
	arr=[]
	while (t <= b and l <= r):
		if dir==0: #move right
			for i in range(l,r+1,1):
				print(matrix[t][i])
				arr.append(matrix[t][i])
			t += 1
			dir = 1
		elif dir == 1: # move down
			for i in range(t,b+1,1):
				print(matrix[i][r])
				arr.append(matrix[t][i])
			r-=1
			dir = 2
		elif dir == 2: # move left
			for i in range(r,l-1,-1):
				print(matrix[b][i])
				arr.append(matrix[t][i])
			b -= 1
			dir = 3
		elif dir ==3 : # move up
			for i in range(r,t-1,-1):
				print(matrix[i][l])
				arr.append(matrix[t][i])
			l += 1
			dir = 0
	return arr
		

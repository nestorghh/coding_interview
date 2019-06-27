#766. Toeplitz Matrix

def isToeplitz(M):
	for i in range(len(M)-1):
		for j in range(len(M[1])-1):
			if M[i][j]!=M[i+1][j+1]:
				return False
	return True
				
print(isToeplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))		
print(isToeplitz([[1,1,3,4],[5,1,2,3],[9,5,1,2]]))		
print(isToeplitz([[1,2,3],[2,1,2],[3,2,1]]))		
print(isToeplitz([[1,5,6],[2,1,5],[3,2,1],[4,3,2]]))
print(isToeplitz([[1,2],[2,2]]))		

#Runtime: 32 ms, faster than 99.67% of Python3 online submissions for Toeplitz Matrix.
#Memory Usage: 13.1 MB, less than 79.93% of Python3 online submissions for Toeplitz Matrix.

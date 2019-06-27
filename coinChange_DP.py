# Coin-change problem using traditional dynamic programming

def coinChange_dp(denom,A):
	n = len(denom)-1
	#C=[[None]*(A+1)]*len(denom) never create a matrix in this way

	# create an empty matrix (m*n) where m is the number of coin denominations
	# and n is the value you're looking to change. optimal solution is element
	# C[0][A]
	C = [[None] * (A+1) for i in range(len(denom))]
	# (A+1) is the number of columns
	# len(denom) is the number of rows

	for j in range(0,A+1):
		C[n][j] = j

	for i in range(n-1,-1,-1):
		for j in range(0,A+1):
			if (denom[i] > j) or (C[i+1][j] < 1 + C[i][j-denom[i]]):
				C[i][j] = C[i+1][j]
			else:
				C[i][j] = 1 + C[i][j-denom[i]]
	return C[0][A]


def print_matrix(C):
	for c in C:
		print(c)

print(coinChange_dp([10,6,1],12))
print(coinChange_dp([10,5,1],12))
print(coinChange_dp([10,5,2,1],54))
#print_matrix(coinChange_dp([10,6,1],12))		
		
	









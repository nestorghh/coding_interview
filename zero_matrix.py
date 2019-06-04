# set to zero the columns and rows of zero elements in a matrix

def zero_matrix(A):

	pos=[]
	for i in range(len(A)):
		for j in range(len(A[1])):
			if A[i][j]==0:
				#a,b=i,j
				pos.append((i,j))
	
	for i in range(len(A)):
		for j in range(len(A[1])):
			for t in pos:
				if i==t[0]:
					A[i]=[0]*len(A[1])
			#if i==a:
			#	A[i]=[0]*len(A[1])
			#if j==b:
			#	A[i][j]=0	
				if j==t[1]:
					A[i][j]=0
	return A						


def print_matrix(A):
	for i in A:
		print(i)

A=[[1,4,3,2],[1,0,2,3],[1,0,1,2],[0,1,2,3]]


print('Before')
print_matrix(A)
print("After")
print_matrix(zero_matrix(A))





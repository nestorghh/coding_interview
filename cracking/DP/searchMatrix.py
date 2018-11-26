#Write an efficient algorithm that searches for a value in an m x n matrix. 
#This matrix has the following properties:

#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.

matrix = [
[1,3,5,7],
[10,11,16,20],
[23,30,34,50],
[54,67,89,90]
]

print(matrix)

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]

def searchMatrix(matrix,target):
	
	if len(matrix)==0 or len(matrix[0])==0 or matrix[0][0]> target:
		return False

	if len(matrix)==1 and len(matrix[0])==1 and matrix[0][0]==target:
		return True
	
	start = 0
	end = len(matrix) - 1

	while start < end:
		midpoint = (start + end +1)//2
		
		if matrix[midpoint][0] == target:
			return True
		if matrix[midpoint][0] > target:
			end = midpoint -1
		else:
			start = midpoint

	row = start
	print('row',row)


	low = 0
	upp = len(matrix[row])-1


	start = 0
	end = len(matrix[row]) + 1
	
	while start <= end:
		midpoint = (end-start)//2 + start
		if matrix[row][midpoint] == target:
			return True
		if matrix[row][midpoint] < target:
			start = midpoint + 1
		else:
			end = midpoint -1
	return False



#the naive way to solve the problem.
# O(n²)
# problem url: https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
#####################################################################################
def max_difference(x):
	x_len = len(x)
	max_d = x[1]-x[0]
	
	for i in range(0, x_len):
		for j in range(i+1,x_len):
			if (x[j] - x[i]>max_d ):
				max_d = x[j] - x[i]
	return max_d
	
x=[1,2,9,10,110]
x=[6,2,3,4]
print (max_difference(x))

#####################################################################################
#O(n) solution to the problem.
#O(1) space
def max_diff_efficient(x):
	x_len = len(x)
	max_d = x[1] - x[0]
	min_ele = x[0]

	for i in range(1,x_len):
		if (x[i]- min_ele > max_d):
			max_d = x[i] - min_ele
		
		if (x[i]<min_ele):
			min_ele = x[i]
	return max_d

x=[1,2,9,10,110]
x=[6,2,3,4]
print (max_diff_efficient(x))





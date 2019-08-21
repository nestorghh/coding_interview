#Given a target value and a list, if the target is found in the list, return the target. If not found, return the integer in the list that is closest to the target but smaller than the target.

def search_ele(A,t):
	d=float('Inf')
	result=-1
	for i in range(len(A)):
		if (abs(A[i]-t))<d and (A[i]<=t):
			d=abs(A[i]-t)
			ele=i
			result=A[ele]
	return result
	
	




# We are given an array arr[] of size n. Numbers are from 1 to (n) in random order. 
#The array has only one repetitive element. We need to find the missing element.

def missing_ele(arr):
	
	# we first look for the repeated element

	v = []
	for a in arr:
		if a in v:
			R=a
			break
		v.append(a)

	n = len(arr)
	T = (n*(n+1))//2
	E = sum(arr)

	return T-E+R # we use that E = T - F + R




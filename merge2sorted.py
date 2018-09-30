# Time Complexity: O(n1+n2)
# Space Complexity: O(n1+n2)


def merge2sorted(a1,a2):
	n1 = len(a1)
	n2 = len(a2)
	a3 = [None]*(n1+n2)
	
	i, j, k= 0, 0, 0
	
	#traverse both arrays
	while i<n1 and j<n2:
		if a1[i] < a2[j]:
			a3[k] = a1[i]
			k += 1
			i += 1
		else:
			a3[k] = a2[j]
			k += 1
			j += 1
	# strore remaining elements of first array
	while i < n1:
		a3[k] = a1[i]
		k  += 1
		i  += 1

	# store remaining elements of second array
	while j < n2:
		a3[k] = a2[j]
		k += 1
		j += 1

	return a3


a1=[1,2,3,4,5]
a2=[2,4,5,5,9]

#a1 = [1,3,4,5]
#a2 = [2,4,6,8]

print(merge2sorted(a1,a2))


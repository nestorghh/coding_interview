# Longest increasing subsequence problem. O(n ^ 2) solution.

def lis(arr):
	l={}
	l = dict((el,[]) for el in range(len(arr)))
	l[0] = [arr[0]]
	print(l)
	for i in range(1,len(arr)):
		print(i)
		for j in range(0,i):
			print(j)
			if ((arr[j] < arr[i]) and (len(l[i]) < len(l[j])+1)):
				l[i] = l[j]
				print(l[i])
		l[i] = l[i] + [arr[i]]

	return l

# use dictionary instead of list for l. follow video. almost there.


def uniqueOcurrences(arr):

	from collections import Counter

	count = Counter(arr)
	u=[]

	for c in count:
		if count[c] in u:
			return False
		u.append(count[c])

	return True
		

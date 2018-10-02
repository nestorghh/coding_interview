# 41. First Missing Positive
# Given an unsorted integer array, find the smallest missing positive integer.
#############################################################################
def fmp(arr):
	b = {}
	for i in arr:
		if i > 0:
			try:
				b[i] += 1
			except:
				b[i] = 1

	for i in range(1,len(b)+1):
		try:
			b[i] += 1 # try to access this element
		except:
			return i # if not, this is the first missing.
	return len(b)+1

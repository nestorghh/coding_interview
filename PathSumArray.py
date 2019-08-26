
def PathSumArray (r, Sum):
	if A[r] is None or Sum - A[r] < 0:
		return False
	if A[r] - Sum == 0 and hasChildren(r) == False:
		print(A[r])
		return True
	if 2*r + 1 < len(A) and PathSumArray(2*r + 1, Sum - A[r]):
		print(A[r])
		return True
	if 2*r + 2 < len(A) and PathSumArray(2*r + 2, Sum - A[r]):
		print(A[r])
		return True
	return False

def hasChildren(i):
	lc = 2*i+1
	rc = 2*i+2
	if (lc >= len(A) or A[lc] is None) and (rc >= len(A) or A[rc] is None):
		return False
	return True


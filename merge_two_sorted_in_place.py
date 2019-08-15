def merge(A,B):

	m=sum([1 for a in A if a!=0])
	n=len(B)
	w_id=m+n-1
	a=m-1
	b=n-1

	while a>=0 and b>=0:
		if A[a]>B[b]:
			A[w_id]=A[a]
			a-=1
		else:
			A[w_id]=B[b]
			b-=1
		w_id-=1
	
	while b>=0:
		A[w_id] = B[b]
		w_id-=1
		b_=1

	return A
		

print(merge([1,2,3,0,0,0],[2,5,6]))
print(merge([3,13,17,0,0,0,0],[3,7,11,19]))

#Runtime: 24 ms, faster than 62.48% of Python online submissions for Merge Sorted Array.
#Memory Usage: 11.8 MB, less than 17.95% of Python online submissions for Merge Sorted Array.



def sortedSquares(A):
	i=0
	ns = []

	# get the negative part
	while i<len(A) and A[i]<0:
		ns.insert(0,A[i]**2)
		i+=1

	#the rest is the positive part
	ps=A[i::]
	ps = [a**2 for a in ps]
	
	i, j, n, m = 0, 0, len(ns), len(ps)

	result=[]
	while i<n and j<m:
		if ns[i]<ps[j]:
			result.append(ns[i])
			i+=1
		else:
			result.append(ps[j])
			j+=1
	
	while i<n:
		result.append(ns[i])
		i+=1

	while j<m:
		result.append(ps[j])
		j+=1
		
	return result			

	
def sortedSquares2(A):
	pos, neg = [], []
	for a in A:
		if a<0:
			pos.append(a**2)
		else:
			neg.insert(0,a**2)

	while 1:
		if len(pos)>0:
			a=pos.pop(0)
		if len(neg)>0:
			b=neg.pop(0)
 
	
		
	





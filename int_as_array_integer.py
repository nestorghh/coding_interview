def int_as_array_increment(A):
	ni=int("".join(map(str,A)))+1
	return [int(x) for x in str(ni)]

def int_as_array_increment(A):
	A[-1]+=1
	
	for i in reversed(range(1,len(A))):
		if A[i]!=10:
			break
		A[i]=0
		A[i-1]+=1

	if A[0]==10:
		A[0]=1
		A.append(0)

	return A
		



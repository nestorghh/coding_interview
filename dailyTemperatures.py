def dailyTemperatures(T):
	n=len(T)
	r=[]

	for i in range(n-1):
		c=0
		for j in range(i+1,n):
			if T[j]>T[i]:
				c=1
				break
			if T[j]<T[i]:
				c+=1

		if c==(n-i-1):
			c=0
		r.append(c)
	return r





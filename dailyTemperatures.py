def dailyTemperatures(T):
	n=len(T)
	ans=[0]*n
	stack=[]

	for i in range(n-1,-1,-1):
		while stack and T[i]>=T[stack[-1]]:
			stack.pop()
		if stack:
			ans[i] = stack[-1] - i

		stack.append(i)

	return 




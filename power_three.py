def power_three(n):
	r=0
	if n==0:
		return False
	if n==1:
		return True
	while (r==0):
		r=n%3
		n=n/3	
		if n==1:
			break
		print(n)
		print(r)
	if r!=0:
		return False
	return True


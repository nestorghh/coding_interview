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

#Runtime: 84 ms, faster than 91.85% of Python3 online submissions for Power of Three.

#Memory Usage: 13.3 MB, less than 31.74% of Python3 online submissions for Power of Three.

def power_three_log(n):
	import math
	x = math.log(n)/math.log(3)
	return x.is_integer()




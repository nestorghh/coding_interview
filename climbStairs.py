# 70. Climbing Stairs

#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Note: Given n will be a positive integer.


def climbStairs(n):

	# Fibonnaci in disguise?

	f={}
	f[1]=1
	f[2]=2

	for i in range(3,n+1)
		f[i] = f[i-1] + f[i-2]

	return f[n]





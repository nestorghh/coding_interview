#Sqrt leetcode problem
#Newton's method
def mySqrt(x):
	import numpy as np
	epsilon=0.000001
	z0=2
	stop=4
	while (stop>epsilon):
		z=z0-(((z0**2-x)*1.0)/(2*z0))
		print z
		stop=abs(z**2-x)
		z0=z
	return int(z)

a=mySqrt(16)
b=mySqrt(25)
c=mySqrt(9.06)
d=mySqrt(8)

print a, b, c, d


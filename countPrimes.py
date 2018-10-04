class Solution(object):
	def countPrimes(self,n):

		if n<=1:
			return 0

		primes = [True]*n
		primes[0] = False
		primes[1] = False
	
		for i in range(2,n+1):
			j = i**2
			while j < n:
				primes[j] = False
				j = j + i
		return [x for x in range(n) if primes[x]==True]







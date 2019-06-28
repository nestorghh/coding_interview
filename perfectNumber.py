def isPerfectNumber(n):
	suma=0
	i=1
	while i*i<=n:
		if n%i==0:
			suma+=i
			print(i)
			if i*i!=n:
				suma+=n//i
		i+=1
	print(suma-n)
	return suma-n==n
			
print(isPerfectNumber(28))	
print(isPerfectNumber(6))
print(isPerfectNumber(496))
print(isPerfectNumber(8128))


#Runtime: 48 ms, faster than 46.14% of Python3 online submissions for Perfect Number.
#Memory Usage: 13.2 MB, less than 58.66% of Python3 online submissions for Perfect Number.




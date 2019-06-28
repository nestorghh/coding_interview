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





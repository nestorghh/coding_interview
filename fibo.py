# recursive Fibonnaci
#def fib(n):
#	if n<=1:
#		return n
#	return fib(n-1) + fib(n-2)

#n=9
#print('The {}th Fibonnaci number is {}'.format(n,fib(n)))

#Dynamic programming solution

def fibdp(n):
	fib={}
	fib[0]=0
	fib[1]=1
	for i in range(2,n+1):
		fib[i]=fib[i-1] + fib[i-2]
	return fib[n]

n=100
print('The {}th Fibonnaci number is {}'.format(n,fibdp(n)))



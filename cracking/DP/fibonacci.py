import time 


def fibo_naive(n):
	if n<=2:
		f = 1
	else:
		f = fibo_naive(n-1) + fibo_naive(n-2)
	return f

#start_time = time.time()
#fibo_naive(10)
#print("--- %s seconds ---" % (time.time() - start_time))

def fibo_memo(n):
	memo={}
	if n in memo:
		return memo[n]
	if n<=2:
		f=1
	else:
		f = fibo_memo(n-1) + fibo_memo(n-2)
		memo[n] = f
	return f

#start_time = time.time()
#fibo_memo(40)
#print("--- %s seconds ---" % (time.time() - start_time))


def fibo_opti(n):
	fib={}
	for k in range(n):
		k+=1
		if k<=2:
			f = 1
		else:
			f = fib[k-1] + fib[k-2] 
		fib[k] = f
	return fib[n]

start_time = time.time()
fibo_opti(1000)
print("--- %s seconds ---" % (time.time() - start_time))






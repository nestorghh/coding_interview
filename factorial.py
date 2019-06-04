import time

def factorial(n):
	if n==0:
		return 1
	return n*factorial(n-1)


def factorial_v2(n):
	f=1
	for i in range(2,n+1):
		f=f*i
	return f

def factorial_memo(n):
	memo={}
	
	if n in memo:
		return memo[n]
	if n==0:
		f = 1
	else:
		f = n*factorial_memo(n-1)
		memo[n] = f
	return f
		

def factorial_opti(n):
	memo={}
	
	for k in range(1,n+1):
		if k<=1:
			f=1
		else:
			f = k*memo[k-1]
		memo[k]=f
	
	return memo[n]


start_time = time.time()
print(factorial(20))
print("Recursive solution takes --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(factorial_v2(20))
print("Non-recursive solution takes --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(factorial_memo(20))
print("Memo-based solution takes --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(factorial_opti(20))
print("Memo-based opti solution takes --- %s seconds ---" % (time.time() - start_time))


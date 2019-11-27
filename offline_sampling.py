def offline_sampling(A,k):
	import random
	for i in range(k):
		r = random.randint(i,len(A)-1)
		A[i], A[r] = A[r], A[i]
	return A[:k]

print(offline_sampling([3,7,5,11],3))


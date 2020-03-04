def productExceptSelf(nums):
	if len(nums)==2:
		return nums[::-1]

	import numpy as np

	plist=[]

	for i in range(1,len(nums)-1):
		l=np.array(nums[:i])
		r=np.array(nums[(i+1)::])
		
		plist.append(np.prod(l)*np.prod(r))

	plist.append(np.prod(np.array(nums[:(len(nums)-1)])))

	return [np.prod(np.array(nums[1::]))]+plist



def productExcept(nums):

	def multiply(a):
		p=1
		for e in a:
			p*=e
		return p

	return [multiply(nums[:i])* multiply(nums[i+1:]) for i in range(len(nums))]


# create two lists L (products to the left) and R (products to the right). 
# multiply both lists
def productExcept2(nums):
	n=len(nums)
	answer = [0]*n

	L, R = [0]*n, [0]*n

	L[0]=1
	for i in range(1,n):
		L[i] = nums[i-1] * L[i-1]

	R[n-1]=1
	for i in reversed(range(n-1)):
		R[i] = nums[i+1] * R[i+1]

	for i in range(n):
		answer[i] = L[i] * R[i]

	print(L)
	print(R)

	return answer



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





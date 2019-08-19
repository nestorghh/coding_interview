def k_closest(L,p,K):

	def euclidean_distance(a,b):
		import numpy as np
		from math import sqrt
		a=np.array(a)
		b=np.array(b)
		return sqrt(sum((a-b)**2))
	
	def get_k_closest(L,p0,K):
		dist=[]
		k_closest_p=[]
		for i,p in enumerate(L):
			dist.append((euclidean_distance(p,p0),i))
		
		for k in sorted(dist)[:K]:
			k_closest_p.append(L[k[1]])

		return k_closest_p
			
			
	return get_k_closest(L,p,K)




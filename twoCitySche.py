def twoCitySchedCost(costs):
	n=len(costs)//2
	costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)
	A,B,cost=0,0,0

	for c in costs:
		if A<n and B<n:
			if c[0]<c[1]:
				A+=1
				cost+=c[0]
			else:
				B+=1
				cost+=c[1]
		elif A<n:
			A+=1
			cost+=c[0]
		else:
			B+=1
			cost+=c[1]
	return cost


print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))


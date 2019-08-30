def mergeIntervals(I):
	merged=[]
	I.sort(key = lambda x: x[0])
	
	merged.insert(0,I[0])

	for i in range(1,len(I)):
		top = merged[0]
		
		if top[1]< I[i][0]:
			merged.insert(0,I[i])
		elif top[1] < I[i][1]:
			top[1] = I[i][1]
			merged[0]=top
		print(merged) 
	return merged
	




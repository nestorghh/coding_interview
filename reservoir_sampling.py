def reservoir_sampling(stream,k):
	import random
	reservoir = [None]*k
	n=len(stream)

	for i in range(k):
		reservoir[i] = stream[i]
	
	while i<n:
		j = random.randrange(i+1)

		if (j<k):
			reservoir[j] = stream[i]
		i+=1

	return reservoir	

print(reservoir_sampling([5,7,1,10,65,55,112,101,0,6],6))


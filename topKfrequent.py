def topKFrequent(nums,k):

	# using buckets

	from collections import Counter

	count = Counter(nums)

	maxi = max(v for v in count.values())

	bucketList = [None]*(maxi+1)

	for i in range(maxi+1):
		bucketList[i] = []

	for c in count:
		freq = count[c]
		bucketList[freq] = bucketList[freq] + [c]

	count = 0

	result = []
	
	print(bucketList)
	for i in range(maxi,0,-1):
		currentList = bucketList[i]
		
		for l in currentList:
			if count<k:
				result.append(l)
				count+=1
			else:
				return result
	return result	


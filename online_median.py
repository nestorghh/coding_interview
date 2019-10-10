def online_median(stream):

	import heapq
	max_heap=[]
	min_heap=[]

	max_heap=[-stream[0]]

	r=[stream[0]]

	for s in stream[1:]:

		# check where to send the value
		if -s >= max_heap[0]:
			heapq.heappush(max_heap,-s)
		else:
			heapq.heappush(min_heap,s)

		# balance the heaps
		if abs(len(min_heap)-len(max_heap))>=2:
			mini = len(min_heap)
			maxi = len(max_heap)

			if maxi>mini:
				heapq.heappush(min_heap,-heapq.heappop(max_heap))
			else:
				heapq.heappush(max_heap,-heapq.heappop(min_heap))
		
		# compute the median 
		if len(min_heap)==len(max_heap):

			r.append(0.5*(min_heap[0]+(-max_heap[0])))

		elif len(max_heap)>len(min_heap):
			r.append(-max_heap[0])
		
		else:
			r.append(min_heap[0])

	return r	
		

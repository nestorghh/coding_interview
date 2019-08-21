def minMeetingRooms(intervals):
	import heapq
	free_rooms =[]

	if len(intervals)==0:
		return 0

	#start = [p[0] for p in intervals]
	#end = [p[1] for p in intervals]
	
	# sort the intervals in increasing order of their start time
	intervals.sort(key= lambda x: x[0])
	
	# add the first meeting. we have to give a new room to the first meeting.
	heapq.heappush(free_rooms, intervals[0][1])

	for i in range(1,len(intervals)):
		# if the room due to free up the earlist is free, assign that room to this meeting
		if free_rooms[0]<= intervals[i][0]:
			heapq.heappop(free_rooms)
		
		# If a new room is to be assigned, then also we add to the heap,
		# If an old room is allocated, then also we have to add to the heap with updated 
		# end time.
		heapq.heappush(free_rooms, intervals[i][1])

	return len(free_rooms)
		
#Runtime: 60 ms, faster than 79.56% of Python online submissions for Meeting Rooms II.
#Memory Usage: 15.2 MB, less than 57.14% of Python online submissions for Meeting Rooms II.



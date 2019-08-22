def canAttendMeetings(self, intervals):

	if len(intervals)==0:
		return True
        
	intervals.sort(key= lambda x: x[0])
	count=0

	for i in range(len(intervals)-1):
		if intervals[i][1]<=intervals[i+1][0]:
			count+=1

	return count==len(intervals)-1




